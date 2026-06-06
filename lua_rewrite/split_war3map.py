from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


LIBRARY_START_RE = re.compile(r"^-- library (.*):$")
LIBRARY_END_RE = re.compile(r"^-- library (.*) ends$")
GLOBALS_START_RE = re.compile(r"^-- globals from (.*):$")
FUNCTION_RE = re.compile(r"^function ([A-Za-z0-9_]+)\(")


@dataclass
class Section:
    name: str
    file: str
    category: str
    start_line: int
    end_line: int
    library_name: str | None = None


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return handle.read()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sanitize_name(name: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    return sanitized or "section"


def find_first_regex(lines: list[str], pattern: re.Pattern[str], start_line: int = 1, end_line: int | None = None) -> int:
    end_line = end_line or len(lines)
    for line_no in range(start_line, end_line + 1):
        if pattern.match(lines[line_no - 1].rstrip("\r\n")):
            return line_no
    raise RuntimeError(f"Pattern not found: {pattern.pattern}")


def find_exact_line(lines: list[str], text: str) -> int:
    for line_no, line in enumerate(lines, 1):
        if line.rstrip("\r\n") == text:
            return line_no
    raise RuntimeError(f"Line not found: {text}")


def collect_libraries(lines: list[str]) -> list[Section]:
    starts: list[tuple[int, str]] = []
    ends: dict[str, int] = {}

    for line_no, raw_line in enumerate(lines, 1):
        line = raw_line.rstrip("\r\n")
        match = LIBRARY_START_RE.match(line)
        if match:
            starts.append((line_no, match.group(1)))
            continue

        match = LIBRARY_END_RE.match(line)
        if match:
            ends[match.group(1)] = line_no

    sections: list[Section] = []
    for index, (start_line, library_name) in enumerate(starts, 1):
        end_line = ends.get(library_name)
        if end_line is None:
            raise RuntimeError(f"Missing library end marker for {library_name}")

        sections.append(
            Section(
                name=f"library:{library_name}",
                file=f"libraries/{index:02d}_{sanitize_name(library_name)}.lua",
                category="library",
                start_line=start_line,
                end_line=end_line,
                library_name=library_name,
            )
        )

    if len(starts) != len(ends):
        raise RuntimeError("Library start/end marker count mismatch")

    return sections


def build_section_manifest(source_text: str) -> list[Section]:
    lines = source_text.splitlines(keepends=True)

    first_globals_line = find_first_regex(lines, GLOBALS_START_RE)
    first_library_line = find_first_regex(lines, LIBRARY_START_RE)
    first_pre_library_function = find_first_regex(lines, FUNCTION_RE, start_line=first_globals_line, end_line=first_library_line - 1)

    library_sections = collect_libraries(lines)
    last_library_end = library_sections[-1].end_line

    init_custom_triggers_line = find_exact_line(lines, "function InitCustomTriggers()")
    run_initialization_line = find_exact_line(lines, "function RunInitializationTriggers()")
    init_custom_player_slots_line = find_exact_line(lines, "function InitCustomPlayerSlots()")
    main_line = find_exact_line(lines, "function main()")
    config_line = find_exact_line(lines, "function config()")

    sections: list[Section] = [
        Section("prelude", "00_prelude.lua", "prelude", 1, first_globals_line - 1),
        Section("globals", "01_globals.lua", "globals", first_globals_line, first_pre_library_function - 1),
        Section(
            "pre_library_functions",
            "02_pre_library_functions.lua",
            "functions",
            first_pre_library_function,
            first_library_line - 1,
        ),
    ]
    sections.extend(library_sections)
    sections.extend(
        [
            Section(
                "generated_runtime",
                "80_generated_runtime.lua",
                "generated_runtime",
                last_library_end + 1,
                init_custom_triggers_line - 1,
            ),
            Section(
                "init_custom_triggers",
                "90_InitCustomTriggers.lua",
                "entrypoint",
                init_custom_triggers_line,
                run_initialization_line - 1,
            ),
            Section(
                "run_initialization_triggers",
                "91_RunInitializationTriggers.lua",
                "entrypoint",
                run_initialization_line,
                init_custom_player_slots_line - 1,
            ),
            Section(
                "map_setup",
                "92_map_setup.lua",
                "entrypoint",
                init_custom_player_slots_line,
                main_line - 1,
            ),
            Section("main", "93_main.lua", "entrypoint", main_line, config_line - 1),
            Section("config", "94_config.lua", "entrypoint", config_line, len(lines)),
        ]
    )

    expected_start = 1
    for section in sections:
        if section.start_line != expected_start:
            raise RuntimeError(
                f"Gap or overlap before section {section.name}: expected line {expected_start}, got {section.start_line}"
            )
        if section.end_line < section.start_line:
            raise RuntimeError(f"Invalid section range for {section.name}")
        expected_start = section.end_line + 1

    if expected_start != len(lines) + 1:
        raise RuntimeError("Section coverage does not reach end of file")

    return sections


def write_split_source(output_dir: Path, source_path: Path, source_text: str, sections: list[Section]) -> None:
    lines = source_text.splitlines(keepends=True)
    sections_dir = output_dir / "sections"

    for section in sections:
        text = "".join(lines[section.start_line - 1 : section.end_line])
        write_text(sections_dir / section.file, text)

    manifest = {
        "source_path": str(source_path),
        "source_sha256": sha256_text(source_text),
        "section_count": len(sections),
        "sections": [asdict(section) for section in sections],
    }
    write_text(output_dir / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def load_manifest(manifest_path: Path) -> dict:
    return json.loads(read_text(manifest_path))


def rebuild_from_manifest(output_dir: Path) -> str:
    manifest = load_manifest(output_dir / "manifest.json")
    sections_dir = output_dir / "sections"
    parts: list[str] = []
    for section in manifest["sections"]:
        parts.append(read_text(sections_dir / section["file"]))
    return "".join(parts)


def split_and_rebuild(source_path: Path, output_dir: Path, rebuild_output: Path | None, verify: bool) -> int:
    source_text = read_text(source_path)
    sections = build_section_manifest(source_text)
    write_split_source(output_dir, source_path, source_text, sections)

    rebuilt_text = rebuild_from_manifest(output_dir)
    if rebuild_output is not None:
        write_text(rebuild_output, rebuilt_text)

    rebuilt_hash = sha256_text(rebuilt_text)
    source_hash = sha256_text(source_text)

    print(f"Sections written: {len(sections)}")
    print(f"Source sha256:  {source_hash}")
    print(f"Rebuilt sha256: {rebuilt_hash}")

    if verify:
        if rebuilt_text != source_text:
            raise RuntimeError("Rebuilt script does not match original source text")
        print("Verify: exact text match")

    return 0


def build_only(output_dir: Path, rebuild_output: Path) -> int:
    rebuilt_text = rebuild_from_manifest(output_dir)
    write_text(rebuild_output, rebuilt_text)
    print(f"Rebuilt {rebuild_output}")
    print(f"Rebuilt sha256: {sha256_text(rebuilt_text)}")
    return 0


def main() -> int:
    root = Path(__file__).resolve().parent
    repo_root = root.parent
    default_source = repo_root / "map.w3x" / "war3map.lua"
    default_output_dir = repo_root / "map.w3x" / "_lua" / "monolith_split"
    default_rebuild_output = repo_root / "map.w3x" / "war3map.lua"

    parser = argparse.ArgumentParser(description="Split the canonical map.w3x/war3map.lua into stable source sections.")
    parser.add_argument("--source", type=Path, default=default_source)
    parser.add_argument("--output-dir", type=Path, default=default_output_dir)
    parser.add_argument("--rebuild-output", type=Path, default=default_rebuild_output)
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.build_only:
        return build_only(args.output_dir, args.rebuild_output)

    return split_and_rebuild(args.source, args.output_dir, args.rebuild_output, args.verify)


if __name__ == "__main__":
    raise SystemExit(main())
