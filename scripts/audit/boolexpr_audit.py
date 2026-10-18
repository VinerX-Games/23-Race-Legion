"""Find boolexpr/filterfunc/conditionfunc params receiving a raw Lua function."""
import re, sys
from pathlib import Path
from luaparser import ast, astnodes as N
sys.setrecursionlimit(100000)
src, jdir, jmap = sys.argv[1:4]
sigs = {}
for f in list(Path(jdir).glob('*')) + [Path(jmap)]:
    t = f.read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'^\s*(?:constant\s+)?(?:native|function)\s+(\w+)\s+takes\s+(.*?)\s+returns', t, re.M):
        a = m.group(2).strip()
        sigs[m.group(1)] = [] if a == 'nothing' else [p.split()[0] for p in a.split(',')]
tree = ast.parse(Path(src).read_text(encoding='utf-8-sig'))
funcs = set()
def collect(n):
    if isinstance(n, list):
        for x in n: collect(x)
        return
    if not isinstance(n, N.Node): return
    if isinstance(n, N.Function) and isinstance(n.name, N.Name): funcs.add(n.name.id)
    for k, v in vars(n).items():
        if not k.startswith('_') and k != 'comments': collect(v)
collect(tree)
BX = {'boolexpr', 'filterfunc', 'conditionfunc'}
hits = []
def walk(n):
    if isinstance(n, list):
        for x in n: walk(x)
        return
    if not isinstance(n, N.Node): return
    if isinstance(n, N.Call) and isinstance(n.func, N.Name) and n.func.id in sigs:
        for i, a in enumerate(n.args):
            ts = sigs[n.func.id]
            if i < len(ts) and ts[i] in BX:
                raw = isinstance(a, N.AnonymousFunction) or (isinstance(a, N.Name) and a.id in funcs)
                if raw:
                    hits.append((getattr(n._first_token, 'line', '?'), n.func.id, getattr(a, 'id', '<anon>')))
    for k, v in vars(n).items():
        if not k.startswith('_') and k != 'comments': walk(v)
walk(tree)
for h in hits: print(*h)
print('total', len(hits))
