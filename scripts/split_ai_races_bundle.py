from __future__ import annotations

import json
import os
import re
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPLIT_ROOT = ROOT / "map.w3x" / "_lua" / "monolith_split"
SECTIONS_DIR = SPLIT_ROOT / "sections"
SOURCE_FILE = SECTIONS_DIR / "82_ai_races.lua"
TARGET_DIR = SECTIONS_DIR / "82_ai_races"
MANIFEST_FILE = SPLIT_ROOT / "manifest.json"

REGISTER_RE = re.compile(r'^RegisterAiRace\("([A-Za-z0-9_]+)"\s*,\s*\{', re.M)
FUNCTION_RE = re.compile(r"^function\s+([A-Za-z0-9_]+)\s*\(", re.M)


def snake_name(name: str) -> str:
    parts = re.findall(r"[A-Z]+[0-9]*(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+[0-9]*|[0-9]+", name)
    return "_".join(part.lower() for part in parts)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def extract_blocks(text: str) -> tuple[str, list[tuple[str, str]]]:
    registers = list(REGISTER_RE.finditer(text))
    if not registers:
        raise RuntimeError("RegisterAiRace blocks not found")

    functions = list(FUNCTION_RE.finditer(text))
    header = text[:registers[0].start()].strip()

    blocks: list[tuple[str, str]] = []
    current_name = registers[0].group(1)
    current_start = registers[0].start()
    pending_next_start: int | None = None

    register_positions = {m.start(): m.group(1) for m in registers}
    function_positions = [m.start() for m in functions]
    markers = sorted(
        [(pos, "register") for pos in register_positions]
        + [(pos, "function") for pos in function_positions]
    )

    active_register_index = 0
    for pos, kind in markers[1:]:
        if kind == "function" and pos > registers[active_register_index].start():
            if pending_next_start is None:
                pending_next_start = pos
            continue

        if kind == "register":
            next_name = register_positions[pos]
            block_end = pending_next_start if pending_next_start is not None else pos
            blocks.append((current_name, text[current_start:block_end].strip()))
            current_name = next_name
            current_start = pending_next_start if pending_next_start is not None else pos
            pending_next_start = None
            active_register_index += 1

    blocks.append((current_name, text[current_start:].strip()))
    return header, blocks


def load_manifest() -> dict:
    return json.loads(read_text(MANIFEST_FILE))


def write_manifest(manifest: dict) -> None:
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def build_manifest_entries(base_entry: dict, files: list[str]) -> list[dict]:
    entries = []
    for relpath in files:
        entry = dict(base_entry)
        stem = Path(relpath).stem
        entry["name"] = f"ai_race_{stem.split('_', 1)[1]}"
        entry["file"] = relpath.replace("\\", "/")
        entries.append(entry)
    return entries


def main() -> None:
    text = read_text(SOURCE_FILE)
    header, blocks = extract_blocks(text)

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    old_race_files = []
    for index, (race_name, block) in enumerate(blocks, start=1):
        relpath = f"82_ai_races/{index:02d}_{snake_name(race_name)}.lua"
        (SECTIONS_DIR / relpath).write_text(block + "\n", encoding="utf-8", newline="\n")
        old_race_files.append(relpath)

    carry_over = [
        ("82_ai_races/01_dragons.lua", "82_ai_races/31_dragons.lua"),
        ("82_ai_races/02_elementals.lua", "82_ai_races/32_elementals.lua"),
    ]
    for src_rel, dst_rel in carry_over:
        src = SECTIONS_DIR / src_rel
        if not src.exists():
            raise FileNotFoundError(src)
        dst = SECTIONS_DIR / dst_rel
        dst.write_text(read_text(src).strip() + "\n", encoding="utf-8", newline="\n")

    keep_files = set(old_race_files + [dst for _, dst in carry_over])
    for path in TARGET_DIR.glob("*.lua"):
        rel = path.relative_to(SECTIONS_DIR).as_posix()
        if rel not in keep_files:
            try:
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
                path.unlink()
            except PermissionError:
                path.write_text(
                    "-- Legacy split file kept as a stub.\n"
                    "-- Active AI race files are listed in manifest.json.\n",
                    encoding="utf-8",
                    newline="\n",
                )

    header_text = (
        "-- AI race registry header.\n"
        "-- Concrete race registrations live in sections/82_ai_races/*.lua.\n"
    )
    SOURCE_FILE.write_text(header_text, encoding="utf-8", newline="\n")

    manifest = load_manifest()
    sections = manifest["sections"]
    header_index = next(i for i, section in enumerate(sections) if section["file"] == "82_ai_races.lua")
    base_entry = dict(sections[header_index])

    filtered_sections = []
    for idx, section in enumerate(sections):
        if idx == header_index:
            filtered_sections.append(section)
            continue
        if section["file"].startswith("82_ai_races/"):
            continue
        filtered_sections.append(section)

    all_race_files = old_race_files + [dst for _, dst in carry_over]
    insert_entries = build_manifest_entries(base_entry, all_race_files)
    filtered_sections[header_index + 1:header_index + 1] = insert_entries

    manifest["sections"] = filtered_sections
    manifest["section_count"] = len(filtered_sections)
    write_manifest(manifest)

    if header:
        print("Header preserved in 82_ai_races.lua stub")
    print(f"Split {len(blocks)} races into {TARGET_DIR}")


if __name__ == "__main__":
    main()
