"""Prepare remaining ship spells without inventing final flagship multipliers."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    before = json.loads((folder / "faceless_flagship_before.json").read_text(encoding="utf-8"))
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    white = lambda v: "|cffffffff" + str(v) + "|cffced4da"
    bonus = lambda v: "|cffc8e087+" + str(v) + "|cffced4da"
    names = {"A00G": "Массированный обстрел", "A009": "Назначение флагмана", "A008": "Особенность флагмана",
             "A007": "Аура выносливости", "A006": "Аура меткости", "A005": "Аура стойкости",
             "A00F": "Аура выносливости", "A00E": "Аура меткости", "A00C": "Аура стойкости", "A001": "Абордаж"}
    aura = {
        "A007": "Даёт союзным механическим войскам, включая сам флагман, в радиусе " + white(900)
                + " бонусы: " + bonus("20%") + " к скорости передвижения и " + bonus("5%") + " к скорости атаки.",
        "A006": "Даёт союзным механическим войскам, включая сам флагман, в радиусе " + white(900)
                + " бонус " + bonus("15%") + " к урону дальних атак. На ближние атаки не действует.",
        "A005": "Даёт союзным механическим войскам, включая сам флагман, в радиусе " + white(900)
                + " бонус " + bonus(2) + " к броне.",
    }
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        title = "|cffe4cfa3" + names[code] + "|r"
        values = {"name": title}
        for level in range(1, int(old["levels"]) + 1):
            data = lambda f: format(float(old[f + str(level)]), "g").replace(".", ",")
            if code == "A00G":
                body = ("Обстреливает выбранную область радиусом " + white(data("area"))
                        + ". Выпускает " + white(data("datac")) + " снарядов и наносит " + white(data("dataa"))
                        + " урона с интервалом " + white(data("datab")) + " сек. Предел урона по области — " + white(data("datad"))
                        + ". Здания получают " + white(125) + "% урона. Поражает наземных и воздушных противников, включая здания. "
                        "Оглушение: " + white(data("dur")) + " сек.; для героев — " + white(data("herodur"))
                        + " сек.|n|nТребует исследования «Обстрел». Перезарядка — " + white(data("cool"))
                        + " сек.|n|n|cffa6afb8Уровень:|cffced4da " + white(level) + " из " + white(old["levels"]) + ".")
            elif code in aura:
                body = aura[code]
            elif code in ("A00F", "A00E", "A00C"):
                selected = {"A00F": "A007", "A00E": "A006", "A00C": "A005"}[code]
                body = ("Наделяет выбранный флагман постоянной аурой. " + aura[selected]
                        + "|n|nСтоимость — " + white(250) + " золота и " + white(250)
                        + " древесины. При применении флагман должен оставаться выделенным. Выбор закрывает меню особенностей.")
            elif code == "A008":
                body = ("Открывает выбор одной постоянной ауры флагмана: выносливости, стойкости или меткости. "
                        "Каждый вариант стоит " + white(250) + " золота и " + white(250)
                        + " древесины. При выборе ауры флагман должен оставаться выделенным.")
            elif code == "A009":
                body = ("Назначает корабль флагманом: усиливает базовый урон главных орудий, максимальное здоровье и броню, "
                        "увеличивает размер и открывает выбор постоянной ауры.|n|nСтоимость — " + white(2500)
                        + " золота и " + white(2500) + " древесины.")
            else:
                body = ("Команда абордажа вражеской механической цели."
                        "|n|n|cffe69a8dЗахват кораблей в текущей версии недоступен.|cffced4da "
                        "Применение этой команды не передаёт корабль другому игроку.")
            key = resolve(old.get("hotkey", "")).strip('"')
            values["tip" + str(level)] = title + (" (|cffffffff" + key + "|r)" if key else "")
            values["ubertip" + str(level)] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"
        for field, value in values.items():
            ops.append(dict(type="ability", id=code, field=field, value=value))
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))
    inventory = dict(scope="Оставшиеся десять корабельных способностей, включая выбор и три ауры флагмана",
                     objects_before=before, strings=strings, in_game_checked=False,
                     evidence=["05_common_spells.lua: flagship creation and aura selection callbacks",
                               "06_transport_portals.lua: boarding callback returns before capture",
                               "Installed AbilityMetaData: ANcs, AAns, AEar"],
                     remaining=["Measure final flagship stats: same action registered on CAST, EFFECT and ENDCAST; numeric bonus intentionally unresolved",
                                "Check resource charging, single-flagship gates and selected-unit condition in engine",
                                "Fix broken dynamic flagship display name as a separate text change",
                                "Verify cluster-rocket pulse count and maximum damage semantics in engine",
                                "Audit visible aura/status effects and update their text"])
    for filename, content in (("faceless_flagship", inventory), ("faceless_flagship_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
