# -*- coding: utf-8 -*-
"""Inspect all Race 25: Nagi (Наги) objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, resolve, extract_wts_id

def main():
    print("=== INSPECTING NAGI (RACE 25) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A14O')
    selection_markers = [inspect_upgrade('R0FS'), inspect_upgrade('R0KZ')]

    # 2. Buildings (10)
    bld_ids = [
        'h0JW', 'h0JX', 'h0JY', 'n04L', 'n055',
        'nnfm', 'nnsa', 'nnsg', 'nntg', 'nntt'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Worker
    worker_data = [inspect_unit('nmpe')]

    # 4. Heroes
    hero_ids = ['H0JU', 'H0JV', 'H0OZ', 'N07A', 'N054']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Units (16 combat units + 1 summon)
    unit_ids = [
        'n04Z', 'n050', 'n051', 'n052', 'n053', 'n054', 'n056', 'n057',
        'n079', 'nmyr', 'nnmg', 'nnrg', 'nnsw', 'nwgs', 'nsnp', 'nhyc',
        'ntor'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 6. Upgrades / Researches
    upgrade_ids = [
        'R0FS', 'R0FE', 'R0FF', 'R0FD', 'R0FH', 'R0FP', 'R0FQ', 'R0FR',
        'R0KP', 'Rnam', 'Rnat', 'Rnen', 'Rnsb', 'Rnsi', 'Rnsw', 'R0KZ'
    ]
    upgrade_data = [inspect_upgrade(u) for u in upgrade_ids]

    # 7. Abilities
    ability_ids = [
        # Selection
        'A14O',
        # Heroes
        'A13C', 'AEbl', 'A13A', 'A13D',
        'A136', 'A137', 'A138', 'A139', 'A135',
        'A14F', 'A14G', 'A14H', 'A14I',
        'AEtq', 'AHbn', 'AHab', 'ANrf',
        'A16B', 'A16C', 'A16D', 'A16E',
        # Units
        'A1LT', 'S00E', 'A1LV', 'A13B', 'A14J', 'A14K', 'A14L', 'A14M', 'A14N',
        'A1OL', 'A1OM', 'A1ON', 'A1OO', 'A1OP', 'A1OQ', 'A1OR',
        'AChx', 'S00A', 'ACcb', 'ACen', 'ACfu', 'ACpv', 'ACsk', 'ANen',
        'ANpa', 'Acny', 'Asb2', 'drAq', 'A06U', 'A0I3',
        # Buildings
        'A0IQ', 'A0LI', 'A0LJ', 'A1KB'
    ]
    ability_data = [inspect_ability(a) for a in ability_ids]

    # 8. Buffs
    buff_ids = ['B06G', 'B06P', 'B06Q', 'B08I']
    buff_data = [inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/nagi_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'worker': worker_data,
        'heroes': hero_data,
        'units': unit_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Nagi:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Worker: {len(worker_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
