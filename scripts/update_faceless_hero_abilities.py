"""Prepare hero spells, learning tooltips and auxiliary passive effects."""
import json
import re
from decimal import Decimal

from faceless_text_batch import ROOT
from wc3_hivewe import load_wts_strings

FOLDER = ROOT / "docs/ui_text"


def main():
    snapshot = json.loads((FOLDER / "faceless_hero_abilities_before.json").read_text(encoding="utf-8"))
    objects = {obj["id"]: obj for obj in snapshot["objects"]}
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    titles = {
        "A10H": "Удар клешнёй", "A10I": "Крепкий панцирь", "A10J": "Обжигающий жар", "A10K": "Тёмный портал",
        "A10L": "Сотрясение Бездны", "A10N": "Сокрытие Бездной", "A10Q": "Тёмный раскол", "A0WQ": "Взрыв бездны",
        "A10R": "Аура Бездны", "A10S": "Пространство Бездны", "A1CJ": "Безумие бездны", "A1CH": "Скорость бездны",
        "A1CI": "Вампиризм бездны", "A1CG": "Метка охотника", "A12G": "Служение Йогг`Сарону", "A12I": "Саронитовый панцирь",
        "A12H": "Антимагическая аура", "A0V5": "Вечная служба", "A12J": "Пары саронита", "A0V7": "Приказ генерала",
    }
    troop_names = {"h0MP": "Порабощённый зверь", "h0MQ": "Жестокий порабощённый зверь", "h0I9": "Безликий дозорный",
                   "h0IB": "Сущность бездны", "h0IF": "Бессмертный страж", "h0IC": "Могущественная Сущность бездны", "h0IG": "К`Траксис"}

    def number(value, color="ffffff"):
        value = format(Decimal(value).normalize(), "f").replace(".", ",")
        return "|cff" + color + value + "|cffced4da"

    def data(code, prefix, level, color="ffffff", percentage=False):
        value = Decimal(objects[code]["fields"][prefix + str(level)])
        return number(value * (100 if percentage else 1), color) + ("%" if percentage else "")

    def text(code, level):
        value = lambda prefix, color="ffffff", percentage=False: data(code, prefix, level, color, percentage)
        if code == "A10H":
            return ("Наносит органическим наземным противникам в радиусе " + value("area") + " " + value("dataa") + " урона. "
                    "Снижает скорость передвижения и атаки на " + value("datac", percentage=True) + ". Замедление длится " + value("dur") + " сек., на героях — " + value("herodur") + " сек.")
        if code in ("A10I", "A12I"):
            return "Снижает урон от атак ближнего и дальнего боя на " + value("datac", "c8e087") + ", но не ниже " + value("datab") + " урона за удар."
        if code == "A10J":
            return ("Пока способность включена, каждые " + value("dur") + " сек. наносит органическим наземным врагам в радиусе " + value("area") + " " + value("dataa") + " урона. "
                    "Расходует " + value("datab", "e69a8d") + " маны в секунду.")
        if code in ("A10K", "A10Q"):
            choices = objects[code]["fields"]["dataa" + str(level)].split(",")
            return ("Открывает портал и призывает " + value("datab") + " воинов из следующего списка:" +
                    "".join("|n- |cffa9c7de" + troop_names[unit] + "|cffced4da." for unit in choices))
        if code == "A10L":
            return ("С вероятностью " + value("dataa") + "% атака наносит " + value("datac") + " дополнительного урона и оглушает цель на " + value("dur") + " сек. "
                    "Герои оглушаются на " + value("herodur") + " сек.")
        if code == "A10N":
            return ("Через " + value("dataa") + " сек. герой становится невидимым на " + value("dur") + " сек. "
                    "Скорость передвижения повышается на " + value("datab", "c8e087", True) + ". Атака из невидимости наносит " + value("datac") + " дополнительного урона и раскрывает героя. "
                    "Восстановление начинается после выхода из невидимости.")
        if code == "A0WQ":
            return ("Создаёт пламя Бездны в радиусе " + value("area") + ". Сильное пламя наносит " + value("dataa") + " урона за импульс с интервалом " + value("datab") + " сек.; "
                    "остаточное пламя — " + value("datac") + " урона с интервалом " + value("datad") + " сек. "
                    "Здания получают " + value("datae", percentage=True) + " урона. Предел урона по области: " + value("dataf") + "."
                    "|n|n|cffe6c07bПоражает наземные цели, включая союзников и самого героя; уничтожает деревья.|cffced4da")
        if code == "A10R":
            amount = abs(Decimal(objects[code]["fields"]["datab" + str(level)]))
            return "Снижает восстановление здоровья врагов в радиусе " + value("area") + " на " + number(amount) + " ед. в секунду."
        if code == "A10S":
            return ("Пока герой поддерживает заклинание, враги в радиусе " + value("area") + " теряют " + value("dataa", percentage=True) + " максимального здоровья в секунду. "
                    "Действует до " + value("dur") + " сек. Поражает также воздушные цели и здания; уничтожает деревья.")
        if code == "A1CJ":
            return ("Повышает скорость атаки героя на " + data("A1CH", "dataa", level, "c8e087", True) + " и даёт вампиризм: "
                    "восстанавливает здоровье в размере " + data("A1CI", "dataa", level, "c8e087", True) + " урона его атак.")
        if code == "A1CH":
            return "Повышает скорость атаки героя на " + value("dataa", "c8e087", True) + ". Эффект «Безумия бездны»."
        if code == "A1CI":
            return "Восстанавливает здоровье в размере " + value("dataa", "c8e087", True) + " урона атак владельца. Эффект «Безумия бездны»."
        if code == "A1CG":
            return ("Снижает броню врага на " + value("dataa") + " и позволяет видеть отмеченную цель, в том числе невидимую. "
                    "Действует " + value("dur") + " сек.; на героях — " + value("herodur") + " сек.")
        if code == "A12G":
            return ("Передаёт игроку контроль над Древним богом Йогг`Сароном и делает его столицей. Его положение становится видно всем игрокам."
                    "|n|n|cffe6c07bПосле применения способность становится недоступна всем игрокам.|cffced4da")
        if code == "A12H":
            amount = abs(Decimal(objects[code]["fields"]["dataa" + str(level)]))
            return "Снижает восстановление маны врагов в радиусе " + value("area") + " на " + number(amount) + " ед. в секунду."
        if code == "A0V5":
            inherit = objects[code]["fields"]["datac" + str(level)] == "1"
            return ("Поднимает до " + value("dataa") + " павших воинов из трупов в радиусе " + value("area") + " на " + value("dur") + " сек. Они сражаются на стороне героя. "
                    + ("Поднятые воины наследуют исследования владельца." if inherit else "Поднятые воины не наследуют исследования владельца."))
        if code == "A12J":
            body = ("Пока герой поддерживает заклинание, лечит дружественные и нейтральные цели в радиусе " + value("area") + ", включая себя, на " + value("dataa", "c8e087") + " здоровья каждые " + value("datab") + " сек. "
                    "Действует до " + value("dur") + " сек.")
            if Decimal(objects[code]["fields"]["datad" + str(level)]):
                body += " В начале поддержания герой неуязвим в течение " + value("datad", "c8e087") + " сек."
            return body
        if code == "A0V7":
            return ("Повышает урон от атак союзных войск и самого героя в радиусе " + value("area") + " на " + value("dataa", "c8e087", True) + ". Действует на ближний и дальний бой.")
        raise ValueError(code)

    ops, strings = [], []
    for code, obj in objects.items():
        old = obj["fields"]
        maximum = int(old["levels"])
        title = "|cffe4cfa3" + titles[code] + "|r"
        key = resolve(old["hotkey"]).strip('"')
        short = title + (" (|cffffffff" + key + "|r)" if key else "")
        values = {"name": title}
        for level in range(1, maximum + 1):
            values["tip" + str(level)] = short
            body = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + text(code, level)
            if maximum > 1:
                body += "|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff" + str(level) + "/" + str(maximum) + "|cffced4da."
            values["ubertip" + str(level)] = body + "|r"
            if code == "A10J":
                values["untip" + str(level)] = short
                values["unubertip" + str(level)] = body + "|n|n|cffa6afb8Состояние:|cffced4da включено; повторное применение отключает жар.|r"
        if old["hero"] == "1":
            learn_key = resolve(old["researchhotkey"]).strip('"')
            values["researchtip"] = title + (" (|cffffffff" + learn_key + "|r)" if learn_key else "")
            descriptions = ["|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + titles[code] + ".|n|n|cffa6afb8Уровни:|cffced4da"]
            for level in range(1, maximum + 1):
                descriptions.append("|n- |cffffffff" + str(level) + "|cffced4da: " + text(code, level))
            values["researchubertip"] = "".join(descriptions) + "|r"
        for field, value in values.items():
            ops.append(dict(type="ability", id=code, field=field, value=value))
            strings.append(dict(rawcode=code, field=field, reference_before=old.get(field, ""), before=resolve(old.get(field, "")), after=value))
    inventory = dict(scope="Безликие: все геройские заклинания четырёх героев и два вспомогательных эффекта Безумия бездны",
                     variants=["SD", "HD"], in_game_checked=False, strings=strings,
                     evidence=["faceless_hero_abilities_before.json", "faceless_hero_ability_metadata.json", "Stromgard.lua: Trig_Passive", "Bezlikie.lua: Trig_Sluga_qqgsarona"],
                     remaining=["В Warcraft III проверить интервалы и минимальный запас маны Обжигающего жара, фазы и предел урона Взрыва бездны", "Проверить окна изучения, цели и высоту списков", "Согласовать новое название Служения с карточкой Везакса"])
    (FOLDER / "faceless_hero_abilities.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (FOLDER / "faceless_hero_abilities_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(abilities=len(objects), operations=len(ops))))


if __name__ == "__main__":
    main()
