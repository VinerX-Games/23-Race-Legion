# -*- coding: utf-8 -*-
"""Test exact mapping of Elements hero abilities text fields to WTS IDs and inline."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
raw_data = json.load((ROOT / "docs/ui_text/elements_hero_abils_raw.json").open(encoding="utf-8"))

# Load hero_abilities from update_elements_hero_abils
from update_elements_hero_abils import hero_abilities

wts_mapping = {}
inline_ops = []

for abil in hero_abilities:
    aid = abil["id"]
    raw_fields = raw_data.get(aid, {})
    vals = abil.get("values", {})
    for f, expected in vals.items():
        f_info = raw_fields.get(f)
        if isinstance(f_info, dict) and "wts_id" in f_info:
            wid = f_info["wts_id"]
            orig_text = f_info.get("text", "")
            wts_mapping[(aid, f)] = (wid, orig_text)
        else:
            inline_ops.append((aid, f, f_info.get("raw") if isinstance(f_info, dict) else f_info))

print(f"Total fields: {len(wts_mapping) + len(inline_ops)}")
print(f"WTS mapped: {len(wts_mapping)}")
print(f"Inline ops: {len(inline_ops)}")
print("\nInline fields:")
for aid, f, orig in inline_ops:
    print(f"  [{aid}] {f} (orig: {repr(str(orig)[:40])})")

# Check for duplicate WTS IDs inside Elements hero abilities
wts_to_abils = {}
for (aid, f), (wid, orig) in wts_mapping.items():
    wts_to_abils.setdefault(wid, []).append((aid, f))

duplicates = {wid: afs for wid, afs in wts_to_abils.items() if len(afs) > 1}
print(f"\nWTS IDs used multiple times inside Elements hero abilities: {len(duplicates)}")
for wid, afs in duplicates.items():
    print(f"  WTS_{wid}: {afs}")
