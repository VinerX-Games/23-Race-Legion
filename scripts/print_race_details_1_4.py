# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "scripts/silitids_raw_dump.json", encoding="utf-8"))

print("=== 1. SELECTION ===")
s = data['selection']
print(f"[{s['id']}] name={s['name']} (sid: {s['name_sid']})")
print(f"  hotkey={s['hotkey']} (raw_hk={s['raw_hotkey']})")
print(f"  tip={s['tips']['tip1']['val']} (sid: {s['tips']['tip1']['sid']})")
print(f"  ub={s['ubertips']['ubertip1']['val']} (sid: {s['ubertips']['ubertip1']['sid']})")

print("\n=== 2. SELECTION MARKERS ===")
for m in data['selection_markers']:
    print(f"[{m['id']}]")
    for lvl, d in m['names'].items():
        print(f"  name_{lvl}={d['val']} (sid: {d['sid']})")
    for lvl, d in m['tips'].items():
        print(f"  tip_{lvl}={d['val']} (sid: {d['sid']})")
    for lvl, d in m['ubertips'].items():
        print(f"  ub_{lvl}={d['val']} (sid: {d['sid']})")

print("\n=== 3. BUILDINGS ===")
for b in data['buildings']:
    print(f"[{b['id']}] name={b['name']} (raw: {b['raw_name']}) | tip={b['tip']} (raw: {b['raw_tip']}) | hk={b['hotkey']} (raw: {b['raw_hotkey']})")
    print(f"     ub={b['ubertip']} (raw: {b['raw_ubertip']})")

print("\n=== 4. HEROES ===")
for h in data['heroes']:
    print(f"[{h['id']}] name={h['name']} (raw: {h['raw_name']}) | propernames={h['propernames']} (raw: {h['raw_propernames']})")
    print(f"     tip={h['tip']} (raw: {h['raw_tip']}) | hk={h['hotkey']} (raw: {h['raw_hotkey']})")
    print(f"     awakentip={h['awakentip']} (raw: {h['raw_awakentip']}) | revivetip={h['revivetip']} (raw: {h['raw_revivetip']})")
    print(f"     ub={h['ubertip']} (raw: {h['raw_ubertip']})")
