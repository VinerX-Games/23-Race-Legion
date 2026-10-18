# -*- coding: utf-8 -*-
import json
from pathlib import Path

inv = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))

# Let's count how many WTS strings need updates
sids_to_update = {}

for cat, objs in inv.items():
    for oid, odata in objs.items():
        for fld, finfo in odata['fields'].items():
            sid = finfo['sid']
            if not sid: continue
            cur = finfo['current_val']
            # hotkey strings like 'Q', 'W' do not need update
            if fld.startswith('hotkey') or fld.startswith('researchhotkey'):
                continue
            sids_to_update[sid] = (cat, oid, fld, cur)

print(f"Total non-hotkey WTS strings across Undead: {len(sids_to_update)}")

by_cat = {}
for sid, (cat, oid, fld, cur) in sids_to_update.items():
    by_cat.setdefault(cat, []).append((sid, oid, fld, cur))

for cat, lst in by_cat.items():
    print(f"  {cat}: {len(lst)} strings")
