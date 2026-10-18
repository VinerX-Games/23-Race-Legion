# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / 'scripts/hordew2_raw_dump.json', encoding='utf-8'))

with open(ROOT / 'scripts/hordew2_upgrades_inspect.txt', 'w', encoding='utf-8') as f:
    for up in data['upgrades']:
        f.write(f"=== UPGRADE {up['id']} (levels: {up.get('levels')}) ===\n")
        for k in ['names', 'tips', 'ubertips']:
            f.write(f"  {k}:\n")
            for lvl, val in up.get(k, {}).items():
                f.write(f"    {lvl}: sid={val.get('sid')} raw={val.get('raw')} val={repr(val.get('val'))}\n")
        f.write("\n")

with open(ROOT / 'scripts/hordew2_abilities_inspect.txt', 'w', encoding='utf-8') as f:
    for ab in data['abilities']:
        f.write(f"=== ABILITY {ab['id']} ({ab.get('name')}) levels: {ab.get('levels')} ===\n")
        f.write(f"  raw_name: {ab.get('raw_name')}\n")
        f.write(f"  researchtip: sid={ab.get('raw_researchtip')} val={repr(ab.get('researchtip'))}\n")
        f.write(f"  researchubertip: sid={ab.get('raw_researchubertip')} val={repr(ab.get('researchubertip'))}\n")
        for k in ['tips', 'ubertips']:
            f.write(f"  {k}:\n")
            for lvl, val in ab.get(k, {}).items():
                f.write(f"    {lvl}: sid={val.get('sid')} raw={val.get('raw')} val={repr(val.get('val'))}\n")
        f.write("\n")

print("Wrote hordew2_upgrades_inspect.txt and hordew2_abilities_inspect.txt")
