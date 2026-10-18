# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from implement_draenei_rework import object_records

for name, path in [("war3map.w3u", ROOT / "map.w3x/war3map.w3u"), ("war3mapSkin.w3u", ROOT / "map.w3x/war3mapSkin.w3u")]:
    ver, tables = object_records(path.read_bytes(), extended=False)
    print(f"=== {name} ===")
    for table_idx, table in enumerate(tables):
        for rec in table:
            if rec["id"] == "h06Z":
                print(f"  Table {table_idx} ({'orig' if table_idx==0 else 'custom'}): base={rec.get('base')}")
                for m in rec["modifications"]:
                    print(f"    mod: id={m['id']}, val={repr(m['value'])}")
