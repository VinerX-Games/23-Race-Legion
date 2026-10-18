# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

inv = json.loads((ROOT / 'scripts/scarlet_complete_inventory.json').read_text(encoding='utf-8'))

print("=== 5. ABILITIES ===")
for aid, a in inv['abilities'].items():
    print(f"[{aid}] Name: {a['name']['val']} (sid={a['name']['sid']}), Levels: {a['levels']}")
    for lvl in range(1, 5):
        t = a['tips'].get(str(lvl))
        u = a['ubertips'].get(str(lvl))
        h = a['hotkeys'].get(str(lvl))
        ut = a['untips'].get(str(lvl))
        uu = a['unubertips'].get(str(lvl))
        if t or u or h:
            print(f"   L{lvl}: Tip={t['val'] if t else None} (sid={t['sid'] if t else None}) | Hotkey={h['val'] if h else None} (sid={h['sid'] if h else None})")
            print(f"       Ubt={u['val'] if u else None} (sid={u['sid'] if u else None})")
        if ut or uu:
            print(f"   L{lvl} UN: Tip={ut['val'] if ut else None} (sid={ut['sid'] if ut else None}) | Ubt={uu['val'] if uu else None} (sid={uu['sid'] if uu else None})")
    print()

print("\n=== 6. UPGRADES ===")
for uid, u in inv['upgrades'].items():
    print(f"[{uid}] Name: {u['name']['val']} (sid={u['name']['sid']}), Levels: {u['levels']}")
    for lvl in range(1, 7):
        n = u['names'].get(str(lvl))
        t = u['tips'].get(str(lvl))
        ub = u['ubertips'].get(str(lvl))
        h = u['hotkeys'].get(str(lvl))
        if n or t or ub:
            print(f"   L{lvl}: Name={n['val'] if n else None} (sid={n['sid'] if n else None}) | Tip={t['val'] if t else None} (sid={t['sid'] if t else None}) | Hotkey={h['val'] if h else None} (sid={h['sid'] if h else None})")
            print(f"       Ubt={ub['val'] if ub else None} (sid={ub['sid'] if ub else None})")
    print()
