# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wc3_object_tools import cli, require

bld_ids = ['h070', 'h077', 'h073', 'h074', 'h075', 'h076', 'h079', 'h07S', 'o016', 'h0D7']
unit_ids = ['n00V', 'h06K', 'h06L', 'h06M', 'h06N', 'h06O', 'h06Q', 'h078', 'h07R', 'h06S', 'h06U', 'h06Y', 'h06Z', 'h06R', 'h06T', 'o00W', 'o00Y', 'o00X', 'h06P', 'h06X', 'h06V', 'h06W', 'h0DM', 'h0OD']

all_ids = bld_ids + unit_ids
bulk = require(cli(['get-objects-bulk', '--type', 'unit', '--ids', ','.join(all_ids)]))

found_abils = set()
for obj in bulk.get('objects', []):
    uid = obj['id']
    name = obj.get('name', '')
    abils = [a.strip() for a in obj['fields'].get('abillist', '').split(',') if a.strip()]
    auto_abils = [a.strip() for a in obj['fields'].get('auto', '').split(',') if a.strip()]
    all_obj_abils = abils + auto_abils
    found_abils.update(all_obj_abils)
    print(f"[{uid}] {name}: abillist={abils}, auto={auto_abils}")

print(f"\nTotal unique abilities found on Goblin units & buildings: {len(found_abils)}")
print(sorted(list(found_abils)))
