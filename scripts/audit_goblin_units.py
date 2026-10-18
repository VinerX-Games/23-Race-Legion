# -*- coding: utf-8 -*-
"""Audit Goblin units: fields, WTS keys, abilities, attacks."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
raw_path = ROOT / "docs/ui_text/goblin_units_raw.json"
units = json.loads(raw_path.read_text(encoding="utf-8"))

print(f"Total units audited: {len(units)}")
wts_to_units = {}

for uid, u in sorted(units.items()):
    n_raw = u.get("name_raw")
    t_raw = u.get("tip_raw")
    ub_raw = u.get("ubertip_raw")
    hotkey = u.get("hotkey")
    abils = u.get("abillist")
    atk1 = f"{u.get('mindmg1')}-{u.get('maxdmg1')} ({u.get('atktype1')}/{u.get('weaptp1')}, cool: {u.get('cool1')}, targs: {u.get('targs1')})" if u.get('mindmg1') != ' - ' and u.get('mindmg1') is not None else "None"
    atk2 = f"{u.get('mindmg2')}-{u.get('maxdmg2')} ({u.get('atktype2')}/{u.get('weaptp2')}, cool: {u.get('cool2')}, targs: {u.get('targs2')})" if u.get('mindmg2') != ' - ' and u.get('mindmg2') is not None else "None"
    
    print(f"[{uid}] {u.get('name')} | hotkey={hotkey}")
    print(f"   Name raw: {n_raw} | Tip raw: {t_raw} | Ubertip raw: {ub_raw}")
    print(f"   Abils: {abils}")
    print(f"   Atk1: {atk1}")
    if atk2 != "None":
        print(f"   Atk2: {atk2}")
    print(f"   Old Ubertip: {u.get('ubertip')[:80]}...")
    print("-" * 50)

    for f_name, raw_val in [("name", n_raw), ("tip", t_raw), ("ubertip", ub_raw)]:
        if isinstance(raw_val, str) and raw_val.startswith("TRIGSTR_"):
            sid = int(raw_val[8:])
            wts_to_units.setdefault(sid, []).append((uid, f_name))

print("\nShared WTS check across units:")
shared = {sid: refs for sid, refs in wts_to_units.items() if len(refs) > 1}
if shared:
    for sid, refs in shared.items():
        print(f"  TRIGSTR_{sid}: used by {refs}")
else:
    print("  All WTS strings are unique across units!")
