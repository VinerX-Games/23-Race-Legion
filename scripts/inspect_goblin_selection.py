# -*- coding: utf-8 -*-
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

args = ["get-object", "--map", str(hw.DEFAULT_MAP), "--type", "ability", "--id", "A0AC"]
data = hw.run_cli_json(args)
obj = data.get("object", {}) or data.get("fields", {})

wts = hw.load_wts_strings()
print("Raw fields for A0AC:")
for k in ["name", "tip", "tip1", "ubertip", "ubertip1", "hotkey", "editorsuffix"]:
    val = obj.get(k)
    print(f"  {k}: {val}")
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        sid = int(val[8:])
        print(f"    -> string {sid}: {repr(wts.get(sid))}")
