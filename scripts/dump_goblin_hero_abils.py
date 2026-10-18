# -*- coding: utf-8 -*-
"""Dump detailed fields of Goblin hero abilities."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

hero_abils = [
    # H0BD
    "A0D8", "A0D7", "AEar", "A0D5",
    # Galh
    "ANhs", "ANab", "ANcr", "ANtm",
    # Gmex
    "ANsy", "ANcs", "ANeg", "ANrg",
    # N018
    "A0DR", "A1KK", "A0DL", "A0DK",
    # N019
    "A0DU", "A1N0", "A1N3", "A1N1", "A1N4",
    # N01A
    "A0E2", "A0E1", "A0E0", "A13G"
]

res_dict = {}

for aid in hero_abils:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", aid])
    if not res.get("ok"):
        print(f"Error fetching {aid}: {res}")
        continue
    f = res.get("object", {}) or res.get("fields", {})
    levels = int(f.get("levels", 1))
    
    info = {
        "id": aid,
        "name_raw": f.get("name"),
        "name": resolve(f.get("name")),
        "levels": levels,
        "hotkey_raw": f.get("hotkey"),
        "hotkey": resolve(f.get("hotkey")),
        "researchtip_raw": f.get("researchtip"),
        "researchtip": resolve(f.get("researchtip")),
        "researchubertip_raw": f.get("researchubertip"),
        "researchubertip": resolve(f.get("researchubertip")),
        "researchhotkey_raw": f.get("researchhotkey"),
        "researchhotkey": resolve(f.get("researchhotkey")),
        "level_fields": {}
    }
    for lvl in range(1, levels + 1):
        info["level_fields"][lvl] = {
            "tip_raw": f.get(f"tip{lvl}"),
            "tip": resolve(f.get(f"tip{lvl}")),
            "ubertip_raw": f.get(f"ubertip{lvl}"),
            "ubertip": resolve(f.get(f"ubertip{lvl}")),
            "cost": f.get(f"cost{lvl}"),
            "cool": f.get(f"cool{lvl}"),
            "rng": f.get(f"rng{lvl}"),
            "dur": f.get(f"dur{lvl}"),
            "herodur": f.get(f"herodur{lvl}"),
            "area": f.get(f"area{lvl}"),
            "dataa": f.get(f"dataa{lvl}"),
            "datab": f.get(f"datab{lvl}"),
            "datac": f.get(f"datac{lvl}"),
            "datad": f.get(f"datad{lvl}"),
        }
    res_dict[aid] = info

with open(ROOT / "docs/ui_text/goblin_hero_abils_raw.json", "w", encoding="utf-8") as out:
    json.dump(res_dict, out, ensure_ascii=False, indent=2)

print(f"Dumped {len(res_dict)} hero abilities to docs/ui_text/goblin_hero_abils_raw.json")
