# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / 'scripts/kultiras_raw_dump.json', encoding='utf-8'))
for uid in ['R0KL', 'R0H4', 'kt01', 'R027', 'R02S']:
    up = [u for u in d['upgrades'] if u['id'] == uid][0]
    print(f"=== {uid} ===")
    for i in range(1, up['levels'] + 1):
        print(f"  Level {i}:")
        print(f"    name: {up['names'].get(f'name{i}')}")
        print(f"    tip: {up['tips'].get(f'tip{i}')}")
        print(f"    ubertip: {up['ubertips'].get(f'ubertip{i}')}")
        print(f"    hotkey: {up['hotkeys'].get(f'hotkey{i}')}")
