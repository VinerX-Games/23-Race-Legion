# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def resolve(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            sid = int(val[8:])
            return sid, wts.get(sid, "")
        except ValueError:
            return None, val
    return None, val

d1 = json.load(open(ROOT / "scripts/illidari_raw_dump.json", encoding="utf-8"))
d2 = json.load(open(ROOT / "scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

output_lines = []

def p(s=""):
    output_lines.append(s)

p("=== 1. SELECTION ===")
sel = d1["selection"]
sid_name, str_name = resolve(sel.get("raw_name"))
sid_tip, str_tip = resolve(sel.get("raw_tip"))
sid_ubertip, str_ubertip = resolve(sel.get("raw_ubertip"))
p(f"A0OK name: sid={sid_name} val={repr(str_name)}")
p(f"A0OK tip: sid={sid_tip} val={repr(str_tip)}")
p(f"A0OK ubertip: sid={sid_ubertip} val={repr(str_ubertip)}")
p(f"A0OK fields: {sel.get('fields')}")
p(f"A0OK hotkey: {sel.get('hotkey')}")

p("\n=== 2. BUILDINGS ===")
for b in d1["buildings"]:
    bid = b.get("id")
    p(f"Building: {bid}")
    for fld in ["name", "tip", "ubertip"]:
        sid, val = resolve(b.get(f"raw_{fld}"))
        p(f"  {fld}: sid={sid} raw={b.get(f'raw_{fld}')} val={repr(val)}")
    p(f"  trains={b.get('trains')} researches={b.get('researches')} upgrades_to={b.get('upgrades_to')} hotkey={b.get('hotkey')}")

p("\n=== 3. UNITS ===")
for u in d1["units"]:
    uid = u.get("id")
    p(f"Unit: {uid}")
    for fld in ["name", "tip", "ubertip"]:
        sid, val = resolve(u.get(f"raw_{fld}"))
        p(f"  {fld}: sid={sid} raw={u.get(f'raw_{fld}')} val={repr(val)}")
    p(f"  abils={u.get('abils')} atk1={u.get('atk1_targets')} atk2={u.get('atk2_targets')} hotkey={u.get('hotkey')}")

p("\n=== 4. HEROES ===")
for h in d1["heroes"]:
    hid = h.get("id")
    p(f"Hero: {hid}")
    for fld in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
        sid, val = resolve(h.get(f"raw_{fld}"))
        p(f"  {fld}: sid={sid} raw={h.get(f'raw_{fld}')} val={repr(val)}")
    p(f"  abils={h.get('abils')} atk1={h.get('atk1_targets')} atk2={h.get('atk2_targets')} hotkey={h.get('hotkey')}")

p("\n=== 5. UPGRADES ===")
for uid, upg in d2["upgrades"].items():
    p(f"Upgrade: {uid} max_lvl={upg.get('max_level')}")
    # inspect all fields
    for k, v in upg.items():
        if isinstance(v, dict):
            for subk, subv in v.items():
                if isinstance(subv, dict) and "raw" in subv:
                    sid, val = resolve(subv["raw"])
                    p(f"  {k}.{subk}: sid={sid} raw={subv['raw']} val={repr(val)}")

p("\n=== 6. ABILITIES ===")
for aid, ab in d2["abils"].items():
    p(f"Ability: {aid} lvls={ab.get('levels')}")
    for k, v in ab.items():
        if isinstance(v, dict):
            for subk, subv in v.items():
                if isinstance(subv, dict) and "raw" in subv:
                    sid, val = resolve(subv["raw"])
                    p(f"  {k}.{subk}: sid={sid} raw={subv['raw']} val={repr(val)}")
        elif k in ["raw_name", "name"]:
            sid, val = resolve(ab.get("raw_name"))
            p(f"  name: sid={sid} raw={ab.get('raw_name')} val={repr(val)}")

(ROOT / "scripts/illidari_detailed_strings.txt").write_text("\n".join(output_lines), encoding="utf-8")
print(f"Wrote {len(output_lines)} lines to scripts/illidari_detailed_strings.txt")
