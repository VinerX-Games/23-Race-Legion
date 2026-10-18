"""Prepare the first Faceless unit text batch from current object data."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/ui_text"


def main():
    ids = ["h0I9", "h0IA", "h0IB", "h0IC"]
    fields = "name,tip,ubertip,hotkey,abillist,weapson,targs1,atktype1,upgrades"
    objects = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(ids),
                           "--fields", fields]))["objects"]
    wts = load_wts_strings()

    def resolve(value):
        return wts[int(value[8:])] if value.startswith("TRIGSTR_") else value

    def ref(value):
        return "|cffa9c7de" + value + "|cffced4da"

    burn = (ref("Разрушение Эфира") + ": атаки сжигают ману цели "
            "(требуется исследование «Разрушение Эфира»).")
    specs = {
        "h0I9": ("Безликий дозорный", "Боец с атакой хаосом для наземных сражений.", []),
        "h0IA": ("Безликий разрушитель", "Осадный боец для разрушения зданий.", []),
        "h0IB": ("Сущность бездны", "Боец с колющей атакой и усилениями против заклинателей.", [
            burn,
            ref("Сотрясение Бездны") + ": атаки могут оглушить цель и нанести дополнительный урон "
            "(требуется исследование «Улучшение Сущности»).",
        ]),
        "h0IC": ("Могущественная Сущность бездны", "Боец с атакой хаосом и критическими ударами.", [
            ref("Сила Бездны") + ": атаки могут нанести увеличенный урон.", burn,
        ]),
    }
    operations, strings = [], []
    for obj in objects:
        rawcode, old = obj["id"], obj["fields"]
        name, role, abilities = specs[rawcode]
        text = "|cffa6afb8ЮНИТ:|cffced4da " + role
        if abilities:
            text += "|n|n|cffa6afb8Способности:|cffced4da|n- " + "|n- ".join(abilities)
        text += "|n|nАтакует наземные цели.|r"
        key = resolve(old["hotkey"])
        values = {"name": "|cffe4cfa3" + name + "|r",
                  "tip": "|cffe4cfa3" + name + "|r (|cffffffff" + key + "|r)",
                  "ubertip": text}
        for field, value in values.items():
            operations.append(dict(type="unit", id=rawcode, field=field, value=value))
            strings.append(dict(rawcode=rawcode, field=field, source="object data / war3map.wts",
                                reference_before=old[field], before=resolve(old[field]), after=value))
    inventory = dict(scope="Безликие: первая партия юнитов; не вся категория",
                     variants=["SD", "HD"], in_game_checked=False,
                     objects_before=objects, strings=strings,
                     evidence={"abilities": ["A10X: Afbk, requires R0EL",
                                             "A10W: AHbh, requires R0EK, levels=1",
                                             "A10Z: AOcr, levels=1"],
                               "attacks": "weapson=1; targs1 includes ground and excludes air",
                               "lua": "Bezlikie.lua: no references to these four units or three abilities"},
                     remaining=["Остальные юниты, рабочие, призывы и формы",
                                "Собственные карточки способностей и исследований",
                                "Проверка отображения в Warcraft III"])
    (OUT / "faceless_units_01.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "faceless_units_01_plan.json").write_text(json.dumps(dict(operations=operations), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
