# -*- coding: utf-8 -*-
"""Inspect all Silitids race objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_race_base as ib
import wc3_hivewe as hw

def main():
    print("=== INSPECTING SILITIDS (RACE 22) OBJECTS ===")

    # 1. Selection
    selection_ability = ib.inspect_ability('A0J7')
    selection_markers = [ib.inspect_upgrade('R0BV')]

    # 2. Buildings (16)
    bld_ids = [
        'e01H', 'e021', 'e020', 'e01I', 'e01J', 'e01K', 'e01L', 'e01M',
        'e01X', 'e00B', 'h00C', 'o015', 'o017', 'h08L', 'h0MG', 'h0DL'
    ]
    bld_data = [ib.inspect_unit(b) for b in bld_ids]

    # 3. Units (16)
    unit_ids = [
        'e01G', 'e01N', 'e01O', 'e01P', 'e01Q', 'e01R', 'e01S', 'e01T',
        'e01U', 'e01V', 'e01Y', 'e01Z', 'e023', 'e02W', 'u020', 'u022'
    ]
    unit_data = [ib.inspect_unit(u) for u in unit_ids]

    # 4. Heroes (6 primary + 2 unreferenced clones)
    hero_ids = ['U023', 'U024', 'U025', 'U02A', 'U02R', 'U02S']
    hero_data = [ib.inspect_unit(h) for h in hero_ids]

    extra_heroes = ['U037', 'U038']
    extra_hero_data = [ib.inspect_unit(h) for h in extra_heroes]

    # 5. Upgrades (23)
    silitid_upgrade_ids = [
        'R0BV', 'R08G', 'R088',
        'R089', 'R08B', 'R085', 'R08A', 'R083', 'R084', 'R07Z', 'R07Y', 'R009', 'R07X',
        'R0D0',
        'R08C', 'R08D', 'R08F', 'R08E',
        'R086', 'R080', 'R081', 'R082',
        'R087'
    ]
    upgrade_data = [ib.inspect_upgrade(u) for u in silitid_upgrade_ids]

    # 6. Abilities
    silitid_ability_ids = [
        # Selection & C'Thun
        'A0J7', 'A1B7', 'A1B8',
        # Buildings
        'A0T1', 'A0SW', 'A0LJ', 'A0LI', 'A0IQ', 'Argl', 'A0ML', 'Arlm', 'A0J0', 'A0Z5', 'A0KP',
        'A0B0', 'A0B1', 'A0B2', 'A0AZ', 'AHad', 'Aivs',
        # Worker & Units
        'A0I3', 'Aren', 'ANha', 'A0VH', 'A0J9', 'A1KD', 'Apoi',
        'A0SX', 'A0KR', 'A0KQ', 'A0ZU', 'A0IW', 'Ansk', 'Afae', 'A0JG', 'A0IY', 'A0JF',
        'A0KO', 'A0IZ', 'A1KF', 'A1KG', 'A1KE', 'A0KN', 'A0KM', 'A0C4', 'Arpl', 'Arpm',
        'A1R4', 'Afak', 'Aabs', 'ACmi', 'A1JE',
        # Heroes
        'A0J2', 'A0SU', 'A0SV', 'A0J1',
        'AUls', 'AEah', 'AUts', 'A0SQ',
        'AEtq', 'AUau', 'AOhx', 'A0ST',
        'A0Y2',
        'A1B6', 'A193', 'A192', 'A188',
        'A197', 'A195', 'A191'
    ]
    ability_data = [ib.inspect_ability(a) for a in silitid_ability_ids]

    # 7. Buffs
    buff_ids = [
        # Custom
        'B04G', 'B04H', 'B04I', 'B04K', 'B05Z', 'B06W', 'B06X', 'B082', 'B042', 'B004', 'B023',
        # Standard WC3 buffs used by abilities
        'BEah', 'BHad', 'BHtc', 'BNab', 'BNcg', 'BNfy', 'BNpa', 'BNpm', 'BNrf', 'BOae',
        'BOhx', 'BOwd', 'BUau', 'BUcs', 'BUim', 'BUsl', 'BUsp', 'BUts', 'Bfae', 'Bfzy',
        'Blsa', 'Bpoi', 'Bpsd', 'Brpl', 'Brpm', 'Bspl', 'Bust'
    ]
    buff_data = [ib.inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/silitids_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'units': unit_data,
        'heroes': hero_data,
        'extra_heroes': extra_hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)} (plus {len(extra_hero_data)} unused/clones)")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
