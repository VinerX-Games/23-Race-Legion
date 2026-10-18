# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit

units = [
    'o03W', 'o03F', 'o03G', 'o03H', 'o03I', 'o03K', 'o03L', 'o03M',
    'o03N', 'o03O', 'o03P', 'o03Q', 'o03R', 'o03S', 'o03T', 'o03U', 'o03V'
]
heroes = ['N05J', 'N05K', 'N05L']

print("=== HEROES ===")
for hid in heroes:
    h = inspect_unit(hid)
    print(f"\nHero {hid}:")
    print(f"  raw_name: {h['raw_name']} -> '{h['name']}'")
    print(f"  raw_propernames: {h['raw_propernames']} -> '{h['propernames']}'")
    print(f"  raw_tip: {h['raw_tip']} -> '{h['tip']}'")
    print(f"  raw_ubertip: {h['raw_ubertip']} -> '{h['ubertip']}'")
    print(f"  raw_awakentip: {h['raw_awakentip']} -> '{h['awakentip']}'")
    print(f"  raw_revivetip: {h['raw_revivetip']} -> '{h['revivetip']}'")
    print(f"  raw_hotkey: {h['raw_hotkey']} -> '{h['hotkey']}'")
    print(f"  primary={h['fields'].get('pra')}, abillist={h['heroabillist']}, abils={h['abillist']}")
    print(f"  atktype1={h['atktype1']}, targs1={h['targs1']}, weaptype1={h['weaptype1']}")
    print(f"  atktype2={h['atktype2']}, targs2={h['targs2']}, weaptype2={h['weaptype2']}")

print("\n=== UNITS ===")
for uid in units:
    u = inspect_unit(uid)
    print(f"\nUnit {uid}:")
    print(f"  raw_name: {u['raw_name']} -> '{u['name']}'")
    print(f"  raw_tip: {u['raw_tip']} -> '{u['tip']}'")
    print(f"  raw_ubertip: {u['raw_ubertip']} -> '{u['ubertip']}'")
    print(f"  raw_hotkey: {u['raw_hotkey']} -> '{u['hotkey']}'")
    print(f"  hp={u['hp']}, def={u['def']}, deftype={u['deftype']}")
    print(f"  atktype1={u['atktype1']}, targs1={u['targs1']}, weaptype1={u['weaptype1']}")
    print(f"  atktype2={u['atktype2']}, targs2={u['targs2']}, weaptype2={u['weaptype2']}")
    print(f"  abillist={u['abillist']}")
    print(f"  upgrades={u['upgrades']}")
