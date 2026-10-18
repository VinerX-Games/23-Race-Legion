# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

unit_ids = [
    'e02Y', 'u026', 'n025', 'n026', 'n02D', 'n02E',
    'n023', 'n027', 'n02I', 'n020', 'n028', 'n024',
    'n022', 'n021', 'n029'
]

bld_wts = []
unit_field_info = {}

for uid in unit_ids:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    name_raw = f.get('name')
    tip_raw = f.get('tip')
    ubertip_raw = f.get('ubertip')
    hotkey_raw = f.get('hotkey')
    
    unit_field_info[uid] = {
        'name_raw': name_raw,
        'name': resolve(name_raw),
        'tip_raw': tip_raw,
        'tip': resolve(tip_raw),
        'ubertip_raw': ubertip_raw,
        'ubertip': resolve(ubertip_raw),
        'hotkey_raw': hotkey_raw,
        'hotkey': resolve(hotkey_raw),
    }
    
    for raw in [name_raw, tip_raw, ubertip_raw]:
        if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
            sid = int(raw[8:])
            bld_wts.append(sid)

print(f"Total WTS keys across 15 units: {len(bld_wts)} (unique: {len(set(bld_wts))})")

# Check binary file usages
bin_files = [
    ROOT / "map.w3x/war3map.w3u",
    ROOT / "map.w3x/war3mapSkin.w3u",
    ROOT / "map.w3x/war3map.w3a",
    ROOT / "map.w3x/war3mapSkin.w3a",
    ROOT / "map.w3x/war3map.w3q",
    ROOT / "map.w3x/war3mapSkin.w3q",
    ROOT / "map.w3x/war3map.w3h",
    ROOT / "map.w3x/war3mapSkin.w3h",
    ROOT / "map.w3x/war3map.w3t",
    ROOT / "map.w3x/war3mapSkin.w3t",
]

found_counts = {k: 0 for k in set(bld_wts)}
for bf in bin_files:
    if not bf.exists(): continue
    raw = bf.read_bytes()
    for sid in found_counts.keys():
        target = f"TRIGSTR_{sid}".encode('utf-8')
        count = raw.count(target)
        if count > 0:
            found_counts[sid] += count

print("Usage counts for each WTS string across binary files:")
for sid, cnt in sorted(found_counts.items()):
    if cnt != 1:
        print(f"  SHARED WARNING: TRIGSTR_{sid}: {cnt} usages")
    else:
        print(f"  TRIGSTR_{sid}: 1 usage (OK)")

for uid, info in unit_field_info.items():
    print(f"\n{uid}:")
    print(f"  name: {info['name_raw']} -> {info['name']}")
    print(f"  tip: {info['tip_raw']} -> {info['tip']}")
    print(f"  ubertip: {info['ubertip_raw']}")
    print(f"  hotkey: {info['hotkey_raw']} -> {info['hotkey']}")
