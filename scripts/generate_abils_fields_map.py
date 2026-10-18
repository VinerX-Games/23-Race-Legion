# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

abil_ids = [
    'A0AW', 'A0AV', 'A0A6', 'A0D6', 'A0AX', 'A0D2', 'A0Z4', 'A0D1', 'A0AB',
    'A0AR', 'A0A8', 'A0A7', 'A0A5', 'A0BL', 'A0A9', 'A1MT', 'A0LG', 'A0LF',
    'A0A4', 'A0D3', 'A0D4', 'Asds', 'A0AH', 'A0BK', 'A0AS', 'A0AT', 'A0AU',
    'A0KS', 'A0LD', 'A0LE', 'A0LH', 'S001', 'A15N', 'A0UU'
]
buff_ids = ['B028', 'B02H', 'B02I', 'B087', 'B02A', 'B02J', 'B02V', 'B02W', 'B089']

bulk_a = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(abil_ids)]))
bulk_b = require(cli(['get-objects-bulk', '--type', 'buff', '--ids', ','.join(buff_ids)]))

# Also read shared WTS keys
from audit_goblin_unit_abils_wts import shared_wts

mapping = {}

for obj in bulk_a.get('objects', []):
    aid = obj['id']
    f = obj['fields']
    mapping[aid] = {"type": "ability", "fields": {}}
    for k, v in f.items():
        if k.startswith(('name', 'tip', 'ubertip')) and not k.startswith(('research')):
            if isinstance(v, str) and v.startswith("TRIGSTR_"):
                wid = int(v[8:])
                mapping[aid]["fields"][k] = {
                    "raw": v,
                    "wts_id": wid,
                    "is_shared": wid in shared_wts
                }
            else:
                mapping[aid]["fields"][k] = {
                    "raw": v,
                    "wts_id": None,
                    "is_shared": True # inline, must be patched into skin
                }

for obj in bulk_b.get('objects', []):
    bid = obj['id']
    f = obj['fields']
    mapping[bid] = {"type": "buff", "fields": {}}
    for k in ['bufftip', 'buffubertip', 'name']:
        v = f.get(k)
        if v:
            if isinstance(v, str) and v.startswith("TRIGSTR_"):
                wid = int(v[8:])
                mapping[bid]["fields"][k] = {
                    "raw": v,
                    "wts_id": wid,
                    "is_shared": wid in shared_wts
                }
            else:
                mapping[bid]["fields"][k] = {
                    "raw": v,
                    "wts_id": None,
                    "is_shared": True
                }

Path(ROOT / "docs/ui_text/goblins_unit_abils_fields_map.json").write_text(
    json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Saved mapping to docs/ui_text/goblins_unit_abils_fields_map.json")
