# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

lines = []
for u in d['upgrades']:
    uid = u['id']
    lvls = u['levels']
    lines.append(f"=== {uid} (lvls={lvls}) ===")
    for i in range(1, lvls+1):
        n = u['names'].get(f'name{i}', {})
        t = u['tips'].get(f'tip{i}', {})
        ub = u['ubertips'].get(f'ubertip{i}', {})
        hk = u['hotkeys'].get(f'hotkey{i}', {})
        lines.append(f"  Lvl {i}:")
        lines.append(f"    name ({n.get('sid')}): {n.get('val')}")
        lines.append(f"    tip ({t.get('sid')}): {t.get('val')}")
        lines.append(f"    ubertip ({ub.get('sid')}): {ub.get('val')}")
        lines.append(f"    hotkey: {hk.get('val')}")

out_path = ROOT / "scripts/gnomes_upgrades_details.txt"
out_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote upgrades details to {out_path}")
