# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return (s, wts.get(int(s[8:]), s))
    return (None, s)

unit_ids = [
    'h0G9', 'h0F4', 'h0GS', 'h0GT', 'h0GV', 'h0GU',
    'h0GW', 'h0GX', 'h0HD', 'h0HE', 'h0L3', 'o03X',
    'h0GY', 'h0HC', 'h02Z', 'h0HX', 'h0I3',
    'o02Q', 'o06A', 'o06B', 'o06C',
    'o02R', 'o06D', 'o06E', 'o06F'
]

print("=== INSPECTION OF STROMGARD UNITS ===")
for uid in unit_ids:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    name_wts, name_val = res(f.get('name'))
    tip_wts, tip_val = res(f.get('tip'))
    ubertip_wts, ubertip_val = res(f.get('ubertip'))
    suffix_wts, suffix_val = res(f.get('editorsuffix'))
    print(f"ID: {uid} | Name: {name_val} ({name_wts}) | Suffix: {suffix_val} ({suffix_wts})")
    print(f"  Hotkey: {f.get('hotkey')}")
    print(f"  Tip: {tip_val} ({tip_wts})")
    print(f"  Ubertip: {ubertip_val} ({ubertip_wts})")
    print(f"  Abilities: {f.get('abillist')}")
    print(f"  Atk1: type={f.get('atktype1')} weapon={f.get('weapsontype1')} targs={f.get('targs1')} range={f.get('rangeN1')}")
    print(f"  Atk2: type={f.get('atktype2')} weapon={f.get('weapsontype2')} targs={f.get('targs2')} range={f.get('rangeN2')}")
    print(f"  Trains: {f.get('trains')} Builds: {f.get('builds')}")
    print("-" * 60)
