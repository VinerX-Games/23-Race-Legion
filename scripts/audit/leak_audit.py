"""Per-function handle create/destroy balance (heuristic)."""
import sys
from collections import Counter
from pathlib import Path
from luaparser import ast, astnodes as N
sys.setrecursionlimit(100000)
LOC_NEW = {"Location", "GetUnitLoc", "GetSpellTargetLoc", "GetRectCenter", "PolarProjectionBJ",
           "OffsetLocation", "GetUnitRallyPoint", "GetOrderPointLoc", "GetRandomLocInRect", "CameraSetupGetDestPositionLoc"}
GRP_NEW = {"CreateGroup", "GetUnitsInRangeOfLocAll", "GetUnitsInRangeOfLocMatching", "GetUnitsInRectAll",
           "GetUnitsInRectMatching", "GetUnitsOfPlayerAll", "GetUnitsOfPlayerMatching", "GetUnitsOfTypeIdAll",
           "GetUnitsOfPlayerAndTypeId", "GetUnitsSelectedAll"}
FX_NEW = {"AddSpecialEffect", "AddSpecialEffectTarget", "AddSpecialEffectLoc", "AddSpecialEffectTargetUnitBJ", "AddSpecialEffectLocBJ"}
tree = ast.parse(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
res = []
def count(body):
    c = Counter()
    def w(n):
        if isinstance(n, list):
            for x in n: w(x)
            return
        if not isinstance(n, N.Node): return
        if isinstance(n, (N.Function, N.LocalFunction)): return   # nested named fn counted separately
        if isinstance(n, N.Call) and isinstance(n.func, N.Name):
            f = n.func.id
            if f in LOC_NEW: c['loc+'] += 1
            if f == 'RemoveLocation': c['loc-'] += 1
            if f in GRP_NEW: c['grp+'] += 1
            if f in ('DestroyGroup',): c['grp-'] += 1
            if f in FX_NEW: c['fx+'] += 1
            if f in ('DestroyEffect', 'DestroyEffectBJ', 'RemoveEffectTimed', 'DestroyEffectTimed'): c['fx-'] += 1
            if f == 'CreateTimer': c['tmr+'] += 1
            if f in ('DestroyTimer', 'ReleaseTimer'): c['tmr-'] += 1
            if f == 'bj_wantDestroyGroup': pass
        if isinstance(n, N.Assign):
            for t in n.targets:
                if isinstance(t, N.Name) and t.id == 'bj_wantDestroyGroup': c['grp-'] += 1
        for k, v in vars(n).items():
            if not k.startswith('_') and k != 'comments': w(v)
    w(body)
    return c
def find(n):
    if isinstance(n, list):
        for x in n: find(x)
        return
    if not isinstance(n, N.Node): return
    if isinstance(n, N.Function) and isinstance(n.name, N.Name):
        c = count(n.body.body)
        issues = []
        for k in ('loc', 'grp', 'fx', 'tmr'):
            if c[k+'+'] > c[k+'-']:
                issues.append(f"{k} +{c[k+'+']}/-{c[k+'-']}")
        if issues:
            res.append((getattr(n._first_token, 'line', 0), n.name.id, ', '.join(issues)))
    for k, v in vars(n).items():
        if not k.startswith('_') and k != 'comments': find(v)
find(tree)
for r in res: print(*r, sep=' | ')
kinds = Counter(i.split()[0] for r in res for i in r[2].split(', '))
print('functions', len(res), dict(kinds))
