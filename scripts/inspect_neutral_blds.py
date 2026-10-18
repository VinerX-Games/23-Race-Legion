# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_object_tools import snapshot
from wc3_hivewe import load_wts_strings, clean_wc3_string

wts = load_wts_strings()
snap = snapshot('map.w3x', fields='name,tip,ubertip,propernames')
units = snap['unit']

neutral_bld_ids = [
    'n01L', 'n01M', 'n01N', 'n02J', 'n02K', 'n02L', 'n04E',
    'n01C', 'n04K',
    'n001', 'n003', 'n006', 'n00W', 'n01B', 'n01D', 'n01Y', 'n01Z', 'n04O', 'n060', 'n065',
    'h0LH', 'h0F5', 'h0CA',
    'h0L6', 'h0L7', 'h0L8', 'h0L9', 'h0LA', 'h0LB', 'h0LC', 'h0LE', 'h0LF', 'h0LG',
    'h0LI', 'h0LJ', 'h0LK', 'h0LL', 'h0LM', 'h0LN', 'h0LO', 'h0LP', 'h0LQ', 'h0LR', 'h0LS', 'h0LV', 'h0M0', 'h0M1', 'h0MH', 'h0P1',
    'h0PA', 'h0PC', 'h0PD', 'h0PE', 'h0PF', 'h0PG'
]

print(f'Checking {len(neutral_bld_ids)} neutral/common objects:')
for uid in neutral_bld_ids:
    f = units.get(uid, {}).get('fields', {})
    name_raw = f.get('name')
    tip_raw = f.get('tip')
    uber_raw = f.get('ubertip')
    def resolve(v):
        if not v: return 'None'
        if str(v).startswith('TRIGSTR_'):
            sid = int(v[8:])
            return f"{v} -> '{clean_wc3_string(wts.get(sid, ''))}'"
        return repr(v)
    print(f"{uid}: name={resolve(name_raw)} | tip={resolve(tip_raw)} | uber={resolve(uber_raw)[:80]}")
