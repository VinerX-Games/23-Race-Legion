"""Prepare the remaining trained troops and worker; retain verified mechanics."""
import json
from faceless_text_batch import ROOT, apply_wts_batch
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"
    spec = {
        "h0ID": ("Злобный бичеватель разума", "Заклинатель, ослабляющий противников.", [
            ("Замедление", "снижает скорость атаки и передвижения врага."),
            ("Порождение щупальца", "призывает щупальце; требуется второй уровень «Укрепления Древних Знаний»."),
            ("Проклятие", "заставляет противника промахиваться; требуется третий уровень «Укрепления Древних Знаний»."),
        ]),
        "h0IE": ("Пожиратель Бездны", "Заклинатель для борьбы с магией и призванными существами.", [
            ("Пожирание Магии", "рассеивает магические эффекты, восстанавливает здоровье и ману; требуется первый уровень «Расширения Знаний»."),
            ("Ледяная стрела", "наносит урон и оглушает врага; требуется второй уровень «Расширения Знаний»."),
            ("Иней", "поражает цель и окружающих врагов, замедляя их; требуется третий уровень «Расширения Знаний»."),
            ("Пожирание", "после убийства даёт временный бонус к атаке; повторные убийства во время действия бонуса не складывают его."),
        ]),
        "h0IF": ("Бессмертный страж", "Воин, ослабляющий врагов и возвращающийся после гибели.", [
            ("Ужасающий вой", "временно снижает урон от атак окружающих врагов."),
            ("Реинкарнация", "возрождает после гибели; требуется «Суть бессмертия». Убийство противника сбрасывает восстановление способности."),
        ]),
        "h0IG": ("К`Траксис", "Тяжёлый наземный боец с защитными способностями.", [
            ("Тёмная оболочка", "возвращает часть урона атакующим в ближнем бою и повышает броню."),
            ("Крепкий панцирь", "снижает получаемый урон от атак; требуется второй уровень «Усиления К`Траксис»."),
            ("Взрыв Эфира", "наносит урон вокруг воина при его гибели."),
        ]),
        "h0K2": ("Проклинатель Бездны", "Заклинатель, создающий существ из трупов и поддерживающий союзников.", [
            ("Породить Кошмар", "создаёт из трупа временного Кошмара."),
            ("Пронзание", "поражает наземных врагов вокруг цели атаки осколками; требуется второй уровень «Знания проклинателей»."),
            ("Морозный доспех", "повышает броню союзника и замедляет атакующих его в ближнем бою; требуется третий уровень «Знания проклинателей»."),
        ]),
        "h0MO": ("Безликий Кошмар", "Боец, оглушающий врагов и наносящий дополнительный урон.", [
            ("Кража будущего", "при начале атаки дополнительно наносит врагу урон от его максимального здоровья; не действует на здания."),
            ("Кошмар", "оглушает противника; на героях длительность меньше."),
            ("Яд кошмара", "наносит периодический урон; на героях действует меньше времени."),
        ]),
        "n05I": ("Водное Порождение", "Наземный боец с критическими ударами и захватом противника.", [
            ("Сила Бездны", "атаки могут нанести увеличенный урон."),
            ("Опутывание", "обездвиживает врага и притягивает воздушную цель к земле; требует исследования сетей."),
        ]),
        "u02D": ("Безликий прислужник", "Рабочий безликих: возводит здания, добывает золото и древесину, ремонтирует постройки и технику.", [
            ("Небольшой скачок", "переносит рабочего на короткое расстояние."),
        ]),
        "h0MP": ("Порабощённый зверь", "Наземный боец без собственных способностей.", []),
        "h0MQ": ("Жестокий порабощённый зверь", "Наземный боец без собственных способностей.", []),
        "h0MN": ("Страх", "Боец против заклинателей, разрушающий защиту противника.", [
            ("Помутнение разума", "атаки снижают броню цели; требуется «Помутнение рассудка»."),
            ("Разрушение Эфира", "атаки сжигают ману цели; требуется исследование «Разрушение Эфира»."),
        ]),
    }
    fields = "name,tip,ubertip,hotkey,abillist,weapson,targs1,targs2,atktype1,upgrades,builds"
    objects = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(spec), "--fields", fields]))["objects"]
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    strings, ops = [], []
    for obj in objects:
        code, old = obj["id"], obj["fields"]
        name, role, abilities = spec[code]
        text = "|cffa6afb8ЮНИТ:|cffced4da " + role
        if abilities:
            text += "|n|n|cffa6afb8Способности:|cffced4da" + "".join("|n- " + ref(n) + ": " + effect for n, effect in abilities)
        text += "|n|nАтакует наземные цели.|r"
        values = {"name": "|cffe4cfa3" + name + "|r", "tip": "|cffe4cfa3" + name + "|r (|cffffffff" + resolve(old["hotkey"]) + "|r)", "ubertip": text}
        for field, value in values.items():
            strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
            ops.append(dict(type="unit", id=code, field=field, value=value))
    # Keep the portal's training list consistent with the corrected unit name.
    for sid, value in wts.items():
        if "Бессмертый страж" in value and sid not in {int(row["reference_before"][8:]) for row in strings}:
            strings.append(dict(rawcode="related", field="text", reference_before="TRIGSTR_" + str(sid), before=value, after=value.replace("Бессмертый страж", "Бессмертный страж")))
    folder = ROOT / "docs/ui_text"
    inventory = dict(scope="Безликие: 11 юнитов; рабочий, остальные обучаемые войска и звери", variants=["SD", "HD"],
                     in_game_checked=False, objects_before=objects, strings=strings,
                     evidence=["faceless_ability_dependencies.json", "Bezlikie.lua: Trig_Spell2 / Trig_SpellRes", "Stromgard.lua: Trig_ChillBonus; A1R5 dataa1=3"],
                     remaining=["Призываемые e009, h0OM; герои; собственные карточки способностей", "Игровая проверка"])
    path = folder / "faceless_units_02.json"
    path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_units_02_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(ok=True, prepared_units=len(objects), strings=len(strings))))


if __name__ == "__main__":
    main()
