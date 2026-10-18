# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

catalog = json.loads((ROOT / "scripts/twilight_strings_catalog.json").read_text(encoding="utf-8"))

print(f"Total entries in catalog: {len(catalog)}")

field_types = {}
for sid, occurrences in catalog.items():
    fields = set(o['field'] for o in occurrences)
    val = occurrences[0]['current_val']
    for f in fields:
        field_types[f] = field_types.get(f, 0) + 1

for f, count in sorted(field_types.items(), key=lambda x: -x[1]):
    print(f"{f:20s}: {count}")
