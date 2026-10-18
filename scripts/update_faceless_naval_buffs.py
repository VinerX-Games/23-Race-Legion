"""Prepare fleet status text with all shared aura sources considered."""
import json
from pathlib import Path
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    before = json.loads((folder / "faceless_naval_buffs_before.json").read_text(encoding="utf-8"))
    users = json.loads((folder / "faceless_naval_buff_users.json").read_text(encoding="utf-8"))
    assert users["scanned_objects"] < users["max"] and users["scanned_objects"] > 1000
    specs = {
        "B002": ("Все паруса", "Скорость передвижения |cffc8e087повышена|cffced4da, но получаемый урон |cffe69a8dувеличен|cffced4da. Величины зависят от уровня ускорения."),
        "BEar": ("Аура урона", "Повышает урон атак. Величина бонуса и затрагиваемый тип атак — ближние или дальние — зависят от источника ауры."),
        "BHad": ("Аура брони", "Изменяет броню. Источник ауры может давать бонус к защите или снижать её; величина и направление эффекта указаны в описании способности-источника."),
        "BOae": ("Аура скорости", "Изменяет скорость передвижения и атаки. Источник ауры может ускорять или замедлять войска; величины указаны в описании способности-источника."),
    }
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ops, strings = [], []
    for obj in before["objects"]:
        code, old = obj["id"], obj["fields"]
        name, body = specs[code]
        values = {"bufftip": "|cffe4cfa3" + name + "|r", "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            op = dict(type="buff", id=code, field=field, value=value)
            if code != "B002":
                op["base_object"] = True
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, before=resolve(old.get(field, "")), after=value))
    inventory = dict(scope="Четыре оставшихся видимых эффекта флота, общие с другими расами",
                     objects_before=before, users=users, strings=strings, in_game_checked=False,
                     evidence=["All 4103 abilities enumerated with --max 100000, only declared levels considered",
                               "BHad also used by negative armor A094; BOae also used by negative speed A1MD",
                               "BEar used by ranged and melee bonus sources, so the effect cannot promise only ranged damage"],
                     remaining=["Verify display and stacking of shared buffs in game"])
    for filename, value in (("faceless_naval_buffs", inventory), ("faceless_naval_buffs_plan", dict(operations=ops))):
        (folder / (filename + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
