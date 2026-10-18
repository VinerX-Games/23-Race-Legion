# -*- coding: utf-8 -*-
"""Analyze nerubs_raw_dump.json and categorize objects, strings, abilities, and upgrades."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def main():
    dump_path = ROOT / "scripts/nerubs_raw_dump.json"
    data = json.loads(dump_path.read_text(encoding="utf-8"))

    print("=== 1. SELECTION ===")
    sel = data['selection']
    print(f"Selection ability: {sel['id']} name={repr(sel['name'])} tip={repr(sel['tips'].get('tip1', {}).get('val'))} hotkey={repr(sel.get('hotkey'))}")
    print(f"Ubertip: {repr(sel['ubertips'].get('ubertip1', {}).get('val'))}")
    for m in data['selection_markers']:
        print(f"Marker {m['id']}: name={repr(m['names'].get('name1', {}).get('val'))} tip={repr(m['tips'].get('tip1', {}).get('val'))} ubertip={repr(m['ubertips'].get('ubertip1', {}).get('val'))}")

    print("\n=== 2. BUILDINGS (12) ===")
    for b in data['buildings']:
        print(f"Building [{b['id']}] name={repr(b['name'])} (raw={b.get('raw_name')}) tip={repr(b['tip'])} (raw={b.get('raw_tip')}) hk={repr(b['hotkey'])} (raw={b.get('raw_hotkey')})")
        print(f"  upgrades_to={b.get('upgrades_to')} trains={b.get('train')} res={b.get('researches')} abils={b.get('abillist')} fmade={b.get('fmade')}")
        print(f"  ubertip={repr(b.get('ubertip'))} (raw={b.get('raw_ubertip')})")

    print("\n=== 3. UNITS (15) ===")
    for u in data['units']:
        print(f"Unit [{u['id']}] name={repr(u['name'])} (raw={u.get('raw_name')}) tip={repr(u['tip'])} (raw={u.get('raw_tip')}) hk={repr(u['hotkey'])} (raw={u.get('raw_hotkey')})")
        print(f"  atk1={u.get('atktype1')} dmg={u.get('dice1')}d{u.get('sides1')}+{u.get('dmgplus1')} targs1={u.get('targs1')} weap1={u.get('weaptype1')}")
        print(f"  atk2={u.get('atktype2')} dmg={u.get('dice2')}d{u.get('sides2')}+{u.get('dmgplus2')} targs2={u.get('targs2')} weap2={u.get('weaptype2')}")
        print(f"  hp={u.get('hp')} mana={u.get('mana')} def={u.get('def')} ({u.get('deftype')}) abils={u.get('abillist')} upgs={u.get('upgrades')}")
        print(f"  ubertip={repr(u.get('ubertip'))} (raw={u.get('raw_ubertip')})")

    print("\n=== 4. HEROES (3) ===")
    for h in data['heroes']:
        print(f"Hero [{h['id']}] name={repr(h['name'])} (raw={h.get('raw_name')}) proper={repr(h['propernames'])} (raw={h.get('raw_propernames')}) tip={repr(h['tip'])} (raw={h.get('raw_tip')}) hk={repr(h['hotkey'])}")
        print(f"  heroabils={h.get('heroabillist')} abils={h.get('abillist')}")
        print(f"  atk1={h.get('atktype1')} dmg={h.get('dice1')}d{h.get('sides1')}+{h.get('dmgplus1')} targs1={h.get('targs1')}")
        print(f"  ubertip={repr(h.get('ubertip'))} (raw={h.get('raw_ubertip')})")

    print("\n=== 5. UPGRADES ===")
    for up in data['upgrades']:
        print(f"Upgrade [{up['id']}] levels={up['levels']} class={up.get('raw_class')}")
        for l in range(1, up['levels'] + 1):
            nm = up['names'].get(f'name{l}', {}).get('val')
            tp = up['tips'].get(f'tip{l}', {}).get('val')
            ub = up['ubertips'].get(f'ubertip{l}', {}).get('val')
            hk = up['hotkeys'].get(f'hotkey{l}', {}).get('val')
            print(f"  L{l}: name={repr(nm)} tip={repr(tp)} hk={repr(hk)}")
            print(f"      ubertip={repr(ub)}")

    print("\n=== 6. ABILITIES ===")
    for ab in data['abilities']:
        print(f"Ability [{ab['id']}] name={repr(ab['name'])} levels={ab['levels']} hk={repr(ab['hotkey'])} res_hk={repr(ab.get('researchhotkey'))}")
        rtip = ab.get('researchtip')
        rub = ab.get('researchubertip')
        if rtip or rub:
            print(f"  Research: tip={repr(rtip)} rub={repr(rub)}")
        for l in range(1, ab['levels'] + 1):
            tp = ab['tips'].get(f'tip{l}', {}).get('val')
            ub = ab['ubertips'].get(f'ubertip{l}', {}).get('val')
            print(f"  L{l}: tip={repr(tp)}")
            print(f"      ub={repr(ub)}")

    print("\n=== 7. BUFFS ===")
    for bf in data['buffs']:
        print(f"Buff [{bf['id']}] editorname={repr(bf['editorname'])} tip={repr(bf['bufftip'])} ubertip={repr(bf['buffubertip'])}")

if __name__ == '__main__':
    main()
