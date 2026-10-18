# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

hero_ids = ['N02F', 'N02A', 'U028', 'N02G', 'N02B', 'N02H', 'U027']

for hid in hero_ids:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid])
    f = res.get('object', {}) or res.get('fields', {})
    name = resolve(f.get('name'))
    proper = resolve(f.get('propernames'))
    tip = resolve(f.get('tip'))
    ubertip = resolve(f.get('ubertip'))
    hotkey = resolve(f.get('hotkey'))
    habils = f.get('heroabils') or res.get('overrides', {}).get('heroabillist')
    print(f"=== {hid}: {name} ({proper}) ===")
    print(f"  name_raw: {f.get('name')}")
    print(f"  proper_raw: {f.get('propernames')}")
    print(f"  tip: {f.get('tip')} -> {repr(tip)}")
    print(f"  ubertip: {f.get('ubertip')} -> {repr(ubertip)}")
    print(f"  hotkey: {f.get('hotkey')} ({repr(hotkey)})")
    print(f"  heroabils: {habils}")
    print(f"  atk1: dice={f.get('dice1')} sides={f.get('sides1')} dmgplus={f.get('dmgplus1')} cool={f.get('cool1')} targs={f.get('targs1')}")
    print(f"  atk2: dice={f.get('dice2')} sides={f.get('sides2')} dmgplus={f.get('dmgplus2')} cool={f.get('cool2')} targs={f.get('targs2')}")
    print(f"  primary={f.get('primary')} hp={f.get('hp')} mana={f.get('mana0') or f.get('mana')} armor={f.get('def')} deftype={f.get('deftype')}")
    print()
