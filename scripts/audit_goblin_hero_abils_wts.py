# -*- coding: utf-8 -*-
"""Audit Goblin hero abilities WTS keys and shared strings."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
raw_path = ROOT / "docs/ui_text/goblin_hero_abils_raw.json"
abils = json.loads(raw_path.read_text(encoding="utf-8"))

print(f"Total abilities: {len(abils)}")
wts_refs = {}

for aid, a in sorted(abils.items()):
    name = a.get("name")
    levels = a.get("levels")
    rtip = a.get("researchtip")
    rubertip = a.get("researchubertip")
    hotkey = a.get("hotkey")
    rhotkey = a.get("researchhotkey")
    print(f"=== [{aid}] {name} (levels={levels}, hotkey={hotkey}/{rhotkey}) ===")
    
    # Check string fields
    fields_to_check = [("name", a.get("name_raw")), ("researchtip", a.get("researchtip_raw")), ("researchubertip", a.get("researchubertip_raw"))]
    for lvl, lf in a.get("level_fields", {}).items():
        fields_to_check.append((f"tip{lvl}", lf.get("tip_raw")))
        fields_to_check.append((f"ubertip{lvl}", lf.get("ubertip_raw")))
    
    for fname, rval in fields_to_check:
        if isinstance(rval, str) and rval.startswith("TRIGSTR_"):
            sid = int(rval[8:])
            wts_refs.setdefault(sid, []).append((aid, fname))
        elif rval is not None:
            print(f"  Inline {fname}: {repr(rval)[:60]}")

print("\n=== Shared WTS check across hero abilities ===")
shared_internal = {sid: refs for sid, refs in wts_refs.items() if len(refs) > 1}
if shared_internal:
    for sid, refs in shared_internal.items():
        print(f"  Internal shared TRIGSTR_{sid}: {refs}")
else:
    print("  No internal shared strings between hero abilities.")

print("\n=== Checking all hero ability WTS against entire map object data ===")
map_dir = ROOT / "map.w3x"
all_sids = list(wts_refs.keys())
shared_map = {}
for f in map_dir.glob("war3map*.*"):
    if f.suffix in [".w3u", ".w3a", ".w3q", ".w3h", ".w3t", ".w3b", ".w3d"]:
        data = f.read_bytes()
        for sid in all_sids:
            cnt = data.count(f"TRIGSTR_{sid}".encode("ascii"))
            if cnt > len(wts_refs[sid]):
                shared_map.setdefault(sid, []).append((f.name, cnt, len(wts_refs[sid])))

if shared_map:
    print("  FOUND SHARED STRINGS WITH OTHER OBJECTS:")
    for sid, info in shared_map.items():
        print(f"    TRIGSTR_{sid} (used by {wts_refs[sid]}): occurrences = {info}")
else:
    print("  ALL HERO ABILITY WTS KEYS ARE 100% EXCLUSIVE TO THESE HERO ABILITIES!")

with open(ROOT / "docs/ui_text/goblin_hero_abils_wts_refs.json", "w", encoding="utf-8") as out:
    json.dump({str(k): v for k, v in wts_refs.items()}, out, ensure_ascii=False, indent=2)
