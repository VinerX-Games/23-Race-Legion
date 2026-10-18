# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

r_ids = [
    "R0D4", "R007",
    "R04P", "R04E", "R04F", "R04G", "R04H", "R04I", "R04J", "R04K", "R04L", "R04M",
    "R056", "R07A", "R05X", "R05Y", "R04N", "R04Q", "R04R", "R053", "R05W"
]

for rid in r_ids:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "upgrade", "--id", rid])
    f = res.get("object", {}) or res.get("fields", {})
    name = resolve(f.get("name") or f.get("name1"))
    print(f"[{rid}] {name}")
