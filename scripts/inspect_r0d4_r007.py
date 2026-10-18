# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

bulk = require(cli(['get-objects-bulk', '--type', 'upgrade', '--ids', 'R0D4,R007']))
for o in bulk['objects']:
    print(f"\n[{o['id']}] levels={o['fields'].get('levels')}")
    for k in sorted(o['fields'].keys()):
        if any(k.startswith(p) for p in ['name', 'tip', 'ubertip', 'hotkey', 'effect', 'base', 'mod']):
            print(f"  {k}: {repr(resolve(o['fields'][k]))}")
