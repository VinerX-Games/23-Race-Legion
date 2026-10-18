# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / 'scripts/hordew2_raw_dump.json', encoding='utf-8'))

with open(ROOT / 'scripts/hordew2_details.txt', 'w', encoding='utf-8') as f:
    f.write("=== RACE INFO ===\n")
    f.write(f"Race: {data.get('race')}\n\n")

    f.write("=== SELECTION ABILITY ===\n")
    sel = data.get("selection", {})
    f.write(f"ID: {sel.get('id')}\n")
    f.write(f"Name: {sel.get('name')} (raw: {sel.get('raw_name')})\n")
    f.write(f"Tips: {sel.get('tips')} (raw: {sel.get('raw_tips')})\n")
    f.write(f"Ubertips: {sel.get('ubertips')} (raw: {sel.get('raw_ubertips')})\n\n")

    f.write("=== SELECTION MARKERS ===\n")
    for m in data.get("selection_markers", []):
        f.write(f"[{m.get('id')}]\n")
        f.write(f"  names: {m.get('names')}\n")
        f.write(f"  tips: {m.get('tips')}\n")
        f.write(f"  ubertips: {m.get('ubertips')}\n\n")

    f.write("=== BUILDINGS (11) ===\n")
    for b in data.get("buildings", []):
        f.write(f"[{b.get('id')}] {b.get('name')} (HK: {b.get('hotkey')})\n")
        f.write(f"  raw_name: {b.get('raw_name')} | raw_tip: {b.get('raw_tip')} | raw_ubertip: {b.get('raw_ubertip')}\n")
        f.write(f"  tip: {b.get('tip')}\n")
        f.write(f"  ubertip: {b.get('ubertip')}\n")
        f.write(f"  trains: {b.get('train')} | researches: {b.get('researches')} | upgrades_to: {b.get('upgrades_to')}\n")
        f.write(f"  fmade: {b.get('fmade')} | attacks: {b.get('atktype1')} ({b.get('targs1')})\n\n")

    f.write("=== HEROES (2) ===\n")
    for h in data.get("heroes", []):
        f.write(f"[{h.get('id')}] {h.get('name')} (HK: {h.get('hotkey')})\n")
        f.write(f"  raw_name: {h.get('raw_name')} | raw_tip: {h.get('raw_tip')} | raw_ubertip: {h.get('raw_ubertip')}\n")
        f.write(f"  propernames: {h.get('propernames')} (raw: {h.get('raw_propernames')})\n")
        f.write(f"  awakentip: {h.get('awakentip')} (raw: {h.get('raw_awakentip')})\n")
        f.write(f"  revivetip: {h.get('revivetip')} (raw: {h.get('raw_revivetip')})\n")
        f.write(f"  heroabillist: {h.get('heroabillist')} | abillist: {h.get('abillist')}\n")
        f.write(f"  targs1: {h.get('targs1')} | targs2: {h.get('targs2')}\n")
        f.write(f"  tip: {h.get('tip')}\n")
        f.write(f"  ubertip: {h.get('ubertip')}\n\n")

    f.write("=== UNITS (23) ===\n")
    for u in data.get("units", []):
        f.write(f"[{u.get('id')}] {u.get('name')} (HK: {u.get('hotkey')})\n")
        f.write(f"  raw_name: {u.get('raw_name')} | raw_tip: {u.get('raw_tip')} | raw_ubertip: {u.get('raw_ubertip')}\n")
        f.write(f"  tip: {u.get('tip')}\n")
        f.write(f"  ubertip: {u.get('ubertip')}\n")
        f.write(f"  abillist: {u.get('abillist')}\n")
        f.write(f"  attacks: {u.get('atktype1')} ({u.get('targs1')}) / {u.get('atktype2')} ({u.get('targs2')})\n\n")

    f.write("=== UPGRADES (17) ===\n")
    for up in data.get("upgrades", []):
        f.write(f"[{up.get('id')}] levels: {up.get('levels')}\n")
        f.write(f"  names: {up.get('names')}\n")
        f.write(f"  tips: {up.get('tips')}\n")
        f.write(f"  ubertips: {up.get('ubertips')}\n\n")

    f.write("=== ABILITIES (37) ===\n")
    for a in data.get("abilities", []):
        f.write(f"[{a.get('id')}] {a.get('name')} (levels: {a.get('levels')})\n")
        f.write(f"  raw_name: {a.get('raw_name')}\n")
        f.write(f"  tips: {a.get('tips')}\n")
        f.write(f"  ubertips: {a.get('ubertips')}\n")
        f.write(f"  researchtip: {a.get('researchtip')} | researchubertip: {a.get('researchubertip')}\n\n")

print("Done writing scripts/hordew2_details.txt")
