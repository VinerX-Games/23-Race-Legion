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
buff_ids = set()
for aid, a in inv['abilities'].items():
    f = a['fields']
    for k, v in f.items():
        if 'buff' in k.lower():
            print(f"{aid}.{k} = {v}")
            for part in str(v).split(','):
                part = part.strip()
                if part and part != 'None' and len(part) == 4:
                    buff_ids.add(part)

print(f"\nDiscovered buff IDs: {sorted(buff_ids)}")
for bid in sorted(buff_ids):
    res_b = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid])
    bf = res_b.get('object', {}) or res_b.get('fields', {})
    name_sid, name_val = res(bf.get('name'))
    tip_sid, tip_val = res(bf.get('tip'))
    ubt_sid, ubt_val = res(bf.get('ubertip'))
    print(f"[{bid}] Name: {name_val} (sid={name_sid})")
    print(f"      Tip: {tip_val} (sid={tip_sid})")
    print(f"      Ubt: {ubt_val} (sid={ubt_sid})")
