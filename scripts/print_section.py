# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

inv = json.loads((ROOT / 'scripts/scarlet_complete_inventory.json').read_text(encoding='utf-8'))

print("=== 1. SELECTION ===")
sel = inv['selection']
print(f"ID: {sel['id']}")
print(f"Name: {sel['name']['val']} (sid={sel['name']['sid']})")
print(f"Tip1: {sel['tip1']['val']} (sid={sel['tip1']['sid']})")
print(f"Ubertip1: {sel['ubertip1']['val']} (sid={sel['ubertip1']['sid']})")
print(f"Hotkey: {sel['hotkey']['val']} (sid={sel['hotkey']['sid']})")

print("\n=== 2. BUILDINGS ===")
for bid, b in inv['buildings'].items():
    print(f"[{bid}] Name: {b['name']['val']} (sid={b['name']['sid']})")
    print(f"      Tip: {b['tip']['val']} (sid={b['tip']['sid']})")
    print(f"      Ubertip: {b['ubertip']['val']} (sid={b['ubertip']['sid']})")
    print(f"      Hotkey: {b['hotkey']['val']} (sid={b['hotkey']['sid']})")
    print(f"      Trains: {b['trains']}, Researches: {b['researches']}, Upgrade: {b['upgrade']}, Upgrades: {b['upgrades']}")
    print()

print("\n=== 3. HEROES ===")
for hid, h in inv['heroes'].items():
    print(f"[{hid}] Name: {h['name']['val']} (sid={h['name']['sid']})")
    print(f"      Propernames: {h['propernames']['val']} (sid={h['propernames']['sid']})")
    print(f"      Tip: {h['tip']['val']} (sid={h['tip']['sid']})")
    print(f"      Ubertip: {h['ubertip']['val']} (sid={h['ubertip']['sid']})")
    print(f"      Hotkey: {h['hotkey']['val']} (sid={h['hotkey']['sid']})")
    print(f"      HeroAbils: {h['heroabils']}, Targs: {h['targs1']}, WeapType: {h['weaptype1']}")
    print()
