# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wc3_object_tools import cli, require

research_ids = [
    'R0D4',
    'R04P', 'R04E', 'R04F', 'R04G', 'R04H', 'R04I', 'R04J', 'R04K', 'R04L', 'R04M',
    'R056', 'R07A', 'R05X', 'R05Y', 'R04N', 'R04Q', 'R04R', 'R053', 'R05W'
]

bulk = require(cli(['get-objects-bulk', '--type', 'upgrade', '--ids', ','.join(research_ids)]))
objects = {o['id']: o['fields'] for o in bulk.get('objects', [])}

from audit_goblin_research_wts import shared_with_other

res_fields_map = {}
for rid in research_ids:
    f = objects.get(rid, {})
    res_fields_map[rid] = {}
    for k, v in f.items():
        if any(k.startswith(p) for p in ['name', 'tip', 'ubertip']):
            wts_id = int(v[8:]) if isinstance(v, str) and v.startswith("TRIGSTR_") else None
            is_shared = (wts_id in shared_with_other) if wts_id is not None else True
            res_fields_map[rid][k] = {
                "raw": v,
                "wts_id": wts_id,
                "is_shared": is_shared
            }

Path(ROOT / "docs/ui_text/goblins_research_fields_map.json").write_text(
    json.dumps(res_fields_map, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"Saved research fields map to docs/ui_text/goblins_research_fields_map.json")
