"""Prepare shared shipyard and its three ship cards from their actual contents."""
import json
from pathlib import Path
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    before = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h0D1,h0D2,h0CZ,h0D0", "--fields",
                          "name,tip,ubertip,hotkey,abillist,trains,researches,weapson,targs1"]))
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"
    white = lambda s: "|cffffffff" + str(s) + "|cffced4da"
    names = {"h0D1": "Верфь", "h0D2": "Транспорт", "h0CZ": "Фрегат", "h0D0": "Линкор"}
    common = [
        ("Тактическое ускорение", "временно повышает скорость передвижения ценой увеличения получаемого урона; требует «Дополнительных парусов»"),
        ("Массированный обстрел", "поражает противников в выбранной области; требует «Обстрела»"),
        ("Починка", "восстанавливает здоровье при поддержании; требует одноимённого исследования"),
    ]
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        if code == "h0D1":
            assert old["trains"] == "h0D2,h0CZ,h0D0"
            assert old["researches"] == "R005,R006,R007,R002,R003"
            assert old["abillist"] == "A15N"
            body = ("ЗДАНИЕ:|cffced4da Строит корабли и исследует общие улучшения флота."
                    "|n|n|cffa6afb8Обучает:|cffced4da|n- " + "|n- ".join(ref(names[k]) for k in ("h0D2", "h0CZ", "h0D0"))
                    + ".|n|n|cffa6afb8Исследования:|cffced4da|n- "
                    + "|n- ".join(ref(s) for s in ("Обстрел", "Дополнительные паруса", "Починка", "Орудия флота", "Укреплённый корпус"))
                    + ".|n|n" + ref("Зона ремонта") + " восстанавливает " + "|cffc8e0872,5|cffced4da здоровья/сек. союзным наземным механическим войскам в радиусе " + white(550) + ".")
            marker = "ЗДАНИЕ:"
        else:
            marker = "ЮНИТ:"
            if code == "h0D2":
                assert old["abillist"] == "A00I,A00A,A00B,Sch5,Slo3,Sdro"
                role = "Неатакующий корабль для перевозки наземных союзных войск. Грузовой отсек вмещает " + white(10) + " мест."
                abilities = [
                    ("Магическая посадка", "перемещает подходящие войска игрока из выбранной области к выделенным транспортам того же типа и отдаёт приказ посадки"),
                    ("Посадка на борт", "принимает выбранного союзника при наличии места"),
                    ("Высадка", "высаживает груз в указанном месте"),
                    common[0], common[2],
                ]
            else:
                role = "Боевой корабль для поддержки флота и обстрела противников." if code == "h0CZ" else "Тяжёлый боевой корабль для обстрела наземных целей и зданий."
                abilities = [
                    ("Боковые пушки фрегата" if code == "h0CZ" else "Боковые пушки линкора",
                     "автоматически стреляют по вражеским механическим целям, в том числе на ходу" + ("; требуют «Обстрела»" if code == "h0D0" else "")),
                    *common,
                    ("Прицельная пальба", "наносит урон и оглушает органическую цель") if code == "h0CZ" else
                    ("Абордаж", "захват кораблей в текущей версии недоступен"),
                    ("Назначение флагмана", "усиливает корабль и открывает выбор постоянной ауры"),
                ]
                expected = "A009,A002,A00B,A00G,A00A,A1PP" if code == "h0CZ" else "A009,A003,A00B,A00G,A00A,A001"
                assert old["abillist"] == expected
            body = "ЮНИТ:|cffced4da " + role + "|n|n|cffa6afb8Способности:|cffced4da|n- " + "|n- ".join(ref(n) + ": " + s + "." for n, s in abilities)
            if code != "h0D2":
                assert old["weapson"] == "1"
                body += "|n|nАтакует наземные" + (" и воздушные" if "air" in old["targs1"].split(",") else "") + " цели."
            else:
                assert old["weapson"] == "0"
        title = "|cffe4cfa3" + names[code] + "|r"
        key = resolve(old["hotkey"]).strip('"')
        values = {"name": title, "tip": title + (" (|cffffffff" + key + "|r)" if key else ""), "ubertip": "|cffa6afb8" + body + "|r"}
        for field, value in values.items():
            ops.append(dict(type="unit", id=code, field=field, value=value, marker=marker))
            strings.append(dict(rawcode=code, field=field, before=resolve(old[field]), after=value))
    inventory = dict(scope="Общая верфь рабочего Безликих и все три обучаемых корабля", objects_before=before,
                     strings=strings, in_game_checked=False,
                     remaining=["Check training, build hotkey and research gates in game",
                                "Check tooltip heights, ship skills and target restrictions in SD/HD",
                                "Flagship final numerical bonuses remain unverified; boarding unavailable in current Lua"])
    for filename, value in (("faceless_naval_cards", inventory), ("faceless_naval_cards_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
