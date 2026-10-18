"""Prepare the three passive abilities used by the first Faceless unit batch."""
import json
from pathlib import Path

from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    fields = ("name,tip1,ubertip1,code,levels,requires,targs1,dataa1,datab1,datac1,"
              "datad1,datae1,dur1,herodur1")
    objects = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A10X,A10W,A10Z",
                           "--fields", fields]))["objects"]
    wts = load_wts_strings()
    specs = {
        "A10X": ("Разрушение Эфира", "При атаке сжигает до |cffffffff20|cffced4da ед. маны "
                  "у обычного противника или до |cffffffff10|cffced4da ед. у героя. "
                  "Каждая сожжённая единица маны наносит |cffffffff2|cffced4da ед. урона."
                  "|n|n|cffe6c07bТребуется исследование «Разрушение Эфира»."),
        "A10W": ("Сотрясение Бездны", "С вероятностью |cffffffff10%|cffced4da атака наносит "
                  "|cffffffff10|cffced4da дополнительного урона и оглушает цель на "
                  "|cffffffff0,5|cffced4da сек. Герои оглушаются на |cffffffff0,2|cffced4da сек."
                  "|n|n|cffe6c07bТребуется исследование «Улучшение Сущности»."),
        "A10Z": ("Сила Бездны", "С вероятностью |cffffffff15%|cffced4da атака наносит "
                  "|cffffffff1,9|cffced4da-кратный урон."),
    }
    operations, strings = [], []
    for obj in objects:
        name, body = specs[obj["id"]]
        values = {"name": "|cffe4cfa3" + name + "|r", "tip1": "|cffe4cfa3" + name + "|r",
                  "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            before = obj["fields"][field]
            resolved = wts[int(before[8:])] if before.startswith("TRIGSTR_") else before
            strings.append(dict(rawcode=obj["id"], field=field, reference_before=before,
                                before=resolved, after=value))
            operations.append(dict(type="ability", id=obj["id"], field=field, value=value))
    folder = ROOT / "docs/ui_text"
    inventory = dict(scope="Безликие: три пассивные способности; только единственный действующий уровень",
                     variants=["SD", "HD"], in_game_checked=False, objects_before=objects,
                     strings=strings, remaining=["Остальные способности, эффекты и уровни", "Проверка в игре"])
    for name, value in [("faceless_abilities_01", inventory),
                        ("faceless_abilities_01_plan", dict(operations=operations))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
