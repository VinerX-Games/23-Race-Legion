"""Shared engine for AST-based idiomatization of the split Lua tree.

The split section files are NOT independently parseable (the auto-split cut
through function bodies). So we concatenate them exactly like build_map_lua.py,
parse the whole monolith once, let a transform collect (start, stop, new_text)
replacements over global offsets, then map each replacement back to the single
section file that contains it and rewrite that file.

A transform is a callable: transform(text, tree) -> list[(start, stop_incl, new)].
"""
from __future__ import annotations

import json
from pathlib import Path

import luaparser.ast as a

SPLIT_DIR = Path(__file__).resolve().parent / "map.w3x" / "_lua" / "monolith_split"
SECTIONS = SPLIT_DIR / "sections"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def load_sections():
    manifest = json.loads(read_text(SPLIT_DIR / "manifest.json"))
    return [s["file"] for s in manifest["sections"]]


def build_concat():
    """Return (concat_text, segments) where segments=[(start,end,relpath,text)]."""
    files = load_sections()
    parts = []
    segments = []
    pos = 0
    for rel in files:
        text = read_text(SECTIONS / rel)
        parts.append(text)
        segments.append([pos, pos + len(text), rel, text])
        pos += len(text)
    return "".join(parts), segments


def seg_of(segments, off):
    for seg in segments:
        if seg[0] <= off < seg[1]:
            return seg
    return None


def run(transform, write=False, reparse=True):
    text, segments = build_concat()
    tree = a.parse(text)
    repls = transform(text, tree)
    # filter: keep only replacements fully inside one segment
    valid = []
    skipped = 0
    for start, stop, new in repls:
        s1 = seg_of(segments, start)
        s2 = seg_of(segments, stop)
        if s1 is None or s2 is None or s1 is not s2:
            skipped += 1
            continue
        valid.append((start, stop, new, s1))
    # group by segment
    by_seg = {}
    for start, stop, new, seg in valid:
        by_seg.setdefault(id(seg), (seg, []))[1].append((start, stop, new))
    changed_files = 0
    for seg, items in by_seg.values():
        base, _, rel, ftext = seg
        items.sort(key=lambda r: r[0], reverse=True)
        out = ftext
        for start, stop, new in items:
            ls, le = start - base, stop - base
            out = out[:ls] + new + out[le + 1:]
        if write and out != ftext:
            (SECTIONS / rel).write_text(out, encoding="utf-8", newline="\n")
            changed_files += 1
        seg[3] = out
    print(f"replacements={len(valid)} skipped_straddle={skipped} files_changed={changed_files}")
    if write and reparse:
        new_text, _ = build_concat()
        try:
            a.parse(new_text)
            print("REPARSE OK")
        except Exception as ex:  # noqa
            print(f"REPARSE FAIL: {str(ex)[:300]}")
    return len(valid)
