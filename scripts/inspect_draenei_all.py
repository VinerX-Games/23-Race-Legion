# -*- coding: utf-8 -*-
"""Inspect all Draenei race objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def inspect_unit(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    return {
        'id': uid,
        'raw_name': f.get('name'),
        'name': resolve(f.get('name')),
        'raw_tip': f.get('tip'),
        'tip': resolve(f.get('tip')),
        'raw_ubertip': f.get('ubertip'),
        'ubertip': resolve(f.get('ubertip')),
        'raw_propernames': f.get('propernames'),
        'propernames': resolve(f.get('propernames')),
        'raw_hotkey': f.get('hotkey'),
        'hotkey': resolve(f.get('hotkey')),
        'trains': f.get('trains') or overrides.get('trains'),
        'researches': f.get('researches') or overrides.get('researches'),
        'upgrades_to': f.get('upgrades_to') or f.get('upg') or f.get('upgrade') or overrides.get('upgrade'),
        'abils': f.get('abillist') or overrides.get('abillist'),
        'heroabils': f.get('heroabillist') or overrides.get('heroabillist'),
        'upgrades': f.get('upgrades') or overrides.get('upgrades'),
        'builds': f.get('builds') or overrides.get('builds'),
        'hp': f.get('hp'),
        'mana': f.get('mana0') or f.get('mana'),
        'def': f.get('def'),
        'deftype': f.get('deftype'),
        'atktype1': f.get('atktype1'),
        'atktype2': f.get('atktype2'),
        'dice1': f.get('dice1'),
        'sides1': f.get('sides1'),
        'dmgplus1': f.get('dmgplus1'),
        'cool1': f.get('cool1'),
        'targs1': f.get('targs1'),
        'weaptype1': f.get('weaptype1'),
        'dice2': f.get('dice2'),
        'sides2': f.get('sides2'),
        'dmgplus2': f.get('dmgplus2'),
        'cool2': f.get('cool2'),
        'targs2': f.get('targs2'),
        'weaptype2': f.get('weaptype2'),
        'fields': f,
        'overrides': overrides
    }

def inspect_ability(aid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    levels = int(f.get('levels') or 1)
    tips = {}
    ubertips = {}
    for i in range(1, levels + 1):
        tips[f'tip{i}'] = {'raw': f.get(f'tip{i}'), 'val': resolve(f.get(f'tip{i}'))}
        ubertips[f'ubertip{i}'] = {'raw': f.get(f'ubertip{i}'), 'val': resolve(f.get(f'ubertip{i}'))}
    return {
        'id': aid,
        'raw_name': f.get('name'),
        'name': resolve(f.get('name')),
        'levels': levels,
        'hotkey': resolve(f.get('hotkey')),
        'raw_hotkey': f.get('hotkey'),
        'researchhotkey': resolve(f.get('researchhotkey')),
        'raw_researchtip': f.get('researchtip'),
        'researchtip': resolve(f.get('researchtip')),
        'raw_researchubertip': f.get('researchubertip'),
        'researchubertip': resolve(f.get('researchubertip')),
        'tips': tips,
        'ubertips': ubertips,
        'fields': f,
        'overrides': overrides
    }

def inspect_upgrade(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    levels = int(f.get('levels') or f.get('maxlevel') or 1)
    names = {}
    tips = {}
    ubertips = {}
    hotkeys = {}
    for i in range(1, levels + 1):
        names[f'name{i}'] = {'raw': f.get(f'name{i}') or f.get('name'), 'val': resolve(f.get(f'name{i}') or f.get('name'))}
        tips[f'tip{i}'] = {'raw': f.get(f'tip{i}'), 'val': resolve(f.get(f'tip{i}'))}
        ubertips[f'ubertip{i}'] = {'raw': f.get(f'ubertip{i}'), 'val': resolve(f.get(f'ubertip{i}'))}
        hotkeys[f'hotkey{i}'] = {'raw': f.get(f'hotkey{i}') or f.get('hotkey'), 'val': resolve(f.get(f'hotkey{i}') or f.get('hotkey'))}
    return {
        'id': uid,
        'levels': levels,
        'raw_class': f.get('class'),
        'names': names,
        'tips': tips,
        'ubertips': ubertips,
        'hotkeys': hotkeys,
        'fields': f,
        'overrides': overrides
    }

def inspect_buff(bid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    return {
        'id': bid,
        'raw_name': f.get('buffname') or f.get('name'),
        'name': resolve(f.get('buffname') or f.get('name')),
        'raw_tip': f.get('bufftip') or f.get('tip'),
        'tip': resolve(f.get('bufftip') or f.get('tip')),
        'raw_ubertip': f.get('buffubertip') or f.get('ubertip'),
        'ubertip': resolve(f.get('buffubertip') or f.get('ubertip')),
        'fields': f,
        'overrides': overrides
    }

def main():
    print("=== INSPECTING DRAENEI (RACE 19) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HS')
    selection_markers = [inspect_upgrade('R07G')]

    # 2. Buildings
    bld_ids = [
        'h015', 'h016', 'h017', 'h033', 'h055', 'h056',
        'h057', 'h058', 'h05A', 'h05B', 'h05C', 'h011'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units
    # Candidate units from 16_draenei.lua, wc3_hivewe, triggers
    unit_ids = [
        'h012', 'e000', 'h01O', 'h01P', 'h01Q', 'h01R',
        'h01S', 'h01T', 'h01U', 'h059', 'h05D', 'h05E',
        'n005', 'nDr1', 'o00H', 'n00P'
    ]
    unit_data = []
    for u in unit_ids:
        try:
            ud = inspect_unit(u)
            unit_data.append(ud)
        except Exception as e:
            print(f"Error inspecting unit {u}: {e}")

    # 4. Heroes
    hero_ids = ['H05K', 'H05L', 'H05M', 'H0MI']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Collect all potential upgrades and abilities
    upgrade_ids = ['R07G', 'RDr1', 'RDr2', 'RDr3', 'RDr4', 'RDr5', 'R0EB', 'R027', 'R02S', 'R023', 'R024', 'R02P', 'R02R', 'R02Q', 'R0D8', 'Rguv']
    ability_ids = ['A0HS', 'A0Z3', 'ADr1', 'ADr2', 'ADr3', 'ADr4', 'ADr5', 'A031']

    for obj in bld_data + unit_data + hero_data:
        # Upgrades
        for fld in ['upgrades', 'researches']:
            val = obj.get(fld)
            if val:
                for item in str(val).split(','):
                    item = item.strip()
                    if not item: continue
                    if item.startswith('R') or item in ['Rhac', 'Rgfo', 'Rguv', 'R0D8', 'Arlm', 'Abds']:
                        if item.startswith('A'):
                            if item not in ability_ids:
                                ability_ids.append(item)
                        else:
                            if item not in upgrade_ids:
                                upgrade_ids.append(item)
                    elif item.startswith('A'):
                        if item not in ability_ids:
                            ability_ids.append(item)

        # Abilities
        for fld in ['abils', 'heroabils']:
            val = obj.get(fld)
            if val:
                for item in str(val).split(','):
                    item = item.strip()
                    if not item: continue
                    if item not in ability_ids:
                        ability_ids.append(item)

    print(f"Discovered Upgrades: {upgrade_ids}")
    print(f"Discovered Abilities: {ability_ids}")

    upgrade_data = []
    for uid in upgrade_ids:
        try:
            upgrade_data.append(inspect_upgrade(uid))
        except Exception as e:
            print(f"Error inspecting upgrade {uid}: {e}")

    ability_data = []
    for aid in ability_ids:
        try:
            ability_data.append(inspect_ability(aid))
        except Exception as e:
            print(f"Error inspecting ability {aid}: {e}")

    out_file = ROOT / "scripts/draenei_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data
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
    print(f"\nSaved raw dump to {out_file}")

if __name__ == '__main__':
    main()
