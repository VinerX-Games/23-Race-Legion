# -*- coding: utf-8 -*-
"""Catalog all WTS string IDs for Race 12: Scarlet Crusade.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from implement_draenei_rework import object_records

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
res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', 'A0HM'])
f = res.get('object', {}) or res.get('fields', {})
for k in ['name', 'tip1', 'ubertip1', 'hotkey']:
    v = f.get(k)
    if isinstance(v, str) and v.startswith('TRIGSTR_'):
        add_wts(int(v[8:]), "selection", "A0HM", k)

# 2. Buildings
buildings = ['h05U', 'h05V', 'h05W', 'h05X', 'h05Y', 'h05Z', 'h060', 'h061', 'h062', 'h063', 'h064', 'h068']
for bid in buildings:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', bid])
    f = res.get('object', {}) or res.get('fields', {})
    for k in ['name', 'tip', 'ubertip', 'hotkey']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "building", bid, k)

# 3. Heroes
heroes = ['H03H', 'H06C', 'H06B']
for hid in heroes:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid])
    f = res.get('object', {}) or res.get('fields', {})
    for k in ['name', 'propernames', 'tip', 'ubertip', 'hotkey']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "hero", hid, k)

# 4. Units
units = ['h014', 'h039', 'h03A', 'h03B', 'h03C', 'h03D', 'h03F', 'h03G', 'h03I', 'h065', 'h066', 'h067', 'n007', 'n008', 'o00I']
for uid in units:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    for k in ['name', 'tip', 'ubertip', 'hotkey']:
        v = f.get(k)
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            add_wts(int(v[8:]), "unit", uid, k)

# 5. Abilities (Hero & Unit)
hero_abils = ['A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J']
unit_abils = [
    'A07I', 'A07X', 'A07Y', 'A07Z', 'A080', 'A081', 'A082', 'A083', 'A084',
    'A085', 'A087', 'A088', 'A089', 'A08A', 'A08B', 'A08C', 'A08D', 'A08E',
    'A08F', 'A08G', 'A08J', 'A08K', 'A08L', 'A08M', 'A08N', 'A08O', 'A08P',
    'A08X', 'A08Y', 'A09O'
]
for aid in hero_abils + unit_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    cat = "hero_ability" if aid in hero_abils else "unit_ability"
    for k, v in f.items():
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            # Only consider text fields
            if any(k.startswith(p) for p in ['name', 'tip', 'ubertip', 'hotkey', 'untip', 'unubertip', 'unhotkey', 'researchtip', 'researchubertip', 'researchhotkey']):
                add_wts(int(v[8:]), cat, aid, k)

# 6. Buffs
w3h_skin_bytes = (ROOT / 'map.w3x/war3mapSkin.w3h').read_bytes()
header, tables = object_records(w3h_skin_bytes, False)
buff_ids = ['B01K', 'B01L', 'B01M', 'B01N', 'B01P', 'B01R', 'B01W', 'B01X', 'B01Y', 'B01Z', 'B020', 'B021', 'B022']
for table in tables:
    for obj in table:
        oid = obj['id']
        if oid in buff_ids:
            for mod_key, raw_bytes in obj['mods']:
                tag = mod_key[0]
                val_bytes = raw_bytes[8:]
                try:
                    val_str = val_bytes.split(b'\x00')[0].decode('utf-8', errors='ignore')
                    if val_str.startswith('TRIGSTR_'):
                        add_wts(int(val_str[8:]), "buff", oid, tag)
                except Exception:
                    pass

# 7. Upgrades
upgrades = [
    'R03K', 'R03L', 'R03M', 'R03S', 'R03T', 'R03U', 'R03V', 'R03W', 'R03X',
    'R03Y', 'R03Z', 'R040', 'R041', 'R042', 'R043', 'R044', 'R045', 'R046',
    'R047', 'R048', 'R049', 'R04A', 'R04B', 'R04C', 'R07B', 'R0KG', 'R0KH'
]
for upg in upgrades:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', upg])
    f = res.get('object', {}) or res.get('fields', {})
    for k, v in f.items():
        if isinstance(v, str) and v.startswith('TRIGSTR_'):
            if any(k.startswith(p) for p in ['name', 'tip', 'ubertip', 'hotkey']):
                add_wts(int(v[8:]), "upgrade", upg, k)

print(f"Total unique WTS strings discovered: {len(catalog)}")
out_file = ROOT / "scripts/scarlet_strings_catalog.json"
out_file.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Catalog saved to {out_file}")
