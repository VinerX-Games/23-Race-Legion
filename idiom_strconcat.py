"""Fix string concatenation written with `+` (JASS->Lua conversion artifact).

In Lua `+` is arithmetic; concatenation is `..`. The converter left string
concatenations as `+`, which crash at runtime (arithmetic on a string).

A `+`-chain is string concatenation if any operand is a string literal or a
call to a known string-returning function. We replace only the `+` operator
tokens of such chains with `..`, preserving everything else.
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng

# Functions that return strings (WC3 BJ/native + map helpers seen in tree).
STRING_FUNCS = {
    "GetPlayerName", "GetUnitName", "GetObjectName", "GetHeroProperName",
    "I2S", "R2S", "R2SW", "GetEventPlayerChatString", "name", "SubString",
    "GetLocalizedString", "GetAbilityName", "TimeToString",
}


def is_string_call(node):
    if not isinstance(node, n.Call):
        return False
    f = node.func
    if isinstance(f, n.Name):
        return f.id in STRING_FUNCS
    if isinstance(f, n.Index) and isinstance(f.idx, n.Name):
        return f.idx.id in STRING_FUNCS
    return False


def stringy(node):
    """True if this expression is (part of) a string concatenation."""
    if isinstance(node, n.String):
        return True
    if isinstance(node, n.Concat):
        return True
    if is_string_call(node):
        return True
    if isinstance(node, n.AddOp):
        return stringy(node.left) or stringy(node.right)
    return False


def collect_plus_tokens(text, node, out):
    """For a stringy AddOp tree, record every `+` operator offset."""
    if not isinstance(node, n.AddOp):
        return
    collect_plus_tokens(text, node.left, out)
    # the '+' sits between left.stop and right.start
    lo = node.left.last_token.stop + 1
    hi = node.right.first_token.start
    gap = text[lo:hi]
    idx = gap.index("+")
    out.append(lo + idx)
    collect_plus_tokens(text, node.right, out)


def transform(text, tree):
    repls = []
    seen = set()
    for node in a.walk(tree):
        if not isinstance(node, n.AddOp):
            continue
        if id(node) in seen:
            continue
        if not stringy(node):
            continue
        # mark whole chain as seen so we don't reprocess sub-AddOps
        stack = [node]
        while stack:
            cur = stack.pop()
            if isinstance(cur, n.AddOp):
                seen.add(id(cur))
                stack.extend([cur.left, cur.right])
        offs = []
        collect_plus_tokens(text, node, offs)
        for off in offs:
            repls.append((off, off, ".."))
    return repls


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write)
