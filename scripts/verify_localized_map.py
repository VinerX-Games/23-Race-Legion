"""Verify that generated locale assets are present and unchanged in a map MPQ."""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
from pathlib import Path


def read_mpq_file(storm, archive, name: str) -> bytes:
    handle = ct.c_void_p()
    if not storm.SFileOpenFileEx(archive, name.encode("utf-8"), 0, ct.byref(handle)):
        raise FileNotFoundError(f"MPQ entry is missing: {name}")
    try:
        high = ct.c_uint32()
        size = storm.SFileGetFileSize(handle, ct.byref(high))
        if high.value:
            raise ValueError(f"MPQ entry is too large to verify: {name}")
        buffer = ct.create_string_buffer(size)
        read = ct.c_uint32()
        if size and not storm.SFileReadFile(handle, buffer, size, ct.byref(read), None):
            raise OSError(f"Could not read MPQ entry: {name}")
        if read.value != size:
            raise OSError(f"Short read for MPQ entry {name}: {read.value}/{size}")
        return buffer.raw[:size]
    finally:
        storm.SFileCloseFile(handle)


def verify(archive_path: Path, stormlib_path: Path, locale: str, map_dir: Path) -> dict:
    storm = ct.WinDLL(str(stormlib_path))
    handle = ct.c_void_p()
    storm.SFileOpenArchive.argtypes = [ct.c_wchar_p, ct.c_uint32, ct.c_uint32, ct.POINTER(ct.c_void_p)]
    storm.SFileOpenArchive.restype = ct.c_int
    storm.SFileOpenFileEx.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_uint32, ct.POINTER(ct.c_void_p)]
    storm.SFileOpenFileEx.restype = ct.c_int
    storm.SFileGetFileSize.argtypes = [ct.c_void_p, ct.POINTER(ct.c_uint32)]
    storm.SFileGetFileSize.restype = ct.c_uint32
    storm.SFileReadFile.argtypes = [ct.c_void_p, ct.c_void_p, ct.c_uint32, ct.POINTER(ct.c_uint32), ct.c_void_p]
    storm.SFileReadFile.restype = ct.c_int
    storm.SFileCloseFile.argtypes = [ct.c_void_p]
    storm.SFileCloseArchive.argtypes = [ct.c_void_p]

    if not storm.SFileOpenArchive(str(archive_path), 0, 0x100, ct.byref(handle)):
        raise OSError(f"Could not open map archive: {archive_path}")
    expected = [
        map_dir / "_Locales" / f"{locale}.w3mod" / "war3map.wts",
        map_dir / "_Locales" / f"{locale}.w3mod" / "Units" / "CommandStrings.txt",
    ]
    checked = []
    try:
        for source in expected:
            name = source.relative_to(map_dir).as_posix()
            actual = read_mpq_file(storm, handle, name)
            intended = source.read_bytes()
            actual_hash = hashlib.sha256(actual).hexdigest()
            expected_hash = hashlib.sha256(intended).hexdigest()
            if actual_hash != expected_hash:
                raise ValueError(f"Packaged data differs from generated file: {name}")
            checked.append({"file": name, "size": len(actual), "sha256": actual_hash})
    finally:
        storm.SFileCloseArchive(handle)
    return {"ok": True, "archive": str(archive_path), "files": checked}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--stormlib", required=True, type=Path)
    parser.add_argument("--locale", default="enUS")
    parser.add_argument("--map-dir", type=Path, default=root / "map.w3x")
    args = parser.parse_args()
    if not args.archive.is_file() or not args.stormlib.is_file():
        parser.error("archive or StormLib.dll does not exist")
    try:
        result = verify(args.archive, args.stormlib, args.locale, args.map_dir)
    except (OSError, ValueError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
