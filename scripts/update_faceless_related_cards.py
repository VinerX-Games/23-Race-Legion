"""Fix related card terminology and the Fragmentation Shards tooltip."""
import json
from pathlib import Path
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    text = ("|cffa6afb8СПОСОБНОСТЬ:|cffced4da Осколки поражают наземных врагов вокруг цели атаки: "
            "|cffffffff25|cffced4da урона в радиусе |cffffffff100|cffced4da, "
            "|cffffffff15|cffced4da урона на расстоянии от |cffffffff100|cffced4da до |cffffffff225|cffced4da "
            "и |cffffffff10|cffced4da урона дальше, до радиуса |cffffffff275|cffced4da."
            "|n|n|cffe6c07bТребуется второй уровень «Знания проклинателей».|r")
    spell = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A16P", "--fields", "name,tip1,ubertip1,area1,dataa1,datab1,datac1,datad1,datae1,requires,requiresamount"]))["objects"][0]
    ops, strings = [], []
    values = {"name": "|cffe4cfa3Пронзание|r", "tip1": "|cffe4cfa3Пронзание|r", "ubertip1": text}
    for field, value in values.items():
        ops.append(dict(type="ability", id="A16P", field=field, value=value))
        strings.append(dict(rawcode="A16P", field=field, before=resolve(spell["fields"][field]), after=value))
    plan = dict(operations=ops)
    (folder / "faceless_shards_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    metadata = dict(source="Warcraft III CASC: units/abilitymetadata.slk, ui/worldeditstrings.txt", ability="Afsh",
                    fields={"area": "Full damage radius", "flk1/dataa": "Medium Damage Radius", "flk2/datab": "Small Damage Radius", "flk3/datac": "Full Damage Amount", "flk4/datad": "Medium Damage Amount", "flk5/datae": "Small Damage Amount"})
    (folder / "faceless_shards.json").write_text(json.dumps(dict(scope="Пронзание", objects_before=[spell], strings=strings, metadata=metadata, in_game_checked=False), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    objects = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h0I1,h0I2,h0I4,h0I6,h0HZ,h0I7,h0I8,h0K2", "--fields", "ubertip,isbldg"]))["objects"]
    ops, strings = [], []
    replacements = {"Развить силу": "Развитие силы", "Развить скорость": "Развитие скорости", "Развить Скорость": "Развитие скорости", "Наращивание Мышц": "Наращивание мышц"}
    for obj in objects:
        before = resolve(obj["fields"]["ubertip"])
        after = before
        for old, new in replacements.items():
            after = after.replace(old, new)
        if obj["id"] == "h0K2":
            after = after.replace("усиливает урон по целям без брони и со средней бронёй", "поражает наземных врагов вокруг цели атаки осколками")
        if before != after:
            marker = "ЗДАНИЕ:" if obj["fields"]["isbldg"] == "1" else "ЮНИТ:"
            ops.append(dict(type="unit", id=obj["id"], field="ubertip", value=after, marker=marker))
            strings.append(dict(rawcode=obj["id"], field="ubertip", before=before, after=after))
    (folder / "faceless_related_cards_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_related_cards.json").write_text(json.dumps(dict(scope="Связанные списки зданий и карточка проклинателя", objects_before=objects, strings=strings, in_game_checked=False), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
