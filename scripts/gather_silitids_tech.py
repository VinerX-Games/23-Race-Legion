# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def get_obj(otype, oid):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    ov = res.get('overrides', {})
    get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
    return get_v, f, ov

buildings = ['e00B', 'e01H', 'e01I', 'e01J', 'e01K', 'e01L', 'e01M', 'e01X', 'e020', 'e021', 'h00C', 'h0DL', 'o015', 'o017', 'h08L', 'h0MG']
heroes = ['U023', 'U024', 'U025', 'U02A', 'U02R', 'U02S']
units = ['e01G', 'e01N', 'e01O', 'e01P', 'e01Q', 'e01R', 'e01S', 'e01T', 'e01U', 'e01V', 'e01Y', 'e01Z', 'e023', 'e02W', 'u020', 'u022']

all_abils = set()
all_upgs = set()

for uid in buildings + heroes + units:
    get_v, _, _ = get_obj('unit', uid)
    abils = (get_v('abillist') or '').split(',') + (get_v('heroabillist') or '').split(',')
    res = (get_v('researches') or '').split(',')
    upg = (get_v('upgrades') or '').split(',')
    for a in abils:
        a = a.strip()
        if a and len(a) == 4:
            all_abils.add(a)
    for r in res:
        r = r.strip()
        if r and len(r) == 4:
            all_upgs.add(r)
    for u in upg:
        u = u.strip()
        if u and len(u) == 4:
            all_upgs.add(u)

# Add selection ability and marker
all_abils.add('A0J7')
all_upgs.add('R0BV')

print(f"Total collected abilities: {len(all_abils)}")
print(f"Total collected upgrades: {len(all_upgs)}")

print("\n--- UPGRADES ---")
for uid in sorted(all_upgs):
    get_v, _, _ = get_obj('upgrade', uid)
    name = resolve(get_v('name1') or get_v('name'))
    ed = resolve(get_v('editorsuffix'))
    print(f"[{uid}] {name} (ed: {ed})")

print("\n--- ABILITIES ---")
for aid in sorted(all_abils):
    get_v, _, _ = get_obj('ability', aid)
    name = resolve(get_v('name'))
    tip = resolve(get_v('tip1') or get_v('researchtip'))
    ed = resolve(get_v('editorsuffix'))
    print(f"[{aid}] {name} (ed: {ed}) | tip: {tip}")
