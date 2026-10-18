# -*- coding: utf-8 -*-
"""Inspect all Dalaran race objects and output structured JSON and summary."""
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
        'fields': f
    }

def main():
    print("=== INSPECTING DALARAN (RACE 16) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HN')
    selection_markers = [inspect_upgrade(u) for u in ['R0BW', 'R0KK']]

    # 2. Buildings
    bld_ids = [
        'h030', 'h031', 'h02V', 'h02W', 'h02X', 'h02Y',
        'h034', 'h035', 'h036', 'h032', 'h037', 'h038',
        'n063', 'h011'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units
    unit_ids = [
        'u001', 'h02I', 'h02J', 'h02K', 'h02L', 'h02M',
        'h02N', 'h02O', 'h02P', 'n009', 'n00A', 'n00B',
        'n00M', 'n00N'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes
    hero_ids = ['H04S', 'H04W', 'H04X', 'H052', 'H053']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Researches
    upgrade_ids = [
        # Magic Forge (h02Y)
        'R013', 'R014', 'R012', 'R00Q', 'R00T',
        # Arcane Sanctuary / Town Hall (h030)
        'R018', 'R017', 'R015',
        # Magic Library (h02W)
        'R016', 'R00Z', 'R010', 'Rhse', 'R011',
        # Magic Armory (h02X)
        'R01C', 'Rhde', 'R01B', 'R01A',
        # Mana Vault T2 (h035)
        'R00S',
        # Mana Accumulator (h036)
        'R00R',
        # Selection markers
        'R0BW', 'R0KK'
    ]
    # Remove duplicates preserving order
    seen_u = set()
    dedup_upgrade_ids = []
    for u in upgrade_ids:
        if u not in seen_u:
            seen_u.add(u)
            dedup_upgrade_ids.append(u)
    upgrade_data = [inspect_upgrade(u) for u in dedup_upgrade_ids]

    # 6. Gather all ability IDs from buildings, units, heroes
    ability_ids = [
        # Selection
        'A0HN',
        # Worker
        'A0I3', 'ANha', 'Arst',
        # Heroes
        # H04S (Верховный маг)
        'A03K', 'A03J', 'A03I', 'A03D',
        # H04W (Огненный мастер)
        'A03Q', 'A03O', 'A03M', 'A03L',
        # H04X (Мастер Тайной магии)
        'A044', 'A03V', 'A03U', 'A1FQ',
        # H052 (Глава Кирин-Тора - Ронин)
        'A0YK', 'AInv', 'A04E', 'A04D', 'A04B', 'A04A',
        # H053 (Хранитель - Кадгар)
        'A04I', 'A04H', 'A04G',
        # Unit abilities
        'Adef', 'A03H',
        'A02J', 'A00W', 'A01W', 'A01O', 'A01N',
        'A01V', 'A01U', 'A01T', 'A01Q',
        'A040', 'A031', 'A03Z', 'A03Y', 'A03X',
        'A03S', 'A01M', 'A01L', 'A01K',
        'A03G', 'A01G', 'A03F', 'A01F', 'A03E',
        'A021', 'A022', 'A01X',
        'A01S', 'A01R', 'A045',
        # Building abilities
        'Afbt', 'A0LJ', 'A1MK', 'A0IQ', 'Argl', 'Abds', 'Adts',
        'A03W', 'A018', 'Asid', 'Avul', 'Ane2', 'A0HY', 'AHad', 'Awrp',
        'A15N', 'A1O5'
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

    out_file = ROOT / "scripts/dalaran_raw_dump.json"
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
