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
    trains = f.get("trains") or f.get("train")
    researches = f.get("researches") or f.get("reserches")
    sellunits = f.get("sellunits")
    upgrades = f.get("upgrades")
    print(f"=== [{b}] {name} ===")
    if trains:
        print(f"  trains: {trains}")
        for uid in trains.split(","):
            uid = uid.strip()
            ures = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid])
            uf = ures.get("object", {}) or ures.get("fields", {})
            print(f"    - [{uid}] {resolve(uf.get('name'))} ({resolve(uf.get('editorsuffix'))})")
    if sellunits:
        print(f"  sellunits: {sellunits}")
        for uid in sellunits.split(","):
            uid = uid.strip()
            ures = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid])
            uf = ures.get("object", {}) or ures.get("fields", {})
            print(f"    - [{uid}] {resolve(uf.get('name'))} ({resolve(uf.get('editorsuffix'))})")
    if researches:
        print(f"  researches: {researches}")
        for rid in researches.split(","):
            rid = rid.strip()
            rres = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "upgrade", "--id", rid])
            rf = rres.get("object", {}) or rres.get("fields", {})
            print(f"    - [{rid}] {resolve(rf.get('name'))} ({resolve(rf.get('editorsuffix'))})")
    if upgrades:
        print(f"  upgrades: {upgrades}")
