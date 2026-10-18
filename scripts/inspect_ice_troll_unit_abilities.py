# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

unit_abils = [
    'A10O', 'A1CL', 'A1CM', 'A1CN', 'A1CO', 'A1CP', 'A1CR', 'A1CS', 'A1CT', 'A1CV',
    'A1CW', 'A1D6', 'A1D7', 'A1DP', 'A1FF', 'A1FU', 'A1FV', 'A1FX', 'A1FY', 'A1OV',
    'A1OW', 'A1P4', 'A1P5', 'A1P6', 'A1P9', 'A1PA', 'A1PB', 'A1PC', 'A1PI', 'A1PJ', 'S00F'
]

# Load unit mappings from ice_troll_units.json and ice_troll_heroes.json
u_map = {}
units_json_path = ROOT / "docs" / "ui_text" / "ice_troll_units.json"
if units_json_path.exists():
    u_data = json.loads(units_json_path.read_text(encoding="utf-8"))
    for item in u_data.get("objects_before", {}).get("SD", []):
        uid = item.get("id")
        fields = item.get("fields", {})
        uname = res(fields.get("name", ""))
        abils = [a.strip() for a in fields.get("abillist", "").split(",") if a.strip()]
        u_map[uid] = {"name": uname, "abils": abils}

results = []
for aid in unit_abils:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    lvls = int(fields.get('levels', '1'))
    
    holders = []
    for uid, uinfo in u_map.items():
        if aid in uinfo['abils']:
            holders.append(f"{uid} ({uinfo['name']})")
            
    resolved_fields = {}
    for k, v in fields.items():
        resolved_fields[k] = res(v)
        
    entry = {
        'id': aid,
        'code': fields.get('code', aid),
        'levels': lvls,
        'name': res(fields.get('name', '')),
        'hotkey': res(fields.get('hotkey', '')),
        'unhotkey': res(fields.get('unhotkey', '')),
        'holders': holders,
        'levels_data': [],
        'fields': resolved_fields
    }
    for l in range(1, lvls + 1):
        t_key = f'tip{l}' if f'tip{l}' in fields else ('tip' if l == 1 else '')
        u_key = f'ubertip{l}' if f'ubertip{l}' in fields else ('ubertip' if l == 1 else '')
        un_t_key = f'untip{l}' if f'untip{l}' in fields else ('untip' if l == 1 else '')
        un_u_key = f'unubertip{l}' if f'unubertip{l}' in fields else ('unubertip' if l == 1 else '')
        entry['levels_data'].append({
            'level': l,
            'tip': res(fields.get(t_key, '')),
            'ubertip': res(fields.get(u_key, '')),
            'untip': res(fields.get(un_t_key, '')),
            'unubertip': res(fields.get(un_u_key, ''))
        })
    results.append(entry)
    print(f"=== {aid} (lvls={lvls}, code={entry['code']}) name='{entry['name']}' hotkey='{entry['hotkey']}' unhotkey='{entry['unhotkey']}' holders={holders} ===")
    for ld in entry['levels_data']:
        u = ld['ubertip']
        if u and len(u) > 80: u = u[:80] + '...'
        print(f"  lvl {ld['level']}: tip='{ld['tip']}' ubertip='{u}'")
        if ld['untip'] or ld['unubertip']:
            print(f"    untip='{ld['untip']}' unubertip='{ld['unubertip']}'")

(ROOT / "docs" / "ui_text" / "ice_troll_unit_abilities_raw.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print("\nSaved raw data to docs/ui_text/ice_troll_unit_abilities_raw.json")
