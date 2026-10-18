"""Prepare building abilities, Yogg-Saron spells and remaining linked effects."""
import json
from faceless_text_batch import ROOT
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    snapshot = json.loads((folder / "faceless_remaining_abilities_before.json").read_text(encoding="utf-8"))
    objects = {obj["id"]: obj for obj in snapshot["objects"]}
    white = lambda v: "|cffffffff" + str(v) + "|cffced4da"
    green = lambda v: "|cffc8e087" + str(v) + "|cffced4da"
    ref = lambda v: "|cffa9c7de" + str(v) + "|cffced4da"
    specs = {
        "A11G": ("Порождение придатка", "Бесплатно создаёт " + ref("Малое порождение") + " в выбранном месте. Оно увеличивает доход владельца и поддерживает союзников аурой. Восстановление: " + white(60) + " сек."),
        "A06M": ("Дымка бездны", "Повышает скорость передвижения союзников в радиусе " + white(900) + " на " + green("6%") + ", восстановление здоровья — на " + green("1,5") + " ед. в секунду. Действует также на источник ауры."),
        "A0DW": ("Сильный удар", "С вероятностью " + white("12%") + " атака наносит " + white(10) + " дополнительного урона и оглушает цель на " + white(1) + " сек. Не оглушает героев."),
        "A0PB": ("Кошмар", "Оглушает органического противника на " + white(10) + " сек.; героя — на " + white(5) + " сек. Само оглушение не наносит урона."),
        "A0RS": ("Рассекающий удар", "Атаки наносят окружающим основную цель наземным врагам " + white("40%") + " урона от атаки. Радиус: " + white(250) + "."),
        "ACce": ("Рассекающий удар", "Атаки наносят окружающим основную цель наземным врагам " + white("7%") + " урона от атаки. Радиус: " + white(150) + "."),
        "ACtn": ("Порождение щупальца", "Призывает одно " + ref("Щупальце") + " на " + white(180) + " сек. Щупальце атакует наземные цели."),
        "A16Q": ("Смертельная связь", "Связывает до " + white(60) + " органических наземных врагов в радиусе " + white(500) + " на " + white(75) + " сек. " + white("100%") + " получаемого ими урона перераспределяется между связанными целями."),
        "A16R": ("Божественное видение", "Открывает обзор в выбранной области радиусом " + white(99999) + " на " + white(12) + " сек. Обнаруживает невидимые войска."),
        "A16T": ("Покровительство бога", "За " + white(12) + " сек. восстанавливает дружественной или нейтральной органической цели " + green(4000) + " здоровья и " + green(4000) + " маны."),
        "A0T7": ("Щупальце Йогг`Сарона", "Призывает одно " + ref("Щупальце Йогг`Сарона") + " на " + white(30) + " сек. Оно атакует наземные цели и владеет «Рассекающим ударом»."),
        "A1NA": ("Призыв бессмертных стражей", "Призывает " + white(8) + " " + ref("Бессмертных стражей") + " на " + white(60) + " сек. Они атакуют наземные цели."),
        "A1NB": ("Призыв сущностей Бездны", "Призывает " + white(15) + " " + ref("Могущественных Сущностей бездны") + " на " + white(60) + " сек. Они атакуют наземные цели."),
        "A1NC": ("Портал в Бездну", "Открывает портал и выпускает одну " + ref("Тварь из Бездны") + ". Восстановление: " + white(400) + " сек.|n|n|cffe6c07bДождитесь завершения призыва.|cffced4da"),
    }
    for code in ("A10T", "A10U", "A10V"):
        count = objects[code]["fields"]["dataa1"]
        specs[code] = ("Рой саранчи", "Призывает рой из " + white(count) + " насекомых, атакующих наземных и воздушных врагов в радиусе " + white(800) + ". "
                       "Возвращаясь к источнику роя, насекомые восстанавливают ему здоровье в размере " + green("75%") + " нанесённого ими урона. Действует " + white(30) + " сек.")
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    ops, strings = [], []
    for code, (name, body) in specs.items():
        old = objects[code]["fields"]
        assert old["levels"] == "1"
        title = "|cffe4cfa3" + name + "|r"
        key = resolve(old["hotkey"]).strip('"')
        values = {"name": title, "tip1": title + (" (|cffffffff" + key + "|r)" if key else ""),
                  "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            ops.append(dict(type="ability", id=code, field=field, value=value))
            strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
    inv = dict(scope="Безликие: 17 строительных, вспомогательных и связанных с Йогг`Сароном способностей",
               variants=["SD", "HD"], in_game_checked=False, strings=strings,
               evidence=["faceless_remaining_abilities_before.json", "faceless_remaining_ability_metadata.json"],
               remaining=["Проверить цели Смертельной связи, возврат здоровья роя и призывы в Warcraft III", "Согласовать новые названия в карточках", "Проверить размещённых существ и путь получения Везакса"])
    for name, value in [("faceless_remaining_abilities", inv), ("faceless_remaining_abilities_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
