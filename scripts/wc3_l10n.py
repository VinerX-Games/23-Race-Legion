"""Inventory, build and validation for 23 Race Forever localizations.

The WTS in the repository stays Russian: it is the translation source. A
locale build copies every source string and replaces only translated entries,
which keeps WTS IDs stable and lets untranslated text fall back to Russian.

The base locale (``"base": true`` in locale.json, currently enUS) becomes the
packaged map's main WTS/W3I/CommandStrings, so every non-Russian client gets
it. The Russian originals are packed as the _Locales/ruRU.w3mod override.
The base files are staged in .cache/l10n/<locale>/ and swapped in by
scripts/build_localized_map.py; map.w3x itself is never rewritten.
"""
from __future__ import annotations

import argparse
import codecs
import hashlib
import json
import re
import shutil
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
STAGE_DIR = ROOT / ".cache/l10n"
SOURCE_LOCALE = "ruRU"
# Map files replaced by a locale; CommandStrings comes from the locale overlay.
LOCALIZED_MAP_FILES = ("war3map.wts", "war3map.w3i")
LOCALE_PROBE_KEY = "TRIGSTR_000"

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
             "ucut": "description", "ides": "shop_description"},
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
COLOR_START = re.compile(r"\|c", re.IGNORECASE)
FORMAT = re.compile(r"%(?:\d+\$)?[sdifxXc%]")
TOKEN = re.compile(r"<[A-Za-z0-9]{4},[A-Za-z0-9]+>")
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
        if line.startswith("STRING") and match is None:
            raise ValueError(f"invalid STRING ID declaration: {line!r} in {path}")
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
            if current in strings:
                raise ValueError(f"duplicate STRING {current} in {path}")
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


def inline_object_texts():
    """Player-visible object strings stored inline instead of as TRIGSTR (the catalog cannot see them)."""
    found = []
    for kind, ext in OBJECT_FILES:
        for prefix in ("war3map", "war3mapSkin"):
            path = MAP / f"{prefix}.{ext}"
            if not path.is_file():
                continue
            extended = extended_for(path.name)
            _, tables = object_records(path.read_bytes(), extended)
            for table in tables:
                for record in table:
                    for (tag, level, _pointer), raw in record["mods"]:
                        field = TEXT_FIELDS.get(kind, {}).get(tag)
                        value = string_value(raw, extended) if field else None
                        if value and not value.startswith("TRIGSTR_") and CYRILLIC.search(value):
                            found.append({"file": path.name, "key": object_entry_key(
                                record["id"], kind, field, level, prefix == "war3mapSkin"), "text": value})
    return found


def externalize_inline_texts() -> int:
    """Move inline Cyrillic object strings into the WTS as new TRIGSTR entries, like the World Editor does."""
    strings, meta = load_wts()
    original_wts = WTS_PATH.read_bytes()
    if (codecs.BOM_UTF8 if meta["bom"] else b"") + dump_wts(strings, meta).encode("utf-8") != original_wts:
        raise SystemExit("war3map.wts does not round-trip; refusing to rewrite it")
    next_sid = max(strings) + 1
    moved, outputs = [], {}
    for kind, ext in OBJECT_FILES:
        for prefix in ("war3map", "war3mapSkin"):
            path = MAP / f"{prefix}.{ext}"
            if not path.is_file():
                continue
            blob = path.read_bytes()
            extended = extended_for(path.name)
            version, tables = object_records(blob, extended)
            out, changed = [struct.pack("<I", version)], False
            for table in tables:
                out.append(struct.pack("<I", len(table)))
                for record in table:
                    mods = []
                    for (tag, level, _pointer), raw in record["mods"]:
                        field = TEXT_FIELDS.get(kind, {}).get(tag)
                        value = string_value(raw, extended) if field else None
                        if value and not value.startswith("TRIGSTR_") and CYRILLIC.search(value):
                            head = raw[:16 if extended else 8]
                            raw = head + f"TRIGSTR_{next_sid:03d}".encode("ascii") + b"\0" + raw[-4:]
                            strings[next_sid] = value
                            moved.append({"file": path.name, "id": record["id"], "field": field,
                                          "level": level, "sid": next_sid})
                            next_sid += 1
                            changed = True
                        mods.append(raw)
                    out.append(record["header"] + struct.pack("<I", len(mods)) + b"".join(mods))
            rebuilt = b"".join(out)
            if not changed and rebuilt != blob:
                raise SystemExit(f"{path.name} does not round-trip; refusing to rewrite it")
            if changed:
                object_records(rebuilt, extended)
                outputs[path] = rebuilt
    for path, data in outputs.items():
        path.write_bytes(data)
    if moved:
        write_wts(WTS_PATH, strings, meta)
    print(json.dumps({"ok": True, "moved": len(moved),
                      "files": sorted(path.name for path in outputs),
                      "first_sid": moved[0]["sid"] if moved else None}, ensure_ascii=False, indent=2))
    return 0


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
    wts_path = path / "wts.json"
    wts = read_json(wts_path).get("translations", {}) if wts_path.is_file() else {}
    data["wts_translations"] = wts
    w3i_path = path / "w3i.json"
    w3i = read_json(w3i_path).get("translations", {}) if w3i_path.is_file() else {}
    data["w3i_translations"] = w3i
    return data, ui, path


