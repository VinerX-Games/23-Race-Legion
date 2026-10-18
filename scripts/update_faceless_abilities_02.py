"""Prepare normal troop spells from object data and the implemented Lua hooks."""
import json
import re
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    specs = {
        "A114": ("Замедление", ["Снижает скорость передвижения врага на 35%, скорость атаки — на 25%. Действует 45 сек., на героях — 10 сек."]),
        "A115": ("Проклятие", ["На 20 сек. даёт органическому противнику 15%-ю вероятность промаха при атаке.|n|nТребуется третий уровень «Укрепления Древних Знаний»."]),
        "A116": ("Порождение щупальца", ["Призывает одно щупальце на 40 сек.|n|nТребуется второй уровень «Укрепления Древних Знаний»."]),
        "A126": ("Ледяная стрела", ["Наносит врагу 100 урона и оглушает его на 5 сек. Герои оглушаются на 0,5 сек.|n|nТребуется второй уровень «Расширения Знаний»."]),
        "A112": ("Иней", ["Наносит органической цели 100 прямого урона и ещё 50 урона по области радиусом 130. Холод замедляет цели на 4 сек., героев — на 2 сек.|n|nТребуется третий уровень «Расширения Знаний»."]),
        "A1R2": ("Пожирание Магии", ["Рассеивает магические эффекты в радиусе 200. За каждый поглощённый эффект восстанавливает владельцу 55 здоровья и 55 маны. Наносит призванным существам 300 урона.|n|nТребуется первый уровень «Расширения Знаний»."]),
        "A1R3": ("Пожирание", ["После убийства даёт +3 к атаке на 9 сек. Пока бонус действует, новые убийства не складывают его и не обновляют длительность."]),
        "A1R5": ("Пожирание", ["Временный бонус: +3 к атаке. Выдаётся на 9 сек. после убийства; повторные убийства во время действия не складывают и не обновляют бонус."]),
        "A10P": ("Ужасающий вой", ["На 10 сек. снижает урон от атак врагов в радиусе 800 на 10%."]),
        "A123": ("Реинкарнация", ["После гибели возрождает владельца через 3 сек. Восстановление: 120 сек. Убийство противника немедленно сбрасывает восстановление.|n|nТребуется исследование «Суть бессмертия»."]),
        "A10Y": ("Крепкий панцирь", ["Снижает получаемый урон от атак на 8, но не ниже 3 урона за удар.|n|nТребуется второй уровень «Усиления К`Траксис»."]),
        "A111": ("Тёмная оболочка", ["Даёт +4 к броне и возвращает атакующим в ближнем бою 30% урона от их атак."]),
        "A0RR": ("Взрыв Эфира", ["При гибели наносит наземным врагам 100 урона в радиусе 120 и 30 урона за пределами этого радиуса, но не дальше 250."]),
        "A1N5": ("Взрыв Эфира", ["При гибели воин взрывается. Наземные враги в радиусе 120 получают 100 урона; дальше, до радиуса 250, — 30 урона."]),
        "A16O": ("Морозный доспех", ["На 45 сек. даёт союзнику +5 к броне. Противники, атакующие его в ближнем бою, замедляются на 3 сек.|n|nТребуется третий уровень «Знания проклинателей»."]),
        "A16N": ("Порождение Кошмара", ["Создаёт из трупа одного Кошмара на 50 сек. Одновременно можно поддерживать до 6 Кошмаров."]),
        "A1CK": ("Помутнение разума", [f"Атаки снижают броню цели на {armor} на 7 сек.; на героях — на 1,5 сек.|n|nТребуется исследование «Помутнение рассудка»." for armor in (2, 3, 4)]),
        "A1CF": ("Помутнение рассудка", [f"Атаки снижают броню цели на {armor} на 7 сек.; на героях — на 1,5 сек.|n|nТребуется исследование «Помутнение рассудка»." for armor in (2, 3, 4)]),
        "A122": ("Кража будущего", ["При начале атаки дополнительно наносит цели урон в размере 1,4% её максимального здоровья. Не действует на здания."]),
        "A113": ("Кошмар", ["Оглушает органического противника на 10 сек.; героя — на 5 сек. Само оглушение не наносит урона."]),
        "A0PC": ("Яд кошмара", ["Наносит органическому врагу 5 урона в секунду в течение 10 сек. На героях действует 5 сек."]),
        "ACen": ("Опутывание", ["Обездвиживает вражеского юнита на 8 сек. Воздушная цель притягивается к земле и считается наземной. Не действует на героев."]),
        "A0I3": ("Небольшой скачок", ["Мгновенно переносит владельца на расстояние до 500. Восстановление: 40 сек."]),
    }
    # Roen is a shared research: the rawcode belongs in the registry, not the UI.
    specs["ACen"][1][0] = specs["ACen"][1][0].replace(" (Roen)", "")
    fields = ["name", "hotkey", "levels", "requires", "requiresamount", "code", "cool1", "area1", "targs1"]
    fields += [f"{field}{level}" for field in ("tip", "ubertip", "dataa", "datab", "datac", "datad", "datae", "dur", "herodur") for level in range(1, 4)]
    objects = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(specs), "--fields", ",".join(fields)]))["objects"]
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    ops, strings = [], []

    def formatted(body):
        return re.sub(r"(?<![\w])\+?\d+(?:,\d+)?%?", lambda m: ("|cffc8e087" if m[0].startswith("+") else "|cffffffff") + m[0] + "|cffced4da", body)

    for obj in objects:
        code, old = obj["id"], obj["fields"]
        name, bodies = specs[code]
        assert int(old["levels"]) == len(bodies), code
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old.get("hotkey", "")).strip('"')
        tip = title + (" (|cffffffff" + key + "|r)" if key else "")
        values = {"name": title}
        for level, body in enumerate(bodies, 1):
            values["tip" + str(level)] = tip
            formatted_body = formatted(body)
            if code == "A1R2":
                formatted_body = formatted_body.replace("|cffffffff55|cffced4da", "|cffc8e08755|cffced4da")
            values["ubertip" + str(level)] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + formatted_body + "|r"
        if code in ("A114", "A115", "A16O"):
            values["untip1"] = tip
            values["unubertip1"] = values["ubertip1"][:-2] + "|n|n|cffa6afb8Автоприменение:|cffced4da переключается правой кнопкой мыши.|r"
            values["ubertip1"] = values["unubertip1"]
        for field, value in values.items():
            ops.append(dict(type="ability", id=code, field=field, value=value))
            strings.append(dict(rawcode=code, field=field, reference_before=old.get(field, "not requested"), before=resolve(old.get(field, "")), after=value))
    folder = ROOT / "docs/ui_text"
    inventory = dict(scope="Безликие: обычные заклинания, состояния и вспомогательные пассивные способности; общие ACen и A0I3",
                     variants=["SD", "HD"], in_game_checked=False, objects_before=objects, strings=strings,
                     evidence=["faceless_ability_dependencies.json", "Bezlikie.lua: Trig_Spell2 / Trig_SpellRes", "Stromgard.lua: Trig_ChillBonus"],
                     remaining=["A16P: проверить параметры осколков", "Геройские заклинания и эффекты", "Игровая проверка"])
    (folder / "faceless_abilities_02.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_abilities_02_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
