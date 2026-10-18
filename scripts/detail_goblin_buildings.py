# -*- coding: utf-8 -*-
"""Detail audit of all 10 Goblin buildings."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

building_ids = ["h070", "h077", "h073", "h074", "h075", "h076", "h079", "h07S", "o016", "h0D7"]

result = {}

for bid in building_ids:
    args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", bid]
    res = hw.run_cli_json(args)
    if not res.get("ok"):
        print(f"Error fetching {bid}: {res}")
        continue
    f = res.get("object", {}) or res.get("fields", {})
    
    # Extract keys and check their raw TRIGSTR_ values
    info = {
        "id": bid,
        "name_raw": f.get("name"),
        "name": resolve(f.get("name")),
        "editorsuffix": resolve(f.get("editorsuffix")),
        "hotkey_raw": f.get("hotkey"),
        "hotkey": resolve(f.get("hotkey")),
        "tip_raw": f.get("tip"),
        "tip": resolve(f.get("tip")),
        "ubertip_raw": f.get("ubertip"),
        "ubertip": resolve(f.get("ubertip")),
        "train": f.get("train"),
        "researches": f.get("reserches") or f.get("researches"),
        "sellunits": f.get("sellunits"),
        "sellitems": f.get("sellitems"),
        "upgrades": f.get("upgrades"),
        "abillist": f.get("abillist"),
        "goldcost": f.get("goldcost"),
        "lumbercost": f.get("lumbercost"),
        "bldtm": f.get("bldtm"),
        "fmade": f.get("fmade"),
        "fused": f.get("fused"),
        "hp": f.get("hp"),
        "def": f.get("def"),
        "deftype": f.get("deftype"),
        "weaptp1": f.get("weaptp1"),
        "atktype1": f.get("atktype1"),
        "mindmg1": f.get("mindmg1"),
        "maxdmg1": f.get("maxdmg1"),
        "cool1": f.get("cool1"),
        "ran1": f.get("ran1") or f.get("rangeN1"),
        "targs1": f.get("targs1"),
    }
    result[bid] = info

print(json.dumps(result, ensure_ascii=False, indent=2))
with open(ROOT / "docs/ui_text/goblin_buildings_raw.json", "w", encoding="utf-8") as out:
    json.dump(result, out, ensure_ascii=False, indent=2)
