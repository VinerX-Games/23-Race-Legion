# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

candidates = ['h06W', 'h0DM', 'h06V', 'h06X', 'h070', 'h07R', 'h071', 'h072', 'h06K', 'h060', 'h06Q', 'h06L', 'h06N', 'h078', 'h06M', 'h06P', 'h06S', 'h06U', 'h06Y', 'h06R', 'h06T', 'o00W', 'o00X', 'o00Y', 'H0BD', 'N018', 'N019', 'N01A', 'Nalc', 'Ntin', 'Galh', 'Gmex']

for uid in candidates:
    res = hw.run_cli_json(['get-object', '--map', str(ROOT / 'map.w3x'), '--type', 'unit', '--id', uid])
    if res.get('ok'):
        f = res.get('object', {}) or res.get('fields', {})
        name = resolve(f.get("name"))
        suffix = resolve(f.get("editorsuffix"))
        isbldg = f.get("isbldg")
        train = f.get("train")
        upgrades = f.get("upgrades")
        builds = f.get("builds")
        print(f"[{uid}] {name} ({suffix}) -> isbldg={isbldg}, train={train}, upg={upgrades}, builds={builds}")
    else:
        print(f"[{uid}] NOT FOUND")
