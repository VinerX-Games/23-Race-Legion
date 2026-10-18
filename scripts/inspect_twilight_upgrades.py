# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def inspect_upg(uid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    f = res.get('fields', {})
    levels = int(f.get('maxlevel') or f.get('levels') or 1)
    lines = [f"=== UPGRADE {uid} (levels: {levels}) ==="]
    for i in range(1, levels + 1):
        name = resolve(f.get(f'name{i}') or f.get('name'))
        tip = resolve(f.get(f'tip{i}'))
        ubertip = resolve(f.get(f'ubertip{i}'))
        hk = resolve(f.get(f'hotkey{i}') or f.get('hotkey'))
        raw_name = f.get(f'name{i}') or f.get('name')
        raw_tip = f.get(f'tip{i}')
        raw_ub = f.get(f'ubertip{i}')
        raw_hk = f.get(f'hotkey{i}') or f.get('hotkey')
        lines.append(f" Level {i}:")
        lines.append(f"   name: {name} (raw: {raw_name})")
        lines.append(f"   tip: {tip} (raw: {raw_tip})")
        lines.append(f"   hotkey: {hk} (raw: {raw_hk})")
        lines.append(f"   ubertip: {ubertip} (raw: {raw_ub})")
    return "\n".join(lines)

all_upgs = ['R07K', 'R0KD', 'R04D', 'R04V', 'R00O', 'R04S', 'R04U', 'R0EJ', 'R05S', 'R05T', 'R05U', 'R05V', 'R04Z', 'R050', 'R051', 'R052', 'R04W', 'R04X']
output = []
for u in all_upgs:
    output.append(inspect_upg(u))

(ROOT / "scripts/twilight_upgrades_dump.txt").write_text("\n\n".join(output), encoding="utf-8")
print("Done writing twilight_upgrades_dump.txt")
