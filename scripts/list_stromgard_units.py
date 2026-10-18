# -*- coding: utf-8 -*-
import sys, re, struct
from pathlib import Path

wts = {}
with open('map.w3x/war3map.wts', 'r', encoding='utf-8') as f:
    text = f.read()
for m in re.finditer(r'STRING\s+(\d+)\s*\{([^}]*)\}', text):
    wts[int(m.group(1))] = m.group(2).strip()

def res(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        return wts.get(int(s[8:]), s)
    return s

def parse_w3u(path):
    with open(path, 'rb') as f:
        data = f.read()
    pos = 4
    results = {}
    for table_idx in range(2):
        count = struct.unpack_from('<I', data, pos)[0]
        pos += 4
        for _ in range(count):
            base_id = data[pos:pos+4].decode('latin1', errors='replace')
            new_id = data[pos+4:pos+8].decode('latin1', errors='replace')
            pos += 8
            fcount = struct.unpack_from('<I', data, pos)[0]
            pos += 4
            fields = {}
            for _ in range(fcount):
                fid = data[pos:pos+4].decode('latin1', errors='replace')
                ftype, fval, fend = struct.unpack_from('<III', data, pos+4)
                pos += 16
                if ftype == 0:
                    val = fval
                elif ftype == 3:
                    slen = struct.unpack_from('<I', data, pos)[0]
                    pos += 4
                    val = data[pos:pos+slen-1].decode('utf-8', errors='replace')
                    pos += slen
                else:
                    val = fval
                pos += 4
                fields[fid] = val
            uid = new_id if new_id != '\x00\x00\x00\x00' else base_id
            results[uid] = (base_id, fields)
    return results

units = parse_w3u('map.w3x/war3map.w3u')
for uid, (base, fields) in sorted(units.items()):
    name = res(fields.get('unam', ''))
    suffix = res(fields.get('unsf', ''))
    isbldg = fields.get('ubdg', 0)
    if 'стромгард' in str(suffix).lower() or 'стромгард' in str(name).lower() or uid in ['h0G9', 'h0F4', 'h0GS', 'h0GT', 'h0GV', 'h0GU', 'h0GW', 'h0GX', 'h0HD', 'h0HE', 'h0L3', 'o03X', 'h0GY', 'h0HC', 'h02Z', 'h0HX', 'h0I3', 'o02Q', 'o02R', 'o06A', 'o06B', 'o06C', 'o06D', 'o06E', 'o06F']:
        print(f"{uid} (base {base}) bldg={isbldg}: name={name!r} suffix={suffix!r} raw_tip={fields.get('utip')} raw_ubertip={fields.get('utub')}")
