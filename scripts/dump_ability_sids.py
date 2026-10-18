# -*- coding: utf-8 -*-
import json
from pathlib import Path

inv = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))

print("=== HERO ABILITIES SIDS ===")
for aid, data in inv['hero_abilities'].items():
    sids = {k: v['sid'] for k, v in data['fields'].items() if v['sid'] and not k.startswith('hotkey') and not k.startswith('researchhotkey')}
    print(f"[{aid}] (lvls={data['levels']}): {sids}")

print("\n=== UNIT ABILITIES SIDS ===")
for aid, data in inv['unit_abilities'].items():
    sids = {k: v['sid'] for k, v in data['fields'].items() if v['sid'] and not k.startswith('hotkey') and not k.startswith('researchhotkey')}
    print(f"[{aid}] (lvls={data['levels']}): {sids}")
