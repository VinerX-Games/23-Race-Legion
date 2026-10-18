# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path("scripts/gilneas_raw_dump.json").read_text(encoding="utf-8"))

def parse_sid(raw):
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

print("=== SELECTION ===")
a = dump["selection"]
print("A121 name:", parse_sid(a.get("raw_name")), "tip1:", parse_sid(a["tips"].get("tip1", {}).get("raw")), "ub1:", parse_sid(a["ubertips"].get("ubertip1", {}).get("raw")))
for m in dump["selection_markers"]:
    print(m["id"], "name1:", parse_sid(m["names"].get("name1", {}).get("raw")), "tip1:", parse_sid(m["tips"].get("tip1", {}).get("raw")), "ub1:", parse_sid(m["ubertips"].get("ubertip1", {}).get("raw")))

print("\n=== BUILDINGS ===")
for b in dump["buildings"]:
    print(b["id"], "name:", parse_sid(b.get("raw_name")), "tip:", parse_sid(b.get("raw_tip")), "ub:", parse_sid(b.get("raw_ubertip")))

print("\n=== WORKER ===")
w = dump["worker"]
print(w["id"], "name:", parse_sid(w.get("raw_name")), "tip:", parse_sid(w.get("raw_tip")), "ub:", parse_sid(w.get("raw_ubertip")))

print("\n=== UNITS ===")
for u in dump["units"]:
    print(u["id"], "name:", parse_sid(u.get("raw_name")), "tip:", parse_sid(u.get("raw_tip")), "ub:", parse_sid(u.get("raw_ubertip")))

print("\n=== HEROES ===")
for h in dump["heroes"]:
    print(h["id"], "name:", parse_sid(h.get("raw_name")), "proper:", parse_sid(h.get("raw_propernames")), "tip:", parse_sid(h.get("raw_tip")), "ub:", parse_sid(h.get("raw_ubertip")), "awaken:", parse_sid(h.get("raw_awakentip")), "revive:", parse_sid(h.get("raw_revivetip")))

print("\n=== UPGRADES ===")
for u in dump["upgrades"]:
    print(f"Upgrade {u['id']}:")
    for k, v in u["names"].items():
        if parse_sid(v.get("raw")):
            print(f"  {k}: {parse_sid(v.get('raw'))}")
    for k, v in u["tips"].items():
        if parse_sid(v.get("raw")):
            print(f"  {k}: {parse_sid(v.get('raw'))}")
    for k, v in u["ubertips"].items():
        if parse_sid(v.get("raw")):
            print(f"  {k}: {parse_sid(v.get('raw'))}")

print("\n=== ABILITIES ===")
for a in dump["abilities"]:
    sids = []
    if parse_sid(a.get("raw_name")):
        sids.append(f"name: {parse_sid(a.get('raw_name'))}")
    if parse_sid(a.get("raw_researchtip")):
        sids.append(f"rtip: {parse_sid(a.get('raw_researchtip'))}")
    if parse_sid(a.get("raw_researchubertip")):
        sids.append(f"rub: {parse_sid(a.get('raw_researchubertip'))}")
    for k, v in a["tips"].items():
        if parse_sid(v.get("raw")):
            sids.append(f"{k}: {parse_sid(v.get('raw'))}")
    for k, v in a["ubertips"].items():
        if parse_sid(v.get("raw")):
            sids.append(f"{k}: {parse_sid(v.get('raw'))}")
    if sids:
        print(f"Ability {a['id']}: {', '.join(sids)}")

print("\n=== BUFFS ===")
for b in dump["buffs"]:
    print(b["id"], "bufftip:", parse_sid(b.get("raw_bufftip")), "buffubertip:", parse_sid(b.get("raw_buffubertip")))
