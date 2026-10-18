# -*- coding: utf-8 -*-
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

hero_abils = [
    'A0M8', 'A0MB', 'A0MC', 'A0M9', # N02F
    'A0MF', 'A0MA', 'A0ME', 'A0MD', # N02A
    'A0MG', 'A0MO', 'A0MN', 'A0MP', # U028
    'A0NG', 'A0ND', 'A0NB', 'A0NC', # N02G (+ trigger spell A0NC)
    'A0NA', 'A1BY', 'A0N7', 'A0N8', 'A1BV', # N02B (+ trigger spell A0N8)
    'A0MV', 'A0MU', 'A0MT', # N02H
    'A0MS', 'A0MR', 'A0MQ', 'S006', # U027
]

unit_abils = [
    'A0LU', 'A0I3', 'A0VY', 'Aren', 'ANha', 'Arst',
    'S004', 'S003', 'A0LW', 'S005', 'A0LX', 'A0LV',
    'A0M3', 'A16J', 'A0M1', 'A0M2', 'A0M0', 'A0LZ',
    'Advc', 'A0LY', 'A0MW', 'A0MX', 'A0M7', 'A0M6',
    'A0M5', 'A0M4', 'ACce', 'A1KB'
]

print("=== HERO ABILITIES ===")
for aid in hero_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    lvls = int(f.get('levels', 1) or 1)
    name = resolve(f.get('name'))
    code = f.get('code')
    hotkey = resolve(f.get('hotkey'))
    buffs = [f.get(f'buffid{i}') for i in range(1, lvls+1) if f.get(f'buffid{i}')]
    print(f"{aid} ({code}): {name} [lvls={lvls}, hotkey={hotkey}, buffs={buffs}]")
    for lvl in range(1, lvls + 1):
        tip = resolve(f.get(f'tip{lvl}') or f.get('tip'))
        ubertip = resolve(f.get(f'ubertip{lvl}') or f.get('ubertip'))
        print(f"  lvl {lvl}: tip={repr(tip)}")
        print(f"         ubertip={repr(ubertip)}")

print("\n=== UNIT ABILITIES ===")
for aid in unit_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    lvls = int(f.get('levels', 1) or 1)
    name = resolve(f.get('name'))
    code = f.get('code')
    hotkey = resolve(f.get('hotkey'))
    buffs = [f.get(f'buffid{i}') for i in range(1, lvls+1) if f.get(f'buffid{i}')]
    print(f"{aid} ({code}): {name} [lvls={lvls}, hotkey={hotkey}, buffs={buffs}]")
    for lvl in range(1, lvls + 1):
        tip = resolve(f.get(f'tip{lvl}') or f.get('tip'))
        ubertip = resolve(f.get(f'ubertip{lvl}') or f.get('ubertip'))
        print(f"  lvl {lvl}: tip={repr(tip)}")
        print(f"         ubertip={repr(ubertip)}")
