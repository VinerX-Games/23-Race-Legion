# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

cat = json.loads((ROOT / "scripts/scarlet_strings_catalog.json").read_text(encoding="utf-8"))

fields_summary = {}
for sid_str, usages in cat.items():
    sid = int(sid_str)
    for u in usages:
        f = u['field']
        fields_summary[f] = fields_summary.get(f, 0) + 1

print("Fields in catalog:")
for f, count in sorted(fields_summary.items()):
    print(f"  {f}: {count}")
