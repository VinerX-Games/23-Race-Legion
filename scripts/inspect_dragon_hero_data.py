# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

hero_abils = [
    'A0RB', 'A0QY', 'A0R0', 'A0QX', 'A0QZ',
    'A0RD', 'A0R4', 'A0R3', 'A0R2', 'A1MX',
    'A0RA', 'A0R5', 'A0R6', 'A0R7', 'A0R8',
    'A0RC', 'A0QV', 'A0QU', 'A0QT', 'A10E'
]

bulk = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(hero_abils)]))
for o in bulk['objects']:
    aid = o['id']
    f = o['fields']
    nm = resolve(f.get('name'))
    print(f"=== {aid} ({nm}) ===")
    for k in sorted(f.keys()):
        if any(k.startswith(p) for p in ['data', 'cost', 'cool', 'rng', 'dur', 'area', 'buff']):
            print(f"  {k}: {f[k]}")