def render_localized_w3i(base: bytes, translations: dict[str, dict[str, str]]) -> bytes:
    rendered = base
    for key, entry in translations.items():
        source = entry["source"].encode("utf-8")
        target = entry["translation"].encode("utf-8")
        occurrences = rendered.count(source)
        if occurrences != 1:
            raise ValueError(f"W3I source for {key} occurs {occurrences} times; expected exactly once")
        rendered = rendered.replace(source, target, 1)
    return rendered


def lua_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r") + '"'


def render_ui_lua(translations: dict[str, dict[str, str]], game_locales=None, locale_probes=None,
                  default_locale: str = SOURCE_LOCALE) -> str:
    """Lua tables for Loc(): mapped game locales get their table, all others get default_locale."""
    game_locales = game_locales or {}
    locale_probes = locale_probes or {}
    lines = [
        "-- Generated by scripts/wc3_l10n.py build. Do not edit.",
        "-- Source: localization/ui/ruRU.json and localization/locales/*/ui.json",
        "-- MapLocale differs between clients: Loc() is for displayed text only, never for sync logic.",
        f"MapLocale = {lua_quote(default_locale)}",
        "local GAME_LOCALES = {",
    ]
    for game_locale in sorted(game_locales):
        lines.append(f"    [{lua_quote(game_locale)}] = {lua_quote(game_locales[game_locale])},")
    lines += [
        "}",
        "local function SelectMapLocale()",
        "    local locale = BlzGetLocale and BlzGetLocale() or nil",
        "    local selected = locale and GAME_LOCALES[locale] or nil",
        "    if selected == nil and GetLocalizedString then",
    ]
    for locale, probe in sorted(locale_probes.items()):
        lines.append(f"        if GetLocalizedString({lua_quote(probe['key'])}) == {lua_quote(probe['value'])} then selected = {lua_quote(locale)} end")
    lines += [
        "    end",
        f"    MapLocale = selected or {lua_quote(default_locale)}",
        "end",
        "SelectMapLocale()",
        "-- Repeat on the first tick in case the locale natives are not ready while the chunk loads.",
        "if TimerStart and CreateTimer then",
        "    TimerStart(CreateTimer(), 0.0, false, SelectMapLocale)",
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
        f"    local values = UI_STRINGS[MapLocale] or UI_STRINGS.{SOURCE_LOCALE}",
        "    local text = values[key]",
        f"    if text == nil then text = UI_STRINGS.{SOURCE_LOCALE}[key] end",
        "    return text or key",
        "end",
        "",
    ]
    return "\n".join(lines)


def collect_ui():
    """Loc() tables, game-locale mapping, WTS probes and the locale for unmapped clients."""
    source = read_json(UI_SOURCE_PATH)
    tables = {SOURCE_LOCALE: source}
    base_wts, _ = load_wts()
    probe_sid = int(LOCALE_PROBE_KEY.removeprefix("TRIGSTR_"))
    game_locales = {SOURCE_LOCALE: SOURCE_LOCALE}
    locale_probes = {SOURCE_LOCALE: {"key": LOCALE_PROBE_KEY, "value": base_wts[probe_sid]}}
    default_locale = SOURCE_LOCALE
    for config_path in sorted(LOCALES_DIR.glob("*/locale.json")):
        config = read_json(config_path)
        locale = config["locale"]
        ui_path = config_path.parent / "ui.json"
        tables[locale] = {**source, **(read_json(ui_path) if ui_path.is_file() else {})}
        if config.get("base"):
            default_locale = locale
            continue
        for game_locale in config.get("game_locales", []):
            game_locales[game_locale] = locale
        locale_probes.update(config.get("locale_probes", {}))
    return tables, game_locales, locale_probes, default_locale


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


