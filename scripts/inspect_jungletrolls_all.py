# -*- coding: utf-8 -*-
"""Inspect all Jungle Trolls (Тролли джунглей, Race 30) objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_race_base as base

def main():
    print("=== INSPECTING JUNGLE TROLLS (RACE 30) OBJECTS ===")

    # 1. Selection
    selection_ability = base.inspect_ability('A1DZ')
    selection_markers = [
        base.inspect_upgrade('R0IH'),
        base.inspect_upgrade('R0IR'),
    ]

    # 2. Buildings (10)
    bld_ids = [
        'h0N5', 'h0N1', 'h0N6', 'h0N2', 'h0MY', 'h0MW', 'h0MX', 'h0N0', 'h0N3', 'h0D3'
    ]
    bld_data = base.bulk_inspect_units(bld_ids)

    # 3. Units (14)
    unit_ids = [
        'o04Q', 'o04M', 'o05K', 'o04L', 'o05E', 'o04O', 'o04R', 'o04N', 'o04P',
        'o04S', 'o05J', 'o04U', 'o05G', 'o05I'
    ]
    unit_data = base.bulk_inspect_units(unit_ids)

    # 4. Heroes (6)
    hero_ids = ['O054', 'O05A', 'O05D', 'O055', 'O05L', 'O05C']
    hero_data = base.bulk_inspect_units(hero_ids)

    # 5. Upgrades (14)
    upgrade_ids = [
        'R0IH', 'R0IR', 'R0I8', 'R0I9', 'R0IA', 'R0IB', 'R0IC',
        'R0ID', 'R0II', 'R0IJ', 'R0IK', 'R0IL', 'R0IM', 'R0IN'
    ]
    upgrade_data = base.bulk_inspect_upgrades(upgrade_ids)

    # 6. Abilities (52)
    ability_ids = [
        # Selection & choices
        'A1DZ', 'A1EP', 'A1EQ',
        # Racial mechanics & passives
        'A1D0', 'A1D1', 'A1CX', 'A1DU',
        # Worker & Units
        'A0I3', 'A1EJ', 'A1EI', 'A1DF', 'A1DG', 'A1DH', 'A1DX', 'A1D2',
        'A1D3', 'A1D5', 'A1DT', 'A1DV', 'A1DW', 'A1F4', 'A1F5', 'A1F6',
        'A1DY', 'A1EH', 'A1DK', 'A1DN', 'A1DI',
        # Heroes
        'AOhw', 'A1E0', 'AOsw', 'AOls',
        'A1E2', 'A1E5', 'A1E3', 'A1E4',
        'A1E6', 'A1EA', 'A1E8', 'A1E9',
        'A1DC', 'A1DM', 'A1EL', 'A1DB', 'A1DD', 'A1EM', 'A1EK',
        'A1EV', 'A1EW', 'A1EX', 'A1EY', 'A1ER', 'A1ES', 'A1ET', 'A1EZ', 'A1EU',
        # Dummies
        'A1E1', 'A1E7'
    ]
    ability_data = base.bulk_inspect_abilities(ability_ids)

    # 7. Buffs (14)
    buff_ids = [
        'B076', 'B07A', 'B07B', 'B07C', 'B07D', 'B07E', 'B07G',
        'BOhx', 'BOww', 'Bhwd', 'BUfa', 'BHca', 'Bcsd', 'BUdd'
    ]
    buff_data = base.bulk_inspect_buffs(buff_ids)

    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }

    out_file = ROOT / "scripts/jungletrolls_raw_dump.json"
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Jungle Trolls:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
