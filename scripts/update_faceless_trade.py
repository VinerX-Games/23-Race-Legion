"""Prepare the trade service sold by Faceless capitals and all 100 counter levels."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    fields = ["name", "levels", "code"] + [f"{field}{n}" for field in ("tip", "ubertip") for n in range(1, 101)]
    before = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A0SM", "--fields", ",".join(fields)]))
    unit = require(cli(["get-objects-bulk", "--type", "unit", "--ids", "h0G8", "--fields", "name,tip,ubertip,hotkey,goldcost,lumbercost"]))
    old = before["objects"][0]["fields"]
    assert old["levels"] == "100" and old["code"] == "APai"
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    title = "|cffe4cfa3Налаженная торговля|r"
    values = {"name": title}
    for n in range(1, 101):
        values["tip" + str(n)] = title
        values["ubertip" + str(n)] = ("|cffa6afb8СПОСОБНОСТЬ:|cffced4da Учтённый вклад торговли этого здания в базовый доход золота за выплату: "
            "|cffc8e087+" + str(n * 75) + "|cffced4da. Это суммарное значение текущей ступени. Итоговый доход зависит от модификаторов экономики."
            "|n|n|cffa6afb8Ступень:|cffced4da |cffffffff" + str(n) + "|cffced4da из |cffffffff100|cffced4da.|r")
    ops, strings = [], []
    for field, value in values.items():
        ops.append(dict(type="ability", id="A0SM", field=field, value=value))
        strings.append(dict(rawcode="A0SM", field=field, before=resolve(old[field]), after=value))
    old = unit["objects"][0]["fields"]
    assert resolve(old["hotkey"]).strip('"') == "D" and old["goldcost"] == "0" and old["lumbercost"] == "9000"
    title = "|cffe4cfa3Торговля|r"
    values = {"name": title, "tip": title + " (|cffffffffD|r)",
              "ubertip": "|cffa6afb8УСЛУГА:|cffced4da Покупка торгового улучшения для здания. Увеличивает базовый доход золота владельца на "
              "|cffc8e08775|cffced4da за выплату и повышает ступень показателя «Налаженная торговля». Итоговый доход зависит от модификаторов экономики."
              "|n|nСтоимость — |cffffffff9000|cffced4da древесины. Покупка не создаёт постоянного воина.|r"}
    for field, value in values.items():
        ops.append(dict(type="unit", id="h0G8", field=field, value=value, marker="УСЛУГА:"))
        strings.append(dict(rawcode="h0G8", field=field, before=resolve(old[field]), after=value))
    inventory = dict(scope="Торговля главных зданий Безликих и все 100 уровней связанного показателя дохода",
                     objects_before=[before, unit], strings=strings, in_game_checked=False,
                     evidence=["01_core_economy.lua Trig_Moneta_C: remove sold token, income += 75, add/increment A0SM",
                               "54_count_dis.lua: recorded building trade contribution equals A0SM level * 75"],
                     limitations=["A0SM is capped at 100 levels; purchase callback does not explicitly enforce a purchase cap. Further-purchase/recalculation inconsistency is not changed by text work"],
                     verification_owner="Игровые проверки выполняет пользователь")
    for filename, value in (("faceless_trade", inventory), ("faceless_trade_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
