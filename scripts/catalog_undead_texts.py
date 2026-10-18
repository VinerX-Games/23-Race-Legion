# -*- coding: utf-8 -*-
"""Detailed catalog of Undead UI texts to standardize."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def get_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

data = json.load(open('scripts/undead_overrides.json', encoding='utf-8'))

# Map oid -> item
by_id = {item['id']: item for item in data}

def dump_obj(oid, title):
    item = by_id.get(oid)
    if not item:
        print(f"[{oid}] NOT FOUND")
        return
    print(f"\n=== {title} [{oid}] ===")
    ov = item['all_overrides']
    for k, v in sorted(ov.items()):
        if any(tk in k.lower() for tk in ['name', 'tip', 'ubertip', 'propernames', 'hotkey']):
            sid = get_sid(v)
            val = wts.get(sid, v) if sid else v
            print(f"  {k}: {v} (SID={sid}) -> {val!r}")

print("--- 1. SELECTION ---")
dump_obj('A0HV', 'Race Selection')

print("\n--- 2. BUILDINGS ---")
bld_list = ['n014', 'u00F', 'u00G', 'u00H', 'u00I', 'u00J', 'u00K', 'u00L', 'u00M', 'u00N', 'n012', 'u03B', 'u017']
for b in bld_list:
    dump_obj(b, 'Building')

print("\n--- 3. HEROES ---")
hero_list = ['U00O', 'U00V', 'U00U', 'U030', 'U014', 'CM00', 'FL00']
for h in hero_list:
    dump_obj(h, 'Hero')

print("\n--- 4. UNITS ---")
unit_list = ['u00P', 'n011', 'n013', 'u03E', 'u02B', 'u00A', 'u00B', 'u00D', 'u00C', 'u008', 'u00E', 'u034', 'ft00', 'ft01', 'n07H', 'u03D', 'n016', 'n017']
for u in unit_list:
    dump_obj(u, 'Unit')

print("\n--- 5. RESEARCHES ---")
res_list = ['R0DQ', 'R05I', 'R05J', 'R05N', 'R05O', 'R05P', 'R05Q', 'R05L', 'R05H', 'R05E', 'R05F', 'R05G', 'R05A', 'R05R', 'R05D', 'R05C', 'R07I', 'R0J5']
for r in res_list:
    dump_obj(r, 'Research')

print("\n--- 6. HERO ABILITIES ---")
hero_abils = ['A0CO', 'A0CP', 'A0CR', 'A0CN', 'AQ95', 'UN99', 'A0CS', 'AQ11', 'A0CK', 'A0CM', 'A0BW', 'A1Q7', 'A1LI', 'A1LJ', 'A1LL', 'A1LM', 'A1LK', 'A0WD', 'A0CX', 'A0WE', 'A0CZ', 'A0WB', 'A0WC', 'A0WF', 'CM01', 'CM02', 'CM04', 'CM05', 'FL01', 'FL02', 'FL03', 'FL04']
for ha in hero_abils:
    dump_obj(ha, 'Hero Ability')

print("\n--- 7. UNIT ABILITIES ---")
unit_abils = ['A0BO', 'A0BP', 'A0C5', 'Sch2', 'Amel', 'Amed', 'A0C7', 'A0C8', 'A0BT', 'A0BU', 'A1PV', 'A0C4', 'Arpl', 'Arpm', 'A0BX', 'unA5', 'A1PY', 'A0C0', 'A0C2', 'A1PX', 'unA0', 'Aspa', 'A1N8', 'Arst', 'Auns', 'Afra', 'A0BR', 'Agyd', 'Arlm', 'A15N', 'A0CA', 'A0CC', 'A1ND', 'A0CG', 'kel0', 'A1E7']
for ua in unit_abils:
    dump_obj(ua, 'Unit Ability')
