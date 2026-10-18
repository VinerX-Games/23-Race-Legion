# -*- coding: utf-8 -*-
"""Inspect exact mechanics and level values of all 25 Goblin hero abilities."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
raw_path = ROOT / "docs/ui_text/goblin_hero_abils_plan_raw.json"
plan = json.loads(raw_path.read_text(encoding="utf-8"))

for aid, info in sorted(plan.items()):
    raw = info["raw"]
    name = info["name"]
    hero = info["hero"]
    hotkey = info["hotkey"]
    levels = info["max_lvl"]
    
    rtip = raw.get("researchtip")
    rub = raw.get("researchubertip")
    
    print(f"=== [{aid}] {name} ({hero}) | hotkey={hotkey} | lvls={levels} ===")
    print(f"  ResearchTip: {rtip}")
    print(f"  ResearchUbertip: {rub}")
    for lvl, lf in raw.get("level_fields", {}).items():
        tip = lf.get("tip")
        ub = lf.get("ubertip")
        cost = lf.get("cost")
        cool = lf.get("cool")
        rng = lf.get("rng")
        dur = lf.get("dur")
        print(f"  [L{lvl}] Tip: {tip}")
        print(f"       Ubertip: {ub}")
        print(f"       Cost: {cost} | Cool: {cool} | Rng: {rng} | Dur: {dur}")
    print()
