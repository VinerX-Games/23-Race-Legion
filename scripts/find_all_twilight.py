# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

for t in ['unit', 'ability', 'upgrade', 'buff']:
    res = hw.run_cli_json(['find-objects', '--map', str(hw.DEFAULT_MAP), '--type', t, '--query', ''])
    objs = res.get('objects', [])
    print(f"=== TYPE {t.upper()}: {len(objs)} objects ===")
    matches = []
    for obj in objs:
        oid = obj.get('id', '')
        name = resolve(obj.get('name', ''))
        suffix = resolve(obj.get('suffix', ''))
        art = obj.get('art', '')
        # check criteria
        is_match = False
        text_str = f"{oid} {name} {suffix} {art}".lower()
        if any(w in text_str for w in ['сумереч', 'молот', 'ksmolot', 'культ', 'бездн']):
            is_match = True
        if is_match:
            matches.append((oid, name, suffix, art))
    print(f"Found {len(matches)} matches for {t}:")
    for m in matches:
        print(f"  {m[0]}: name={m[1]!r} suffix={m[2]!r} art={m[3]!r}")
