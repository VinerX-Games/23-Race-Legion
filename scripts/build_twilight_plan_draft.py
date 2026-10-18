# -*- coding: utf-8 -*-
"""Draft helper to verify all object field to WTS string ID mappings for Twilight Hammer."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/twilight_hammer_raw_dump.json").read_text(encoding="utf-8"))

def get_str_id(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            return int(val[8:])
        except ValueError:
            return None
    return None

print("=== CHECKING BUILDINGS MAPPINGS ===")
for b in dump['buildings']:
    bid = b['id']
    f = b['fields']
    print(f"Building {bid} ({b['name']}):")
    for k in ['name', 'tip', 'ubertip']:
        sid = get_str_id(f.get(k))
        print(f"  {k}: sid={sid} (raw={f.get(k)})")

print("\n=== CHECKING HEROES MAPPINGS ===")
for h in dump['heroes']:
    hid = h['id']
    f = h['fields']
    print(f"Hero {hid} ({h['name']}):")
    for k in ['name', 'propernames', 'tip', 'ubertip', 'revivetip', 'awakentip']:
        sid = get_str_id(f.get(k))
        print(f"  {k}: sid={sid} (raw={f.get(k)})")

print("\n=== CHECKING UNITS MAPPINGS ===")
for u in dump['units']:
    uid = u['id']
    f = u['fields']
    print(f"Unit {uid} ({u['name']}):")
    for k in ['name', 'tip', 'ubertip']:
        sid = get_str_id(f.get(k))
        print(f"  {k}: sid={sid} (raw={f.get(k)})")

print("\n=== CHECKING UPGRADES MAPPINGS ===")
for up in dump['upgrades']:
    upid = up['id']
    f = up['fields']
    lvls = up['levels']
    print(f"Upgrade {upid} (levels: {lvls}):")
    for i in range(1, lvls + 1):
        for k in [f'name{i}', f'tip{i}', f'ubertip{i}']:
            sid = get_str_id(f.get(k) or (f.get(k[:-1]) if i == 1 else None))
            print(f"  {k}: sid={sid}")

print("\n=== CHECKING ABILITIES MAPPINGS ===")
for ab in dump['abilities']:
    aid = ab['id']
    f = ab['fields']
    lvls = ab['levels']
    print(f"Ability {aid} (levels: {lvls}):")
    for k in ['name', 'researchtip', 'researchubertip']:
        sid = get_str_id(f.get(k))
        if sid:
            print(f"  {k}: sid={sid}")
    for i in range(1, lvls + 1):
        for k in [f'tip{i}', f'ubertip{i}', f'untip{i}', f'unubertip{i}']:
            sid = get_str_id(f.get(k) or (f.get(k[:-1]) if i == 1 else None))
            if sid:
                print(f"  {k}: sid={sid}")

print("\n=== CHECKING BUFFS MAPPINGS ===")
for bu in dump['buffs']:
    bid = bu['id']
    f = bu['fields']
    print(f"Buff {bid} ({bu['name']}):")
    for k in ['buffname', 'name', 'bufftip', 'tip', 'buffubertip', 'ubertip']:
        sid = get_str_id(f.get(k))
        if sid:
            print(f"  {k}: sid={sid}")
