"""Reader for Warcraft III object-data tables (w3u, w3a, w3q, ...)."""
from __future__ import annotations

import struct


def extended_for(name: str) -> bool:
    """Abilities and upgrades use level/pointer headers; doodads only in the base file."""
    suffix = name.rsplit(".", 1)[-1].lower()
    if suffix in ("w3a", "w3q"):
        return True
    return suffix == "w3d" and not name.startswith("war3mapSkin")


def string_value(raw: bytes, extended: bool) -> str | None:
    """Return a string modification value, or None for numeric modifications."""
    if struct.unpack_from("<I", raw, 4)[0] != 3:
        return None
    pos = 8 + (8 if extended else 0)
    return raw[pos:].split(b"\x00")[0].decode("utf-8", "replace")


def object_records(blob: bytes, extended: bool):
    """Read record boundaries without normalizing values, end tokens or unknown fields."""
    version = struct.unpack_from("<I", blob)[0]
    pos, tables = 4, []
    for _ in range(2):
        count = struct.unpack_from("<I", blob, pos)[0]
        pos += 4
        records = []
        for _ in range(count):
            start = pos
            old, new = blob[pos:pos + 4], blob[pos + 4:pos + 8]
            pos += 8
            if version >= 3:
                extra_count = struct.unpack_from("<I", blob, pos)[0]
                pos += 4 + extra_count * 4
            header = blob[start:pos]
            mods_count = struct.unpack_from("<I", blob, pos)[0]
            pos += 4
            mods = []
            for _ in range(mods_count):
                mod_start = pos
                field = blob[pos:pos + 4].decode("ascii")
                value_type = struct.unpack_from("<I", blob, pos + 4)[0]
                pos += 8
                level, pointer = 0, 0
                if extended:
                    level, pointer = struct.unpack_from("<II", blob, pos)
                    pos += 8
                if value_type == 3:
                    pos = blob.index(0, pos) + 1
                else:
                    assert value_type in (0, 1, 2)
                    pos += 4
                pos += 4  # Preserve original end token.
                mods.append(((field, level, pointer), blob[mod_start:pos]))
            code = (new if new != b"\0" * 4 else old).decode("latin1")
            records.append({"id": code, "header": header, "mods": mods, "raw": blob[start:pos]})
        tables.append(records)
    assert pos == len(blob), (pos, len(blob))
    return version, tables
