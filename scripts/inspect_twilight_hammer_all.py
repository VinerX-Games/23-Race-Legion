# -*- coding: utf-8 -*-
"""Inspect all Twilight Hammer (Культ Сумеречного Молота) race objects and output structured JSON and summary."""
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
        'trains': f.get('trains'),
        'researches': f.get('researches'),
        'upgrades_to': f.get('upgrade') or f.get('upg') or overrides.get('upgrade'),
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
        'weaptype1': f.get('weaptp1') or f.get('weaptype1'),
        'dice2': f.get('dice2'),
        'sides2': f.get('sides2'),
        'dmgplus2': f.get('dmgplus2'),
        'cool2': f.get('cool2'),
        'targs2': f.get('targs2'),
        'weaptype2': f.get('weaptp2') or f.get('weaptype2'),
        'revivetip': resolve(f.get('revivetip')),
        'raw_revivetip': f.get('revivetip'),
        'awakentip': resolve(f.get('awakentip')),
        'raw_awakentip': f.get('awakentip'),
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
    untips = {}
    unubertips = {}
    for i in range(1, levels + 1):
        tips[f'tip{i}'] = {'raw': f.get(f'tip{i}'), 'val': resolve(f.get(f'tip{i}'))}
        ubertips[f'ubertip{i}'] = {'raw': f.get(f'ubertip{i}'), 'val': resolve(f.get(f'ubertip{i}'))}
        if f.get(f'untip{i}'):
            untips[f'untip{i}'] = {'raw': f.get(f'untip{i}'), 'val': resolve(f.get(f'untip{i}'))}
        if f.get(f'unubertip{i}'):
            unubertips[f'unubertip{i}'] = {'raw': f.get(f'unubertip{i}'), 'val': resolve(f.get(f'unubertip{i}'))}
    return {
        'id': aid,
        'raw_name': f.get('name'),
        'name': resolve(f.get('name')),
        'levels': levels,
        'hotkey': resolve(f.get('hotkey')),
        'raw_hotkey': f.get('hotkey'),
        'researchhotkey': resolve(f.get('researchhotkey')),
        'raw_researchhotkey': f.get('researchhotkey'),
        'raw_researchtip': f.get('researchtip'),
        'researchtip': resolve(f.get('researchtip')),
        'raw_researchubertip': f.get('researchubertip'),
        'researchubertip': resolve(f.get('researchubertip')),
        'tips': tips,
        'ubertips': ubertips,
        'untips': untips,
        'unubertips': unubertips,
        'fields': f,
        'overrides': overrides
    }

def inspect_upgrade(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
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
        'fields': f,
        'overrides': overrides
    }

def inspect_buff(bid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid, '--all'])
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
    print("=== INSPECTING ALL TWILIGHT HAMMER (RACE 20) OBJECTS ===")

    # 1. Selection & Markers
    selection_ability = inspect_ability('A0HX')
    marker_ids = ['R07K', 'R0KD']
    selection_markers = [inspect_upgrade(m) for m in marker_ids]

    # 2. Buildings (9)
    bld_ids = ['o00K', 'o00T', 'o00L', 'o00R', 'o00V', 'o00P', 'o00U', 'o00Q', 'h0D3']
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units (13)
    unit_ids = ['o00J', 'o00M', 'o00N', 'o00S', 'o002', 'u004', 'n00R', 'n00U', 'n00D', 'n00C', 'o00O', 'n00S', 'u005']
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes (3)
    hero_ids = ['O011', 'N010', 'N00Z']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Upgrades (16 + 2 markers)
    upgrade_ids = [
        'R07K', 'R0KD',
        'R04D', 'R04V', 'R00O', 'R04S', 'R04U', 'R0EJ', 'R05S', 'R05T', 'R05U', 'R05V',
        'R04Z', 'R050', 'R051', 'R052', 'R04W', 'R04X'
    ]
    upgrade_data = [inspect_upgrade(u) for u in upgrade_ids]

    # 6. Abilities (33)
    ability_ids = [
        'A0HX', 'A01Z', 'A09Q', 'A09R', 'A09S', 'A09T', 'A09U', 'A09V', 'A09W', 'A09X',
        'A0A0', 'A0A1', 'A0A2', 'A0AI', 'A0AJ', 'A0AK', 'A0AL', 'A0AM', 'A0AN', 'A1QQ',
        'A09Z', 'A0AO', 'A0AP', 'A0B6', 'A0B8', 'A0B9', 'A0BA', 'A0BB', 'A0BC', 'A0BD',
        'A0BE', 'A0BF', 'A0B7'
    ]
    ability_data = [inspect_ability(a) for a in ability_ids]

    # 7. Buffs (11)
    buff_ids = ['B025', 'B026', 'B02C', 'B02D', 'B02K', 'B00A', 'B00B', 'B02B', 'B02G', 'B02E', 'B02L']
    buff_data = [inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/twilight_hammer_raw_dump.json"
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
    out_file.write_text(json.dumps(dump_data, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"\nInspection summary:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"\nSaved raw dump to {out_file}")

if __name__ == '__main__':
    main()
