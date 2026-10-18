# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_object_tools import snapshot
from wc3_hivewe import load_wts_strings, clean_wc3_string

wts = load_wts_strings()
snap = snapshot('map.w3x', fields='name,tip,ubertip,description,abillist,goldcost,lumbercost')
items = snap['item']

with open('scripts/items_detailed_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

for cid in sorted(catalog):
    item_data = items.get(cid, {})
    f = item_data.get('fields', {})
    catalog[cid]['abillist'] = f.get('abillist', '')

with open('scripts/items_detailed_catalog.json', 'w', encoding='utf-8') as out:
    json.dump(catalog, out, ensure_ascii=False, indent=2)

print('Updated catalog with abillist')
