"""Prepare the two race markers and the Yogg-Saron victory notification."""
import json
from faceless_text_batch import ROOT
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    before = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", "R07M,R0F9", "--fields", "name1,tip1,ubertip1,maxlevel,effect1,effect2"]))
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    bodies = {
        "R0F9": "Расовое знание безликих, необходимое для найма Верховного генерала. Выдаётся автоматически при выборе расы.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВерховный генерал|cffced4da в Ульдуаре (внешнем).",
        "R07M": "Сведения о безликих. Н`раки появились из органической материи разрушенных тел Древних богов в первобытную эру Азерота.",
    }
    ops, strings = [], []
    for obj in before["objects"]:
        assert obj["fields"]["maxlevel"] == "1"
        values = {"name1": "|cffe4cfa3Безликие|r", "tip1": "|cffe4cfa3Безликие|r",
                  "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da " + bodies[obj["id"]] + "|r"}
        for field, value in values.items():
            ops.append(dict(type="upgrade", id=obj["id"], field=field, value=value))
            strings.append(dict(rawcode=obj["id"], field=field, before=resolve(obj["fields"][field]), after=value))
    inv = dict(scope="Два расовых маркера безликих", objects_before=before, strings=strings, variants=["SD","HD"], in_game_checked=False,
               evidence=["faceless_marker_consumers.json", "04_race_selection.lua: SetPlayerTechResearchedSwap R0F9", "13_Races.lua: bezlikie", "h0DR trains U02F; U02F requires R0F9"],
               notes=["R07M has no acquisition/use reference found; its existing lore is edited without attributing gameplay bonuses."])
    for name, value in [("faceless_markers", inv), ("faceless_markers_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    message = ("|cffa6afb8СОБЫТИЕ:|cffced4da |cffe4cfa3Йогг`Сарон|cffced4da повержен. Победитель получает "
               "|cffc8e08720000|cffced4da золота и |cffc8e08720000|cffced4da древесины. "
               "На месте гибели остаётся |cffa9c7deКасание безумия|cffced4da.|r")
    message_inv = dict(scope="Сообщение о гибели Йогг`Сарона", in_game_checked=False,
                       strings=[dict(rawcode="Trig_Qogg_Die_Actions", field="message", reference_before="TRIGSTR_20558", before=wts[20558], after=message)],
                       evidence="OldGods.lua: Trig_Qogg_Die_Actions: +20000 gold, +20000 lumber, SpawnGroundItem I01Q",
                       remaining=["Проверить сообщение и предмет в игре", "Имя после Служения: убрать ошибочный Lua-префикс cffd45e19r"])
    (folder / "faceless_messages.json").write_text(json.dumps(message_inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
