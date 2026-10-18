# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

cat = json.loads((ROOT / "scripts/scarlet_strings_catalog.json").read_text(encoding="utf-8"))

non_hotkey_sids = {}
hotkey_sids = {}

for sid_str, usages in cat.items():
    sid = int(sid_str)
    # Check if all usages are hotkeys
    is_hotkey = all('hotkey' in u['field'].lower() for u in usages)
    if is_hotkey:
        hotkey_sids[sid] = usages
    else:
        non_hotkey_sids[sid] = usages

print(f"Non-hotkey SIDs: {len(non_hotkey_sids)}")
print(f"Pure hotkey SIDs: {len(hotkey_sids)}")
