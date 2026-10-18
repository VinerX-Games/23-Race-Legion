# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def search_by_suffix(otype):
    res = hw.run_cli_json(['list-objects', '--map', str(hw.DEFAULT_MAP), '--type', otype])
    objs = res.get('objects', [])
    matched = []
    for oid in objs:
        ores = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid])
        f = ores.get('fields', {}) or ores.get('object', {})
        ov = ores.get('overrides', {})
        get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
        ed = resolve(get_v('editorsuffix') or get_v('editorname') or '')
        name = resolve(get_v('name') or get_v('bufftip') or '')
        txt = (str(ed) + " " + str(name)).lower()
        if any(w in txt for w in ['силитид', 'кираж', 'аз’акир', "аз'акир", 'анкираж', 'к\'тун', 'ктун', 'улей', 'личинк']):
            matched.append((oid, name, ed))
    return matched

print("Searching units...")
units = search_by_suffix('unit')
print(f"Found {len(units)} units:")
for u in units:
    print(f"  {u[0]}: {u[1]} ({u[2]})")

print("\nSearching abilities...")
abils = search_by_suffix('ability')
print(f"Found {len(abils)} abilities:")
for a in abils:
    print(f"  {a[0]}: {a[1]} ({a[2]})")

print("\nSearching upgrades...")
upgs = search_by_suffix('upgrade')
print(f"Found {len(upgs)} upgrades:")
for up in upgs:
    print(f"  {up[0]}: {up[1]} ({up[2]})")

print("\nSearching buffs...")
buffs = search_by_suffix('buff')
print(f"Found {len(buffs)} buffs:")
for b in buffs:
    print(f"  {b[0]}: {b[1]} ({b[2]})")
