# -*- coding: utf-8 -*-
"""Inspect all Ogres (Race 28) objects and output structured JSON and summary."""
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
        'raw_name': overrides.get('name') or f.get('name'),
        'name': resolve(overrides.get('name') or f.get('name')),
        'raw_tip': overrides.get('tip') or f.get('tip'),
        'tip': resolve(overrides.get('tip') or f.get('tip')),
        'raw_ubertip': overrides.get('ubertip') or f.get('ubertip'),
        'ubertip': resolve(overrides.get('ubertip') or f.get('ubertip')),
        'raw_propernames': overrides.get('propernames') or f.get('propernames'),
        'propernames': resolve(overrides.get('propernames') or f.get('propernames')),
        'raw_awakentip': overrides.get('awakentip') or f.get('awakentip'),
        'awakentip': resolve(overrides.get('awakentip') or f.get('awakentip')),
        'raw_revivetip': overrides.get('revivetip') or f.get('revivetip'),
        'revivetip': resolve(overrides.get('revivetip') or f.get('revivetip')),
        'raw_hotkey': overrides.get('hotkey') or f.get('hotkey'),
        'hotkey': resolve(overrides.get('hotkey') or f.get('hotkey')),
        'train': overrides.get('trains') or f.get('train'),
        'researches': overrides.get('researches') or f.get('res'),
        'upgrades_to': overrides.get('upgrade') or f.get('upg') or f.get('upgrades_to'),
        'abillist': overrides.get('abillist') or f.get('abillist'),
        'heroabillist': overrides.get('heroabillist') or f.get('heroabillist'),
        'upgrades': overrides.get('upgrades') or f.get('upgrades'),
        'builds': overrides.get('builds') or f.get('builds'),
        'hp': overrides.get('hp') or f.get('hp'),
        'mana': overrides.get('mana') or f.get('mana0') or f.get('mana'),
        'def': overrides.get('def') or f.get('def'),
        'deftype': overrides.get('deftype') or f.get('deftype'),
        'atktype1': overrides.get('atktype1') or f.get('atktype1'),
        'atktype2': overrides.get('atktype2') or f.get('atktype2'),
        'dice1': overrides.get('dice1') or f.get('dice1'),
        'sides1': overrides.get('sides1') or f.get('sides1'),
        'dmgplus1': overrides.get('dmgplus1') or f.get('dmgplus1'),
        'cool1': overrides.get('cool1') or f.get('cool1'),
        'targs1': overrides.get('targs1') or f.get('targs1'),
        'weaptype1': overrides.get('weaptp1') or f.get('weaptype1'),
        'dice2': overrides.get('dice2') or f.get('dice2'),
        'sides2': overrides.get('sides2') or f.get('sides2'),
        'dmgplus2': overrides.get('dmgplus2') or f.get('dmgplus2'),
        'cool2': overrides.get('cool2') or f.get('cool2'),
        'targs2': overrides.get('targs2') or f.get('targs2'),
        'weaptype2': overrides.get('weaptp2') or f.get('weaptype2'),
        'fmade': overrides.get('fmade') or f.get('fmade'),
        'fused': overrides.get('fused') or f.get('fused'),
        'goldcost': overrides.get('goldcost') or f.get('goldcost'),
        'lumbercost': overrides.get('lumbercost') or f.get('lumbercost'),
        'bldtm': overrides.get('bldtm') or f.get('bldtm'),
        'editorsuffix': resolve(overrides.get('editorsuffix') or f.get('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_ability(aid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    levels = int(overrides.get('levels') or f.get('levels') or 1)
    tips = {}
    ubertips = {}
    for i in range(1, levels + 1):
        raw_t = overrides.get(f'tip{i}') or f.get(f'tip{i}')
        raw_ub = overrides.get(f'ubertip{i}') or f.get(f'ubertip{i}')
        tips[f'tip{i}'] = {'raw': raw_t, 'val': resolve(raw_t)}
        ubertips[f'ubertip{i}'] = {'raw': raw_ub, 'val': resolve(raw_ub)}
    raw_hk = overrides.get('hotkey') or f.get('hotkey')
    raw_rtip = overrides.get('researchtip') or f.get('researchtip')
    raw_rub = overrides.get('researchubertip') or f.get('researchubertip')
    raw_rhk = overrides.get('researchhotkey') or f.get('researchhotkey')
    return {
        'id': aid,
        'raw_name': overrides.get('name') or f.get('name'),
        'name': resolve(overrides.get('name') or f.get('name')),
        'levels': levels,
        'hotkey': resolve(raw_hk),
        'raw_hotkey': raw_hk,
        'researchhotkey': resolve(raw_rhk),
        'raw_researchhotkey': raw_rhk,
        'raw_researchtip': raw_rtip,
        'researchtip': resolve(raw_rtip),
        'raw_researchubertip': raw_rub,
        'researchubertip': resolve(raw_rub),
        'tips': tips,
        'ubertips': ubertips,
        'editorsuffix': resolve(overrides.get('editorsuffix') or f.get('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_upgrade(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    levels = int(overrides.get('maxlevel') or overrides.get('levels') or f.get('maxlevel') or f.get('levels') or 1)
    names = {}
    tips = {}
    ubertips = {}
    hotkeys = {}
    for i in range(1, levels + 1):
        raw_n = overrides.get(f'name{i}') or f.get(f'name{i}') or overrides.get('name') or f.get('name')
        raw_t = overrides.get(f'tip{i}') or f.get(f'tip{i}')
        raw_ub = overrides.get(f'ubertip{i}') or f.get(f'ubertip{i}')
        raw_hk = overrides.get(f'hotkey{i}') or f.get(f'hotkey{i}') or overrides.get('hotkey') or f.get('hotkey')
        names[f'name{i}'] = {'raw': raw_n, 'val': resolve(raw_n)}
        tips[f'tip{i}'] = {'raw': raw_t, 'val': resolve(raw_t)}
        ubertips[f'ubertip{i}'] = {'raw': raw_ub, 'val': resolve(raw_ub)}
        hotkeys[f'hotkey{i}'] = {'raw': raw_hk, 'val': resolve(raw_hk)}
    return {
        'id': uid,
        'levels': levels,
        'raw_class': overrides.get('class') or f.get('class'),
        'names': names,
        'tips': tips,
        'ubertips': ubertips,
        'hotkeys': hotkeys,
        'editorsuffix': resolve(overrides.get('editorsuffix') or f.get('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_buff(bid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    return {
        'id': bid,
        'raw_bufftip': overrides.get('bufftip') or f.get('bufftip'),
        'bufftip': resolve(overrides.get('bufftip') or f.get('bufftip')),
        'raw_buffubertip': overrides.get('buffubertip') or f.get('buffubertip'),
        'buffubertip': resolve(overrides.get('buffubertip') or f.get('buffubertip')),
        'raw_editorname': overrides.get('editorname') or f.get('editorname'),
        'editorname': resolve(overrides.get('editorname') or f.get('editorname')),
        'fields': f,
        'overrides': overrides
    }

def main():
    print("=== INSPECTING OGRES (RACE 28) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A17N')
    selection_markers = [inspect_upgrade('R0HT')]

    # 2. Buildings (11)
    bld_ids = [
        'o035', 'o03D', 'o03E', 'o036', 'o037', 'o038',
        'o03A', 'o039', 'o03J', 'o03C', 'o03B'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Units (19 = 1 worker + 16 regular + 2 summons)
    unit_ids = [
        'o03W',
        'o03F', 'o03G', 'o03H', 'o03I', 'o03K', 'o03L', 'o03M',
        'o03N', 'o03O', 'o03P', 'o03Q', 'o03R', 'o03S', 'o03T',
        'o03U', 'o03V',
        'n05M', 'n05N'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 4. Heroes (4)
    hero_ids = ['N05J', 'N05K', 'N05L', 'N05O']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 5. Upgrades (19)
    ogre_upgrade_ids = [
        'R0HT',
        'R0GL', 'R0GM', 'R0GN', 'R0GO', 'R0GP', 'R0GQ',
        'R09W', 'R0GU', 'R0L2',
        'R0GR', 'R0GS', 'R0GT',
        'R0GF', 'R0GG', 'R0GH', 'R0GI', 'R0GJ', 'R0GK'
    ]
    upgrade_data = [inspect_upgrade(u) for u in ogre_upgrade_ids]

    # 6. Abilities (36)
    ogre_ability_ids = [
        # Selection
        'A17N',
        # Worker & Units
        'A0I3', 'ANha', 'Arep',
        'A176', 'A177', 'A178', 'A179', 'A17A', 'A17B', 'A17O', 'A0WU',
        'A17D', 'A17E', 'A17C', 'A17F', 'A1RA', 'A1R6', 'A1R7', 'A1R8',
        'A17G', 'A17H', 'A17I', 'A17M', 'A17L', 'A17K',
        'A189', 'A18A',
        # Heroes N05J, N05K, N05L
        'A16Y', 'A170', 'A175', 'A171',
        'A173', 'A172', 'A174',
        'A16V', 'A16U', 'A16X', 'A16W',
        # Hero N05O
        'A18U', 'A18Q', 'A18R', 'A18S', 'A1LF', 'A01C',
        # Shared hero inventory
        'AInv'
    ]
    # Remove duplicates preserving order
    seen_abils = set()
    unique_ability_ids = []
    for a in ogre_ability_ids:
        if a not in seen_abils:
            seen_abils.add(a)
            unique_ability_ids.append(a)

    ability_data = [inspect_ability(a) for a in unique_ability_ids]

    # 7. Buffs
    buff_ids = [
        'B083', 'B097', 'B098', 'B081',
        'BUfa', 'BUts', 'Bspl', 'Bliq', 'Bblo', 'Bfzy', 'Blsh', 'B05G'
    ]
    buff_data = [inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/ogres_raw_dump.json"
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
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
