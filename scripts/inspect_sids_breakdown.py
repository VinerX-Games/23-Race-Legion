# -*- coding: utf-8 -*-
import json
import sys

data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))

print("=== UPGRADES SIDS BREAKDOWN ===")
total_upg_sids = 0
for up in data['upgrades']:
    sids = []
    for k in ['names', 'tips', 'ubertips']:
        for subk, subv in up.get(k, {}).items():
            if isinstance(subv, dict) and subv.get('sid'):
                sids.append((subk, subv['sid'], subv.get('val')))
    print(f"{up['id']} (levels={up.get('levels')}): {len(sids)} sids")
    total_upg_sids += len(sids)
print(f"Total upgrade sids: {total_upg_sids}")

print("\n=== ABILITIES SIDS BREAKDOWN ===")
total_ab_sids = 0
for ab in data['abilities']:
    sids = []
    for k in ['name_sid', 'researchtip_sid', 'researchubertip_sid', 'untip_sid', 'unubertip_sid']:
        if ab.get(k):
            sids.append((k, ab[k]))
    for k in ['tips', 'ubertips']:
        for subk, subv in ab.get(k, {}).items():
            if isinstance(subv, dict) and subv.get('sid'):
                sids.append((subk, subv['sid']))
    if sids:
        print(f"{ab['id']} (levels={ab.get('levels')}): {len(sids)} sids")
    total_ab_sids += len(sids)
print(f"Total ability sids: {total_ab_sids}")
