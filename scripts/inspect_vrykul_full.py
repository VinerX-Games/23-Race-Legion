# -*- coding: utf-8 -*-
"""Inspect all Vryculs & Random objects with full Warcraft III base data."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(raw):
    if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
        try:
            sid = int(raw[8:])
            return sid, wts.get(sid, raw)
        except:
            return None, raw
    return None, raw

def get_obj_fields(oid, otype):
    args = ["get-object", "--map", str(hw.DEFAULT_MAP), "--type", otype, "--id", oid]
    if hw.DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(hw.DEFAULT_WARCRAFT)])
    data = hw.run_cli_json(args)
    if not data.get("ok"):
        return {}
    f = data.get("fields", {}) or data.get("object", {})
    overrides = data.get("overrides", {})
    # merge: overrides take precedence, but if field exists in f and not in overrides, take f
    combined = dict(f)
    combined.update(overrides)
    return combined

def main():
    # 1. Selection
    print("=== 1. SELECTION ===")
    for sid, stype in [('A0HP', 'ability'), ('A12Q', 'ability')]:
        f = get_obj_fields(sid, stype)
        print(f"\nSelection {sid}:")
        for k in ['name', 'tip', 'tip1', 'ubertip', 'ubertip1', 'hotkey', 'buttonpos']:
            if k in f:
                sid_num, text = res(f[k])
                print(f"  {k}: [{sid_num}] {text}")

    # 2. Markers
    print("\n=== 2. MARKERS ===")
    for mid in ['R07F', 'R067', 'R068']:
        f = get_obj_fields(mid, 'upgrade')
        print(f"\nMarker {mid}:")
        for k in ['name', 'name1', 'tip', 'tip1', 'ubertip', 'ubertip1', 'hotkey1']:
            if k in f:
                sid_num, text = res(f[k])
                print(f"  {k}: [{sid_num}] {text}")

    # 3. Buildings
    print("\n=== 3. BUILDINGS ===")
    blds = ['h0BQ', 'h0BR', 'h0BS', 'h0BT', 'h0BU', 'h0BV', 'h0BW', 'h0BX', 'wk01']
    for bid in blds:
        f = get_obj_fields(bid, 'unit')
        print(f"\nBuilding {bid}:")
        for k in ['name', 'tip', 'ubertip', 'hotkey', 'train', 'trains', 'researches', 'upgrades_to', 'upgrade', 'builds', 'abillist']:
            if k in f:
                sid_num, text = res(f[k])
                val_str = f"[{sid_num}] {text}" if sid_num is not None else str(f[k])
                print(f"  {k}: {val_str}")

    # 4. Heroes
    print("\n=== 4. HEROES ===")
    heroes = ['H0C4', 'H0C5', 'H0C6', 'H0C7']
    for hid in heroes:
        f = get_obj_fields(hid, 'unit')
        print(f"\nHero {hid}:")
        for k in ['name', 'propernames', 'tip', 'ubertip', 'awakentip', 'revivetip', 'hotkey', 'heroabillist', 'abillist', 'targs1', 'targs2', 'weaptype1']:
            if k in f:
                sid_num, text = res(f[k])
                val_str = f"[{sid_num}] {text}" if sid_num is not None else str(f[k])
                print(f"  {k}: {val_str}")

    # 5. Units
    print("\n=== 5. UNITS ===")
    units = ['h0C9', 'h0AA', 'h0AD', 'h0A5', 'h0A6', 'h0BP', 'h0A9', 'h0AC', 'h0AE', 'wk08', 'wk02', 'wk00', 'h0A8', 'h0A7']
    for uid in units:
        f = get_obj_fields(uid, 'unit')
        print(f"\nUnit {uid}:")
        for k in ['name', 'tip', 'ubertip', 'hotkey', 'abillist', 'upgrades', 'targs1', 'weaptype1']:
            if k in f:
                sid_num, text = res(f[k])
                val_str = f"[{sid_num}] {text}" if sid_num is not None else str(f[k])
                print(f"  {k}: {val_str}")

if __name__ == '__main__':
    main()
