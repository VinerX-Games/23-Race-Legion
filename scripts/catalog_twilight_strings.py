# -*- coding: utf-8 -*-
"""Catalog all WTS string IDs for Race 20: Культ Сумеречного Молота (Twilight Hammer)."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
catalog = {}

def add_wts(sid, category, obj_id, field, note=""):
    if sid is None: return
    try:
        sid = int(sid)
    except (ValueError, TypeError):
        return
    if sid not in catalog:
        catalog[sid] = []
    catalog[sid].append({
        "category": category,
        "obj_id": obj_id,
        "field": field,
        "note": note,
        "current_val": wts.get(sid, "")
    })

# 1. Selection
res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', 'A0HX', '--all'])
f = res.get('fields', {})
for k in ['name', 'tip1', 'ubertip1', 'hotkey']:
    v = f.get(k)
    if isinstance(v, str) and v.startswith('TRIGSTR_'):
        add_wts(int(v[8:]), "selection", "A0HX", k)

for mid in ['R07K', 'R0KD']:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', mid, '--all'])
    f = res.get('fields', {})
    for k in ['name1', 'tip1', 'ubertip1', 'hotkey1']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "selection_marker", mid, k)

# 2. Buildings
buildings = ['o00K', 'o00T', 'o00L', 'o00R', 'o00V', 'o00P', 'o00U', 'o00Q', 'h0D3']
for bid in buildings:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', bid, '--all'])
    f = res.get('fields', {})
    for k in ['name', 'tip', 'ubertip', 'hotkey']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "building", bid, k)

# 3. Heroes
heroes = ['O011', 'N010', 'N00Z']
for hid in heroes:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid, '--all'])
    f = res.get('fields', {})
    for k in ['name', 'propernames', 'tip', 'ubertip', 'hotkey', 'revivetip', 'awakentip']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "hero", hid, k)

# 4. Units
units = ['o00J', 'o00M', 'o00N', 'o00S', 'o002', 'u004', 'n00R', 'n00U', 'n00D', 'n00C', 'o00O', 'n00S', 'u005']
for uid in units:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--all'])
    f = res.get('fields', {})
    for k in ['name', 'tip', 'ubertip', 'hotkey']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "unit", uid, k)

# 5. Researches
upgrades = [
    'R04D', 'R04V', 'R00O', 'R04S', 'R04U', 'R0EJ', 'R05S', 'R05T', 'R05U', 'R05V',
    'R04Z', 'R050', 'R051', 'R052', 'R04W', 'R04X'
]
for uid in upgrades:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
    f = res.get('fields', {})
    levels = int(f.get('maxlevel') or f.get('levels') or 1)
    for i in range(1, levels + 1):
        for prefix in ['name', 'tip', 'ubertip', 'hotkey']:
            k = f'{prefix}{i}'
            v = f.get(k) or (f.get(prefix) if i == 1 else None)
            if isinstance(v, str) and v.startswith('TRIGSTR_'):
                add_wts(int(v[8:]), "research", uid, k, f"level {i}")

# 6. Hero & Unit Abilities
hero_abils = [
    'A0AO', 'A0AP', 'A0B6', 'A0B8',
    'A0B9', 'A0BA', 'A0BB', 'A0BC',
    'A0BD', 'A0BE', 'A0BF', 'A0B7'
]
unit_abils = [
    'A01Z', 'A09Q', 'A09R', 'A09S', 'A09T', 'A09U', 'A09V', 'A09W', 'A09X',
    'A0A0', 'A0A1', 'A0A2', 'A0AI', 'A0AJ', 'A0AK', 'A0AL', 'A0AM', 'A0AN', 'A1QQ', 'A09Z'
]
for aid in hero_abils + unit_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {})
    cat = "hero_ability" if aid in hero_abils else "unit_ability"
    levels = int(f.get('levels') or 1)
    for k in ['name', 'hotkey', 'researchhotkey', 'researchtip', 'researchubertip']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), cat, aid, k)
    for i in range(1, levels + 1):
        for prefix in ['tip', 'ubertip', 'untip', 'unubertip', 'unhotkey']:
            k = f'{prefix}{i}'
            v = f.get(k) or (f.get(prefix) if i == 1 else None)
            if isinstance(v, str) and v.startswith('TRIGSTR_'):
                add_wts(int(v[8:]), cat, aid, k, f"level {i}")

# 7. Buffs
buff_ids = ['B025', 'B026', 'B02C', 'B02D', 'B02K', 'B00A', 'B00B', 'B02B', 'B02G', 'B02E', 'B02L']
for bid in buff_ids:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid, '--all'])
    f = res.get('fields', {})
    for k in ['buffname', 'name', 'bufftip', 'tip', 'buffubertip', 'ubertip']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "buff", bid, k)

out_file = ROOT / "scripts/twilight_strings_catalog.json"
out_file.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total unique WTS string IDs cataloged: {len(catalog)}")
print(f"Catalog saved to {out_file}")
