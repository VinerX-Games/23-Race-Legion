# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "scripts/silitids_raw_dump.json", encoding="utf-8"))

print("=== BUILDINGS STATS ===")
for b in data['buildings']:
    print(f"[{b['id']}] {b['name']} | hp={b['hp']} | gold={b['goldcost']} | lum={b['lumbercost']} | fmade={b['fmade']} | train={b['train']} | res={b['researches']} | upg={b['upgrades_to']}")

print("\n=== UNITS STATS ===")
for u in data['units']:
    print(f"[{u['id']}] {u['name']} | hp={u['hp']} | gold={u['goldcost']} | lum={u['lumbercost']} | fused={u['fused']} | atk1={u['atktype1']} ({u['targs1']}) | atk2={u['atktype2']} ({u['targs2']}) | abils={u['abillist']}")

print("\n=== HEROES STATS ===")
for h in data['heroes']:
    print(f"[{h['id']}] {h['name']} ({h['propernames']}) | gold={h['goldcost']} | lum={h['lumbercost']} | atk1={h['atktype1']} ({h['targs1']}) | heroabils={h['heroabillist']}")

print("\n=== UPGRADES STATS ===")
for up in data['upgrades']:
    print(f"[{up['id']}] lvl={up['levels']} | class={up['raw_class']}")
    for lvl in range(1, up['levels'] + 1):
        n = up['names'].get(f'name{lvl}', {})
        t = up['tips'].get(f'tip{lvl}', {})
        ub = up['ubertips'].get(f'ubertip{lvl}', {})
        hk = up['hotkeys'].get(f'hotkey{lvl}', {})
        print(f"  lvl {lvl}: name='{n.get('val')}' (sid:{n.get('sid')}) | tip='{t.get('val')}' (sid:{t.get('sid')}) | hk='{hk.get('val')}'")
        print(f"         ub='{ub.get('val')}' (sid:{ub.get('sid')})")

print("\n=== ABILITIES STATS ===")
for a in data['abilities']:
    print(f"[{a['id']}] {a['name']} (sid:{a['name_sid']}) | lvls={a['levels']} | hk={a['hotkey']} | rtip={a['researchtip']} (sid:{a['researchtip_sid']})")
    for lvl in range(1, a['levels'] + 1):
        t = a['tips'].get(f'tip{lvl}', {})
        ub = a['ubertips'].get(f'ubertip{lvl}', {})
        print(f"  lvl {lvl}: tip='{t.get('val')}' (sid:{t.get('sid')})")
        print(f"         ub='{ub.get('val')}' (sid:{ub.get('sid')})")

print("\n=== BUFFS STATS ===")
for b in data['buffs']:
    print(f"[{b['id']}] tip='{b['bufftip']}' (sid:{b['bufftip_sid']}) | ed='{b['editorname']}' (sid:{b['editorname_sid']}) | ub='{b['buffubertip']}' (sid:{b['buffubertip_sid']})")
