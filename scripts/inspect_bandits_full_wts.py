# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

blds = ['h007', 'h008', 'h009', 'h00A', 'h00B', 'h00O', 'h01V', 'h01W', 'h03O', 'h03P', 'h03Q', 'h03R', 'h051', 'h07G', 'h0DF', 'h0DG', 'h0DH']
heroes = ['H03S', 'H047', 'H048']
units = ['h002', 'h003', 'h005', 'h006', 'h00P', 'h00Q', 'h00S', 'h00U', 'h029', 'h02A', 'h02B', 'h02Q', 'h02R', 'h02S', 'h02T', 'h02U', 'h03K', 'h03L', 'h03N', 'n000', 'n002', 'n004', 'o00C']

print("=== 1. BUILDINGS ===")
for b in blds:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', b])
    f = res.get('object', {}) or res.get('fields', {})
    print(f"Bld {b}:")
    print(f"  name: {f.get('name')} -> {resolve(f.get('name'))!r}")
    print(f"  tip: {f.get('tip')} -> {resolve(f.get('tip'))!r}")
    print(f"  ubertip: {f.get('ubertip')} -> {resolve(f.get('ubertip'))!r}")
    print(f"  hotkey: {f.get('hotkey')} -> {resolve(f.get('hotkey'))!r}")
    print(f"  trains: {f.get('trains')}")
    print(f"  researches: {f.get('researches')}")
    print(f"  upgrades_to: {f.get('upgrades_to') or f.get('upg')}")

print("\n=== 2. HEROES ===")
for h in heroes:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', h])
    f = res.get('object', {}) or res.get('fields', {})
    print(f"Hero {h}:")
    print(f"  name: {f.get('name')} -> {resolve(f.get('name'))!r}")
    print(f"  propernames: {f.get('propernames')} -> {resolve(f.get('propernames'))!r}")
    print(f"  tip: {f.get('tip')} -> {resolve(f.get('tip'))!r}")
    print(f"  ubertip: {f.get('ubertip')} -> {resolve(f.get('ubertip'))!r}")
    print(f"  hotkey: {f.get('hotkey')} -> {resolve(f.get('hotkey'))!r}")
    print(f"  heroabils: {f.get('heroabils') or f.get('heroabillist')}")
    print(f"  targs1: {f.get('targs1')}, weaptype1: {f.get('weaptype1')}")

print("\n=== 3. UNITS ===")
for u in units:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', u])
    f = res.get('object', {}) or res.get('fields', {})
    print(f"Unit {u}:")
    print(f"  name: {f.get('name')} -> {resolve(f.get('name'))!r}")
    print(f"  tip: {f.get('tip')} -> {resolve(f.get('tip'))!r}")
    print(f"  ubertip: {f.get('ubertip')} -> {resolve(f.get('ubertip'))!r}")
    print(f"  hotkey: {f.get('hotkey')} -> {resolve(f.get('hotkey'))!r}")
    print(f"  abillist: {f.get('abillist')}")
    print(f"  targs1: {f.get('targs1')}, weaptype1: {f.get('weaptype1')}")
