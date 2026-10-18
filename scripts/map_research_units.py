# -*- coding: utf-8 -*-
import json
from pathlib import Path

inv = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))

# Map each research to list of units that have it in 'upgrades'
res_to_units = {}

for cat in ['units', 'heroes']:
    for uid, udata in inv[cat].items():
        upgs = udata.get('upgrades')
        if upgs:
            for r in upgs.split(','):
                r = r.strip()
                res_to_units.setdefault(r, []).append((uid, udata['fields'].get('name', {}).get('current_val', uid)))

print("=== RESEARCH APPLIES_TO BASED ON UNIT UPGRADES ===")
for r, ulist in sorted(res_to_units.items()):
    print(f"\n[{r}] affects {len(ulist)} units:")
    for uid, uname in ulist:
        print(f"  - {uid}: {uname}")
