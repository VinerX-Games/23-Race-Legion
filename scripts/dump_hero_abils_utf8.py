# -*- coding: utf-8 -*-
"""Inspect exact mechanics and level values of all 25 Goblin hero abilities directly to UTF-8 file."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
raw_path = ROOT / "docs/ui_text/goblin_hero_abils_plan_raw.json"
plan = json.loads(raw_path.read_text(encoding="utf-8"))

out_lines = []
for aid, info in sorted(plan.items()):
    raw = info["raw"]
    name = info["name"]
    hero = info["hero"]
    hotkey = info["hotkey"]
    levels = info["max_lvl"]
    
    rtip = raw.get("researchtip")
    rub = raw.get("researchubertip")
    
    out_lines.append(f"=== [{aid}] {name} ({hero}) | hotkey={hotkey} | lvls={levels} ===")
    out_lines.append(f"  ResearchTip: {rtip}")
    out_lines.append(f"  ResearchUbertip: {rub}")
    for lvl, lf in raw.get("level_fields", {}).items():
        tip = lf.get("tip")
        ub = lf.get("ubertip")
        cost = lf.get("cost")
        cool = lf.get("cool")
        rng = lf.get("rng")
        dur = lf.get("dur")
        dataa = lf.get("dataa")
        datab = lf.get("datab")
        datac = lf.get("datac")
        datad = lf.get("datad")
        out_lines.append(f"  [L{lvl}] Tip: {tip}")
        out_lines.append(f"       Ubertip: {ub}")
        out_lines.append(f"       Cost: {cost} | Cool: {cool} | Rng: {rng} | Dur: {dur} | data=({dataa}, {datab}, {datac}, {datad})")
    out_lines.append("")

out_file = ROOT / "docs/ui_text/goblin_hero_abils_mechanics_clean.txt"
out_file.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Saved {len(out_lines)} lines to docs/ui_text/goblin_hero_abils_mechanics_clean.txt")
