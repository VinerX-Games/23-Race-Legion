"""Prepare all 13 Faceless researches, their actual levels and named consumers."""
import json
import re
from decimal import Decimal
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    dependencies = json.loads((folder / "faceless_research_dependencies.json").read_text(encoding="utf-8"))
    specs = {o["id"]: o["fields"] for o in dependencies["objects"] if o["id"] not in ("R07M", "R0F9")}
    consumers = json.loads((folder / "faceless_research_consumers.json").read_text(encoding="utf-8"))
    names = {"R0EK": "Улучшение Сущности", "R0EL": "Разрушение Эфира", "R0ER": "Усиление мышц",
             "R0ES": "Помутнение рассудка", "R0ET": "Наращивание мышц", "R0EV": "Усиление К`Траксис",
             "R0EW": "Расширение Знаний", "R0EX": "Укрепление Древних Знаний", "R0F7": "Развитие силы",
             "R0F8": "Развитие скорости", "R0FA": "Суть бессмертия", "R0GD": "Знание проклинателей", "R0GE": "Дереводобыча"}
    fields = ["maxlevel"] + [f"{f}{n}" for f in ("name", "tip", "ubertip", "hotkey") for n in range(1, 7)]
    objects = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(specs), "--fields", ",".join(fields)]))["objects"]
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    plain = lambda s: re.sub(r"\|c[0-9a-fA-F]{8}|\|r", "", s).strip()
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"

    def n(value):
        return format(Decimal(value).normalize(), "f").replace(".", ",")

    def bonus(value, suffix=""):
        return "|cffc8e087+" + n(value) + suffix + "|cffced4da"

    def total(code, slot, level):
        d = specs[code]
        return Decimal(d["base" + str(slot)]) + Decimal(d["mod" + str(slot)]) * (level - 1)

    def targets(code):
        result = []
        for obj in consumers:
            if code not in obj["fields"].get("upgrades", "").split(","):
                continue
            name = plain(obj["name"])
            if obj["id"] in ("n03B", "n03C", "n04C"):
                name = "Щупальце Йогг`Сарона"
            elif obj["id"] == "h0OM":
                name = "Тварь из Бездны"
            if code == "R0ER":
                name += ": " + bonus(Decimal(obj["fields"]["defup"]) * current_level) + " к броне"
            if code == "R0ET":
                minimum = total(code, 1, current_level)
                maximum = minimum * Decimal(obj["fields"]["sides1"])
                name += ": " + bonus(minimum) + "–" + bonus(maximum) + " к урону"
            if name not in result:
                result.append(name)
        return result

    ops, strings = [], []
    notes = []
    for obj in objects:
        code, old = obj["id"], obj["fields"]
        maximum = int(old["maxlevel"])
        for level in range(1, maximum + 1):
            current_level = level
            extra = ""
            affected = targets(code)
            if code == "R0EK":
                effect = "Открывает «Сотрясение Бездны»: атаки могут оглушить противника и нанести дополнительный урон."
                affected = ["Сущность бездны — Сотрясение Бездны"]
            elif code == "R0EL":
                effect = "Открывает «Разрушение Эфира»: атаки сжигают ману и наносят урон за каждую сожжённую единицу."
                affected = ["Сущность бездны", "Могущественная Сущность бездны", "Страх"]
            elif code == "R0ER":
                effect = "Повышает броню перечисленных существ. Суммарный бонус после изучения этого уровня указан у каждой цели."
            elif code == "R0ET":
                effect = "Увеличивает урон атак перечисленных войск и башни. Суммарная прибавка к диапазону урона после изучения этого уровня указана у каждой цели."
            elif code == "R0ES":
                effect = "Даёт Страху бонус к уровню «Помутнения разума» и «Помутнения рассудка»: " + bonus(level) + " относительно исходного уровня способностей."
                affected = ["Страх — Помутнение разума и Помутнение рассудка"]
                extra = "|n|n|cffa6afb8Примечание:|cffced4da способности имеют по три уровня; исследование не добавляет новых уровней сверх их максимума."
            elif code == "R0EV":
                effect = "Суммарный бонус: " + bonus(total(code, 1, level) * 100, "%") + " к максимальному здоровью и " + bonus(total(code, 2, level) * 100, "%") + " к восстановлению здоровья."
                if level == 2:
                    extra = "|n|nОткрывает «Крепкий панцирь»."
            elif code == "R0EW":
                dice = total(code, 1, level)
                effect = ("Суммарные бонусы Пожирателя Бездны: " + bonus(dice) + "–" + bonus(dice * 2) + " к урону атак, "
                          + bonus(total(code, 2, level) * 100, "%") + " к максимальной мане, " + bonus(total(code, 3, level)) + " к дальности атак и "
                          + bonus(total(code, 4, level) * 100, "%") + " к скорости атаки.")
                extra = "|n|nОткрывает «" + ("Пожирание Магии", "Ледяная стрела", "Иней")[level - 1] + "»."
            elif code in ("R0EX", "R0GD"):
                if code == "R0EX":
                    effect = "Суммарные бонусы: " + bonus(total(code, 1, level) * 100, "%") + " к максимальному здоровью и " + bonus(total(code, 2, level) * 100, "%") + " к максимальной мане."
                    if level >= 2:
                        extra = "|n|nОткрывает «" + ("Порождение щупальца" if level == 2 else "Проклятие") + "»."
                else:
                    affected = ["Проклинатель Бездны"]
                    effect = "Подготавливает изучение следующих уровней знаний проклинателей." if level == 1 else "Открывает «" + ("Пронзание" if level == 2 else "Морозный доспех") + "»."
                    extra = ""
            elif code == "R0F7":
                effect = "Суммарный бонус: " + bonus(total(code, 1, level) * 100, "%") + " к максимальному здоровью и " + bonus(total(code, 2, level) * 100, "%") + " к восстановлению здоровья."
                extra = "|n|n|cffe6c07bВзаимоисключается с исследованием «Развитие скорости».|cffced4da"
            elif code == "R0F8":
                effect = "Суммарный бонус: " + bonus(total(code, 3, level) * 100, "%") + " к скорости передвижения и " + bonus(total(code, 4, level) * 100, "%") + " к скорости атаки."
                extra = "|n|n|cffe6c07bВзаимоисключается с исследованием «Развитие силы».|cffced4da"
            elif code == "R0FA":
                effect = "Открывает «Реинкарнацию»: Бессмертный страж возвращается после гибели; убийство противника сбрасывает восстановление способности."
                affected = ["Бессмертный страж — Реинкарнация"]
            elif code == "R0GE":
                effect = "Увеличивает объём переносимой древесины Безликого прислужника. Суммарный бонус: " + bonus(total(code, 1, level)) + " древесины за одну доставку."
            text = "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da " + effect + extra
            text += "|n|n|cffa6afb8Применяется к:|cffced4da" + "".join("|n- " + ref(s) + "." for s in affected)
            if maximum > 1:
                text += "|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff" + str(level) + "/" + str(maximum) + "|cffced4da."
            text += "|r"
            title = "|cffe4cfa3" + names[code] + "|r"
            if maximum > 1:
                title += " — уровень |cffffffff" + str(level) + "|r"
            key = resolve(old["hotkey" + str(level)]).strip('"')
            values = {"name" + str(level): title, "tip" + str(level): title + (" (|cffffffff" + key + "|r)" if key else ""), "ubertip" + str(level): text}
            for field, value in values.items():
                ops.append(dict(type="upgrade", id=code, field=field, value=value))
                strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
    notes += ["R0GD is absent from h0K2.upgrades: its percentage stat effects do not apply to that unit; ability requirements still unlock A16P/A16O.",
              "R0ES rlev is a bonus to original ability level; both affected abilities have three levels. Runtime level cap needs verification.",
              "R0ET ratd changes attack dice; named damage ranges use each unit's sides1. R0EW uses the same effect.",
              "Empty effect3/effect4 slots were excluded, even when stale numeric data exists."]
    inv = dict(scope="Безликие: 13 исследований, все 42 действующих уровня", variants=["SD", "HD"], in_game_checked=False,
               objects_before=objects, strings=strings, notes=notes,
               evidence=["faceless_research_dependencies.json", "faceless_research_consumers.json", "faceless_effect_metadata.json", "Bezlikie.lua: Trig_Sila1/2, Trig_Skorost1/2"],
               remaining=["Расовые маркеры R07M/R0F9", "Связанные списки зданий", "Игровая проверка уровней и высоты списков"])
    (folder / "faceless_research.json").write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_research_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
