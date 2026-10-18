# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

for hid in ['W200', 'W201', 'W202', 'W203']:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    ov = res.get('overrides', {})
    print(f"=== HERO {hid} ===")
    for k in ['name', 'tip', 'ubertip', 'propernames', 'awakentip', 'revivetip', 'heroabillist', 'abillist', 'hotkey', 'atktype1', 'targs1', 'atktype2', 'targs2']:
        raw_val = ov.get(k) or f.get(k)
        print(f"  {k}: raw={raw_val} -> {resolve(raw_val)}")
