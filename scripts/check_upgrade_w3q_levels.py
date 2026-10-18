# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from implement_draenei_rework import object_records

research_ids = [
    'R0D4',
    'R04P', 'R04E', 'R04F', 'R04G', 'R04H', 'R04I', 'R04J', 'R04K', 'R04L', 'R04M',
    'R056', 'R07A', 'R05X', 'R05Y', 'R04N', 'R04Q', 'R04R', 'R053', 'R05W'
]

v, tables = object_records((ROOT / 'map.w3x/war3map.w3q').read_bytes(), extended=True)
custom = {r['id']: r for r in tables[1] if r['id'] in research_ids}

for rid in research_ids:
    r = custom.get(rid)
    if r:
        base = r['header'][:4].decode('latin1')
        mod_levels = {}
        for (f, lvl, ptr), raw_data in r['mods']:
            mod_levels.setdefault(f, set()).add(lvl)
        print(f"[{rid}] base={base}")
        for f in ['gnam', 'gtp1', 'gub1', 'ghk1']:
            if f in mod_levels:
                print(f"   {f}: levels {sorted(list(mod_levels[f]))}")
