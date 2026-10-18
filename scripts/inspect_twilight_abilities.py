# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

# Load discovered ability IDs from twilight_hammer_raw_dump.json
dump_path = ROOT / "scripts/twilight_hammer_raw_dump.json"
dump = json.loads(dump_path.read_text(encoding="utf-8"))
ability_ids = [a['id'] for a in dump['abilities']]

# Also check abilities on n00D and n00C
extra_abils = ['A0A1', 'A0A0', 'A09X', 'A09W', 'A09V', 'A1QQ']
for ea in extra_abils:
    if ea not in ability_ids:
        ability_ids.append(ea)

print(f"Total abilities to inspect: {len(ability_ids)}")

def inspect_ab(aid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {})
    ov = res.get('overrides', {})
    levels = int(f.get('levels') or 1)
    lines = [f"=== ABILITY {aid} (levels: {levels}) ==="]
    name = resolve(f.get('name'))
    raw_name = f.get('name')
    hk = resolve(f.get('hotkey'))
    raw_hk = f.get('hotkey')
    rhk = resolve(f.get('researchhotkey'))
    raw_rhk = f.get('researchhotkey')
    rtip = resolve(f.get('researchtip'))
    raw_rtip = f.get('researchtip')
    rub = resolve(f.get('researchubertip'))
    raw_rub = f.get('researchubertip')
    lines.append(f" Name: {name} (raw: {raw_name})")
    lines.append(f" Hotkey: {hk} (raw: {raw_hk}), ResearchHotkey: {rhk} (raw: {raw_rhk})")
    if rtip or raw_rtip:
        lines.append(f" ResearchTip: {rtip} (raw: {raw_rtip})")
    if rub or raw_rub:
        lines.append(f" ResearchUbertip: {rub} (raw: {raw_rub})")
    for i in range(1, levels + 1):
        tip = resolve(f.get(f'tip{i}') or f.get('tip'))
        raw_t = f.get(f'tip{i}') or f.get('tip')
        ub = resolve(f.get(f'ubertip{i}') or f.get('ubertip'))
        raw_u = f.get(f'ubertip{i}') or f.get('ubertip')
        lines.append(f" Level {i}:")
        lines.append(f"   tip: {tip} (raw: {raw_t})")
        lines.append(f"   ubertip: {ub} (raw: {raw_u})")
    return "\n".join(lines)

output = []
for aid in sorted(ability_ids):
    output.append(inspect_ab(aid))

(ROOT / "scripts/twilight_abilities_dump.txt").write_text("\n\n".join(output), encoding="utf-8")
print("Done writing twilight_abilities_dump.txt")
