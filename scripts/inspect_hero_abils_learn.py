# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:]), wts.get(int(s[8:]), '')
    return None, str(s)

inv = json.loads((ROOT / 'scripts/scarlet_complete_inventory.json').read_text(encoding='utf-8'))
hero_abils = ['A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J']
for aid in hero_abils:
    f = inv['abilities'][aid]['fields']
    rt = f.get('researchtip')
    ru = f.get('researchubertip')
    rh = f.get('researchhotkey')
    print(f"=== {aid} ===")
    print(f"  researchtip: {rt} -> {res(rt)}")
    print(f"  researchubertip: {ru} -> {res(ru)}")
    print(f"  researchhotkey: {rh} -> {res(rh)}")
