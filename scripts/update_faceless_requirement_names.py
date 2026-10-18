"""Localize names shown by inherited requirement lines, without changing external techs."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent


def main():
    names = {"Rugf": "Ярость вурдалака", "Rhrt": "Залповый огонь", "Rhlh": "Улучшенная лесозаготовка", "Rhan": "Дрессировка животных"}
    before = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(names), "--fields", "maxlevel," + ",".join("name" + str(n) for n in range(1, 7))]))
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    ops, strings = [], []
    for obj in before["objects"]:
        for n in range(1, int(obj["fields"]["maxlevel"]) + 1):
            field = "name" + str(n)
            value = "|cffe4cfa3" + names[obj["id"]] + "|r"
            ops.append(dict(type="upgrade", id=obj["id"], field=field, value=value, base_object=True))
            strings.append(dict(rawcode=obj["id"], field=field, before=resolve(obj["fields"][field]), after=value))
    folder = ROOT / "docs/ui_text"
    inventory = dict(scope="Подписи внешних требований, автоматически отображаемые у способностей Безликих и общих показателей дохода",
                     objects_before=before, strings=strings, in_game_checked=False,
                     evidence=["checkdep=1 and requires on A0AY/A0B5/A0SM/A122/A0T3/A1N5/A1R3",
                               "Research menus of these other factions are outside the Faceless tree; only the names visible as requirements are migrated here"],
                     limitations=["Requirements and gameplay effects are not removed or changed; inherited requirements may remain unavailable to Faceless"],
                     verification_owner="Игровые проверки выполняет пользователь")
    for filename, value in (("faceless_requirement_names", inventory), ("faceless_requirement_names_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
