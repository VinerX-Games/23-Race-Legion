# -*- coding: utf-8 -*-
"""Scan all abilities and buffs for Stromgard."""
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return (s, wts.get(int(s[8:]), s))
    return (None, s)

# All Stromgard ability IDs
hero_abils = [
    'A0XM', 'A0XW', 'A0Y8', 'A0XZ',
    'A0XV', 'A0ZP', 'A0ZO', 'A0ZN',
    'A0ZQ', 'A0XK', 'A0Y6', 'A0Y7',
    'A17X', 'A17W', 'A17V', 'A17S', 'A1LH'
]

unit_abils = [
    'A0WG', 'A0WI', 'A0VI', 'A0WT',
    'A0XS', 'A0XQ', 'A0WO', 'A0WP',
    'A0WM', 'A0WN', 'A0WJ', 'A0WK', 'A0WH', 'A0WL',
    'A0WS', 'A17U', 'A0WU',
    'A0XP', 'A0XO', 'A0XN', 'A0XR', 'A0XY', 'A0XT',
    'A0ZM', 'A0ZR', 'A0ZS', 'A1O6', 'A0ZT', 'A1O7', 'A1O3', 'A1O8', 'A1O4'
]

print("=== HERO ABILITIES STORAGE & LEVELS ===")
for aid in hero_abils:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    levels = int(f.get('levels', 1))
    name_wts, name = res(f.get('name'))
    hotkey = f.get('hotkey')
    print(f"ID: {aid} | Name: {name} ({name_wts}) | Levels: {levels} | Hotkey: {hotkey}")
    for lvl in range(1, levels + 1):
        tip_wts, tip = res(f.get(f'tip{lvl}'))
        ub_wts, ub = res(f.get(f'ubertip{lvl}'))
        print(f"  Lvl {lvl}: Tip={tip} ({tip_wts}) | Ub={ub} ({ub_wts})")
    rtip_wts, rtip = res(f.get('researchtip'))
    rub_wts, rub = res(f.get('researchubertip'))
    rhotkey = f.get('researchhotkey')
    print(f"  Research: Tip={rtip} ({rtip_wts}) | Ub={rub} ({rub_wts}) | Hotkey={rhotkey}")
    print("-" * 50)
