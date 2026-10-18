# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from implement_draenei_rework import object_records
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        return wts.get(int(s[8:]), s)
    return s

# Check buffs (w3h)
content_h = Path('map.w3x/war3map.w3h').read_bytes()
ver_h, tables_h = object_records(content_h, False)
print("=== Scanning war3map.w3h ===")
for table in tables_h:
    for rec in table:
        bid = rec['id']
        mods = {}
        for (tag, sub1, sub2), raw_val in rec['mods']:
            val_bytes = raw_val[8:-4] if len(raw_val) >= 12 else b""
            null_pos = val_bytes.find(b'\x00')
            if null_pos != -1:
                mods[tag] = val_bytes[:null_pos].decode('utf-8', errors='replace')
        fnam = r(mods.get('fnam'))
        ftip = r(mods.get('ftip'))
        fube = r(mods.get('fube'))
        text_all = f"{fnam} {ftip} {fube}".lower()
        if any(w in text_all for w in ['иллидар', 'illidar', 'скверн', 'охотник']):
            print(f"Buff [{bid}] fnam={repr(fnam)} ftip={repr(ftip)}")
            print(f"   fube={repr(fube)}")

