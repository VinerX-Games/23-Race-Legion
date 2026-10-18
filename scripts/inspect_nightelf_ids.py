# -*- coding: utf-8 -*-
"""Inspect ability and upgrade IDs to see which are unique to Night Elf vs shared."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
dump = json.loads((ROOT / 'scripts/nightelf_raw_dump.json').read_text(encoding='utf-8'))

print("=== ABILITIES IN NIGHT ELF ===")
for ab in dump['abilities']:
    aid = ab['id']
    name = ab.get('name')
    tips = [t.get('val') for t in ab.get('tips', {}).values() if t.get('val')]
    has_wts = any(isinstance(t.get('raw'), str) and t.get('raw').startswith('TRIGSTR_') for t in ab.get('tips', {}).values())
    if has_wts or (isinstance(ab.get('raw_name'), str) and ab.get('raw_name').startswith('TRIGSTR_')):
        print(f"  {aid}: {name} (tips: {len(tips)}) | raw_name={ab.get('raw_name')}")

print("\n=== UPGRADES IN NIGHT ELF ===")
for upg in dump['upgrades']:
    uid = upg['id']
    n1 = upg['names'].get('name1', {}).get('val')
    has_wts = any(isinstance(t.get('raw'), str) and t.get('raw').startswith('TRIGSTR_') for t in upg.get('tips', {}).values())
    print(f"  {uid}: {n1} (levels: {upg['levels']}) | has_wts={has_wts}")
