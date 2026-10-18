# -*- coding: utf-8 -*-
"""Inspect hero abilities of Night Elf."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
dump = json.loads((ROOT / 'scripts/nightelf_raw_dump.json').read_text(encoding='utf-8'))

hero_aids = ['A0FJ', 'A0FH', 'A0FI', 'ken0', 'A0FL', 'A0FQ']
for ab in dump['abilities']:
    if ab['id'] in hero_aids:
        print(f"=== {ab['id']} ({ab['name']}) [levels: {ab['levels']}] ===")
        print(f"  raw_name: {ab.get('raw_name')}")
        print(f"  hotkey: {ab.get('hotkey')}")
        for i in range(1, ab['levels'] + 1):
            t = ab['tips'].get(f'tip{i}', {})
            ub = ab['ubertips'].get(f'ubertip{i}', {})
            print(f"  L{i} tip: [{t.get('raw')}] {t.get('val')}")
            print(f"  L{i} ub: [{ub.get('raw')}] {ub.get('val')}")
        print()
