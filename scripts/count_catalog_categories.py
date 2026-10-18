# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

cat = json.loads((ROOT / "scripts/scarlet_strings_catalog.json").read_text(encoding="utf-8"))

categories = {}
for sid_str, usages in cat.items():
    sid = int(sid_str)
    for u in usages:
        c = u['category']
        if c not in categories:
            categories[c] = set()
        categories[c].add(sid)

print("Unique strings per category:")
for c, sids in sorted(categories.items()):
    print(f"  {c}: {len(sids)} strings")
