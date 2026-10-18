# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import inspect_race_base as ib
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

upg_ids = [
    'R0BV', 'R08G', 'R088',
    'R089', 'R08B', 'R085', 'R08A', 'R083', 'R084', 'R07Z', 'R07Y', 'R009', 'R07X',
    'R0D0',
    'R08C', 'R08D', 'R08F', 'R08E',
    'R086', 'R080', 'R081', 'R082',
    'R087'
]

upg_details = {}
for uid in upg_ids:
    u = ib.inspect_upgrade(uid)
    upg_details[uid] = u

with open(ROOT / "scripts/silitids_upgrades_check.json", "w", encoding="utf-8") as f:
    json.dump(upg_details, f, ensure_ascii=False, indent=2)

print(f"Inspected {len(upg_ids)} upgrades, saved to scripts/silitids_upgrades_check.json")
