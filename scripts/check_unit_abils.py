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

unit_ids = ["h0EI", "h0EJ", "o01A", "o01B", "o019", "h0EK", "h0EL", "n02O", "n02M", "n02N", "h04Y", "h04Z", "h050", "H043", "E01W", "E024", "E025"]

for uid in unit_ids:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid])
    obj = res.get("object", {}) or res.get("fields", {})
    name = r(obj.get("name"))
    abils = obj.get("abils")
    heroabils = obj.get("heroabils")
    code = obj.get("code")
    print(f"[{uid}] code={code} name='{name}'")
    print(f"     abils={abils} heroabils={heroabils}")
    print(f"     upgrades={obj.get('upgrades')}")
    print(f"     trains={obj.get('trains')} builds={obj.get('builds')}")
