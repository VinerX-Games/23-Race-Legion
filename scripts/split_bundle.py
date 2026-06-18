"""Split a multi-race trigger bundle into per-race files at trigger boundaries.

The bundle file is independently parseable (functions are whole). We chunk it as
(leading --=== Trigger comment + function) units, then route each chunk to a
target file; the target switches when a chunk's `-- Trigger: <Name>` banner
matches a configured boundary. The concatenation of the produced files is
byte-identical to the original bundle, and they replace the bundle in the
manifest at the same position, so the built war3map.lua is unchanged.

Edit PLAN below, then run with --write.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import luaparser.ast as a
from luaparser import astnodes as n

SP = Path(__file__).resolve().parent / "map.w3x" / "_lua" / "monolith_split"
SE = SP / "sections"

# bundle relpath -> (first_target, [(boundary_trigger_name, target_relpath), ...])
R = "80_runtime/triggers/races/"
T = "80_runtime/triggers/"
PLAN = {
    "80_runtime/triggers/07_hero_bezlikie_horde.lua": (
        T + "07_mixed_heroes.lua",
        [
            ("StromgardOn", R + "Stromgard.lua"),
            ("Sluga qqgsarona", R + "Bezlikie.lua"),
            ("TrainW2", R + "HordeW2.lua"),
        ],
    ),
    "80_runtime/triggers/09_alliance.lua": (
        R + "Alliance.lua",
        [],
    ),
    "80_runtime/triggers/11_horde.lua": (
        R + "Horde.lua",
        [],
    ),
}

BANNER_RE = re.compile(r"^-- Trigger:\s*(\S.*?)\s*$", re.M)


def banner_trigger(chunk_head):
    m = BANNER_RE.search(chunk_head)
    return m.group(1) if m else None


def split_one(bundle_rel, first_target, boundaries):
    text = (SE / bundle_rel).read_text(encoding="utf-8-sig")
    tree = a.parse(text)
    funcs = [x for x in tree.body.body if isinstance(x, n.Function)]
    bmap = dict(boundaries)
    order = [first_target]
    for _, t in boundaries:
        if t not in order:
            order.append(t)
    out = {t: [] for t in order}

    cur = first_target
    prev_end = 0
    for fn in funcs:
        end = fn.last_token.stop
        chunk = text[prev_end:end + 1]
        name = banner_trigger(chunk)
        if name in bmap:
            cur = bmap[name]
        out[cur].append(chunk)
        prev_end = end + 1
    tail = text[prev_end:]
    out[order[-1]].append(tail)

    new_files = {t: "".join(out[t]) for t in order}
    assert "".join(new_files[t] for t in order) == text, "CONCAT MISMATCH"
    return order, new_files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    man = json.loads((SP / "manifest.json").read_text(encoding="utf-8-sig"))
    sections = man["sections"]

    for bundle_rel, (first_target, boundaries) in PLAN.items():
        order, new_files = split_one(bundle_rel, first_target, boundaries)
        print(f"\n{bundle_rel}:")
        for t in order:
            cnt = new_files[t].count("\nfunction ") + new_files[t].startswith("function ")
            print(f"   {t}: {len(new_files[t]):>7} bytes")
        # independent parse check
        for t in order:
            try:
                if new_files[t].strip():
                    a.parse(new_files[t])
            except Exception as ex:  # noqa
                print(f"   PARSE-FAIL {t}: {str(ex)[:120]}")
                return
        if args.write:
            (SE / order[0]).parent.mkdir(parents=True, exist_ok=True)
            for t in order:
                (SE / t).write_text(new_files[t], encoding="utf-8", newline="\n")
            # rewrite manifest: replace bundle entry with the new ones in order
            idx = next(i for i, s in enumerate(sections) if s["file"] == bundle_rel)
            base = sections[idx]
            new_entries = []
            for t in order:
                e = dict(base)
                e["file"] = t
                e["name"] = "gen:" + t.split("/")[-1][:-4]
                new_entries.append(e)
            sections[idx:idx + 1] = new_entries
            (SE / bundle_rel).unlink()

    if args.write:
        man["section_count"] = len(sections)
        (SP / "manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False),
                                          encoding="utf-8", newline="\n")
        print("\nmanifest updated; bundle removed")


if __name__ == "__main__":
    main()
