import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from implement_draenei_rework import object_records
import struct
import re

raw_data = open('map.w3x/war3map.w3q', 'rb').read()
_, tables_data = object_records(raw_data, True)
data_recs = {r['id']: r for t in tables_data for r in t}

troll_upgs = [
    'R09L', 'R09P', 'R0AD', 'R0AI', 'R0AJ', 'R0EU', 'R0HZ', 'R0I0', 'R0I1', 'R0I2',
    'R0I3', 'R0I4', 'R0I5', 'R0I6', 'R0I7', 'R0IE', 'R0IF', 'R0IG', 'R0IX', 'R0IY'
]

# Check IceTrolls.lua for SetPlayerTechMaxAllowedSwap
lua_text = Path('map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/IceTrolls.lua').read_text(encoding='utf-8')
lua_limits = {}
for m in re.finditer(r"SetPlayerTechMaxAllowedSwap\(FourCC\('([^']+)'\),\s*(-?\d+)", lua_text):
    qid, limit = m.group(1), int(m.group(2))
    lua_limits[qid] = limit

for qid in troll_upgs:
    data_entry = data_recs.get(qid)
    glvl = 1
    if data_entry:
        for k, raw in data_entry['mods']:
            if k[0] == 'glvl':
                glvl = struct.unpack_from('<I', raw, 16)[0]
    limit = lua_limits.get(qid, 'default')
    print(f"{qid}: glvl={glvl}, lua_limit={limit}")
