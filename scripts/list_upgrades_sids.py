# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

inv = json.loads((ROOT / "scripts/scarlet_complete_inventory.json").read_text(encoding="utf-8"))

print("=== UPGRADES SIDS ===")
for uid, u in sorted(inv['upgrades'].items()):
    nsid = u['name']['sid']
    print(f"[{uid}] Name={nsid}: {u['name']['val']}")
    for lvl in range(1, 7):
        n = u['names'].get(str(lvl))
        t = u['tips'].get(str(lvl))
        ub = u['ubertips'].get(str(lvl))
        h = u['hotkeys'].get(str(lvl))
        if n or t or ub:
            print(f"   L{lvl}: name={n['sid'] if n else None} tip={t['sid'] if t else None} ubt={ub['sid'] if ub else None}")
