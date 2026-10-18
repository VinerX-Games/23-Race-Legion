# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

research_ids = [
    'R0D4',
    'R04P', 'R04E', 'R04F', 'R04G', 'R04H', 'R04I', 'R04J', 'R04K', 'R04L', 'R04M',
    'R056', 'R07A', 'R05X', 'R05Y', 'R04N', 'R04Q', 'R04R', 'R053', 'R05W'
]

bulk = require(cli(['get-objects-bulk', '--type', 'upgrade', '--ids', ','.join(research_ids)]))

all_upgrade_wts = {}
for obj in bulk.get('objects', []):
    rid = obj['id']
    f = obj['fields']
    for k, v in f.items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            wid = int(v[8:])
            all_upgrade_wts.setdefault(wid, []).append((rid, k))

print(f"Total WTS keys referenced by Goblin upgrades: {len(all_upgrade_wts)}")

# Check if any are shared with non-w3q files
binary_files = [
    "war3map.w3u", "war3map.w3t", "war3map.w3a", "war3map.w3b",
    "war3map.w3d", "war3map.w3h",
    "war3mapSkin.w3u", "war3mapSkin.w3t", "war3mapSkin.w3a",
    "war3mapSkin.w3b", "war3mapSkin.w3d", "war3mapSkin.w3h"
]
shared_with_other = {}
for wid, refs in all_upgrade_wts.items():
    s_bytes = f"TRIGSTR_{wid}".encode("ascii")
    hits = []
    for fn in binary_files:
        p = ROOT / "map.w3x" / fn
        if p.exists() and p.read_bytes().count(s_bytes) > 0:
            hits.append(fn)
    if hits:
        shared_with_other[wid] = {"refs": refs, "hits": hits}

print(f"WTS keys shared with non-w3q files: {len(shared_with_other)}")
for wid, info in shared_with_other.items():
    print(f"  TRIGSTR_{wid}: refs={info['refs']} hits={info['hits']}")
