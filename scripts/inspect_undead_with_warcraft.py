# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

uids = [
    'n014', 'u00F', 'u00G', 'u00H', 'u00I', 'u00J', 'u00K', 'u00L', 'u00M', 'u00N', 'n012', 'u03B', 'u017', 'h0D1',
    'u00P', 'n011', 'n013', 'u03E', 'u00A', 'u00B', 'u00D', 'u00C', 'u008', 'u00E', 'u034', 'ft00', 'ft01', 'n07H', 'u03D', 'n016', 'n017', 'CM00', 'FL00',
    'U00O', 'U00V', 'U00U', 'U030', 'U014'
]

print("=== INSPECTING WITH BASE DATA ===")
for uid in uids:
    args = ["get-object", "--map", str(hw.DEFAULT_MAP), "--type", "unit", "--id", uid]
    if hw.DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(hw.DEFAULT_WARCRAFT)])
    data = hw.run_cli_json(args)
    obj = data.get("object", {}) or data.get("fields", {})
    name = hw.resolve_trigstr(obj.get('name', ''))
    tip = hw.resolve_trigstr(obj.get('tip', ''))
    abils = obj.get('abillist')
    heroabils = obj.get('heroabillist')
    trains = obj.get('train')
    researches = obj.get('researches')
    upgrades = obj.get('upgrades')
    upgrades_to = obj.get('upgrade')
    print(f"[{uid}] {name} ({hw.clean_wc3_string(name)})")
    if abils: print(f"    Abils: {abils}")
    if heroabils: print(f"    HeroAbils: {heroabils}")
    if trains: print(f"    Trains: {trains}")
    if researches: print(f"    Researches: {researches}")
    if upgrades_to: print(f"    Upgrades_to: {upgrades_to}")
    if upgrades: print(f"    Upgrades: {upgrades}")
