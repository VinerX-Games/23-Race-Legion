# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

blds = ['h0CB', 'h0CC', 'h0CD', 'h0CE', 'h0CF', 'h0CG', 'h0CH', 'h0CI', 'h0CK', 'h0CL', 'h0CM', 'h0D8']
for b in blds:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', b, '--all'])
    ov = res.get('overrides', {})
    fd = res.get('fields', {})
    name = resolve(ov.get('name') or fd.get('name'))
    trains = ov.get('trains') or fd.get('trains')
    researches = ov.get('researches') or fd.get('researches')
    abils = ov.get('abillist') or fd.get('abillist')
    print(f"{b} ({name}):")
    print(f"  trains: {trains}")
    print(f"  researches: {researches}")
    print(f"  abils: {abils}")
