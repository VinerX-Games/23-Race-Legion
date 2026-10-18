import re
import struct
from pathlib import Path

wts = Path('map.w3x/war3map.wts').read_text(encoding='utf-8', errors='ignore')
m = re.findall(r'STRING (\d+)\s*\{\s*([^}]+)\}', wts)
strings = {f'TRIGSTR_{k}': v.strip() for k, v in m}

ids = ['h012', 'h015', 'h016', 'h017', 'h05C', 'h057', 'h033', 'h058', 'h056', 'h05A', 'h055',
       'h01S', 'h01P', 'e000', 'h01O', 'h01R', 'h059', 'h01T', 'h01U', 'h01Q', 'n005', 'h05E', 'h05D',
       'H05K', 'H05L', 'H05M']

buf = Path('map.w3x/war3map.w3u').read_bytes()
pos = 0
ver, = struct.unpack_from('<I', buf, pos); pos += 4

def parse_tbl(pos):
    count, = struct.unpack_from('<I', buf, pos); pos += 4
    objects = {}
    for i in range(count):
        orig = buf[pos:pos+4].decode('latin1', 'replace'); pos += 4
        cust = buf[pos:pos+4].decode('latin1', 'replace'); pos += 4
        extra1, extra2 = struct.unpack_from('<II', buf, pos); pos += 8
        mod_count, = struct.unpack_from('<I', buf, pos); pos += 4
        mods = {}
        for m_idx in range(mod_count):
            mod_id = buf[pos:pos+4].decode('latin1', 'replace'); pos += 4
            v_type, = struct.unpack_from('<I', buf, pos); pos += 4
            if v_type == 0: val, = struct.unpack_from('<i', buf, pos); pos += 4
            elif v_type in (1, 2): val, = struct.unpack_from('<f', buf, pos); pos += 4
            elif v_type == 3:
                s_end = buf.find(b'\x00', pos)
                val = buf[pos:s_end].decode('utf-8', 'replace')
                pos = s_end + 1
            end_token, = struct.unpack_from('<I', buf, pos); pos += 4
            mods[mod_id] = val
        key = cust if cust != '\x00\x00\x00\x00' else orig
        objects[key] = (orig, cust, mods)
    return objects, pos

orig_objs, pos = parse_tbl(pos)
custom_objs, pos = parse_tbl(pos)
all_objs = {**orig_objs, **custom_objs}

print("=== ДРЕНЕИ: ЗДАНИЯ, ЮНИТЫ И ГЕРОИ ===")
for uid in ids:
    if uid in all_objs:
        orig, cust, mods = all_objs[uid]
        raw_name = mods.get('unam', '')
        name = strings.get(raw_name, raw_name)
        uabi = mods.get('uabi', '')
        tip = strings.get(mods.get('utip', ''), '')
        print(f"[{uid}] ({orig}->{cust}) {name} | Спеллы: {uabi}")
    else:
        print(f"[{uid}] Не найден в w3u")
