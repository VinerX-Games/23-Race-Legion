# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

wts_text = (ROOT / "map.w3x/war3map.wts").read_text(encoding="utf-8")
cat = json.loads((ROOT / "scripts/scarlet_strings_catalog.json").read_text(encoding="utf-8"))

def has_sid(sid):
    import re
    return bool(re.search(rf"STRING 0*{sid}\s*\{{\s*\r?\n", wts_text))

valid_sids = {}
for sid_str, usages in cat.items():
    sid = int(sid_str)
    if has_sid(sid):
        valid_sids[sid] = usages

print(f"Total valid WTS strings for Scarlet: {len(valid_sids)}")
