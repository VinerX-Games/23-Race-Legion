# -*- coding: utf-8 -*-
import json
import sys

data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))

with open('scripts/abilities_detail.txt', 'w', encoding='utf-8') as f:
    for i, ab in enumerate(data['abilities']):
        aid = ab['id']
        name = ab.get('name')
        name_sid = ab.get('name_sid')
        hotkey = ab.get('hotkey')
        levels = ab.get('levels', 1)
        f.write(f"[{i+1}] Ability {aid} (lvls={levels}, hotkey='{hotkey}'): name='{name}' (sid={name_sid})\n")
        if ab.get('researchtip_sid') or ab.get('researchubertip_sid'):
            f.write(f"  researchtip: sid={ab.get('researchtip_sid')}, val='{ab.get('researchtip')}'\n")
            f.write(f"  researchubertip: sid={ab.get('researchubertip_sid')}, val='{ab.get('researchubertip')}'\n")
        if ab.get('untip_sid') or ab.get('unubertip_sid'):
            f.write(f"  untip: sid={ab.get('untip_sid')}, val='{ab.get('untip')}'\n")
            f.write(f"  unubertip: sid={ab.get('unubertip_sid')}, val='{ab.get('unubertip')}'\n")
        for lvl in range(1, levels + 1):
            t = ab.get('tips', {}).get(f'tip{lvl}', {})
            u = ab.get('ubertips', {}).get(f'ubertip{lvl}', {})
            f.write(f"  L{lvl}: tip: sid={t.get('sid')}, val='{t.get('val')}'\n")
            f.write(f"      ubertip: sid={u.get('sid')}, val='{u.get('val')}'\n")
        f.write("\n")

print("Wrote scripts/abilities_detail.txt")
