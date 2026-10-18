# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def check_units(uids, title):
    print(f"=== {title} ===")
    for uid in uids:
        res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
        f = res.get('object', {}) or res.get('fields', {})
        name = resolve(f.get('name'))
        tip = resolve(f.get('tip'))
        trains = f.get('trains') or f.get('train')
        reses = f.get('researches')
        abils = f.get('abils') or f.get('abillist')
        heroabils = f.get('heroabils') or f.get('heroabillist')
        print(f"[{uid}] {name}")
        print(f"   tip: {tip}")
        if trains: print(f"   trains: {trains}")
        if reses: print(f"   researches: {reses}")
        if abils: print(f"   abils: {abils}")
        if heroabils: print(f"   heroabils: {heroabils}")

undead_check = ['u00A', 'u00B', 'u00C', 'u00D', 'u00E', 'u008', 'U00O', 'U00V', 'U00U', 'U030', 'u00P', 'u034', 'u03E', 'u00H', 'u00I', 'u00J', 'u00K', 'u00L', 'u00M', 'u00N', 'n012', 'n014', 'u00F', 'u00G', 'u017', 'u03B']
check_units(undead_check, "UNDEAD INSPECTION")

scarlet_check = ['h05U', 'h05V', 'h05W', 'h05X', 'h05Y', 'h05Z', 'h060', 'h061', 'h062', 'h063', 'h064', 'h068', 'h014', 'h039', 'h03A', 'h03B', 'h03C', 'h03D', 'h03F', 'h03G', 'h03I', 'h065', 'h066', 'h067', 'n007', 'n008', 'o00I', 'H03H', 'H06C', 'H06B']
check_units(scarlet_check, "SCARLET INSPECTION")
