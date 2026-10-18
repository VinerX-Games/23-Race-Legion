# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))

print('=== SELECTION ===')
s = data['selection']
print(f"id: {s.get('id')}, name: {s.get('name')}, name_sid: {s.get('name_sid')}, hotkey: {s.get('hotkey')}")
print(f"researchtip: {s.get('researchtip')}, sid: {s.get('researchtip_sid')}")
print(f"researchubertip: {s.get('researchubertip')}, sid: {s.get('researchubertip_sid')}")
print(f"tips: {s.get('tips')}")
print(f"ubertips: {s.get('ubertips')}")

print('\n=== SELECTION MARKERS ===')
for m in data['selection_markers']:
    print(m['id'], m.get('names'), m.get('tips'), m.get('ubertips'))

print('\n=== BUILDINGS (10) ===')
for b in data['buildings']:
    print(f"{b['id']}: name='{b.get('name')}' (sid={b.get('name_sid')}), hotkey={b.get('hotkey')}, tip_sid={b.get('tip_sid')}, ubertip_sid={b.get('ubertip_sid')}")
    print(f"   tip: {b.get('tip')}")
    print(f"   ubertip: {b.get('ubertip')}")
    print(f"   train: {b.get('train')}, researches: {b.get('researches')}, upgrades_to: {b.get('upgrades_to')}")
    print(f"   attacks: targs1={b.get('targs1')}, targs2={b.get('targs2')}")

print('\n=== HEROES (3) ===')
for h in data['heroes']:
    print(f"{h['id']}: name='{h.get('name')}', propernames='{h.get('propernames')}', hotkey={h.get('hotkey')}")
    print(f"   name_sid={h.get('name_sid')}, tip_sid={h.get('tip_sid')}, ubertip_sid={h.get('ubertip_sid')}")
    print(f"   raw_revivetip={h.get('raw_revivetip')}, raw_awakentip={h.get('raw_awakentip')}")
    print(f"   heroabillist: {h.get('heroabillist')}, targs1={h.get('targs1')}")
    print(f"   ubertip: {h.get('ubertip')}")

print('\n=== UNITS (18) ===')
for u in data['units']:
    print(f"{u['id']}: name='{u.get('name')}', hotkey={u.get('hotkey')}, tip_sid={u.get('tip_sid')}, ubertip_sid={u.get('ubertip_sid')}")
    print(f"   tip: {u.get('tip')}")
    print(f"   ubertip: {u.get('ubertip')}")
    print(f"   abillist: {u.get('abillist')}, targs1={u.get('targs1')}, targs2={u.get('targs2')}")

print('\n=== UPGRADES (20) ===')
for up in data['upgrades']:
    print(f"{up['id']}: names={up.get('names')}, levels={up.get('levels')}, tips={up.get('tips')}, ubertips={up.get('ubertips')}")

print('\n=== ABILITIES (56) ===')
for ab in data['abilities']:
    print(f"{ab['id']}: name='{ab.get('name')}' (sid={ab.get('name_sid')}), levels={ab.get('levels')}, hotkey={ab.get('hotkey')}, tips={ab.get('tips')}, ubertips={ab.get('ubertips')}")
