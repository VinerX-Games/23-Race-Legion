# -*- coding: utf-8 -*-
import json

data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))
with open('scripts/units_detail.txt', 'w', encoding='utf-8') as f:
    for u in data['units']:
        f.write(f"Unit [{u['id']}]: hotkey='{u.get('hotkey')}'\n")
        f.write(f"  name: sid={u.get('name_sid')}, val='{u.get('name')}'\n")
        f.write(f"  tip: sid={u.get('tip_sid')}, val='{u.get('tip')}'\n")
        f.write(f"  ubertip: sid={u.get('ubertip_sid')}, val='{u.get('ubertip')}'\n")
        f.write(f"  attacks: targs1={u.get('targs1')}, targs2={u.get('targs2')}\n")
        f.write(f"  abillist: {u.get('abillist')}\n\n")
print("Wrote scripts/units_detail.txt")
