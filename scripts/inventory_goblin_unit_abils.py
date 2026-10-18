# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
def resolve(v):
    if isinstance(v, str) and v.startswith("TRIGSTR_"):
        return wts.get(int(v[8:]), v)
    return v

# All 34 Goblin abilities
abil_ids = [
    'A0AW', 'A0AV', 'A0A6', 'A0D6', 'A0AX', 'A0D2', 'A0Z4', 'A0D1', 'A0AB',
    'A0AR', 'A0A8', 'A0A7', 'A0A5', 'A0BL', 'A0A9', 'A1MT', 'A0LG', 'A0LF',
    'A0A4', 'A0D3', 'A0D4', 'Asds', 'A0AH', 'A0BK', 'A0AS', 'A0AT', 'A0AU',
    'A0KS', 'A0LD', 'A0LE', 'A0LH', 'S001', 'A15N', 'A0UU'
]

bulk = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(abil_ids)]))
objects = {o['id']: o for o in bulk.get('objects', [])}

for aid in abil_ids:
    obj = objects.get(aid)
    if not obj:
        print(f"[{aid}] MISSING!")
        continue
    f = obj.get('fields', {})
    code = f.get('code')
    name = resolve(f.get('name'))
    hotkey = f.get('hotkey')
    lvls = int(f.get('levels', '1'))
    print(f"\n=== [{aid}] (code={code}, lvls={lvls}, hotkey={hotkey}) {name} ===")
    for k in sorted(f.keys()):
        if k.startswith(('tip', 'ubertip', 'untip', 'unubertip', 'researchtip', 'researchubertip', 'name')):
            v = f[k]
            res_v = resolve(v)
            print(f"  {k}: {repr(v)} -> {repr(res_v)}")
