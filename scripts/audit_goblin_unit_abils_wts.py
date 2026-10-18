# -*- coding: utf-8 -*-
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

abil_ids = [
    'A0AW', 'A0AV', 'A0A6', 'A0D6', 'A0AX', 'A0D2', 'A0Z4', 'A0D1', 'A0AB',
    'A0AR', 'A0A8', 'A0A7', 'A0A5', 'A0BL', 'A0A9', 'A1MT', 'A0LG', 'A0LF',
    'A0A4', 'A0D3', 'A0D4', 'Asds', 'A0AH', 'A0BK', 'A0AS', 'A0AT', 'A0AU',
    'A0KS', 'A0LD', 'A0LE', 'A0LH', 'S001', 'A15N', 'A0UU'
]
buff_ids = ['B028', 'B02H', 'B02I', 'B087', 'B02A', 'B02J', 'B02V', 'B02W', 'B089']

# Read all files to find WTS references
files_to_check = [
    ROOT / "map.w3x" / name
    for name in [
        "war3map.w3u", "war3map.w3t", "war3map.w3a", "war3map.w3b",
        "war3map.w3d", "war3map.w3q", "war3map.w3h",
        "war3mapSkin.w3u", "war3mapSkin.w3t", "war3mapSkin.w3a",
        "war3mapSkin.w3b", "war3mapSkin.w3d", "war3mapSkin.w3q",
        "war3mapSkin.w3h"
    ]
    if (ROOT / "map.w3x" / name).exists()
]

bulk_a = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(abil_ids)]))
bulk_b = require(cli(['get-objects-bulk', '--type', 'buff', '--ids', ','.join(buff_ids)]))

used_wts = {}
for obj in bulk_a.get('objects', []) + bulk_b.get('objects', []):
    oid = obj['id']
    for k, v in obj.get('fields', {}).items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            wts_id = int(v[8:])
            used_wts.setdefault(wts_id, []).append((oid, k))

# Now scan all map binaries for occurrences of TRIGSTR_NNNN
binary_contents = {f.name: f.read_bytes() for f in files_to_check}

shared_wts = {}
unique_wts = {}

for wts_id, refs in used_wts.items():
    s_bytes = f"TRIGSTR_{wts_id}".encode("ascii")
    # also check zero-padded forms if any
    all_hits = []
    for fname, data in binary_contents.items():
        count = data.count(s_bytes)
        if count > 0:
            all_hits.append((fname, count))
    total_hits = sum(c for _, c in all_hits)
    if total_hits > len(refs) or any(not fn.endswith(('w3a', 'w3h')) for fn, _ in all_hits):
        shared_wts[wts_id] = {"refs": refs, "hits": all_hits}
    else:
        unique_wts[wts_id] = {"refs": refs, "hits": all_hits}

print(f"Total WTS keys examined: {len(used_wts)}")
print(f"Unique WTS keys: {len(unique_wts)}")
print(f"Shared WTS keys: {len(shared_wts)}")
for wid, info in shared_wts.items():
    print(f"  TRIGSTR_{wid}: refs={info['refs']} hits={info['hits']}")
