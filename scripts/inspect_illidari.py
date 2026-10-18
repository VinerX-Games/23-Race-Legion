# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

d1 = json.load(open(ROOT / "scripts/illidari_raw_dump.json", encoding="utf-8"))
d2 = json.load(open(ROOT / "scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

print("=== SELECTION ===")
sel = d1["selection"]
print("ID:", sel.get("id"))
print("Name:", sel.get("name"), "raw:", sel.get("raw_name"))
print("Tips:", sel.get("tips"))
print("Ubertips:", sel.get("ubertips"))
print("Hotkey:", sel.get("hotkey"), "raw_hotkey:", sel.get("raw_hotkey"))
print("Fields:", sel.get("fields"))

print("\n=== BUILDINGS ===")
for b in d1["buildings"]:
    print(f"[{b.get('id')}] name='{b.get('name')}' raw_name='{b.get('raw_name')}' tip='{b.get('tip')}' raw_tip='{b.get('raw_tip')}' hotkey='{b.get('hotkey')}'")
    print(f"   ubertip: {b.get('ubertip')[:60]}... raw_ubertip: {b.get('raw_ubertip')}")
    print(f"   trains: {b.get('trains')} researches: {b.get('researches')} upgrades_to: {b.get('upgrades_to')}")

print("\n=== UNITS ===")
for u in d1["units"]:
    print(f"[{u.get('id')}] name='{u.get('name')}' raw_name='{u.get('raw_name')}' tip='{u.get('tip')}' raw_tip='{u.get('raw_tip')}' hotkey='{u.get('hotkey')}'")
    print(f"   ubertip: {u.get('ubertip')[:60]}... raw_ubertip: {u.get('raw_ubertip')}")
    print(f"   abils: {u.get('abils')} atk1: {u.get('atk1_targets')} atk2: {u.get('atk2_targets')}")

print("\n=== HEROES ===")
for h in d1["heroes"]:
    print(f"[{h.get('id')}] name='{h.get('name')}' raw_name='{h.get('raw_name')}' propernames='{h.get('propernames')}' tip='{h.get('tip')}' hotkey='{h.get('hotkey')}'")
    print(f"   ubertip: {h.get('ubertip')[:60]}... raw_ubertip: {h.get('raw_ubertip')}")
    print(f"   abils: {h.get('abils')}")

print("\n=== UPGRADES ===")
for uid, upg in d2["upgrades"].items():
    print(f"[{uid}] max_level={upg.get('max_level')} names={upg.get('names')}")
    print(f"   raw_names={upg.get('raw_names')}")
    print(f"   tips={upg.get('tips')}")
    print(f"   raw_tips={upg.get('raw_tips')}")
    print(f"   raw_ubertips={upg.get('raw_ubertips')}")

print(f"\nTotal abils in dump2: {len(d2['abils'])}")
for aid, ab in d2["abils"].items():
    print(f"[{aid}] name='{ab.get('name')}' levels={ab.get('levels')} raw_name='{ab.get('raw_name')}'")
    print(f"   raw_tips={ab.get('raw_tips')}")
    print(f"   raw_ubertips={ab.get('raw_ubertips')}")
