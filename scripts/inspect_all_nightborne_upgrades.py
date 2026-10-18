# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def parse_sid(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            return int(val[8:])
        except ValueError:
            pass
    return None

upg_ids = [
    # Selection
    'R07J',
    # Lumber mill (h0CH)
    'R0DU', 'R06U', 'R06V', 'R06W', 'R06X', 'R06Y',
    # Barracks (h0CF)
    'R06G', 'R06H', 'R06I', 'R06J',
    # Sanctum (h0CI)
    'R06T', 'R06S',
    # Temple (h0CK)
    'R06K', 'R06L', 'R06M', 'R06N',
    # House of Shal'dorei Guard (h0CL)
    'R06P', 'R06O', 'R06Q', 'R06R',
]

lines = []
for uid in upg_ids:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    ov = res.get('overrides', {})
    fd = res.get('fields', {})
    levels = int(ov.get('maxlevel') or fd.get('maxlevel') or ov.get('levels') or fd.get('levels') or 1)
    lines.append(f"\n==========================================")
    lines.append(f"UPGRADE: {uid} (levels: {levels})")
    lines.append(f"  class: {ov.get('class') or fd.get('class')}")
    lines.append(f"  applies to: {ov.get('appliesto') or fd.get('appliesto')}")
    for lvl in range(1, levels + 1):
        raw_nm = ov.get(f'name{lvl}') or fd.get(f'name{lvl}') or ov.get('name') or fd.get('name')
        raw_tp = ov.get(f'tip{lvl}') or fd.get(f'tip{lvl}')
        raw_ub = ov.get(f'ubertip{lvl}') or fd.get(f'ubertip{lvl}')
        raw_hk = ov.get(f'hotkey{lvl}') or fd.get(f'hotkey{lvl}') or ov.get('hotkey') or fd.get('hotkey')
        lines.append(f"  Level {lvl}:")
        lines.append(f"    Name: {resolve(raw_nm)} (sid: {parse_sid(raw_nm)})")
        lines.append(f"    Hotkey: {resolve(raw_hk)} (raw: {raw_hk})")
        lines.append(f"    Tip: {resolve(raw_tp)} (sid: {parse_sid(raw_tp)})")
        lines.append(f"    Ubertip: {resolve(raw_ub)} (sid: {parse_sid(raw_ub)})")

out_file = ROOT / "scripts/nightborne_upgrades_details.txt"
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Written {len(lines)} lines to {out_file}")
