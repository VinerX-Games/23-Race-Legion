"""Drop redundant comparisons to boolean literals.

Safe because the code was converted from statically-typed JASS, where `X == true`
only type-checks when X is boolean.

    X == true   -> X            X == false  -> not (X)
    X ~= true   -> not (X)      X ~= false  -> X
(and mirrored when the literal is on the left)
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng


def src_of(text, node):
    return text[node.first_token.start:node.last_token.stop + 1]


def bool_lit(node):
    if isinstance(node, n.TrueExpr):
        return True
    if isinstance(node, n.FalseExpr):
        return False
    return None


def transform(text, tree):
    cands = []
    for node in a.walk(tree):
        is_eq = isinstance(node, n.EqToOp)
        is_ne = isinstance(node, n.NotEqToOp)
        if not (is_eq or is_ne):
            continue
        lb, rb = bool_lit(node.left), bool_lit(node.right)
        if (lb is None) == (rb is None):
            continue  # need exactly one boolean-literal side
        if rb is not None:
            other, lit = node.left, rb
        else:
            other, lit = node.right, lb
        # equality keeps polarity of lit; inequality flips it
        positive = lit if is_eq else (not lit)
        expr = src_of(text, other)
        new = expr if positive else f"not ({expr})"
        cands.append((node.first_token.start, node.last_token.stop, new))
    # drop any candidate whose span is contained in another candidate's span
    cands.sort(key=lambda c: (c[0], -c[1]))
    kept = []
    for c in cands:
        if kept and c[0] >= kept[-1][0] and c[1] <= kept[-1][1]:
            continue  # nested inside previous
        kept.append(c)
    return kept


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write)
