# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / 'scripts/kultiras_raw_dump.json', encoding='utf-8'))

print("=== 1. BUILDINGS ===")
for b in d['buildings']:
    print(f"ID: {b['id']} | Name: {b['name']} ({b['raw_name']}) | Hotkey: {b['hotkey']} ({b['raw_hotkey']})")
    print(f"  Tip: {b['tip']} ({b['raw_tip']})")
    print(f"  Ubertip: {b['ubertip']} ({b['raw_ubertip']})")
    print(f"  Trains: {b.get('trains')}")
    print(f"  Researches: {b.get('researches')}")
    print(f"  Upgrades to: {b.get('upgrades_to')}")
    print(f"  Abils: {b.get('abils')}")
    print()

print("=== 2. HEROES ===")
for h in d['heroes']:
    print(f"ID: {h['id']} | Name: {h['name']} ({h['raw_name']}) | Hotkey: {h['hotkey']} ({h['raw_hotkey']})")
    print(f"  Tip: {h['tip']} ({h['raw_tip']})")
    print(f"  Ubertip: {h['ubertip']} ({h['raw_ubertip']})")
    print(f"  Hero Abils: {h.get('heroabils')}")
    print(f"  Targs1: {h.get('targs1')} | Weaptype1: {h.get('weaptype1')}")
    print(f"  Targs2: {h.get('targs2')} | Weaptype2: {h.get('weaptype2')}")
    print()

print("=== 3. UNITS ===")
for u in d['units']:
    print(f"ID: {u['id']} | Name: {u['name']} ({u['raw_name']}) | Hotkey: {u['hotkey']} ({u['raw_hotkey']})")
    print(f"  Tip: {u['tip']} ({u['raw_tip']})")
    print(f"  Ubertip: {u['ubertip']} ({u['raw_ubertip']})")
    print(f"  Abils: {u.get('abils')}")
    print(f"  Upgrades: {u.get('upgrades')}")
    print(f"  Targs1: {u.get('targs1')} | Weaptype1: {u.get('weaptype1')}")
    print(f"  Targs2: {u.get('targs2')} | Weaptype2: {u.get('weaptype2')}")
    print()
