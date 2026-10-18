# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()

def resolve(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        return wts.get(int(val[8:]), val)
    return val

raw_json = Path(ROOT / "docs/ui_text/goblins_unit_abils_raw.json")
data = json.loads(raw_json.read_text(encoding="utf-8"))
print(f"Total abilities in goblins_unit_abils_raw: {len(data)}")

for aid, info in data.items():
    code = info.get("code")
    name = resolve(info.get("name_raw"))
    hotkey = info.get("hotkey")
    lvls = info.get("levels")
    print(f"[{aid}] code={code} lvls={lvls} hotkey={hotkey} name={repr(name)}")
    print(f"    tip1: {info.get('tip1_raw')} -> {repr(resolve(info.get('tip1_raw')))}")
    print(f"    ubertip1: {info.get('ubertip1_raw')} -> {repr(resolve(info.get('ubertip1_raw')))}")
