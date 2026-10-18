# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from wc3_object_tools import cli

d2 = json.load(open("scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

inline_fields = []
wts_fields = []

for aid, ab in d2["abils"].items():
    res = cli(["get-object", "--type", "ability", "--id", aid])
    obj = res.get("object", {}) or res.get("fields", {})
    lvls = int(obj.get("levels") or 1)
    for lvl in range(1, lvls + 1):
        for prefix in ["tip", "ubertip", "untip", "unubertip"]:
            fld = f"{prefix}{lvl}"
            val = obj.get(fld)
            if val is not None:
                if str(val).startswith("TRIGSTR_"):
                    wts_fields.append((aid, fld, val))
                else:
                    inline_fields.append((aid, fld, val))
    # also check researchtip and researchubertip and name
    for fld in ["name", "researchtip", "researchubertip"]:
        val = obj.get(fld)
        if val is not None:
            if str(val).startswith("TRIGSTR_"):
                wts_fields.append((aid, fld, val))
            else:
                inline_fields.append((aid, fld, val))

print(f"Abilities WTS fields: {len(wts_fields)}")
print(f"Abilities inline fields: {len(inline_fields)}")
for item in inline_fields:
    print("  INLINE:", item)
