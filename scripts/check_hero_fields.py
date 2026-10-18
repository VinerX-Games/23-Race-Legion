# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

for h in d['heroes']:
    hid = h['id']
    print(f"[{hid}] raw_prop={h.get('raw_propernames')} raw_awaken={h.get('raw_awakentip')} raw_revive={h.get('raw_revivetip')}")
