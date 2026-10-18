# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

upg_to_units = {}
all_units = d['workers'] + d['units'] + d['heroes']
for u in all_units:
    upgs = u.get('upgrades')
    if upgs:
        for upg_id in upgs.split(','):
            upg_id = upg_id.strip()
            if upg_id:
                upg_to_units.setdefault(upg_id, []).append(f"{u['name']} ({u['id']})")

for u in d['upgrades']:
    uid = u['id']
    units = upg_to_units.get(uid, [])
    print(f"[{uid}] {u['names']['name1']['val']} -> Units: {units}")
