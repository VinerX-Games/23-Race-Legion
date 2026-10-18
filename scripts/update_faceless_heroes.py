"""Prepare Faceless hero cards, personal names and resurrection button titles."""
import json
import re
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    spec = {
        "U02G": ("Генерал К`Траксис", "Герой ближнего боя: защищает себя панцирем и призывает подкрепления.", [
            ("Крепкий панцирь", "снижает получаемый урон от атак."),
            ("Обжигающий жар", "наносит урон окружающим врагам, расходуя ману, пока способность включена."),
            ("Тёмный портал", "призывает порабощённых зверей; состав зависит от уровня способности."),
            ("Удар клешнёй", "наносит урон вокруг героя и снижает скорость атаки и передвижения врагов."),
        ]),
        "U02H": ("Верховный Душегуб", "Герой ближнего боя для внезапных атак и ослабления брони противника.", [
            ("Безумие бездны", "повышает скорость атаки и даёт вампиризм."),
            ("Сокрытие Бездной", "делает героя невидимым, ускоряет передвижение и усиливает удар из невидимости."),
            ("Сотрясение Бездны", "даёт шанс оглушить противника и нанести дополнительный урон при атаке."),
            ("Метка охотника", "снижает броню врага и позволяет видеть отмеченную цель."),
        ]),
        "U02I": ("Маг Запредельной Тьмы", "Герой-заклинатель, призывающий войска и поражающий область магией Бездны.", [
            ("Тёмный раскол", "призывает воинов безликих; состав зависит от уровня способности."),
            ("Взрыв бездны", "наносит периодический урон наземным целям в указанной области."),
            ("Аура Бездны", "снижает восстановление здоровья окружающих врагов."),
            ("Пространство Бездны", "наносит целям в области периодический урон от максимального здоровья и уничтожает деревья."),
        ]),
        "U02F": ("Верховный генерал", "Легендарный герой ближнего боя, поддерживающий войска аурами и лечением.", [
            ("Антимагическая аура", "снижает восстановление маны окружающих врагов."),
            ("Вечная служба", "поднимает павших воинов для сражения на стороне героя."),
            ("Пары саронита", "восстанавливают здоровье союзников в области действия, пока герой поддерживает заклинание."),
            ("Приказ генерала", "повышает урон от атак союзных войск рядом с героем."),
            ("Саронитовый панцирь", "снижает получаемый урон от атак."),
            ("Стать слугой Йогг`Сарона", "передаёт игроку контроль над Древним богом Йогг`Сароном."),
        ]),
    }
    fields = "name,propernames,tip,ubertip,awakentip,revivetip,hotkey,abillist,heroabillist,weapson,targs1,targs2"
    objects = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(spec), "--fields", fields]))["objects"]
    wts = load_wts_strings()
    resolve = lambda v: wts[int(v[8:])] if v.startswith("TRIGSTR_") else v
    strings, ops = [], []
    for obj in objects:
        code, old = obj["id"], obj["fields"]
        name, role, abilities = spec[code]
        short = "|cffe4cfa3" + name + "|r"
        text = "|cffa6afb8ГЕРОЙ:|cffced4da " + role + "|n|n|cffa6afb8Способности:|cffced4da"
        text += "".join("|n- |cffa9c7de" + n + "|cffced4da: " + effect for n, effect in abilities)
        text += "|n|nАтакует наземные цели.|r"
        personal = re.sub(r"\|c[0-9a-fA-F]{8}|\|r|\|$", "", resolve(old["propernames"]))
        values = {"name": short, "tip": short + " (|cffffffff" + resolve(old["hotkey"]) + "|r)",
                  "ubertip": text, "propernames": "|cffe4cfa3" + personal + "|r",
                  "awakentip": short, "revivetip": short}
        for field, value in values.items():
            strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
            ops.append(dict(type="unit", id=code, field=field, value=value))
    folder = ROOT / "docs/ui_text"
    inventory = dict(scope="Безликие: четыре героя, включая легендарного Везакса", variants=["SD", "HD"], in_game_checked=False,
                     objects_before=objects, strings=strings, evidence=["faceless_hero_dependencies.json", "Bezlikie.lua: Trig_Sluga_qqgsarona", "Stromgard.lua: Trig_Passive"],
                     remaining=["Собственные карточки способностей: все уровни и изучение", "Доступность Везакса и игровая проверка"])
    (folder / "faceless_heroes.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_heroes_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
