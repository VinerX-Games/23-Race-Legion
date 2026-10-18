# -*- coding: utf-8 -*-
"""Inspect all Undead (Race 13) objects from map object data and resolve WTS strings."""
import json
from pathlib import Path
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
    selection_ids = ['A0HV']
    building_ids = ['n014', 'u00F', 'u00G', 'u00H', 'u00I', 'u00J', 'u00K', 'u00L', 'u00M', 'u00N', 'n012', 'u03B', 'u017', 'h0D1']
    unit_ids = ['u00P', 'n011', 'n013', 'u03E', 'u02B', 'u00A', 'u00B', 'u00D', 'u00C', 'u008', 'u00E', 'u034', 'h0CZ', 'h0D0', 'h0D2', 'ft00', 'ft01', 'n07H', 'u03D', 'n016', 'n017', 'CM00', 'FL00', 'Ujsm']
    hero_ids = ['U00O', 'U00V', 'U00U', 'U030', 'U014']
    
    hero_abil_ids = ['A0CO', 'A0CP', 'A0CR', 'A0CN', 'AQ95', 'UN99', 'A0CS', 'AQ11', 'A0CK', 'A0CM', 'A0BW', 'A1Q7', 'A1LI', 'A1LJ', 'A1LL', 'A1LM', 'A0WD', 'A0WE', 'A0WB', 'A0WC', 'A0WF', 'A1ND', 'A0CG', 'A0CA', 'A0CC']
    unit_abil_ids = ['A0BO', 'A0BP', 'A0C5', 'Sch2', 'Amel', 'Amed', 'A0C7', 'A0C8', 'A0BT', 'A0BU', 'A1PV', 'A0C4', 'Arpl', 'Arpm', 'A0BX', 'unA5', 'A1PY', 'A0C0', 'A0C2', 'A1PX', 'unA0', 'Aspa', 'A1N8', 'Arst', 'Auns', 'Afra', 'A0BR', 'Agyd', 'Arlm', 'A15N', 'A0LJ', 'A0LI', 'A0IQ', 'Argl', 'A1KB', 'A0GI', 'A1OS', 'A1E7', 'kel0']
    research_ids = ['R0DQ', 'R05I', 'R05J', 'R05N', 'R05O', 'R05P', 'R05Q', 'R05L', 'R05H', 'R05E', 'R05F', 'R05G', 'R05A', 'R05R', 'R05D', 'R05C', 'R07I', 'R0J5', 'R06Y']

    print("Inspecting Undead objects...")
    blds = {b: inspect_unit(b) for b in building_ids}
    units = {u: inspect_unit(u) for u in unit_ids}
    heroes = {h: inspect_unit(h) for h in hero_ids}
    
    # Discover all abilities referenced by units/heroes/buildings
    all_abils = set(hero_abil_ids + unit_abil_ids + selection_ids)
    all_researches = set(research_ids)
    
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

    print(f"Total abilities to inspect: {len(all_abils)}")
    print(f"Total researches to inspect: {len(all_researches)}")

    abils_data = {}
    for aid in sorted(all_abils):
        try:
            abils_data[aid] = inspect_ability(aid)
        except Exception as e:
            abils_data[aid] = {'id': aid, 'error': str(e)}

    upgs_data = {}
    for uid in sorted(all_researches):
        try:
            upgs_data[uid] = inspect_upgrade(uid)
        except Exception as e:
            upgs_data[uid] = {'id': uid, 'error': str(e)}

    # Check buffs
    buff_candidates = ['B08J', 'B08K', 'Bfro', 'Bapl', 'Bdev', 'Bcsd', 'Bpos', 'Bams', 'Bcrs', 'Bfro', 'Brai', 'Bspe', 'Bweb']
    # Also find buffs referenced in ability fields
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
            buffs_data[bid] = inspect_buff(bid)
        except Exception as e:
            buffs_data[bid] = {'id': bid, 'error': str(e)}

    out_file = ROOT / "scripts/undead_raw_dump.json"
    dump = {
        'selection': {aid: abils_data.get(aid) for aid in selection_ids},
        'buildings': blds,
        'units': units,
        'heroes': heroes,
        'abilities': abils_data,
        'researches': upgs_data,
        'buffs': buffs_data,
    }
    out_file.write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Dump saved to {out_file} (size: {out_file.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
