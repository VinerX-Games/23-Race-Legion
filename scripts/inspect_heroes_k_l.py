# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_ability

for aid in ['A173', 'A172', 'A174', 'A16V', 'A16U', 'A16X', 'A16W']:
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
