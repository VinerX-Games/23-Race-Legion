"""Inventory, build and validation for 23 Race Forever localizations.

The base WTS stays Russian. A locale build copies every base string and
replaces only entries listed in localization/locales/<locale>/strings.json.
This keeps WTS IDs stable and makes untranslated text fall back to Russian.
"""
from __future__ import annotations

import argparse
import codecs
import hashlib
import json
import re
import struct
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from wc3_object_binary import extended_for, object_records, string_value  # noqa: E402

MAP = ROOT / "map.w3x"
WTS_PATH = MAP / "war3map.wts"
CATALOG_PATH = ROOT / "localization/catalog.json"
UI_SOURCE_PATH = ROOT / "localization/ui/ruRU.json"
LOCALES_DIR = ROOT / "localization/locales"
LUA_OUT = MAP / "_lua/monolith_split/sections/03_localization.lua"
LOCALE_MAP_DIR = MAP / "_Locales"

OBJECT_FILES = (
    ("unit", "w3u"),
    ("ability", "w3a"),
    ("item", "w3t"),
    ("upgrade", "w3q"),
    ("buff", "w3h"),
    ("doodad", "w3d"),
    ("destructible", "w3b"),
)

# Player-visible text fields. Hotkeys, editor suffixes, icons and internal
# identifiers are intentionally absent: translating them breaks the game.
TEXT_FIELDS = {
    "unit": {"unam": "name", "utip": "tip", "utub": "ubertip", "upro": "propernames",
             "uawt": "awaken_tip", "utpr": "revive_tip", "ucun": "propernames_list",
             "ucut": "description"},
    "item": {"unam": "name", "utip": "tip", "utub": "ubertip", "ides": "level_text"},
    "ability": {"anam": "name", "atp1": "tip", "atp2": "tip_off", "aub1": "ubertip",
                "aub2": "ubertip_off", "aut1": "turn_off_tip", "auu1": "turn_off_ubertip",
                "aret": "research_tip", "arut": "research_ubertip"},
    "upgrade": {"gnam": "name", "gtp1": "tip", "gub1": "ubertip"},
    "buff": {"fnam": "name", "ftip": "tip", "fube": "ubertip"},
    "doodad": {"dnam": "name"},
    "destructible": {"bnam": "name"},
}

