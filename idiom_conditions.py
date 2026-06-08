"""Collapse converted condition functions to a single return.

    if ( not ( E1 ) ) then return false end
    ...
    return true            -->   return (E1) and (E2) ...
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng


def src_of(text, node):
    return text[node.first_token.start:node.last_token.stop + 1]


def is_return_false(s):
    return isinstance(s, n.Return) and len(s.values) == 1 and isinstance(s.values[0], n.FalseExpr)


def is_return_true(s):
    return isinstance(s, n.Return) and len(s.values) == 1 and isinstance(s.values[0], n.TrueExpr)


def guard_expr(stmt):
    if not isinstance(stmt, n.If):
        return None
    if type(stmt.test).__name__ != "ULNotOp" or not hasattr(stmt.test, "operand"):
        return None
    body = stmt.body.body if isinstance(stmt.body, n.Block) else stmt.body
    if len(body) != 1 or not is_return_false(body[0]):
        return None
    if getattr(stmt, "orelse", None):
        return None
    return stmt.test.operand


def match_condition_fn(fn):
    block = fn.body
    stmts = block.body if isinstance(block, n.Block) else block
    if len(stmts) < 2 or not is_return_true(stmts[-1]):
        return None
    exprs = []
    for g in stmts[:-1]:
        e = guard_expr(g)
        if e is None:
            return None
        exprs.append(e)
    return (exprs, stmts[0], stmts[-1]) if exprs else None


def transform(text, tree):
    repls = []
    for node in a.walk(tree):
        if not isinstance(node, n.Function):
            continue
        m = match_condition_fn(node)
        if not m:
            continue
        exprs, first_stmt, last_stmt = m
        if len(exprs) == 1:
            new_body = f"return {src_of(text, exprs[0])}"
        else:
            new_body = "return " + " and ".join(f"({src_of(text, e)})" for e in exprs)
        repls.append((first_stmt.first_token.start, last_stmt.last_token.stop, new_body))
    return repls


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write)
