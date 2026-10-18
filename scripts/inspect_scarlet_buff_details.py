# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from implement_draenei_rework import object_records
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return int(s[8:]), wts.get(int(s[8:]), '')
    return None, str(s)

w3h_bytes = (ROOT / 'map.w3x/war3mapSkin.w3h').read_bytes()
header, tables = object_records(w3h_bytes, False)
for table in tables:
    for obj in table:
        oid = obj['id']
        if oid in ['B01K', 'B01L', 'B01M', 'B01N', 'B01P', 'B01R', 'B01W', 'B01X', 'B01Y', 'B01Z', 'B020', 'B021', 'B022']:
            print(f"=== Buff {oid} ===")
            for mod_key, raw_bytes in obj['mods']:
                tag = mod_key[0]
                val_bytes = raw_bytes[8:]
                try:
                    val_str = val_bytes.split(b'\x00')[0].decode('utf-8', errors='ignore')
                    print(f"  {tag}: {val_str} -> {res(val_str)}")
                except Exception as e:
                    print(f"  {tag}: {e}")
