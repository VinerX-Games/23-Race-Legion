"""Prepare shared worker/building commands and the Yogg-Saron reward item."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    white = lambda v: "|cffffffff" + str(v) + "|cffced4da"
    green = lambda v: "|cffc8e087" + str(v) + "|cffced4da"
    coral = lambda v: "|cffe69a8d" + str(v) + "|cffced4da"
    ref = lambda v: "|cffa9c7de" + str(v) + "|cffced4da"
    specs = {
        "A0LJ": ("Обмен древесины на золото", "Обменивает " + coral(500) + " древесины на " + green(100) + " золота."),
        "A0LI": ("Обмен золота на древесину", "Обменивает " + coral(500) + " золота на " + green(100) + " древесины."),
        "A0IQ": ("Назначение столицы", "Назначает это здание столицей в соответствующем режиме игры. Завершает строительство, устанавливает " + white(10000) + " максимального и текущего здоровья и " + white(30) + " брони. "
                  "Положение столицы становится видно всем игрокам. Она получает Антимагическую броню и Неуязвимость столицы.|n|n|cffe6c07bПосле назначения кнопка становится недоступной.|cffced4da"),
        "Argl": ("Приём ресурсов", "Позволяет рабочим сдавать в это здание добытые золото и древесину."),
        "ANha": ("Добыча ресурсов", "Добывает золото из рудников и древесину из деревьев. За одну доставку переносит до " + white(10) + " золота или " + white(30) + " древесины. Объём переносимой древесины может быть увеличен исследованиями."),
        "Arst": ("Ремонт", "Восстанавливает здоровье дружественных зданий и механизмов, расходуя золото и древесину. Затраты зависят от ремонтной стоимости цели и восстановленного здоровья. Не действует на Древних."),
        "A1KB": ("Защита столицы", "В радиусе " + white(450) + " снижает восстановление здоровья органических врагов на " + white("2,5%") + " их максимального здоровья в секунду. Действует на наземные и воздушные цели."),
        "A15N": ("Зона ремонта", "Повышает восстановление здоровья дружественных наземных механизмов в радиусе " + white(550) + " на " + green("2,5") + " ед. в секунду."),
        "A0I6": ("Антимагическая броня", "Снижает получаемый урон от заклинаний на " + green("80%") + "."),
        "A145": ("Неуязвимость столицы", "Делает столицу неуязвимой на " + white(30) + " сек. Восстановление: " + white(360) + " сек."),
        "A0VG": ("Дар Йогг`Сарона", "Даёт герою " + green("+15") + " к силе, ловкости и интеллекту."),
        "A0VC": ("Касание безумия", "Открывает заклинания предмета.|n|n|cffa6afb8Содержит:|cffced4da|n- " + ref("Тёмное усиление") + ": временно повышает урон союзников.|n- " + ref("Порождение щупальца") + ": призывает Щупальце Йогг`Сарона."),
        "A0VD": ("Тёмное усиление", "На " + white(45) + " сек. повышает урон от атак союзников в радиусе " + white(500) + " на " + green("35%") + ". Действует также на владельца."),
        "A0VE": ("Порождение щупальца", "Призывает одно " + ref("Щупальце Йогг`Сарона") + " на " + white(180) + " сек. Оно атакует наземные цели и владеет Рассекающим ударом."),
        "A0VF": ("Аура отголоска Йогг`Сарона", "Органические союзники ближнего боя в радиусе " + white(1500) + " восстанавливают здоровье в размере " + green("10%") + " урона своих атак. Действует также на владельца, если он атакует в ближнем бою."),
    }
    fields = "name,tip1,ubertip1,untip1,unubertip1,hotkey,levels,code,area1,dataa1,datab1,datac1,datad1,datae1,unitid1,dur1,cool1,cost1,targs1"
    before = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(specs), "--fields", fields]))
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        name, body = specs[code]
        assert old["levels"] == "1", code
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old["hotkey"]).strip('"')
        tip = title + (" (|cffffffff" + key + "|r)" if key else "")
        values = {"name": title, "tip1": tip, "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"}
        if code == "Arst":
            values["untip1"] = tip
            values["unubertip1"] = values["ubertip1"][:-2] + "|n|n|cffa6afb8Автоприменение:|cffced4da переключается правой кнопкой мыши.|r"
            values["ubertip1"] = values["unubertip1"]
        elif code == "A145":
            values["untip1"] = tip
            values["unubertip1"] = values["ubertip1"]
        for field, value in values.items():
            op = dict(type="ability", id=code, field=field, value=value)
            if code in ("Arst", "Argl"):
                op["base_object"] = True
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))
    # Related descriptions must use the same command name and actual capital aura.
    cards = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h0HZ,h0I7,h0I8,n04M", "--fields", "name,tip,ubertip,isbldg,abillist,weapson,targs1"]))
    for obj in cards["objects"]:
        code, old = obj["id"], obj["fields"]
        if code == "n04M":
            values = {"name": "|cffe4cfa3Щупальце Йогг`Сарона|r", "tip": "|cffe4cfa3Щупальце Йогг`Сарона|r",
                      "ubertip": "|cffa6afb8ЮНИТ:|cffced4da Щупальце, призываемое Касанием безумия для наземного боя.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: атаки задевают врагов рядом с основной целью.|n|nАтакует наземные цели.|r"}
        else:
            current = resolve(old["ubertip"])
            updated = current.replace("Обозначить столицу", "Назначение столицы").replace("аура, ослабляющая броню ближайших противников", "аура, снижающая восстановление здоровья ближайших органических противников")
            values = {"ubertip": updated} if current != updated else {}
        for field, value in values.items():
            ops.append(dict(type="unit", id=code, field=field, value=value, marker="ЗДАНИЕ:" if old["isbldg"] == "1" else "ЮНИТ:"))
            strings.append(dict(rawcode=code, field=field, before=resolve(old[field]), after=value))
    item = require(cli(["get-objects-bulk", "--type", "item", "--ids", "I01Q", "--fields", "name,tip,ubertip,description,hotkey,abillist"]))
    old = item["objects"][0]["fields"]
    body = ("|cffa6afb8ПРЕДМЕТ:|cffced4da Частица силы Йогг`Сарона. Даёт герою " + green("+15") + " к силе, ловкости и интеллекту."
            "|n|n|cffa6afb8Способности:|cffced4da|n- " + ref("Тёмное усиление") + ": на " + white(45) + " сек. повышает урон союзников в радиусе " + white(500) + " на " + green("35%") + "."
            "|n- " + ref("Порождение щупальца") + ": создаёт Щупальце Йогг`Сарона на " + white(180) + " сек."
            "|n- " + ref("Аура отголоска Йогг`Сарона") + ": союзники ближнего боя в радиусе " + white(1500) + " получают " + green("10%") + " вампиризма."
            "|n|nДля применения заклинаний откройте меню предмета.|r")
    values = {"name": "|cffe4cfa3Касание безумия|r", "tip": "|cffe4cfa3Касание безумия|r (|cffffffff" + resolve(old["hotkey"]) + "|r)", "ubertip": body,
              "description": "|cffa6afb8ПРЕДМЕТ:|cffced4da Даёт герою |cffc8e087+15|cffced4da ко всем характеристикам, ауру вампиризма и два заклинания: Тёмное усиление и Порождение щупальца.|r"}
    for field, value in values.items():
        ops.append(dict(type="item", id="I01Q", field=field, value=value))
        strings.append(dict(rawcode="I01Q", field=field, before=resolve(old[field]), after=value))
    inv = dict(scope="Общие команды и зависимости безликих; награда за Йогг`Сарона", before=[before,cards,item], strings=strings,
               variants=["SD","HD"], in_game_checked=False,
               evidence=["02_game_modes.lua: MakeCapital / Trig_MakeStolica_Actions", "OldGods.lua: Trig_Qogg_Die_Actions", "Installed Warcraft III AbilityMetaData: Aoar Amount of Hit Points Regenerated, Percentage"],
               remaining=["Проверить ремонт, обмен, назначение столицы и предмет в игре", "Общие здания, морские исследования и эффекты", "Остальные сообщения и строки Lua"])
    (folder / "faceless_shared_commands.json").write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_shared_commands_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
