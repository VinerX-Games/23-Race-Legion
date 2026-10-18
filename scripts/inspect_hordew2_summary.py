# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / 'scripts/hordew2_raw_dump.json', encoding='utf-8'))

print("=== RACE INFO ===")
print("Race:", data.get("race"))

print("\n=== SELECTION ABILITY ===")
sel = data.get("selection", {})
print("Selection ability ID:", sel.get("id"))
print("Name:", sel.get("name"), "raw:", sel.get("raw_name"))
print("Tip:", sel.get("tips"), "raw:", sel.get("raw_tips"))
print("Ubertip:", sel.get("ubertips"), "raw:", sel.get("raw_ubertips"))

print("\n=== SELECTION MARKERS ===")
for m in data.get("selection_markers", []):
    print(m.get("id"), "names:", m.get("names"), "raw_names:", m.get("raw_names"))
    print("  tips:", m.get("tips"), "raw_tips:", m.get("raw_tips"))
    print("  ubertips:", m.get("ubertips"), "raw_ubertips:", m.get("raw_ubertips"))

print("\n=== BUILDINGS (11) ===")
for b in data.get("buildings", []):
    print(f"[{b.get('id')}] {b.get('name')} (HK: {b.get('hotkey')})")
    print(f"  raw_name: {b.get('raw_name')} | raw_tip: {b.get('raw_tip')} | raw_ubertip: {b.get('raw_ubertip')}")
    print(f"  tip: {b.get('tip')}")
    print(f"  ubertip: {b.get('ubertip')}")
    print(f"  trains: {b.get('train')} | researches: {b.get('researches')} | upgrades_to: {b.get('upgrades_to')}")
    print(f"  fmade: {b.get('fmade')} | attacks: {b.get('atktype1')} ({b.get('targs1')})")

print("\n=== HEROES (2) ===")
for h in data.get("heroes", []):
    print(f"[{h.get('id')}] {h.get('name')} (HK: {h.get('hotkey')})")
    print(f"  propernames: {h.get('propernames')} (raw: {h.get('raw_propernames')})")
    print(f"  heroabillist: {h.get('heroabillist')} | abillist: {h.get('abillist')}")
    print(f"  targs1: {h.get('targs1')} | targs2: {h.get('targs2')}")
    print(f"  tip: {h.get('tip')}")
    print(f"  ubertip: {h.get('ubertip')}")
    print(f"  awakentip: {h.get('awakentip')} | revivetip: {h.get('revivetip')}")

print("\n=== UNITS (23) ===")
for u in data.get("units", []):
    print(f"[{u.get('id')}] {u.get('name')} (HK: {u.get('hotkey')})")
    print(f"  raw_name: {u.get('raw_name')} | raw_tip: {u.get('raw_tip')} | raw_ubertip: {u.get('raw_ubertip')}")
    print(f"  tip: {u.get('tip')}")
    print(f"  ubertip: {u.get('ubertip')}")
    print(f"  abillist: {u.get('abillist')}")
    print(f"  attacks: {u.get('atktype1')} ({u.get('targs1')}) / {u.get('atktype2')} ({u.get('targs2')})")

print("\n=== UPGRADES (17) ===")
for up in data.get("upgrades", []):
    print(f"[{up.get('id')}] levels: {up.get('levels')}")
    print(f"  names: {up.get('names')}")
    print(f"  tips: {up.get('tips')}")
    print(f"  ubertips: {up.get('ubertips')}")

print("\n=== ABILITIES (37) ===")
for a in data.get("abilities", []):
    print(f"[{a.get('id')}] {a.get('name')} (levels: {a.get('levels')})")
    print(f"  raw_name: {a.get('raw_name')}")
    print(f"  tips: {a.get('tips')}")
    print(f"  ubertips: {a.get('ubertips')}")
    print(f"  researchtip: {a.get('researchtip')} | researchubertip: {a.get('researchubertip')}")
