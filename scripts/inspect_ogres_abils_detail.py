# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_ability, inspect_unit, resolve

all_abils = [
    'A16U', 'A16V', 'A16W', 'A16X', 'A16Y', 'A170', 'A171', 'A172', 'A173', 'A174', 'A175',
    'A176', 'A177', 'A178', 'A179', 'A17A', 'A17B', 'A17C', 'A17D', 'A17E', 'A17F', 'A17G',
    'A17H', 'A17I', 'A17K', 'A17L', 'A17M', 'A17O', 'A1R6', 'A1R7', 'A1R8', 'A1RA', 'A0WU'
]

for aid in all_abils:
    a = inspect_ability(aid)
    print(f"\n=== Ability {aid}: '{a.get('name')}' (raw: {a.get('raw_name')}) ===")
    print(f"  code={a['fields'].get('code')}, lvls={a.get('levels')}, hk={a.get('hotkey')}")
    print(f"  researchtip='{a.get('researchtip')}'")
    print(f"  researchubertip='{a.get('researchubertip')}'")
    for k, v in sorted(a['fields'].items()):
        if any(w in k.lower() for w in ['unit', 'summon', 'buff', 'tip', 'target', 'order', 'dmg', 'data']):
            print(f"    {k} = {v} -> {resolve(v)}")
