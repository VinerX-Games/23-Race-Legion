# -*- coding: utf-8 -*-
"""Base inspection helper for WC3 Race UI text standardization.
Provides reusable helpers to inspect units, abilities, upgrades, buffs,
extract TRIGSTR IDs, and crawl tech trees.
"""
from pathlib import Path
import json
import sys
import re

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def extract_wts_id(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

def inspect_unit(uid, raw_data=None):
    res = raw_data if raw_data is not None else hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    
    get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
    
    return {
        'id': uid,
        'name_sid': extract_wts_id(get_v('name')),
        'raw_name': get_v('name'),
        'name': resolve(get_v('name')),
        'tip_sid': extract_wts_id(get_v('tip')),
        'raw_tip': get_v('tip'),
        'tip': resolve(get_v('tip')),
        'ubertip_sid': extract_wts_id(get_v('ubertip')),
        'ubertip': resolve(get_v('ubertip')),
        'raw_propernames': get_v('propernames'),
        'propernames': resolve(get_v('propernames')),
        'raw_awakentip': get_v('awakentip'),
        'awakentip': resolve(get_v('awakentip')),
        'raw_revivetip': get_v('revivetip'),
        'revivetip': resolve(get_v('revivetip')),
        'raw_hotkey': get_v('hotkey'),
        'hotkey': resolve(get_v('hotkey')),
        'train': get_v('trains') or get_v('train'),
        'researches': get_v('researches') or get_v('res'),
        'upgrades_to': get_v('upgrade') or get_v('upg') or get_v('upgrades_to'),
        'abillist': get_v('abillist'),
        'heroabillist': get_v('heroabillist'),
        'upgrades': get_v('upgrades'),
        'builds': get_v('builds'),
        'hp': get_v('hp'),
        'mana': get_v('mana') or get_v('mana0'),
        'def': get_v('def'),
        'deftype': get_v('deftype'),
        'atktype1': get_v('atktype1'),
        'atktype2': get_v('atktype2'),
        'dice1': get_v('dice1'),
        'sides1': get_v('sides1'),
        'dmgplus1': get_v('dmgplus1'),
        'cool1': get_v('cool1'),
        'targs1': get_v('targs1'),
        'weaptype1': get_v('weaptp1') or get_v('weaptype1'),
        'dice2': get_v('dice2'),
        'sides2': get_v('sides2'),
        'dmgplus2': get_v('dmgplus2'),
        'cool2': get_v('cool2'),
        'targs2': get_v('targs2'),
        'weaptype2': get_v('weaptp2') or get_v('weaptype2'),
        'fmade': get_v('fmade'),
        'fused': get_v('fused'),
        'goldcost': get_v('goldcost'),
        'lumbercost': get_v('lumbercost'),
        'bldtm': get_v('bldtm'),
        'editorsuffix': resolve(get_v('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_ability(aid, raw_data=None):
    res = raw_data if raw_data is not None else hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
    
    levels = int(get_v('levels') or 1)
    tips = {}
    ubertips = {}
    for i in range(1, levels + 1):
        raw_t = get_v(f'tip{i}')
        raw_ub = get_v(f'ubertip{i}')
        tips[f'tip{i}'] = {'raw': raw_t, 'val': resolve(raw_t), 'sid': extract_wts_id(raw_t)}
        ubertips[f'ubertip{i}'] = {'raw': raw_ub, 'val': resolve(raw_ub), 'sid': extract_wts_id(raw_ub)}
        
    raw_n = get_v('name')
    raw_hk = get_v('hotkey')
    raw_rtip = get_v('researchtip')
    raw_rub = get_v('researchubertip')
    raw_rhk = get_v('researchhotkey')
    
    # Check untip/unubertip for toggles / autocasts
    raw_untip = get_v('untip')
    raw_unub = get_v('unubertip')
    raw_unhk = get_v('unhotkey')
    
    return {
        'id': aid,
        'raw_name': raw_n,
        'name': resolve(raw_n),
        'name_sid': extract_wts_id(raw_n),
        'levels': levels,
        'hotkey': resolve(raw_hk),
        'raw_hotkey': raw_hk,
        'researchhotkey': resolve(raw_rhk),
        'raw_researchhotkey': raw_rhk,
        'raw_researchtip': raw_rtip,
        'researchtip': resolve(raw_rtip),
        'researchtip_sid': extract_wts_id(raw_rtip),
        'raw_researchubertip': raw_rub,
        'researchubertip': resolve(raw_rub),
        'researchubertip_sid': extract_wts_id(raw_rub),
        'raw_untip': raw_untip,
        'untip': resolve(raw_untip),
        'untip_sid': extract_wts_id(raw_untip),
        'raw_unubertip': raw_unub,
        'unubertip': resolve(raw_unub),
        'unubertip_sid': extract_wts_id(raw_unub),
        'raw_unhotkey': raw_unhk,
        'unhotkey': resolve(raw_unhk),
        'tips': tips,
        'ubertips': ubertips,
        'editorsuffix': resolve(get_v('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_upgrade(uid, raw_data=None):
    res = raw_data if raw_data is not None else hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
    
    levels = int(get_v('maxlevel') or get_v('levels') or 1)
    names = {}
    tips = {}
    ubertips = {}
    hotkeys = {}
    for i in range(1, levels + 1):
        raw_n = get_v(f'name{i}') or get_v('name')
        raw_t = get_v(f'tip{i}')
        raw_ub = get_v(f'ubertip{i}')
        raw_hk = get_v(f'hotkey{i}') or get_v('hotkey')
        names[f'name{i}'] = {'raw': raw_n, 'val': resolve(raw_n), 'sid': extract_wts_id(raw_n)}
        tips[f'tip{i}'] = {'raw': raw_t, 'val': resolve(raw_t), 'sid': extract_wts_id(raw_t)}
        ubertips[f'ubertip{i}'] = {'raw': raw_ub, 'val': resolve(raw_ub), 'sid': extract_wts_id(raw_ub)}
        hotkeys[f'hotkey{i}'] = {'raw': raw_hk, 'val': resolve(raw_hk)}
    return {
        'id': uid,
        'levels': levels,
        'raw_class': get_v('class'),
        'names': names,
        'tips': tips,
        'ubertips': ubertips,
        'hotkeys': hotkeys,
        'editorsuffix': resolve(get_v('editorsuffix')),
        'fields': f,
        'overrides': overrides
    }

def inspect_buff(bid, raw_data=None):
    res = raw_data if raw_data is not None else hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    overrides = res.get('overrides', {})
    get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
    
    raw_bt = get_v('bufftip')
    raw_bub = get_v('buffubertip')
    raw_ed = get_v('editorname')
    
    return {
        'id': bid,
        'raw_bufftip': raw_bt,
        'bufftip': resolve(raw_bt),
        'bufftip_sid': extract_wts_id(raw_bt),
        'raw_buffubertip': raw_bub,
        'buffubertip': resolve(raw_bub),
        'buffubertip_sid': extract_wts_id(raw_bub),
        'raw_editorname': raw_ed,
        'editorname': resolve(raw_ed),
        'editorname_sid': extract_wts_id(raw_ed),
        'fields': f,
        'overrides': overrides
    }

def bulk_inspect_units(uids):
    res = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--ids', ','.join(uids)])
    raw_map = {item['id']: item for item in res.get('objects', [])}
    return [inspect_unit(uid, raw_data=raw_map.get(uid)) for uid in uids]

def bulk_inspect_abilities(aids):
    res = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--ids', ','.join(aids)])
    raw_map = {item['id']: item for item in res.get('objects', [])}
    return [inspect_ability(aid, raw_data=raw_map.get(aid)) for aid in aids]

def bulk_inspect_upgrades(uids):
    res = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--ids', ','.join(uids)])
    raw_map = {item['id']: item for item in res.get('objects', [])}
    return [inspect_upgrade(uid, raw_data=raw_map.get(uid)) for uid in uids]

def bulk_inspect_buffs(bids):
    res = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--ids', ','.join(bids)])
    raw_map = {item['id']: item for item in res.get('objects', [])}
    return [inspect_buff(bid, raw_data=raw_map.get(bid)) for bid in bids]