COLOR = re.compile(r"\|c[0-9a-fA-F]{8}")
FORMAT = re.compile(r"%(?:\d+\$)?[sdifxXc%]")
CYRILLIC = re.compile(r"[А-Яа-яЁё]")
LOC_CALL = re.compile(r"\bLoc\(\s*[\"']([^\"']+)[\"']\s*\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_json(path: Path):
    return json.loads(read_text(path))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_wts(path: Path = WTS_PATH):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    strings, order, current, buf = {}, [], None, []
    for line in text.splitlines():
        match = re.match(r"^STRING (\d+)\s*$", line)
        if match:
            if current is not None:
                raise ValueError(f"unterminated STRING {current} in {path}")
            current, buf = int(match.group(1)), []
            continue
        if current is None:
            continue
        if line.strip() == "{" and not buf:
            continue
        if line.strip() == "}":
            strings[current] = "\n".join(buf)
            order.append(current)
            current, buf = None, []
            continue
        buf.append(line)
    if current is not None:
        raise ValueError(f"unterminated STRING {current} in {path}")
    newline = "\r\n" if b"\r\n" in raw else "\n"
    return strings, {"bom": raw.startswith(codecs.BOM_UTF8), "newline": newline, "order": order}


def dump_wts(strings, meta) -> str:
    newline = meta["newline"]
    order = list(meta.get("order") or [])
    order += sorted(set(strings) - set(order))
    blocks = [f"STRING {sid:03d}{newline}{{{newline}{strings[sid].replace(chr(10), newline)}{newline}}}"
              for sid in order]
    text = (newline * 2).join(blocks) + newline * 2
    return text


def write_wts(path: Path, strings, meta):
    data = (codecs.BOM_UTF8 if meta["bom"] else b"") + dump_wts(strings, meta).encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def race_objects() -> dict[str, list[str]]:
    index = read_json(ROOT / "docs/techtree/index.json")
    result = {}
    for entry in index.get("races", []):
        tree = read_json(ROOT / "docs/techtree" / entry["file"])
        for rawcode in tree.get("objects", {}):
            races = result.setdefault(rawcode, [])
            if entry["race"] not in races:
                races.append(entry["race"])
    return {code: sorted(races) for code, races in result.items()}


def object_entry_key(rawcode, kind, field, level, skin) -> str:
    parts = [rawcode, kind, field]
    if level:
        parts.append(str(level))
    key = "/".join(parts)
    return key + ("@hd" if skin else "")


def extract_catalog():
    strings, _ = load_wts()
    races = race_objects()
    entries, issues = {}, []
    sources = {"wts": WTS_PATH.name, "objects": {}}
    for kind, ext in OBJECT_FILES:
        for prefix in ("war3map", "war3mapSkin"):
            name = f"{prefix}.{ext}"
            path = MAP / name
            if not path.is_file():
                continue
            sources["objects"][name] = sha256(path)
            skin = prefix == "war3mapSkin"
            extended = extended_for(name)
            try:
                _, tables = object_records(path.read_bytes(), extended)
            except Exception as error:
                issues.append({"file": name, "issue": f"cannot read object data: {error}"})
                continue
            for table_index, table in enumerate(tables):
                for record in table:
                    rawcode = record["id"]
                    for (tag, level, pointer), raw in record["mods"]:
                        field = TEXT_FIELDS.get(kind, {}).get(tag)
                        if field is None:
                            continue
                        value = string_value(raw, extended)
                        if not value or not value.startswith("TRIGSTR_"):
                            continue
                        sid = int(value[8:])
                        if sid not in strings:
                            issues.append({"file": name, "id": rawcode, "field": field,
                                           "issue": f"missing WTS STRING {sid}"})
                            continue
                        key = object_entry_key(rawcode, kind, field, level, skin)
                        entries[key] = {
                            "key": key,
                            "kind": kind,
                            "id": rawcode,
                            "field": field,
                            "tag": tag,
                            "level": level,
                            "pointer": pointer,
                            "skin": skin,
                            "custom": table_index == 1,
                            "sid": sid,
                            "races": races.get(rawcode, []),
                            "text": strings[sid],
                        }
    sources["wts_sha256"] = sha256(WTS_PATH)
    return {"schema_version": 1, "source": sources,
            "entries": [entries[key] for key in sorted(entries)], "issues": issues}


def format_catalog(catalog) -> str:
    lines = ["{", f'  "schema_version": {catalog["schema_version"]},']
    source = json.dumps(catalog["source"], ensure_ascii=False, indent=2, sort_keys=True)
    lines.append('  "source": ' + source.replace("\n", "\n  ") + ",")
    lines.append('  "entries": [')
    entries = catalog["entries"]
    for index, entry in enumerate(entries):
        comma = "," if index + 1 < len(entries) else ""
        lines.append("    " + json.dumps(entry, ensure_ascii=False, sort_keys=True) + comma)
    lines.append("  ],")
    lines.append('  "issues": ' + json.dumps(catalog.get("issues", []), ensure_ascii=False) + "")
    lines.append("}")
    return "\n".join(lines) + "\n"


def load_catalog():
    return read_json(CATALOG_PATH)


def catalog_is_fresh(catalog) -> bool:
    return CATALOG_PATH.is_file() and read_text(CATALOG_PATH) == format_catalog(catalog)


def locale_config(locale: str):
    path = LOCALES_DIR / locale
    config_path = path / "locale.json"
    if not config_path.is_file():
        raise SystemExit(f"missing locale file: {config_path}")
    data = read_json(config_path)
    translations = {}
    for source in sorted((path / "objects").glob("*.json")):
        for key, value in read_json(source).get("translations", {}).items():
            if key in translations and translations[key] != value:
                raise SystemExit(f"conflicting translation for {key} in {source}")
            translations[key] = value
    data["translations"] = translations
    ui_path = path / "ui.json"
    ui = read_json(ui_path) if ui_path.is_file() else {}
    return data, ui, path


def lua_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r") + '"'


def render_ui_lua(translations: dict[str, dict[str, str]], game_locales=None) -> str:
    game_locales = game_locales or {}
    lines = [
        "-- Generated by scripts/wc3_l10n.py build. Do not edit.",
        "-- Source: localization/ui/ruRU.json and localization/locales/*/ui.json",
        "MapLocale = \"ruRU\"",
        "local GAME_LOCALES = {",
    ]
    for game_locale in sorted(game_locales):
        lines.append(f"    [{lua_quote(game_locale)}] = {lua_quote(game_locales[game_locale])},")
    lines += [
        "}",
        "do",
        "    local locale = GetLocale and GetLocale() or \"ruRU\"",
        "    if GAME_LOCALES[locale] then MapLocale = GAME_LOCALES[locale] end",
        "end",
        "",
        "local UI_STRINGS = {",
    ]
    for locale in sorted(translations):
        lines.append(f"    {locale} = {{")
        for key in sorted(translations[locale]):
            lines.append(f"        [{lua_quote(key)}] = {lua_quote(translations[locale][key])},")
        lines.append("    },")
    lines += [
        "}",
        "",
        "function Loc(key)",
        "    local values = UI_STRINGS[MapLocale] or UI_STRINGS.ruRU",
        "    local text = values[key]",
        "    if text == nil then text = UI_STRINGS.ruRU[key] end",
        "    return text or key",
        "end",
        "",
    ]
    return "\n".join(lines)


def collect_ui():
    source = read_json(UI_SOURCE_PATH)
    tables = {"ruRU": source}
    game_locales = {}
    for config_path in sorted(LOCALES_DIR.glob("*/locale.json")):
        config = read_json(config_path)
        locale = config["locale"]
        ui_path = config_path.parent / "ui.json"
        tables[locale] = {**source, **(read_json(ui_path) if ui_path.is_file() else {})}
        for game_locale in config.get("game_locales", []):
            game_locales[game_locale] = locale
    return tables, game_locales


def resolve_translations(catalog, translations):
    resolved, conflicts = {}, []
    by_key = {entry["key"]: entry for entry in catalog["entries"]}
    for key, entry in by_key.items():
        text = translations.get(key)
        if text is None and entry["skin"]:
            text = translations.get(key.removesuffix("@hd"))
        if text is None:
            text = entry["text"]
        previous = resolved.get(entry["sid"])
        if previous is not None and previous != text:
            conflicts.append({"sid": entry["sid"], "key": key, "other": previous})
        else:
            resolved[entry["sid"]] = text
    return resolved, conflicts


def output_paths(locale: str):
    root = LOCALE_MAP_DIR / f"{locale}.w3mod"
    return root / "war3map.wts", root


def build(locale: str, check: bool = False) -> int:
    catalog = extract_catalog()
    if not catalog_is_fresh(catalog):
        print(json.dumps({"ok": False, "error": "localization/catalog.json is stale; run extract"},
                         ensure_ascii=False, indent=2))
        return 1
    config, locale_ui, locale_dir = locale_config(locale)
    translations = config.get("translations", {})
    resolved, conflicts = resolve_translations(catalog, translations)
    if conflicts:
        print(json.dumps({"ok": False, "conflicts": conflicts[:20]}, ensure_ascii=False, indent=2))
        return 1
    base, meta = load_wts()
    merged = dict(base)
    merged.update(resolved)
    output_wts, output_root = output_paths(locale)
    expected = [(output_wts, (codecs.BOM_UTF8 if meta["bom"] else b"") + dump_wts(merged, meta).encode("utf-8"))]

    # Locale UI files only contain translated keys; merge over the default table.
    ui, game_locales = collect_ui()
    expected.append((LUA_OUT, render_ui_lua(ui, game_locales).encode("utf-8")))

    overlay = locale_dir / "overlay"
    if overlay.is_dir():
        for source in sorted(overlay.rglob("*")):
            if source.is_file():
                data = source.read_bytes()
                if source.suffix.lower() == ".txt":
                    data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
                expected.append((output_root / source.relative_to(overlay), data))

    stale, missing = [], []
    for path, data in expected:
        if not path.is_file():
            missing.append(str(path.relative_to(ROOT)))
        elif path.read_bytes() != data:
            stale.append(str(path.relative_to(ROOT)))
    if check:
        ok = not (stale or missing)
        print(json.dumps({"ok": ok, "stale": stale, "missing": missing,
                          "translated_sids": sum(1 for sid in resolved if resolved[sid] != base.get(sid))},
                         ensure_ascii=False, indent=2))
        return 0 if ok else 1
    for path, data in expected:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({"ok": True, "locale": locale,
                      "wts": str(output_wts.relative_to(ROOT)),
                      "translated_sids": sum(1 for sid in resolved if resolved[sid] != base.get(sid)),
                      "ui_keys": len(ui[locale]), "overlay_files": len(expected) - 2},
                     ensure_ascii=False, indent=2))
    return 0


