# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

raw_json = Path(ROOT / "docs/ui_text/goblins_unit_abils_raw.json")
data = json.loads(raw_json.read_text(encoding="utf-8"))

# Load all units and buildings
res_u = require(cli(['get-objects-bulk', '--type', 'unit', '--count', '1000']))
units = res_u.get('objects', [])

abil_to_units = {}
for u in units:
    uid = u['id']
    uname = u.get('name', '')
    abils = u['fields'].get('abillist', '').split(',')
    for a in abils:
        a = a.strip()
        if not a: continue
        if a not in abil_to_units:
            abil_to_units[a] = []
        abil_to_units[a].append((uid, uname))

print(f"Total abilities to analyze: {len(data)}\n")
for aid in data.keys():
    users = abil_to_units.get(aid, [])
    user_str = ", ".join([f"{uid} ({uname})" for uid, uname in users[:5]])
    if len(users) > 5:
        user_str += f" and {len(users) - 5} more"
    print(f"[{aid}] used by {len(users)} units/blds: {user_str}")
