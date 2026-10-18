# -*- coding: utf-8 -*-
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wc3_object_tools import cli, require

bld_ids = ['h070', 'h077', 'h073', 'h074', 'h075', 'h076', 'h079', 'h07S', 'o016', 'h0D7']
bulk = require(cli(['get-objects-bulk', '--type', 'unit', '--ids', ','.join(bld_ids)]))

print("=== CHECKING BUILDING ITEMS ===")
for obj in bulk.get('objects', []):
    bid = obj['id']
    name = obj.get('name')
    sell = obj['fields'].get('sellitems', '')
    make = obj['fields'].get('makeitems', '')
    if sell or make:
        print(f"[{bid}] {name}: sellitems={sell}, makeitems={make}")
    else:
        print(f"[{bid}] {name}: no items")

print("\n=== CHECKING LUA MESSAGES IN GOBLINS TRIGGERS ===")
goblin_trigger = ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Goblins.lua"
if goblin_trigger.exists():
    text = goblin_trigger.read_text(encoding="utf-8")
    for match in re.finditer(r'(Display(?:Timed)?TextTo(?:Player|Force)\s*\([^)]*\))', text):
        print(f"Message call: {match.group(1)}")
    # Also check other message functions
    for match in re.finditer(r'(BJDebugMsg\s*\([^)]*\))', text):
        print(f"Debug call: {match.group(1)}")
    # Check if any string literals contain text displayed to player
    for line in text.splitlines():
        if any(k in line for k in ['DisplayText', 'DisplayTimedText', 'CreateQuest', 'CreateLeaderboard', 'DialogAddButton']):
            print(f"UI line: {line.strip()}")

print("\n=== CHECKING CORRUPTION / ECONOMY TRIGGERS FOR MESSAGES ===")
eco_trigger = ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/01_core_economy.lua"
if eco_trigger.exists():
    text = eco_trigger.read_text(encoding="utf-8")
    for line in text.splitlines():
        if 'A0AS' in line or 'A0AT' in line or 'R04N' in line or 'R0D4' in line:
            if 'Display' in line or 'print' in line:
                print(f"Eco message line: {line.strip()}")
