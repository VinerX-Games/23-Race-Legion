# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def check_obj(otype, oid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    ov = res.get('overrides', {})
    get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
    name = resolve(get_v('name') or get_v('bufftip'))
    tip = resolve(get_v('tip') or get_v('tip1'))
    return {
        'id': oid,
        'name': name,
        'raw_name': get_v('name'),
        'tip': tip,
        'trains': get_v('trains') or get_v('train'),
        'researches': get_v('researches') or get_v('res'),
        'upgrades_to': get_v('upgrade') or get_v('upg') or get_v('upgrades_to'),
        'builds': get_v('builds'),
        'abillist': get_v('abillist'),
        'heroabillist': get_v('heroabillist'),
        'propernames': resolve(get_v('propernames')),
        'hotkey': get_v('hotkey'),
    }

units_to_check = [
    # Worker & Buildings
    'e01G', 'e00B', 'e01H', 'e01I', 'e01J', 'e01K', 'e01L', 'e01X', 'e020', 'e021', 'h00C', 'h0DL', 'o015', 'o017',
    'e01M', 'h08L', 'h0MG',
    # Heroes
    'U023', 'U024', 'U025', 'U02A', 'U02R', 'U02S', 'U037', 'U038',
    # Units
    'e01N', 'e01O', 'e01P', 'e01Q', 'e01R', 'e01S', 'e01T', 'e01U', 'e01V', 'e01Y', 'e01Z', 'e023', 'e02W', 'u020', 'u022'
]

print("--- UNITS & BUILDINGS & HEROES ---")
for u in units_to_check:
    info = check_obj('unit', u)
    print(f"[{u}] {info['name']} | trains={info['trains']} | res={info['researches']} | upg={info['upgrades_to']} | builds={info['builds']}")
    print(f"     abils={info['abillist']} | heroabils={info['heroabillist']}")
