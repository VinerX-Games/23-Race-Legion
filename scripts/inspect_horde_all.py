# -*- coding: utf-8 -*-
"""Inspect all Horde (Race 14) objects from map object data and resolve WTS strings."""
import json
from pathlib import Path
import re
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
        tip_k = f'tip{i}' if f.get(f'tip{i}') else 'tip'
        ub_k = f'ubertip{i}' if f.get(f'ubertip{i}') else 'ubertip'
        tips[f'tip{i}'] = {'raw': f.get(tip_k), 'val': resolve(f.get(tip_k))}
        ubertips[f'ubertip{i}'] = {'raw': f.get(ub_k), 'val': resolve(f.get(ub_k))}
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
        'buttonpos': [f.get('buttonpos_1'), f.get('buttonpos_2')],
        'researchbuttonpos': [f.get('researchbuttonpos_1'), f.get('researchbuttonpos_2')],
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
        name_k = f'name{i}' if f.get(f'name{i}') else 'name'
        tip_k = f'tip{i}' if f.get(f'tip{i}') else 'tip'
        ub_k = f'ubertip{i}' if f.get(f'ubertip{i}') else 'ubertip'
        hk_k = f'hotkey{i}' if f.get(f'hotkey{i}') else 'hotkey'
        names[f'name{i}'] = {'raw': f.get(name_k), 'val': resolve(f.get(name_k))}
        tips[f'tip{i}'] = {'raw': f.get(tip_k), 'val': resolve(f.get(tip_k))}
        ubertips[f'ubertip{i}'] = {'raw': f.get(ub_k), 'val': resolve(f.get(ub_k))}
        hotkeys[f'hotkey{i}'] = {'raw': f.get(hk_k), 'val': resolve(f.get(hk_k))}
    return {
        'id': uid,
        'levels': levels,
        'class': f.get('class'),
        'names': names,
        'tips': tips,
        'ubertips': ubertips,
        'hotkeys': hotkeys,
        'effects': {
            'effect1': f.get('effect1'),
            'code1': f.get('code1'),
            'mod1': f.get('mod1'),
            'effect2': f.get('effect2'),
            'code2': f.get('code2'),
            'mod2': f.get('mod2'),
            'effect3': f.get('effect3'),
            'code3': f.get('code3'),
            'mod3': f.get('mod3'),
        },
        'applies_to': f.get('applies_to') or f.get('applies'),
        'fields': f
    }

def inspect_buff(bid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid])
    f = res.get('object', {}) or res.get('fields', {})
    return {
        'id': bid,
        'raw_name': f.get('name'),
        'name': resolve(f.get('name')),
        'raw_tip': f.get('tip'),
        'tip': resolve(f.get('tip')),
        'raw_ubertip': f.get('ubertip'),
        'ubertip': resolve(f.get('ubertip')),
        'fields': f
    }

