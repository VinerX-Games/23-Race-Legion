# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

dump_path = ROOT / "scripts/twilight_hammer_raw_dump.json"
dump = json.loads(dump_path.read_text(encoding="utf-8"))

lines = (ROOT / "scripts/twilight_abilities_dump.txt").read_text(encoding="utf-8").split("\n\n")

print(f"Total blocks in dump: {len(lines)}")
for block in lines:
    first_line = block.splitlines()[0]
    aid = first_line.split()[2]
    # check if custom or standard
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {})
    ov = res.get('overrides', {})
    name = resolve(f.get('name'))
    raw_name = f.get('name')
    has_trigstr = any(isinstance(v, str) and 'TRIGSTR_' in v for v in [f.get('name'), f.get('tip1'), f.get('ubertip1'), f.get('researchtip'), f.get('researchubertip')])
    print(f"{aid}: name={name!r} (raw: {raw_name}) | has_wts={has_trigstr} | overrides_count={len(ov)}")
