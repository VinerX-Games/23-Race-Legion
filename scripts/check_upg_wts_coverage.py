# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

print(f"Total upgrades in dump: {len(d['upgrades'])}")
all_upg_sids = {}
for u in d['upgrades']:
    uid = u['id']
    lvls = u['levels']
    sids = []
    for i in range(1, lvls+1):
        if f'name{i}' in u['names'] and u['names'][f'name{i}'].get('sid'):
            sids.append(('name', i, u['names'][f'name{i}']['sid']))
        if f'tip{i}' in u['tips'] and u['tips'][f'tip{i}'].get('sid'):
            sids.append(('tip', i, u['tips'][f'tip{i}']['sid']))
        if f'ubertip{i}' in u['ubertips'] and u['ubertips'][f'ubertip{i}'].get('sid'):
            sids.append(('ubertip', i, u['ubertips'][f'ubertip{i}']['sid']))
    all_upg_sids[uid] = sids

print(f"Upgrades with WTS: {sum(1 for s in all_upg_sids.values() if s)} / {len(d['upgrades'])}")
for uid, sids in all_upg_sids.items():
    if not sids:
        print(f"  NO WTS: {uid}")
