"""Prepare shared interface strings visible while playing Faceless."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    wts = load_wts_strings()
    values = {
        12089: "|cffa6afb8Пища|r",
        11089: "|cffa6afb8Доход золота|r",
        19833: "|cffe4cfa3Справка|r [|cffffffffF9|r]",
        19831: "|cffe4cfa3Справка|r",
        17185: "|cffa6afb8ИНТЕРФЕЙС:|cffced4da Показывает текущее потребление пищи и доступный предел.|r",
        11093: "|cffa6afb8ИНТЕРФЕЙС:|cffced4da Доход и расходы определяются экономикой карты. Подробности доступны в панели дохода.|r",
        11092: "|cffe4cfa3" + "23 Race Legion|r",
        11091: "|cffe4cfa3" + "23 Race Legion|r",
        11090: "|cffe4cfa3" + "23 Race Legion|r",
        19832: "|cffe4cfa3Справка|r",
    }
    rows = [dict(rawcode="FrameDef", field=str(sid), reference_before="TRIGSTR_" + str(sid), before=wts[sid], after=value) for sid, value in values.items()]
    inv = dict(scope="Десять общих строк FrameDef, используемых в интерфейсе Безликих и остальных рас",
               strings=rows, in_game_checked=False,
               evidence=["All ten WTS references occur only in war3mapSkin.txt among root object data / map-info / text files",
                         "60_income_tooltip.lua replaces upkeep/supply tooltips with income/state panels"],
               exceptions=["23 Race Legion is the map's existing proper name"],
               verification_owner="Пользователь выполняет игровые проверки самостоятельно; они не являются условием задачи агента")
    (folder / "faceless_interface.json").write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    before = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A01C", "--fields", "name,tip1,ubertip1,code,dataa1"]))
    old = before["objects"][0]["fields"]
    assert old["code"] == "Aakb" and float(old["dataa1"]) == 0
    title = "|cffe4cfa3Свечение героя|r"
    ops = [dict(type="ability", id="A01C", field=k, value=v) for k, v in {
        "name": title, "tip1": title,
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Декоративное свечение героя. Не повышает урон от атак.|r"}.items()]
    (folder / "faceless_cosmetic_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_cosmetic.json").write_text(json.dumps(dict(scope="Декоративная способность четырёх героев Безликих", objects_before=before,
        strings=[dict(rawcode="A01C", field=o["field"], before=old[o["field"]], after=o["value"]) for o in ops],
        in_game_checked=False), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
