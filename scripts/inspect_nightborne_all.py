# -*- coding: utf-8 -*-
"""Inspect all Nightborne race objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def inspect_unit(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--all'])
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
        'train': f.get('train'),
        'researches': f.get('res'),
        'upgrades_to': f.get('upg') or f.get('upgrades_to') or overrides.get('upgrade'),
        'abillist': f.get('abillist'),
        'heroabillist': f.get('heroabillist') or overrides.get('heroabillist'),
        'upgrades': f.get('upgrades'),
        'builds': f.get('builds'),
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
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
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
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
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

def main():
    print("=== INSPECTING NIGHTBORNE (RACE 18) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HU')
    selection_markers = [inspect_upgrade('R07J')]

    # 2. Buildings
    bld_ids = [
        'h0CB', 'h0CC', 'h0CD', 'h0CE', 'h0CF', 'h0CG',
        'h0CH', 'h0CI', 'h0CK', 'h0CL', 'h0CM', 'h0D8'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units
    unit_ids = [
        'h0CJ', 'e013', 'e014', 'e015', 'e016', 'e017',
        'e018', 'e019', 'e01A', 'e01B', 'h0CA'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes
    hero_ids = ['E01E', 'E01D', 'E01F']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Collect all potential upgrades and abilities
    upgrade_ids = ['R07J']
    ability_ids = ['A0HU']

    for obj in bld_data + unit_data + hero_data:
        # Upgrades
        for fld in ['upgrades', 'researches']:
            val = obj.get(fld)
            if val:
                for item in val.split(','):
                    item = item.strip()
                    if not item: continue
                    if item.startswith('R') or item in ['Rhac', 'Rgfo', 'Rguv']:
                        if item not in upgrade_ids:
                            upgrade_ids.append(item)
                    elif item.startswith('A'):
                        if item not in ability_ids:
                            ability_ids.append(item)

        # Abilities
        for fld in ['abillist', 'heroabillist']:
            val = obj.get(fld)
            if val:
                for item in val.split(','):
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

    out_file = ROOT / "scripts/nightborne_raw_dump.json"
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
