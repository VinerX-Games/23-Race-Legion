"""Prepare all commands of the shared teleportation mage from native data/Lua."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    before = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A0IR,A0IO,A1IG,A1IH", "--fields", "name,tip1,ubertip1,hotkey,levels,code,dataa1,datab1,datac1,area1,cool1,cost1,targs1"]))
    white = lambda v: "|cffffffff" + str(v) + "|cffced4da"
    ref = lambda v: "|cffa9c7de" + v + "|cffced4da"
    restriction = "|n|n|cffe6c07bТёмный призыв недоступен, если маг находится в радиусе |cffffffff1350|cffe6c07b от вражеской столицы.|cffced4da"
    specs = {
        "A0IR": ("Массовая телепортация", "Через " + white(3) + " сек. переносит до " + white(15) + " воинов игрока из радиуса " + white(800) + ", включая самого мага, к выбранному союзному зданию."),
        "A0IO": ("Тёмный призыв", "Через " + white("0,1") + " сек. переносит до " + white(15) + " воинов игрока из выбранной области радиусом " + white(700) + " к магу. "
                  "При начале призыва маг получает неуязвимость на " + white("1,5") + " сек." + restriction),
        "A1IG": ("Поддержание связи", "Сохраняет выбранную точку и включает автоматические попытки применить " + ref("Тёмный призыв") + " из этой области. "
                  "Интервал попыток — не менее " + white(15) + " сек.; первая выполняется после первого интервала. Каждый призыв расходует " + white(100) + " маны. "
                  "Режим выключается кнопкой «Прекращение связи»." + restriction),
        "A1IH": ("Прекращение связи", "Отключает автоматические попытки " + ref("Тёмного призыва") + " из сохранённой точки и возвращает кнопку «Поддержание связи»."),
    }
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ops, strings = [], []
    for obj in before["objects"]:
        name, body = specs[obj["id"]]
        old = obj["fields"]
        assert old["levels"] == "1"
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old["hotkey"]).strip('"')
        values = {"name": title, "tip1": title + (" (|cffffffff" + key + "|r)" if key else ""), "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            ops.append(dict(type="ability", id=obj["id"], field=field, value=value))
            strings.append(dict(rawcode=obj["id"], field=field, before=resolve(old[field]), after=value))
    mage = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h07A", "--fields", "ubertip,abillist,weapson,targs1"]))
    old = mage["objects"][0]["fields"]
    text = ("|cffa6afb8ЮНИТ:|cffced4da Заклинатель для переброски войск игрока.|n|n|cffa6afb8Способности:|cffced4da"
            "|n- " + ref("Массовая телепортация") + ": переносит мага и ближайшие войска игрока к союзному зданию."
            "|n- " + ref("Тёмный призыв") + ": переносит войска игрока из выбранной области к магу."
            "|n- " + ref("Поддержание связи") + ": включает автоматические попытки Тёмного призыва из сохранённой точки; режим выключается кнопкой «Прекращение связи»."
            + restriction + "|n|nАтакует наземные и воздушные цели.|r")
    ops.append(dict(type="unit", id="h07A", field="ubertip", value=text, marker="ЮНИТ:"))
    strings.append(dict(rawcode="h07A", field="ubertip", before=resolve(old["ubertip"]), after=text))
    inv = dict(scope="Общий маг телепортации: все четыре команды и согласованная карточка", variants=["SD", "HD"], in_game_checked=False,
               objects_before=[before,mage], strings=strings,
               evidence=["06_transport_portals.lua: Trig_MageTp / Trig_TPrepeat / Trig_TPrepatStop / Trig_NoTpNearCapital", "Installed Warcraft III HumanAbilityStrings: AHmt count includes the caster", "AbilityMetaData: AHmt/AUds casting delay, maximum units, teleport clustering"],
               remaining=["В игре проверить таймер связи и проверку UnitAlive", "Проверить допустимые цели и задержки телепортации", "Проверить читаемость и состояние отмены в SD/HD"])
    for name, value in [("faceless_teleport_mage", inv), ("faceless_teleport_mage_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
