# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_hivewe import load_wts_strings, clean_wc3_string

wts = load_wts_strings()

with open('scripts/custom_items_dump.json', 'r', encoding='utf-8') as f:
    dump = json.load(f)

print(f'Total custom items: {len(dump)}')
for cid, d in sorted(dump.items()):
    tip = d.get('tip_raw')
    uber = d.get('ubertip_raw')
    desc = d.get('desc_raw')
    if tip and str(tip).startswith('TRIGSTR_'):
        sid = int(tip[8:])
        tip_text = clean_wc3_string(wts.get(sid, ''))
        uber_sid = int(uber[8:]) if uber and str(uber).startswith('TRIGSTR_') else None
        uber_text = clean_wc3_string(wts.get(uber_sid, '')) if uber_sid else ''
        desc_sid = int(desc[8:]) if desc and str(desc).startswith('TRIGSTR_') else None
        print(f'{cid} | tip_sid={sid}: {tip_text!r} | uber_sid={uber_sid}: {uber_text[:60]!r}')
