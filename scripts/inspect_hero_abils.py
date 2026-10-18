# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return wts.get(int(s[8:]), s)
    return s

habils = [
    'A0XM', 'A0XW', 'A0Y8', 'A0XZ',
    'A0XV', 'A0ZP', 'A0ZO', 'A0ZN',
    'A0ZQ', 'A0XK', 'A0Y6', 'A0Y7',
    'A17X', 'A17W', 'A17V', 'A17S', 'A1LH'
]

for aid in habils:
    obj = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = obj.get('fields', {})
    name = res(f.get('name'))
    tip = res(f.get('tip1')) or res(f.get('tip'))
    ubertip = res(f.get('ubertip1')) or res(f.get('ubertip'))
    rtip = res(f.get('researchtip'))
    rubertip = res(f.get('researchubertip'))
    print(f"=== {aid}: {name} ===")
    print(f"  Tip1: {tip}")
    print(f"  Ubertip1: {ubertip}")
    print(f"  RTip: {rtip}")
    print(f"  RUbertip: {rubertip}")
    data_fields = {k: v for k, v in f.items() if any(k.startswith(p) for p in ['Data', 'data', 'Dur', 'dur', 'Cool', 'cool', 'Cost', 'cost', 'Rng', 'rng', 'Area', 'area'])}
    print(f"  Data: {data_fields}")
    print("-" * 50)