def output_root(locale: str, config) -> Path:
    """Where a locale's files go: the base locale is staged, other locales become a map override."""
    if config.get("base"):
        return STAGE_DIR / locale
    return LOCALE_MAP_DIR / f"{locale}.w3mod"


def unexpected_locale_dirs(expected_roots) -> list[Path]:
    if not LOCALE_MAP_DIR.is_dir():
        return []
    return sorted(path for path in LOCALE_MAP_DIR.iterdir() if path not in expected_roots)


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
    wts_translations = config.get("wts_translations", {})
    unknown_wts = sorted(set(wts_translations) - {str(sid) for sid in base})
    if unknown_wts:
        print(json.dumps({"ok": False, "unknown_wts_ids": unknown_wts}, ensure_ascii=False, indent=2))
        return 1
    merged.update({int(sid): text for sid, text in wts_translations.items()})
    root = output_root(locale, config)
    output_wts = root / "war3map.wts"
    expected = [(output_wts, (codecs.BOM_UTF8 if meta["bom"] else b"") + dump_wts(merged, meta).encode("utf-8"))]
    w3i_translations = config.get("w3i_translations", {})
    try:
        localized_w3i = render_localized_w3i((MAP / "war3map.w3i").read_bytes(), w3i_translations)
    except (KeyError, ValueError) as error:
        print(json.dumps({"ok": False, "w3i_error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    expected.append((root / "war3map.w3i", localized_w3i))

    # Locale UI files only contain translated keys; merge over the default table.
    ui, game_locales, locale_probes, default_locale = collect_ui()
    expected.append((LUA_OUT, render_ui_lua(ui, game_locales, locale_probes, default_locale).encode("utf-8")))

    overlay = locale_dir / "overlay"
    overlay_files = []
    if overlay.is_dir():
        for source in sorted(overlay.rglob("*")):
            if source.is_file():
                data = source.read_bytes()
                if source.suffix.lower() == ".txt":
                    data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
                relative = source.relative_to(overlay)
                overlay_files.append(relative)
                expected.append((root / relative, data))

    expected_roots = {root}
    if config.get("base"):
        # The packaged base becomes non-Russian, so the Russian originals turn into an override.
        source_root = LOCALE_MAP_DIR / f"{SOURCE_LOCALE}.w3mod"
        expected_roots.add(source_root)
        for relative in [Path(name) for name in LOCALIZED_MAP_FILES] + overlay_files:
            expected.append((source_root / relative, (MAP / relative).read_bytes()))
    unexpected = unexpected_locale_dirs(expected_roots)

    stale, missing = [], []
    for path, data in expected:
        if not path.is_file():
            missing.append(str(path.relative_to(ROOT)))
        elif path.read_bytes() != data:
            stale.append(str(path.relative_to(ROOT)))
    if check:
        ok = not (stale or missing or unexpected)
        print(json.dumps({"ok": ok, "stale": stale, "missing": missing,
                          "unexpected": [str(path.relative_to(ROOT)) for path in unexpected],
                          "translated_sids": sum(1 for sid in resolved if resolved[sid] != base.get(sid))},
                         ensure_ascii=False, indent=2))
        return 0 if ok else 1
    for path in unexpected:
        # A leftover override (e.g. the old _Locales/enUS.w3mod) would be packed into the map.
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    for path, data in expected:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({"ok": True, "locale": locale, "base": bool(config.get("base")),
                      "wts": str(output_wts.relative_to(ROOT)),
                      "translated_sids": sum(1 for sid in resolved if resolved[sid] != base.get(sid)),
                      "ui_keys": len(ui[locale]), "overlay_files": len(overlay_files),
                      "removed": [str(path.relative_to(ROOT)) for path in unexpected]},
                     ensure_ascii=False, indent=2))
    return 0


def check_text(source: str, target: str):
    problems = []
    for label, value in (("source", source), ("translation", target)):
        if len(COLOR_START.findall(value)) != len(COLOR.findall(value)):
            problems.append(f"malformed color code in {label}")
    if COLOR.findall(source) != COLOR.findall(target):
        problems.append("color sequence differs")
    if Counter(FORMAT.findall(source)) != Counter(FORMAT.findall(target)):
        problems.append("format placeholders differ")
    if Counter(TOKEN.findall(source)) != Counter(TOKEN.findall(target)):
        problems.append("ability data references differ")
    if re.findall(r"\d+", COLOR.sub("", source)) != re.findall(r"\d+", COLOR.sub("", target)):
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


def source_hash_issues(by_key, translations, source_hashes):
    missing, stale = [], []
    for key in sorted(set(translations) & set(by_key)):
        source = by_key[key]
        source_text = source["text"] if isinstance(source, dict) else source
        expected = hashlib.sha256(source_text.encode("utf-8")).hexdigest()
        if key not in source_hashes:
            missing.append(key)
        elif source_hashes[key] != expected:
            stale.append(key)
    return missing, stale


def untranslated_lua_wts_ids(lua_text, base_wts, resolved, wts_translations):
    referenced = {int(value) for value in re.findall(r"TRIGSTR_0*(\d+)", lua_text)}
    return sorted(sid for sid in referenced
                  if sid in base_wts and CYRILLIC.search(base_wts[sid])
                  and sid not in resolved and str(sid) not in wts_translations)


def localization_source_texts(catalog, locale_dir: Path):
    sources = {entry["key"]: entry["text"] for entry in catalog["entries"]}
    sources.update({f"ui/{key}": value for key, value in read_json(UI_SOURCE_PATH).items()})
    wts_path = locale_dir / "wts.json"
    if wts_path.is_file():
        base_wts, _ = load_wts()
        for sid in read_json(wts_path).get("translations", {}):
            if str(sid).isdigit() and int(sid) in base_wts:
                sources[f"wts/{sid}"] = base_wts[int(sid)]
    w3i_path = locale_dir / "w3i.json"
    if w3i_path.is_file():
        for key, entry in read_json(w3i_path).get("translations", {}).items():
            sources[f"w3i/{key}"] = entry.get("source", "")
    base = command_sections(MAP / "Units/CommandStrings.txt")
    for section, values in base.items():
        for key, value in values.items():
            sources[f"overlay/Units/CommandStrings.txt/{section}/{key}"] = value
    return sources


def localization_values(translations, locale_ui, locale_dir: Path):
    values = dict(translations)
    values.update({f"ui/{key}": value for key, value in locale_ui.items()})
    wts_path = locale_dir / "wts.json"
    if wts_path.is_file():
        values.update({f"wts/{sid}": value for sid, value in
                       read_json(wts_path).get("translations", {}).items()})
    w3i_path = locale_dir / "w3i.json"
    if w3i_path.is_file():
        values.update({f"w3i/{key}": entry.get("translation", "") for key, entry in
                       read_json(w3i_path).get("translations", {}).items()})
    overlay = locale_dir / "overlay/Units/CommandStrings.txt"
    if overlay.is_file():
        for section, entries in command_sections(overlay).items():
            for key, value in entries.items():
                values[f"overlay/Units/CommandStrings.txt/{section}/{key}"] = value
    return values


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
            if len(COLOR_START.findall(right)) != len(COLOR.findall(right)):
                errors.append({"key": f"CommandStrings/{section}/{key}", "issue": "malformed color code"})


def validate(locale: str, check_output: bool = True) -> int:
    catalog = extract_catalog()
    if not catalog_is_fresh(catalog):
        print(json.dumps({"ok": False, "error": "localization/catalog.json is stale; run extract"},
                         ensure_ascii=False, indent=2))
        return 1
    config, locale_ui, locale_dir = locale_config(locale)
    translations = config.get("translations", {})
    wts_translations = config.get("wts_translations", {})
    w3i_translations = config.get("w3i_translations", {})
    hashes_path = locale_dir / "source_hashes.json"
    source_hashes = read_json(hashes_path) if hashes_path.is_file() else {}
    by_key = {entry["key"]: entry for entry in catalog["entries"]}
    errors, warnings = [], []
    scope = set(config.get("scope_races", []))
    required = {key for key, entry in by_key.items() if CYRILLIC.search(entry["text"])}
    source_texts = localization_source_texts(catalog, locale_dir)
    hash_values = localization_values(translations, locale_ui, locale_dir)
    missing_hashes, stale_hashes = source_hash_issues(source_texts, hash_values, source_hashes)
    errors.extend({"key": key, "issue": "missing source_sha256"} for key in missing_hashes)
    errors.extend({"key": key, "issue": "stale translation source_sha256"} for key in stale_hashes)
    for key in sorted(set(translations) - set(by_key)):
        errors.append({"key": key, "issue": "translation key is not in catalog"})
    for item in inline_object_texts():
        errors.append({"key": item["key"], "issue": f"inline object text in {item['file']}; run externalize"})
    for key in sorted(required - set(translations)):
        if by_key[key]["skin"] and translations.get(key.removesuffix("@hd")) is not None:
            continue
        errors.append({"key": key, "issue": "missing translation"})
    for key in sorted(set(translations) & set(by_key)):
        text = translations[key]
        entry = by_key[key]
        for problem in check_text(entry["text"], text):
            errors.append({"key": key, "issue": problem})
        if text == entry["text"] and CYRILLIC.search(entry["text"]):
            errors.append({"key": key, "issue": "translation equals source"})
        if len(text) > len(entry["text"]) * 1.6 + 40:
            warnings.append({"key": key, "issue": "translation is much longer than source"})
    base_wts, _ = load_wts()
    w3i = (MAP / "war3map.w3i").read_bytes()
    w3i_sids = {int(match) for match in re.findall(rb"TRIGSTR_([0-9]+)", w3i)}
    required_wts = {str(sid) for sid in w3i_sids
                    if sid in base_wts and CYRILLIC.search(base_wts[sid])}
    for sid in sorted(set(wts_translations) - {str(value) for value in base_wts}):
        errors.append({"key": f"wts/{sid}", "issue": "WTS translation ID is not in source"})
    for sid in sorted(required_wts - set(wts_translations)):
        errors.append({"key": f"wts/{sid}", "issue": "missing map metadata translation"})
    for sid, text in sorted(wts_translations.items()):
        if not sid.isdigit() or int(sid) not in base_wts:
            continue
        for problem in check_text(base_wts[int(sid)], text):
            errors.append({"key": f"wts/{sid}", "issue": problem})
        if CYRILLIC.search(base_wts[int(sid)]) and text == base_wts[int(sid)]:
            errors.append({"key": f"wts/{sid}", "issue": "translation equals source"})
    w3i_bytes = (MAP / "war3map.w3i").read_bytes()
    w3i_sources = []
    for raw in w3i_bytes.split(b"\0"):
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if CYRILLIC.search(text):
            w3i_sources.append(text)
    translated_w3i_sources = {entry.get("source", "") for entry in w3i_translations.values()}
    for source in sorted(set(w3i_sources) - translated_w3i_sources):
        errors.append({"key": "w3i", "issue": f"missing W3I text translation: {source[:80]}"})
    for key, entry in sorted(w3i_translations.items()):
        source, text = entry.get("source", ""), entry.get("translation", "")
        if w3i_bytes.count(source.encode("utf-8")) != 1:
            errors.append({"key": f"w3i/{key}", "issue": "W3I source text is not unique or is absent"})
            continue
        for problem in check_text(source, text):
            errors.append({"key": f"w3i/{key}", "issue": problem})
    resolved, conflicts = resolve_translations(catalog, translations)
    for conflict in conflicts:
        errors.append({"key": conflict["key"], "issue": f"shared WTS {conflict['sid']} has conflicting translations"})
    lua_source = (MAP / "war3map.lua").read_text(encoding="utf-8-sig")
    for sid in untranslated_lua_wts_ids(lua_source, base_wts, resolved, wts_translations):
        errors.append({"key": f"wts/{sid}", "issue": "missing translation for Lua-referenced WTS string"})
    for probe_locale, probe in sorted(config.get("locale_probes", {}).items()):
        match = re.fullmatch(r"TRIGSTR_(\d+)", probe.get("key", ""))
        if not match:
            errors.append({"key": f"locale_probes/{probe_locale}", "issue": "invalid WTS probe key"})
            continue
        sid = int(match.group(1))
        actual = resolved.get(sid, base_wts.get(sid))
        if actual != probe.get("value"):
            errors.append({"key": f"locale_probes/{probe_locale}",
                           "issue": "WTS probe does not match the generated locale"})
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
    stale_translations = [item for item in errors if item["issue"] == "stale translation source_sha256"]
    missing_translations = [item for item in errors if item["issue"] == "missing translation"]
    report = {"ok": not errors and build_code == 0, "errors": errors, "warnings": warnings,
              "stale": stale_translations, "missing": missing_translations,
              "missing_source_hashes": [item for item in errors if item["issue"] == "missing source_sha256"],
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


def status(locale: str = "enUS", all_races: bool = False) -> int:
    catalog = extract_catalog()
    config, locale_ui, _ = locale_config(locale)
    translations = config.get("translations", {})
    scope = set(config.get("scope_races", []))
    if all_races:
        scope = {race for entry in catalog["entries"] for race in entry.get("races", [])}
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
    cyrillic = [entry for entry in catalog["entries"] if CYRILLIC.search(entry["text"])]
    inventory = {
        "cyrillic_entries": len(cyrillic),
        "custom": sum(bool(entry["custom"]) for entry in cyrillic),
        "shared_or_unassigned": sum(len(entry.get("races") or []) != 1 for entry in cyrillic),
        "translated_object_keys": sum(entry["key"] in translations for entry in cyrillic),
        "distinct_wts_ids": len({entry["sid"] for entry in cyrillic}),
    }
    print(json.dumps({"ok": True, "locale": locale, "all_races": all_races,
                      "inventory": inventory, "races": rows, "ui_keys": len(locale_ui)},
                     ensure_ascii=False, indent=2))
    return 0


def fingerprint(locale: str, refresh: set[str] | None = None) -> int:
    """Record source hashes for translated entries that have no baseline yet."""
    catalog = extract_catalog()
    config, locale_ui, locale_dir = locale_config(locale)
    translations = config.get("translations", {})
    path = locale_dir / "source_hashes.json"
    hashes = read_json(path) if path.is_file() else {}
    sources = localization_source_texts(catalog, locale_dir)
    values = localization_values(translations, locale_ui, locale_dir)
    added, unknown = 0, []
    for key in values:
        source = sources.get(key)
        if source is None:
            unknown.append(key)
        elif key not in hashes or key in (refresh or set()):
            hashes[key] = hashlib.sha256(source.encode("utf-8")).hexdigest()
            added += 1
    unknown_refresh = sorted((refresh or set()) - set(values))
    unknown.extend(f"--refresh key is not translated: {key}" for key in unknown_refresh)
    path.write_text(json.dumps(hashes, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": not unknown, "added": added, "unknown": unknown}, ensure_ascii=False, indent=2))
    return 0 if not unknown else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p_extract = sub.add_parser("extract", help="build the object-text catalog")
    p_extract.add_argument("--check", action="store_true")
    sub.add_parser("externalize", help="move inline Cyrillic object strings into war3map.wts")
    p_build = sub.add_parser("build", help="write locale WTS, UI Lua and overlays")
    p_build.add_argument("--locale", default="enUS")
    p_build.add_argument("--check", action="store_true")
    p_check = sub.add_parser("check", help="validate translations and generated files")
    p_check.add_argument("--locale", default="enUS")
    p_check.add_argument("--no-output", action="store_true")
    p_status = sub.add_parser("status", help="translation coverage by race")
    p_status.add_argument("--locale", default="enUS")
    p_status.add_argument("--all-races", action="store_true", help="report every race present in the catalog")
    p_fingerprint = sub.add_parser("fingerprint", help="record source hashes for new translations")
    p_fingerprint.add_argument("--locale", default="enUS")
    p_fingerprint.add_argument("--refresh", action="append", default=[], metavar="KEY",
                               help="refresh a reviewed stale translation hash; repeat for multiple keys")
    args = parser.parse_args()
    if args.command == "extract":
        return extract(args.check)
    if args.command == "externalize":
        return externalize_inline_texts()
    if args.command == "build":
        return build(args.locale, args.check)
    if args.command == "check":
        return validate(args.locale, not args.no_output)
    if args.command == "fingerprint":
        return fingerprint(args.locale, set(args.refresh))
    return status(args.locale, args.all_races)


if __name__ == "__main__":
    raise SystemExit(main())
