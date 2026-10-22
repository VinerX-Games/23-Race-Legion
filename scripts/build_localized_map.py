"""Build and package the map after validating locale assets."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
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

    run(sys.executable, "scripts/wc3_l10n.py", "extract")
    run(sys.executable, "scripts/wc3_l10n.py", "check", "--locale", args.locale, "--no-output")
    run(sys.executable, "scripts/wc3_l10n.py", "build", "--locale", args.locale)
    run(sys.executable, "build_map_lua.py")
    run(sys.executable, "scripts/wc3_l10n.py", "check", "--locale", args.locale)
    output.parent.mkdir(parents=True, exist_ok=True)
    run(str(hivewe), "build-map", "--map", str(ROOT / "map.w3x"), "--out", str(output))
    run(sys.executable, "scripts/verify_localized_map.py", "--archive", str(output),
        "--stormlib", str(stormlib), "--locale", args.locale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
