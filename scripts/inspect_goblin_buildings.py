# -*- coding: utf-8 -*-
"""Inspect Goblin buildings, their upgrades, trains, and researches."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw

buildings = ["h070", "h077", "h073", "h074", "h075", "h076", "h079", "h07S", "o016", "h0D7"]

seen = set(buildings)
queue = list(buildings)

all_buildings = {}

while queue:
    bid = queue.pop(0)
    args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", bid]
    res = hw.run_cli_json(args)
    if not res.get("ok"):
        print(f"Failed to fetch {bid}: {res}")
        continue
    fields = res.get("object", {}) or res.get("fields", {})
    all_buildings[bid] = fields
    # check upgrades to other buildings
    upg = fields.get("upgrades") or fields.get("upgrade")
    if upg:
        for u in upg.split(","):
            u = u.strip()
            if len(u) == 4 and u not in seen:
                # check if it is a building
                check = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", u])
                if check.get("ok"):
                    cf = check.get("object", {}) or check.get("fields", {})
                    if cf.get("isbldg") == 1 or cf.get("isbldg") == "1":
                        seen.add(u)
                        queue.append(u)

# Also check builds from other buildings or workers
wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

print(f"Total Goblin buildings found: {len(all_buildings)}")
for bid, f in sorted(all_buildings.items()):
    name = resolve(f.get("name"))
    suffix = resolve(f.get("editorsuffix"))
    train = f.get("train", "")
    researches = f.get("reserches", "") or f.get("researches", "")
    upgrades = f.get("upgrades", "")
    hotkey = resolve(f.get("hotkey", ""))
    tip = resolve(f.get("tip", ""))
    ubertip = resolve(f.get("ubertip", ""))
    print(f"=== [{bid}] {name} ({suffix}) ===")
    print(f"  Hotkey: {hotkey}")
    print(f"  Tip: {tip}")
    print(f"  Ubertip: {ubertip[:100]}...")
    print(f"  Trains: {train}")
    print(f"  Researches: {researches}")
    print(f"  Upgrades to: {upgrades}")
