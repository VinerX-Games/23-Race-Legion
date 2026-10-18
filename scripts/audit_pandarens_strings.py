# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

def parse_sid(raw):
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        try:
            return int(raw[8:])
        except ValueError:
            pass
    return None

report = []

# 1. Selection & Marker
report.append("=== 1. SELECTION & MARKER ===")
s = dump["selection"]
for f in ["name", "researchtip", "researchubertip"]:
    sid = parse_sid(s.get(f"raw_{f}"))
    report.append(f"A1I6 {f}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")
for lvl, tip_data in s.get("tips", {}).items():
    sid = parse_sid(tip_data.get("raw"))
    report.append(f"A1I6 tip_{lvl}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")
for lvl, ub_data in s.get("ubertips", {}).items():
    sid = parse_sid(ub_data.get("raw"))
    report.append(f"A1I6 ubertip_{lvl}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

for m in dump["selection_markers"]:
    mid = m["id"]
    for l in range(1, (m.get("levels") or 1) + 1):
        for f in ["name", "tip", "ubertip"]:
            k = f"{f}{l}"
            field_dict = m.get(f"{f}s", {}).get(k, {})
            sid = parse_sid(field_dict.get("raw"))
            report.append(f"{mid} {k}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

# 2. Buildings
report.append("\n=== 2. BUILDINGS ===")
for b in dump["buildings"]:
    bid = b["id"]
    for f in ["name", "tip", "ubertip"]:
        sid = parse_sid(b.get(f"raw_{f}"))
        report.append(f"Building {bid} {f}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

# 3. Units
report.append("\n=== 3. UNITS ===")
for u in dump["units"]:
    uid = u["id"]
    for f in ["name", "tip", "ubertip"]:
        sid = parse_sid(u.get(f"raw_{f}"))
        report.append(f"Unit {uid} {f}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

# 4. Heroes
report.append("\n=== 4. HEROES ===")
for h in dump["heroes"]:
    hid = h["id"]
    for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
        sid = parse_sid(h.get(f"raw_{f}"))
        report.append(f"Hero {hid} {f}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

# 5. Upgrades
report.append("\n=== 5. UPGRADES ===")
for up in dump["upgrades"]:
    uid = up["id"]
    lvls = up.get("levels") or 1
    for l in range(1, lvls + 1):
        for f in ["name", "tip", "ubertip"]:
            k = f"{f}{l}"
            field_dict = up.get(f"{f}s", {}).get(k, {})
            sid = parse_sid(field_dict.get("raw"))
            report.append(f"Upgrade {uid} {k}: sid={sid} | text={wts.get(sid, '') if sid else 'None'}")

# 6. Abilities
report.append("\n=== 6. ABILITIES ===")
for ab in dump["abilities"]:
    aid = ab["id"]
    sid_name = parse_sid(ab.get("raw_name"))
    report.append(f"Ability {aid} name: sid={sid_name} | text={wts.get(sid_name, '') if sid_name else 'None'}")
    sid_rt = parse_sid(ab.get("raw_researchtip"))
    if sid_rt:
        report.append(f"Ability {aid} researchtip: sid={sid_rt} | text={wts.get(sid_rt, '')}")
    sid_ru = parse_sid(ab.get("raw_researchubertip"))
    if sid_ru:
        report.append(f"Ability {aid} researchubertip: sid={sid_ru} | text={wts.get(sid_ru, '')}")
    lvls = ab.get("levels") or 1
    for l in range(1, lvls + 1):
        t_sid = parse_sid(ab.get("tips", {}).get(f"tip{l}", {}).get("raw"))
        u_sid = parse_sid(ab.get("ubertips", {}).get(f"ubertip{l}", {}).get("raw"))
        report.append(f"Ability {aid} tip{l}: sid={t_sid} | text={wts.get(t_sid, '') if t_sid else 'None'}")
        report.append(f"Ability {aid} ubertip{l}: sid={u_sid} | text={wts.get(u_sid, '') if u_sid else 'None'}")

(ROOT / "scripts/pandarens_all_sids.txt").write_text("\n".join(report), encoding="utf-8")
print("Wrote scripts/pandarens_all_sids.txt")
