# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, resolve

bld_ids = ['o035', 'o03D', 'o03E', 'o036', 'o037', 'o038', 'o03A', 'o039', 'o03J', 'o03C', 'o03B']
unit_ids = [
    'o03W', 'o03F', 'o03G', 'o03H', 'o03I', 'o03K', 'o03L', 'o03M',
    'o03N', 'o03O', 'o03P', 'o03Q', 'o03R', 'o03S', 'o03T', 'o03U', 'o03V'
]
hero_ids = ['N05J', 'N05K', 'N05L']

all_abils = set()
for b in bld_ids:
    u = inspect_unit(b)
    if u.get('abillist'):
        for a in u['abillist'].split(','):
            if a.strip(): all_abils.add(a.strip())

for uid in unit_ids:
    u = inspect_unit(uid)
    if u.get('abillist'):
        for a in u['abillist'].split(','):
            if a.strip(): all_abils.add(a.strip())

for hid in hero_ids:
    u = inspect_unit(hid)
    if u.get('heroabillist'):
        for a in u['heroabillist'].split(','):
            if a.strip(): all_abils.add(a.strip())
    if u.get('abillist'):
        for a in u['abillist'].split(','):
            if a.strip(): all_abils.add(a.strip())

print(f"Total abilities to inspect: {len(all_abils)}")
print("Abilities:", sorted(list(all_abils)))

all_buffs = set()
for aid in sorted(list(all_abils)):
    a = inspect_ability(aid)
    print(f"\nAbility {aid}: name='{a.get('name')}', lvls={a.get('levels')}, hk='{a.get('hotkey')}'")
    for lvl, tip in a.get('tips', {}).items():
        print(f"  {lvl}: tip='{tip.get('val')}' (sid={tip.get('sid')})")
    for lvl, ub in a.get('ubertips', {}).items():
        print(f"  {lvl}: ubertip='{ub.get('val')}' (sid={ub.get('sid')})")
    if a.get('researchtip'):
        print(f"  researchtip='{a.get('researchtip')}' (sid={a.get('researchtip_sid')})")
    if a.get('researchubertip'):
        print(f"  researchubertip='{a.get('researchubertip')}' (sid={a.get('researchubertip_sid')})")
    # check buff fields in raw fields
    for k, v in a['fields'].items():
        if 'buff' in k.lower():
            print(f"    field {k} = {v}")
            if isinstance(v, str) and len(v) == 4:
                all_buffs.add(v)

print(f"\nDiscovered buffs: {sorted(list(all_buffs))}")
