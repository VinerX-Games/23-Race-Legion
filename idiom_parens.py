"""Strip redundant wrapping parens in positions where parens are never needed:

    return ( X )      -> return X
    if ( X ) then     -> if X then        (covers elseif: each is an If node)
    while ( X ) do    -> while X do
    until ( X )       -> until X

Only the outer pair is removed and only when it wraps the ENTIRE expression
(verified by paren-matching that skips Lua strings). Run repeatedly to peel
nested layers. A whole-tree AST fingerprint guard rejects any change that would
alter structure, so this is safe by construction.
"""
from __future__ import annotations

import argparse

import luaparser.ast as a
from luaparser import astnodes as n

import idiom_engine as eng


def wholly_wrapped(s):
    """True if s starts with '(' whose match is the final char."""
    if len(s) < 2 or s[0] != "(" or s[-1] != ")":
        return False
    depth = 0
    i = 0
    quote = None
    while i < len(s):
        c = s[i]
        if quote:
            if c == "\\" and quote in ('"', "'"):
                i += 2
                continue
            if (quote in ('"', "'") and c == quote):
                quote = None
        else:
            if c in ('"', "'"):
                quote = c
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return i == len(s) - 1
        i += 1
    return False


def collect(text, node):
    s, e = node.first_token.start, node.last_token.stop
    src = text[s:e + 1]
    if wholly_wrapped(src):
        # remove first '(' and last ')' plus the padding they introduced
        return (s, e, src[1:-1].strip())
    return None


def transform(text, tree):
    repls = []
    for node in a.walk(tree):
        if isinstance(node, n.Return):
            # parens around a bare call/vararg in return adjust arity -> keep them
            if len(node.values) == 1 and not isinstance(node.values[0], (n.Call, n.Invoke, n.Dots)):
                r = collect(text, node.values[0])
                if r:
                    repls.append(r)
        elif isinstance(node, (n.If, n.While)):
            r = collect(text, node.test)
            if r:
                repls.append(r)
        elif isinstance(node, n.Repeat):
            r = collect(text, node.test)
            if r:
                repls.append(r)
    return repls


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    eng.run(transform, write=args.write, guard=True)
