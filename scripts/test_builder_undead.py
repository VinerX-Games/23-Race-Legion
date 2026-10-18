# -*- coding: utf-8 -*-
"""Draft and validate Undead plan generator."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

inv = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))
wts_raw = Path('map.w3x/war3map.wts').read_text(encoding='utf-8')

def check_wts_has(sid):
    pattern = rf"STRING 0*{sid}\s*\{{\s*\r?\n"
    return bool(re.search(pattern, wts_raw))

print("Checking sample SIDs in WTS...")
print("A0HV name (38877):", check_wts_has(38877))
print("n014 name (8527):", check_wts_has(8527))
