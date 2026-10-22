"""Экспорт базы зависимостей рас (дерево технологий) из object data и Lua карты.

Источник истины — карта: object data (через HiveWE_cli describe-race / dump-objects)
и Lua-триггеры выбора расы. Результат — docs/techtree/races/<Раса>.json и
docs/techtree/index.json; руками эти файлы не править.

    python scripts/export_techtree.py           # перегенерировать базу
    python scripts/export_techtree.py --check   # сверить базу с картой (exit 1 при расхождении)

Нужен HiveWE_cli (путь — wc3.local.json / переменная HIVEWE_CLI, см. docs/TOOLING_WORKFLOW.md).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wc3_object_tools import cli, require  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "map.w3x"
OUT = ROOT / "docs" / "techtree"
RACE_TRIGGERS = MAP / "_lua/monolith_split/sections/80_runtime/triggers/04_race_selection.lua"
SKIP_RACES = {"Random"}  # случайный выбор — объединение всех рас, отдельный файл не нужен

FIELDS = {
    "unit": "name,goldcost,lumbercost,fused,fmade,hp,bldtm,hotkey,requires,requires1,requiresamount,dependencyor,researches,upgrades",
    "upgrade": "name,maxlevel,goldbase,goldmod,lumberbase,lumbermod,timebase,timemod,hotkey,requires,requires1,requiresamount",
    "ability": "name,hero,item,levels,reqlevel,hotkey,requires,requiresamount",
    "item": "name,goldcost,lumbercost,hotkey,requires",
}
# поле object data -> ключ в базе
RENAME = {"goldcost": "gold", "lumbercost": "lumber", "fused": "food", "fmade": "food_made",
          "bldtm": "time", "goldbase": "gold", "goldmod": "gold_per_level", "lumberbase": "lumber",
          "lumbermod": "lumber_per_level", "timebase": "time", "timemod": "time_per_level",
          "maxlevel": "levels", "reqlevel": "hero_level_req", "requiresamount": "requires_amount",
          "dependencyor": "equivalents"}
LIST_FIELDS = {"requires", "requires1", "dependencyor", "researches", "upgrades"}
LIST_KEYS = {"requires1": "requires", "dependencyor": "equivalents", "upgrades": "affected_by"}
COLOR = re.compile(r"\|c[0-9a-fA-F]{8}|\|r")


def plain(text):
    return COLOR.sub("", text or "").strip()


def load_wts():
    text = (MAP / "war3map.wts").read_bytes().decode("utf-8-sig", "replace")
    return {int(m.group(1)): m.group(2) for m in
            re.finditer(r"STRING (\d+)[^\n]*\r?\n(?://[^\n]*\r?\n)?\{\r?\n(.*?)\r?\n\}", text, re.S)}


def race_tokens():
    names = re.findall(r"function Trig_Race_([A-Za-z0-9_]+)_Actions", RACE_TRIGGERS.read_text(encoding="utf-8"))
    tokens = []
    for name in names:
        token = name[:-2] if name.endswith("_O") else name
        if token not in SKIP_RACES and token not in tokens:
            tokens.append(token)
    return tokens


def object_fields(ids_by_kind, wts):
    """Поля object data для набора id, сгруппированных по типу."""
    result = {}
    for kind, ids in ids_by_kind.items():
        ids = sorted(ids)
        for start in range(0, len(ids), 200):
            data = require(cli(["get-objects-bulk", "--type", kind, "--ids", ",".join(ids[start:start + 200]),
                                "--fields", FIELDS[kind]]))
            for obj in data["objects"]:
                fields = {}
                # The effective display name may be returned at object level
                # even when the unnumbered name field is empty (e.g. kt01).
                # Do not preserve an empty describe-race label in that case.
                effective_name = plain(obj.get("name", ""))
                if effective_name:
                    fields["name"] = effective_name
                for key, value in obj["fields"].items():
                    value = (value or "").strip()
                    if value.startswith("TRIGSTR_"):
                        value = wts.get(int(value[8:]), "")
                    if key == "name" or value in ("", "-", "0") and key not in ("hero", "item"):
                        continue
                    if key in LIST_FIELDS:
                        target = fields.setdefault(LIST_KEYS.get(key, key), [])
                        target += [x for x in value.split(",") if x and x not in target]
                        continue
                    if key in ("hero", "item"):
                        if value == "1":
                            fields[key] = True
                        continue
                    fields[RENAME.get(key, key)] = int(value) if re.fullmatch(r"-?\d+", value) else value
                result[obj["id"]] = fields
    return result


def category(node):
    cat = node["category"]
    if cat == "unit" and node["id"][:1].isupper():
        return "hero"
    return cat


def normalize_research_edges(edges, nodes, fields):
    """The CLI graph conflates research menus with UnitData 'Upgrades Used'.

    Reconstruct these two relations from their distinct effective object fields.
    An altar affected by masonry does not offer masonry in its command card.
    """
    unit_ids = {oid for oid, node in nodes.items() if node["category"] in {"unit", "building"}}
    result = {edge for edge in edges
              if not (edge.split(" ", 2)[0] in unit_ids and edge.split(" ", 2)[1] == "researches")}
    for oid in sorted(unit_ids):
        for field, relation in (("researches", "researches"), ("affected_by", "affected-by")):
            for target in fields.get(oid, {}).get(field, []):
                result.add(f"{oid} {relation} {target}")
    return result


def export_race(token, wts):
    data = require(cli(["describe-race", "--suffix", token]))
    view = data["agent_view"]
    nodes = {n["id"]: n for n in data["nodes"] if n["category"] != "race"}
    edges = set()
    for e in data["edges"]:
        kind = e["kind"]
        if kind == "has-ability" and e.get("detail") == "heroabillist":
            kind = "hero-ability"
        edges.add(f"{e['from']} {kind} {e['to']}")

    kinds = {"unit": set(), "upgrade": set(), "ability": set(), "item": set()}
    for node in nodes.values():
        kind = {"building": "unit", "unit": "unit"}.get(node["category"], node["category"])
        if kind in kinds:
            kinds[kind].add(node["id"])
    # describe-race can classify valid non-R upgrade IDs (kt01, PA85, ...)
    # as unknown. The typed research relation tells us which object table to
    # query; promote the node only if that read actually returns an object.
    unknown_researches = {edge.split(" ", 2)[2] for edge in edges
                         if edge.split(" ", 2)[1] in {"researches", "lua-start-tech", "affected-by"}
                         and nodes.get(edge.split(" ", 2)[2], {}).get("category") == "unknown"}
    unknown_abilities = {edge.split(" ", 2)[2] for edge in edges
                         if edge.split(" ", 2)[1] in {"has-ability", "hero-ability"}
                         and nodes.get(edge.split(" ", 2)[2], {}).get("category") == "unknown"}
    # A graph keyed solely by rawcode cannot disambiguate conflicting typed
    # references. Keep those unknown instead of borrowing another table's read.
    ambiguous = unknown_researches & unknown_abilities
    unknown_researches -= ambiguous
    unknown_abilities -= ambiguous
    kinds["upgrade"].update(unknown_researches)
    kinds["ability"].update(unknown_abilities)
    fields = object_fields(kinds, wts)
    for oid in unknown_researches & fields.keys():
        nodes[oid]["category"] = "upgrade"
    for oid in unknown_abilities & fields.keys():
        nodes[oid]["category"] = "ability"
    edges = normalize_research_edges(edges, nodes, fields)

    # требования — тоже рёбра графа; недостающие цели подтягиваем как узлы
    extra = {"unit": set(), "upgrade": set()}
    missing_menu = set()
    for oid, f in fields.items():
        for tech in f.get("researches", []):
            if tech not in nodes:
                missing_menu.add(tech)
                extra["upgrade"].add(tech)
        for req in f.get("requires", []):
            edges.add(f"{oid} requires {req}")
            if req not in nodes:
                extra["upgrade" if req[:1] == "R" else "unit"].add(req)
    if any(extra.values()):
        found = object_fields(extra, wts)
        for oid in set().union(*extra.values()):
            kind = "upgrade" if oid in extra["upgrade"] else "unit"
            nodes.setdefault(oid, {"id": oid, "category": kind if oid in found else "unknown",
                                   "name": "", "base_id": "", "source": "researches" if oid in missing_menu else "requires"})
            if oid in found:
                fields.setdefault(oid, found[oid])

    objects = {}
    for oid in sorted(nodes):
        node = nodes[oid]
        entry = {"type": category(node), "name": plain(node.get("name"))}
        if node.get("base_id") and node["base_id"] != oid:
            entry["base"] = node["base_id"]
        if node.get("source") == "requires":
            entry["only_required"] = True
        entry.update(fields.get(oid, {}))
        objects[oid] = entry

    lua = sorted({(Path(s["file"]).resolve().relative_to(ROOT).as_posix(), s["symbol"])
                  for s in view.get("lua_sections", []) if not s["file"].endswith("war3map.lua")})
    return {
        "race": token,
        "start_units": sorted(u["id"] for u in view.get("start_units", [])),
        "start_tech": sorted(u["id"] for u in view.get("start_tech", [])),
        "lua": [{"file": f, "symbol": s} for f, s in lua],
        "objects": objects,
        "edges": sorted(edges),
    }


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="только сверить, ничего не писать")
    args = parser.parse_args()

    wts = load_wts()
    files = {}
    index = []
    for token in race_tokens():
        race = export_race(token, wts)
        files[f"races/{token}.json"] = dump(race)
        counts = {}
        for obj in race["objects"].values():
            counts[obj["type"]] = counts.get(obj["type"], 0) + 1
        index.append({"race": token, "file": f"races/{token}.json", "start_units": race["start_units"],
                      "counts": dict(sorted(counts.items()))})
    files["index.json"] = dump({"generated_by": "scripts/export_techtree.py", "races": index})

    # git с autocrlf отдаёт файлы с CRLF — сравниваем без учёта переводов строк
    stale = [p for p, text in files.items()
             if not (OUT / p).exists() or (OUT / p).read_text(encoding="utf-8").replace("\r\n", "\n") != text]
    extra = [p.relative_to(OUT).as_posix() for p in (OUT / "races").glob("*.json")
             if p.relative_to(OUT).as_posix() not in files] if (OUT / "races").exists() else []
    if args.check:
        for p in stale:
            print(f"устарел: docs/techtree/{p}")
        for p in extra:
            print(f"лишний: docs/techtree/{p}")
        print("OK: база зависимостей совпадает с картой" if not stale and not extra
              else "База зависимостей устарела: python scripts/export_techtree.py")
        return 1 if stale or extra else 0
    for p in stale:
        target = OUT / p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(files[p], encoding="utf-8", newline="\n")
    for p in extra:
        (OUT / p).unlink()
    print(f"рас: {len(index)}, обновлено файлов: {len(stale)}, удалено: {len(extra)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
