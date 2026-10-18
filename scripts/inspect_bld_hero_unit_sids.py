# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

def parse_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:])
    return None

print("=== BUILDINGS ===")
for b in dump['buildings']:
    print(f"{b['id']}: name_sid={parse_sid(b.get('raw_name'))} ('{b.get('name')}')")
    print(f"      tip_sid={parse_sid(b.get('raw_tip'))} ('{b.get('tip')}')")
    print(f"      ub_sid={parse_sid(b.get('raw_ubertip'))} ('{b.get('ubertip')}')")
    print(f"      hk={b.get('hotkey')}")

print("\n=== HEROES ===")
for h in dump['heroes']:
    print(f"{h['id']}: name_sid={parse_sid(h.get('raw_name'))} ('{h.get('name')}') proper={h.get('propernames')}")
    print(f"      tip_sid={parse_sid(h.get('raw_tip'))} ('{h.get('tip')}')")
    print(f"      ub_sid={parse_sid(h.get('raw_ubertip'))} ('{h.get('ubertip')}')")
    print(f"      awaken_sid={parse_sid(h.get('raw_awakentip'))} revive_sid={parse_sid(h.get('raw_revivetip'))}")
    print(f"      proper_sid={parse_sid(h.get('raw_propernames'))} hk={h.get('hotkey')}")

print("\n=== UNITS ===")
for u in dump['units']:
    print(f"{u['id']}: name_sid={parse_sid(u.get('raw_name'))} ('{u.get('name')}')")
    print(f"      tip_sid={parse_sid(u.get('raw_tip'))} ('{u.get('tip')}')")
    print(f"      ub_sid={parse_sid(u.get('raw_ubertip'))} ('{u.get('ubertip')}')")
    print(f"      hk={u.get('hotkey')}")
