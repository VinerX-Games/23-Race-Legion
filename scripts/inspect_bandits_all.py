# -*- coding: utf-8 -*-
"""Inspect all Bandits race objects and output structured JSON and summary."""
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

def main():
    blds = ['h007', 'h008', 'h009', 'h00A', 'h00B', 'h00O', 'h01V', 'h01W', 'h03O', 'h03P', 'h03Q', 'h03R', 'h051', 'h07G', 'h0DF', 'h0DG', 'h0DH']
    units = ['h002', 'h003', 'h005', 'h006', 'h00P', 'h00Q', 'h00S', 'h00U', 'h029', 'h02A', 'h02B', 'h02Q', 'h02R', 'h02S', 'h02T', 'h02U', 'h03K', 'h03L', 'h03N', 'n000', 'n002', 'n004', 'o00C']
    heroes = ['H03S', 'H047', 'H048']

    bld_data = [inspect_unit(b) for b in blds]
    unit_data = [inspect_unit(u) for u in units]
    hero_data = [inspect_unit(h) for h in heroes]
    selection_data = inspect_ability('A0HR')

    print(f"=== BANDITS INSPECTION ===")
    print(f"Buildings: {len(bld_data)}")
    for b in bld_data:
        print(f"  {b['id']}: {b['name']} | tip={b['raw_tip']} | ubertip={b['raw_ubertip']} | hotkey={b['hotkey']}")
        print(f"     trains: {b['trains']} | researches: {b['researches']} | upgrades_to: {b['upgrades_to']}")

    print(f"\nUnits: {len(unit_data)}")
    for u in unit_data:
        print(f"  {u['id']}: {u['name']} | tip={u['raw_tip']} | ubertip={u['raw_ubertip']} | hotkey={u['hotkey']}")
        print(f"     abils: {u['abils']} | upgrades: {u['upgrades']} | atk1_targs={u['targs1']}")

    print(f"\nHeroes: {len(hero_data)}")
    for h in hero_data:
        print(f"  {h['id']}: {h['name']} ({h['propernames']}) | tip={h['raw_tip']} | ubertip={h['raw_ubertip']}")
        print(f"     heroabils: {h['heroabils']} | abils: {h['abils']} | atk1_targs={h['targs1']}")

    print(f"\nSelection ability A0HR:")
    print(f"  name: {selection_data['raw_name']} -> {selection_data['name']}")
    print(f"  tip1: {selection_data['tips'].get('tip1', {}).get('raw')} -> {selection_data['tips'].get('tip1', {}).get('val')}")
    print(f"  ubertip1: {selection_data['ubertips'].get('ubertip1', {}).get('raw')} -> {selection_data['ubertips'].get('ubertip1', {}).get('val')}")

    out_file = ROOT / "scripts/bandits_raw_dump.json"
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump({
            'selection': selection_data,
            'buildings': bld_data,
            'units': unit_data,
            'heroes': hero_data,
        }, f, ensure_ascii=False, indent=2)
    print(f"\nSaved raw dump to {out_file}")

if __name__ == '__main__':
    main()
