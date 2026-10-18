# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

buildings = ["h070", "h073", "h074", "h075", "h076", "h077", "h079", "h07S", "o016", "h0D7"]

for b in buildings:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", b])
    f = res.get("object", {}) or res.get("fields", {})
    name = resolve(f.get("name"))
    print(f"=== [{b}] {name} ===")
    for k in ["train", "upro", "researches", "reserches", "ures", "sellunits", "uslu", "sellitems", "usli", "upgrades", "uver"]:
        if k in f and f[k]:
            print(f"  {k}: {f[k]}")
