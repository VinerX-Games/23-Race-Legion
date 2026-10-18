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

hero_abils = [
    'AOhw', 'A1DL', 'AOsw', 'AOvd',
    'A1DR', 'A1DA', 'A1DS', 'A1EB',
    'A1EE', 'A1ED', 'A1EC', 'A1EF',
    'A1CE', 'A1CB', 'A1CC', 'A1CD',
    'A1PD', 'A1PE', 'A1PF', 'A1PG', 'A1PH',
    'A1CA'
]

results = []
for aid in hero_abils:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    lvls = int(fields.get('levels', '1'))
    entry = {
        'id': aid,
        'code': fields.get('code', aid),
        'levels': lvls,
        'name': res(fields.get('name', '')),
        'hotkey': res(fields.get('hotkey', '')),
        'researchhotkey': res(fields.get('researchhotkey', '')),
        'researchtip': res(fields.get('researchtip', '')),
        'researchubertip': res(fields.get('researchubertip', '')),
        'levels_data': []
    }
    for l in range(1, lvls + 1):
        entry['levels_data'].append({
            'level': l,
            'tip': res(fields.get(f'tip{l}', '')),
            'ubertip': res(fields.get(f'ubertip{l}', '')),
            'untip': res(fields.get(f'untip{l}', '')),
            'unubertip': res(fields.get(f'unubertip{l}', ''))
        })
    results.append(entry)
    print(f"=== {aid} (lvls={lvls}, code={entry['code']}) name='{entry['name']}' hotkey='{entry['hotkey']}' rhotkey='{entry['researchhotkey']}' ===")
    print(f"  rtip: {entry['researchtip']}")
    rub = entry['researchubertip']
    if rub and len(rub) > 80: rub = rub[:80] + '...'
    print(f"  rub:  {rub}")
    for ld in entry['levels_data']:
        u = ld['ubertip']
        if u and len(u) > 60: u = u[:60] + '...'
        print(f"  lvl {ld['level']}: tip='{ld['tip']}' ubertip='{u}'")

(ROOT / "docs" / "ui_text" / "ice_troll_hero_abilities_raw.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
