"""Build a current-source UI inventory and a review queue; never edits map data.

Stored object modifications are inventoried, including skin overrides and levels.
Inherited CASC fields and runtime-computed strings still require effective HiveWE
readback / manual review: a clean result is not proof of gameplay correctness.
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
import struct
import argparse
from pathlib import Path

from implement_draenei_rework import object_records
from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "map.w3x"
OUT = ROOT / "docs/ui_text"
COLOR = re.compile(r"\|c[0-9a-fA-F]{8}|\|r", re.I)
PALETTE = {"ced4da", "ffffff", "c8e087", "ef8173", "f2a35e", "ebc56c", "b99d66", "f0cb5c", "5f6874"}
FIELDS = {
    "w3u": {"unam", "utip", "utub", "upro", "uawt", "utpr", "ucun", "ucut"},
    "w3t": {"unam", "utip", "utub", "ides"},
    "w3a": {"anam", "atp1", "aub1", "aut1", "auu1", "aret", "arut"},
    "w3q": {"gnam", "gtp1", "gub1"},
    "w3h": {"fnam", "ftip", "fube"},
    "w3b": {"bnam", "bsuf"},
    "w3d": {"dnam"},
}
SHORT = {"unam", "utip", "uawt", "utpr", "anam", "atp1", "aut1", "aret", "gnam", "gtp1", "ftip"}
LONG = {"utub", "aub1", "auu1", "arut", "gub1", "fube"}
TECHNICAL_FIELDS = {
    "uhot": "hotkey", "ahky": "hotkey", "arhk": "hotkey", "auhk": "hotkey", "ghk1": "hotkey",
    "unsf": "editor_suffix", "ansf": "editor_suffix", "gnsf": "editor_suffix", "fnsf": "editor_suffix", "bsuf": "editor_suffix",
    "gef1": "effect_rawcode", "gef2": "effect_rawcode", "gef3": "effect_rawcode", "gef4": "effect_rawcode",
    "gcls": "upgrade_class",
}
# The lexer skips comments, preserves long strings, and handles escaped quotes.
LUA_TOKEN = re.compile(
    r"--\[(?P<ceq>=*)\[.*?\](?P=ceq)\]|--[^\n]*"
    r"|\[(?P<eq>=*)\[(?P<long>.*?)\](?P=eq)\]"
    r"|(?P<quote>['\"])(?P<quoted>(?:\\.|(?!(?P=quote))[^\\])*)(?P=quote)", re.S)
LOG_SINKS = {"ProbeLogWrite", "AiProbeLogLimited", "BrainLog", "BrainLogTag", "BrainLogEvery", "DipLog", "DipLogEvery"}
PLAYER_TEXT_SINKS = {
    "DisplayTextToForce", "DisplayTimedTextToForce", "DisplayTextToPlayer", "DisplayTimedTextToPlayer",
    "BJDebugMsg", "BlzFrameSetText", "BlzSetAbilityTooltip", "BlzSetAbilityExtendedTooltip",
    "BlzSetAbilityResearchTooltip", "BlzSetAbilityResearchExtendedTooltip", "BlzSetAbilityActivatedTooltip",
    "BlzSetAbilityActivatedExtendedTooltip", "SetPlayerName", "SetPlayerNameForced", "BlzSetUnitName",
    "BlzSetHeroProperName", "LeaderboardSetLabel", "LeaderboardAddItem", "MultiboardSetTitleText",
    "MultiboardSetItemValue", "TimerDialogSetTitle", "DialogSetMessage", "DialogAddButton", "QuestSetTitle",
    "QuestSetDescription", "QuestItemSetDescription", "CreateQuestBJ", "CreateDefeatConditionBJ",
    "SetTextTagText", "DipChat", "DipBroadcast", "DipRpBroadcast",
}


def lua_literals_with_calls(text):
    """Track enclosing calls while skipping quoted text and comments.

    This deliberately recognizes only named parenthesized calls. Unknown sinks
    remain review candidates rather than being guessed from an English prefix.
    """
    calls, last, pos = [], None, 0
    for match in LUA_TOKEN.finditer(text):
        for token in re.findall(r"[A-Za-z_][A-Za-z0-9_.]*|[^\s]", text[pos:match.start()]):
            if token == "(":
                calls.append(last)
                last = None
            elif token == ")":
                if calls:
                    calls.pop()
                last = None
            else:
                last = token if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", token) else None
        value = match["long"] if match["long"] is not None else match["quoted"]
        if value is not None:
            yield match, tuple(calls)
            last = None
        pos = match.end()


def plain(value):
    return COLOR.sub("", value).replace("|n", "\n").strip()


def write_json(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


def is_effective_object_source(path):
    return path.suffix[1:] in FIELDS or path.name in {"war3map.wts", "war3mapSkin.txt"}


def verify_batch(path):
    """Resolve every consumer in an audited WTS batch through effective SD/HD data."""
    plan = json.loads(path.read_text(encoding="utf-8"))
    wts = load_wts_strings(MAP / "war3map.wts")
    kinds = {"w3u": "unit", "w3a": "ability", "w3q": "upgrade", "w3h": "buff", "w3t": "item"}
    aliases = {"unam": "name", "anam": "name", "gnam": "name", "fnam": "name",
               "utip": "tip", "atp1": "tip", "gtp1": "tip", "ftip": "bufftip",
               "uawt": "awakentip", "utpr": "revivetip", "aret": "researchtip", "aut1": "untip",
               "upro": "propernames"}
    groups = collections.defaultdict(list)
    for row in plan["strings"]:
        for consumer in row["consumers"]:
            kind = kinds[Path(consumer["source"]).suffix[1:]]
            field = aliases[consumer["field"]]
            if consumer["level"]:
                field += str(consumer["level"])
            groups[kind].append((consumer, field, row["after"]))
    results = []
    for kind, entries in sorted(groups.items()):
        for hd in (False, True):
            args = ["get-objects-bulk", "--type", kind, "--ids", ",".join(sorted({c["id"] for c, _, _ in entries})),
                    "--fields", ",".join(sorted({f for _, f, _ in entries}))]
            if hd:
                args.append("--hd")
            data = require(cli(args))
            found = {obj["id"]: obj["fields"] for obj in data["objects"]}
            for consumer, field, expected in entries:
                value = found[consumer["id"]][field]
                if re.fullmatch(r"TRIGSTR_\d+", value):
                    value = wts[int(value[8:])]
                results.append(dict(consumer=consumer, variant="HD" if hd else "SD", field=field,
                                    exact_match=value == expected, actual=value))
    report = dict(checks=results, exact_matches=sum(r["exact_match"] for r in results), total=len(results))
    write_json(path.with_name(path.stem + "_readback.json"), report)
    print(json.dumps({k: v for k, v in report.items() if k != "checks"}))
    if report["exact_matches"] != report["total"]:
        raise AssertionError("Effective SD/HD readback differs from the audited batch; see readback report")


def effective_inventory():
    """Include inherited text and skin precedence, without truncating object dumps."""
    stored = json.loads((OUT / "global_inventory.json").read_text(encoding="utf-8"))
    ownership = collections.defaultdict(set)
    for obj in stored["objects"]:
        ownership[obj["id"]].update(obj["races"])
    wts = load_wts_strings(MAP / "war3map.wts")
    rows, counts = [], {}
    for kind in ("unit", "ability", "upgrade", "buff", "item", "destructible", "doodad"):
        metadata = require(cli(["list-fields", "--type", kind]))
        fields = sorted({f["column"] for f in metadata["fields"]
                         if re.fullmatch(r"(?:name|tip|ubertip|untip|unubertip|researchtip|researchubertip|propernames|awakentip|revivetip|bufftip|buffubertip|description|casterupgradename|casterupgradetip|levels|maxlevel)\d*", f["column"])})
        for hd in (False, True):
            args = ["dump-objects", "--type", kind, "--max", "100000", "--fields", ",".join(fields)]
            if hd:
                args.append("--hd")
            data = require(cli(args))
            objects = data["objects"]
            assert len(objects) < 100000, "Object dump may have hit its cap"
            variant = "HD" if hd else "SD"
            counts[kind + "/" + variant] = len(objects)
            for obj in objects:
                values = obj["fields"]
                # dump-objects exposes the resolved name at object level rather
                # than in fields, unlike get-objects-bulk.
                values.setdefault("name", obj.get("name", ""))
                levels = int(values.get("levels") or values.get("maxlevel") or 1)
                for field, value in values.items():
                    if not value or field in {"levels", "maxlevel"}:
                        continue
                    match = re.search(r"(\d+)$", field)
                    level = int(match[1]) if match else 0
                    if level > levels:
                        continue
                    row = dict(type=kind, id=obj["id"], variant=variant, field=field,
                               races=sorted(ownership[obj["id"]]))
                    if re.fullmatch(r"TRIGSTR_\d+", value):
                        row["sid"] = int(value[8:])
                        row["text"] = wts.get(row["sid"])
                    else:
                        row["text"] = value
                    rows.append(row)
            print(f"{kind}/{variant}: {len(objects)} objects", flush=True)
    report = dict(schema=1, counts=counts, rows=rows,
                  sources={p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(MAP.glob("war3map*")) if p.is_file() and is_effective_object_source(p)},
                  limitations=["Dump includes unused standard objects: presence is not reachability.",
                               "Level filtering uses the effective declared number of levels.",
                               "Runtime-created text and Lua replacements require separate review."])
    write_json(OUT / "global_effective.json", report)
    print(json.dumps({"effective_text_fields": len(rows), "objects": counts}))


def prepare_short_names():
    """Use an object's current nominative name for its command-style unit titles.

    Only WTS entries whose known consumers all agree on the canonical title are
    eligible. Inherited literals and ambiguous shared references remain queued.
    """
    inventory = json.loads((OUT / "global_inventory.json").read_text(encoding="utf-8"))
    effective = json.loads((OUT / "global_effective.json").read_text(encoding="utf-8"))
    wts = {row["sid"]: row for row in inventory["wts"]}
    names = {(row["id"], row["variant"]): plain(row["text"] or "")
             for row in effective["rows"] if row["type"] == "unit" and row["field"] == "name"}
    prefix = re.compile(r"(?:Нанять|Обучить|Призвать|Исследовать|Улучшить до|Построить|Купить|Воскресить|Вырастить|Train|Hire|Summon|Research|Upgrade to|Build|Resurrect)\s", re.I)
    candidates, skipped = {}, []
    for row in effective["rows"]:
        if row["type"] != "unit" or row["field"] not in {"tip", "awakentip", "revivetip"}:
            continue
        if not prefix.match(plain(row["text"] or "")):
            continue
        name = names.get((row["id"], row["variant"]), "")
        if not name or prefix.match(name) or re.search(r"[A-Za-z]{3,}|\([A-Za-zА-Яа-я]\)$", name) or "sid" not in row:
            skipped.append(row)
            continue
        candidates.setdefault(row["sid"], set()).add("|cffebc56c" + name + "|r")
    plan = []
    for sid, desired in sorted(candidates.items()):
        if len(desired) != 1:
            continue
        after = next(iter(desired))
        consumers, safe = [], True
        for ref in wts[sid]["references"]:
            if "object" not in ref:
                safe = False
                break
            obj = inventory["objects"][ref["object"]]
            if not obj["source"].endswith(".w3u") or obj["field"] not in {"unam", "utip", "uawt", "utpr"}:
                safe = False
                break
            for variant in ("SD", "HD"):
                if "|cffebc56c" + names.get((obj["id"], variant), "") + "|r" != after:
                    safe = False
            consumers.append({k: obj[k] for k in ("source", "id", "field", "level", "pointer")})
        if safe:
            plan.append(dict(reference_before=f"TRIGSTR_{sid:03d}", before=wts[sid]["text"],
                             after=after, consumers=consumers))
    path = OUT / "global_short_names.json"
    write_json(path, dict(scope="Короткие названия юнитов: имя текущего объекта вместо командного префикса; WTS-only.",
                         strings=plan, skipped=skipped))
    print(json.dumps({"strings": len(plan), "consumers": sum(len(r["consumers"]) for r in plan),
                      "skipped_effective_rows": len(skipped)}))


def refresh_effective_wts():
    path = OUT / "global_effective.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    wts = load_wts_strings(MAP / "war3map.wts")
    for relative, digest in data["sources"].items():
        if relative != "map.w3x/war3map.wts":
            assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest, relative
    for row in data["rows"]:
        if "sid" in row:
            row["text"] = wts.get(row["sid"])
    # Resolved top-level object names lack a SID. Require them to be unchanged.
    # Callers changing object names must run --effective again instead.
    data["sources"]["map.w3x/war3map.wts"] = hashlib.sha256((MAP / "war3map.wts").read_bytes()).hexdigest()
    write_json(path, data)
    print("Refreshed effective WTS values; binary sources unchanged. Object names require separate verification.")


def prepare_menu_batch(path):
    """Preview requested menu sections; keep every other paragraph unchanged."""
    plan = json.loads(path.read_text(encoding="utf-8"))
    requests = {row["id"]: row for row in plan["requests"]}
    effective = json.loads((OUT / "global_effective.json").read_text(encoding="utf-8"))
    for name, digest in effective["sources"].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    lookup = {(r["id"], r["variant"], r["field"]): r for r in effective["rows"] if r["type"] == "unit"}
    relations = collections.defaultdict(lambda: collections.defaultdict(set))
    targets, sources = {}, {}
    for source in sorted((ROOT / "docs/techtree/races").glob("*.json")):
        data = json.loads(source.read_text(encoding="utf-8"))
        used = False
        for edge in data["edges"]:
            origin, kind, target = edge.split(" ", 2)
            if origin in requests and kind in {"trains", "researches", "morphs-to"}:
                obj = data["objects"][target]
                assert obj.get("name") and obj["type"] != "unknown", (origin, kind, target)
                assert not plain(obj["name"]).startswith(("СПОСОБНОСТЬ:", "ЮНИТ:", "ИССЛЕДОВАНИЕ:")), target
                relations[origin][kind].add(target)
                targets[target] = obj
                used = True
        if used:
            sources[source.relative_to(ROOT).as_posix()] = hashlib.sha256(source.read_bytes()).hexdigest()

    def section(heading, ids, research=False):
        entries = []
        for code in sorted(ids):
            name = targets[code]["name"]
            if research:
                name = re.sub(r"\s*(?:[—–-]\s*(?:уровень|ступень)\s+1|\[\s*1(?:\s*/\s*\d+)?\s*\])$", "", name, flags=re.I)
            entries.append("- |cffebc56c" + name + "|cffced4da.")
        return "|cffb99d66" + heading + ":|cffced4da|n" + "|n".join(entries)

    operations = []
    for code, request in sorted(requests.items()):
        original = lookup[code, "SD", "ubertip"]["text"]
        assert original == lookup[code, "HD", "ubertip"]["text"], code
        parts = original.removesuffix("|r").split("|n|n")
        if request.get("reset_description"):
            assert "intro" in request, (code, "Replacement description requires a reviewed intro")
            parts = [""]
        if "intro" in request:
            parts[0] = "|cffb99d66ЗДАНИЕ:|cffced4da " + request["intro"]
        assert plain(parts[0]).startswith("ЗДАНИЕ:"), code
        wanted, emitted, output = set(request["sections"]), set(), []
        if request.get("reset_description"):
            required_sections = {kind for kind, values in relations[code].items() if values}
            assert required_sections <= wanted, (code, "Full replacement must include all confirmed menus", required_sections - wanted)

        def emit(kind):
            values = relations[code][kind]
            assert values, (code, kind, "No confirmed menu objects")
            if kind == "researches":
                return [section("Исследования", values, True)]
            if kind == "morphs-to":
                return [section("Улучшение", values)]
            heroes = {target for target in values if targets[target]["type"] == "hero"}
            units = values - heroes
            return ([section("Обучает", units)] if units else []) + ([section("Герои", heroes)] if heroes else [])

        for part in parts:
            content = plain(part)
            kind = "trains" if content.startswith(("Обучает:", "Герои:")) else "researches" if content.startswith("Исследования:") else "morphs-to" if content.startswith("Улучшение:") else None
            if kind in wanted:
                if kind not in emitted:
                    output.extend(emit(kind))
                    emitted.add(kind)
            else:
                output.append(part)
        for kind in ("trains", "researches", "morphs-to"):
            if kind in wanted - emitted:
                output.extend(emit(kind))
        value = "|n|n".join(output) + "|r"
        assert value != original, (code, "No changes")
        operations.append(dict(type="unit", id=code, field="ubertip", value=value))
    operations.extend(plan.get("extra_operations", []))
    plan["operations"] = operations
    plan["graph_sources"] = sources
    plan["menu_objects"] = {code: {kind: sorted(ids) for kind, ids in kinds.items()}
                            for code, kinds in relations.items()}
    write_json(path, plan)
    print(json.dumps({"previewed_buildings": len(requests), "operations": len(operations), "map_edited": False}))


def building_list_review(effective):
    """Compare explicit building list headings with the generated techtree.

    This is a review queue: Lua-conditional menus and hero/name aliases require
    interpretation. It never rewrites descriptions or treats graph hints as a
    substitute for investigating a contradiction.
    """
    lookup = {(r["type"], r["id"], r["variant"], r["field"]): r for r in effective["rows"]}
    def normalized(value, research=False):
        value = plain(value).casefold().replace("ё", "е").strip(' .«»"')
        if research:
            # Lists name the research family, not the first level shown on its
            # button. Both forms refer to the same menu object.
            value = re.sub(r"\s*(?:[—–-]\s*(?:уровень|ступень)\s+1|\[\s*1(?:\s*/\s*\d+)?\s*\])$", "", value)
        return value
    result = []
    for path in sorted((ROOT / "docs/techtree/races").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        edges = collections.defaultdict(lambda: collections.defaultdict(set))
        for edge in data["edges"]:
            origin, relation, target = edge.split(" ", 2)
            if relation in {"trains", "researches"}:
                edges[origin][relation].add(target)
        for code, relations in sorted(edges.items()):
            if data["objects"].get(code, {}).get("type") != "building":
                continue
            for variant in ("SD", "HD"):
                row = lookup.get(("unit", code, variant, "ubertip"))
                if not row:
                    result.append(dict(race=data["race"], id=code, variant=variant, issue="missing_building_description"))
                    continue
                text = plain(row["text"] or "")
                sections = collections.defaultdict(list)
                section = None
                for line in text.splitlines():
                    line = line.strip()
                    if line in {"Обучает:", "Герои:", "Исследования:", "Улучшение:", "Способности:"}:
                        section = line[:-1]
                    elif line.startswith(("- ", "• ")) and section:
                        sections[section].append(line[2:].strip())
                    elif line:
                        section = None
                for relation, targets in sorted(relations.items()):
                    heading = "Исследования" if relation == "researches" else "Обучает/Герои"
                    listed = sections["Исследования"] if relation == "researches" else sections["Обучает"] + sections["Герои"]
                    menu_name = lambda value: normalized(value, relation == "researches")
                    listed_names = {menu_name(x) for x in listed}
                    expected = []
                    for target in sorted(targets):
                        kind = "upgrade" if relation == "researches" else "unit"
                        name = lookup.get((kind, target, variant, "name"), {}).get("text")
                        name = name or data["objects"].get(target, {}).get("name", target)
                        expected.append(dict(id=target, name=plain(name)))
                    missing = [x for x in expected if menu_name(x["name"]) not in listed_names]
                    extra = [x for x in listed if menu_name(x) not in {menu_name(t["name"]) for t in expected}]
                    if missing or extra:
                        result.append(dict(race=data["race"], id=code, variant=variant, section=heading,
                                           expected=expected, listed=listed, missing=missing, extra=extra))
    return result


def main():
    sources = {}
    strings = load_wts_strings(MAP / "war3map.wts")
    refs = collections.defaultdict(list)
    objects, lua_strings, interface = [], [], []
    localization_mentions, constant_localizations, dynamic_localization_references = [], [], []
    owners = collections.defaultdict(set)
    ownership_sources = sorted((ROOT / "docs/techtree/races").glob("*.json"))
    for path in ownership_sources:
        data = json.loads(path.read_text(encoding="utf-8"))
        for code in data["objects"]:
            owners[code].add(data["race"])

    def source(path):
        relative = path.relative_to(ROOT).as_posix()
        sources[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        return relative

    source(MAP / "war3map.wts")
    source(Path(__file__).resolve())
    reviewed_ui = collections.defaultdict(set)
    reviewed_roles = {}
    role_path = OUT / "global_lua_classification.json"
    if role_path.exists():
        source(role_path)
        roles = json.loads(role_path.read_text(encoding="utf-8"))
        valid_sources = {name for name, digest in roles.get("sources", {}).items()
                         if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest}
        for row in roles.get("rows", []):
            if row["source"] in valid_sources:
                reviewed_roles[row["source"], row["line"], row["text"]] = row
    review_path = OUT / "global_lua_review.json"
    if review_path.exists():
        source(review_path)
        review = json.loads(review_path.read_text(encoding="utf-8"))
        for relative, hashes in review.get("sources", {}).items():
            if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == hashes.get("after_sha256"):
                reviewed_ui[relative].update(row["after"] for row in review.get("translations", []))
    for path in ownership_sources:
        source(path)
    for ext, fields in FIELDS.items():
        for stem in ("war3map", "war3mapSkin"):
            path = MAP / f"{stem}.{ext}"
            if not path.exists():
                continue
            relative = source(path)
            extended = ext in {"w3a", "w3q", "w3d"}
            _, tables = object_records(path.read_bytes(), extended)
            for table in tables:
                for obj in table:
                    for (field, level, pointer), raw in obj["mods"]:
                        if struct.unpack_from("<I", raw, 4)[0] != 3:
                            continue
                        offset = 16 if extended else 8
                        value = raw[offset:-5].decode("utf-8")
                        match = re.fullmatch(r"TRIGSTR_(\d+)", value)
                        if field not in fields and not match:
                            continue
                        row = dict(source=relative, id=obj["id"], field=field, level=level,
                                   pointer=pointer, races=sorted(owners[obj["id"]]), raw=value,
                                   role=TECHNICAL_FIELDS.get(field, "ui_text" if field in fields else "unmapped_field_requires_review"))
                        if match:
                            row["sid"] = int(match[1])
                            row["text"] = strings.get(row["sid"])
                            refs[row["sid"]].append({"object": len(objects)})
                        else:
                            row["text"] = value
                        objects.append(row)

    for path in sorted((MAP / "_lua/monolith_split/sections").rglob("*.lua")):
        relative = source(path)
        text = path.read_text(encoding="utf-8-sig")
        masked = LUA_TOKEN.sub(lambda m: " " * len(m[0]), text)
        for mention in re.finditer(r"\b(GetLocalizedString|GetLocalizedHotkey)\b", masked):
            localization_mentions.append(dict(source=relative, line=text.count("\n", 0, mention.start()) + 1,
                                              api=mention[1]))
        for match, calls in lua_literals_with_calls(text):
            value = match["long"] if match["long"] is not None else match["quoted"]
            if value is None:
                continue
            line = text.count("\n", 0, match.start()) + 1
            if (calls and calls[-1] in {"GetLocalizedString", "GetLocalizedHotkey"}
                    and re.fullmatch(r"TRIGSTR_\d+", value) and re.match(r"\s*\)", text[match.end():])):
                constant_localizations.append(dict(source=relative, line=line, api=calls[-1], key=value))
            if value in {"GetLocalizedString", "GetLocalizedHotkey"} or value.startswith("TRIGSTR_") and not re.fullmatch(r"TRIGSTR_\d+", value):
                dynamic_localization_references.append(dict(source=relative, line=line, value=value))
            for sid in re.findall(r"TRIGSTR_(\d+)", value):
                refs[int(sid)].append(dict(source=relative, line=line))
            # Candidate literals include Russian prose and English sentences.
            # Rawcodes, native names and asset paths aren't UI review candidates.
            # Include single-word native UI labels too. A nested frame lookup's
            # identifier is not itself the text passed to BlzFrameSetText.
            direct_ui = bool(calls) and calls[-1] in PLAYER_TEXT_SINKS
            if (re.search(r"[А-Яа-яЁё]", value) or re.search(r"[A-Za-z]{2,} [A-Za-z]{2,}", value)
                    or direct_ui and value.strip()):
                diagnostic = sorted(set(calls) & LOG_SINKS)
                classification = "needs_ui_or_debug_review"
                reason = "Sink/visibility requires review."
                if diagnostic:
                    classification = "diagnostic_log"
                    reason = "Argument of " + ", ".join(diagnostic) + "; diagnostic output may be echoed by the debug log filter."
                elif value in reviewed_ui[relative]:
                    classification = "reviewed_player_ui"
                    reason = "Player-facing translation reviewed in global_lua_review.json; source SHA-256 matches."
                elif (relative, line, value) in reviewed_roles:
                    role = reviewed_roles[relative, line, value]
                    classification, reason = role["classification"], role["reason"]
                elif "TriggerRegisterPlayerChatEvent" in calls:
                    classification = "technical_command"
                    reason = "Literal chat command registered with the engine; preserve command syntax."
                elif direct_ui:
                    classification = "player_text_sink_requires_content_review"
                    reason = "Direct literal argument of " + calls[-1] + "; check translation, purpose and styling."
                lua_strings.append(dict(source=relative, line=line, text=value,
                                        calls=[call for call in calls if call],
                                        classification=classification, reason=reason))

    for path in sorted(MAP.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".txt", ".fdf"}:
            relative = source(path)
            for line, value in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
                if value.strip() and not value.lstrip().startswith("//"):
                    interface.append(dict(source=relative, line=line, text=value))
                    for sid in re.findall(r"TRIGSTR_(\d+)", value):
                        refs[int(sid)].append(dict(source=relative, line=line))

    # Metadata uses WTS references in binary C strings (e.g. name/loading screen
    # in w3i). These consumers must not be mistaken for abandoned WTS entries.
    for path in sorted(MAP.glob("war3map*")):
        if not path.is_file() or path.suffix[1:] in FIELDS or path.suffix.lower() in {".wts", ".lua", ".txt"}:
            continue
        relative = source(path)
        for match in re.finditer(rb"TRIGSTR_(\d+)", path.read_bytes()):
            refs[int(match[1])].append(dict(source=relative, byte_offset=match.start()))

    findings = collections.defaultdict(list)
    for row in objects:
        value = row["text"]
        key = {k: row[k] for k in ("source", "id", "field", "level", "pointer")}
        if row["role"] == "hotkey" and value is not None:
            candidate = value.strip()
            if len(candidate) > 1 and not candidate.isdigit():
                findings["invalid_hotkey_reference"].append(key | {"sid": row.get("sid"), "actual": value})
        if row["role"] == "effect_rawcode" and value is not None:
            if value.strip() not in {"", "_", "-"} and not re.fullmatch(r"[A-Za-z0-9]{4}", value.strip()):
                findings["invalid_effect_reference"].append(key | {"sid": row.get("sid"), "actual": value})
        if row["role"] != "ui_text":
            continue
        if value is None:
            findings["missing_wts"].append(key | {"sid": row["sid"]})
            continue
        clean = plain(value)
        if not clean or clean == "_":
            continue
        if re.search(r"[A-Za-z]{3,}", clean):
            findings["latin_review"].append(key)
        if row["field"] in SHORT:
            if re.match(r"(?:Нанять|Обучить|Призвать|Исследовать|Изучить|Улучшить до|Построить|Купить|Train|Hire|Summon|Research|Learn|Upgrade to|Build)\s", clean, re.I):
                findings["short_command_prefix"].append(key)
            if re.search(r"\([A-Za-zА-Яа-я]\)\s*$", clean):
                findings["short_hotkey"].append(key)
        if row["field"] in LONG and not re.match(r"[А-ЯЁ /-]+:", clean):
            findings["missing_type_label"].append(key)
        invalid = sorted({c.lower() for c in re.findall(r"\|cff([0-9a-fA-F]{6})", value)} - PALETTE)
        if invalid:
            findings["palette_review"].append(key | {"colors": invalid})
        if re.search(r"\|c(?!ff)[0-9a-fA-F]{8}", value, re.I):
            findings["nonopaque_color"].append(key)
        if "|c" in value.lower() and not value.lower().rstrip().endswith("|r"):
            findings["missing_final_reset"].append(key)

    wts_rows = []
    constant_localization_only = (len(localization_mentions) == len(constant_localizations)
                                  and not dynamic_localization_references)
    for sid, value in sorted(strings.items()):
        roles = sorted({objects[r["object"]]["role"] if "object" in r else "runtime_or_metadata"
                        for r in refs[sid]})
        technical_only = bool(roles) and set(roles) <= set(TECHNICAL_FIELDS.values())
        wts_rows.append(dict(sid=sid, text=value, references=refs[sid], roles=roles,
                             classification="technical_or_editor" if technical_only else "referenced" if refs[sid]
                             else "unreferenced_legacy_storage" if constant_localization_only else "unreferenced_requires_review",
                             exclusion_reason="No reference in stored object fields, binary metadata, interface files or Lua; localization natives use only constant keys. Retained without editing."
                             if not refs[sid] and constant_localization_only else None))
        if (re.search(r"[A-Za-z]{3,}", plain(value)) and not technical_only
                and (refs[sid] or not constant_localization_only)):
            findings["wts_latin_review"].append(sid)
    # Text is normalized in the WTS table; references use zero-based object indexes.
    stored_objects = [{k: v for k, v in row.items()
                       if k != "raw" and not (k == "text" and "sid" in row)} for row in objects]
    inventory = dict(schema=1, sources=sources, wts=wts_rows, objects=stored_objects,
                     lua_candidates=lua_strings, interface_lines=interface,
                     localization_key_audit=dict(mentions=localization_mentions, constant_calls=constant_localizations,
                                                  dynamic_references=dynamic_localization_references,
                                                  constant_keys_only=constant_localization_only),
                     limitations=["Stored overrides only; inherited CASC text requires effective SD/HD readback.",
                                  "Race ownership is a techtree hint, not runtime reachability proof.",
                                  "Lua candidates include debug strings and require sink review.",
                                  "Unreferenced WTS are excluded only while the stored reference and constant localization key audit remains valid; they are never deleted."])
    report = dict(schema=1, sources=sources,
                  counts=dict(wts=len(strings), referenced_wts=sum(bool(refs[sid]) for sid in strings),
                              object_text_fields=sum(r["role"] == "ui_text" for r in objects),
                              stored_string_references=len(objects),
                              unreferenced_wts=sum(not refs[sid] for sid in strings),
                              unreferenced_wts_excluded=constant_localization_only,
                              field_roles=dict(collections.Counter(r["role"] for r in objects)), lua_candidates=len(lua_strings),
                              lua_classifications=dict(collections.Counter(r["classification"] for r in lua_strings)),
                              interface_lines=len(interface)),
                  findings=dict(findings), finding_counts={k: len(v) for k, v in findings.items()},
                  completion_proven=False,
                  remaining=["Classify unresolved fields and Lua candidates; review Latin exceptions explicitly.",
                             "Review effective inherited SD/HD fields and all levels.",
                             "Reconcile descriptions and building lists against current mechanics."])
    effective_path = OUT / "global_effective.json"
    if effective_path.exists():
        effective = json.loads(effective_path.read_text(encoding="utf-8"))
        current = all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest
                      for name, digest in effective["sources"].items())
        effective_findings = collections.defaultdict(list)
        for i, row in enumerate(effective["rows"]):
            value = row["text"]
            text = plain(value or "")
            if not text or text == "_":
                continue
            field = re.sub(r"\d+$", "", row["field"])
            if re.search(r"[A-Za-z]{3,}", text):
                effective_findings["latin_review"].append(i)
            if field in {"tip", "untip", "researchtip", "awakentip", "revivetip"} and re.match(
                    r"(?:Нанять|Обучить|Призвать|Исследовать|Изучить|Улучшить до|Построить|Купить|Воскресить|Вырастить|Train|Hire|Summon|Research|Learn|Upgrade to|Build|Resurrect)\s", text, re.I):
                effective_findings["short_command_prefix"].append(i)
            if field in {"ubertip", "unubertip", "researchubertip", "buffubertip"} and not re.match(r"[А-ЯЁ /-]+:", text):
                effective_findings["missing_type_label"].append(i)
        report["effective"] = dict(sources_current=current, findings=dict(effective_findings),
                                   counts={k: len(v) for k, v in effective_findings.items()},
                                   race_linked_counts={k: sum(bool(effective["rows"][i]["races"]) for i in v)
                                                       for k, v in effective_findings.items()},
                                   note="Indexes refer to global_effective.json rows; includes unused standard objects and both variants.")
        report["building_list_review"] = building_list_review(effective)
    write_json(OUT / "global_inventory.json", inventory)
    write_json(OUT / "global_audit.json", report)
    print(json.dumps({"counts": report["counts"], "findings": report["finding_counts"]}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-batch", type=Path)
    parser.add_argument("--effective", action="store_true")
    parser.add_argument("--prepare-short-names", action="store_true")
    parser.add_argument("--refresh-effective-wts", action="store_true")
    parser.add_argument("--prepare-menu-batch", type=Path)
    args = parser.parse_args()
    if args.verify_batch:
        verify_batch(args.verify_batch)
    elif args.effective:
        effective_inventory()
    elif args.prepare_short_names:
        prepare_short_names()
    elif args.refresh_effective_wts:
        refresh_effective_wts()
    elif args.prepare_menu_batch:
        prepare_menu_batch(args.prepare_menu_batch)
    else:
        main()
