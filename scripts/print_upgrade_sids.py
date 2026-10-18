# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

def parse_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:])
    return None

print("=== UPGRADES ===")
for u in dump['upgrades']:
    uid = u['id']
    lvls = u.get('levels', 1)
    print(f"\nUpgrade {uid} (lvls={lvls}):")
    for lvl in range(1, lvls + 1):
        n_raw = u['names'].get(f'name{lvl}', {}).get('raw')
        t_raw = u['tips'].get(f'tip{lvl}', {}).get('raw')
        ub_raw = u['ubertips'].get(f'ubertip{lvl}', {}).get('raw')
        hk_raw = u['hotkeys'].get(f'hotkey{lvl}', {}).get('raw')
        hk_val = u['hotkeys'].get(f'hotkey{lvl}', {}).get('val')
        print(f"  L{lvl}: name_sid={parse_sid(n_raw)} tip_sid={parse_sid(t_raw)} ub_sid={parse_sid(ub_raw)} hk='{hk_val}'")
