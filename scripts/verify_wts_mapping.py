# -*- coding: utf-8 -*-
import json
import re

audit = json.loads(open('docs/ui_text/dragon_hero_abils_audit.json', encoding='utf-8').read())
script_txt = open('scripts/update_dragon_hero_abils.py', encoding='utf-8').read()

mismatches = []
missing = []

for aid, data in audit.items():
    m = re.search(rf'\"id\":\s*\"{aid}\"[\s\S]*?\"wts\":\s*\{{([^}}]*)\}}', script_txt)
    wts_block = m.group(1) if m else ""
    for f, finfo in data['fields'].items():
        if finfo['is_wts']:
            expected_wid = finfo['wts_id']
            fm = re.search(rf'\"{f}\":\s*(\d+)', wts_block)
            if fm:
                script_wid = int(fm.group(1))
                if script_wid != expected_wid:
                    mismatches.append((aid, f, script_wid, expected_wid))
            else:
                missing.append((aid, f, expected_wid))

print(f"Mismatches: {len(mismatches)}")
for m in mismatches:
    print(f"  {m[0]}.{m[1]}: script={m[2]} audit={m[3]}")

print(f"Missing: {len(missing)}")
for m in missing:
    print(f"  {m[0]}.{m[1]}: audit={m[2]}")
