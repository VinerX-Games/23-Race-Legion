# -*- coding: utf-8 -*-
"""Generate registry and plan for Ice Troll race marker R0L1, items and messages audit."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

def main():
    folder = ROOT / "docs/ui_text"
    before = require(cli(["get-object", "--type", "upgrade", "--id", "R0L1", "--fields", "name1,tip1,ubertip1,maxlevel"]))
    wts = hw.load_wts_strings()
    resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    body = ("Расовое знание ледяных троллей Драккари, необходимое для найма Властелина Холода. "
            "Выдаётся автоматически при выборе расы.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n"
            "- |cffa9c7deВластелин Холода|cffced4da в Зул`Драке.")

    values = {
        "name1": "|cffe4cfa3Ледяные тролли|r",
        "tip1": "|cffe4cfa3Ледяные тролли|r",
        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da " + body + "|r"
    }

    ops = []
    strings = []
    for f, val in values.items():
        ops.append({"type": "upgrade", "id": "R0L1", "field": f, "value": val})
        strings.append({
            "rawcode": "R0L1",
            "field": f,
            "before": resolve(before["fields"].get(f, "")),
            "after": val
        })

    inv = {
        "scope": "Расовый маркер ледяных троллей R0L1, предметы, сообщения и специальные интерфейсы",
        "objects_before": before,
        "strings": strings,
        "variants": ["SD", "HD"],
        "in_game_checked": False,
        "evidence": [
            "04_race_selection.lua:329: SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, GetOwningPlayer(GetTriggerUnit()))",
            "libraries/13_Races.lua:3600: SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, p)",
            "h09K Зул`Драк trains O06L Властелин Холода",
            "O06L requires R0L1"
        ],
        "items_audit": "Не применимо: у Ледяных троллей нет собственных предметов; поля sellitems/makeitems пусты у всех 16 зданий; в скриптах карты нет создания или выдачи расовых предметов.",
        "messages_audit": "Не применимо: триггеры расы в IceTrolls.lua не содержат видимых игровых сообщений (DisplayTextToPlayer отключены в отладочных комментариях).",
        "interfaces_audit": "Не применимо: раса не использует специальных диалогов, интерфейсных панелей или фреймов."
    }

    (folder / "ice_troll_items_messages.json").write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "ice_troll_items_messages_plan.json").write_text(json.dumps({"operations": ops}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated plan with {len(ops)} operations in {folder / 'ice_troll_items_messages_plan.json'}")

if __name__ == "__main__":
    main()
