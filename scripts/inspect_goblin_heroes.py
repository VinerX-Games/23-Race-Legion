# -*- coding: utf-8 -*-
"""Inspect all 6 Goblin heroes: алтарные и легендарные."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

hero_ids = ["H0BD", "Galh", "Gmex", "N018", "N019", "N01A"]

heroes_data = {}
for hid in hero_ids:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", hid])
    if not res.get("ok"):
        print(f"Error fetching {hid}: {res}")
        continue
    f = res.get("object", {}) or res.get("fields", {})
    heroes_data[hid] = {
        "id": hid,
        "name_raw": f.get("name"),
        "name": resolve(f.get("name")),
        "propernames_raw": f.get("propernames"),
        "propernames": resolve(f.get("propernames")),
        "hotkey_raw": f.get("hotkey"),
        "hotkey": resolve(f.get("hotkey")),
        "tip_raw": f.get("tip"),
        "tip": resolve(f.get("tip")),
        "ubertip_raw": f.get("ubertip"),
        "ubertip": resolve(f.get("ubertip")),
        "revivetip_raw": f.get("revivetip"),
        "revivetip": resolve(f.get("revivetip")),
        "awakentip_raw": f.get("awakentip"),
        "awakentip": resolve(f.get("awakentip")),
        "heroabillist": f.get("heroabillist"),
        "abillist": f.get("abillist"),
        "atktype1": f.get("atktype1"),
        "weaptp1": f.get("weaptp1"),
        "mindmg1": f.get("mindmg1"),
        "maxdmg1": f.get("maxdmg1"),
        "cool1": f.get("cool1"),
        "ran1": f.get("ran1") or f.get("rangeN1"),
        "targs1": f.get("targs1"),
        "hp": f.get("hp"),
        "mana0": f.get("mana0"),
        "def": f.get("def"),
        "deftype": f.get("deftype"),
        "spd": f.get("spd"),
        "movetp": f.get("movetp")
    }

with open(ROOT / "docs/ui_text/goblin_heroes_raw.json", "w", encoding="utf-8") as out:
    json.dump(heroes_data, out, ensure_ascii=False, indent=2)

print(f"Dumped {len(heroes_data)} heroes to docs/ui_text/goblin_heroes_raw.json")
