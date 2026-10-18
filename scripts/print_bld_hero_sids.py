# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

def parse_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:])
    return None

print('=== BUILDINGS ===')
for b in dump['buildings']:
    print(f"{b['id']}: name_sid={parse_sid(b.get('raw_name'))} tip_sid={parse_sid(b.get('raw_tip'))} ub_sid={parse_sid(b.get('raw_ubertip'))} hk={b.get('hotkey')}")

print('\n=== HEROES ===')
for h in dump['heroes']:
    print(f"{h['id']}: name_sid={parse_sid(h.get('raw_name'))} tip_sid={parse_sid(h.get('raw_tip'))} ub_sid={parse_sid(h.get('raw_ubertip'))} awaken_sid={parse_sid(h.get('raw_awakentip'))} revive_sid={parse_sid(h.get('raw_revivetip'))} proper_sid={parse_sid(h.get('raw_propernames'))} hk={h.get('hotkey')}")
