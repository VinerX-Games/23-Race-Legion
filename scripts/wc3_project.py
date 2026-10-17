"""Shared project paths, manifest reader, source map and Lua symbol index."""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPLIT = ROOT / "map.w3x/_lua/monolith_split"
CACHE = ROOT / ".cache/wc3"


def read(path):
    return Path(path).read_text(encoding="utf-8-sig")


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def settings():
    path = ROOT / "wc3.local.json"
    local = json.loads(read(path)) if path.exists() else {}
    defaults = {"map": str(ROOT / "map.w3x"), "warcraft": "F:/Games/Warcraft III",
                "cli": "F:/WARCRAFT III/WARCRAFT_SOFT/HiveWE/HiveWE_cli.exe",
                "custom_data": str(Path(os.environ.get("USERPROFILE", str(Path.home()))) /
                                   "Documents/Warcraft III/CustomMapData"),
                "model_cli": "F:/Gemini_Test/tools/mdlxl-cli/mdlxl-cli.mjs",
                "mdlxl_home": "F:/WARCRAFT III/WARCRAFT_SOFT/MDLxL"}
    env = {"map": "WC3_MAP", "warcraft": "WC3_WARCRAFT", "cli": "HIVEWE_CLI",
           "custom_data": "WC3_CUSTOM_DATA", "model_cli": "WC3_MODEL_CLI", "mdlxl_home": "MDLXL_HOME"}
    return {key: str(Path(os.environ.get(env[key]) or local.get(key) or value).resolve())
            for key, value in defaults.items()}


def load_sections(split=SPLIT):
    split = Path(split)
    manifest = json.loads(read(split / "manifest.json"))
    sections, seen, offset, line = [], set(), 0, 1
    root = (split / "sections").resolve()
    for entry in manifest["sections"]:
        name = entry["file"]
        path = (root / name).resolve()
        if not path.is_relative_to(root) or name in seen:
            raise ValueError(f"Unsafe or duplicate manifest entry: {name}")
        seen.add(name)
        text = read(path)  # missing sections are errors, never silently skipped
        sections.append({"file": name, "full_path": str(path), "text": text,
                         "start_offset": offset, "end_offset": offset + len(text),
                         "start_line": line,
                         "end_line": line + text.count("\n") - int(text.endswith("\n")),
                         "lines": text.splitlines()})
        offset += len(text)
        line += text.count("\n")
    return sections


def source_map(sections):
    text = "".join(s["text"] for s in sections)
    return {"schema_version": 1, "sha256": digest(text),
            "sections": [{**{k: s[k] for k in ("file", "start_offset", "end_offset",
                                               "start_line", "end_line")},
                          "sha256": digest(s["text"])} for s in sections]}


def map_line(line, split=SPLIT, built=None, saved_map=None, expected_hash=None, context=5):
    if line < 1 or not 0 <= context <= 100:
        raise ValueError("line must be positive; context must be 0..100")
    sections = load_sections(split)
    mapping = json.loads(read(saved_map)) if saved_map else source_map(sections)
    if expected_hash and mapping["sha256"] != expected_hash:
        raise ValueError("Source map does not match the requested build hash")
    if built and not saved_map and digest(read(built)) != mapping["sha256"]:
        raise ValueError("Source/output mismatch; use the source map from the actual probe build")
    results = []
    by_name = {s["file"]: s for s in sections}
    for entry in mapping["sections"]:
        if entry["end_offset"] > entry["start_offset"] and entry["start_line"] <= line <= entry["end_line"]:
            local_line = line - entry["start_line"] + 1
            current = by_name.get(entry["file"])
            stale = not current or digest(current["text"]) != entry.get("sha256")
            row = {"file": entry["file"], "line": local_line, "stale_source": stale, "context": []}
            if current and not stale:
                row["path"] = current["full_path"]
                start = max(0, local_line - 1 - context)
                end = min(len(current["lines"]), local_line + context)
                row["context"] = [{"line": i + 1, "text": current["lines"][i]} for i in range(start, end)]
            results.append(row)
    if not results:
        raise ValueError(f"Line {line} outside source map")
    return {"ok": True, "sha256": mapping["sha256"], "built_line": line, "results": results}


# Ignore comments and strings including long-bracket forms before indexing code.
TOKEN = re.compile(r'--\[(=*)\[.*?\]\1\]|--[^\n]*|\[(=*)\[.*?\]\2\]|'
                   r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|[A-Za-z_]\w*|\S', re.S)
IDENT = re.compile(r"[A-Za-z_]\w*$")


def lua_tokens(text):
    line, last = 1, 0
    for match in TOKEN.finditer(text):
        line += text[last:match.start()].count("\n")
        value = match.group()
        if not (value.startswith("--") or value[0] in "\"'" or
                re.match(r"\[=*\[", value)):
            yield value, line, match.start()
        line += value.count("\n")
        last = match.end()


def build_index(sections):
    text = "".join(s["text"] for s in sections)
    toks = list(lua_tokens(text))
    functions, stack, refs = [], [], {}
    for i, (token, line, offset) in enumerate(toks):
        if IDENT.fullmatch(token):
            refs.setdefault(token, []).append(offset)
        if token == "function":
            j = i + 1
            name_parts = []
            while j < len(toks) and toks[j][0] != "(":
                name_parts.append(toks[j][0]); j += 1
            name = "".join(name_parts)
            if not name and i >= 2 and toks[i - 1][0] == "=":
                k = i - 2
                name_parts = [toks[k][0]]
                while k >= 2 and toks[k - 1][0] in (".", ":"):
                    name_parts[:0] = [toks[k - 2][0], toks[k - 1][0]]; k -= 2
                name = "".join(name_parts)
            info = {"name": name, "start_offset": offset, "start_line": line}
            stack.append(("function", info))
        elif token in ("if", "do", "repeat"):
            stack.append((token, None))
        elif token in ("end", "until") and stack:
            kind, info = stack.pop()
            if kind == "function":
                info.update(end_offset=offset + len(token), end_line=line)
                if info["name"]:
                    functions.append(info)
    return {"schema_version": 2, "sha256": digest(text), "functions": functions, "refs": refs}


def index(sections, cache=CACHE):
    text = "".join(s["text"] for s in sections)
    key = digest(text)
    path = Path(cache) / f"index-v2-{key}.json"
    try:
        data = json.loads(read(path))
        if data.get("schema_version") == 2 and data.get("sha256") == key:
            return data
    except (OSError, ValueError):
        pass
    data = build_index(sections)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)
    return data


def locate_offset(sections, offset):
    for sec in sections:
        if sec["start_offset"] <= offset < sec["end_offset"]:
            local = offset - sec["start_offset"]
            return {"file": sec["file"], "line": sec["text"][:local].count("\n") + 1,
                    "path": sec["full_path"]}
    raise ValueError(f"Offset outside source: {offset}")
