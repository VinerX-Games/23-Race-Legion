# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, resolve, extract_wts_id

bld_ids = ['h0JW', 'h0JX', 'h0JY', 'n04L', 'n055', 'nnfm', 'nnsa', 'nnsg', 'nntg', 'nntt']
hero_ids = ['H0JU', 'H0JV', 'H0OZ', 'N07A', 'N054']
worker_ids = ['nmpe']
unit_ids = ['n04Z', 'n050', 'n051', 'n052', 'n053', 'n054', 'n056', 'n057', 'n079', 'nmyr', 'nnmg', 'nnrg', 'nnsw', 'nwgs', 'nsnp', 'nhyc']

all_units = bld_ids + hero_ids + worker_ids + unit_ids

inspected_units = {}
all_abils = set()
all_upgs = set()

for uid in all_units:
    u = inspect_unit(uid)
    inspected_units[uid] = u
    # collect abilities
    for fld in ['abillist', 'heroabillist']:
        val = u.get(fld)
        if val:
            for a in str(val).split(','):
                a = a.strip()
                if a and a != '-':
                    all_abils.add(a)
    # collect builds
    # collect researches
    res = u.get('researches')
    if res:
        for r in str(res).split(','):
            r = r.strip()
            if r and r != '-':
                all_upgs.add(r)
    # collect upgrades
    upg = u.get('upgrades')
    if upg:
        for r in str(upg).split(','):
            r = r.strip()
            if r and r != '-':
                all_upgs.add(r)

print(f"Total units inspected: {len(inspected_units)}")
print("Collected Researches/Upgrades:", sorted(list(all_upgs)))
print("Collected Abilities:", sorted(list(all_abils)))

# Let's inspect all collected upgrades
inspected_upgs = {}
for uid in sorted(list(all_upgs)):
    upg_data = inspect_upgrade(uid)
    inspected_upgs[uid] = upg_data
    # print summary
    print(f"UPGRADE {uid}: name1={upg_data['names'].get('name1', {}).get('val')} (sid={upg_data['names'].get('name1', {}).get('sid')}) levels={upg_data['levels']}")

