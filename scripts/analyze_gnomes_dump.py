# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

print("=== 1. SELECTION & MARKERS ===")
print("Selection ability:", d['selection']['id'], d['selection']['name'], "tip:", d['selection']['tips'])
for m in d['selection_markers']:
    print("Marker:", m['id'], m['names'], m['tips'])

print("\n=== 2. BUILDINGS (10) ===")
for b in d['buildings']:
    print(f"{b['id']}: name={b['name']!r}, tip={b['tip']!r}, hotkey={b['hotkey']!r}, trains={b.get('train')!r}, res={b.get('researches')!r}, upg={b.get('upgrades_to')!r}, food={b.get('fmade')}/{b.get('fused')}")

print("\n=== 3. WORKERS (2) ===")
for w in d['workers']:
    print(f"{w['id']}: name={w['name']!r}, tip={w['tip']!r}, hotkey={w['hotkey']!r}, abils={w.get('abillist')!r}")

print("\n=== 4. UNITS (21) ===")
for u in d['units']:
    print(f"{u['id']}: name={u['name']!r}, tip={u['tip']!r}, hotkey={u['hotkey']!r}, abils={u.get('abillist')!r}, upgs={u.get('upgrades')!r}, targs1={u.get('targs1')!r}")

print("\n=== 5. HEROES (8) ===")
for h in d['heroes']:
    print(f"{h['id']}: name={h['name']!r}, propernames={h.get('propernames')!r}, tip={h['tip']!r}, hotkey={h['hotkey']!r}, heroabils={h.get('heroabillist')!r}, abils={h.get('abillist')!r}")

print(f"\n=== 6. UPGRADES ({len(d['upgrades'])}) ===")
for u in d['upgrades']:
    n1 = u.get('names', {}).get('name1', {}).get('val')
    t1 = u.get('tips', {}).get('tip1', {}).get('val')
    ub1 = u.get('ubertips', {}).get('ubertip1', {}).get('val')
    print(f"{u['id']} (lvls={u['levels']}): name1={n1!r}, tip1={t1!r}")

print(f"\n=== 7. ABILITIES ({len(d['abilities'])}) ===")
for a in d['abilities']:
    t1 = a.get('tips', {}).get('tip1', {}).get('val')
    print(f"{a['id']} (lvls={a['levels']}): name={a['name']!r}, tip1={t1!r}, rtip={a.get('researchtip')!r}")
