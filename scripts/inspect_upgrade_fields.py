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
    'R0D4', 'R007',
    'R04P', 'R04E', 'R04F', 'R04G', 'R04H', 'R04I', 'R04J', 'R04K', 'R04L', 'R04M',
    'R056', 'R07A', 'R05X', 'R05Y', 'R04N', 'R04Q', 'R04R', 'R053', 'R05W'
]

bulk = require(cli(['get-objects-bulk', '--type', 'upgrade', '--ids', ','.join(research_ids)]))
for obj in bulk.get('objects', []):
    rid = obj['id']
    f = obj['fields']
    levels = f.get('levels', '1')
    code = f.get('code')
    print(f"\nUpgrade [{rid}] code={code} levels={levels}")
    for k in sorted(f.keys()):
        if any(k.startswith(p) for p in ['name', 'tip', 'ubertip', 'hotkey', 'effect', 'base', 'mod', 'code', 'class']):
            v = f[k]
            res_v = resolve(v)
            print(f"  {k}: {repr(v)} -> {repr(res_v)}")
