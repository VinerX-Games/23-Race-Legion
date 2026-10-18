"""Localize inherited engine commands while preserving bindings and format tokens."""
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path
from implement_draenei_rework import register_imports

ROOT = Path(__file__).resolve().parent.parent


def parse(text):
    sections, current = {}, None
    for line in text.splitlines():
        if line.startswith("["):
            current = line[1:-1]
            sections[current] = {}
        elif current and "=" in line and not line.startswith("//"):
            key, value = line.split("=", 1)
            sections[current][key] = value
    return sections


def main():
    source = ROOT / ".cache/wc3/game-metadata/ruru_commandstrings.txt"
    before = parse(source.read_text(encoding="utf-8-sig"))
    after = {s: dict(fields) for s, fields in before.items()}
    titles = {"CmdMove": "Перемещение", "CmdAttack": "Атака", "CmdAttackGround": "Атака по области",
              "CmdHoldPos": "Удержание позиции", "CmdPatrol": "Патрулирование", "CmdPurchase": "Продажа предметов",
              "CmdRally": "Точка сбора", "CmdSelectSkill": "Способности героя", "CmdStop": "Остановка"}
    bodies = {
        "CmdMove": "Перемещает войска в указанную точку. При выборе союзника войска следуют за ним.",
        "CmdAttack": "При выборе точки войска движутся к ней, атакуя встреченных врагов. При выборе противника сосредоточивают атаки на этой цели.",
        "CmdAttackGround": "Приказывает обстреливать указанную область до отмены или получения другого приказа.",
        "CmdHoldPos": "Удерживает войска на месте. Они атакуют доступных противников, но не преследуют их.",
        "CmdPatrol": "Приказывает войскам перемещаться между текущей позицией и указанной точкой, вступая в бой со встреченными врагами.",
        "CmdPurchase": "Позволяет продавать предметы магазину.",
        "CmdRally": "Задаёт точку назначения для новых войск. Рабочие могут сразу приступить к добыче, если целью выбран подходящий источник ресурсов.",
        "CmdSelectSkill": "Открывает меню способностей героя для распределения доступных очков навыков.",
        "CmdStop": "Прерывает текущий приказ. Войска останавливаются и могут самостоятельно атаковать ближайших противников.",
        "CmdCancel": "Отменяет текущий выбор приказа или цели.",
        "CmdCancelBuild": "Отменяет строительство или выбор места для здания.",
        "CmdCancelTrain": "Прерывает обучение выбранного в очереди воина.",
        "CmdCancelRevive": "Прерывает воскрешение героя.",
    }
    for section, fields in after.items():
        if not section.startswith("Cmd"):
            continue
        title = titles.get(section)
        if section.startswith("CmdBuild"):
            title, body = "Строительство", "Открывает список доступных зданий."
        else:
            title = title or "Отмена"
            body = bodies[section]
        fields["Tip"] = "|cffe4cfa3" + title + "|r"
        fields["Ubertip"] = '"|cffa6afb8КОМАНДА:|cffced4da ' + body + '|r"'
        assert {k: v for k, v in fields.items() if k.startswith("Hotkey")} == {
            k: v for k, v in before[section].items() if k.startswith("Hotkey")}
    for key, value in before["Errors"].items():
        old = next(csv.reader([value], skipinitialspace=True))
        new = []
        for message in old:
            # Preserve each race alternative and every printf argument in order.
            message = re.sub(r"\|c[0-9a-fA-F]{8}|\|[rR]", "", message)
            if key == "Nofood":
                message = "Недостаточно доступной пищи для создания войска."
            positive = key in {"Goldandlumberfromally", "Goldfromally", "Lumberfromally", "Controlgranted"}
            warning = key in {"Herodies", "Allyunderattack", "Allytownattack", "Herodeath", "Goldminelow", "Goldminedestroyed", "Allyminimapping"}
            event = positive or warning or key in {"Upkeeplevel", "Herokilledhero", "Controlrevoked"}
            color = "c8e087" if positive else "e6c07b" if warning else "e69a8d" if not event or key == "Controlrevoked" else "ced4da"
            prefix = "СОБЫТИЕ:" if event else "НЕДОСТУПНО:"
            new.append('"|cffa6afb8' + prefix + '|cff' + color + ' ' + message.replace('"', '""') + '|r"')
        fields_value = ",".join(new)
        after["Errors"][key] = fields_value
        decoded = next(csv.reader([fields_value], skipinitialspace=True))
        assert len(decoded) == len(old)
        assert [re.findall(r"%[-+ #0-9.]*[a-zA-Z]", s) for s in decoded] == [re.findall(r"%[-+ #0-9.]*[a-zA-Z]", s) for s in old]
    text = "// Map-owned Russian command strings; preserve original engine hotkeys.\n\n"
    text += "\n\n".join("[" + section + "]\n" + "\n".join(k + "=" + v for k, v in fields.items()) for section, fields in after.items()) + "\n"
    assert parse(text) == after
    target = ROOT / "map.w3x/Units/CommandStrings.txt"
    if target.exists():
        previous = ROOT / "docs/ui_text/faceless_standard_commands.json"
        previous_hash = json.loads(previous.read_text(encoding="utf-8"))["file_sha256"] if previous.exists() else None
        assert target.read_text(encoding="utf-8") == text or hashlib.sha256(target.read_bytes()).hexdigest() == previous_hash, "Refuse to overwrite an independently changed command file"
    imports = ROOT / "map.w3x/war3map.imp"
    backup = ROOT / ".cache/wc3/faceless_standard_commands_before.imp"
    if not backup.exists():
        shutil.copy2(imports, backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    added = register_imports(imports, ["Units/CommandStrings.txt"])
    inventory = dict(scope="19 inherited commands and 216 engine message keys, including 234 race alternatives",
                     source="Installed Warcraft III: war3.w3mod:_locales/ruru.w3mod:units/commandstrings.txt",
                     source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), before=before, after=after,
                     target="map.w3x/Units/CommandStrings.txt", file_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                     import_added=added, hotkeys_preserved=True, printf_arguments_and_alternatives_preserved=True,
                     verification_owner="Игровую проверку выполняет пользователь", in_game_checked=False,
                     limitations=["Static file/import validation does not prove rendering or custom client hotkey precedence"])
    out = ROOT / "docs/ui_text/faceless_standard_commands.json"
    out.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(commands=len(after)-1, engine_message_keys=len(after["Errors"]), imports_added=added)))


if __name__ == "__main__":
    main()
