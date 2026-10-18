# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

abils = [
    'A0I3', 'Arep', 'A1LR', 'A0RK', 'drat', 'A0RE', 'drAa', 'drAs', 'Alit',
    'A0RO', 'A0RJ', 'drAz', 'drA2', 'drAw', 'drAy', 'drAe', 'drAr', 'drEt',
    'drAd', 'drA0', 'drA3', 'drA4', 'A1BD', 'drA5', 'A0QB', 'Afrb', 'dra3',
    'drA6', 'drA1', 'drAq', 'drA7', 'A0RM', 'drA8', 'drA9', 'A1BF', 'A0RL',
    'A0QO', 'A0RN'
]

bulk = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(abils), '--fields', 'name,tip1,ubertip1,researchtip,researchubertip']))
for o in bulk['objects']:
    aid = o['id']
    f = o['fields']
    nm = resolve(f.get('name'))
    tp = resolve(f.get('tip1'))
    ub = resolve(f.get('ubertip1'))
    print(f"=== {aid} ({nm}) ===")
    print(f"tip1: {tp}")
    print(f"ubertip1: {ub}\n")
