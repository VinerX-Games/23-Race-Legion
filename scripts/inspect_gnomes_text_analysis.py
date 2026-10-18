# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

lines = []
lines.append("=== 1. SELECTION & MARKERS ===")
lines.append(f"Selection ability: {d['selection']['id']} | Name: {d['selection']['name']} | Tip: {d['selection']['tips']} | Ubertip: {d['selection']['ubertips']}")
for m in d['selection_markers']:
    lines.append(f"Marker {m['id']}: name={m['names']} tip={m['tips']} ubertip={m['ubertips']}")

lines.append("\n=== 2. BUILDINGS (10) ===")
for b in d['buildings']:
    lines.append(f"Building {b['id']}: name={b['name']} | tip={b['tip']} | hotkey={b['hotkey']} | ubertip={b['ubertip']}")
    lines.append(f"   trains={b.get('train')} | researches={b.get('researches')} | upgrades_to={b.get('upgrades_to')} | food={b.get('fmade')}/{b.get('fused')}")

lines.append("\n=== 3. WORKERS (2) ===")
for w in d['workers']:
    lines.append(f"Worker {w['id']}: name={w['name']} | tip={w['tip']} | hotkey={w['hotkey']} | ubertip={w['ubertip']}")
    lines.append(f"   abillist={w.get('abillist')} | builds={w.get('builds')}")

lines.append("\n=== 4. UNITS (21) ===")
for u in d['units']:
    lines.append(f"Unit {u['id']}: name={u['name']} | tip={u['tip']} | hotkey={u['hotkey']} | ubertip={u['ubertip']}")
    lines.append(f"   abillist={u.get('abillist')} | upgrades={u.get('upgrades')} | atk1={u.get('atktype1')}/{u.get('targs1')} | atk2={u.get('atktype2')}/{u.get('targs2')}")

lines.append("\n=== 5. HEROES (8) ===")
for h in d['heroes']:
    lines.append(f"Hero {h['id']}: name={h['name']} | propernames={h.get('propernames')} | tip={h['tip']} | ubertip={h['ubertip']}")
    lines.append(f"   heroabillist={h.get('heroabillist')} | abillist={h.get('abillist')} | primary={h['fields'].get('pra')} | atk1={h.get('atktype1')}/{h.get('targs1')}")

lines.append(f"\n=== 6. UPGRADES ({len(d['upgrades'])}) ===")
for u in d['upgrades']:
    lines.append(f"Upgrade {u['id']} (lvls={u['levels']}):")
    for i in range(1, u['levels'] + 1):
        n = u['names'].get(f'name{i}', {}).get('val')
        t = u['tips'].get(f'tip{i}', {}).get('val')
        ub = u['ubertips'].get(f'ubertip{i}', {}).get('val')
        hk = u['hotkeys'].get(f'hotkey{i}', {}).get('val')
        lines.append(f"   Lvl {i}: name={n} | tip={t} | hotkey={hk} | ubertip={ub}")

lines.append(f"\n=== 7. ABILITIES ({len(d['abilities'])}) ===")
for a in d['abilities']:
    lines.append(f"Ability {a['id']} (lvls={a['levels']}): name={a['name']} | hotkey={a.get('hotkey')} | rhotkey={a.get('researchhotkey')}")
    if a.get('researchtip') or a.get('researchubertip'):
        lines.append(f"   Research: tip={a.get('researchtip')} | ubertip={a.get('researchubertip')}")
    for i in range(1, a['levels'] + 1):
        t = a['tips'].get(f'tip{i}', {}).get('val')
        ub = a['ubertips'].get(f'ubertip{i}', {}).get('val')
        lines.append(f"   Lvl {i}: tip={t} | ubertip={ub}")

lines.append(f"\n=== 8. BUFFS ({len(d['buffs'])}) ===")
for b in d['buffs']:
    lines.append(f"Buff {b['id']}: editorname={b.get('editorname')} | tip={b.get('bufftip')} | ubertip={b.get('buffubertip')}")

out_path = ROOT / "scripts/gnomes_analysis.txt"
out_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote analysis to {out_path}")
