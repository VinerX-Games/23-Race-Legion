"""Prepare summoned units, Yogg-Saron and its scripted spell unlocks."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    snapshot = json.loads((folder / "faceless_remaining_units_before.json").read_text(encoding="utf-8"))
    objects = {obj["id"]: obj for obj in snapshot["objects"]}
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"
    tentacle_abilities = [("Рассекающий удар", "атакой задевает наземных врагов рядом с основной целью.")]
    specs = {
        "e009": ("Кошмар", "Призываемый боец, создаваемый Проклинателем Бездны из трупа.", [], True),
        "h0OM": ("Тварь из Бездны", "Могучий наземный боец Бездны с атакой по нескольким целям.", [
            ("Порождение щупальца", "призывает временное Щупальце для наземного боя."),
            ("Рассекающий удар", "наносит часть урона атаки врагам вокруг основной цели."),
            ("Взрыв Эфира", "при гибели наносит урон наземным врагам вокруг воина."),
        ], False),
        "n01T": ("Щупальце", "Неподвижное существо для наземного боя.", [], False),
        "nfgt": ("Щупальце", "Призываемое существо, атакующее наземных противников.", [], False),
        "uloc": ("Саранча", "Насекомое роя: автоматически атакует противников и возвращается к источнику роя, восстанавливая ему здоровье. Нельзя выбрать и отдавать обычные команды.", [], True),
        "n03B": ("Щупальце Йогг`Сарона", "Защитное щупальце Древнего бога для наземного боя.", tentacle_abilities, False),
        "n03C": ("Щупальце Йогг`Сарона", "Защитное щупальце Древнего бога для наземного боя.", tentacle_abilities, False),
        "n04C": ("Щупальце Йогг`Сарона", "Защитное щупальце Древнего бога для наземного боя.", tentacle_abilities, False),
        "n03A": ("Йогг`Сарон", "Древний бог, призывающий войска и поддерживающий их магией. После «Служения Йогг`Сарону» становится столицей игрока.", [
            ("Смертельная связь", "перераспределяет урон между связанными вражескими войсками."),
            ("Божественное видение", "открывает обзор и обнаруживает невидимые войска."),
            ("Покровительство бога", "восстанавливает союзнику здоровье и ману."),
            ("Щупальце Йогг`Сарона", "призывает временное щупальце."),
            ("Призыв бессмертных стражей", "создаёт восемь Бессмертных стражей на ограниченное время."),
            ("Призыв сущностей Бездны", "создаёт пятнадцать Могущественных Сущностей бездны на ограниченное время."),
            ("Портал в Бездну", "выпускает Тварь из Бездны."),
        ], True),
    }
    ops, strings = [], []
    for code, (name, role, abilities, air) in specs.items():
        old = objects[code]["fields"]
        marker = "ЗДАНИЕ:" if old["isbldg"] == "1" else "ЮНИТ:"
        text = "|cffa6afb8" + marker + "|cffced4da " + role
        if abilities:
            text += "|n|n|cffa6afb8Способности:|cffced4da" + "".join("|n- " + ref(n) + ": " + effect for n, effect in abilities)
        if code == "n03A":
            text += ("|n|n|cffa6afb8Усиление при снижении здоровья:|cffced4da"
                     "|n- Ниже |cffffffff17000|cffced4da здоровья получает «Залповый огонь»; требуется одноимённое исследование."
                     "|n- Ниже |cffffffff15000|cffced4da здоровья получает «Подчинение». Взятие под контроль сохраняет полученные способности.")
        text += "|n|nАтакует " + ("наземные и воздушные" if air else "наземные") + " цели.|r"
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old["hotkey"])
        values = {"name": title, "tip": title + (" (|cffffffff" + key + "|r)" if key else ""), "ubertip": text}
        for field, value in values.items():
            op = dict(type="unit", id=code, field=field, value=value, marker=marker)
            if code in ("nfgt", "uloc"):
                op["base_object"] = True
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
    inv = dict(scope="Безликие: призывы, Йогг`Сарон и его щупальца; общие nfgt/uloc",
               strings=strings, in_game_checked=False, variants=["SD", "HD"],
               evidence=["faceless_remaining_units_before.json", "OldGods.lua: InitTrig_AncienGods_Add_MassAttak, InitTrig_AncientGods_add_MindControl", "Bezlikie.lua: Trig_Sluga_qqgsarona"],
               remaining=["Игра: призывы, обе атаки Твари и динамические способности Йогг`Сарона", "OldGods.lua: случайные призывы n04K/n04L сейчас ссылаются на Пиратский порт и Serpent's Lair; механику в этой задаче не менять"])
    (folder / "faceless_summons.json").write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_summons_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Read the scripted unlocks separately, including every declared ability level.
    fields = "name,hero,levels,hotkey,researchhotkey,researchtip,researchubertip,tip1,tip2,ubertip1,ubertip2,code,dataa1,dataa2,datab1,datac1,area1,requires,targs1,targs2"
    dynamic = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A0T3,A0W4", "--fields", fields]))
    (folder / "faceless_yogg_unlocks_before.json").write_text(json.dumps(dynamic, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ops, strings = [], []
    for obj in dynamic["objects"]:
        code, old = obj["id"], obj["fields"]
        name = "Залповый огонь" if code == "A0T3" else "Подчинение"
        if code == "A0T3":
            body = ("Позволяет поражать до |cffffffff9|cffced4da вражеских целей в радиусе |cffffffff600|cffced4da. "
                    "Урон каждой цели: |cffffffff300|cffced4da; предел урона: |cffffffff3000|cffced4da."
                    "|n|n|cffe6c07bЙогг`Сарон получает способность при снижении здоровья ниже 17000. Требуется исследование «Залповый огонь».|cffced4da")
        else:
            body = ("Навсегда подчиняет вражеского или нейтрального юнита не выше |cffffffff7|cffced4da-го уровня. "
                    "Не действует на героев и здания."
                    "|n|n|cffe6c07bЙогг`Сарон получает способность при снижении здоровья ниже 15000.|cffced4da")
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old["hotkey"]).strip('"')
        short = title + (" (|cffffffff" + key + "|r)" if key else "")
        values = {"name": title}
        for level in range(1, int(old["levels"]) + 1):
            values["tip" + str(level)] = short
            values["ubertip" + str(level)] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"
        if old["hero"] == "1":
            learnkey = resolve(old["researchhotkey"]).strip('"')
            values["researchtip"] = title + (" (|cffffffff" + learnkey + "|r)" if learnkey else "")
            values["researchubertip"] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|n|nОба уровня имеют одинаковый предел уровня цели.|r"
        for field, value in values.items():
            ops.append(dict(type="ability", id=code, field=field, value=value))
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))
    (folder / "faceless_yogg_unlocks.json").write_text(json.dumps(dict(scope="Способности, добавляемые Йогг`Сарону при снижении здоровья", strings=strings, in_game_checked=False), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "faceless_yogg_unlocks_plan.json").write_text(json.dumps(dict(operations=ops), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
