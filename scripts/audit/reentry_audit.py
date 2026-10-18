"""Detect group re-entrancy: ForGroup/GroupEnum over global group G whose callback
(transitively) re-enumerates, clears, or destroys the same G.
Usage: python reentry_audit.py war3map.lua
"""
import sys
from collections import defaultdict
from pathlib import Path
from luaparser import ast, astnodes as N

sys.setrecursionlimit(100000)
ENUMS = {"GroupEnumUnitsInRange", "GroupEnumUnitsInRect", "GroupEnumUnitsOfPlayer",
         "GroupEnumUnitsInRangeOfLoc", "GroupEnumUnitsOfType", "GroupEnumUnitsSelected",
         "GroupEnumUnitsInRangeCounted", "GroupEnumUnitsInRectCounted", "GroupEnumUnitsOfTypeCounted"}
MUTATE = ENUMS | {"GroupClear", "DestroyGroup", "ForGroup"}


def line(n):
    t = getattr(n, "_first_token", None)
    return getattr(t, "line", "?")


def cb_name(e):
    """Function name referenced by a callback expression: f, Condition(f), Filter(f)."""
    if isinstance(e, N.Name):
        return e.id
    if isinstance(e, N.Call) and isinstance(e.func, N.Name) and e.func.id in ("Condition", "Filter") and e.args:
        return cb_name(e.args[0])
    return None


funcs = {}                       # name -> body node
mut = defaultdict(set)           # name -> globals mutated directly
calls = defaultdict(set)         # name -> functions called / referenced
sites = []                       # (func, line, group, callback, kind)
anon = [0]


def scan(body, owner):
    def walk(n):
        if isinstance(n, list):
            for x in n:
                walk(x)
            return
        if not isinstance(n, N.Node):
            return
        if isinstance(n, (N.Function, N.LocalFunction)) and isinstance(n.name, N.Name):
            funcs[n.name.id] = n.body
            scan(n.body, n.name.id)
            calls[owner].add(n.name.id) if isinstance(n, N.LocalFunction) else None
            return
        if isinstance(n, N.AnonymousFunction):
            anon[0] += 1
            name = f"<anon#{anon[0]}@{line(n)}>"
            funcs[name] = n.body
            calls[owner].add(name)
            scan(n.body, name)
            return
        if isinstance(n, N.Call) and isinstance(n.func, N.Name):
            fn = n.func.id
            calls[owner].add(fn)
            if fn in MUTATE and n.args and isinstance(n.args[0], N.Name):
                g = n.args[0].id
                mut[owner].add(g)
                cb = None
                if fn == "ForGroup" and len(n.args) > 1:
                    cb = n.args[1]
                elif fn in ENUMS and len(n.args) > 1:
                    cb = n.args[-1]
                if cb is not None:
                    name = cb_name(cb)
                    if isinstance(cb, N.AnonymousFunction):
                        anon[0] += 1
                        name = f"<anon#{anon[0]}@{line(cb)}>"
                        funcs[name] = cb.body
                        scan(cb.body, name)
                        sites.append((owner, line(n), g, name, fn))
                        for a in n.args[:-1]:
                            walk(a)
                        return
                    if name:
                        sites.append((owner, line(n), g, name, fn))
            for a in n.args:
                if isinstance(a, N.Name):
                    calls[owner].add(a.id)      # function refs passed as values
        for k, v in vars(n).items():
            if not k.startswith("_") and k != "comments":
                walk(v)
    walk(body)


tree = ast.parse(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
scan(tree.body, "<chunk>")


def reaches(start, g, depth=6):
    seen, frontier, path = set(), [(start, [start])], None
    while frontier:
        nxt = []
        for f, p in frontier:
            if f in seen:
                continue
            seen.add(f)
            if g in mut.get(f, ()):
                return p
            if len(p) <= depth:
                for c in calls.get(f, ()):
                    if c in funcs:
                        nxt.append((c, p + [c]))
        frontier = nxt
    return None


out = []
for owner, ln, g, cb, kind in sites:
    if cb not in funcs:
        continue
    p = reaches(cb, g)
    if p:
        out.append((ln, owner, kind, g, " -> ".join(p)))
for o in sorted(out, key=lambda x: int(x[0]) if str(x[0]).isdigit() else 0):
    print(*o, sep=" | ")
print("total", len(out))
