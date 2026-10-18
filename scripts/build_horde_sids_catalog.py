# -*- coding: utf-8 -*-
"""Build exact catalog of all WTS string IDs for Horde objects."""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/horde_raw_dump.json").read_text(encoding="utf-8"))

def extract_obj_sids(oid, odata, otype):
    res = {}
    f = odata.get('fields', {})
    
    # Direct properties
    for k in ['raw_name', 'raw_tip', 'raw_ubertip', 'raw_propernames', 'raw_hotkey']:
        val = odata.get(k)
        if isinstance(val, str) and val.startswith('TRIGSTR_'):
            sid = int(val[8:])
            field_name = k[4:] # strip raw_
            res[sid] = (otype, oid, field_name, wts.get(sid, ''))
            
    # For upgrades / abilities / units, check fields dictionary
    for k, val in f.items():
        if isinstance(val, str) and val.startswith('TRIGSTR_'):
            sid = int(val[8:])
            res[sid] = (otype, oid, k, wts.get(sid, ''))
            
    return res

catalog = {}
categories = {
    'selection': dump.get('selection', {}),
    'selection_markers': dump.get('selection_markers', {}),
    'buildings': dump.get('buildings', {}),
    'heroes': dump.get('heroes', {}),
    'units': dump.get('units', {}),
    'abilities': dump.get('abilities', {}),
    'researches': dump.get('researches', {}),
    'buffs': dump.get('buffs', {})
}

for cat_name, objs in categories.items():
    for oid, odata in objs.items():
        if not odata or not isinstance(odata, dict):
            continue
        obj_sids = extract_obj_sids(oid, odata, cat_name)
        for sid, info in obj_sids.items():
            if sid not in catalog:
                catalog[sid] = []
            catalog[sid].append(info)

print(f"Total unique SIDs found across Horde objects: {len(catalog)}")

# Save catalog to json
out = {}
for sid, occurrences in sorted(catalog.items()):
    out[sid] = {
        'occurrences': occurrences,
        'current_val': wts.get(sid, '')
    }

(ROOT / "scripts/horde_sids_catalog.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved to scripts/horde_sids_catalog.json")
