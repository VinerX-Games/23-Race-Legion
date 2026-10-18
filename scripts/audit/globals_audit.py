"""Scope-aware global usage audit for war3map.lua.

Usage: python globals_audit.py <war3map.lua> <jass_dir> <out.json>
Collects every global read / write / call (with line numbers), lists
reads of names that are never defined anywhere (not in the map, not a
WC3 native/BJ, not Lua stdlib), and functions defined more than once.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from luaparser import ast, astnodes as N

sys.setrecursionlimit(100000)


def line_of(node):
    tok = getattr(node, "_first_token", None)
    return getattr(tok, "line", None) if tok is not None else None


class Audit:
    def __init__(self):
        self.reads = defaultdict(list)    # name -> lines
        self.writes = defaultdict(list)
        self.funcdefs = defaultdict(list)  # global function definitions
        self.arity = {}                    # name -> (nparams, vararg, line)
        self.calls = defaultdict(list)     # name -> [(nargs, line, last_is_multi)]
        self.scopes = [set()]
        self.cur_line = 0

    # ---- scope helpers ----
    def push(self, names=()):
        self.scopes.append(set(names))

    def pop(self):
        self.scopes.pop()

    def declare(self, name):
        self.scopes[-1].add(name)

    def is_local(self, name):
        return any(name in s for s in reversed(self.scopes[1:]))

    def ln(self, node):
        l = line_of(node)
        if l:
            self.cur_line = l
        return self.cur_line

    # ---- generic walk ----
    def walk(self, node):
        if node is None:
            return
        if isinstance(node, list):
            for n in node:
                self.walk(n)
            return
        if not isinstance(node, N.Node):
            return
        self.ln(node)
        m = getattr(self, "v_" + type(node).__name__, None)
        if m:
            m(node)
        else:
            self.children(node)

    def children(self, node):
        for k, v in vars(node).items():
            if k.startswith("_") or k in ("comments", "wrapped"):
                continue
            if isinstance(v, (N.Node, list)):
                self.walk(v)

    # ---- names ----
    def v_Name(self, node):
        if not self.is_local(node.id):
            self.reads[node.id].append(self.ln(node))

    def write_target(self, t):
        if isinstance(t, N.Name):
            if not self.is_local(t.id):
                self.writes[t.id].append(self.ln(t))
        else:
            self.walk(t)

    def v_Index(self, node):
        self.walk(node.value)
        if node.notation == N.IndexNotation.SQUARE:
            self.walk(node.idx)

    def v_Field(self, node):
        if node.between_brackets:
            self.walk(node.key)
        self.walk(node.value)

    def v_Invoke(self, node):
        self.walk(node.source)
        self.walk(node.args)

    def v_Call(self, node):
        if isinstance(node.func, N.Name) and not self.is_local(node.func.id):
            last = node.args[-1] if node.args else None
            multi = isinstance(last, (N.Call, N.Invoke, N.Varargs))
            self.calls[node.func.id].append((len(node.args), self.ln(node), multi))
        self.walk(node.func)
        self.walk(node.args)

    # ---- statements ----
    def v_Chunk(self, node):
        self.walk(node.body)

    def v_Block(self, node):
        self.push()
        self.walk(node.body)
        self.pop()

    def v_LocalAssign(self, node):
        self.walk(node.values)
        for t in node.targets:
            self.declare(t.id)

    def v_Assign(self, node):
        self.walk(node.values)
        for t in node.targets:
            self.write_target(t)

    def body_with(self, args, body, extra=()):
        self.push([a.id for a in args if isinstance(a, N.Name)] + list(extra))
        self.walk(body.body if isinstance(body, N.Block) else body)
        self.pop()

    def v_Function(self, node):
        name = node.name
        if isinstance(name, N.Name):
            if self.is_local(name.id):
                pass
            else:
                self.writes[name.id].append(self.ln(node))
                self.funcdefs[name.id].append(self.ln(node))
                va = any(isinstance(x, N.Varargs) for x in node.args)
                self.arity[name.id] = (sum(isinstance(x, N.Name) for x in node.args), va, self.ln(node))
        else:
            self.walk(name)
        self.body_with(node.args, node.body)

    def v_LocalFunction(self, node):
        self.declare(node.name.id)
        self.body_with(node.args, node.body)

    def v_Method(self, node):
        self.walk(node.source)
        self.body_with(node.args, node.body, extra=["self"])

    def v_AnonymousFunction(self, node):
        self.body_with(node.args, node.body)

    def v_Fornum(self, node):
        self.walk(node.start)
        self.walk(node.stop)
        self.walk(node.step)
        self.body_with([node.target], node.body)

    def v_Forin(self, node):
        self.walk(node.iter)
        self.body_with(node.targets, node.body)

    def v_Repeat(self, node):
        self.push()
        self.walk(node.body.body if isinstance(node.body, N.Block) else node.body)
        self.walk(node.test)
        self.pop()


def jass_names(jass_dir):
    names = set()
    for f in Path(jass_dir).glob("*"):
        txt = f.read_text(encoding="utf-8", errors="replace")
        names.update(re.findall(r"^\s*(?:constant\s+)?native\s+(\w+)", txt, re.M))
        names.update(re.findall(r"^\s*function\s+(\w+)", txt, re.M))
        # globals: "<type> [array] name [= ...]" inside globals blocks
        for block in re.findall(r"^globals(.*?)^endglobals", txt, re.M | re.S):
            for m in re.finditer(r"^\s*(?:constant\s+)?\w+\s+(?:array\s+)?(\w+)", block, re.M):
                names.add(m.group(1))
    return names


LUA_STD = set("""_G _VERSION _ENV assert collectgarbage coroutine debug dofile error getmetatable
ipairs load loadfile math next os pairs pcall print rawequal rawget rawlen rawset require
select setmetatable string table tonumber tostring type utf8 xpcall io package""".split())


def arity_report(a):
    out = {}
    for name, (np, va, line) in a.arity.items():
        if va:
            continue
        over = [(n, l) for n, l, multi in a.calls.get(name, []) if n > np]
        if over:
            out[name] = {"params": np, "def_line": line, "calls_with_more_args": over[:8], "n": len(over)}
    return dict(sorted(out.items()))


def main():
    src, jass_dir, out = sys.argv[1:4]
    text = Path(src).read_text(encoding="utf-8-sig")
    tree = ast.parse(text)
    a = Audit()
    a.walk(tree)
    known = jass_names(jass_dir) | LUA_STD | set(a.writes)
    undefined = {k: v for k, v in a.reads.items() if k not in known}
    dup = {k: v for k, v in a.funcdefs.items() if len(v) > 1}
    unused_writes = {k: v for k, v in a.writes.items() if k not in a.reads}
    res = {
        "undefined_reads": dict(sorted(undefined.items())),
        "duplicate_function_defs": dict(sorted(dup.items())),
        "written_never_read": dict(sorted(unused_writes.items())),
        "arity_mismatch": arity_report(a),
        "stats": {"globals_written": len(a.writes), "globals_read": len(a.reads)},
    }
    Path(out).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res["stats"]))
    print("arity mismatches:", len(res["arity_mismatch"]))
    print("undefined:", len(undefined), "dups:", len(dup), "unused writes:", len(unused_writes))


if __name__ == "__main__":
    main()
