# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

res_items = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', 'item', '--warcraft', str(hw.DEFAULT_WARCRAFT)])
objects = res_items.get('objects', [])
print(f"Total custom/modified items: {len(objects)}")
for obj in objects:
    oid = obj.get('id')
    f = obj.get('fields', {})
    name = res(f.get('name', ''))
    tip = res(f.get('tip', ''))
    ubertip = res(f.get('ubertip', ''))
    desc = res(f.get('description', ''))
    abils = f.get('abillist', '')
    print(f"{oid}: name='{name}', tip='{tip}', abils='{abils}'")
