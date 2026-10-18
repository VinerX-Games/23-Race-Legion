# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

def get_str(raw):
    if raw is None:
        return "None"
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        try:
            sid = int(raw[8:])
            return f"[{sid}] {wts.get(sid, '<MISSING>')}"
        except ValueError:
            pass
    return str(raw)

out = []
out.append("=== SELECTION ===")
s = dump['selection']
out.append(f"ID: {s.get('id')}")
out.append(f"Name: {get_str(s.get('raw_name'))}")
out.append(f"Hotkey: {s.get('hotkey')}")
out.append(f"Researchtip: {get_str(s.get('raw_researchtip'))}")
out.append(f"Researchubertip: {get_str(s.get('raw_researchubertip'))}")
for k, tip_data in s.get('tips', {}).items():
    out.append(f"Tip {k}: {get_str(tip_data.get('raw'))}")
for k, ub_data in s.get('ubertips', {}).items():
    out.append(f"Ubertip {k}: {get_str(ub_data.get('raw'))}")

out.append("\n=== SELECTION MARKERS ===")
for m in dump['selection_markers']:
    out.append(f"ID: {m.get('id')}")
    out.append(f"Name: {get_str(m.get('names', {}).get('name1', {}).get('raw'))}")
    out.append(f"Tip: {get_str(m.get('tips', {}).get('tip1', {}).get('raw'))}")
    out.append(f"Ubertip: {get_str(m.get('ubertips', {}).get('ubertip1', {}).get('raw'))}")

out.append("\n=== BUILDINGS ===")
for b in dump['buildings']:
    out.append(f"\nBuilding ID: {b.get('id')}")
    out.append(f"Name: {get_str(b.get('raw_name'))}")
    out.append(f"Hotkey: {b.get('hotkey')}")
    out.append(f"Tip: {get_str(b.get('raw_tip'))}")
    out.append(f"Ubertip: {get_str(b.get('raw_ubertip'))}")
    out.append(f"Trains: {b.get('train')}")
    out.append(f"Researches: {b.get('researches')}")
    out.append(f"UpgradesTo: {b.get('upgrades_to')}")
    out.append(f"Attacks: {b.get('attacks')}")

out.append("\n=== HEROES ===")
for h in dump['heroes']:
    out.append(f"\nHero ID: {h.get('id')}")
    out.append(f"Name: {get_str(h.get('raw_name'))}")
    out.append(f"Propernames: {get_str(h.get('raw_propernames'))}")
    out.append(f"Hotkey: {h.get('hotkey')}")
    out.append(f"Tip: {get_str(h.get('raw_tip'))}")
    out.append(f"Ubertip: {get_str(h.get('raw_ubertip'))}")
    out.append(f"Awakentip: {get_str(h.get('raw_awakentip'))}")
    out.append(f"Revivetip: {get_str(h.get('raw_revivetip'))}")
    out.append(f"Abilities: {h.get('heroabillist')} | Normal: {h.get('abillist')}")
    out.append(f"Attacks: {h.get('attacks')}")

out.append("\n=== UNITS ===")
for u in dump['units']:
    out.append(f"\nUnit ID: {u.get('id')}")
    out.append(f"Name: {get_str(u.get('raw_name'))}")
    out.append(f"Hotkey: {u.get('hotkey')}")
    out.append(f"Tip: {get_str(u.get('raw_tip'))}")
    out.append(f"Ubertip: {get_str(u.get('raw_ubertip'))}")
    out.append(f"Abilities: {u.get('abillist')}")
    out.append(f"Attacks: {u.get('attacks')}")

out.append("\n=== UPGRADES ===")
for up in dump['upgrades']:
    out.append(f"\nUpgrade ID: {up.get('id')}, Levels: {up.get('levels')}")
    for lvl in range(1, (up.get('levels') or 1) + 1):
        name_k = f"name{lvl}"
        tip_k = f"tip{lvl}"
        ub_k = f"ubertip{lvl}"
        out.append(f"  L{lvl} Name: {get_str(up.get('names', {}).get(name_k, {}).get('raw'))}")
        out.append(f"  L{lvl} Tip: {get_str(up.get('tips', {}).get(tip_k, {}).get('raw'))}")
        out.append(f"  L{lvl} Ubertip: {get_str(up.get('ubertips', {}).get(ub_k, {}).get('raw'))}")

out.append("\n=== ABILITIES ===")
for ab in dump['abilities']:
    out.append(f"\nAbility ID: {ab.get('id')}, Levels: {ab.get('levels')}")
    out.append(f"Name: {get_str(ab.get('raw_name'))}")
    out.append(f"Researchtip: {get_str(ab.get('raw_researchtip'))}")
    out.append(f"Researchubertip: {get_str(ab.get('raw_researchubertip'))}")
    for lvl in range(1, (ab.get('levels') or 1) + 1):
        tip_k = f"tip{lvl}"
        ub_k = f"ubertip{lvl}"
        out.append(f"  L{lvl} Tip: {get_str(ab.get('tips', {}).get(tip_k, {}).get('raw'))}")
        out.append(f"  L{lvl} Ubertip: {get_str(ab.get('ubertips', {}).get(ub_k, {}).get('raw'))}")

(ROOT / "scripts/pandarens_inspected_text.txt").write_text("\n".join(out), encoding="utf-8")
print("Done writing scripts/pandarens_inspected_text.txt")
