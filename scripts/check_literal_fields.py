# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

d = json.loads((ROOT / "scripts/undead_raw_dump.json").read_text(encoding="utf-8"))

print("=== CHECKING STRING SOURCES ===")
for category in ['selection', 'buildings', 'units', 'heroes', 'researches', 'abilities']:
    print(f"\n--- {category.upper()} ---")
    items = d[category]
    for oid, obj in items.items():
        if not obj or 'error' in obj: continue
        fields = obj.get('fields', {})
        for k, v in fields.items():
            if any(text_k in k.lower() for text_k in ['name', 'tip', 'ubertip', 'propernames', 'hotkey']):
                if isinstance(v, str):
                    if v.startswith('TRIGSTR_'):
                        sid = int(v[8:])
                        # print if interesting
                    else:
                        print(f"[{oid}] Non-TRIGSTR field: {k} = {v!r}")
