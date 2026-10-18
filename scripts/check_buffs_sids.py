# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

print(f"Total buffs in dump: {len(d['buffs'])}")
for b in d['buffs']:
    bid = b['id']
    btsid = b.get('bufftip_sid')
    bubsid = b.get('buffubertip_sid')
    if btsid or bubsid or bid.startswith('B0'):
        print(f"[{bid}] editorname={b.get('editorname')} btsid={btsid} bubsid={bubsid} tip={b.get('bufftip')!r}")
