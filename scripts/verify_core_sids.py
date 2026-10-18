# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

wts_text = (ROOT / "map.w3x/war3map.wts").read_text(encoding="utf-8")
inv = json.loads((ROOT / "scripts/scarlet_complete_inventory.json").read_text(encoding="utf-8"))

def has_sid(sid):
    import re
    return bool(re.search(rf"STRING 0*{sid}\s*\{{\s*\r?\n", wts_text))

print("=== CHECK BUILDINGS ===")
for bid, b in inv['buildings'].items():
    for f in ['name', 'tip', 'ubertip']:
        sid = b[f]['sid']
        assert sid and has_sid(sid), f"Missing building {bid} {f} {sid}"

print("=== CHECK HEROES ===")
for hid, h in inv['heroes'].items():
    for f in ['name', 'tip', 'ubertip']:
        sid = h[f]['sid']
        assert sid and has_sid(sid), f"Missing hero {hid} {f} {sid}"

print("=== CHECK UNITS ===")
for uid, u in inv['units'].items():
    for f in ['name', 'tip', 'ubertip']:
        sid = u[f]['sid']
        assert sid and has_sid(sid), f"Missing unit {uid} {f} {sid}"

print("All buildings, heroes, units have valid WTS string IDs!")
