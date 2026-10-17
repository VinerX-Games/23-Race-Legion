#!/usr/bin/env python3
"""
HiveWE CLI Python Wrapper & Token-Optimized Inspector
Auto-locates HiveWE_cli.exe, injects canonical map & Warcraft III paths,
resolves TRIGSTR_* from war3map.wts, and formats output into compact Markdown.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
from wc3_project import settings

CONFIG = settings()
DEFAULT_MAP = Path(CONFIG["map"])
DEFAULT_WARCRAFT = Path(CONFIG["warcraft"])
WTS_PATH = DEFAULT_MAP / "war3map.wts"

# Known potential locations for HiveWE_cli.exe
CANDIDATE_PATHS = [
    Path(CONFIG["cli"]),
    Path(os.environ.get("HIVEWE_CLI", "")),
    Path("F:/WARCRAFT III/WARCRAFT_SOFT/HiveWE/HiveWE_cli.exe"),
    Path("F:/WARCRAFT III/WARCRAFT_SOFT/HiveWE_backup_2026-10-03/HiveWE_cli.exe"),
    Path("C:/Games/HiveWE_VinerX_Edition/build/Release/Release/HiveWE_cli.exe"),
]

_WTS_CACHE: dict[int, str] | None = None
_WTS_CACHE_KEY = None


def clean_wc3_string(s: str) -> str:
    """Removes WC3 color tags |cff... and |r, plus strips excess whitespace."""
    if not isinstance(s, str):
        return str(s)
    cleaned = re.sub(r"\|c[0-9a-fA-F]{8}", "", s)
    cleaned = cleaned.replace("|r", "").replace("|R", "").strip()
    return cleaned


def load_wts_strings(path=None) -> dict[int, str]:
    """Parses war3map.wts into {string_id: text} with caching."""
    global _WTS_CACHE
    global _WTS_CACHE_KEY
    source = Path(path or WTS_PATH)
    if not source.is_file():
        return {}
    from hashlib import sha256
    raw = source.read_bytes()
    key = (str(source.resolve()), sha256(raw).hexdigest())
    if _WTS_CACHE is not None and key == _WTS_CACHE_KEY:
        return _WTS_CACHE

    _WTS_CACHE = {}
    _WTS_CACHE_KEY = key

    try:
        text = raw.decode("utf-8-sig")
    except Exception:
        text = raw.decode("cp1251")

    # Fast line-based parsing of WTS format:
    # STRING <id>
    # {
    # <lines>
    # }
    lines = text.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()
        if line.startswith("STRING "):
            try:
                sid = int(line[7:].strip())
            except ValueError:
                i += 1
                continue
            i += 1
            # Skip until {
            while i < n and lines[i].strip() != "{":
                i += 1
            i += 1
            content = []
            while i < n and lines[i].strip() != "}":
                content.append(lines[i])
                i += 1
            _WTS_CACHE[sid] = "\n".join(content)
        i += 1
    return _WTS_CACHE


def resolve_trigstr(val: str, path=None) -> str:
    """Replaces TRIGSTR_XXXX with actual text from war3map.wts."""
    if not isinstance(val, str) or not val.startswith("TRIGSTR_"):
        return val
    try:
        sid = int(val[8:])
        wts = load_wts_strings(path)
        if sid in wts:
            return clean_wc3_string(wts[sid])
    except ValueError:
        pass
    return val


def find_hivewe_cli() -> Path:
    """Finds the working HiveWE_cli.exe executable."""
    for cand in CANDIDATE_PATHS:
        if cand and cand.is_file():
            return cand.resolve()

    which_path = shutil.which("HiveWE_cli") or shutil.which("HiveWE_cli.exe")
    if which_path:
        return Path(which_path).resolve()

    raise FileNotFoundError(
        "Could not find HiveWE_cli.exe!\n"
        "Set HIVEWE_CLI environment variable or place HiveWE_cli in F:/WARCRAFT III/WARCRAFT_SOFT/HiveWE/"
    )


def run_cli_json(cmd_args: list[str]) -> dict:
    """Executes HiveWE_cli with arguments and parses JSON response."""
    cli_exe = find_hivewe_cli()
    full_cmd = [str(cli_exe)] + cmd_args
    try:
        proc = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120
        )
    except Exception as e:
        return {"ok": False, "error": f"Failed to execute HiveWE_cli: {e}"}

    stdout = proc.stdout.strip()
    if not stdout:
        if proc.returncode != 0:
            return {"ok": False, "error": f"Process exited with {proc.returncode}: {proc.stderr}"}
        return {"ok": True, "raw": ""}

    try:
        data = json.loads(stdout)
        if not isinstance(data, dict):
            return {"ok": False, "error": "CLI response must be a JSON object"}
        if proc.returncode != 0:
            data["ok"] = False
            data.setdefault("error", proc.stderr.strip() or f"CLI exit code {proc.returncode}")
        return data
    except json.JSONDecodeError:
        return {"ok": proc.returncode == 0, "raw": stdout, "stderr": proc.stderr}


def cmd_object(obj_id: str, obj_type: str = "unit", show_all: bool = False, map_path: Path = DEFAULT_MAP):
    """Fetches and displays a compact object summary with resolved names."""
    args = ["get-object", "--map", str(map_path), "--type", obj_type, "--id", obj_id]
    if DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])

    data = run_cli_json(args)
    if not data.get("ok"):
        alt_types = [t for t in ["ability", "item", "upgrade", "doodad", "destructible", "buff"] if t != obj_type]
        for alt in alt_types:
            alt_args = ["get-object", "--map", str(map_path), "--type", alt, "--id", obj_id]
            if DEFAULT_WARCRAFT.is_dir():
                alt_args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])
            alt_data = run_cli_json(alt_args)
            if alt_data.get("ok"):
                data = alt_data
                obj_type = alt
                break

    if not data.get("ok"):
        print(f"Error fetching object '{obj_id}': {data.get('error') or data.get('raw')}")
        return 1

    obj = data.get("object", {})
    if not obj and "fields" in data:
        obj = data["fields"]

    # Filter and resolve
    resolved_fields = {}
    for k, v in obj.items():
        if v is not None and str(v).strip() != "" and str(v).strip() != "_":
            s_val = str(v)
            if s_val.startswith("TRIGSTR_"):
                s_val = resolve_trigstr(s_val)
            else:
                s_val = clean_wc3_string(s_val)
            resolved_fields[k] = s_val

    name = resolved_fields.get("name", obj_id)
    suffix = resolved_fields.get("editorsuffix") or resolved_fields.get("suffix", "")
    suffix_str = f" ({suffix})" if suffix else ""

    print(f"=== Object [{obj_id}] {name}{suffix_str} ===")
    print(f"Type: {obj_type} | Race: {resolved_fields.get('race', 'unknown')}")

    # Core stats
    core_keys = [
        ("HP / Mana", lambda f: f"{f.get('hp', '-')} / {f.get('mana0', '-')}" if 'hp' in f or 'mana0' in f else None),
        ("Armor", lambda f: f"{f.get('def', '-')} ({f.get('deftype', '-')})" if 'def' in f or 'deftype' in f else None),
        ("Speed", lambda f: f.get('spd')),
        ("Damage", lambda f: f"{f.get('mindmg1', '?')}-{f.get('maxdmg1', '?')} (cool: {f.get('cool1', '-')})" if 'mindmg1' in f else None),
        ("Cost", lambda f: f"Gold: {f.get('goldcost', 0)}, Wood: {f.get('lumbercost', 0)}, BuildTime: {f.get('bldtm', '-')}s" if 'goldcost' in f else None),
        ("Builds", lambda f: f.get('builds')),
        ("Trains", lambda f: f.get('train')),
        ("Abilities", lambda f: f.get('abillist')),
        ("Hero Abils", lambda f: f.get('heroabillist')),
        ("Upgrades", lambda f: f.get('upgrades')),
        ("Reqs", lambda f: f.get('reqs')),
        ("Model", lambda f: f.get('file')),
        ("Icon", lambda f: f.get('art')),
        ("Tip", lambda f: f.get('tip')),
        ("Ubertip", lambda f: f.get('ubertip')),
    ]

    for label, extractor in core_keys:
        val = extractor(resolved_fields)
        if val and str(val).strip() and str(val).strip() != "- / -":
            print(f"- {label:12s}: {val}")

    if show_all:
        print("\nAll Fields:")
        for k, v in sorted(resolved_fields.items()):
            print(f"  {k:15s}: {v}")
    return 0


def cmd_search(query: str, obj_type: str = "unit", limit: int = 25, map_path: Path = DEFAULT_MAP):
    """Searches objects by substring and outputs a compact Markdown table."""
    args = ["search-objects", "--map", str(map_path), "--type", obj_type, "--query", query, "--limit", str(limit)]
    if DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])

    data = run_cli_json(args)
    if not data.get("ok"):
        print(f"Search error: {data.get('error') or data.get('raw')}")
        return 1

    results = data.get("matches", []) or data.get("results", []) or data.get("objects", [])
    if not results:
        print(f"No objects found matching '{query}' in {obj_type}.")
        return 0

    print(f"=== Found {len(results)} object(s) matching '{query}' ({obj_type}) ===")
    print(f"| ID   | Type | Name | Suffix |")
    print(f"| :--- | :--- | :--- | :----- |")
    for r in results:
        r_id = r.get("id", "")
        r_name = clean_wc3_string(resolve_trigstr(r.get("name", "")))
        r_suffix = clean_wc3_string(resolve_trigstr(r.get("suffix", "")))
        print(f"| `{r_id}` | {obj_type} | {r_name} | {r_suffix} |")
    return 0


def cmd_race(suffix: str, obj_type: str = "all", map_path: Path = DEFAULT_MAP):
    """Inspects all objects belonging to a race suffix."""
    args = ["list-race-objects", "--map", str(map_path), "--suffix", suffix, "--type", obj_type]
    if DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])

    data = run_cli_json(args)
    if not data.get("ok"):
        print(f"Race lookup error: {data.get('error') or data.get('raw')}")
        return 1

    objects = data.get("objects", [])
    if not objects:
        print(f"No objects found for race suffix '{suffix}'.")
        return 0

    parsed = []
    for item in objects:
        if isinstance(item, dict) and "line" in item:
            parts = item["line"].split(None, 2)
            if len(parts) >= 3:
                parsed.append({"id": parts[0], "type": parts[1], "name": resolve_trigstr(parts[2])})
            elif len(parts) == 2:
                parsed.append({"id": parts[0], "type": parts[1], "name": ""})
            else:
                parsed.append({"id": item["line"][:4], "type": "unknown", "name": item["line"][4:].strip()})
        elif isinstance(item, dict):
            parsed.append({
                "id": item.get("id", ""),
                "type": item.get("type", "unknown"),
                "name": resolve_trigstr(item.get("name", ""))
            })

    buildings = [o for o in parsed if o.get("type") == "building"]
    units = [o for o in parsed if o.get("type") == "unit"]
    heroes = [o for o in parsed if o.get("type") == "hero"]
    others = [o for o in parsed if o.get("type") not in ("building", "unit", "hero")]

    print(f"=== Race: {suffix} (Total: {len(parsed)}) ===")
    if buildings:
        print(f"\nBuildings ({len(buildings)}):")
        for b in buildings:
            print(f"- `{b['id']}`: {clean_wc3_string(b['name'])}")
    if units:
        print(f"\nUnits ({len(units)}):")
        for u in units:
            print(f"- `{u['id']}`: {clean_wc3_string(u['name'])}")
    if heroes:
        print(f"\nHeroes ({len(heroes)}):")
        for h in heroes:
            print(f"- `{h['id']}`: {clean_wc3_string(h['name'])}")
    if others:
        print(f"\nOther ({len(others)}):")
        for o in others:
            print(f"- `{o['id']}`: {clean_wc3_string(o['name'])}")
    return 0


def cmd_races(map_path: Path = DEFAULT_MAP):
    """Lists all race suffixes detected in the map."""
    args = ["list-all-races", "--map", str(map_path)]
    if DEFAULT_WARCRAFT.is_dir():
        args.extend(["--warcraft", str(DEFAULT_WARCRAFT)])

    data = run_cli_json(args)
    if not data.get("ok"):
        print(f"Failed to list races: {data.get('error') or data.get('raw')}")
        return 1

    races = data.get("races", [])
    print(f"=== All Map Races ({len(races)}) ===")
    print(f"| Suffix | Bld | Unt | Hero | Workers |")
    print(f"| :----- | :-- | :-- | :--- | :------ |")
    for r in races:
        worker_strs = []
        for w in r.get("workers", []):
            worker_strs.append(resolve_trigstr(w))
        workers = ", ".join(worker_strs)
        if len(workers) > 35:
            workers = workers[:32] + "..."
        print(f"| {r.get('suffix')} | {r.get('buildings', 0)} | {r.get('units', 0)} | {r.get('heroes', 0)} | {workers} |")
    return 0


def cmd_probe(wait: int = 300, click_after: int = 60, bridge_script: str = "",
              probe_log: str = "23Race_probe_log.pld", keep_open: bool = True,
              map_path: Path = DEFAULT_MAP):
    """Runs probe-map with canonical parameters."""
    if wait <= 0 or click_after < 0 or click_after >= wait:
        print("Error: wait must be positive and click must be inside the probe window")
        return 1
    cli_exe = find_hivewe_cli()
    cmd = [
        str(cli_exe), "probe-map",
        "--map", str(map_path),
        "--warcraft", str(DEFAULT_WARCRAFT),
        "--args", "-window -nowfpause",
        "--click-after", str(click_after),
        "--wait", str(wait),
        "--probe-log", probe_log
    ]
    if bridge_script:
        cmd.extend(["--bridge-script", bridge_script])
    if keep_open:
        cmd.append("--keep-open")

    print(f"Launching probe-map test (wait={wait}s, click={click_after}s)...")
    print(f"Command: {' '.join(cmd)}")
    return subprocess.run(cmd).returncode


def cmd_raw(raw_args: list[str]):
    """Passes any raw arguments directly to HiveWE_cli.exe."""
    cli_exe = find_hivewe_cli()
    raw_args = list(raw_args)
    for index, flag in enumerate(raw_args[:-1]):
        if flag in ("--map", "--warcraft", "--out", "--file", "--id-file", "--theirs", "--ancestor"):
            raw_args[index + 1] = str(Path(raw_args[index + 1]).resolve())
    if raw_args and not raw_args[0].startswith("--") and raw_args[0] not in ("help", "capabilities", "list-object-types"):
        if "--map" not in raw_args:
            raw_args += ["--map", str(DEFAULT_MAP)]
        if "--warcraft" not in raw_args:
            raw_args += ["--warcraft", str(DEFAULT_WARCRAFT)]
    cmd = [str(cli_exe)] + raw_args
    return subprocess.run(cmd).returncode


def main():
    parser = argparse.ArgumentParser(description="Token-Optimized HiveWE CLI Wrapper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # object / get
    p_obj = subparsers.add_parser("object", aliases=["get"], help="Inspect object by ID")
    p_obj.add_argument("id", type=str, help="Rawcode ID (e.g. hfoo, h014, A0IQ)")
    p_obj.add_argument("-t", "--type", default="unit", help="Object type (unit, ability, item, upgrade, doodad)")
    p_obj.add_argument("-a", "--all", action="store_true", help="Show all properties")

    # search
    p_search = subparsers.add_parser("search", help="Search objects by name/substring")
    p_search.add_argument("query", type=str, help="Search string")
    p_search.add_argument("-t", "--type", default="unit", help="Object type")
    p_search.add_argument("-l", "--limit", type=int, default=25, help="Result limit")

    # race
    p_race = subparsers.add_parser("race", help="List all objects of a race suffix")
    p_race.add_argument("suffix", type=str, help="Race suffix name (e.g. Дренеи, Бандиты)")
    p_race.add_argument("-t", "--type", default="all", choices=["all", "building", "unit", "hero"])

    # races
    subparsers.add_parser("races", help="List all detected races in the map")

    # probe
    p_probe = subparsers.add_parser("probe", help="Run probe-map automated game test")
    p_probe.add_argument("--wait", type=int, default=300, help="Total wait time in seconds")
    p_probe.add_argument("--click", type=int, default=60, help="Click window after N seconds")
    p_probe.add_argument("--bridge-script", type=str, default="", help="Legacy scheduled commands (not consumed by live-only maps)")
    p_probe.add_argument("--log", type=str, default="23Race_probe_log.pld", help="Probe log file name")
    p_probe.add_argument("--close", action="store_true", help="Do not keep window open")

    # raw
    p_raw = subparsers.add_parser("raw", help="Execute raw HiveWE_cli command")
    p_raw.add_argument("args", nargs=argparse.REMAINDER, help="Arguments passed to HiveWE_cli")

    from wc3_object_tools import register, dispatch
    register(subparsers)
    args = parser.parse_args()
    if args.command in ("bulk", "tree", "describe", "diff", "validate-map", "transaction", "recover", "capabilities"):
        return dispatch(args)

    if args.command in ("object", "get"):
        return cmd_object(args.id, args.type, getattr(args, "all", False))
    elif args.command == "search":
        return cmd_search(args.query, args.type, args.limit)
    elif args.command == "race":
        return cmd_race(args.suffix, args.type)
    elif args.command == "races":
        return cmd_races()
    elif args.command == "probe":
        return cmd_probe(wait=args.wait, click_after=args.click, bridge_script=args.bridge_script,
                         probe_log=args.log, keep_open=not args.close)
    elif args.command == "raw":
        return cmd_raw(args.args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
