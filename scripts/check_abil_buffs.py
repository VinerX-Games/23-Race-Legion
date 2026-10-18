# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw
from wc3_object_tools import cli

wts = hw.load_wts_strings()
def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        return wts.get(int(s[8:]), s)
    return s

d2 = json.load(open("scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

print("=== Checking buff fields on abilities ===")
for aid in d2["abils"]:
    res = cli(["get-object", "--type", "ability", "--id", aid])
    obj = res.get("object", {}) or res.get("fields", {})
    name = r(obj.get("name"))
    buff1 = obj.get("buff1") or obj.get("abuf")
    buff2 = obj.get("buff2")
    if buff1 or buff2:
        print(f"Ability {aid} ({name}): buff1={buff1} buff2={buff2}")
