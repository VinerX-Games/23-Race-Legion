# -*- coding: utf-8 -*-
"""Check WTS sharing for Elements hero ability text fields."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_project import read

hero_abils = [
    # H0EZ
    'A1MR', 'A0P4', 'A0P2', 'AEtq',
    # H0F0
    'A0P9', 'A0PA', 'A1LE', 'AHpx',
    # N037
    'ANic', 'AHfs', 'ANlm', 'A0P7',
    # E029
    'A0OU', 'A0OT', 'A0QL', 'A0OR', 'A0YH',
    # E027
    'A0P0', 'A0OX', 'A0OW', 'A0P1', 'A0YI',
    # E028
    'A0OP', 'A0ON', 'A0QJ', 'A0OQ', 'A0YG'
]

raw_data = json.load((ROOT / "docs/ui_text/elements_hero_abils_raw.json").open(encoding="utf-8"))

target_fields = ['name', 'researchtip', 'researchubertip'] + [f'tip{i}' for i in range(1, 5)] + [f'ubertip{i}' for i in range(1, 5)]

hero_wts_map = {} # wts_id -> list of (aid, field)
for aid in hero_abils:
    fields = raw_data.get(aid, {})
    levels = int(fields.get('levels', {}).get('text', '1') or '1')
    active_fields = ['name']
    if 'researchtip' in fields or 'researchubertip' in fields:
        active_fields.extend(['researchtip', 'researchubertip'])
    for i in range(1, levels + 1):
        active_fields.extend([f'tip{i}', f'ubertip{i}'])
    for f in active_fields:
        v = fields.get(f)
        if isinstance(v, dict):
            wts_id = v.get('wts_id')
            raw = v.get('raw', '')
            hero_wts_map[(aid, f)] = {'wts_id': wts_id, 'raw': raw, 'text': v.get('text', '')}

print(f"Total active text fields across 27 hero abilities: {len(hero_wts_map)}")

# Now scan all binary files to see where these WTS strings appear
all_wts_ids = {info['wts_id'] for info in hero_wts_map.values() if info['wts_id'] is not None}
print(f"Unique WTS IDs: {len(all_wts_ids)}")

# Check references in all w3* files
shared_ids = {}
for ext in ['w3u', 'w3t', 'w3a', 'w3q', 'w3h', 'w3b', 'w3d']:
    for prefix in ['war3map', 'war3mapSkin']:
        fn = f"{prefix}.{ext}"
        p = ROOT / "map.w3x" / fn
        if not p.exists(): continue
        # Use regex to find TRIGSTR_XXXX
        content = p.read_bytes()
        # Find all TRIGSTR_
        import re
        matches = set(re.findall(rb"TRIGSTR_(\d+)", content))
        for m in matches:
            wid = int(m.decode("ascii"))
            if wid in all_wts_ids:
                shared_ids.setdefault(wid, set()).add(fn)

# Report
shared_count = 0
for (aid, f), info in sorted(hero_wts_map.items()):
    wid = info['wts_id']
    if wid is None:
        print(f"INLINE (no WTS): [{aid}] {f} = {repr(info['raw'][:50])}")
    else:
        files = shared_ids.get(wid, set())
        if len(files) > 2 or any('w3u' in x or 'w3q' in x or 'w3t' in x or 'w3h' in x for x in files):
            print(f"SHARED WTS_{wid}: [{aid}] {f} used in {files}")
            shared_count += 1

print(f"Total potentially shared WTS entries: {shared_count}")
