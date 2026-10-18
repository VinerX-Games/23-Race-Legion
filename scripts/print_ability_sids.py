# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

def parse_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:])
    return None

print("=== ABILITIES ===")
for a in dump['abilities']:
    aid = a['id']
    name_sid = parse_sid(a.get('raw_name'))
    rtip_sid = parse_sid(a.get('raw_researchtip'))
    rub_sid = parse_sid(a.get('raw_researchubertip'))
    lvls = a.get('levels', 1)
    tips_sids = [parse_sid(a.get('tips', {}).get(f'tip{i}', {}).get('raw')) for i in range(1, lvls + 1)]
    ubs_sids = [parse_sid(a.get('ubertips', {}).get(f'ubertip{i}', {}).get('raw')) for i in range(1, lvls + 1)]
    print(f"{aid}: name_sid={name_sid} rtip_sid={rtip_sid} rub_sid={rub_sid} lvls={lvls} tips={tips_sids} ubs={ubs_sids}")
