# -*- coding: utf-8 -*-
import json
import re
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

# Let's inspect each upgrade's base object and all fields
for obj in bulk.get('objects', []):
    rid = obj['id']
    f = obj['fields']
    base = obj.get('base') or f.get('code')
    # search lua for references
    import subprocess
    out = subprocess.check_output(['rg', f"'{rid}'", 'map.w3x/_lua/monolith_split'], text=True, errors='ignore')
    lua_lines = [l.strip() for l in out.splitlines() if l.strip()]
    print(f"[{rid}] name={resolve(f.get('name1') or f.get('name'))} base={base}")
    if lua_lines:
        for l in lua_lines[:3]:
            print(f"    Lua: {l}")
    else:
        print("    Lua: none")
