# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / 'scripts/twilight_race_abils_detailed.json', encoding='utf-8'))

lines = []
for aid, info in sorted(data.items()):
    name = info['name']['val']
    lvls = info['levels']
    hk = info['hotkey']['val']
    rhk = info['researchhotkey']['val']
    rtip = info['researchtip']['val']
    rub = info['researchubertip']['val']
    lines.append(f"=== {aid}: {name} (lvls: {lvls}, hk: {hk}, rhk: {rhk}) ===")
    if rtip or rub:
        lines.append(f"  researchtip: {rtip}")
        lines.append(f"  researchub: {rub}")
    for lk, ld in info['levels_data'].items():
        tip = ld['tip']['val']
        ub = ld['ubertip']['val']
        lines.append(f"  {lk}: tip={tip}")
        lines.append(f"      ub={ub}")
    lines.append("")

(ROOT / 'scripts/abils_clean.txt').write_text("\n".join(lines), encoding='utf-8')
print("Wrote scripts/abils_clean.txt")
