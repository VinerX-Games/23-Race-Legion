# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
d2 = json.load(open('scripts/bandits_abils_upgrades_dump.json', encoding='utf-8'))
for aid in ['A01J', 'A01D', 'A01H', 'A01I', 'A023']:
    a = d2['abils'].get(aid)
    if not a:
        print(f"MISSING {aid}")
        continue
    print(f"=== {aid}: {a.get('name')} (levels={a.get('levels')}, hotkey={a.get('hotkey')}) ===")
    print(f"  raw_name: {a.get('raw_name')}")
    print(f"  researchhotkey: {a.get('researchhotkey')} raw: {a.get('raw_researchhotkey')}")
    print(f"  researchtip: {a.get('researchtip')} raw: {a.get('raw_researchtip')}")
    print(f"  researchubertip: {a.get('researchubertip')} raw: {a.get('raw_researchubertip')}")
    for k, v in a.get('tips', {}).items():
        print(f"  {k}: {v.get('val')} (raw={v.get('raw')})")
    for k, v in a.get('ubertips', {}).items():
        print(f"  {k}: {v.get('val')} (raw={v.get('raw')})")
