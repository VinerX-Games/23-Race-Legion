"""Flag '/' (float division) flowing into integer params of natives/BJ functions and table indices."""
import re, sys
from pathlib import Path
from luaparser import ast, astnodes as N
sys.setrecursionlimit(100000)
src, jdir, jmap = sys.argv[1:4]
sigs = {}
for f in list(Path(jdir).glob('*')) + [Path(jmap)]:
    t = f.read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'^\s*(?:constant\s+)?(?:native|function)\s+(\w+)\s+takes\s+(.*?)\s+returns', t, re.M):
        if m.group(2).strip() == 'nothing':
            sigs[m.group(1)] = []
        else:
            sigs[m.group(1)] = [p.split()[0] for p in m.group(2).split(',')]
tree = ast.parse(Path(src).read_text(encoding='utf-8-sig'))

TAINT = set()
def has_div(e):
    """True if expression contains '/' not neutralised by an int conversion call."""
    if isinstance(e, N.FloatDivOp):
        return True
    if isinstance(e, N.Name) and e.id in TAINT:
        return True
    if isinstance(e, (N.Call, N.Invoke)):
        return False          # R2I(...), math.floor(...), any call result is opaque
    if isinstance(e, N.Node):
        for k, v in vars(e).items():
            if k.startswith('_') or k in ('comments',):
                continue
            for x in (v if isinstance(v, list) else [v]):
                if isinstance(x, N.Node) and has_div(x):
                    return True
    return False

def line(n):
    t = getattr(n, '_first_token', None); return getattr(t, 'line', '?')

hits = []
def walk(n):
    if isinstance(n, list):
        for x in n:
            walk(x)
        return
    if not isinstance(n, N.Node): return
    if isinstance(n, (N.Assign, N.LocalAssign)):
        for t, v in zip(n.targets, n.values):
            if isinstance(t, N.Name):
                if has_div(v):
                    TAINT.add(t.id)
    if isinstance(n, (N.Function, N.LocalFunction, N.AnonymousFunction, N.Method)):
        saved = set(TAINT); TAINT.clear()
        for k, v in vars(n).items():
            if not k.startswith('_') and k != 'comments':
                walk(v)
        TAINT.clear(); TAINT.update(saved)
        return
    if isinstance(n, N.Call) and isinstance(n.func, N.Name) and n.func.id in sigs:
        types = sigs[n.func.id]
        for i, a in enumerate(n.args):
            if i < len(types) and types[i] == 'integer' and has_div(a):
                hits.append((line(n), n.func.id, i + 1))
    if isinstance(n, N.Index) and n.notation == N.IndexNotation.SQUARE and has_div(n.idx):
        hits.append((line(n), '<index>', 0))
    for k, v in vars(n).items():
        if not k.startswith('_') and k != 'comments':
            walk(v)
walk(tree)
for h in hits: print(*h)
print('total', len(hits))
