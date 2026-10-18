# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_ability, inspect_buff, resolve

hero_abils = [
    'A16Y', 'A170', 'A175', 'A171',
    'A173', 'A172', 'A174',
    'A16V', 'A16U', 'A16X', 'A16W'
]

print("=== HERO ABILITIES ===")
for aid in hero_abils:
    a = inspect_ability(aid)
    print(f"\nHero Ability {aid}: '{a.get('name')}' (raw: {a.get('raw_name')}) lvls={a.get('levels')}")
    print(f"  hotkey: raw={a.get('raw_hotkey')} -> '{a.get('hotkey')}'")
    print(f"  researchhotkey: raw={a.get('raw_researchhotkey')} -> '{a.get('researchhotkey')}'")
    print(f"  researchtip: raw={a.get('raw_researchtip')} -> '{a.get('researchtip')}'")
    print(f"  researchubertip: raw={a.get('raw_researchubertip')} -> '{a.get('researchubertip')}'")
    for lvl in range(1, a.get('levels', 1) + 1):
        tip = a['tips'].get(f'tip{lvl}', {})
        ub = a['ubertips'].get(f'ubertip{lvl}', {})
        print(f"  L{lvl}: tip: raw={tip.get('raw')} -> '{tip.get('val')}'")
        print(f"       ub: raw={ub.get('raw')} -> '{ub.get('val')}'")

unit_abils = [
    'A176', 'A177', 'A178', 'A179', 'A17A', 'A17B', 'A17C', 'A17D',
    'A17E', 'A17F', 'A17G', 'A17H', 'A17I', 'A17K', 'A17L', 'A17M',
    'A17O', 'A1R6', 'A1R7', 'A1R8', 'A1RA', 'A0WU'
]

print("\n=== UNIT ABILITIES ===")
for aid in unit_abils:
    a = inspect_ability(aid)
    print(f"\nUnit Ability {aid}: '{a.get('name')}' (raw: {a.get('raw_name')}) lvls={a.get('levels')}")
    print(f"  hotkey: raw={a.get('raw_hotkey')} -> '{a.get('hotkey')}'")
    for lvl in range(1, a.get('levels', 1) + 1):
        tip = a['tips'].get(f'tip{lvl}', {})
        ub = a['ubertips'].get(f'ubertip{lvl}', {})
        print(f"  L{lvl}: tip: raw={tip.get('raw')} -> '{tip.get('val')}'")
        print(f"       ub: raw={ub.get('raw')} -> '{ub.get('val')}'")
