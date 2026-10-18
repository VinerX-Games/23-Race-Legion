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

abils = [
    'A0I3', 'A0IQ', 'A0LI', 'A0LJ', 'A0W1', 'A10O', 'A15N', 'A1CA', 'A1CB', 'A1CC',
    'A1CD', 'A1CE', 'A1CL', 'A1CM', 'A1CN', 'A1CO', 'A1CP', 'A1CR', 'A1CS', 'A1CT',
    'A1CV', 'A1CW', 'A1D6', 'A1D7', 'A1DA', 'A1DL', 'A1DP', 'A1DR', 'A1DS', 'A1EB',
    'A1EC', 'A1ED', 'A1EE', 'A1EF', 'A1FF', 'A1FR', 'A1FS', 'A1FU', 'A1FV', 'A1FX',
    'A1FY', 'A1KB', 'A1OV', 'A1OW', 'A1P4', 'A1P5', 'A1P6', 'A1P9', 'A1PA', 'A1PB',
    'A1PC', 'A1PD', 'A1PE', 'A1PF', 'A1PG', 'A1PH', 'A1PI', 'A1PJ', 'AInv', 'AOhw',
    'AOsw', 'AOvd', 'Abds', 'Ahar', 'Aorb', 'Arbr', 'Arep', 'Argl', 'Arlm', 'Aspi', 'S00F'
]

out = []
for aid in abils:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    name = res(fields.get('name', ''))
    suffix = res(fields.get('editorsuffix', ''))
    code = fields.get('code', aid)
    hero = fields.get('hero', '0')
    levels = fields.get('levels', '1')
    race = fields.get('race', '')
    out.append({
        'id': aid,
        'name': name,
        'suffix': suffix,
        'code': code,
        'hero': hero,
        'levels': levels,
        'race': race,
        'raw_fields': fields
    })

print(f"Total: {len(out)}")
for item in sorted(out, key=lambda x: (x['hero'], x['id'])):
    print(f"{item['id']} [hero={item['hero']}, lvl={item['levels']}, race={item['race']}] name='{item['name']}' suffix='{item['suffix']}' code={item['code']}")

(ROOT / "docs" / "ui_text" / "ice_troll_ability_audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
