from __future__ import annotations

import argparse
import re
from pathlib import Path


NAMED_FUNCTION_REFERENCE_RE = re.compile(r"\bfunction\s+([A-Za-z_][A-Za-z0-9_]*)\)")
MOJIBAKE_BOM_RE = re.compile(r"^\ufeff?$|^п»ї$")
LOCAL_ARRAY_RE = re.compile(r"^(\s*)local\s+array\s+([A-Za-z_][A-Za-z0-9_]*)\s*$")
LOOP_RE = re.compile(r"^(\s*)loop(\s*.*)$")
PLAYER_ABILITY_RAWCODE_RE = re.compile(r"(SetPlayerAbilityAvailable(?:BJ)?\s*\([^,\n]+,\s*)'([A-Za-z0-9]{4})'")
RAWCODE_LITERAL_RE = re.compile(r"(?<!FourCC\()'([A-Za-z0-9]{4})'")


def normalize_text(text: str) -> tuple[str, int]:
    changes = 0
    output_lines: list[str] = []

    for line in text.splitlines():
        if MOJIBAKE_BOM_RE.match(line):
            changes += 1
            continue

        if not line.lstrip().startswith("--"):
            loop_match = LOOP_RE.match(line)
            if loop_match:
                indent, suffix = loop_match.groups()
                line = f"{indent}while true do{suffix}"
                changes += 1

            local_array_match = LOCAL_ARRAY_RE.match(line)
            if local_array_match:
                indent, name = local_array_match.groups()
                line = f"{indent}local {name} = {{}}"
                changes += 1

            if "!=" in line:
                line = line.replace("!=", "~=")
                changes += 1

            updated, count = PLAYER_ABILITY_RAWCODE_RE.subn(r"\1FourCC('\2')", line)
            line = updated
            changes += count

            updated, count = RAWCODE_LITERAL_RE.subn(r"FourCC('\1')", line)
            line = updated
            changes += count

            updated, count = NAMED_FUNCTION_REFERENCE_RE.subn(r"\1)", line)
            line = updated
            changes += count

            inline_comment_index = line.find("//")
            if inline_comment_index != -1:
                line = line[:inline_comment_index] + "--" + line[inline_comment_index + 2 :]
                changes += 1

            if "/*" in line:
                line = line.replace("/*", "--")
                changes += 1
            if "*/" in line:
                line = line.replace("*/", "")
                changes += 1

        output_lines.append(line)

    normalized = "\n".join(output_lines)
    if text.endswith("\n"):
        normalized += "\n"
    return normalized, changes


def process_path(path: Path) -> int:
    text = path.read_text(encoding="utf-8-sig")
    normalized, changes = normalize_text(text)
    if changes > 0:
        path.write_text(normalized, encoding="utf-8", newline="\n")
    return changes


def iter_lua_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.rglob("*.lua"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize systematic JASS->Lua conversion artifacts.")
    parser.add_argument("path", type=Path, help="Lua file or directory to normalize")
    args = parser.parse_args()

    total_files = 0
    total_changes = 0
    for lua_path in iter_lua_files(args.path):
        changes = process_path(lua_path)
        if changes > 0:
            total_files += 1
            total_changes += changes
            print(f"{lua_path}: {changes} changes")

    print(f"files_changed={total_files} total_changes={total_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
