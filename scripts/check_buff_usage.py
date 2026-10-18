# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

for ab in d['abilities']:
    aid = ab['id']
    f = {**ab.get('fields', {}), **ab.get('overrides', {})}
    for k, v in f.items():
        if isinstance(v, str) and any(b in v for b in ['B01O', 'B02W', 'B03Y', 'B05H', 'B05J', 'B05L']):
            print(f"Ability {aid} uses buff {v} (field {k})")
