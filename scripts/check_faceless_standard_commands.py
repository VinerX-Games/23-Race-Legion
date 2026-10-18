"""Check imported command strings, bindings, printf arguments and import registration."""
import csv
import hashlib
import json
import re
import struct
from pathlib import Path
from update_faceless_standard_commands import parse

ROOT = Path(__file__).resolve().parent.parent


def main():
    inventory = json.loads((ROOT / "docs/ui_text/faceless_standard_commands.json").read_text(encoding="utf-8"))
    target = ROOT / inventory["target"]
    actual = parse(target.read_text(encoding="utf-8"))
    errors = []
    if actual != inventory["after"] or hashlib.sha256(target.read_bytes()).hexdigest() != inventory["file_sha256"]:
        errors.append("Command text differs from approved inventory")
    palette = {"ced4da", "ffffff", "c8e087", "e69a8d", "e6c07b", "e4cfa3", "a6afb8", "a9c7de"}
    checked = 0
    for section, fields in actual.items():
        for key, value in fields.items():
            if key.startswith("Hotkey"):
                if value != inventory["before"][section][key]:
                    errors.append(section + "." + key + ": changed binding")
                continue
            values = next(csv.reader([value], skipinitialspace=True))
            if section == "Errors":
                old = next(csv.reader([inventory["before"][section][key]], skipinitialspace=True))
                if len(old) != len(values) or [re.findall(r"%[-+ #0-9.]*[a-zA-Z]", v) for v in old] != [re.findall(r"%[-+ #0-9.]*[a-zA-Z]", v) for v in values]:
                    errors.append(section + "." + key + ": changed alternatives/arguments")
            for text in values:
                checked += 1
                if set(c.lower() for c in re.findall(r"\|cff([0-9a-fA-F]{6})", text)) - palette:
                    errors.append(section + "." + key + ": palette")
                if not text.endswith("|r") or "\ufffd" in text or re.search(r"\?{3,}", text):
                    errors.append(section + "." + key + ": reset/encoding")
                if key == "Ubertip" and not text.startswith("|cffa6afb8КОМАНДА:|cffced4da "):
                    errors.append(section + "." + key + ": type label")
    blob = (ROOT / "map.w3x/war3map.imp").read_bytes()
    _, count = struct.unpack_from("<II", blob)
    pos, paths = 8, []
    for _ in range(count):
        end = blob.index(0, pos + 1)
        paths.append(blob[pos + 1:end].decode("utf-8").replace("\\", "/").lower())
        pos = end + 1
    if pos != len(blob) or paths.count("units/commandstrings.txt") != 1:
        errors.append("Missing/duplicate command-string import")
    report = dict(ok=not errors, text_variants=checked, errors=errors, in_game_checked=False)
    (ROOT / "docs/ui_text/faceless_standard_commands_check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
