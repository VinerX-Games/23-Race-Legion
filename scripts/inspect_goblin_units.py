# -*- coding: utf-8 -*-
"""Inspect all Goblin units, forms, summons."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

unit_ids = [
    # Worker
    "n00V",
    # Barracks
    "h06K", "h06L", "h06Q", "h06N", "h06M", "h078", "h06O", "h07R",
    # Factory
    "h06S", "h06U", "h06Y", "h06Z", "h06R", "h06T",
    # Plant
    "o00W", "o00Y", "o00X", "h06P",
    # Naval
    "h06X", "h06V", "h06W", "h0DM", "h0OD",
    # Auxiliary/Traded
    "h0G8", "h07A"
]

units_data = {}
for uid in unit_ids:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid])
    if not res.get("ok"):
        print(f"Error fetching {uid}: {res}")
        continue
    f = res.get("object", {}) or res.get("fields", {})
    units_data[uid] = {
        "id": uid,
        "name_raw": f.get("name"),
        "name": resolve(f.get("name")),
        "editorsuffix": resolve(f.get("editorsuffix")),
        "hotkey_raw": f.get("hotkey"),
        "hotkey": resolve(f.get("hotkey")),
        "tip_raw": f.get("tip"),
        "tip": resolve(f.get("tip")),
        "ubertip_raw": f.get("ubertip"),
        "ubertip": resolve(f.get("ubertip")),
        "abillist": f.get("abillist"),
        "upgrades": f.get("upgrades"),
        "atktype1": f.get("atktype1"),
        "weaptp1": f.get("weaptp1"),
        "mindmg1": f.get("mindmg1"),
        "maxdmg1": f.get("maxdmg1"),
        "cool1": f.get("cool1"),
        "ran1": f.get("ran1") or f.get("rangeN1"),
        "targs1": f.get("targs1"),
        "atktype2": f.get("atktype2"),
        "weaptp2": f.get("weaptp2"),
        "mindmg2": f.get("mindmg2"),
        "maxdmg2": f.get("maxdmg2"),
        "cool2": f.get("cool2"),
        "targs2": f.get("targs2"),
        "goldcost": f.get("goldcost"),
        "lumbercost": f.get("lumbercost"),
        "fused": f.get("fused"),
        "bldtm": f.get("bldtm"),
        "hp": f.get("hp"),
        "mana0": f.get("mana0"),
        "def": f.get("def"),
        "deftype": f.get("deftype"),
        "spd": f.get("spd"),
        "movetp": f.get("movetp")
    }

with open(ROOT / "docs/ui_text/goblin_units_raw.json", "w", encoding="utf-8") as out:
    json.dump(units_data, out, ensure_ascii=False, indent=2)

print(f"Dumped {len(units_data)} units to docs/ui_text/goblin_units_raw.json")
