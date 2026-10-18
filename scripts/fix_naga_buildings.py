import struct
import shutil
from pathlib import Path

W3U_PATH = Path("map.w3x/war3map.w3u")
BACKUP_PATH = Path("map.w3x/war3map.w3u.bak")

def parse_w3u(buf):
    pos = 0
    ver, = struct.unpack_from('<I', buf, pos); pos += 4

    def parse_tbl(pos):
        count, = struct.unpack_from('<I', buf, pos); pos += 4
        objects = []
        for _ in range(count):
            orig = buf[pos:pos+4].decode('latin1'); pos += 4
            cust = buf[pos:pos+4].decode('latin1'); pos += 4
            extra1, extra2 = struct.unpack_from('<II', buf, pos); pos += 8
            mod_count, = struct.unpack_from('<I', buf, pos); pos += 4
            mods = []
            for _ in range(mod_count):
                mod_id = buf[pos:pos+4].decode('latin1'); pos += 4
                v_type, = struct.unpack_from('<I', buf, pos); pos += 4
                if v_type == 0:
                    val, = struct.unpack_from('<i', buf, pos); pos += 4
                elif v_type in (1, 2):
                    val, = struct.unpack_from('<f', buf, pos); pos += 4
                elif v_type == 3:
                    s_end = buf.find(b'\x00', pos)
                    val = buf[pos:s_end].decode('utf-8', 'replace')
                    pos = s_end + 1
                else:
                    raise ValueError(f"Unknown v_type {v_type} at {pos}")
                end_token, = struct.unpack_from('<I', buf, pos); pos += 4
                mods.append({
                    'id': mod_id,
                    'type': v_type,
                    'val': val,
                    'end': end_token
                })
            objects.append({
                'orig': orig,
                'cust': cust,
                'extra1': extra1,
                'extra2': extra2,
                'mods': mods
            })
        return objects, pos

    orig_objs, pos = parse_tbl(pos)
    custom_objs, pos = parse_tbl(pos)
    return ver, orig_objs, custom_objs

def serialize_w3u(ver, orig_objs, custom_objs):
    out = bytearray()
    out.extend(struct.pack('<I', ver))

    def write_tbl(objs):
        out.extend(struct.pack('<I', len(objs)))
        for obj in objs:
            out.extend(obj['orig'].encode('latin1'))
            out.extend(obj['cust'].encode('latin1'))
            out.extend(struct.pack('<II', obj['extra1'], obj['extra2']))
            out.extend(struct.pack('<I', len(obj['mods'])))
            for m in obj['mods']:
                out.extend(m['id'].encode('latin1'))
                out.extend(struct.pack('<I', m['type']))
                if m['type'] == 0:
                    out.extend(struct.pack('<i', int(m['val'])))
                elif m['type'] in (1, 2):
                    out.extend(struct.pack('<f', float(m['val'])))
                elif m['type'] == 3:
                    out.extend(str(m['val']).encode('utf-8') + b'\x00')
                out.extend(struct.pack('<I', m['end']))

    write_tbl(orig_objs)
    write_tbl(custom_objs)
    return bytes(out)

def set_or_add_mod(obj, mod_id, v_type, val):
    for m in obj['mods']:
        if m['id'] == mod_id:
            m['type'] = v_type
            m['val'] = val
            return
    obj['mods'].append({
        'id': mod_id,
        'type': v_type,
        'val': val,
        'end': 0
    })

def main():
    buf = W3U_PATH.read_bytes()
    shutil.copyfile(W3U_PATH, BACKUP_PATH)
    print(f"Read {len(buf)} bytes from {W3U_PATH}")

    ver, orig_objs, custom_objs = parse_w3u(buf)
    print(f"Parsed {len(orig_objs)} orig, {len(custom_objs)} custom objects")

    # Target buildings
    # Orig:
    #   nntt (Temple of the Tides)
    #   nnfm (Coral Bed)
    #   nnsg (Spawning Grounds)
    #   nnsa (Shrine of Azshara)
    #   nnad (Altar of the Depths)
    #   nntg (Tidal Guardian)
    # Custom:
    #   n055 (Portal / Barracks tier 2)
    # n04L (Serpent's Lair) is intentionally excluded: sea-serpent production
    # must stay on shallow water (preventplace=unwalkable,unfloat; movetp=float).
    #   h0JW (Naga Royal Vault)
    #   h0JX (Temple of Ages)
    #   h0JY (Temple of Eternity)

    TARGETS = {'nntt', 'nnfm', 'nnsg', 'nnsa', 'nnad', 'nntg', 'n055', 'h0JW', 'h0JX', 'h0JY'}

    modified_count = 0
    for tbl_name, objs in [('orig', orig_objs), ('custom', custom_objs)]:
        for obj in objs:
            key = obj['cust'] if obj['cust'] != '\x00\x00\x00\x00' else obj['orig']
            if key in TARGETS:
                print(f"Modifying {tbl_name} object: {obj['orig']} -> {obj['cust']} (key={key})")
                # 1. Placement Prevented: only unwalkable (NOT unfloat)
                set_or_add_mod(obj, 'upap', 3, 'unwalkable')
                # 2. Placement Requires: empty (remove water/amphibious requirement)
                set_or_add_mod(obj, 'upar', 3, '')
                # 3. Movement Type: empty (NOT float)
                set_or_add_mod(obj, 'umvt', 3, '')
                # 4. Pathing texture: ensure solid land footprint
                if key == 'nntg':
                    set_or_add_mod(obj, 'upat', 3, 'PathTextures\\4x4SimpleSolid.tga')
                modified_count += 1

    print(f"Modified {modified_count} buildings")

    new_buf = serialize_w3u(ver, orig_objs, custom_objs)
    W3U_PATH.write_bytes(new_buf)
    print(f"Wrote {len(new_buf)} bytes to {W3U_PATH}")

    # Verify round-trip parse
    ver2, orig2, custom2 = parse_w3u(new_buf)
    print(f"Verified re-parse: {len(orig2)} orig, {len(custom2)} custom")
    for tbl_name, objs in [('orig', orig2), ('custom', custom2)]:
        for obj in objs:
            key = obj['cust'] if obj['cust'] != '\x00\x00\x00\x00' else obj['orig']
            if key in TARGETS:
                m_dict = {m['id']: m['val'] for m in obj['mods']}
                print(f"  {key}: upap={repr(m_dict.get('upap'))} upar={repr(m_dict.get('upar'))} umvt={repr(m_dict.get('umvt'))} upat={repr(m_dict.get('upat'))}")

if __name__ == '__main__':
    main()
