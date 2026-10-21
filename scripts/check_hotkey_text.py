"""Проверка, что поля горячих клавиш содержат клавишу, а не описание.

Читает object data напрямую (SD и skin), без HiveWE и CASC:
    python scripts/check_hotkey_text.py [--json]

Код возврата 1, если хотя бы одно поле горячей клавиши указывает на WTS-строку,
которая не является одиночным символом клавиши.
"""
from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from implement_draenei_rework import object_records  # noqa: E402
from wc3_hivewe import load_wts_strings  # noqa: E402

MAP = ROOT / "map.w3x"
HOTKEY_FIELDS = {"ahky": "hotkey", "arhk": "researchhotkey", "auhk": "unhotkey",
                 "uhot": "hotkey", "ghky": "hotkey"}
TYPES = (("ability", "w3a"), ("unit", "w3u"), ("upgrade", "w3q"),
         ("item", "w3t"), ("buff", "w3h"))


def extended_for(name: str, ext: str) -> bool:
    if ext in ("w3a", "w3q"):
        return True
    return ext == "w3d" and not name.startswith("war3mapSkin")


def string_value(raw: bytes, extended: bool):
    if struct.unpack_from("<I", raw, 4)[0] != 3:
        return None
    pos = 8 + (8 if extended else 0)
    return raw[pos:].split(b"\x00")[0].decode("utf-8", "replace")


def is_key(text) -> bool:
    if not isinstance(text, str):
        return True
    return len(text.strip()) <= 1


def collect(wts: dict[int, str]) -> list[dict]:
    problems = []
    for _, ext in TYPES:
        for name in (f"war3map.{ext}", f"war3mapSkin.{ext}"):
            path = MAP / name
            if not path.is_file():
                continue
            extended = extended_for(name, ext)
            _, tables = object_records(path.read_bytes(), extended)
            for table in tables:
                for record in table:
                    for key, raw in record["mods"]:
                        if key[0] not in HOTKEY_FIELDS:
                            continue
                        value = string_value(raw, extended)
                        if value is None:
                            continue
                        if value.startswith("TRIGSTR_"):
                            sid = int(value[8:])
                            shown = wts.get(sid)
                            if shown is None:
                                problems.append(dict(file=name, id=record["id"],
                                                     field=HOTKEY_FIELDS[key[0]],
                                                     wts=sid, issue="missing WTS string"))
                                continue
                        else:
                            sid, shown = None, value
                        if not is_key(shown):
                            problems.append(dict(file=name, id=record["id"],
                                                 field=HOTKEY_FIELDS[key[0]], wts=sid,
                                                 issue="value is text, not a key",
                                                 text=shown[:80]))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="печатать JSON")
    args = parser.parse_args()
    wts = load_wts_strings(MAP / "war3map.wts")
    problems = collect(wts)
    if args.json:
        print(json.dumps({"ok": not problems, "problems": problems}, ensure_ascii=False))
    else:
        print(f"hotkey problems: {len(problems)}")
        for problem in problems:
            print(f"  {problem['file']}:{problem['id']}:{problem['field']} "
                  f"#{problem.get('wts')} — {problem['issue']}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
