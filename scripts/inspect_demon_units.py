# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

unit_candidates = [
    'e02Y', 'u026', # Workers
    'n025', 'n026', 'n02D', 'n02E', # Fel guard / blood lineage
    'n023', # Fel beast
    'n027', # Mo'arg
    'n02I', # Hell chariot
    'n020', # Eredar sorcerer
    'n028', # Jailer
    'n024', # Felhound
    'n022', # Infernal
    'n021', # Doom guard
    'n029', # Fel reaver
    'ndmg', # what is ndmg?
]

for uid in unit_candidates:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    name = resolve(f.get('name'))
    tip = resolve(f.get('tip'))
    ubertip = resolve(f.get('ubertip'))
    hotkey = resolve(f.get('hotkey'))
    race = f.get('race')
    abils = f.get('abils') or res.get('overrides', {}).get('abillist')
    print(f"=== {uid}: {name} (race: {race}) ===")
    print(f"  name_raw: {f.get('name')}")
    print(f"  tip: {f.get('tip')} -> {repr(tip)}")
    print(f"  ubertip: {f.get('ubertip')} -> {repr(ubertip)}")
    print(f"  hotkey: {f.get('hotkey')} ({repr(hotkey)})")
    print(f"  abils: {abils}")
    print(f"  atk1: dice={f.get('dice1')} sides={f.get('sides1')} dmgplus={f.get('dmgplus1')} cool={f.get('cool1')} targs={f.get('targs1')}")
    print(f"  atk2: dice={f.get('dice2')} sides={f.get('sides2')} dmgplus={f.get('dmgplus2')} cool={f.get('cool2')} targs={f.get('targs2')}")
    print(f"  hp={f.get('hp')} mana={f.get('mana0') or f.get('mana')} armor={f.get('def')} deftype={f.get('deftype')}")
    print()
