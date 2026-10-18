# -*- coding: utf-8 -*-
from pathlib import Path
import sys
sys.path.insert(0, 'scripts')
from implement_draenei_rework import object_records
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        return wts.get(int(s[8:]), s)
    return s

content = Path('map.w3x/war3map.w3u').read_bytes()
ver, tables = object_records(content, False)

unit_ids = ['h0EI', 'h0EJ', 'o01A', 'o01B', 'o019', 'h0EK', 'h0EL', 'n02O', 'n02M', 'n02N', 'h04Y', 'h04Z', 'h050', 'H043', 'E01W', 'E024', 'E025']

for table in tables:
    for rec in table:
        uid = rec['id']
        if uid in unit_ids:
            mods_dict = {}
            for (tag, sub1, sub2), raw_val in rec['mods']:
                # decode string if tag is string
                val_bytes = raw_val[8:-4] if len(raw_val) >= 12 else b""
                # check if null-terminated string
                null_pos = val_bytes.find(b'\x00')
                if null_pos != -1:
                    sval = val_bytes[:null_pos].decode('utf-8', errors='replace')
                else:
                    sval = str(val_bytes)
                mods_dict[tag] = sval
            name = r(mods_dict.get('unam'))
            uabi = mods_dict.get('uabi')
            uhab = mods_dict.get('uhab')
            uhot = r(mods_dict.get('uhot'))
            upgr = mods_dict.get('upgr')
            utub = r(mods_dict.get('utub'))
            print(f"[{uid}] {name} (hotkey: {uhot})")
            print(f"   uabi: {uabi}  uhab: {uhab}")
            print(f"   upgr: {upgr}")
            print(f"   utub: {utub[:60]}...")
