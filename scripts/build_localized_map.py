"""Build and package the map after validating locale assets.

The base locale (enUS) replaces the packaged war3map.wts, war3map.w3i and
Units/CommandStrings.txt; the Russian originals go to _Locales/ruRU.w3mod.
HiveWE packs a staging copy of map.w3x (hard links where possible), so the
working map directory is never modified.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_l10n  # noqa: E402


def run(*args: str) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def stage_map(locale: str, stage: Path) -> list[str]:
    """Mirror map.w3x into stage and overwrite the base files with the locale's staged files."""
    if stage.exists():
        shutil.rmtree(stage)
    for source_dir, dirs, files in os.walk(wc3_l10n.MAP):
        target_dir = stage / Path(source_dir).relative_to(wc3_l10n.MAP)
        target_dir.mkdir(parents=True, exist_ok=True)
        for name in files:
            source, target = Path(source_dir) / name, target_dir / name
            try:
                os.link(source, target)
            except OSError:
                shutil.copy2(source, target)
    staged = wc3_l10n.STAGE_DIR / locale
    replaced = []
    for source in sorted(path for path in staged.rglob("*") if path.is_file()):
        relative = source.relative_to(staged)
        target = stage / relative
        if not target.is_file():
            raise SystemExit(f"staged locale file has no base counterpart in map.w3x: {relative}")
        target.unlink()  # break the hard link before writing
        shutil.copyfile(source, target)
        replaced.append(relative.as_posix())
    return replaced


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hivewe", required=True, type=Path, help="path to HiveWE_cli.exe")
    parser.add_argument("--stormlib", type=Path, help="path to StormLib.dll used to verify the result")
    parser.add_argument("--locale", default="enUS")
    parser.add_argument("--out", type=Path, required=True, help="output .w3x path")
    args = parser.parse_args()
    hivewe = args.hivewe.resolve()
    output = args.out if args.out.is_absolute() else ROOT / args.out
    output = output.resolve()
    if not hivewe.is_file():
        parser.error(f"HiveWE_cli not found: {hivewe}")
    stormlib = args.stormlib.resolve() if args.stormlib else next(
        (candidate for candidate in (hivewe.parent / "StormLib.dll",
                                     ROOT / ".cache/hivewe-build/Release/StormLib.dll") if candidate.is_file()),
        None)
    if stormlib is None:
        parser.error("StormLib.dll not found next to HiveWE or in .cache/hivewe-build/Release; pass --stormlib")
    config, _, _ = wc3_l10n.locale_config(args.locale)
    if not config.get("base"):
        parser.error(f"{args.locale} is not the base locale; only the base locale is packaged by this script")
    # Warcraft III does not read an LF-only WTS: every TRIGSTR shows up raw. git restores the file with LF.
    raw = (wc3_l10n.MAP / "war3map.wts").read_bytes()
    if raw.count(b"\n") != raw.count(b"\r\n"):
        parser.error("map.w3x/war3map.wts must use CRLF line endings; Warcraft III shows raw TRIGSTR_ keys otherwise")

    run(sys.executable, "scripts/wc3_l10n.py", "extract")
    run(sys.executable, "scripts/wc3_l10n.py", "check", "--locale", args.locale, "--no-output")
    run(sys.executable, "scripts/wc3_l10n.py", "build", "--locale", args.locale)
    run(sys.executable, "build_map_lua.py")
    run(sys.executable, "scripts/wc3_l10n.py", "check", "--locale", args.locale)
    stage = ROOT / ".cache/l10n-stage" / "map.w3x"
    replaced = stage_map(args.locale, stage)
    print("staged base files:", ", ".join(replaced), flush=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        run(str(hivewe), "build-map", "--map", str(stage), "--out", str(output))
    finally:
        shutil.rmtree(stage.parent, ignore_errors=True)
    run(sys.executable, "scripts/verify_localized_map.py", "--archive", str(output),
        "--stormlib", str(stormlib), "--locale", args.locale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
