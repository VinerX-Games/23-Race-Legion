# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gilneas_raw_dump.json"
d = json.loads(dump_file.read_text(encoding='utf-8'))

def parse_sid(raw):
    if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

def check_obj(category, obj):
    out = []
    oid = obj.get('id')
    # Check top-level raw fields
    for k, v in obj.items():
        if k.startswith('raw_') and v:
            sid = parse_sid(v)
            if sid is not None:
                out.append((sid, category, oid, k[4:], obj.get(k[4:])))
    # For abilities: check tips and ubertips
    for lvl_k, tip_dict in obj.get('tips', {}).items():
        sid = parse_sid(tip_dict.get('raw'))
        if sid is not None:
            out.append((sid, category, oid, lvl_k, tip_dict.get('val')))
    for lvl_k, ub_dict in obj.get('ubertips', {}).items():
        sid = parse_sid(ub_dict.get('raw'))
        if sid is not None:
            out.append((sid, category, oid, lvl_k, ub_dict.get('val')))
    # For upgrades: check names, tips, ubertips
    for lvl_k, ndict in obj.get('names', {}).items():
        sid = parse_sid(ndict.get('raw'))
        if sid is not None:
            out.append((sid, category, oid, lvl_k, ndict.get('val')))
    return out

all_entries = []
all_entries.extend(check_obj('selection', d['selection']))
for m in d['selection_markers']:
    all_entries.extend(check_obj('selection_marker', m))
for b in d['buildings']:
    all_entries.extend(check_obj('building', b))
all_entries.extend(check_obj('worker', d['worker']))
for u in d['units']:
    all_entries.extend(check_obj('unit', u))
for h in d['heroes']:
    all_entries.extend(check_obj('hero', h))
for up in d['upgrades']:
    all_entries.extend(check_obj('upgrade', up))
for ab in d['abilities']:
    all_entries.extend(check_obj('ability', ab))
for bf in d['buffs']:
    all_entries.extend(check_obj('buff', bf))

print(f"Total WTS entries found: {len(all_entries)}")
# Check for unique SIDs
by_sid = {}
for sid, cat, oid, field, val in all_entries:
    if sid not in by_sid:
        by_sid[sid] = []
    by_sid[sid].append((cat, oid, field, val))

print(f"Unique WTS string IDs: {len(by_sid)}")
for sid in sorted(by_sid.keys()):
    usages = by_sid[sid]
    u_str = ", ".join(f"{c}:{oid}.{f}" for c, oid, f, _ in usages)
    sample_val = repr(usages[0][3])[:70]
    print(f"STRING {sid:5d} -> {u_str} | {sample_val}")
