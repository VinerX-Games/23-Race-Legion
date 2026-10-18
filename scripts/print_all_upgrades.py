# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / 'scripts/kultiras_raw_dump.json', encoding='utf-8'))

for up in d['upgrades']:
    if up['id'] == 'Rguv':
        continue
    uid = up['id']
    lvls = up['levels']
    print(f"=== Upgrade {uid} (levels: {lvls}) ===")
    for lvl in range(1, lvls + 1):
        name_obj = up['names'].get(f'name{lvl}', {})
        tip_obj = up['tips'].get(f'tip{lvl}', {})
        uber_obj = up['ubertips'].get(f'ubertip{lvl}', {})
        hotkey_obj = up['hotkeys'].get(f'hotkey{lvl}', {})
        print(f"  Level {lvl}:")
        print(f"    Name: {name_obj.get('val')} (raw: {name_obj.get('raw')})")
        print(f"    Tip: {tip_obj.get('val')} (raw: {tip_obj.get('raw')})")
        print(f"    Ubertip: {uber_obj.get('val')} (raw: {uber_obj.get('raw')})")
        print(f"    Hotkey: {hotkey_obj.get('val')} (raw: {hotkey_obj.get('raw')})")
