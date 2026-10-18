"""Ищет локальные переменные, захваченные замыканием (function() ... end), которые
внешняя функция обнуляет (`x = nil`) ПОСЛЕ создания замыкания.

В Lua upvalue общий с внешней функцией: артефакт JASS `set x = null` в конце
функции обнуляет переменную и для отложенного колбэка (таймер, ForGroup и т.п.).

Запуск: python -I scripts/audit/closure_nil_audit.py map.w3x/war3map.lua
"""
import re
import sys

TOKEN = re.compile(r'--\[(=*)\[.*?\]\1\]|--[^\n]*|\[(=*)\[.*?\]\2\]|"(?:\.|[^"\\n])*"|\'(?:\.|[^\'\\n])*\'|[A-Za-z_]\w*|\n|.', re.S)
OPEN = {'function', 'if', 'do', 'repeat'}
CLOSE = {'end', 'until'}


# Share the string/comment-aware lexer used by the source index.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wc3_project import lua_tokens as tokens


def main(path):
    src = open(path, encoding='utf-8').read()
    toks = list(tokens(src))
    lines = src.split('\n')
    # стек функций: dict(start, locals, closures=[(start_idx, end_idx, names)])
    stack = []  # (kind, info)
    funcs = []
    i = 0
    n = len(toks)
    while i < n:
        t, ln, _ = toks[i]
        if t == 'function':
            anon = i + 1 < n and toks[i + 1][0] == '('
            stack.append(('function', {'anon': anon, 'start': i, 'line': ln}))
        elif t in OPEN:
            stack.append((t, None))
        elif t in CLOSE:
            if stack:
                kind, info = stack.pop()
                if kind == 'function':
                    info['end'] = i
                    funcs.append(info)
        i += 1
    # для каждой функции: локалы, объявленные непосредственно в ней (грубо: 'local NAME' в её диапазоне
    # вне вложенных функций), и параметры
    funcs.sort(key=lambda f: f['start'])
    found = 0
    for f in funcs:
        s, e = f['start'], f['end']
        nested = [g for g in funcs if s < g['start'] and g['end'] < e]
        top_nested = [g for g in nested if not any(h is not g and h['start'] < g['start'] and g['end'] < h['end'] for h in nested)]

        def inside_nested(k):
            return any(g['start'] <= k <= g['end'] for g in top_nested)
        locs = set()
        # параметры
        k = s + 1
        while k < e and toks[k][0] != '(':
            k += 1
        k += 1
        while k < e and toks[k][0] != ')':
            if re.match(r'[A-Za-z_]\w*$', toks[k][0]):
                locs.add(toks[k][0])
            k += 1
        for k in range(s, e):
            if toks[k][0] == 'local' and not inside_nested(k):
                j = k + 1
                if toks[j][0] == 'function':
                    continue
                while j < e and re.match(r'[A-Za-z_]\w*$', toks[j][0]):
                    locs.add(toks[j][0])
                    if toks[j + 1][0] == ',':
                        j += 2
                    else:
                        break
        if not locs:
            continue
        for g in top_nested:
            if not g['anon']:
                continue
            used = {toks[k][0] for k in range(g['start'], g['end']) if toks[k][0] in locs}
            if not used:
                continue
            for k in range(g['end'] + 1, e - 1):
                if inside_nested(k):
                    continue
                name = toks[k][0]
                if name in used and toks[k + 1][0] == '=' and toks[k + 2][0] == 'nil' and (k == 0 or toks[k - 1][0] not in ('.', 'local', ',')):
                    found += 1
                    print(f"{toks[k][1]}: '{name}' = nil после замыкания (стр. {g['line']}) :: {lines[toks[k][1]-1].strip()[:80]}")
    print('total', found)


if __name__ == '__main__':
    main(sys.argv[1])
