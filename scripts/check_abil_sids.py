# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "scripts/silitids_raw_dump.json", encoding="utf-8"))

nerub_plan = json.load(open(ROOT / "docs/ui_text/nerubs_plan.json", encoding="utf-8"))
nerub_sids = set(int(k) for k in nerub_plan["wts_updates"].keys())

print("=== Silitid Abilities with WTS string IDs ===")
for a in data['abilities']:
    ab_sids = []
    if a.get('name_sid'): ab_sids.append(('name', a['name_sid']))
    if a.get('researchtip_sid'): ab_sids.append(('rtip', a['researchtip_sid']))
    if a.get('researchubertip_sid'): ab_sids.append(('rub', a['researchubertip_sid']))
    for lvl, d in a.get('tips', {}).items():
        if d.get('sid'): ab_sids.append((lvl, d['sid']))
    for lvl, d in a.get('ubertips', {}).items():
        if d.get('sid'): ab_sids.append((f'ub_{lvl}', d['sid']))
    
    # Filter out Nerub sids
    clean_sids = [s for s in ab_sids if s[1] not in nerub_sids]
    if clean_sids:
        print(f"[{a['id']}] {a['name']} ({len(clean_sids)} sids): {clean_sids}")
