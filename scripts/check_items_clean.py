# -*- coding: utf-8 -*-
import json
import re

with open('scripts/items_detailed_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

def clean_title(title):
    t = re.sub(r'\|c[0-9a-fA-F]{8}', '', title)
    t = t.replace('|r', '').replace('|R', '').strip()
    if t.lower().startswith('купить'):
        t = t[6:].strip()
    return t

print(f"{'ID':<6} | {'Abils':<16} | {'Clean Title'}")
print("-" * 50)
for cid, d in sorted(catalog.items()):
    ct = clean_title(d['tip_orig'])
    abils = d.get('abillist') or 'None'
    print(f"{cid:<6} | {abils:<16} | {ct}")
