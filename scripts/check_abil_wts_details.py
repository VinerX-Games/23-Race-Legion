# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

print(f"Total abilities in dump: {len(d['abilities'])}")
wts_abils = []
no_wts_abils = []
for a in d['abilities']:
    aid = a['id']
    sids = []
    if a.get('name_sid'): sids.append(('name', a['name_sid']))
    if a.get('researchtip_sid'): sids.append(('rtip', a['researchtip_sid']))
    if a.get('researchubertip_sid'): sids.append(('rub', a['researchubertip_sid']))
    for k, v in a.get('tips', {}).items():
        if v.get('sid'): sids.append((k, v['sid']))
    for k, v in a.get('ubertips', {}).items():
        if v.get('sid'): sids.append((k, v['sid']))
    if sids:
        wts_abils.append((aid, a['name'], sids))
    else:
        no_wts_abils.append((aid, a['name']))

print(f"\nAbilities with WTS strings ({len(wts_abils)}):")
for aid, name, sids in wts_abils:
    print(f"  {aid} ({name}): {[s[1] for s in sids]}")

print(f"\nAbilities WITHOUT WTS strings ({len(no_wts_abils)}):")
for aid, name in no_wts_abils:
    print(f"  {aid} ({name})")
