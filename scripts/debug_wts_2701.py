# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from implement_draenei_rework import object_records

for name in ["war3map.w3q", "war3mapSkin.w3q"]:
    p = ROOT / f"map.w3x/{name}"
    ver, tables = object_records(p.read_bytes(), extended=True)
    for table_idx, table in enumerate(tables):
        for rec in table:
            for k, raw in rec["mods"]:
                if b"TRIGSTR_2701" in raw:
                    print(f"{name} table {table_idx} rec={rec['id']} key={k}")
