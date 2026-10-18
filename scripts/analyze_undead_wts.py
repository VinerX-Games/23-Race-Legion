# -*- coding: utf-8 -*-
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "scripts/undead_overrides.json").read_text(encoding="utf-8"))

wts_map = {} # sid -> list of (object_id, field)
non_wts = [] # list of (object_id, field, value)

for item in data:
    oid = item['id']
    otype = item['type']
    for field, val_info in item['overrides_text'].items():
        raw = val_info['raw']
        resolved = val_info['resolved']
        if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
            try:
                sid = int(raw[8:])
                wts_map.setdefault(sid, []).append((oid, otype, field, resolved))
            except ValueError:
                non_wts.append((oid, otype, field, raw))
        else:
            non_wts.append((oid, otype, field, raw))

print(f"Total unique WTS string IDs used: {len(wts_map)}")
print(f"Total non-WTS overridden fields: {len(non_wts)}")
if non_wts:
    print("Non-WTS fields:")
    for x in non_wts:
        print(f"  {x}")

shared = {sid: uses for sid, uses in wts_map.items() if len(uses) > 1}
print(f"\nShared WTS strings within Undead: {len(shared)}")
for sid, uses in shared.items():
    print(f"  STRING {sid}: {uses}")

out_path = ROOT / "scripts/undead_wts_mapping.json"
out_path.write_text(json.dumps({
    'wts_map': {str(k): v for k, v in sorted(wts_map.items())},
    'non_wts': non_wts,
    'shared': {str(k): v for k, v in shared.items()}
}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved mapping to {out_path}")
