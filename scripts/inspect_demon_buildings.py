# -*- coding: utf-8 -*-
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

blds = ['h0DS', 'h0DT', 'h0DU', 'h0DV', 'h0DW', 'h0DX', 'h0DY', 'h0DZ', 'h0E0', 'h0E1', 'n02C']
wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

for b in blds:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', b])
    f = res.get('object', {}) or res.get('fields', {})
    name = resolve(f.get('name'))
    tip = resolve(f.get('tip'))
    ubertip = resolve(f.get('ubertip'))
    trains = f.get('trains')
    reser = f.get('researches')
    upg = f.get('upgrades_to') or f.get('upg') or f.get('upgrade')
    hotkey = f.get('hotkey')
    abils = f.get('abils')
    bpos = (f.get('buttonpos_1'), f.get('buttonpos_2'))
    print(f"=== {b}: {name} ===")
    print(f"  raw name: {f.get('name')}")
    print(f"  tip: {f.get('tip')} -> {repr(tip)}")
    print(f"  ubertip: {f.get('ubertip')} -> {repr(ubertip)}")
    print(f"  trains: {trains}")
    print(f"  researches: {reser}")
    print(f"  upgrades_to: {upg}")
    print(f"  hotkey: {hotkey} ({repr(resolve(hotkey))})")
    print(f"  buttonpos: {bpos}")
    print(f"  abils: {abils}")
    print()
