"""Ищет чтение имени после закрытия блока, где оно было объявлено `local`,
если в текущей области видимости такого локала нет (артефакт vJASS->Lua:
`local x` внутри if/while, а использование — после блока; тогда читается
глобал x, обычно nil или чужое значение).

Запуск: python -I scripts/audit/scope_leak_audit.py map.w3x/war3map.lua
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from closure_nil_audit import tokens  # noqa: E402

NAME = re.compile(r'[A-Za-z_]\w*$')
KEYWORDS = {'and', 'break', 'do', 'else', 'elseif', 'end', 'false', 'for', 'function', 'goto', 'if', 'in',
            'local', 'nil', 'not', 'or', 'repeat', 'return', 'then', 'true', 'until', 'while'}


def main(path):
    src = open(path, encoding='utf-8').read()
    toks = list(tokens(src))
    lines = src.split('\n')
    # scope: dict(kind, names:set, closed:set (имена из закрытых дочерних блоков), is_func)
    scopes = [{'kind': 'chunk', 'names': set(), 'closed': {}, 'func': True}]
    pending_for = None  # имена переменных for, объявляемых в следующем 'do'
    pending_params = None
    found = 0
    seen = set()
    n = len(toks)
    i = 0
    braces = 0
    while i < n:
        t, ln, _ = toks[i]
        if t == '{':
            braces += 1
        elif t == '}':
            braces -= 1
        prev = toks[i - 1][0] if i else ''
        nxt = toks[i + 1][0] if i + 1 < n else ''
        if t == 'function':
            # имя функции (глобальной) пропускаем; параметры
            j = i + 1
            while j < n and toks[j][0] != '(':
                j += 1
            params = set()
            j += 1
            while j < n and toks[j][0] != ')':
                if NAME.match(toks[j][0]):
                    params.add(toks[j][0])
                j += 1
            if prev == 'local' and NAME.match(nxt):
                scopes[-1]['names'].add(nxt)
            scopes.append({'kind': 'function', 'names': params, 'closed': {}, 'func': True})
            i = j + 1
            continue
        if t in ('if', 'repeat'):
            scopes.append({'kind': t, 'names': set(), 'closed': {}, 'func': False})
        elif t in ('then', 'else') and scopes[-1]['kind'] in ('if', 'then', 'else'):
            # новая ветка — новый блок
            if t == 'else' or scopes[-1]['kind'] != 'if':
                closing = scopes.pop()
                _close(scopes, closing)
                scopes.append({'kind': t, 'names': set(), 'closed': {}, 'func': False})
            else:
                scopes[-1]['kind'] = 'then'
        elif t == 'elseif':
            closing = scopes.pop()
            _close(scopes, closing)
            scopes.append({'kind': 'if', 'names': set(), 'closed': {}, 'func': False})
        elif t == 'for':
            j = i + 1
            names = set()
            while j < n and toks[j][0] not in ('=', 'in'):
                if NAME.match(toks[j][0]):
                    names.add(toks[j][0])
                j += 1
            pending_for = names
            i = j
            continue
        elif t == 'do':
            scopes.append({'kind': 'do', 'names': pending_for or set(), 'closed': {}, 'func': False})
            pending_for = None
        elif t in ('end', 'until'):
            if len(scopes) > 1:
                closing = scopes.pop()
                _close(scopes, closing)
        elif t == 'local' and nxt != 'function':
            j = i + 1
            names = []
            while j < n and NAME.match(toks[j][0]) and toks[j][0] not in KEYWORDS:
                names.append(toks[j][0])
                if j + 1 < n and toks[j + 1][0] == ',':
                    j += 2
                else:
                    break
            # имена видимы после выражения; упрощённо — сразу
            scopes[-1]['names'].update(names)
            i = j + 1
            continue
        elif NAME.match(t) and t not in KEYWORDS and prev not in ('.', ':', '::', 'goto') and nxt != '::':
            # поле таблицы {x = ...}
            if braces > 0 and prev in ('{', ',', ';') and nxt == '=' and toks[i + 2][0] != '=':
                i += 1
                continue
            if not visible(scopes, t):
                fn_closed = closed_in_func(scopes, t)
                if fn_closed is not None and (ln, t) not in seen:
                    seen.add((ln, t))
                    found += 1
                    print(f"{ln}: '{t}' объявлен local в закрытом блоке (стр. {fn_closed}) :: {lines[ln-1].strip()[:90]}")
        i += 1
    print('total', found)


def _close(scopes, closing):
    parent = scopes[-1]
    if closing['func']:
        return
    for name in closing['names']:
        parent['closed'].setdefault(name, 0)
    for name, l in closing['closed'].items():
        parent['closed'].setdefault(name, l)


def visible(scopes, name):
    return any(name in s['names'] for s in scopes)


def closed_in_func(scopes, name):
    for s in reversed(scopes):
        if name in s['closed']:
            return s['closed'][name]
        if s['func']:
            return None
    return None


if __name__ == '__main__':
    main(sys.argv[1])
