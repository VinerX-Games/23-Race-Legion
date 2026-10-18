# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

data = json.load(open('scripts/undead_complete_inventory.json', encoding='utf-8'))

for cat, objs in data.items():
    print(f"\n==================== {cat.upper()} ({len(objs)}) ====================")
    for oid, info in objs.items():
        sids = {k: v['sid'] for k, v in info['fields'].items() if v['sid']}
        vals = {k: v['current_val'] for k, v in info['fields'].items() if v['sid']}
        print(f"[{oid}] (lvls={info['levels']}) SIDs={len(sids)}")
        for k in sorted(sids.keys()):
            sid = sids[k]
            v = vals[k]
            # Print single line preview
            prev = repr(v) if v else 'None'
            if len(prev) > 80: prev = prev[:77] + "...'"
            print(f"    {k:20s}: SID {sid:5d} -> {prev}")
