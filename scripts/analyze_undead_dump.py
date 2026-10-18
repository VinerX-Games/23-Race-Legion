# -*- coding: utf-8 -*-
"""Analyze the raw dump of Undead objects, extract WTS strings and print catalog."""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

data = json.loads((ROOT / "scripts/undead_raw_dump.json").read_text(encoding="utf-8"))

def get_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

print("=== SELECTION ===")
for aid, obj in data['selection'].items():
    print(f"[{aid}] Name: {obj.get('raw_name')} -> {obj.get('name')}")
    print(f"     Tip: {obj.get('tips', {}).get('tip1', {}).get('raw')} -> {obj.get('tips', {}).get('tip1', {}).get('val')}")
    print(f"     Ubertip: {obj.get('ubertips', {}).get('ubertip1', {}).get('raw')} -> {obj.get('ubertips', {}).get('ubertip1', {}).get('val')}")
    print(f"     Hotkey: {obj.get('hotkey')}")

print("\n=== BUILDINGS ===")
for bid, obj in data['buildings'].items():
    print(f"[{bid}] Name: {obj.get('raw_name')} ({obj.get('name')}) | Tip: {obj.get('raw_tip')} | Ub: {obj.get('raw_ubertip')} | HK: {obj.get('hotkey')}")
    print(f"     Trains: {obj.get('trains')} | Res: {obj.get('researches')} | Upg: {obj.get('upgrades_to')} | Abils: {obj.get('abils')}")

print("\n=== UNITS ===")
for uid, obj in data['units'].items():
    print(f"[{uid}] Name: {obj.get('raw_name')} ({obj.get('name')}) | Tip: {obj.get('raw_tip')} | Ub: {obj.get('raw_ubertip')} | HK: {obj.get('hotkey')}")
    print(f"     Abils: {obj.get('abils')} | Upg: {obj.get('upgrades')} | Targs1: {obj.get('targs1')}")

print("\n=== HEROES ===")
for hid, obj in data['heroes'].items():
    print(f"[{hid}] Name: {obj.get('raw_name')} ({obj.get('name')}) | Propernames: {obj.get('propernames')}")
    print(f"     Tip: {obj.get('raw_tip')} | Ub: {obj.get('raw_ubertip')} | HK: {obj.get('hotkey')}")
    print(f"     Abils: {obj.get('abils')} | HeroAbils: {obj.get('heroabils')} | Targs1: {obj.get('targs1')}")

print("\n=== RESEARCHES ===")
for rid, obj in data['researches'].items():
    lvls = obj.get('levels', 1)
    print(f"[{rid}] Levels: {lvls} | Class: {obj.get('class')} | Applies: {obj.get('applies_to')}")
    for i in range(1, lvls + 1):
        n = obj.get('names', {}).get(f'name{i}', {})
        t = obj.get('tips', {}).get(f'tip{i}', {})
        u = obj.get('ubertips', {}).get(f'ubertip{i}', {})
        hk = obj.get('hotkeys', {}).get(f'hotkey{i}', {})
        print(f"   L{i}: name={n.get('raw')} ({n.get('val')}) | tip={t.get('raw')} | ub={u.get('raw')} | hk={hk.get('val')}")

print("\n=== ABILITIES (Sample) ===")
for aid, obj in data['abilities'].items():
    lvls = obj.get('levels', 1)
    n = obj.get('name')
    raw_n = obj.get('raw_name')
    print(f"[{aid}] ({raw_n} -> {n}) lvls={lvls} hk={obj.get('hotkey')} res_hk={obj.get('researchhotkey')}")
    for i in range(1, min(lvls + 1, 3)):
        t = obj.get('tips', {}).get(f'tip{i}', {})
        u = obj.get('ubertips', {}).get(f'ubertip{i}', {})
        print(f"   L{i}: tip={t.get('raw')} | ub={u.get('raw')}")
    if obj.get('raw_researchtip') or obj.get('raw_researchubertip'):
        print(f"   Res: tip={obj.get('raw_researchtip')} | ub={obj.get('raw_researchubertip')}")
