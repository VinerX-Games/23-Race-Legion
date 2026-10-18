# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw
from implement_draenei_rework import object_records

wts = hw.load_wts_strings()

def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

# Collect all upgrades from Ice Troll buildings
b1 = json.loads((ROOT / 'docs/ui_text/ice_troll_buildings_01.json').read_text(encoding='utf-8'))
b2 = json.loads((ROOT / 'docs/ui_text/ice_troll_buildings_02.json').read_text(encoding='utf-8'))
units_doc = json.loads((ROOT / 'docs/ui_text/ice_troll_units.json').read_text(encoding='utf-8'))

bldg_researches = set()
for item in b1.get('objects_before', {}).get('SD', []):
    res_list = [r.strip() for r in item.get('fields', {}).get('researches', '').split(',') if r.strip()]
    bldg_researches.update(res_list)

for item in b2.get('objects_before', {}).get('SD', {}).get('buildings', []):
    res_list = [r.strip() for r in item.get('fields', {}).get('researches', '').split(',') if r.strip()]
    bldg_researches.update(res_list)

unit_upgrades = set()
for item in units_doc.get('objects_before', {}).get('SD', []):
    upg_list = [u.strip() for u in item.get('fields', {}).get('upgrades', '').split(',') if u.strip()]
    unit_upgrades.update(upg_list)

print("Researches in Ice Troll buildings:", sorted(bldg_researches))
print("Upgrades on Ice Troll units:", sorted(unit_upgrades))

all_troll_upgrades = sorted(bldg_researches | unit_upgrades)
# Exclude shared naval upgrades: R005, R006, R007, R002, R003 (already updated)
naval_shared = {'R002', 'R003', 'R005', 'R006', 'R007'}
troll_specific_upgrades = [u for u in all_troll_upgrades if u not in naval_shared]

print(f"\nTroll specific upgrades ({len(troll_specific_upgrades)}):", troll_specific_upgrades)

# Inspect each upgrade via HiveWE
results = []
for qid in troll_specific_upgrades:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', qid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    lvls = int(fields.get('levels', '1'))
    code = fields.get('code', qid)
    name = res(fields.get('name', ''))
    hotkey = res(fields.get('hotkey', ''))
    
    # check which buildings research this
    researchers = []
    for item in b1.get('objects_before', {}).get('SD', []):
        if qid in item.get('fields', {}).get('researches', ''):
            researchers.append(f"{item['id']} ({item.get('name', '')})")
    for item in b2.get('objects_before', {}).get('SD', {}).get('buildings', []):
        if qid in item.get('fields', {}).get('researches', ''):
            researchers.append(f"{item['id']} ({item.get('name', '')})")
            
    # check which units benefit from this
    consumers = []
    for item in units_doc.get('objects_before', {}).get('SD', []):
        if qid in item.get('fields', {}).get('upgrades', ''):
            consumers.append(f"{item['id']} ({item.get('name', '')})")

    entry = {
        'id': qid,
        'code': code,
        'name': name,
        'levels': lvls,
        'hotkey': hotkey,
        'researchers': researchers,
        'consumers': consumers,
        'levels_data': [],
        'fields': {k: res(v) for k, v in fields.items()}
    }
    
    for l in range(1, lvls + 1):
        t_key = f'tip{l}' if f'tip{l}' in fields else ('tip' if l == 1 else '')
        u_key = f'ubertip{l}' if f'ubertip{l}' in fields else ('ubertip' if l == 1 else '')
        entry['levels_data'].append({
            'level': l,
            'name': res(fields.get(f'name{l}', fields.get('name', ''))),
            'tip': res(fields.get(t_key, '')),
            'ubertip': res(fields.get(u_key, ''))
        })
        
    results.append(entry)
    print(f"=== {qid} (code={code}, lvls={lvls}) name='{name}' hotkey='{hotkey}' ===")
    print(f"  Researchers: {researchers}")
    print(f"  Consumers: {consumers}")
    for ld in entry['levels_data']:
        u = ld['ubertip']
        if u and len(u) > 80: u = u[:80] + '...'
        print(f"  L{ld['level']}: tip='{ld['tip']}' ubertip='{u}'")

(ROOT / 'docs/ui_text/ice_troll_research_raw.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nSaved raw research data to docs/ui_text/ice_troll_research_raw.json")
