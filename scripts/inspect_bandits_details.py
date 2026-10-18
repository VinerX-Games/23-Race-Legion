# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

d1 = json.load(open('scripts/bandits_raw_dump.json', encoding='utf-8'))
d2 = json.load(open('scripts/bandits_abils_upgrades_dump.json', encoding='utf-8'))

print("=== 1. SELECTION ===")
s = d1['selection']
print(f"ID: {s['id']}")
print(f"Name raw: {s.get('raw_name')}, text: {s.get('name')}")
print(f"Tips: {s.get('tips')}")
print(f"Ubertips: {s.get('ubertips')}")
print(f"Hotkey: {s.get('hotkey')}, raw_hotkey: {s.get('raw_hotkey')}")

print("\n=== 2. BUILDINGS (17) ===")
for b in d1['buildings']:
    tips = b.get('tips', {})
    ubertips = b.get('ubertips', {})
    print(f"{b['id']}: name={b.get('name')!r} (raw={b.get('raw_name')}), hotkey={b.get('hotkey')!r}")
    print(f"   tip: {tips.get('tip1')}")
    print(f"   ubertip: {ubertips.get('ubertip1')}")

print("\n=== 3. HEROES (3) ===")
for h in d1['heroes']:
    tips = h.get('tips', {})
    ubertips = h.get('ubertips', {})
    propers = h.get('propers', {})
    print(f"{h['id']}: name={h.get('name')!r} (raw={h.get('raw_name')}), proper={propers}, hotkey={h.get('hotkey')!r}")
    print(f"   tip: {tips.get('tip1')}")
    print(f"   ubertip: {ubertips.get('ubertip1')}")

print("\n=== 4. UNITS (23) ===")
for u in d1['units']:
    tips = u.get('tips', {})
    ubertips = u.get('ubertips', {})
    print(f"{u['id']}: name={u.get('name')!r} (raw={u.get('raw_name')}), hotkey={u.get('hotkey')!r}")
    print(f"   tip: {tips.get('tip1')}")
    print(f"   ubertip: {ubertips.get('ubertip1')}")

print("\n=== 5. ABILITIES ===")
for aid, a in d2['abils'].items():
    print(f"{aid}: name={a.get('name')!r} (raw={a.get('raw_name')}), levels={a.get('levels')}")
    print(f"   hotkey: {a.get('hotkey')}")
    print(f"   tips: {a.get('tips')}")
    print(f"   ubertips: {a.get('ubertips')}")

print("\n=== 6. UPGRADES ===")
for uid, up in d2['upgrades'].items():
    print(f"{uid}: name={up.get('name')!r} (raw={up.get('raw_name')}), levels={up.get('levels')}")
    print(f"   hotkeys: {up.get('hotkeys')}")
    print(f"   tips: {up.get('tips')}")
    print(f"   ubertips: {up.get('ubertips')}")
