"""Prepare transport commands and unambiguous native ship abilities."""
import json
from pathlib import Path

from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    before = json.loads((folder / "faceless_naval_abilities_before.json").read_text(encoding="utf-8"))
    names = {"A00I": "Магическая посадка", "A00A": "Починка", "A00B": "Тактическое ускорение",
             "Sch5": "Грузовой отсек", "Slo3": "Посадка на борт", "Sdro": "Высадка",
             "A002": "Боковые пушки фрегата", "A003": "Боковые пушки линкора", "A1PP": "Прицельная пальба"}
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    white = lambda v: "|cffffffff" + str(v) + "|cffced4da"
    bonus = lambda v: "|cffc8e087+" + str(v) + "|cffced4da"
    penalty = lambda v: "|cffe69a8d+" + str(v) + "|cffced4da"
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        title = "|cffe4cfa3" + names[code] + "|r"
        values = {"name": title}
        for level in range(1, int(old["levels"]) + 1):
            data = lambda f: format(float(old[f + str(level)]), "g").replace(".", ",")
            if code == "A00I":
                body = ("Перемещает подходящие войска игрока из радиуса " + white(250) + " вокруг выбранной точки к выбранным транспортам того же типа и отдаёт приказ посадки. "
                        "Распределяет войска по свободным местам: до " + white(10) + " на транспорт. Успех посадки зависит от допустимости груза и доступности места высадки у корабля.")
            elif code == "Sch5":
                body = "Позволяет перевозить наземные союзные войска. Вместимость — " + white(10) + " мест. Для посадки и высадки используются отдельные команды."
            elif code == "Slo3":
                body = "Принимает на борт выбранного наземного союзника при наличии свободного места в грузовом отсеке."
            elif code == "Sdro":
                body = "Высаживает перевозимые войска в указанном месте, если местность позволяет разместить их."
            elif code == "A00B":
                move = round(float(old["dataa" + str(level)]) * 100)
                taken = round(float(old["datac" + str(level)]) * 100)
                body = ("На " + white(data("dur")) + " сек. даёт " + bonus(str(move) + "%") + " к скорости передвижения. "
                        "Получаемый кораблём урон увеличивается на " + penalty(str(taken) + "%") + ". Требует исследования «Дополнительные паруса».")
            elif code == "A00A":
                body = ("Во время поддержания восстанавливает " + white(data("dataa")) + " здоровья каждые " + white(data("datab"))
                        + " сек. подходящим союзным и нейтральным целям в радиусе " + white(data("area")) + ", включая сам корабль. "
                        "Длительность — до " + white(data("dur")) + " сек. Корабль не может использовать главные орудия, пока поддерживает способность. Требует исследования «Починка».")
                if level > 1:
                    body += " В начале применения корабль получает неуязвимость на " + white(data("datad")) + " сек."
            elif code in ("A002", "A003"):
                body = ("Автоматически стреляет по вражеским механическим целям в радиусе " + white(data("area")) + ", нанося "
                        + white(data("dataa")) + " урона за попадание. Интервал выстрелов — " + white(data("cool"))
                        + " сек. Дополнительные пушки могут стрелять во время движения корабля.")
                if code == "A003":
                    body += " Требует исследования «Обстрел»."
            else:
                body = ("Наносит выбранному наземному или воздушному органическому противнику " + white(data("dataa"))
                        + " урона и оглушает на " + white(data("dur")) + " сек.; героя — на " + white(data("herodur")) + " сек.")
            if code not in ("A002", "A003", "Sch5", "Slo3", "Sdro"):
                body += "|n|n|cffa6afb8Перезарядка:|cffced4da " + white(data("cool")) + " сек."
            if int(old["levels"]) > 1:
                body += "|n|n|cffa6afb8Уровень:|cffced4da " + white(level) + " из " + white(old["levels"]) + "."
            key = resolve(old.get("hotkey", "")).strip('"')
            values["tip" + str(level)] = title + (" (|cffffffff" + key + "|r)" if key else "")
            values["ubertip" + str(level)] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"
        for field, value in values.items():
            op = dict(type="ability", id=code, field=field, value=value)
            if code == "Sch5":
                op["base_object"] = True
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))
    inventory = dict(scope="Девять общих корабельных способностей, все объявленные уровни", strings=strings,
                     objects_before=before, in_game_checked=False,
                     evidence=["Native ability data and installed AbilityMetaData: AEtq, Absk, Apxf",
                               "06_transport_portals.lua Trig_MassPosadka2: actual radius 250; transport capacity 10"],
                     remaining=["Check transport loading, channelled repair and initial immunity in engine",
                                "Verify native side-gun firing while moving and actual ability-level assignment",
                                "Flagship, boarding and cluster bombardment remain separate unfinished objects"])
    for filename, value in (("faceless_naval_abilities", inventory), ("faceless_naval_abilities_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
