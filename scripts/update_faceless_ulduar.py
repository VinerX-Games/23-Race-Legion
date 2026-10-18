"""Prepare Ulduar and its shared city commands from current object data/Lua."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    names = {"A0MK": "Разведка", "A0B0": "Укрепление города", "A0B1": "Развитие производства",
             "A0B2": "Расширение города", "A0AZ": "Увеличение сбора дани", "AHad": "Поселение",
             "A0AY": "Сбор дани", "A0B5": "Налаженное производство"}
    fields = ["name", "levels", "hotkey", "code", "dataa1", "datab1", "dataf1", "dur1", "area1", "cool1"]
    fields += [f"{f}{n}" for f in ("tip", "ubertip") for n in range(1, 6)]
    before = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(names), "--fields", ",".join(fields)]))
    unit = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h0DR", "--fields", "name,tip,ubertip,hotkey,trains,abillist,weapson"]))
    buff = require(cli(["get-objects-bulk", "--type", "buff", "--ids", "B023", "--fields", "bufftip,buffubertip"]))
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    white = lambda s: "|cffffffff" + str(s) + "|cffced4da"
    bonus = lambda s: "|cffc8e087+" + str(s) + "|cffced4da"
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"
    ops, strings = [], []

    def add(kind, code, old, values, marker=None):
        for field, value in values.items():
            op = dict(type=kind, id=code, field=field, value=value)
            if marker:
                op["marker"] = marker
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))

    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        title = "|cffe4cfa3" + names[code] + "|r"
        values = {"name": title}
        for level in range(1, int(old["levels"]) + 1):
            if code == "A0MK":
                body = ("Открывает обзор в выбранной области радиусом " + white(1000) + " на " + white(50)
                        + " сек. и обнаруживает невидимые войска. Перезарядка — " + white(30) + " сек.")
            elif code in ("A0B0", "A0B2"):
                body = ("Команда " + ("укрепления защиты" if code == "A0B0" else "расширения") + " города."
                        "|n|n|cffe69a8dУлучшение в текущей версии недоступно.|cffced4da "
                        + ("Применение не повышает броню здания." if code == "A0B0" else "Применение не повышает максимальное здоровье здания."))
            elif code in ("A0B1", "A0AZ"):
                gold = code == "A0AZ"
                body = ("Повышает вклад поселения в " + ("базовый доход золота" if gold else "доход древесины")
                        + " за каждый доходный цикл на " + bonus(100 if gold else 50) + ". "
                        + ("Итоговый доход золота зависит от модификаторов экономики. " if gold else "")
                        + "При применении поселение должно оставаться выделенным."
                        + "|n|nСтоимость — " + white(int(float(old["dataa1"]))) + " золота и "
                        + white(int(float(old["datab1"]))) + " древесины. Доступность команды зависит от текущей ступени развития поселения.")
            elif code in ("A0AY", "A0B5"):
                gold = code == "A0AY"
                body = ("Вклад этой ступени развития поселения в " + ("базовый доход золота" if gold else "доход древесины")
                        + " за каждый доходный цикл: " + bonus(level * (100 if gold else 50))
                        + ". Это суммарное значение ступени, а не прибавка к предыдущей."
                        + (" Итоговый доход золота зависит от модификаторов экономики." if gold else "")
                        + "|n|n|cffa6afb8Ступень:|cffced4da " + white(level) + ".")
            else:
                body = "Обозначает поселение. Эта аура не даёт бонуса к броне."
            key = resolve(old.get("hotkey", "")).strip('"')
            values["tip" + str(level)] = title + (" (|cffffffff" + key + "|r)" if key else "")
            values["ubertip" + str(level)] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"
        add("ability", code, old, values)
    obj = unit["objects"][0]
    old = obj["fields"]
    assert old["trains"] == "U02F" and old["abillist"] == "A0MK,A0B0,A0B1,A0B2,A0AZ,AHad" and old["weapson"] == "0"
    title = "|cffe4cfa3Ульдуар (внешний)|r"
    body = ("|cffa6afb8ЗДАНИЕ:|cffced4da Поселение, в котором Безликие могут нанять легендарного героя."
            "|n|n|cffa6afb8Герои:|cffced4da|n- " + ref("Верховный генерал") + ": требуется выбор расы Безликих."
            "|n|n|cffa6afb8Возможности:|cffced4da"
            "|n- " + ref("Разведка") + ": временно открывает обзор и обнаруживает невидимые войска."
            "|n- " + ref("Увеличение сбора дани") + ": повышает базовый доход золота поселения."
            "|n- " + ref("Развитие производства") + ": повышает доход древесины поселения."
            "|n- " + ref("Поселение") + ": городская аура без бонуса к броне."
            "|n|n|cffe6c07bУкрепление и расширение города в текущей версии недоступны.|r")
    add("unit", "h0DR", old, {"name": title, "tip": title + " (|cffffffffU|r)", "ubertip": body}, "ЗДАНИЕ:")
    old = buff["objects"][0]["fields"]
    add("buff", "B023", old, {"bufftip": "|cffe4cfa3Поселение|r",
                               "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Городская аура. Не изменяет броню здания.|r"})
    inventory = dict(scope="Ульдуар (внешний), шесть общих команд/аур и два динамических показателя дохода всех пяти уровней",
                     objects_before=[before, unit, buff], strings=strings, in_game_checked=False,
                     evidence=["01_core_economy.lua Trig_Upgrade_Gold_C and Trig_Upgrade_Lumber: income increments and selected-unit guards",
                               "54_count_dis.lua: city income equals A0AY level * 100, A0B5 level * 50",
                               "A0B0/A0B2 only referenced by removal in canonical Lua; AAns native only charges resources",
                               "Native A0MK duration 50, area 1000; AHad armor bonus zero; U02F requires R0F9"],
                     remaining=["Check city capture/replacement and recruitment gates in Warcraft III",
                                "Check resource charging, unavailable armor/health commands and income progression in engine",
                                "Automatic legendary grant maps h0DR to Demons, conflicting with the player's Faceless recruitment route; mechanics untouched",
                                "Audit related income/status buffs and other shared city text; no whole-map completion claimed"])
    for filename, value in (("faceless_ulduar", inventory), ("faceless_ulduar_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
