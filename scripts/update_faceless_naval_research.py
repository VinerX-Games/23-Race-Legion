"""Prepare the shared shipyard research text from actual consumers and effects."""
import json
import re
from pathlib import Path

from wc3_hivewe import load_wts_strings
from wc3_object_tools import cli, require

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    names = {"R005": "Обстрел", "R006": "Дополнительные паруса", "R007": "Починка",
             "R002": "Орудия флота", "R003": "Укреплённый корпус"}
    fields = ["maxlevel", "effect1", "effect2", "base1", "mod1", "base2", "mod2"]
    fields += [f"{field}{level}" for field in ("name", "tip", "ubertip", "hotkey") for level in range(1, 7)]
    before = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(names), "--fields", ",".join(fields)]))
    consumers = json.loads((folder / "faceless_shared_naval_consumers.json").read_text(encoding="utf-8"))["objects"]
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    plain = lambda s: re.sub(r"\|c[0-9a-fA-F]{8}|\|r", "", s)
    bonus = lambda n, suffix="": "|cffc8e087+" + str(n) + suffix + "|cffced4da"
    number = lambda n: "|cffffffff" + str(n) + "|cffced4da"
    ref = lambda s: "|cffa9c7de" + s + "|cffced4da"
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        selected = [o for o in consumers if code in o["fields"]["upgrades"].split(",")]
        for level in range(1, int(old["maxlevel"]) + 1):
            affected = []
            for unit in selected:
                entry = ref(plain(unit["name"]))
                if code == "R002":
                    entry += ": " + bonus(level) + "–" + bonus(level * int(unit["fields"]["sides1"])) + " к урону"
                elif code == "R003":
                    entry += ": " + bonus(level * int(unit["fields"]["defup"])) + " к броне"
                if entry not in affected:
                    affected.append(entry)
            if code == "R005":
                effect = "Суммарный бонус к дальности атак: " + bonus(30 * level) + "."
                if level == 1:
                    effect += " Открывает «Массированный обстрел» и боковые пушки линкора у кораблей, имеющих эти способности."
            elif code == "R006":
                effect = "Суммарный бонус к скорости передвижения перечисленных транспортов: " + bonus(5 * level, "%") + "."
                if level == 1:
                    effect += " Открывает «Тактическое ускорение» у кораблей, имеющих эту способность, включая фрегаты и линкоры."
            elif code == "R007":
                effect = "Суммарный бонус к максимальному здоровью перечисленных кораблей: " + bonus(50 * level) + "."
                if level == 1:
                    effect += " Открывает способность «Починка» у кораблей, имеющих её."
            elif code == "R002":
                effect = "Увеличивает урон атак перечисленных войск. Суммарная прибавка к диапазону урона указана у каждой цели."
            else:
                effect = "Суммарный бонус к максимальному здоровью: " + bonus(100 * level) + ". Прибавка к броне указана у каждой цели."
            title = "|cffe4cfa3" + names[code] + " — уровень " + str(level) + "|r"
            key = resolve(old["hotkey" + str(level)]).strip('"')
            values = {"name": title, "tip": title + (" (|cffffffff" + key + "|r)" if key else ""),
                      "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da " + effect
                      + "|n|n|cffa6afb8Уровень:|cffced4da " + number(level) + " из " + number(old["maxlevel"])
                      + ". Бонусы указаны относительно состояния без исследования."
                      + "|n|n|cffa6afb8Затрагивает:|cffced4da|n- " + "|n- ".join(affected) + ".|r"}
            for field, value in values.items():
                field += str(level)
                ops.append(dict(type="upgrade", id=code, field=field, value=value))
                strings.append(dict(rawcode=code, field=field, before=resolve(old[field]), after=value))
    inventory = dict(scope="Пять общих исследований верфи Безликих, все 23 уровня", objects_before=before,
                     consumers=consumers, strings=strings, in_game_checked=False,
                     evidence=["Installed UpgradeEffectMetaData: ratr/rmov/rhpx/ratd/rarm", "All object-data upgrade consumers, including pa17"],
                     remaining=["Verify Lua-driven A00G/A00B/A00A levels in engine: callbacks use a shared player variable",
                                "R005 levels 4/5 do not set the ability level on newly trained ships",
                                "Check long shared-recipient lists visually; no engine validation claimed"])
    for filename, content in (("faceless_naval_research", inventory), ("faceless_naval_research_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
