# -*- coding: utf-8 -*-
"""Inspect all Blood Elves race objects and output structured JSON and summary."""
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
    f = res.get('object', {}) or res.get('fields', {})
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
        'trains': f.get('trains'),
        'researches': f.get('researches'),
        'upgrades_to': f.get('upgrades_to') or f.get('upg') or f.get('upgrade'),
        'abils': f.get('abils'),
        'heroabils': f.get('heroabils') or res.get('overrides', {}).get('heroabillist'),
        'upgrades': f.get('upgrades'),
        'hp': f.get('hp'),
        'mana': f.get('mana0') or f.get('mana'),
        'def': f.get('def'),
        'deftype': f.get('deftype'),
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
        'fields': f
    }

def inspect_ability(aid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
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
        'fields': f
    }

def inspect_upgrade(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    levels = int(f.get('levels') or 1)
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
        'fields': f
    }

def main():
    print("=== INSPECTING BLOOD ELVES (RACE 15) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HQ')
    selection_markers = [inspect_upgrade(u) for u in ['R07C', 'R0L0']]

    # 2. Buildings
    bld_ids = [
        'h04C', 'h04B', 'h04A', 'h04M', 'h04D', 'h04N', 'h04O', 'h04P',
        'h04Q', 'h04R', 'h05J', 'h04G', 'h04E', 'h04F', 'h011', 'h0HO'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units
    unit_ids = [
        'h04K', 'h03V', 'n00I', 'h03X', 'h03Y', 'e001', 'e030',
        'h046', 'h03Z', 'h03W', 'h040', 'h041', 'h042',
        'n00O', 'h0BY', 'h0O6'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes
    hero_ids = ['H043', 'Hjnd', 'H045', 'H03H', 'H044', 'H05H', 'H05I', 'Hkal']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Researches
    upgrade_ids = [
        # Blacksmith
        'R01N', 'R01K', 'R01L', 'R01M', 'R01R', 'R01J',
        # Lumber mill
        'R03I', 'R03J', 'R01T', 'R03E', 'R03F',
        # Barracks
        'R03K', 'R01Y', 'R01X', 'R01W',
        # Sanctum
        'R0BU', 'R01O', 'R01P', 'R01Q', 'R01S', 'R025', 'R026', 'R03C', 'R03D',
        # Aviary / Workshop
        'R03N', 'R021', 'R03Q', 'Rhcd',
        # 4 Paths (Temple)
        'R03R', 'R01H', 'R01I', 'R01G', 'R01D', 'R01E', 'R01F', 'R020',
        # Selection markers
        'R07C', 'R0L0'
    ]
    # Remove duplicates preserving order
    seen = set()
    dedup_upgrade_ids = []
    for u in upgrade_ids:
        if u not in seen:
            seen.add(u)
            dedup_upgrade_ids.append(u)
    upgrade_data = [inspect_upgrade(u) for u in dedup_upgrade_ids]

    # 6. Gather all ability IDs from buildings, units, heroes, and triggers
    ability_ids = [
        # Hero abilities
        # Kael'thas
        'AHfs', 'AHdr', 'AHpx', 'AHbn', 'A08R',
        # Lor'themar
        'A07U', 'A0LQ', 'AEar', 'A07V', 'A16M', 'A0DD', 'ACmi',
        # Rommath
        'A08H', 'A07W', 'AHbh', 'AHre',
        # Liadrin
        'A1KU', 'A1KV', 'A1KY',
        # Unit abilities
        'A05J', 'A05K', 'A049', 'Asps',
        'A07L', 'A037', 'A07K',
        'A07P', 'A07Q', 'A07N', 'A07O', 'A02G', 'A07D',
        'A07M', 'A07S', 'A07R', 'A07T',
        'A02J', 'A00W', 'A030', 'A02Z', 'A02R', 'A02U',
        'A02D', 'A02E', 'A02N', 'A02O', 'A02Q', 'A02S', 'A02T', 'A02X', 'A02Y',
        'A032', 'A035', 'A0IQ', 'A0LI', 'A0LJ', 'A0SY',
        'A16H', 'A1LW', 'A1QZ', 'A1R0', 'A1R1',
        'Afbt', 'AHta', 'Arlm', 'Argl', 'B00F'
    ]
    # Also collect abils from inspected units/heroes
    for obj in bld_data + unit_data + hero_data:
        for fld in ['abils', 'heroabils', 'researches']:
            val = obj.get(fld)
            if val:
                for a in val.split(','):
                    a = a.strip()
                    if a and a not in ability_ids and a not in dedup_upgrade_ids:
                        ability_ids.append(a)

    seen_a = set()
    dedup_ability_ids = []
    for a in ability_ids:
        if a not in seen_a:
            seen_a.add(a)
            dedup_ability_ids.append(a)

    ability_data = []
    for aid in dedup_ability_ids:
        try:
            ability_data.append(inspect_ability(aid))
        except Exception as e:
            print(f"Error inspecting ability {aid}: {e}")

    out_file = ROOT / "scripts/blood_elves_raw_dump.json"
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
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"\nSaved raw dump to {out_file}")

if __name__ == '__main__':
    main()
