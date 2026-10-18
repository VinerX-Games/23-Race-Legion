# -*- coding: utf-8 -*-
"""Analyze all WTS strings in HordeW2 objects."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def parse_str_id(raw):
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

def main():
    dump = json.loads((ROOT / "scripts/hordew2_raw_dump.json").read_text(encoding="utf-8"))

    print("=== SELECTION ===")
    sel = dump.get("selection", {})
    for f in ["raw_name", "raw_tips", "raw_ubertips"]:
        val = sel.get(f)
        if isinstance(val, dict):
            for k, v in val.items():
                sid = parse_str_id(v.get("raw"))
                print(f"Selection {f}[{k}]: sid={sid} -> {repr(wts.get(sid))}")
        else:
            sid = parse_str_id(val)
            print(f"Selection {f}: sid={sid} -> {repr(wts.get(sid))}")

    print("\n=== MARKERS ===")
    for m in dump.get("selection_markers", []):
        mid = m.get("id")
        for f in ["names", "tips", "ubertips"]:
            val = m.get(f, {})
            for k, v in val.items():
                sid = parse_str_id(v.get("raw"))
                if sid:
                    print(f"Marker {mid} {f}[{k}]: sid={sid} -> {repr(wts.get(sid))}")

    print("\n=== BUILDINGS (13) ===")
    for b in dump.get("buildings", []):
        bid = b.get("id")
        name_sid = parse_str_id(b.get("raw_name"))
        tip_sid = parse_str_id(b.get("raw_tip"))
        ub_sid = parse_str_id(b.get("raw_ubertip"))
        print(f"[{bid}] name_sid={name_sid} ({repr(wts.get(name_sid))}), tip_sid={tip_sid} ({repr(wts.get(tip_sid))}), ub_sid={ub_sid} ({repr(wts.get(ub_sid))[:60] if ub_sid else None})")

    print("\n=== HEROES (4) ===")
    for h in dump.get("heroes", []):
        hid = h.get("id")
        name_sid = parse_str_id(h.get("raw_name"))
        tip_sid = parse_str_id(h.get("raw_tip"))
        ub_sid = parse_str_id(h.get("raw_ubertip"))
        prop_sid = parse_str_id(h.get("raw_propernames"))
        awk_sid = parse_str_id(h.get("raw_awakentip"))
        rev_sid = parse_str_id(h.get("raw_revivetip"))
        print(f"[{hid}] name_sid={name_sid}, tip_sid={tip_sid}, ub_sid={ub_sid}, prop_sid={prop_sid}, awk_sid={awk_sid}, rev_sid={rev_sid}")
        print(f"   name: {repr(wts.get(name_sid))}")
        print(f"   tip: {repr(wts.get(tip_sid))}")
        print(f"   ubertip: {repr(wts.get(ub_sid))}")
        print(f"   propernames: {repr(wts.get(prop_sid))}")
        print(f"   awakentip: {repr(wts.get(awk_sid))}")
        print(f"   revivetip: {repr(wts.get(rev_sid))}")

    print("\n=== UNITS (21) ===")
    for u in dump.get("units", []):
        uid = u.get("id")
        name_sid = parse_str_id(u.get("raw_name"))
        tip_sid = parse_str_id(u.get("raw_tip"))
        ub_sid = parse_str_id(u.get("raw_ubertip"))
        print(f"[{uid}] name_sid={name_sid} ({repr(wts.get(name_sid))}), tip_sid={tip_sid} ({repr(wts.get(tip_sid))}), ub_sid={ub_sid} ({repr(wts.get(ub_sid))[:50] if ub_sid else None})")

    print("\n=== UPGRADES (40) ===")
    upg_sids_count = 0
    for up in dump.get("upgrades", []):
        upid = up.get("id")
        sids = []
        for f in ["names", "tips", "ubertips"]:
            val = up.get(f, {})
            for k, v in val.items():
                sid = parse_str_id(v.get("raw"))
                if sid:
                    sids.append((f, k, sid, repr(wts.get(sid))[:40]))
        if sids:
            upg_sids_count += len(sids)
            print(f"[{upid}] levels={up.get('levels')} (sids: {len(sids)})")
            for s in sids:
                print(f"   {s[0]}[{s[1]}]: sid={s[2]} -> {s[3]}")
        else:
            print(f"[{upid}] levels={up.get('levels')} NO SIDS")

    print("\n=== ABILITIES (86) ===")
    ab_sids_count = 0
    for a in dump.get("abilities", []):
        aid = a.get("id")
        sids = []
        name_sid = parse_str_id(a.get("raw_name"))
        if name_sid:
            sids.append(("name", name_sid, repr(wts.get(name_sid))[:40]))
        res_tip_sid = parse_str_id(a.get("raw_researchtip"))
        if res_tip_sid:
            sids.append(("researchtip", res_tip_sid, repr(wts.get(res_tip_sid))[:40]))
        res_ub_sid = parse_str_id(a.get("raw_researchubertip"))
        if res_ub_sid:
            sids.append(("researchubertip", res_ub_sid, repr(wts.get(res_ub_sid))[:40]))
        for f in ["tips", "ubertips"]:
            val = a.get(f, {})
            for k, v in val.items():
                sid = parse_str_id(v.get("raw"))
                if sid:
                    sids.append((f"{f}_{k}", sid, repr(wts.get(sid))[:40]))
        if sids:
            ab_sids_count += len(sids)
            print(f"[{aid}] {a.get('name')} (levels: {a.get('levels')}) sids: {len(sids)}")
            for s in sids:
                print(f"   {s[0]}: sid={s[1]} -> {s[2]}")
        else:
            print(f"[{aid}] {a.get('name')} NO SIDS")

if __name__ == '__main__':
    main()
