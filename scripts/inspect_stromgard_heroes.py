# -*- coding: utf-8 -*-
"""Inspect Stromgard heroes and their abilities."""
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return (s, wts.get(int(s[8:]), s))
    return (None, s)

heroes = ['H0HB', 'H0HL', 'H0HA', 'H0L4']

print("=== STROMGARD HEROES ===")
for hid in heroes:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    name_wts, name = res(f.get('name'))
    tip_wts, tip = res(f.get('tip'))
    ubertip_wts, ubertip = res(f.get('ubertip'))
    rev_wts, rev = res(f.get('revivetip'))
    awk_wts, awk = res(f.get('awakentip'))
    prop_wts, prop = res(f.get('propernames'))
    print(f"ID: {hid} | Name: {name} ({name_wts}) | Suffix: {f.get('editorsuffix')}")
    print(f"  Propernames: {prop} ({prop_wts})")
    print(f"  Hotkey: {f.get('hotkey')}")
    print(f"  Tip: {tip} ({tip_wts})")
    print(f"  Ubertip: {ubertip} ({ubertip_wts})")
    print(f"  Revivetip: {rev} ({rev_wts})")
    print(f"  Awakentip: {awk} ({awk_wts})")
    print(f"  HeroAbils: {f.get('heroabillist')}")
    print(f"  Abils: {f.get('abillist')}")
    print(f"  Atk1: type={f.get('atktype1')} weapon={f.get('weapsontype1')} targs={f.get('targs1')} range={f.get('rangeN1')}")
    print(f"  Atk2: type={f.get('atktype2')} weapon={f.get('weapsontype2')} targs={f.get('targs2')} range={f.get('rangeN2')}")
    print("-" * 60)
