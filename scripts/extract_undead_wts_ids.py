# -*- coding: utf-8 -*-
import json
from pathlib import Path

inv = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))

# Collect all sids
cat_sids = {}
for cat, objs in inv.items():
    cat_sids[cat] = {}
    for oid, odata in objs.items():
        sids = {k: v['sid'] for k, v in odata['fields'].items() if v['sid']}
        cat_sids[cat][oid] = sids

out_file = Path('scripts/undead_sids_by_object.json')
out_file.write_text(json.dumps(cat_sids, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved to {out_file}")

total_sids = sum(len(sids) for cat in cat_sids.values() for sids in cat.values())
unique_sids = len(set(sid for cat in cat_sids.values() for sids in cat.values() for sid in sids.values()))
print(f"Total SID references: {total_sids}, Unique SIDs: {unique_sids}")
