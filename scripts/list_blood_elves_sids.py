# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / 'scripts/blood_elves_raw_dump.json', encoding='utf-8') as f:
    d = json.load(f)

for cat in ['buildings', 'units', 'heroes']:
    print(f'=== {cat.upper()} ===')
    for item in d[cat]:
        print(f"{item['id']}: name={item['raw_name']}, tip={item['raw_tip']}, ubt={item['raw_ubertip']}, hk={item['raw_hotkey']}")

print('=== UPGRADES ===')
for u in d['upgrades']:
    s = f"{u['id']}: "
    for k in u['names']:
        s += f"{k}={u['names'][k].get('raw')} "
    for k in u['tips']:
        s += f"{k}={u['tips'][k].get('raw')} "
    for k in u['ubertips']:
        s += f"{k}={u['ubertips'][k].get('raw')} "
    print(s)

print('=== ABILITIES ===')
for a in d['abilities']:
    s = f"{a['id']}: name={a['raw_name']} hk={a['raw_hotkey']} "
    for k in a['tips']:
        s += f"{k}={a['tips'][k].get('raw')} "
    for k in a['ubertips']:
        s += f"{k}={a['ubertips'][k].get('raw')} "
    if a.get('raw_researchtip'):
        s += f"rtip={a.get('raw_researchtip')} rubt={a.get('raw_researchubertip')} "
    print(s)
