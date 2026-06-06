from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_manifest(split_dir: Path) -> dict:
    return json.loads(read_text(split_dir / "manifest.json"))


def rebuild_from_manifest(split_dir: Path) -> str:
    manifest = load_manifest(split_dir)
    sections_dir = split_dir / "sections"
    parts: list[str] = []
    for section in manifest["sections"]:
        parts.append(read_text(sections_dir / section["file"]))
    return "".join(parts)


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    default_split_dir = repo_root / "map.w3x" / "_lua" / "monolith_split"
    default_output = repo_root / "map.w3x" / "war3map.lua"

    parser = argparse.ArgumentParser(
        description="Rebuild the canonical map.w3x/war3map.lua from the split Lua source tree."
    )
    parser.add_argument("--split-dir", type=Path, default=default_split_dir)
    parser.add_argument("--output", type=Path, default=default_output)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    rebuilt_text = rebuild_from_manifest(args.split_dir)
    rebuilt_hash = sha256_text(rebuilt_text)
    current_hash = None

    if args.output.is_file():
        current_hash = sha256_text(read_text(args.output))

    if args.check_only:
        print(f"split_dir={args.split_dir}")
        print(f"output={args.output}")
        print(f"rebuilt_sha256={rebuilt_hash}")
        print(f"current_sha256={current_hash or 'missing'}")
        print(f"matches_current={current_hash == rebuilt_hash}")
        return 0

    write_text(args.output, rebuilt_text)
    print(f"rebuilt={args.output}")
    print(f"rebuilt_sha256={rebuilt_hash}")
    print(f"previous_sha256={current_hash or 'missing'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
