# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / 'scripts/kultiras_raw_dump.json', encoding='utf-8'))

def check_obj(cat, o):
    for k, v in o.items():
        if isinstance(v, dict):
            for subk, subv in v.items():
                if isinstance(subv, dict) and 'raw' in subv:
                    raw = subv['raw']
                    if raw and not str(raw).startswith('TRIGSTR_'):
                        print(f"LITERAL in {cat} {o.get('id')}: {k}.{subk} = {repr(raw)[:80]}")
        elif k.startswith('raw_'):
            if v and not str(v).startswith('TRIGSTR_'):
                print(f"LITERAL in {cat} {o.get('id')}: {k} = {repr(v)[:80]}")

for b in d['buildings']:
    check_obj('building', b)
for h in d['heroes']:
    check_obj('hero', h)
for u in d['units']:
    check_obj('unit', u)
for up in d['upgrades']:
    if up['id'] != 'Rguv':
        check_obj('upgrade', up)
for a in d['abilities']:
    check_obj('ability', a)
