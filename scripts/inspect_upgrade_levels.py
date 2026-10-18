# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from wc3_object_tools import cli
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        sid = int(s[8:])
        return sid, wts.get(sid, "")
    return None, s

d2 = json.load(open("scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

res_dict = {}
for uid in d2["upgrades"]:
    res = cli(["get-object", "--type", "upgrade", "--id", uid])
    obj = res.get("object", {}) or res.get("fields", {})
    maxl = int(obj.get("maxlevel") or 1)
    res_dict[uid] = {"maxlevel": maxl, "levels": {}}
    for lvl in range(1, maxl + 1):
        name_k = f"name{lvl}"
        tip_k = f"tip{lvl}"
        ub_k = f"ubertip{lvl}"
        hot_k = f"hotkey{lvl}"
        res_dict[uid]["levels"][lvl] = {
            "name": r(obj.get(name_k)),
            "tip": r(obj.get(tip_k)),
            "ubertip": r(obj.get(ub_k)),
            "hotkey": r(obj.get(hot_k))
        }

Path("scripts/illidari_upgrades_levels.json").write_text(json.dumps(res_dict, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved scripts/illidari_upgrades_levels.json")
