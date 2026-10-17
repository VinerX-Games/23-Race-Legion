"""Compact code queries, environment diagnosis and change checks."""
import argparse
import importlib.util
import json
import sys
import shutil
from pathlib import Path

from wc3_project import ROOT, SPLIT, settings, load_sections, index, locate_offset, digest, read


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def register(parsers):
    for command in ("symbol", "refs", "context"):
        parser = parsers.add_parser(command, help="Bounded Lua source query")
        parser.add_argument("query")
        parser.add_argument("--json", action="store_true")
        parser.add_argument("--limit", type=positive, default=10)
        parser.add_argument("--max-lines", type=positive, default=40)
    parser = parsers.add_parser("doctor", help="Diagnose paths and dependencies")
    parser.add_argument("--json", action="store_true")
    parser = parsers.add_parser("check", help="Strict checks for a change type; never rebuilds implicitly")
    parser.add_argument("--kind", choices=("lua", "ai", "objects", "docs", "release"), default="lua")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-lines", type=positive, default=8)
    parser.add_argument("--timeout", type=positive, default=180)
    parser = parsers.add_parser("audit", help="Run static audits and compare explicit baseline")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--update-baseline", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-lines", type=positive, default=8)


def query(command, needle, limit=10, max_lines=40):
    sections = load_sections()
    data = index(sections)
    text = "".join(s["text"] for s in sections)
    if command == "refs":
        offsets = data["refs"].get(needle, [])
        rows = [{**locate_offset(sections, offset), "built_line": text[:offset].count("\n") + 1}
                for offset in offsets[:limit]]
        return {"ok": True, "sha256": data["sha256"], "count": len(offsets), "results": rows}
    functions = sorted([f for f in data["functions"] if needle.lower() in f["name"].lower()],
                       key=lambda f: (f["name"] != needle, f["start_offset"]))
    rows = []
    budget = max_lines
    for function in functions[:limit]:
        row = {"name": function["name"], **locate_offset(sections, function["start_offset"]),
               "built_start": function["start_line"], "built_end": function["end_line"]}
        if command == "context":
            lines = text[function["start_offset"]:function["end_offset"]].splitlines()
            row["code"] = lines[:budget]
            row["truncated"] = len(lines) > budget
            budget -= len(row["code"])
        rows.append(row)
        if command == "context" and budget <= 0:
            break
    return {"ok": True, "sha256": data["sha256"], "count": len(functions), "results": rows}


def doctor():
    config = settings()
    checks = {key: Path(value).exists() for key, value in config.items()}
    dependencies = {name: importlib.util.find_spec(name) is not None for name in ("lupa", "luaparser")}
    errors = []
    try:
        sections = load_sections()
        built = ROOT / "map.w3x/war3map.lua"
        sync = built.exists() and digest(read(built)) == digest("".join(s["text"] for s in sections))
    except (OSError, ValueError, KeyError) as exc:
        sync = False; errors.append(str(exc))
    return {"ok": all(checks[k] for k in ("map", "warcraft", "cli")) and all(dependencies.values()) and sync,
            "paths": config, "exists": checks, "dependencies": dependencies, "source_sync": sync,
            "optional_features": {"models": checks["model_cli"] and checks["mdlxl_home"] and bool(shutil.which("node")),
                                  "placed_pathing": importlib.util.find_spec("PIL") is not None and checks["model_cli"]},
            "errors": errors, "python": sys.executable}


def dispatch(args):
    if args.command in ("symbol", "refs", "context"):
        result = query(args.command, args.query, args.limit, args.max_lines)
    elif args.command == "doctor":
        result = doctor()
    else:
        from wc3_checks import verify, audit, present, run_check
        if args.command == "audit":
            report = audit(args.baseline, args.update_baseline)
        elif args.kind == "docs":
            report = {"ok": True, "checks": [], "note": "Documentation change: review links and command examples."}
        elif args.kind == "objects":
            check = run_check("validate-map", [sys.executable, str(ROOT / "scripts/wc3_hivewe.py"),
                                               "validate-map", "--json"], args.timeout)
            report = {"ok": check["ok"], "checks": [check], "in_game_required": True}
        else:
            report = verify(args.timeout)
            report["in_game_required"] = True
        return present(report, args.json, args.max_lines, ROOT / f".cache/wc3/{args.command}.json")
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    elif "results" in result:
        print(f"Matches: {result['count']}; showing {len(result['results'])}; sha256={result['sha256']}")
        for row in result["results"]:
            print(f"{row['file']}:{row['line']} {row.get('name', '')}")
            for line in row.get("code", []):
                print(line[:500])
            if row.get("truncated"):
                print("... output limited; increase --max-lines")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1
