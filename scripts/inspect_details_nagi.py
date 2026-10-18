# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path('scripts/nagi_raw_dump.json').read_text('utf-8'))

print("=== BUILDINGS ===")
for b in dump['buildings']:
    print(f"[{b['id']}] Name: {b['raw_name']} -> {b['name']}")
    print(f"     Tip: {b['raw_tip']} -> {b['tip']}")
    print(f"     Ub: {b['raw_ubertip']} -> {repr(b['ubertip'])[:60]}...")
    print(f"     HK: {b['raw_hotkey']} -> {b['hotkey']}")
    print(f"     Trains: {b['train']}")
    print(f"     Researches: {b['researches']}")
    print(f"     Upgrades_to: {b['upgrades_to']}")
    print(f"     FoodMade: {b['fmade']}")

print("\n=== HEROES ===")
for h in dump['heroes']:
    print(f"[{h['id']}] Name: {h['raw_name']} -> {h['name']}")
    print(f"     Tip: {h['raw_tip']} -> {h['tip']}")
    print(f"     Ub: {h['raw_ubertip']} -> {repr(h['ubertip'])[:60]}...")
    print(f"     HK: {h['raw_hotkey']} -> {h['hotkey']}")
    print(f"     HeroAbils: {h['heroabillist']}")
    print(f"     Abils: {h['abillist']}")
    print(f"     Atk1: type={h['atktype1']}, dice={h['dice1']}d{h['sides1']}+{h['dmgplus1']}, targs={h['targs1']}")

print("\n=== WORKER & UNITS ===")
for u in dump['worker'] + dump['units']:
    print(f"[{u['id']}] Name: {u['raw_name']} -> {u['name']}")
    print(f"     Tip: {u['raw_tip']} -> {u['tip']}")
    print(f"     Ub: {u['raw_ubertip']} -> {repr(u['ubertip'])[:60]}...")
    print(f"     HK: {u['raw_hotkey']} -> {u['hotkey']}")
    print(f"     Abils: {u['abillist']}")
    print(f"     Upgs: {u['upgrades']}")
    print(f"     Atk1: type={u['atktype1']}, dice={u['dice1']}d{u['sides1']}+{u['dmgplus1']}, targs={u['targs1']}")
    print(f"     Atk2: type={u['atktype2']}, dice={u['dice2']}d{u['sides2']}+{u['dmgplus2']}, targs={u['targs2']}")

