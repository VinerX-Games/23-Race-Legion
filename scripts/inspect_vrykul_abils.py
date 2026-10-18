# -*- coding: utf-8 -*-
"""Inspect all Vrycul abilities with HiveWE game data."""
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
    combined = dict(f)
    combined.update(overrides)
    return combined

def main():
    abils = [
        'A0E3', 'A0E4', 'A0E5', 'A0E7', 'A0E8', 'A0E9', 'A0EA', 'A0EB',
        'A0ED', 'A0EE', 'A0EI', 'A0EM', 'A0EN', 'A0EO', 'A0EP', 'A0EQ',
        'A0ER', 'A0ES', 'A0ET', 'A0EU', 'A0EV', 'A0EW', 'A0EX', 'A0EY',
        'A0EZ', 'A0F1', 'A0HP', 'A0YQ', 'A0Z1', 'wk03', 'wk04', 'wk05',
        'wk06', 'wk07', 'wk09', 'wk10'
    ]
    
    print("=== VRYCUL ABILITIES ===")
    for aid in abils:
        f = get_obj_fields(aid, 'ability')
        print(f"\nAbility {aid}:")
        for k in sorted(f.keys()):
            if any(k.startswith(p) for p in ['name', 'tip', 'ubertip', 'research', 'hotkey', 'levels', 'buff']):
                sid_num, text = res(f[k])
                val_str = f"[{sid_num}] {text}" if sid_num is not None else str(f[k])
                print(f"  {k}: {val_str}")

if __name__ == '__main__':
    main()
