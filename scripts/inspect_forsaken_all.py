# -*- coding: utf-8 -*-
"""Inspect all Forsaken race objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff

def inspect_item(iid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'item', '--id', iid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    wts = hw.load_wts_strings()
    resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s
    extract_wts_id = lambda s: int(s[8:]) if isinstance(s, str) and s.startswith('TRIGSTR_') and s[8:].isdigit() else None
    
    get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
    raw_n = get_v('name')
    raw_t = get_v('tip')
    raw_ub = get_v('ubertip')
    raw_desc = get_v('description')
    
    return {
        'id': iid,
        'raw_name': raw_n,
        'name': resolve(raw_n),
        'name_sid': extract_wts_id(raw_n),
        'raw_tip': raw_t,
        'tip': resolve(raw_t),
        'tip_sid': extract_wts_id(raw_t),
        'raw_ubertip': raw_ub,
        'ubertip': resolve(raw_ub),
        'ubertip_sid': extract_wts_id(raw_ub),
        'raw_description': raw_desc,
        'description': resolve(raw_desc),
        'description_sid': extract_wts_id(raw_desc),
        'fields': f,
        'overrides': overrides
    }

def main():
    print("=== INSPECTING FORSAKEN (RACE 27) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A155')
    selection_markers = [inspect_upgrade('R0G3')]

    # 2. Buildings (11 + shipyard)
    bld_ids = [
        'h0JP', 'h0JQ', 'h0JL', 'h0JD', 'h0JJ', 'h0JI',
        'h0JO', 'h0JR', 'h0JK', 'h0JM', 'h0JZ', 'h0D1'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units (12 regular + 8 summons/subunits = 20)
    unit_ids = [
        'h0J5', 'n04T', 'h0JC', 'h0JN', 'n04U', 'o02X',
        'u02C', 'o02Y', 'n04Y', 'n04X', 'n04V', 'h0JA',
        'e034', 'u02J', 'u02K', 'u02L', 'u02M', 'u02N', 'u02O', 'u02P'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes (5: Sylvanas, Sylvanas Banshee, Dark Ranger, Apothecary, Eliminator)
    hero_ids = ['N059', 'N05E', 'N058', 'O031', 'O030']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Upgrades (17)
    upgrade_ids = [
        'R0G3', 'R0FI', 'R0FJ', 'R0FK', 'R0FL', 'R0FM',
        'R0FT', 'R0FY', 'R0FU', 'R0FV', 'R0FB', 'R0KJ',
        'R0FW', 'R0G0', 'R0FZ', 'R0FN', 'R0FO'
    ]
    upgrade_data = [inspect_upgrade(u) for u in upgrade_ids]

    # 6. Abilities (63)
    ability_ids = [
        # Selection
        'A155',
        # Heroes
        'A166', 'A15S', 'A15R', 'A15Q', 'A15T',
        'ANsi', 'ANba', 'ANdr', 'A0W4',
        'A15D', 'A15C', 'A15B', 'A15A',
        'A158', 'A157', 'A156', 'AOwk',
        # Worker
        'A0I3', 'ANha', 'Ahrp',
        # Barracks units
        'A15J', 'A15I', 'A14U', 'A14T', 'A14S', 'A14W', 'A14X', 'A15L', 'A15M', 'Adef',
        # Laboratory units & modes
        'A13J', 'A13L', 'A15E', 'A13K',
        'A142', 'A132', 'A143', 'A13U', 'A15H', 'A144', 'A13R',
        'A14C', 'A13M', 'A13T', 'A14E', 'A13N', 'A13S', 'A14D', 'A13O', 'A13V',
        # Sanctum units
        'A14P', 'A14R', 'A1H7', 'A14Q', 'Aiun',
        'A154', 'A153', 'A152', 'A14Y', 'A151', 'A14Z', 'A150',
        # Subunits
        'A13H', 'A15F', 'A13Z', 'A141', 'A140', 'A133', 'A13W', 'A16G', 'A13X', 'A13Y',
        # Triggers & dummies
        'A15P', 'A15V', 'ACch', 'A159'
    ]
    ability_data = [inspect_ability(a) for a in ability_ids]

    # 7. Buffs (4 custom Forsaken buffs)
    buff_ids = ['B06I', 'B06J', 'B06K', 'B06L']
    buff_data = [inspect_buff(b) for b in buff_ids]

    # 8. Items (4 runes spawned by A15B)
    item_ids = ['I01X', 'I01V', 'I01W', 'I01Y']
    item_data = [inspect_item(i) for i in item_ids]

    out_file = ROOT / "scripts/forsaken_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data,
        'items': item_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"  Items: {len(item_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
