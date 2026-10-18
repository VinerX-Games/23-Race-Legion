# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        return wts.get(int(s[8:]), s)
    return s

d2 = json.load(open(ROOT / "scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

for aid, ab in d2["abils"].items():
    name = r(ab.get("raw_name") or ab.get("name"))
    print(f"=== Ability {aid} ({name}) lvls={ab.get('levels')} ===")
    for k, v in sorted(ab.items()):
        if k in ["name", "raw_name", "levels", "fields"]:
            continue
        if isinstance(v, dict):
            for subk, subv in sorted(v.items()):
                val = subv.get("val") if isinstance(subv, dict) else subv
                raw = subv.get("raw") if isinstance(subv, dict) else None
                print(f"  {k}.{subk}: {r(val)} [raw: {raw}]")
        else:
            print(f"  {k}: {v}")
