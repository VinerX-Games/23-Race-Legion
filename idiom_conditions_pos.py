"""Positive-form condition collapse:

    if ( E1 ) then return true end
    ...
    return false              -->   return (E1) or (E2) ...
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng
from idiom_conditions import src_of, is_return_true, is_return_false


def pos_guard_expr(stmt):
    if not isinstance(stmt, n.If):
        return None
    if getattr(stmt, "orelse", None):
        return None
    body = stmt.body.body if isinstance(stmt.body, n.Block) else stmt.body
    if len(body) != 1 or not is_return_true(body[0]):
        return None
    return stmt.test


def match_pos_fn(fn):
    block = fn.body
    stmts = block.body if isinstance(block, n.Block) else block
    if len(stmts) < 2 or not is_return_false(stmts[-1]):
        return None
    exprs = []
    for g in stmts[:-1]:
        e = pos_guard_expr(g)
        if e is None:
            return None
        exprs.append(e)
    return (exprs, stmts[0], stmts[-1]) if exprs else None


def transform(text, tree):
    repls = []
    for node in a.walk(tree):
        if not isinstance(node, n.Function):
            continue
        m = match_pos_fn(node)
        if not m:
            continue
        exprs, first_stmt, last_stmt = m
        if len(exprs) == 1:
            new_body = f"return {src_of(text, exprs[0])}"
        else:
            new_body = "return " + " or ".join(f"({src_of(text, e)})" for e in exprs)
        repls.append((first_stmt.first_token.start, last_stmt.last_token.stop, new_body))
    return repls


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write)
