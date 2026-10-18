# -*- coding: utf-8 -*-
"""Collect all WTS strings for Horde objects and map them."""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

dump = json.loads((ROOT / "scripts/horde_raw_dump.json").read_text(encoding="utf-8"))

def extract_trigstrs(data):
    sids = []
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str) and v.startswith('TRIGSTR_'):
                try:
                    sids.append((k, int(v[8:]), v))
                except ValueError:
                    pass
            elif isinstance(v, (dict, list)):
                for sub_k, sid, raw in extract_trigstrs(v):
                    sids.append((f"{k}.{sub_k}", sid, raw))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            for sub_k, sid, raw in extract_trigstrs(item):
                sids.append((f"[{idx}].{sub_k}", sid, raw))
    return sids

all_sids = {}
category_objects = {
    'selection': dump.get('selection', {}),
    'selection_markers': dump.get('selection_markers', {}),
    'buildings': dump.get('buildings', {}),
    'heroes': dump.get('heroes', {}),
    'units': dump.get('units', {}),
    'abilities': dump.get('abilities', {}),
    'researches': dump.get('researches', {}),
    'buffs': dump.get('buffs', {})
}

summary = []

for cat, objs in category_objects.items():
    print(f"\n=================== {cat.upper()} ===================")
    cat_sids = set()
    for oid, odata in objs.items():
        if not odata or not isinstance(odata, dict):
            continue
        extracted = extract_trigstrs(odata)
        if extracted:
            print(f"Object [{oid}]: {odata.get('name') or odata.get('names', {}).get('name1', {}).get('val')}")
            for field, sid, raw in extracted:
                print(f"   field: {field:25s} -> STRING {sid}")
                all_sids[sid] = (cat, oid, field)
                cat_sids.add(sid)
    print(f"Total unique SIDs in {cat}: {len(cat_sids)}")

print(f"\n=======================================================")
print(f"TOTAL UNIQUE SIDS ACROSS ALL HORDE OBJECTS: {len(all_sids)}")
