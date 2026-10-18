# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

inv = json.loads((ROOT / "scripts/scarlet_complete_inventory.json").read_text(encoding="utf-8"))

print("=== HERO ABILITIES SIDS ===")
for aid in ['A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J']:
    a = inv['abilities'][aid]
    f = a['fields']
    print(f"[{aid}] {a['name']['sid']}: {a['name']['val']}")
    print(f"   research: tip={f.get('researchtip')} ubt={f.get('researchubertip')}")
    for lvl in range(1, 5):
        t = a['tips'].get(str(lvl))
        u = a['ubertips'].get(str(lvl))
        ut = a['untips'].get(str(lvl))
        uu = a['unubertips'].get(str(lvl))
        if t or u:
            print(f"   L{lvl}: tip={t['sid'] if t else None} ubt={u['sid'] if u else None}")
        if ut or uu:
            print(f"   L{lvl} UN: tip={ut['sid'] if ut else None} ubt={uu['sid'] if uu else None}")

print("\n=== UNIT ABILITIES SIDS ===")
for aid, a in sorted(inv['abilities'].items()):
    if aid in ['A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J']:
        continue
    f = a['fields']
    nsid = a['name']['sid']
    t1 = a['tips'].get('1')
    u1 = a['ubertips'].get('1')
    ut1 = a['untips'].get('1')
    uu1 = a['unubertips'].get('1')
    print(f"[{aid}] name={nsid} tip={t1['sid'] if t1 else None} ubt={u1['sid'] if u1 else None} untip={ut1['sid'] if ut1 else None} unubt={uu1['sid'] if uu1 else None}")
