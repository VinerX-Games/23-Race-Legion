# -*- coding: utf-8 -*-
"""Inspect all objects, abilities, and upgrades for the next 5 races:
16: Dalaran
17: KulTiras
18: Nightborne (ночнорожденные)
19: Draenei (дренеи)
20: Twilight Hammer (сумеречный Молот)
"""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def inspect_obj(oid, otype):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid])
    if not res.get('success'):
        return None
    f = res.get('object', {}) or res.get('fields', {})
    
    data = {
        'id': oid,
        'type': otype,
        'raw_name': f.get('name') or f.get('name1'),
        'name': resolve(f.get('name') or f.get('name1')),
        'fields': f
    }
    if otype == 'unit':
        data['raw_tip'] = f.get('tip')
        data['tip'] = resolve(f.get('tip'))
        data['raw_ubertip'] = f.get('ubertip')
        data['ubertip'] = resolve(f.get('ubertip'))
        data['raw_propernames'] = f.get('propernames')
        data['propernames'] = resolve(f.get('propernames'))
        data['raw_hotkey'] = f.get('hotkey')
        data['hotkey'] = resolve(f.get('hotkey'))
        data['trains'] = f.get('trains')
        data['researches'] = f.get('researches')
        data['upgrades_to'] = f.get('upgrades_to') or f.get('upg')
        data['abils'] = f.get('abils')
        data['heroabils'] = f.get('heroabils') or res.get('overrides', {}).get('heroabillist')
        data['upgrades'] = f.get('upgrades')
        data['builds'] = f.get('builds')
    elif otype == 'ability':
        levels = int(f.get('levels') or 1)
        data['levels'] = levels
        data['raw_hotkey'] = f.get('hotkey')
        data['hotkey'] = resolve(f.get('hotkey'))
        data['raw_researchhotkey'] = f.get('researchhotkey')
        data['researchhotkey'] = resolve(f.get('researchhotkey'))
        data['raw_researchtip'] = f.get('researchtip')
        data['researchtip'] = resolve(f.get('researchtip'))
        data['raw_researchubertip'] = f.get('researchubertip')
        data['researchubertip'] = resolve(f.get('researchubertip'))
        tips = {}
        ubertips = {}
        for i in range(1, levels + 1):
            tk = f'tip{i}' if f.get(f'tip{i}') else 'tip'
            uk = f'ubertip{i}' if f.get(f'ubertip{i}') else 'ubertip'
            tips[f'tip{i}'] = {'raw': f.get(tk), 'val': resolve(f.get(tk))}
            ubertips[f'ubertip{i}'] = {'raw': f.get(uk), 'val': resolve(f.get(uk))}
        data['tips'] = tips
        data['ubertips'] = ubertips
    elif otype == 'upgrade':
        levels = int(f.get('levels') or 1)
        data['levels'] = levels
        names = {}
        tips = {}
        ubertips = {}
        hotkeys = {}
        for i in range(1, levels + 1):
            nk = f'name{i}' if f.get(f'name{i}') else 'name'
            tk = f'tip{i}' if f.get(f'tip{i}') else 'tip'
            uk = f'ubertip{i}' if f.get(f'ubertip{i}') else 'ubertip'
            hk = f'hotkey{i}' if f.get(f'hotkey{i}') else 'hotkey'
            names[f'name{i}'] = {'raw': f.get(nk), 'val': resolve(f.get(nk))}
            tips[f'tip{i}'] = {'raw': f.get(tk), 'val': resolve(f.get(tk))}
            ubertips[f'ubertip{i}'] = {'raw': f.get(uk), 'val': resolve(f.get(uk))}
            hotkeys[f'hotkey{i}'] = {'raw': f.get(hk), 'val': resolve(f.get(hk))}
        data['names'] = names
        data['tips'] = tips
        data['ubertips'] = ubertips
        data['hotkeys'] = hotkeys
    return data

def main():
    race_queries = {
        'dalaran': ['Даларан', 'даларан'],
        'kultiras': ['Кул-Тирас', 'Кул тирас'],
        'nightborne': ['ночнорожденные', 'Ночнорожденные', 'ночнорождённые', 'Ночнорождённые'],
        'draenei': ['Дренеи', 'дренеи'],
        'twilight_hammer': ['Сумеречный Молот', 'сумеречный Молот']
    }
    
    # Also manual object lists from triggers / AI
    race_seeds = {
        'dalaran': {
            'selection': 'A0HN',
            'markers': ['R0BW', 'R0KK'],
            'worker': 'u001',
            'town_halls': ['h030']
        },
        'kultiras': {
            'selection': 'A0HO',
            'markers': ['R07D', 'R0HX'],
            'worker': 'h013',
            'town_halls': ['h01X', 'h01Y', 'h01Z']
        },
        'nightborne': {
            'selection': 'A0HU',
            'markers': ['R07J'],
            'worker': 'h0CJ',
            'town_halls': ['h0CB', 'h0CC', 'h0CD']
        },
        'draenei': {
            'selection': 'A0HS',
            'markers': ['R07G'],
            'worker': 'h012',
            'town_halls': []
        },
        'twilight_hammer': {
            'selection': 'A0HX',
            'markers': ['R07K', 'R0KD'],
            'worker': 'o00J',
            'town_halls': []
        }
    }

    results = {}
    for rkey, qlist in race_queries.items():
        print(f"Collecting data for {rkey}...")
        bld_ids = set()
        unt_ids = set()
        hero_ids = set()
        
        for q in qlist:
            res = hw.run_cli_json(['race', '--race', q])
            if res.get('success'):
                # parsing race output
                pass
            # Also let's inspect via raw HiveWE get-object or scan
        
        # Let's collect through seed objects & builds recursively
        seeds = race_seeds[rkey]
        worker = seeds['worker']
        worker_obj = inspect_obj(worker, 'unit')
        if worker_obj:
            builds = worker_obj.get('builds', '')
            if builds:
                for bid in builds.split(','):
                    bid = bid.strip()
                    if bid:
                        bld_ids.add(bid)
        for th in seeds['town_halls']:
            bld_ids.add(th)
            
        results[rkey] = {
            'seeds': seeds,
            'worker_data': worker_obj,
            'initial_buildings': sorted(list(bld_ids))
        }

    out_file = ROOT / "scripts/five_races_seeds.json"
    out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved initial seeds to {out_file}")

if __name__ == '__main__':
    main()
