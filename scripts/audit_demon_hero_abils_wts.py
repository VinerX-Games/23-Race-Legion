# -*- coding: utf-8 -*-
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

hero_abils = [
    'A0M8', 'A0MB', 'A0MC', 'A0M9', # N02F
    'A0MF', 'A0MA', 'A0ME', 'A0MD', # N02A
    'A0MG', 'A0MO', 'A0MN', 'A0MP', # U028
    'A0NG', 'A0ND', 'A0NB', 'A0NC', # N02G (+ trigger spell A0NC)
    'A0NA', 'A1BY', 'A0N7', 'A0N8', 'A1BV', # N02B (+ trigger spell A0N8)
    'A0MV', 'A0MU', 'A0MT', # N02H
    'A0MS', 'A0MR', 'A0MQ', 'S006', # U027
]

all_wts = []
abil_details = {}

for aid in hero_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    lvls = int(f.get('levels', 1) or 1)
    name_raw = f.get('name')
    hotkey = resolve(f.get('hotkey'))
    
    details = {
        'name_raw': name_raw,
        'name': resolve(name_raw),
        'hotkey': hotkey,
        'levels': lvls,
        'tips': {},
        'ubertips': {},
        'researchtip': f.get('researchtip'),
        'researchubertip': f.get('researchubertip'),
    }
    
    for raw in [name_raw, f.get('researchtip'), f.get('researchubertip')]:
        if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
            all_wts.append(int(raw[8:]))
            
    for lvl in range(1, lvls + 1):
        tip_k = f'tip{lvl}' if f.get(f'tip{lvl}') else 'tip'
        ub_k = f'ubertip{lvl}' if f.get(f'ubertip{lvl}') else 'ubertip'
        tip_raw = f.get(tip_k)
        ub_raw = f.get(ub_k)
        details['tips'][lvl] = (tip_raw, resolve(tip_raw))
        details['ubertips'][lvl] = (ub_raw, resolve(ub_raw))
        
        for raw in [tip_raw, ub_raw]:
            if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
                all_wts.append(int(raw[8:]))
                
    abil_details[aid] = details

print(f"Total hero ability WTS references: {len(all_wts)} (unique: {len(set(all_wts))})")

# Check usage counts across binary files
bin_files = [
    ROOT / 'map.w3x/war3map.w3u',
    ROOT / 'map.w3x/war3mapSkin.w3u',
    ROOT / 'map.w3x/war3map.w3a',
    ROOT / 'map.w3x/war3mapSkin.w3a',
    ROOT / 'map.w3x/war3map.w3q',
    ROOT / 'map.w3x/war3mapSkin.w3q',
    ROOT / 'map.w3x/war3map.w3h',
    ROOT / 'map.w3x/war3mapSkin.w3h',
    ROOT / 'map.w3x/war3map.w3t',
    ROOT / 'map.w3x/war3mapSkin.w3t',
]

counts = {k: 0 for k in set(all_wts)}
for bf in bin_files:
    if not bf.exists(): continue
    raw = bf.read_bytes()
    for sid in counts.keys():
        target = f'TRIGSTR_{sid}'.encode('utf-8')
        counts[sid] += raw.count(target)

shared_warnings = []
for sid, cnt in sorted(counts.items()):
    if cnt > 1:
        shared_warnings.append((sid, cnt))

print(f"Shared WTS keys count: {len(shared_warnings)}")
for sid, cnt in shared_warnings:
    print(f"  SHARED: TRIGSTR_{sid}: {cnt} usages")

with open(ROOT / 'docs/ui_text/demon_hero_abils_raw.json', 'w', encoding='utf-8') as f:
    json.dump(abil_details, f, ensure_ascii=False, indent=2)
print("Saved demon_hero_abils_raw.json")
