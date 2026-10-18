# -*- coding: utf-8 -*-
"""Inspect all Kul Tiras race objects, abilities, and upgrades."""
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
        'abils': f.get('abils') or f.get('abillist'),
        'heroabils': f.get('heroabils') or res.get('overrides', {}).get('heroabillist') or f.get('heroabillist'),
        'upgrades': f.get('upgrades'),
        'hp': f.get('hp'),
        'mana': f.get('mana0') or f.get('mana') or f.get('manan'),
        'def': f.get('def'),
        'deftype': f.get('deftype'),
        'atktype1': f.get('atktype1'),
        'dice1': f.get('dice1'),
        'sides1': f.get('sides1'),
        'dmgplus1': f.get('dmgplus1'),
        'cool1': f.get('cool1'),
        'targs1': f.get('targs1'),
        'weaptype1': f.get('weaptype1'),
        'atktype2': f.get('atktype2'),
        'dice2': f.get('dice2'),
        'sides2': f.get('sides2'),
        'dmgplus2': f.get('dmgplus2'),
        'cool2': f.get('cool2'),
        'targs2': f.get('targs2'),
        'weaptype2': f.get('weaptype2'),
        'builds': f.get('builds'),
        'editorsuffix': resolve(f.get('editorsuffix')),
        'raw_editorsuffix': f.get('editorsuffix'),
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
    levels = int(f.get('maxlevel') or f.get('levels') or 1)
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
    print("=== INSPECTING KUL TIRAS (RACE 17) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HO')
    selection_markers = [inspect_upgrade(u) for u in ['R07D', 'R0HX']]

    # 2. Buildings
    bld_ids = [
        'h01X', 'h01Y', 'h01Z', 'h020', 'h021', 'h0G6',
        'h022', 'h023', 'h024', 'h025', 'h026', 'h027', 'kt02'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units
    unit_ids = [
        'h013', 'h019', 'h01A', 'h01C', 'h01D', 'h01E', 'h01F', 'h01G', 'h01H', 'h01I', 'kt00',
        'h0NC', 'h0ND', 'h0NE', 'h0NF', 'h0NG', 'h0NH', 'h0NI', 'h0NJ', 'h0NS',
        'h0NL', 'h0NM', 'h0NN', 'h0NO', 'h0NP', 'h0NQ', 'h0NR', 'h0NK', 'h0NT', 'h0NU', 'h0NV'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes
    hero_ids = ['H01L', 'H01N', 'H01K']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Upgrades from buildings / AI
    upgrade_ids = [
        'R07D', 'R0HX',
        # Upgrades used by buildings/units:
        'R0KL', 'R035', 'R036', 'R037', 'R038', 'R039',
        'kt01'
    ]
    for b in bld_data:
        res = b.get('researches')
        if res:
            for u in res.split(','):
                u = u.strip()
                if u and u not in upgrade_ids:
                    upgrade_ids.append(u)
    for u in unit_data:
        upgs = u.get('upgrades')
        if upgs:
            for up in upgs.split(','):
                up = up.strip()
                if up and up not in upgrade_ids:
                    upgrade_ids.append(up)

    upgrade_data = []
    for uid in upgrade_ids:
        try:
            upg = inspect_upgrade(uid)
            # check if it actually exists as upgrade
            if upg['names'].get('name1', {}).get('val'):
                upgrade_data.append(upg)
            else:
                print(f"Upgrade {uid} returned empty name, might be ability or unused")
        except Exception as e:
            print(f"Error inspecting upgrade {uid}: {e}")

    # 6. Abilities from units, heroes, and buildings
    ability_ids = [
        # Hero skills
        'A0TM', 'A1MF', 'A07F', 'A07C',
        'A075', 'A076', 'A078', 'A077',
        'A07B', 'A07A', 'A079', 'A05I',
        # AI mentioned abilities
        'Abds', 'Arlm', 'Adts', 'A0LJ', 'A0LI', 'A0IQ', 'Argl',
    ]
    for obj in bld_data + unit_data + hero_data:
        for fld in ['abils', 'heroabils', 'researches']:
            val = obj.get(fld)
            if val:
                for a in val.split(','):
                    a = a.strip()
                    if a and a not in ability_ids:
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
            ab = inspect_ability(aid)
            if ab['name'] or ab['tips'].get('tip1', {}).get('val'):
                ability_data.append(ab)
            else:
                print(f"Ability {aid} returned empty name/tip")
        except Exception as e:
            print(f"Error inspecting ability {aid}: {e}")

    out_file = ROOT / "scripts/kultiras_raw_dump.json"
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
