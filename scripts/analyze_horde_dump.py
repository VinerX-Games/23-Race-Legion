# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

dump = json.loads((ROOT / "scripts/horde_raw_dump.json").read_text(encoding="utf-8"))

def analyze_obj(oid, odata, otype):
    name = odata.get('name') or ''
    if not name and 'names' in odata:
        name = odata['names'].get('name1', {}).get('val') or ''
    raw_name = odata.get('raw_name') or ''
    if not raw_name and 'names' in odata:
        raw_name = odata['names'].get('name1', {}).get('raw') or ''
    raw_tip = odata.get('raw_tip') or ''
    if not raw_tip and 'tips' in odata:
        raw_tip = odata['tips'].get('tip1', {}).get('raw') or ''
    tip = odata.get('tip') or ''
    if not tip and 'tips' in odata:
        tip = odata['tips'].get('tip1', {}).get('val') or ''
    raw_ub = odata.get('raw_ubertip') or ''
    if not raw_ub and 'ubertips' in odata:
        raw_ub = odata['ubertips'].get('ubertip1', {}).get('raw') or ''
    ub = odata.get('ubertip') or ''
    if not ub and 'ubertips' in odata:
        ub = odata['ubertips'].get('ubertip1', {}).get('val') or ''
    return {
        'id': oid,
        'type': otype,
        'name': name,
        'raw_name': raw_name,
        'tip': tip,
        'raw_tip': raw_tip,
        'ubertip': ub[:80] + '...' if len(ub) > 80 else ub,
        'raw_ub': raw_ub,
        'hotkey': odata.get('hotkey'),
        'propernames': odata.get('propernames')
    }

print("=== SELECTION ===")
for k, v in dump['selection'].items():
    print(k, analyze_obj(k, v, 'ability'))

print("\n=== SELECTION MARKERS ===")
for k, v in dump['selection_markers'].items():
    print(k, analyze_obj(k, v, 'upgrade'))

print("\n=== BUILDINGS ===")
for k, v in dump['buildings'].items():
    print(k, analyze_obj(k, v, 'building'))

print("\n=== HEROES ===")
for k, v in dump['heroes'].items():
    print(k, analyze_obj(k, v, 'hero'))

print("\n=== UNITS ===")
for k, v in dump['units'].items():
    res = analyze_obj(k, v, 'unit')
    print(f"{k}: name='{res['name']}' raw_name='{res['raw_name']}' tip='{res['tip']}'")

print("\n=== RESEARCHES ===")
for k, v in dump['researches'].items():
    res = analyze_obj(k, v, 'upgrade')
    print(f"{k}: name='{res['name']}' raw_name='{res['raw_name']}' tip='{res['tip']}'")

print("\n=== ABILITIES ===")
for k, v in dump['abilities'].items():
    res = analyze_obj(k, v, 'ability')
    print(f"{k}: name='{res['name']}' raw_name='{res['raw_name']}' tip='{res['tip']}'")
