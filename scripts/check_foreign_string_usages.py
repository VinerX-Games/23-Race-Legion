# -*- coding: utf-8 -*-
"""Check if any of Scarlet Crusade string IDs are used in other objects across the map."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from implement_draenei_rework import object_records

cat = json.loads((ROOT / "scripts/scarlet_strings_catalog.json").read_text(encoding="utf-8"))
scarlet_sids = {int(k) for k in cat.keys()}

# Let's inspect all objects in w3u, w3a, w3q, w3h
scarlet_obj_ids = {
    'A0HM',
    'h05U', 'h05V', 'h05W', 'h05X', 'h05Y', 'h05Z', 'h060', 'h061', 'h062', 'h063', 'h064', 'h068',
    'H03H', 'H06C', 'H06B',
    'h014', 'h039', 'h03A', 'h03B', 'h03C', 'h03D', 'h03F', 'h03G', 'h03I', 'h065', 'h066', 'h067', 'n007', 'n008', 'o00I',
    'A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J',
    'A07I', 'A07X', 'A07Y', 'A07Z', 'A080', 'A081', 'A082', 'A083', 'A084', 'A085', 'A087', 'A088',
    'A089', 'A08A', 'A08B', 'A08C', 'A08D', 'A08E', 'A08F', 'A08G', 'A08J', 'A08K', 'A08L', 'A08M',
    'A08N', 'A08O', 'A08P', 'A08X', 'A08Y', 'A09O',
    'B01K', 'B01L', 'B01M', 'B01N', 'B01P', 'B01R', 'B01W', 'B01X', 'B01Y', 'B01Z', 'B020', 'B021', 'B022',
    'R03K', 'R03L', 'R03M', 'R03S', 'R03T', 'R03U', 'R03V', 'R03W', 'R03X', 'R03Y', 'R03Z', 'R040',
    'R041', 'R042', 'R043', 'R044', 'R045', 'R046', 'R047', 'R048', 'R049', 'R04A', 'R04B', 'R04C',
    'R07B', 'R0KG', 'R0KH'
}

foreign_usages = {}

for ext in ['w3u', 'w3a', 'w3q', 'w3h']:
    for name in [f'war3map.{ext}', f'war3mapSkin.{ext}']:
        p = ROOT / 'map.w3x' / name
        if not p.exists(): continue
        header, tables = object_records(p.read_bytes(), False)
        for table in tables:
            for obj in table:
                oid = obj['id']
                if oid in scarlet_obj_ids: continue
                for mod_key, raw_bytes in obj['mods']:
                    tag = mod_key[0]
                    val_bytes = raw_bytes[8:]
                    try:
                        val_str = val_bytes.split(b'\x00')[0].decode('utf-8', errors='ignore')
                        if val_str.startswith('TRIGSTR_'):
                            sid = int(val_str[8:])
                            if sid in scarlet_sids:
                                if sid not in foreign_usages:
                                    foreign_usages[sid] = []
                                foreign_usages[sid].append((oid, name, tag))
                    except Exception:
                        pass

print(f"Total Scarlet strings used by foreign objects: {len(foreign_usages)}")
for sid, usages in sorted(foreign_usages.items()):
    val = cat[str(sid)][0]['current_val']
    print(f"  STRING {sid} (val={repr(val)[:40]}): used by {usages}")
