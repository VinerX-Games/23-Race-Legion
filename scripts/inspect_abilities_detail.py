# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return wts.get(int(s[8:]), s)
    return s

abils = [
    'A0WG', 'A0WI', 'A0VI', 'A0WT',
    'A0XS', 'A0XQ', 'A0WO', 'A0WP', 'A0WM', 'A0WN', 'A0WJ',
    'A0WK', 'A0WH', 'A0WL', 'A0WS', 'A17U', 'A0WU',
    'A0XP', 'A0XO', 'A0XN', 'A0XR', 'A0XY', 'A0XT'
]

for aid in abils:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    print(f"=== {aid}: {res(f.get('name'))} ===")
    print(f"  tip: {res(f.get('tip1')) or res(f.get('tip'))}")
    print(f"  ubertip: {res(f.get('ubertip1')) or res(f.get('ubertip'))}")
    for k in sorted(f.keys()):
        if any(k.startswith(p) for p in ['data', 'Data', 'dur', 'cool', 'cost', 'rng']):
            print(f"  {k}: {f[k]}")