def check_text(source: str, target: str):
    problems = []
    if COLOR.findall(source) != COLOR.findall(target):
        problems.append("color sequence differs")
    if Counter(FORMAT.findall(source)) != Counter(FORMAT.findall(target)):
        problems.append("format placeholders differ")
    if Counter(re.findall(r"\d+", COLOR.sub("", source))) != Counter(re.findall(r"\d+", COLOR.sub("", target))):
        problems.append("numbers differ")
    if source.count("|n") != target.count("|n"):
        problems.append("line break count differs")
    if source.count("|r") != target.count("|r"):
        problems.append("color reset count differs")
    if CYRILLIC.search(target):
        problems.append("Cyrillic text remains")
    if target[:1].isspace() and not source[:1].isspace():
        problems.append("leading whitespace")
    if target[-1:].isspace() and not source[-1:].isspace():
        problems.append("trailing whitespace")
    return problems


def in_scope(entry, scope) -> bool:
    races = entry.get("races") or []
    return bool(entry.get("custom")) and len(races) == 1 and races[0] in scope


def command_sections(path: Path):
    sections, current = {}, None
    for raw in read_text(path).splitlines():
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            sections[current] = {}
        elif current is not None and "=" in line:
            key, value = line.split("=", 1)
            sections[current][key.strip()] = value
    return sections


