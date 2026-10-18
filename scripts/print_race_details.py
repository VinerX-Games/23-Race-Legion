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
print(f"  tips={s['tips']}")
print(f"  ubertips={s['ubertips']}")

print("\n=== 2. SELECTION MARKERS ===")
for m in data['selection_markers']:
    print(f"[{m['id']}] names={m['names']} | tips={m['tips']} | ubertips={m['ubertips']}")

print("\n=== 3. BUILDINGS ===")
for b in data['buildings']:
    print(f"[{b['id']}] name={b['name']} ({b['raw_name']}) | tip={b['tip']} ({b['raw_tip']}) | hk={b['hotkey']} ({b['raw_hotkey']})")
    print(f"     ub={b['ubertip'][:120] if b['ubertip'] else 'None'} ({b['raw_ubertip']})")

print("\n=== 4. HEROES ===")
for h in data['heroes']:
    print(f"[{h['id']}] name={h['name']} ({h['raw_name']}) | propernames={h['propernames']} ({h['raw_propernames']})")
    print(f"     tip={h['tip']} ({h['raw_tip']}) | hk={h['hotkey']} ({h['raw_hotkey']})")
    print(f"     awakentip={h['awakentip']} ({h['raw_awakentip']}) | revivetip={h['revivetip']} ({h['raw_revivetip']})")
    print(f"     ub={h['ubertip'][:120] if h['ubertip'] else 'None'} ({h['raw_ubertip']})")
    print(f"     atk1={h['atktype1']}, targets1={h['targs1']}, weap1={h['weaptype1']}, cool1={h['cool1']}")
    print(f"     atk2={h['atktype2']}, targets2={h['targs2']}, weap2={h['weaptype2']}, cool2={h['cool2']}")

print("\n=== 5. UNITS ===")
for u in data['units']:
    print(f"[{u['id']}] name={u['name']} ({u['raw_name']}) | tip={u['tip']} ({u['raw_tip']}) | hk={u['hotkey']} ({u['raw_hotkey']})")
    print(f"     ub={u['ubertip'][:120] if u['ubertip'] else 'None'} ({u['raw_ubertip']})")
    print(f"     atk1={u['atktype1']}, targets1={u['targs1']}, weap1={u['weaptype1']}, cool1={u['cool1']}")
    print(f"     atk2={u['atktype2']}, targets2={u['targs2']}, weap2={u['weaptype2']}, cool2={u['cool2']}")
