# -*- coding: utf-8 -*-
"""Dump detailed ability and upgrade data for Illidari and Bandits."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def inspect_ability(aid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
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
        'raw_hotkey': f.get('hotkey'),
        'hotkey': resolve(f.get('hotkey')),
        'raw_researchhotkey': f.get('researchhotkey'),
        'researchhotkey': resolve(f.get('researchhotkey')),
        'raw_researchtip': f.get('researchtip'),
        'researchtip': resolve(f.get('researchtip')),
        'raw_researchubertip': f.get('researchubertip'),
        'researchubertip': resolve(f.get('researchubertip')),
        'tips': tips,
        'ubertips': ubertips,
        'untips': untips,
        'unubertips': unubertips,
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
    # Illidari abils & upgrades
    ill_abils = ['AHfs', 'AHbn', 'AHdr', 'AHpx', 'AEmb', 'AEim', 'AEev', 'A0NZ', 'A0UV', 'A0NJ', 'A0NS', 'A0NU', 'A0NF', 'A0NX', 'A0NW', 'A0NV', 'A0O2', 'A0O5', 'A0OH', 'A0OG', 'A1GU', 'A0OF', 'A0OE', 'A0O1', 'A0O0', 'A048', 'A1KL', 'A1KO', 'A0NI', 'A0NT', 'A0NY', 'A0NO', 'A0NM', 'A0NP', 'A0NK', 'A0NR', 'A0NL', 'A0NQ', 'A0NN']
    ill_upgs = ['R08W', 'R08T', 'R08U', 'R08V', 'R08X', 'R096', 'R099', 'R09A', 'R09B', 'R08Y', 'R091', 'R095', 'R08Z', 'R090', 'R094', 'R092', 'R093', 'R097', 'R098', 'R07H', 'R0KZ', 'R0L0']

    # Bandits abils & upgrades
    ban_abils = ['A01J', 'A01D', 'A01H', 'A01I', 'A023', 'ANrf', 'AHab', 'ANlm', 'A0WV', 'A026', 'A028', 'A029', 'Aamk']
    ban_upgs = ['R00J', 'R00L', 'R00M', 'R00V', 'R00U', 'R00X', 'R00K', 'R00N', 'R00W', 'R0HP', 'R00Y', 'R00G']

    ill_dump = {
        'abils': {aid: inspect_ability(aid) for aid in ill_abils},
        'upgrades': {uid: inspect_upgrade(uid) for uid in ill_upgs}
    }
    with open(ROOT / 'scripts/illidari_abils_upgrades_dump.json', 'w', encoding='utf-8') as f:
        json.dump(ill_dump, f, ensure_ascii=False, indent=2)
    print("Saved illidari_abils_upgrades_dump.json")

    ban_dump = {
        'abils': {aid: inspect_ability(aid) for aid in ban_abils},
        'upgrades': {uid: inspect_upgrade(uid) for uid in ban_upgs}
    }
    with open(ROOT / 'scripts/bandits_abils_upgrades_dump.json', 'w', encoding='utf-8') as f:
        json.dump(ban_dump, f, ensure_ascii=False, indent=2)
    print("Saved bandits_abils_upgrades_dump.json")

if __name__ == '__main__':
    main()