def validate_overlay(locale_dir: Path, errors):
    source = MAP / "Units/CommandStrings.txt"
    target = locale_dir / "overlay/Units/CommandStrings.txt"
    if not target.is_file():
        return
    base, translated = command_sections(source), command_sections(target)
    if set(base) != set(translated):
        errors.append({"key": "CommandStrings", "issue": "section list differs from the base file"})
    for section in sorted(set(base) & set(translated)):
        if set(base[section]) != set(translated[section]):
            errors.append({"key": f"CommandStrings/{section}", "issue": "key list differs from the base file"})
            continue
        for key in base[section]:
            left, right = base[section][key], translated[section][key]
            if Counter(FORMAT.findall(left)) != Counter(FORMAT.findall(right)):
                errors.append({"key": f"CommandStrings/{section}/{key}", "issue": "format placeholders differ"})
            if len(re.findall(r"\|c", right)) != len(COLOR.findall(right)):
                errors.append({"key": f"CommandStrings/{section}/{key}", "issue": "malformed color code"})


def validate(locale: str, check_output: bool = True) -> int:
    catalog = extract_catalog()
    if not catalog_is_fresh(catalog):
        print(json.dumps({"ok": False, "error": "localization/catalog.json is stale; run extract"},
                         ensure_ascii=False, indent=2))
        return 1
    config, locale_ui, locale_dir = locale_config(locale)
    translations = config.get("translations", {})
    by_key = {entry["key"]: entry for entry in catalog["entries"]}
    errors, warnings = [], []
    scope = set(config.get("scope_races", []))
    required = {key for key, entry in by_key.items()
                if in_scope(entry, scope) and CYRILLIC.search(entry["text"])}
    for key in sorted(set(translations) - set(by_key)):
        errors.append({"key": key, "issue": "translation key is not in catalog"})
    for key in sorted(required):
        text = translations.get(key)
        if text is None and by_key[key]["skin"]:
            text = translations.get(key.removesuffix("@hd"))
        if text is None:
            errors.append({"key": key, "issue": "missing translation"})
            continue
        entry = by_key[key]
        for problem in check_text(entry["text"], text):
            errors.append({"key": key, "issue": problem})
        if text == entry["text"]:
            errors.append({"key": key, "issue": "translation equals source"})
        if len(text) > len(entry["text"]) * 1.6 + 40:
            warnings.append({"key": key, "issue": "translation is much longer than source"})
    resolved, conflicts = resolve_translations(catalog, translations)
    for conflict in conflicts:
        errors.append({"key": conflict["key"], "issue": f"shared WTS {conflict['sid']} has conflicting translations"})
    source_ui = read_json(UI_SOURCE_PATH)
    for key in sorted(set(source_ui) - set(locale_ui)):
        errors.append({"key": key, "issue": "missing UI translation"})
    for key in sorted(set(locale_ui) - set(source_ui)):
        errors.append({"key": key, "issue": "UI translation key is not in source"})
    for key in sorted(set(source_ui) & set(locale_ui)):
        for problem in check_text(source_ui[key], locale_ui[key]):
            errors.append({"key": key, "issue": problem})
    validate_overlay(locale_dir, errors)
    used = set()
    for path in sorted((MAP / "_lua/monolith_split/sections").rglob("*.lua")):
        used.update(LOC_CALL.findall(read_text(path)))
    for key in sorted(used - set(source_ui)):
        errors.append({"key": key, "issue": "Loc() key is not defined"})
    coverage = {}
    for race in sorted(scope):
        keys = [key for key, entry in by_key.items()
                if in_scope(entry, {race}) and CYRILLIC.search(entry["text"])]
        translated = sum(1 for key in keys if translations.get(key) is not None
                         or (by_key[key]["skin"] and translations.get(key.removesuffix("@hd")) is not None))
        coverage[race] = {"total": len(keys), "translated": translated, "missing": len(keys) - translated}
    build_code = build(locale, check=True) if check_output else 0
    report = {"ok": not errors and build_code == 0, "errors": errors, "warnings": warnings,
              "coverage": coverage, "catalog_entries": len(by_key)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


def extract(check: bool = False) -> int:
    catalog = extract_catalog()
    rendered = format_catalog(catalog)
    stale = not CATALOG_PATH.is_file() or read_text(CATALOG_PATH) != rendered
    if check:
        print(json.dumps({"ok": not stale, "stale": stale,
                          "entries": len(catalog["entries"]), "issues": len(catalog["issues"])},
                         ensure_ascii=False, indent=2))
        return 0 if not stale else 1
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(rendered, encoding="utf-8")
    print(json.dumps({"ok": True, "entries": len(catalog["entries"]),
                      "issues": len(catalog["issues"]), "path": str(CATALOG_PATH.relative_to(ROOT))},
                     ensure_ascii=False, indent=2))
    return 0 if not catalog["issues"] else 1


def status(locale: str = "enUS") -> int:
    catalog = extract_catalog()
    config, locale_ui, _ = locale_config(locale)
    translations = config.get("translations", {})
    scope = set(config.get("scope_races", []))
    rows = {}
    for entry in catalog["entries"]:
        if in_scope(entry, scope) and CYRILLIC.search(entry["text"]):
            for race in set(entry["races"]) & scope:
                row = rows.setdefault(race, {"total": 0, "translated": 0})
                row["total"] += 1
                text = translations.get(entry["key"])
                if text is None and entry["skin"]:
                    text = translations.get(entry["key"].removesuffix("@hd"))
                if text is not None:
                    row["translated"] += 1
    print(json.dumps({"ok": True, "locale": locale, "races": rows, "ui_keys": len(locale_ui)},
                     ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p_extract = sub.add_parser("extract", help="build the object-text catalog")
    p_extract.add_argument("--check", action="store_true")
    p_build = sub.add_parser("build", help="write locale WTS, UI Lua and overlays")
    p_build.add_argument("--locale", default="enUS")
    p_build.add_argument("--check", action="store_true")
    p_check = sub.add_parser("check", help="validate translations and generated files")
    p_check.add_argument("--locale", default="enUS")
    p_check.add_argument("--no-output", action="store_true")
    p_status = sub.add_parser("status", help="translation coverage by race")
    p_status.add_argument("--locale", default="enUS")
    args = parser.parse_args()
    if args.command == "extract":
        return extract(args.check)
    if args.command == "build":
        return build(args.locale, args.check)
    if args.command == "check":
        return validate(args.locale, not args.no_output)
    return status(args.locale)


if __name__ == "__main__":
    raise SystemExit(main())
