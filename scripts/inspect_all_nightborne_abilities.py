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

abil_ids = [
    # Selection
    'A0HU',
    # Town hall abilities
    'A0LJ', 'A0LI', 'A0IQ', 'Argl', 'A0GL', 'A0GK', 'A1KB',
    # Tower
    'Afbt',
    # Worker
    'A0I3', 'ANha', 'Ahrp',
    # Unit abilities
    # e013: A0GE, A0G5, A0G1, A0FZ, Ault
    # e014: A0GE, A0G2
    # e015: A0GE, A0G5, A0G4, A0G6
    # e016: A0G5, A0GE, A0GG, A0G1, A0FZ
    # e017: A1O9, A0GE, A0G5, A0GJ
    # e018: A0GI, A0GH, A0GE, A0G1, A0G2
    # e019: A03C, A0GF, A0G5, A0GE
    # e01A: A1MO, A0GE, A0G5, A0G7, A0GA
    # e01B: A0G3, Ault
    # h0CA: A1RK, A1RJ, A1RL
    'A0GE', 'A0G5', 'A0G1', 'A0FZ', 'A0G2', 'A0G4', 'A0G6', 'A0GG', 'A1O9', 'A0GJ',
    'A0GI', 'A0GH', 'A03C', 'A0GF', 'A1MO', 'A0G7', 'A0GA', 'A0G3', 'A1RK', 'A1RJ', 'A1RL',
    # Hero E01E:
    'A0GM', 'A0GO', 'A0GT', 'A0GU',
    # Hero E01D:
    'A0GS', 'A0GV', 'A0GW', 'A0GX',
    # Hero E01F:
    'A0GN', 'A0GP', 'A0GQ', 'A0GR',
    # Shared / Common hero/unit abils:
    'AInv', 'Ault', 'Ashm', 'Abds', 'Arlm', 'A15N'
]

lines = []
for aid in abil_ids:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    ov = res.get('overrides', {})
    fd = res.get('fields', {})
    levels = int(ov.get('levels') or fd.get('levels') or 1)
    lines.append(f"\n==========================================")
    lines.append(f"ABILITY: {aid} (levels: {levels})")
    raw_nm = ov.get('name') or fd.get('name')
    raw_hk = ov.get('hotkey') or fd.get('hotkey')
    raw_rhk = ov.get('researchhotkey') or fd.get('researchhotkey')
    raw_rtp = ov.get('researchtip') or fd.get('researchtip')
    raw_rub = ov.get('researchubertip') or fd.get('researchubertip')
    lines.append(f"  Name: {resolve(raw_nm)} (sid: {parse_sid(raw_nm)})")
    lines.append(f"  Hotkey: {resolve(raw_hk)} (raw: {raw_hk})")
    if raw_rhk or raw_rtp or raw_rub:
        lines.append(f"  Research Hotkey: {resolve(raw_rhk)} (raw: {raw_rhk})")
        lines.append(f"  Research Tip: {resolve(raw_rtp)} (sid: {parse_sid(raw_rtp)})")
        lines.append(f"  Research Ubertip: {resolve(raw_rub)} (sid: {parse_sid(raw_rub)})")
    for lvl in range(1, levels + 1):
        raw_tp = ov.get(f'tip{lvl}') or fd.get(f'tip{lvl}') or ov.get('tip') or fd.get('tip')
        raw_ub = ov.get(f'ubertip{lvl}') or fd.get(f'ubertip{lvl}') or ov.get('ubertip') or fd.get('ubertip')
        lines.append(f"  Level {lvl}:")
        lines.append(f"    Tip: {resolve(raw_tp)} (sid: {parse_sid(raw_tp)})")
        lines.append(f"    Ubertip: {resolve(raw_ub)} (sid: {parse_sid(raw_ub)})")

out_file = ROOT / "scripts/nightborne_abilities_details.txt"
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Written {len(lines)} lines to {out_file}")
