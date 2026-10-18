# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def resolve_str(s):
    if not isinstance(s, str):
        return s
    if s.startswith("TRIGSTR_"):
        try:
            return wts.get(int(s[8:]), s)
        except Exception:
            return s
    return s

d1 = json.load(open(ROOT / "scripts/illidari_raw_dump.json", encoding="utf-8"))
d2 = json.load(open(ROOT / "scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

print("=== HEROES DETAILS ===")
for h in d1["heroes"]:
    print(f"[{h['id']}] {resolve_str(h['name'])} (hotkey: {h.get('hotkey')})")
    print(f"  Propernames: {resolve_str(h.get('propernames'))}")
    print(f"  heroabils: {h.get('heroabils')}  abils: {h.get('abils')}")
    print(f"  targs1: {h.get('targs1')}  targs2: {h.get('targs2')}")
    print(f"  hp: {h.get('hp')} mana: {h.get('mana')} def: {h.get('def')} ({h.get('deftype')})")
    print(f"  raw_name: {h.get('raw_name')} raw_tip: {h.get('raw_tip')} raw_ubertip: {h.get('raw_ubertip')}")

print("\n=== UNITS DETAILS ===")
for u in d1["units"]:
    print(f"[{u['id']}] {resolve_str(u['name'])} (hotkey: {u.get('hotkey')})")
    print(f"  abils: {u.get('abils')}  upgrades: {u.get('upgrades')}")
    print(f"  targs1: {u.get('targs1')}  targs2: {u.get('targs2')}")
    print(f"  hp: {u.get('hp')} mana: {u.get('mana')} def: {u.get('def')} ({u.get('deftype')})")
    print(f"  raw_name: {u.get('raw_name')} raw_tip: {u.get('raw_tip')} raw_ubertip: {u.get('raw_ubertip')}")

print("\n=== BUILDINGS DETAILS ===")
for b in d1["buildings"]:
    print(f"[{b['id']}] {resolve_str(b['name'])} (hotkey: {b.get('hotkey')})")
    print(f"  trains: {b.get('trains')}  researches: {b.get('researches')}  upgrades_to: {b.get('upgrades_to')}")
    print(f"  raw_name: {b.get('raw_name')} raw_tip: {b.get('raw_tip')} raw_ubertip: {b.get('raw_ubertip')}")

