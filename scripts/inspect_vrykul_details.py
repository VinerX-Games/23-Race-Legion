# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
def res(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            return wts.get(int(val[8:]), val)
        except:
            return val
    return val

def main():
    print("=== INSPECT VRYCULS & RANDOM ===")
    
    # 1. Selection Spells
    for sid in ['A0HP', 'A12Q']:
        obj = hw.get_object_data(sid, 'abilities')
        print(f"\nSelection {sid}:")
        if obj:
            for k in ['name', 'tip1', 'ubertip1', 'hotkey', 'buttonpos_1', 'buttonpos_2']:
                print(f"  {k}: {obj.get(k)} -> {res(obj.get(k))}")
                
    # 2. Buildings
    blds = ['h0BQ', 'h0BR', 'h0BS', 'h0BT', 'h0BU', 'h0BV', 'h0BW', 'h0BX', 'wk01']
    print("\n=== BUILDINGS ===")
    all_trains = set()
    all_researches = set()
    for bid in blds:
        obj = hw.get_object_data(bid, 'units')
        if not obj:
            print(f"Building {bid} NOT FOUND")
            continue
        print(f"\nBuilding {bid}:")
        for k in ['name', 'tip', 'ubertip', 'hotkey', 'trains', 'researches', 'upgrades_to', 'builds', 'abilList']:
            v = obj.get(k)
            print(f"  {k}: {v} -> {res(v)}")
        if obj.get('trains'):
            for t in str(obj.get('trains')).split(','):
                t = t.strip()
                if t: all_trains.add(t)
        if obj.get('researches'):
            for r in str(obj.get('researches')).split(','):
                r = r.strip()
                if r: all_researches.add(r)
                
    print(f"\nAll trained units: {sorted(all_trains)}")
    print(f"All researches: {sorted(all_researches)}")
    
    # Let's inspect Worker h0C9
    w_obj = hw.get_object_data('h0C9', 'units')
    if w_obj:
        print(f"\nWorker h0C9:")
        for k in ['name', 'tip', 'ubertip', 'hotkey', 'builds', 'abilList']:
            print(f"  {k}: {w_obj.get(k)} -> {res(w_obj.get(k))}")
            
    # Inspect all units
    units = list(all_trains) + ['H0C4', 'h0AE', 'wk00', 'wk02', 'h0A8', 'h0A7']
    units = sorted(list(set(units)))
    print("\n=== UNITS & HEROES ===")
    all_unit_abils = set()
    for uid in units:
        obj = hw.get_object_data(uid, 'units')
        if not obj:
            print(f"Unit {uid} NOT FOUND")
            continue
        is_hero = obj.get('hero', False) or uid.startswith('H') or uid.startswith('U') or uid.startswith('E') or uid.startswith('O')
        print(f"\nUnit/Hero {uid} (is_hero={is_hero}):")
        keys = ['name', 'tip', 'ubertip', 'hotkey', 'propernames', 'awakentip', 'revivetip', 'abilList', 'heroAbilList', 'targs1', 'targs2', 'weapType1', 'weapType2']
        for k in keys:
            if k in obj:
                print(f"  {k}: {obj.get(k)} -> {res(obj.get(k))}")
        for abk in ['abilList', 'heroAbilList']:
            if obj.get(abk):
                for a in str(obj.get(abk)).split(','):
                    a = a.strip()
                    if a: all_unit_abils.add(a)
                    
    print(f"\nAll abilities found: {sorted(all_unit_abils)}")

if __name__ == '__main__':
    main()
