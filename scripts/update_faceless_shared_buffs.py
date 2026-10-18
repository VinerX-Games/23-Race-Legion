"""Prepare visible shared status tooltips without assigning false fixed values."""
import json
from faceless_text_batch import ROOT
from implement_draenei_rework import object_records
from wc3_hivewe import load_wts_strings


def main():
    folder = ROOT / "docs/ui_text"
    snapshot = json.loads((folder / "faceless_shared_buffs_before.json").read_text(encoding="utf-8"))
    active = json.loads((folder / "faceless_active_buff_sources.json").read_text(encoding="utf-8"))["buff_sources"]
    objects = {obj["id"]: obj for obj in snapshot["buffs"]["objects"]}
    specs = {
        "B01D": ("Защитная аура", "В зависимости от источника аура изменяет защиту или восстановление здоровья цели."),
        "B030": ("Аура восстановления", "Восстановление здоровья |cffc8e087ускорено|cffced4da. Величина бонуса определяется источником ауры."),
        "B05N": ("Тёмное усиление", "Урон от атак |cffc8e087повышен на 35%|cffced4da."),
        "B05O": ("Отголосок Йогг`Сарона", "Органические союзники ближнего боя восстанавливают здоровье в размере |cffc8e08710%|cffced4da урона своих атак."),
        "BEim": ("Обжигающий жар", "Существо окружено пламенем, наносящим |cffffffffпериодический урон|cffced4da находящимся рядом противникам."),
        "BHab": ("Аура маны", "Аура изменяет восстановление маны цели. Направление и величина изменения зависят от способности-источника."),
        "BHds": ("Божественный щит", "Цель |cffc8e087неуязвима|cffced4da на время действия щита."),
        "BHtc": ("Раскат грома", "Скорость передвижения и атаки |cffe69a8dснижена|cffced4da."),
        "BIcb": ("Порча", "Броня цели |cffe69a8dснижена|cffced4da."),
        "BNab": ("Кислотная бомба", "Цель поражена кислотой. Заклинание может наносить периодический урон и ослаблять броню; параметры определяются источником."),
        "BNht": ("Ужасающий вой", "Урон от атак цели |cffe69a8dснижен|cffced4da."),
        "BOsf": ("Призванное существо", "Существо создано призывающим заклинанием."),
        "BOwd": ("Призванное создание", "Существо создано магией призыва."),
        "BOwk": ("Танец ветра", "Цель |cffc8e087невидима|cffced4da и передвигается быстрее. Атака из невидимости получает дополнительный урон и раскрывает атакующего."),
        "BPSE": ("Оглушение", "Цель |cffe69a8dне может двигаться, атаковать и применять способности|cffced4da."),
        "BUan": ("Оживление мёртвых", "Существо поднято из трупа и временно сражается на стороне призвавшего его владельца."),
        "BUdd": ("Смерть и разложение", "Цель получает |cffe69a8dпериодический урон|cffced4da от разлагающей магии."),
        "BUfa": ("Морозный доспех", "Броня |cffc8e087повышена|cffced4da. Противники, атакующие цель в ближнем бою, временно теряют скорость передвижения и атаки."),
        "BUsl": ("Оцепенение", "Цель |cffe69a8dне может двигаться, атаковать и применять способности|cffced4da до окончания эффекта."),
        "Bakb": ("Боевые барабаны", "Урон от атак союзника |cffc8e087повышен|cffced4da под действием ауры."),
        "Bcrs": ("Проклятие", "Проклятие |cffe69a8dповышает вероятность промаха|cffced4da при атаке."),
        "Bena": ("Опутывание", "Цель |cffe69a8dне может двигаться|cffced4da. Воздушная цель притянута к земле и считается наземной."),
        "Beng": ("Опутывание", "Цель |cffe69a8dне может двигаться|cffced4da. Воздушная цель притянута к земле и считается наземной."),
        "Bfro": ("Замедление холодом", "Скорость передвижения цели |cffe69a8dснижена|cffced4da холодом."),
        "Brej": ("Омоложение", "Восстанавливающее заклинание восполняет |cffc8e087здоровье и/или ману|cffced4da цели в зависимости от источника."),
        "Bslo": ("Замедление", "Скорость передвижения и атаки цели |cffe69a8dснижена|cffced4da."),
        "Bspl": ("Духовная связь", "Часть получаемого урона перераспределяется между связанными существами. Доля урона определяется наложившим связь заклинанием."),
        "Bvng": ("Дух возмездия", "Из этих останков создан призванный дух."),
    }
    own = {"B01I", "B02L", "B08E", "B08F"}
    hidden = {"AEtr", "BEia", "BUts"}
    missing = set(snapshot["buffs"].get("missing", []))
    assert set(active) == set(specs) | own | hidden | missing
    for code in hidden:
        assert not objects[code]["fields"]["bufftip"] and not objects[code]["fields"]["buffubertip"]
    _, tables = object_records((ROOT / "map.w3x/war3map.w3h").read_bytes(), False)
    known = {obj["id"] for table in tables for obj in table}
    wts = load_wts_strings()
    resolve = lambda s: wts[int(s[8:])] if s.startswith("TRIGSTR_") else s
    strings, ops = [], []
    for code, (name, body) in specs.items():
        old = objects[code]["fields"]
        values = {"bufftip": "|cffe4cfa3" + name + "|r", "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da " + body + "|r"}
        for field, value in values.items():
            op = dict(type="buff", id=code, field=field, value=value)
            if code not in known:
                op["base_object"] = True
            ops.append(op)
            strings.append(dict(rawcode=code, field=field, reference_before=old[field], before=resolve(old[field]), after=value))
    inv = dict(scope="28 общих видимых эффектов, используемых способностями безликих и прямыми зависимостями", variants=["SD", "HD"],
               strings=strings, in_game_checked=False, evidence=["faceless_shared_buffs_before.json", "faceless_active_buff_sources.json", "faceless_shared_custom_buff_users.json"],
               notes=["B01D is shared by A077 and A1KB, B030 by A0DR/A0TE/A15N. Fixed direction or numbers cannot be attributed to every source.",
                      "BHab is used by both mana-regeneration bonuses and penalties; its status wording is neutral.",
                      "BUsl is reused for sleep and the stun of A113. Do not promise awakening on damage for all sources.",
                      "Shared status magnitudes can vary; exact numbers belong to the source spell tooltip. No buff IDs or stacking rules are changed."],
               excluded=dict(no_player_tooltip=sorted(hidden), unresolved_existing_ids=sorted(missing), own_buffs_in_separate_batch=sorted(own)),
               remaining=["Проверить показ эффектов в игре, включая английскую локаль клиента", "BHtb/Bust: существующие неразрешённые ссылки, механические поля в задаче текстов не менять"])
    for name, value in [("faceless_shared_buffs", inv), ("faceless_shared_buffs_plan", dict(operations=ops))]:
        (folder / (name + ".json")).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
