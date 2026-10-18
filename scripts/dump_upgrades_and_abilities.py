# -*- coding: utf-8 -*-
import json
import sys

data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))
out_file = open('scripts/dump_upg_abils.txt', 'w', encoding='utf-8')

def print(*args, **kwargs):
    kwargs['file'] = out_file
    __builtins__.print(*args, **kwargs)

print("=== ALL UPGRADES (20) ===")
for i, up in enumerate(data['upgrades']):
    uid = up['id']
    lvls = up.get('levels', 1)
    name1 = up.get('names', {}).get('name1', {}).get('val', '')
    name1_sid = up.get('names', {}).get('name1', {}).get('sid')
    print(f"\n[{i+1}] Upgrade {uid} (levels={lvls}): name1='{name1}' (sid={name1_sid})")
    for lvl in range(1, lvls + 1):
        n = up.get('names', {}).get(f'name{lvl}', {})
        t = up.get('tips', {}).get(f'tip{lvl}', {})
        u = up.get('ubertips', {}).get(f'ubertip{lvl}', {})
        h = up.get('hotkeys', {}).get(f'hotkey{lvl}', {})
        print(f"  L{lvl}: name='{n.get('val')}' (sid={n.get('sid')})")
        print(f"      tip='{t.get('val')}' (sid={t.get('sid')}) [hotkey={h.get('val')}]")
        print(f"      ubertip='{u.get('val')}' (sid={u.get('sid')})")

print("\n=== ALL ABILITIES (56) ===")
for i, ab in enumerate(data['abilities']):
    aid = ab['id']
    lvls = ab.get('levels', 1)
    name = ab.get('name', '')
    name_sid = ab.get('name_sid')
    hotkey = ab.get('hotkey', '')
    rtip = ab.get('researchtip')
    rtip_sid = ab.get('researchtip_sid')
    rubertip = ab.get('researchubertip')
    rubertip_sid = ab.get('researchubertip_sid')
    untip = ab.get('untip')
    untip_sid = ab.get('untip_sid')
    unubertip = ab.get('unubertip')
    unubertip_sid = ab.get('unubertip_sid')
    
    tips = ab.get('tips', {})
    ubertips = ab.get('ubertips', {})
    
    print(f"\n[{i+1}] Ability {aid} (lvls={lvls}): name='{name}' (sid={name_sid}), hotkey='{hotkey}'")
    if rtip or rubertip:
        print(f"  Research: tip='{rtip}' (sid={rtip_sid}) | ubertip='{rubertip}' (sid={rubertip_sid})")
    if untip or unubertip:
        print(f"  Un: tip='{untip}' (sid={untip_sid}) | ubertip='{unubertip}' (sid={unubertip_sid})")
    for lvl in range(1, lvls + 1):
        t = tips.get(f'tip{lvl}', {})
        u = ubertips.get(f'ubertip{lvl}', {})
        print(f"  L{lvl}: tip='{t.get('val')}' (sid={t.get('sid')})")
        print(f"      ubertip='{u.get('val')}' (sid={u.get('sid')})")
