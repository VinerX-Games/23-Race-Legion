# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, resolve

units = ['o03W', 'o03F', 'o03G', 'o03H', 'o03I', 'o03K', 'o03L', 'o03M', 'o03N', 'o03O', 'o03P', 'o03Q', 'o03R', 'o03S', 'o03T', 'o03U', 'o03V']
heroes = ['N05J', 'N05K', 'N05L']

print('=== HEROES ===')
all_hero_abils = set()
for hid in heroes:
    h = inspect_unit(hid)
    name = h.get('name')
    proper = h.get('propernames')
    habils = h.get('heroabillist')
    abils = h.get('abillist')
    print(f"{hid}: {name} (proper: {proper})")
    print(f"  heroabils: {habils}")
    print(f"  abils: {abils}")
    if habils:
        for a in habils.split(','):
            all_hero_abils.add(a.strip())
    if abils:
        for a in abils.split(','):
            all_hero_abils.add(a.strip())

print('\n=== UNITS ===')
all_unit_abils = set()
all_unit_upgs = set()
for uid in units:
    u = inspect_unit(uid)
    name = u.get('name')
    tip = u.get('tip')
    hk = u.get('hotkey')
    abils = u.get('abillist')
    upgs = u.get('upgrades')
    print(f"{uid}: {name} (tip: {tip}, hotkey: {hk})")
    print(f"  abils: {abils}, upgs: {upgs}")
    if abils:
        for a in abils.split(','):
            if a.strip():
                all_unit_abils.add(a.strip())
    if upgs:
        for up in upgs.split(','):
            if up.strip():
                all_unit_upgs.add(up.strip())

print('\nAll hero abils:', sorted(list(all_hero_abils)))
print('All unit abils:', sorted(list(all_unit_abils)))
print('All unit upgrades:', sorted(list(all_unit_upgs)))
