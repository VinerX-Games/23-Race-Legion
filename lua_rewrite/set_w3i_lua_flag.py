from __future__ import annotations

import argparse
import struct
from pathlib import Path


def read_u32(data: bytes, offset: int) -> tuple[int, int]:
    return struct.unpack_from("<I", data, offset)[0], offset + 4


def read_u8(data: bytes, offset: int) -> tuple[int, int]:
    return data[offset], offset + 1


def read_c_string(data: bytes, offset: int) -> tuple[str, int]:
    end = data.index(0, offset)
    return data[offset:end].decode("utf-8", errors="replace"), end + 1


def locate_lua_flag_offset(data: bytes) -> tuple[int, int]:
    offset = 0
    version, offset = read_u32(data, offset)
    if version < 28:
        raise RuntimeError(f"war3map.w3i version {version} does not have a Lua flag")

    _, offset = read_u32(data, offset)  # map version
    _, offset = read_u32(data, offset)  # editor version
    for _ in range(4):
        _, offset = read_u32(data, offset)  # game version major/minor/patch/build

    for _ in range(4):
        _, offset = read_c_string(data, offset)  # name/author/description/suggested players

    offset += 4 * 2 * 4  # four vec2 camera bounds
    offset += 4 * 4  # camera complements
    _, offset = read_u32(data, offset)  # playable width
    _, offset = read_u32(data, offset)  # playable height
    _, offset = read_u32(data, offset)  # flags
    _, offset = read_u8(data, offset)  # tileset

    _, offset = read_u32(data, offset)  # loading screen number
    for _ in range(4):
        _, offset = read_c_string(data, offset)  # loading screen model/text/title/subtitle

    _, offset = read_u32(data, offset)  # game data set
    for _ in range(4):
        _, offset = read_c_string(data, offset)  # prologue model/text/title/subtitle

    _, offset = read_u32(data, offset)  # fog style
    offset += 4  # fog start
    offset += 4  # fog end
    offset += 4  # fog density
    offset += 4  # fog color
    _, offset = read_u32(data, offset)  # weather id
    _, offset = read_c_string(data, offset)  # custom sound environment
    _, offset = read_u8(data, offset)  # custom light tileset
    offset += 4  # water color

    return version, offset


def read_lua_flag(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    version, offset = locate_lua_flag_offset(data)
    value = struct.unpack_from("<I", data, offset)[0]
    return version, value


def write_lua_flag(path: Path, enabled: bool) -> tuple[int, int, int]:
    data = bytearray(path.read_bytes())
    version, offset = locate_lua_flag_offset(data)
    before = struct.unpack_from("<I", data, offset)[0]
    struct.pack_into("<I", data, offset, 1 if enabled else 0)
    path.write_bytes(data)
    after = struct.unpack_from("<I", data, offset)[0]
    return version, before, after


def main() -> int:
    parser = argparse.ArgumentParser(description="Read or update the Lua flag inside war3map.w3i.")
    parser.add_argument("w3i", type=Path)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--enable-lua", action="store_true")
    group.add_argument("--disable-lua", action="store_true")
    args = parser.parse_args()

    if args.enable_lua or args.disable_lua:
        version, before, after = write_lua_flag(args.w3i, enabled=args.enable_lua)
        print(f"{args.w3i} version={version} lua_before={before} lua_after={after}")
    else:
        version, value = read_lua_flag(args.w3i)
        print(f"{args.w3i} version={version} lua={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
