# -*- coding: utf-8 -*-
"""Inspect Stromgard unit abilities, cauldron abilities, and buffs."""
import json
from pathlib import Path
from wc3_hivewe import run_cli_json, DEFAULT_MAP, DEFAULT_WARCRAFT

unit_ability_ids = [
    # Worker & Militia
    "A0WG", "A0WI",  # Call to arms / Back to work
    # Footman / Defender
    "A0VI", "A0WT",  # Defend / Shield bash or similar
    # Crossbowman
    "A0XS", "A0XQ",
    # Knight
    "A0WO", "A0WP",
    # Priest / Caster
    "A0WM", "A0WN", "A0WJ", "A0WK", "A0WH", "A0WL", "A0WS",
    # Captain / Troll Hunter
    "A17U", "A0WU",
    # Catapult / Tank / Donkey
    "A0XP", "A0XO", "A0XN", "A0XR",
    # Paladins
    "A0XY", "A0XT",
    # Cauldron spells
    "A0ZM", "A0ZR", "A0ZS", "A1O6", "A0ZT", "A1O7", "A1O3", "A1O8", "A1O4"
]

res = {}
for ab_id in unit_ability_ids:
    args = ["get-object", "--map", str(DEFAULT_MAP), "--type", "ability", "--id", ab_id]
    if DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])
    data = run_cli_json(args)
    if data.get("ok"):
        obj = data.get("object", {}) or data.get("fields", {})
        res[ab_id] = {
            "name": obj.get("name"),
            "base": obj.get("base_id") or obj.get("code"),
            "levels": obj.get("levels"),
            "raw": {k: v for k, v in obj.items() if any(sub in k.lower() for sub in ["tip", "ubertip", "hotkey", "buttonpos", "cost", "cool", "mana", "targ", "cast", "dur", "area", "buff"])}
        }
    else:
        res[ab_id] = {"error": data.get("error") or data.get("raw")}

with open("docs/ui_text/stromgard_unit_abilities_raw.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(f"Dumped {len(res)} abilities")
