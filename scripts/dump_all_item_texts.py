# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_hivewe import load_wts_strings

wts = load_wts_strings()

with open('scripts/custom_items_dump.json', 'r', encoding='utf-8') as f:
    dump = json.load(f)

result = {}
for cid, d in sorted(dump.items()):
    tip = d.get('tip_raw')
    uber = d.get('ubertip_raw')
    desc = d.get('desc_raw')
    if tip and str(tip).startswith('TRIGSTR_'):
        sid = int(tip[8:])
        u_sid = int(uber[8:]) if uber and str(uber).startswith('TRIGSTR_') else None
        d_sid = int(desc[8:]) if desc and str(desc).startswith('TRIGSTR_') else None
        result[cid] = {
            'tip_sid': sid,
            'tip_orig': wts.get(sid, ''),
            'uber_sid': u_sid,
            'uber_orig': wts.get(u_sid, '') if u_sid else '',
            'desc_sid': d_sid,
            'desc_orig': wts.get(d_sid, '') if d_sid else '',
            'gold': d.get('gold'),
            'lumber': d.get('lumber')
        }

with open('scripts/items_detailed_catalog.json', 'w', encoding='utf-8') as out:
    json.dump(result, out, ensure_ascii=False, indent=2)

print(f'Wrote {len(result)} items to scripts/items_detailed_catalog.json')
