# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))

out_lines = []

def p(s=""):
    out_lines.append(s)

p("================================================================================")
p("CULT OF THE DAMNED (КУЛЬТ ПРОКЛЯТЫХ) FULL AUDIT")
p("================================================================================")

p("\n--- 1. SELECTION & MARKERS ---")
s = data['selection']
p(f"Selection Ability: id={s['id']}, name={s.get('name')} (sid={s.get('name_sid')}), hotkey={s.get('hotkey')}")
p(f"   tips: {s.get('tips')}")
p(f"   ubertips: {s.get('ubertips')}")
p(f"   researchtip: {s.get('researchtip')} (sid={s.get('researchtip_sid')})")
p(f"   researchubertip: {s.get('researchubertip')} (sid={s.get('researchubertip_sid')})")

for m in data['selection_markers']:
    p(f"Marker: id={m['id']}, levels={m.get('levels')}")
    p(f"   names: {m.get('names')}")
    p(f"   tips: {m.get('tips')}")
    p(f"   ubertips: {m.get('ubertips')}")

p("\n--- 2. BUILDINGS (10) ---")
for b in data['buildings']:
    p(f"\nBuilding [{b['id']}]: name='{b.get('name')}' (sid={b.get('name_sid')}), hotkey='{b.get('hotkey')}'")
    p(f"   tip: sid={b.get('tip_sid')}, val='{b.get('tip')}'")
    p(f"   ubertip: sid={b.get('ubertip_sid')}, val='{b.get('ubertip')}'")
    p(f"   train: {b.get('train')}")
    p(f"   researches: {b.get('researches')}")
    p(f"   upgrades_to: {b.get('upgrades_to')}")
    p(f"   hp={b.get('hp')}, gold={b.get('goldcost')}, lumber={b.get('lumbercost')}, fmade={b.get('fmade')}, fused={b.get('fused')}")
    p(f"   attacks: targs1={b.get('targs1')}, targs2={b.get('targs2')}")
    p(f"   abillist: {b.get('abillist')}")

p("\n--- 3. HEROES (3) ---")
for h in data['heroes']:
    p(f"\nHero [{h['id']}]: name='{h.get('name')}' (sid={h.get('name_sid')}), hotkey='{h.get('hotkey')}'")
    p(f"   tip: sid={h.get('tip_sid')}, val='{h.get('tip')}'")
    p(f"   ubertip: sid={h.get('ubertip_sid')}, val='{h.get('ubertip')}'")
    p(f"   propernames: raw='{h.get('raw_propernames')}', val='{h.get('propernames')}'")
    p(f"   awakentip: raw='{h.get('raw_awakentip')}', val='{h.get('awakentip')}'")
    p(f"   revivetip: raw='{h.get('raw_revivetip')}', val='{h.get('revivetip')}'")
    p(f"   heroabillist: {h.get('heroabillist')}")
    p(f"   abillist: {h.get('abillist')}")
    p(f"   targs1={h.get('targs1')}, targs2={h.get('targs2')}")

p("\n--- 4. UNITS (18) ---")
for u in data['units']:
    p(f"\nUnit [{u['id']}]: name='{u.get('name')}' (sid={u.get('name_sid')}), hotkey='{u.get('hotkey')}'")
    p(f"   tip: sid={u.get('tip_sid')}, val='{u.get('tip')}'")
    p(f"   ubertip: sid={u.get('ubertip_sid')}, val='{u.get('ubertip')}'")
    p(f"   abillist: {u.get('abillist')}")
    p(f"   targs1={u.get('targs1')}, targs2={u.get('targs2')}")

p("\n--- 5. UPGRADES (20) ---")
for up in data['upgrades']:
    p(f"\nUpgrade [{up['id']}]: levels={up.get('levels')}")
    p(f"   names: {up.get('names')}")
    p(f"   tips: {up.get('tips')}")
    p(f"   ubertips: {up.get('ubertips')}")
    p(f"   hotkeys: {up.get('hotkeys')}")
    p(f"   fields: {up.get('fields')}")

p("\n--- 6. ABILITIES (56) ---")
for ab in data['abilities']:
    p(f"\nAbility [{ab['id']}]: name='{ab.get('name')}' (sid={ab.get('name_sid')}), levels={ab.get('levels')}, hotkey='{ab.get('hotkey')}'")
    p(f"   tips: {ab.get('tips')}")
    p(f"   ubertips: {ab.get('ubertips')}")
    p(f"   researchtip: {ab.get('researchtip')} (sid={ab.get('researchtip_sid')})")
    p(f"   researchubertip: {ab.get('researchubertip')} (sid={ab.get('researchubertip_sid')})")
    p(f"   untip: {ab.get('untip')} (sid={ab.get('untip_sid')})")
    p(f"   unubertip: {ab.get('unubertip')} (sid={ab.get('unubertip_sid')})")
    p(f"   fields: {ab.get('fields')}")

Path('scripts/cult_audit_text.txt').write_text('\n'.join(out_lines), encoding='utf-8')
print(f"Audit written to scripts/cult_audit_text.txt ({len(out_lines)} lines)")
