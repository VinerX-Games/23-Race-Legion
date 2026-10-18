# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_upgrade, resolve

upg_candidates = [
    'R0HT',
    # From building fields
    'R0L2', 'R0GU', 'R09W', 'R0GO', 'R0GP', 'R0GL', 'R0GQ', 'R0GM', 'R0GN',
    'R0GF', 'R0GG', 'R0GH', 'R0GI', 'R0GJ', 'R0GK', 'R0GT', 'R0GS', 'R0GR',
    # From 20_ogres.lua
    'R0G4', 'R0G5', 'R0G7', 'R0GW', 'R0GX', 'R0GY', 'R0GZ', 'R0H0', 'R0H1', 'R0H2',
]

unique_upgs = sorted(list(set(upg_candidates)))
print(f"Total upgrade candidates: {len(unique_upgs)}")

for uid in unique_upgs:
    u = inspect_upgrade(uid)
    name1 = u['names'].get('name1', {}).get('val')
    levels = u.get('levels', 1)
    print(f"\nUpgrade {uid}: levels={levels}, name1='{name1}'")
    for lvl in range(1, levels + 1):
        n = u['names'].get(f'name{lvl}', {}).get('val')
        t = u['tips'].get(f'tip{lvl}', {}).get('val')
        ub = u['ubertips'].get(f'ubertip{lvl}', {}).get('val')
        hk = u['hotkeys'].get(f'hotkey{lvl}', {}).get('val')
        print(f"  L{lvl}: name='{n}', tip='{t}', hk='{hk}'")
        print(f"      ubertip='{ub}'")
