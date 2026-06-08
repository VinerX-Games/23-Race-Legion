"""Re-cut the 80_runtime/* section files along whole-function boundaries.

The auto-split cut files by line ranges, so files begin/end mid-function and are
not independently parseable. This snaps every file boundary to a top-level
function edge: each function lands wholly in the file where it currently begins,
together with its leading `--=== Trigger ===` comment block.

Invariant: the concatenation of all runtime files is byte-identical before and
after (only the internal split points move), so the built war3map.lua is
unchanged. Verified before writing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import luaparser.ast as a
from luaparser import astnodes as n

SP = Path(__file__).resolve().parent / "map.w3x" / "_lua" / "monolith_split"
SE = SP / "sections"


def load():
    man = json.loads((SP / "manifest.json").read_text(encoding="utf-8-sig"))
    rt = [s["file"] for s in man["sections"] if s["category"] == "generated_runtime"]
    segs = []
    pos = 0
    parts = []
    for f in rt:
        txt = (SE / f).read_text(encoding="utf-8-sig")
        parts.append(txt)
        segs.append((pos, pos + len(txt), f))
        pos += len(txt)
    return "".join(parts), segs


def file_at(segs, off):
    for s, e, f in segs:
        if s <= off < e:
            return f
    return segs[-1][2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    concat, segs = load()
    tree = a.parse(concat)
    funcs = [x for x in tree.body.body if isinstance(x, n.Function)]
    print(f"top-level functions: {len(funcs)}")

    # chunk_i spans from end of previous function to end of this function,
    # so it carries the leading comment block of function i.
    chunks = []  # (home_file, text)
    prev_end = 0
    for fn in funcs:
        start = fn.first_token.start
        end = fn.last_token.stop
        chunk = concat[prev_end:end + 1]
        home = file_at(segs, start)
        chunks.append((home, chunk))
        prev_end = end + 1
    tail = concat[prev_end:]  # trailing whitespace after last function

    # reassemble per file, preserving manifest file order
    order = [f for _, _, f in segs]
    out = {f: [] for f in order}
    for home, chunk in chunks:
        out[home].append(chunk)
    # append global tail to the last non-reassigned position: last file in order
    out[order[-1]].append(tail)

    new_files = {f: "".join(out[f]) for f in order}

    # invariant: concatenation byte-identical
    rebuilt = "".join(new_files[f] for f in order)
    assert rebuilt == concat, "CONCAT MISMATCH — aborting"
    print("concat byte-identical: OK")

    empties = [f for f in order if new_files[f] == ""]
    print(f"files: {len(order)}  would-be-empty: {len(empties)}")
    for f in empties:
        print("   EMPTY:", f)

    # report parseability of each new file independently
    bad = 0
    for f in order:
        try:
            if new_files[f].strip():
                a.parse(new_files[f])
        except Exception:
            bad += 1
            print("   PARSE-FAIL:", f)
    print(f"independently-parseable: {len(order) - bad}/{len(order)}")

    if args.write:
        for f in order:
            (SE / f).write_text(new_files[f], encoding="utf-8", newline="\n")
        print("written")


if __name__ == "__main__":
    main()
