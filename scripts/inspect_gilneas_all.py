# -*- coding: utf-8 -*-
"""Inspect all Gilneas / Worgens race objects (Race 24) and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff

def main():
    print("=== INSPECTING GILNEAS / WORGENS (RACE 24) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A121')
    selection_markers = [inspect_upgrade('R0FX')]

    # 2. Buildings (11)
    bld_ids = [
        'h0IJ', 'h0IK', 'h0IL', 'h0IM', 'h0IN', 'h0IO',
        'h0IP', 'h0IQ', 'h0IR', 'h0IS', 'h0JT'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Worker (1)
    worker_data = inspect_unit('h0IT')

    # 4. Units (10)
    unit_ids = [
        'h0IU', 'h0IV', 'h0IW', 'h0IX', 'h0IY',
        'h0IZ', 'h0J0', 'h0J1', 'h0NA', 'o02T'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 5. Heroes (4)
    hero_ids = ['H0J2', 'H0J6', 'H0J7', 'H0J8']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 6. Upgrades (16)
    upgrade_ids = [
        'R0FX', 'R0EY', 'Rhri', 'Rhde', 'R0EM', 'R0EN',
        'R0EO', 'R0EP', 'R0EQ', 'R0IP', 'R0F6', 'R0F5',
        'R0EZ', 'R0F1', 'R0F0', 'R0F2'
    ]
    upgrade_data = [inspect_upgrade(u) for u in upgrade_ids]

    # 7. Abilities
    ability_ids = [
        # Selection
        'A121',
        # Heroes
        'A11I', 'A11H', 'A11J', 'A11K',
        'A11L', 'A11N', 'A11M', 'A11O',
        'A11Q', 'A11P', 'A11R', 'A11S',
        'A11Z', 'A11U', 'A11T', 'A120',
        'A11V', 'A11W', 'A11X', 'A11Y',
        # Units
        'A117', 'A118', 'A119', 'A11A', 'A11B', 'A11C',
        'A11D', 'A11E', 'A1F0', 'A1F1', 'A0PE',
        'A06L', 'A06N', 'Adef', 'Ahri', 'Adis',
        # Worker & Buildings
        'A0I3', 'ANha', 'Ahrp', 'A0LJ', 'A0LI', 'A0IQ'
    ]
    ability_data = [inspect_ability(a) for a in ability_ids]

    # 8. Buffs
    buff_ids = [
        'B06A', 'B06B', 'B06C', 'B06D',
        'BEar', 'BHab', 'BHtc', 'BNms', 'BOsf', 'BPSE',
        'BUav', 'BUcs', 'Bblo', 'Broa', 'Brpl'
    ]
    buff_data = [inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/gilneas_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'worker': worker_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Gilneas:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Worker: 1 ({worker_data['id']})")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
