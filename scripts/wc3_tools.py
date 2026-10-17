#!/usr/bin/env python3
"""
WC3 Codebase & Search Utility (Token-Optimized)
Provides ultra-fast symbol search, war3map.lua line mapping to split sections,
rawcode lookups, and fast build verification without context explosion.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPLIT_DIR = REPO_ROOT / "map.w3x" / "_lua" / "monolith_split"
SECTIONS_DIR = SPLIT_DIR / "sections"
MANIFEST_PATH = SPLIT_DIR / "manifest.json"
WAR3MAP_LUA = REPO_ROOT / "map.w3x" / "war3map.lua"


def get_sections_info():
    from wc3_project import load_sections
    return load_sections(SPLIT_DIR)


def cmd_map_line(target_line: int, context_lines: int = 5, saved_map=None, expected_hash=None, json_output=False):
    from wc3_project import map_line
    try:
        report = map_line(target_line, SPLIT_DIR, WAR3MAP_LUA, saved_map, expected_hash, context_lines)
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    if json_output:
        print(json.dumps(report, ensure_ascii=False))
    else:
        print(f"build sha256={report['sha256']}")
        for row in report["results"]:
            print(f"{row.get('path', row['file'])}:{row['line']} (built line {target_line})")
            if row["stale_source"]:
                print("Source changed since this snapshot; showing original location without current context.")
            for item in row["context"]:
                print(f"{'>>' if item['line'] == row['line'] else '  '} {item['line']}: {item['text']}")
    return 0


def cmd_find_symbol(query: str, symbol_type: str = "all", limit: int = 25):
    """Searches for symbol definitions across sections without dumping bodies."""
    sections = get_sections_info()
    q_lower = query.lower()
    matches = []

    func_re = re.compile(r"^\s*(?:local\s+)?function\s+([A-Za-z0-9_.:]+)\s*\((.*?)\)", re.IGNORECASE)
    assign_func_re = re.compile(r"^\s*([A-Za-z0-9_.:]+)\s*=\s*function\s*\((.*?)\)", re.IGNORECASE)
    var_re = re.compile(r"^\s*(?:local\s+)?([A-Za-z0-9_]+)\s*=", re.IGNORECASE)

    for sec in sections:
        for idx, line in enumerate(sec["lines"]):
            l_num = idx + 1
            # Check function definition
            m_fn = func_re.match(line)
            if m_fn and symbol_type in ("all", "func"):
                name, args = m_fn.group(1), m_fn.group(2)
                if q_lower in name.lower():
                    matches.append({
                        "file": sec["file"],
                        "line": l_num,
                        "kind": "function",
                        "sig": f"function {name}({args})",
                        "text": line.strip()
                    })
                    continue

            m_afn = assign_func_re.match(line)
            if m_afn and symbol_type in ("all", "func"):
                name, args = m_afn.group(1), m_afn.group(2)
                if q_lower in name.lower():
                    matches.append({
                        "file": sec["file"],
                        "line": l_num,
                        "kind": "function",
                        "sig": f"{name} = function({args})",
                        "text": line.strip()
                    })
                    continue

            if symbol_type in ("all", "var"):
                m_var = var_re.match(line)
                if m_var:
                    name = m_var.group(1)
                    if q_lower in name.lower():
                        matches.append({
                            "file": sec["file"],
                            "line": l_num,
                            "kind": "var",
                            "sig": line.strip()[:80],
                            "text": line.strip()
                        })

    if not matches:
        print(f"No definitions found matching '{query}'.")
        return 0

    print(f"Found {len(matches)} match(es) for '{query}' (showing up to {limit}):")
    for m in matches[:limit]:
        print(f"- [{m['kind']}] {m['file']}:{m['line']} -> {m['sig']}")
    if len(matches) > limit:
        print(f"... and {len(matches) - limit} more.")
    return 0


def cmd_find_rawcode(rawcode: str, limit: int = 20):
    """Searches for usage of a Warcraft FourCC rawcode (e.g. h014, A0IQ) in split sections."""
    sections = get_sections_info()
    matches = []
    
    # Try raw string or FourCC hex representation
    variants = [rawcode, f"FourCC('{rawcode}')", f'FourCC("{rawcode}")', f"'{rawcode}'", f'"{rawcode}"']

    for sec in sections:
        for idx, line in enumerate(sec["lines"]):
            if any(v in line for v in variants):
                matches.append({
                    "file": sec["file"],
                    "line": idx + 1,
                    "text": line.strip()
                })

    if not matches:
        print(f"No occurrences of rawcode '{rawcode}' found.")
        return 0

    print(f"Found {len(matches)} occurrence(s) of '{rawcode}' (showing up to {limit}):")
    for m in matches[:limit]:
        print(f"- {m['file']}:{m['line']} -> {m['text'][:100]}")
    if len(matches) > limit:
        print(f"... and {len(matches) - limit} more.")
    return 0


def cmd_verify():
    from wc3_checks import verify, present
    return present(verify(), artifact=REPO_ROOT / ".cache/wc3/verify.json")


def main():
    parser = argparse.ArgumentParser(description="WC3 Token-Efficient Codebase Utility")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # map-line / line
    p_line = subparsers.add_parser("line", aliases=["map-line"], help="Map war3map.lua line to split section")
    p_line.add_argument("line", type=int, help="Line number in war3map.lua")
    p_line.add_argument("-c", "--context", type=int, default=5, help="Number of context lines")

    p_line.add_argument("--source-map", type=Path)
    p_line.add_argument("--build-hash")
    p_line.add_argument("--json", action="store_true")

    # find / symbol
    p_find = subparsers.add_parser("find", aliases=["find-func"], help="Search symbol/function definition")
    p_find.add_argument("query", type=str, help="Symbol or function name query")
    p_find.add_argument("-t", "--type", choices=["all", "func", "var"], default="all", help="Symbol type")
    p_find.add_argument("-l", "--limit", type=int, default=25, help="Max matches to display")

    # rawcode
    p_raw = subparsers.add_parser("rawcode", aliases=["find-rawcode"], help="Find FourCC rawcode usages")
    p_raw.add_argument("code", type=str, help="FourCC code (e.g. h014, A0IQ)")
    p_raw.add_argument("-l", "--limit", type=int, default=20, help="Max matches to display")

    # verify
    subparsers.add_parser("verify", help="Run build sync, syntax check, and unit tests")

    # build
    subparsers.add_parser("build", help="Rebuild war3map.lua from split sections")

    from wc3_commands import register, dispatch
    register(subparsers)
    args = parser.parse_args()
    if args.command in ("doctor", "symbol", "refs", "context", "audit", "check"):
        return dispatch(args)

    if args.command in ("line", "map-line"):
        return cmd_map_line(args.line, args.context, args.source_map, args.build_hash, args.json)
    elif args.command in ("find", "find-func"):
        return cmd_find_symbol(args.query, args.type, args.limit)
    elif args.command in ("rawcode", "find-rawcode"):
        return cmd_find_rawcode(args.code, args.limit)
    elif args.command == "verify":
        return cmd_verify()
    elif args.command == "build":
        cmd = [sys.executable, str(REPO_ROOT / "build_map_lua.py")]
        return subprocess.run(cmd).returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
