"""Remove empty else branches: `if X then ... else end` -> `if X then ... end`.

Detected precisely via AST (orelse is an empty Block). The region between the
then-body and the closing `end` must be exactly the `else` keyword surrounded by
whitespace, which we replace with just the whitespace that followed `else`.
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng


def transform(text, tree):
    repls = []
    for node in a.walk(tree):
        if not isinstance(node, n.If):
            continue
        orelse = getattr(node, "orelse", None)
        # empty else == Block with no statements (None means no else at all)
        if not isinstance(orelse, n.Block):
            continue
        if orelse.body:
            continue
        then_block = node.body
        if not (isinstance(then_block, n.Block) and then_block.body):
            continue
        region_start = then_block.body[-1].last_token.stop + 1
        region_end = node.last_token.start  # start of closing `end`
        region = text[region_start:region_end]
        if region.strip() != "else":
            continue
        keep = region[region.index("else") + 4:]
        if keep == "":
            keep = " "
        repls.append((region_start, region_end - 1, keep))
    return repls


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write)
