"""Prepare the four custom statuses used by Faceless spells."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    specs = {
        "B01I": ("Метка охотника", "Броня |cffe69a8dснижена|cffced4da. Отмеченную цель видит наложивший метку противник, даже если цель невидима."),
        "B02L": ("Взрыв бездны", "Цель находится под действием пламени Бездны и получает |cffe69a8dпериодический урон|cffced4da."),
        "B08E": ("Аура Бездны", "Аура Бездны |cffe69a8dснижает восстановление здоровья|cffced4da цели."),
        "B08F": ("Дымка бездны", "Скорость передвижения повышена на |cffc8e0876%|cffced4da, восстановление здоровья — на |cffc8e0871,5|cffced4da ед. в секунду."),
    }
    before = require(cli(["get-objects-bulk", "--type", "buff", "--ids", ",".join(specs), "--fields", "editorname,bufftip,buffubertip"]))
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    strings, ops = [], []
    for obj in before["objects"]:
        name, body = specs[obj["id"]]
        values = {"editorname": "|cffe4cfa3" + name + "|r", "bufftip": "|cffe4cfa3" + name + "|r", "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            ops.append(dict(type="buff", id=obj["id"], field=field, value=value))
            strings.append(dict(rawcode=obj["id"], field=field, before=resolve(obj["fields"][field]), after=value))
    inv = dict(scope="Четыре собственных эффекта безликих; общие стандартные эффекты ещё не охвачены", objects_before=before,
               variants=["SD", "HD"], strings=strings, in_game_checked=False,
               remaining=["Общие стандартные эффекты: проверить использование разными способностями до перевода", "Проверить иконки эффектов и отображение в игре"])
    folder = ROOT / "docs/ui_text"
    for name, value in [("faceless_custom_buffs", inv), ("faceless_custom_buffs_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
