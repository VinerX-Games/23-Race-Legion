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

lines = []
for aid, ab in d2["abils"].items():
    name = r(ab.get("raw_name") or ab.get("name"))
    flds = ab.get("fields", {})
    code = flds.get("code")
    lvls = ab.get("levels")
    hk = ab.get("hotkey")
    raw_hk = ab.get("raw_hotkey")
    wts_refs = []
    for k, v in flds.items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            wts_refs.append((k, int(v[8:]), r(v)[:30]))
    lines.append(f"{aid:4} | code: {str(code):4} | lvls: {str(lvls):1} | hk: {str(hk):4} | name: {name} | wts_count: {len(wts_refs)}")
    for fld, sid, val in wts_refs:
        lines.append(f"     {fld} -> STR_{sid}: {repr(val)}")

(ROOT / "scripts/illidari_abils_summary.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"Summary written: {len(lines)} lines")
