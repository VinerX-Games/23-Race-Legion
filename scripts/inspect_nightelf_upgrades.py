# -*- coding: utf-8 -*-
"""Inspect all Night Elf upgrades and write to UTF-8 file."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/nightelf_raw_dump.json').read_text(encoding='utf-8'))

out = []
for upg in dump['upgrades']:
    out.append(f"=== {upg['id']} [levels: {upg['levels']}] ===")
    for i in range(1, upg['levels'] + 1):
        n = upg['names'].get(f'name{i}', {})
        t = upg['tips'].get(f'tip{i}', {})
        ub = upg['ubertips'].get(f'ubertip{i}', {})
        hk = upg['hotkeys'].get(f'hotkey{i}', {})
        out.append(f"  L{i} [{hk.get('val')}]: name=[{n.get('raw')}] {n.get('val')}")
        out.append(f"      tip: [{t.get('raw')}] {t.get('val')}")
        out.append(f"      ub: [{ub.get('raw')}] {ub.get('val')}")
    out.append("")

(ROOT / 'scripts/nightelf_upgrades_details.txt').write_text("\n".join(out), encoding='utf-8')
print("Wrote UTF-8 nightelf_upgrades_details.txt")
