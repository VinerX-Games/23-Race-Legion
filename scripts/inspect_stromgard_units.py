# -*- coding: utf-8 -*-
"""Inspect all candidate units for Stromgard."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
wts = hw.load_wts_strings()

def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return wts.get(int(s[8:]), s)
    return s

unit_ids = [
    'h0G9', 'h0F4', 'h0GS', 'h0GT', 'h0GV', 'h0GU',
    'h0GW', 'h0GX', 'h0HD', 'h0HE', 'h0L3', 'o03X',
    'h0GY', 'h0HC', 'h02Z', 'h0HX', 'h0I3',
    'o02Q', 'o02R', 'o06A', 'o06B', 'o06C', 'o06D', 'o06E', 'o06F'
]

for uid in unit_ids:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    print(f"=== {uid} {res(f.get('name'))} (suffix: {res(f.get('editorsuffix'))}) ===")
    print('  tip:', repr(res(f.get('tip'))))
    print('  ubertip:', repr(res(f.get('ubertip'))))
    print('  hotkey:', repr(res(f.get('hotkey'))))
    print('  abillist:', f.get('abillist'))
    print('  atk1:', f.get('weapsontype1'), f.get('atktype1'), f.get('targs1'))
    print('  atk2:', f.get('weapsontype2'), f.get('atktype2'), f.get('targs2'))
    print('  isbldg:', f.get('isbldg'))
    print('  race:', f.get('race'))
    print('  trains:', f.get('trains'))
    print('  builds:', f.get('builds'))
    print('  upgrade:', f.get('upgrade'))
    print()
