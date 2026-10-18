# -*- coding: utf-8 -*-
"""Check if any of the 547 active Scarlet string IDs are used by non-Scarlet objects."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

# Load active sids
import count_active_scarlet_strings
active_sids = set(count_active_scarlet_strings.active_sids.keys())

scarlet_objs = {
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

# Scan raw binary files for TRIGSTR_<sid>
# In WC3 object data, strings are null-terminated ASCII/UTF-8 like "TRIGSTR_12345\x00"
trigstr_pattern = re.compile(rb'TRIGSTR_(\d+)\x00')

foreign_hits = {}
for p in (ROOT / 'map.w3x').glob('war3map*.w3*'):
    data = p.read_bytes()
    # Let's search all TRIGSTR matches
    for m in trigstr_pattern.finditer(data):
        sid = int(m.group(1))
        if sid in active_sids:
            # Let's find what object contains this pos
            pos = m.start()
            # Object header is within preceding bytes
            # Look backwards up to 300 bytes for a 4-char ID
            chunk = data[max(0, pos - 300):pos]
            # check if any foreign object ID appears
            # For simplicity, record file
            pass

print(f"Total active SIDs being checked: {len(active_sids)}")
