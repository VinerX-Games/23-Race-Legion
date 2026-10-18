# -*- coding: utf-8 -*-
import json
from pathlib import Path

raw_path = Path("docs/ui_text/ice_troll_unit_abilities_raw.json")
data = json.loads(raw_path.read_text(encoding="utf-8"))

for item in data:
    aid = item['id']
    code = item['code']
    name = item['name']
    lvls = item['levels']
    hk = item['hotkey']
    unhk = item['unhotkey']
    holders = item['holders']
    fields = item['fields']
    
    print(f"==================================================")
    print(f"ID: {aid} | Code: {code} | Lvls: {lvls} | Name: '{name}' | HK: '{hk}' | UnHK: '{unhk}'")
    print(f"Holders: {', '.join(holders) if holders else 'NONE'}")
    
    # print relevant mechanical fields
    for l in range(1, lvls + 1):
        sfx = str(l) if lvls > 1 or f'cool{l}' in fields else '1'
        c = fields.get(f'cool{sfx}', fields.get('cool', ''))
        m = fields.get(f'cost{sfx}', fields.get('cost', ''))
        d = fields.get(f'dur{sfx}', fields.get('dur', ''))
        hd = fields.get(f'herodur{sfx}', fields.get('herodur', ''))
        da = fields.get(f'dataa{sfx}', fields.get('dataa', ''))
        db = fields.get(f'datab{sfx}', fields.get('datab', ''))
        dc = fields.get(f'datac{sfx}', fields.get('datac', ''))
        dd = fields.get(f'datad{sfx}', fields.get('datad', ''))
        area = fields.get(f'area{sfx}', fields.get('area', ''))
        targ = fields.get(f'targs{sfx}', fields.get('targs', ''))
        print(f"  [L{l}] Cool: {c}s | Cost: {m} | Dur: {d}s (hero: {hd}s) | Area: {area} | Targets: {targ}")
        print(f"       Data: A={da}, B={db}, C={dc}, D={dd}")
        
    for ld in item['levels_data']:
        l = ld['level']
        t = ld['tip']
        u = ld['ubertip']
        print(f"  [L{l} Tip] {t}")
        print(f"  [L{l} Uber] {u}")
        if ld['untip'] or ld['unubertip']:
            print(f"  [L{l} UnTip] {ld['untip']}")
            print(f"  [L{l} UnUber] {ld['unubertip']}")
