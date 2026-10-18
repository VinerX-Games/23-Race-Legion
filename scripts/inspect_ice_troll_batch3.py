# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw
from implement_draenei_rework import object_records

wts = hw.load_wts_strings()

def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

# 1. Building abilities
b1 = json.loads((ROOT / 'docs/ui_text/ice_troll_buildings_01.json').read_text(encoding='utf-8'))
b2 = json.loads((ROOT / 'docs/ui_text/ice_troll_buildings_02.json').read_text(encoding='utf-8'))

b_abils = set()
for item in b1.get('objects_before', {}).get('SD', []):
    abils = [a.strip() for a in item.get('fields', {}).get('abillist', '').split(',') if a.strip()]
    b_abils.update(abils)
    print(f"{item['id']} ({item.get('name', '')}): abillist={abils}")

for item in b2.get('objects_before', {}).get('SD', {}).get('buildings', []):
    abils = [a.strip() for a in item.get('fields', {}).get('abillist', '').split(',') if a.strip()]
    b_abils.update(abils)
    print(f"{item['id']} ({item.get('name', '')}): abillist={abils}")

print("\nAll building abilities found in building cards:", sorted(b_abils))

# Also check candidate building / ritual abilities
candidates = sorted(b_abils | {'A1FR', 'A1FS', 'A15N', 'A1KB'})
print("\nCandidates to inspect:", candidates)

# 2. Inspect candidate abilities
abils_info = []
for aid in candidates:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    lvls = int(fields.get('levels', '1'))
    abils_info.append({
        'id': aid,
        'code': fields.get('code', aid),
        'name': res(fields.get('name', '')),
        'levels': lvls,
        'hotkey': res(fields.get('hotkey', '')),
        'tip1': res(fields.get('tip1', fields.get('tip', ''))),
        'ubertip1': res(fields.get('ubertip1', fields.get('ubertip', ''))),
        'fields': {k: res(v) for k, v in fields.items()}
    })
    print(f"Ability {aid} ({fields.get('code', '')}): name='{res(fields.get('name', ''))}', tip='{res(fields.get('tip1', fields.get('tip', '')))}'")

# 3. Inspect buffs referenced by Ice Troll abilities
# Load raw abilities from hero and unit batches
raw_hero = json.loads((ROOT / 'docs/ui_text/ice_troll_hero_abilities_raw.json').read_text(encoding='utf-8'))
raw_unit = json.loads((ROOT / 'docs/ui_text/ice_troll_unit_abilities_raw.json').read_text(encoding='utf-8'))

buff_ids = set()
for item in raw_hero + raw_unit + abils_info:
    f = item.get('fields', {})
    for k, v in f.items():
        if k.startswith('abuf') or k.startswith('buff'):
            for b in str(v).split(','):
                b = b.strip()
                if b and b != '-' and b != '0':
                    buff_ids.add(b)

print(f"\nBuff IDs referenced by abilities ({len(buff_ids)}): {sorted(buff_ids)}")

# Inspect buffs in map.w3h / war3mapSkin.w3h
buffs_info = []
for bid in sorted(buff_ids):
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', bid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    fields = data.get('fields', {})
    buffs_info.append({
        'id': bid,
        'code': fields.get('code', bid),
        'name': res(fields.get('name', fields.get('fnam', ''))),
        'bufftip': res(fields.get('bufftip', fields.get('ftip', ''))),
        'buffubertip': res(fields.get('buffubertip', fields.get('fube', ''))),
        'editorname': res(fields.get('editorname', '')),
        'fields': {k: res(v) for k, v in fields.items()}
    })
    print(f"Buff {bid}: name='{res(fields.get('name', ''))}', tip='{res(fields.get('bufftip', ''))}', ubertip='{res(fields.get('buffubertip', ''))}'")

out = {
    'building_abilities': abils_info,
    'buffs': buffs_info
}
(ROOT / 'docs/ui_text/ice_troll_batch3_raw.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("\nSaved to docs/ui_text/ice_troll_batch3_raw.json")