def main():
    selection_ids = ['A0YV']
    selection_markers = ['R0DV', 'R0IR', 'R0J3']

    building_ids = [
        'ogre', 'ostr', 'ofrt', 'otrb', 'obar', 'obea',
        'owtw', 'ofor', 'oalt', 'osld', 'otto', 'ovln',
        'h0D3', 'h0HO'
    ]

    # Core units & variants
    unit_ids = [
        'opeo', 'ogru', 'o01N', 'otau', 'orai', 'ocat',
        'ohun', 'otbk', 'okod', 'o029', 'owyv', 'o01P',
        'oshm', 'odoc', 'ospw', 'o01W', 'o022', 'h0CY', 'h0OL',
        'o02B', 'h0HN', 'h0HK', 'h0D5', 'h0D4', 'h0D6',
        # Variants from Horde.lua / 05_horde.lua
        'o01I', 'o01E', 'o01F', 'o01H', 'o01J', 'o01K', 'o01L', 'o01M',
        'o01O', 'o01Q', 'o01R', 'o01S', 'o01T', 'o01U', 'o01V', 'o01X',
        'o01Y', 'o01Z', 'o020', 'o021', 'o023', 'o024', 'o025', 'o026',
        'o027', 'o028', 'o02A', 'o02C', 'o02D', 'o02E', 'o02F', 'o02G',
        'o02H', 'o02I', 'o02J', 'o02K', 'o02L', 'o02M', 'o02S', 'o02U',
        'o02W', 'o032', 'n04J', 'h0HM', 'h0HT', 'h0I5', 'h0IH', 'h0J3',
        'h0J4', 'h0JB', 'o00A'
    ]

    hero_ids = [
        'Obla', 'Ofar', 'Otch', 'Oshd', 'O02Z', 'O02P', 'Othr', 'H0BN'
    ]

    # Researches from 05_horde.lua and Horde.lua
    research_ids = [
        # Selection markers
        'R0DV', 'R0IR', 'R0J3',
        # Standard upgrades
        'Ropg', 'R0G5', 'R0E6', 'Rome', 'Roar', 'Rora', 'Rosp', 'Rorb',
        'R0EC', 'R0ED', 'R0EF', 'Rost', 'Rowt', 'Rowd',
        # Iron Horde & branch researches (17+)
        'R0F3', 'R0F4', 'R0EH', 'R0EI', 'R0EE', 'R0EA', 'R0E9', 'R0E5',
        'R0E4', 'R0E3', 'R0E1', 'R0E0', 'R0DZ', 'R0DY', 'R0DX', 'R0DW', 'R0EB',
        # Additional researches in Horde.lua
        'R0D1', 'R0D2', 'R0D3', 'R0E7', 'R0E8', 'R0KO'
    ]

    # Explicit abilities known from Horde.lua and 05_horde.lua
    known_abils = [
        'A0YV', 'A0YU', 'A0ZA', 'A0ZB', 'A0ZC', 'A0ZX', 'A103', 'A124', 'A129',
        'A12A', 'A12L', 'A12M', 'A12X', 'A12Y', 'A12Z', 'A13H', 'A13I', 'A14V',
        'A1LO', 'A1MG', 'A1OJ', 'A1OK', 'AOww', 'A12F', 'AOcr', 'A12E', 'AOcl',
        'AOsf', 'AOfs', 'AOre', 'AOr2', 'A026', 'Abds', 'Arlm', 'A15N'
    ]

    print("Inspecting Horde buildings...")
    blds = {}
    for b in building_ids:
        try:
            blds[b] = inspect_unit(b)
        except Exception as e:
            blds[b] = {'id': b, 'error': str(e)}

    print("Inspecting Horde heroes...")
    heroes = {}
    for h in hero_ids:
        try:
            data = inspect_unit(h)
            if data.get('name'):
                heroes[h] = data
        except Exception as e:
            heroes[h] = {'id': h, 'error': str(e)}

    print("Inspecting Horde units...")
    units = {}
    for u in unit_ids:
        try:
            data = inspect_unit(u)
            if data.get('name'):
                units[u] = data
        except Exception as e:
            units[u] = {'id': u, 'error': str(e)}

    all_abils = set(known_abils)
    all_researches = set(research_ids)

    # Discover abilities and researches attached to buildings, units, heroes
    for obj in list(blds.values()) + list(units.values()) + list(heroes.values()):
        if obj.get('abils'):
            for a in str(obj['abils']).split(','):
                a = a.strip()
                if a: all_abils.add(a)
        if obj.get('heroabils'):
            for a in str(obj['heroabils']).split(','):
                a = a.strip()
                if a: all_abils.add(a)
        if obj.get('researches'):
            for r in str(obj['researches']).split(','):
                r = r.strip()
                if r:
                    if r.startswith('R'):
                        all_researches.add(r)
                    else:
                        all_abils.add(r)
        if obj.get('upgrades'):
            for u in str(obj['upgrades']).split(','):
                u = u.strip()
                if u:
                    if u.startswith('R'):
                        all_researches.add(u)
                    else:
                        all_abils.add(u)

    print(f"Total abilities to inspect: {len(all_abils)}")
    print(f"Total researches to inspect: {len(all_researches)}")

    abils_data = {}
    for aid in sorted(all_abils):
        try:
            res = inspect_ability(aid)
            if res.get('name') or res.get('fields'):
                abils_data[aid] = res
        except Exception as e:
            abils_data[aid] = {'id': aid, 'error': str(e)}

    upgs_data = {}
    for uid in sorted(all_researches):
        try:
            res = inspect_upgrade(uid)
            if res.get('names') or res.get('fields'):
                upgs_data[uid] = res
        except Exception as e:
            upgs_data[uid] = {'id': uid, 'error': str(e)}

    # Buff candidates
    buff_candidates = ['BTLF', 'Bbsk', 'Bblo', 'Bsha', 'Bstt', 'Bspe', 'Bhow', 'Bhea', 'Beye']
    for aid, adata in abils_data.items():
        f = adata.get('fields', {})
        for k, v in f.items():
            if 'buff' in k.lower() and isinstance(v, str) and len(v) == 4:
                buff_candidates.append(v)
    buff_candidates = sorted(list(set(buff_candidates)))
    print(f"Total buffs to inspect: {len(buff_candidates)}")
    buffs_data = {}
    for bid in buff_candidates:
        try:
            b_res = inspect_buff(bid)
            if b_res.get('name') or b_res.get('fields'):
                buffs_data[bid] = b_res
        except Exception as e:
            buffs_data[bid] = {'id': bid, 'error': str(e)}

    dump = {
        'selection': {aid: abils_data.get(aid) for aid in selection_ids},
        'selection_markers': {mid: upgs_data.get(mid) for mid in selection_markers},
        'buildings': blds,
        'heroes': heroes,
        'units': units,
        'abilities': abils_data,
        'researches': upgs_data,
        'buffs': buffs_data
    }

    out_file = ROOT / "scripts/horde_raw_dump.json"
    out_file.write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Horde raw dump saved to {out_file} (size: {out_file.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
