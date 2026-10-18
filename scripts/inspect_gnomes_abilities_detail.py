# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

lines = []
for a in d['abilities']:
    aid = a['id']
    lvls = a['levels']
    lines.append(f"=== {aid} (lvls={lvls}) ===")
    lines.append(f"  name ({a.get('name_sid')}): {a.get('name')}")
    lines.append(f"  hotkey: {a.get('hotkey')} | rhotkey: {a.get('researchhotkey')}")
    if a.get('researchtip_sid') or a.get('researchtip'):
        lines.append(f"  researchtip ({a.get('researchtip_sid')}): {a.get('researchtip')}")
    if a.get('researchubertip_sid') or a.get('researchubertip'):
        lines.append(f"  researchubertip ({a.get('researchubertip_sid')}): {a.get('researchubertip')}")
    for i in range(1, lvls+1):
        t = a['tips'].get(f'tip{i}', {})
        ub = a['ubertips'].get(f'ubertip{i}', {})
        lines.append(f"  Lvl {i}:")
        lines.append(f"    tip ({t.get('sid')}): {t.get('val')}")
        lines.append(f"    ubertip ({ub.get('sid')}): {ub.get('val')}")

out_path = ROOT / "scripts/gnomes_abilities_details.txt"
out_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote abilities details to {out_path}")
