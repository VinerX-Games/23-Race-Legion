# -*- coding: utf-8 -*-
"""Generate complete plan and registry for Stromgard unit abilities, summons, and buffs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Unit & Summon Abilities
UNIT_ABILITIES = [
    # --- Работник (h0G9) ---
    {
        "id": "A0I3",
        "name": "|cffe4cfa3Небольшой скачок|r",
        "tip1": "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит владельца на расстояние до |cffffffff500|cffced4da.|n|nПерезарядка: |cff60b8d040|cffced4da сек.|r",
    },
    # --- Пехотинец (h0GS) - Повышение ---
    {
        "id": "A0VI",
        "name": "|cffe4cfa3Повышение|r",
        "tip1": "|cffe4cfa3Повышение|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пехотинец проходит обучение в бою. Для получения звания капитана необходимо уничтожить |cffffffff2|cffced4da вражеских юнитов.|n|nУничтожено врагов: |cffffffff0|cffced4da.|r",
        "tip2": "|cffe4cfa3Повышение|r",
        "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пехотинец проходит обучение в бою. Для получения звания капитана необходимо уничтожить |cffffffff2|cffced4da вражеских юнитов.|n|nУничтожено врагов: |cffffffff1|cffced4da.|r",
    },
    # --- Защита (h0GS, h0F4, h0GV, h0HE) ---
    {
        "id": "A0WG",
        "name": "|cffe4cfa3Защита|r",
        "tip1": "|cffe4cfa3Защита|r (|cffffffffQ|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает щит, отражая часть пронзающих атак обратно во врагов и снижая входящий урон от стрел на |cffffffff50%|cffced4da, но замедляя скорость перемещения на |cffffffff30%|cffced4da.|r",
        "untip1": "|cffe4cfa3Отменить «Защиту»|r (|cffffffffQ|r)",
        "unubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опускает щит, возвращая обычную скорость перемещения и стандартную защиту от пронзающих атак.|r",
    },
    # --- Стойкость щита (вспомогательное свойство Защиты) ---
    {
        "id": "A0WI",
        "name": "|cffe4cfa3Стойкость щита|r",
        "tip1": "|cffe4cfa3Стойкость щита|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрепляет оборону поднятым щитом, снижая урон от физических атак.|r",
    },
    # --- Защитник / Паладин защиты: Латный доспех ---
    {
        "id": "A0XS",
        "name": "|cffe4cfa3Латный доспех|r",
        "tip1": "|cffe4cfa3Латный доспех|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Тяжёлые латы поглощают до |cffffffff8|cffced4da ед. физического урона от каждой атаки. Минимальный получаемый урон: |cffffffff3|cffced4da ед.|r",
    },
    # --- Защитник / Паладин защиты: Аура защиты ---
    {
        "id": "A0XQ",
        "name": "|cffe4cfa3Аура защиты|r",
        "tip1": "|cffe4cfa3Аура защиты|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает броню союзников в радиусе |cffffffff300|cffced4da на |cffffffff+3|cffced4da ед.|r",
    },
    # --- Арбалетчик: Огненные стрелы ---
    {
        "id": "A0WO",
        "name": "|cffe4cfa3Огненные стрелы|r",
        "tip1": "|cffe4cfa3Огненные стрелы|r (|cffffffffW|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет болты огненной силой, добавляя |cffffffff+12|cffced4da ед. урона к каждой атаке.|n|nРасход маны: |cff6090e08|cffced4da.|r",
        "untip1": "|cffc3dbffПКМ – включить автоприменение.|r",
        "unubertip1": "|cffc3dbffПКМ – отключить автоприменение.|r",
    },
    # --- Рыцарь / Капитан: Критический удар ---
    {
        "id": "A0WP",
        "name": "|cffe4cfa3Критический удар|r",
        "tip1": "|cffe4cfa3Критический удар|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff15%|cffced4da наносит в |cffffffff1.5|cffced4da раза больше урона при атаке в ближнем бою.|r",
    },
    # --- Жрец: Волна исцеления ---
    {
        "id": "A0WM",
        "name": "|cffe4cfa3Волна исцеления|r",
        "tip1": "|cffe4cfa3Волна исцеления|r (|cffffffffE|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну света, восстанавливающую до |cffffffff200|cffced4da ед. здоровья цели и переходящую ещё до |cffffffff4|cffced4da союзников поблизости. Эффективность снижается с каждым переходом.|n|nРасход маны: |cff6090e090|cffced4da. Перезарядка: |cff60b8d010|cffced4da сек.|r",
    },
    # --- Жрец / Осел: Рассеивание заклинаний ---
    {
        "id": "A0WN",
        "name": "|cffe4cfa3Рассеивание заклинаний|r",
        "tip1": "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffQ|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные и отрицательные магические эффекты с юнитов в радиусе |cffffffff200|cffced4da и наносит |cffffffff200|cffced4da ед. урона призванным существам.|n|nРасход маны: |cff6090e075|cffced4da. Перезарядка: |cff60b8d05|cffced4da сек.|r",
    },
    # --- Жрец: Внутренний огонь ---
    {
        "id": "A0WJ",
        "name": "|cffe4cfa3Внутренний огонь|r",
        "tip1": "|cffe4cfa3Внутренний огонь|r (|cffffffffW|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет союзника священным огнём на |cffffffff60|cffced4da сек., увеличивая урон от атак на |cffffffff15%|cffced4da, броню на |cffffffff+6|cffced4da ед. и ускоряя регенерацию здоровья на |cffffffff2|cffced4da ед./сек.|n|nРасход маны: |cff6090e075|cffced4da. Перезарядка: |cff60b8d05|cffced4da сек.|r",
        "untip1": "|cffc3dbffПКМ – включить автоприменение.|r",
        "unubertip1": "|cffc3dbffПКМ – отключить автоприменение.|r",
    },
    # --- Заклинатель: Огненная стрела ---
    {
        "id": "A0WK",
        "name": "|cffe4cfa3Огненная стрела|r",
        "tip1": "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком огня, нанося |cffffffff75|cffced4da ед. урона и оглушая её на |cffffffff2|cffced4da сек.|n|nРасход маны: |cff6090e075|cffced4da. Перезарядка: |cff60b8d016|cffced4da сек.|r",
    },
    # --- Заклинатель: Разъедающий огонь ---
    {
        "id": "A0WH",
        "name": "|cffe4cfa3Разъедающий огонь|r",
        "tip1": "|cffe4cfa3Разъедающий огонь|r (|cffffffffW|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окутывает противника разъедающим пламенем на |cffffffff60|cffced4da сек., снижая его урон на |cffffffff10%|cffced4da и броню на |cffffffff5|cffced4da ед.|n|nРасход маны: |cff6090e075|cffced4da. Перезарядка: |cff60b8d05|cffced4da сек.|r",
        "untip1": "|cffc3dbffПКМ – включить автоприменение.|r",
        "unubertip1": "|cffc3dbffПКМ – отключить автоприменение.|r",
    },
    # --- Заклинатель: Проклятие ---
    {
        "id": "A0WL",
        "name": "|cffe4cfa3Проклятие|r",
        "tip1": "|cffe4cfa3Проклятие|r (|cffffffffE|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает вражеского воина на |cffffffff60|cffced4da сек., заставляя его атаки промахиваться с вероятностью |cffffffff33%|cffced4da.|n|nРасход маны: |cff6090e040|cffced4da. Перезарядка: |cff60b8d01|cffced4da сек.|r",
        "untip1": "|cffc3dbffПКМ – включить автоприменение.|r",
        "unubertip1": "|cffc3dbffПКМ – отключить автоприменение.|r",
    },
    # --- Оруженосец: Аура выносливости ---
    {
        "id": "A0WS",
        "name": "|cffe4cfa3Аура выносливости|r",
        "tip1": "|cffe4cfa3Аура выносливости|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает скорость перемещения союзников в радиусе |cffffffff900|cffced4da на |cffffffff10%|cffced4da и скорость их атаки на |cffffffff20%|cffced4da.|r",
    },
    # --- Пехотинец / Капитан: Зачарованные мечи ---
    {
        "id": "A0WT",
        "name": "|cffe4cfa3Зачарованные мечи|r",
        "tip1": "|cffe4cfa3Зачарованные мечи|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Зачарованная сталь клинков пассивно увеличивает урон в ближнем бою на |cffffffff10|cffced4da ед.|r",
    },
    # --- Охотник на троллей: Снайперский выстрел ---
    {
        "id": "A17U",
        "name": "|cffe4cfa3Снайперский выстрел|r",
        "tip1": "|cffe4cfa3Снайперский выстрел|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Меткие выстрелы пассивно наносят повышенный урон по целям со средней бронёй и целям без защиты.|r",
    },
    # --- Осел: Ударная волна ---
    {
        "id": "A0WU",
        "name": "|cffe4cfa3Ударная волна|r",
        "tip1": "|cffe4cfa3Ударная волна|r (|cffffffffQ|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сильный удар по боевым барабанам порождает волну, наносящую |cffffffff50|cffced4da ед. урона наземным и воздушным врагам на своём пути.|n|nРасход маны: |cff6090e0100|cffced4da. Перезарядка: |cff60b8d010|cffced4da сек.|r",
    },
    # --- Паладин (Возмездие): Огненный порошок ---
    {
        "id": "A0XP",
        "name": "|cffe4cfa3Огненный порошок|r",
        "tip1": "|cffe4cfa3Огненный порошок|r (|cffffffffQ|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Распыляет освящённый порошок вокруг паладина, нанося |cffffffff70|cffced4da ед. урона всем противникам в радиусе |cffffffff400|cffced4da.|n|nРасход маны: |cff6090e0100|cffced4da. Перезарядка: |cff60b8d09|cffced4da сек.|r",
    },
    # --- Паладин (Возмездие): Кара Света ---
    {
        "id": "A0XO",
        "name": "|cffe4cfa3Кара Света|r",
        "tip1": "|cffe4cfa3Кара Света|r (|cffffffffE|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает врага карой Света, нанося |cffffffff100|cffced4da ед. урона основной цели и |cffffffff70|cffced4da ед. урона врагам поблизости, а также замедляя их скорость перемещения и атаки на |cffffffff2|cffced4da сек.|n|nРасход маны: |cff6090e0125|cffced4da. Перезарядка: |cff60b8d015|cffced4da сек.|r",
    },
    # --- Паладин (Возмездие): Командирская аура ---
    {
        "id": "A0XN",
        "name": "|cffe4cfa3Командирская аура|r",
        "tip1": "|cffe4cfa3Командирская аура|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от атак союзников в радиусе |cffffffff900|cffced4da на |cffffffff10%|cffced4da.|r",
    },
    # --- Паладин (Защита): Массовая защита ---
    {
        "id": "A0XR",
        "name": "|cffe4cfa3Массовая защита|r",
        "tip1": "|cffe4cfa3Массовая защита|r (|cffffffffW|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Благословляет союзников в радиусе |cffffffff300|cffced4da, увеличивая их броню на |cffffffff+2|cffced4da ед. на |cffffffff30|cffced4da сек.|n|nРасход маны: |cff6090e0160|cffced4da.|r",
    },
    # --- Паладин (Свет): Массовое исцеление ---
    {
        "id": "A0XT",
        "name": "|cffe4cfa3Массовое исцеление|r",
        "tip1": "|cffe4cfa3Массовое исцеление|r (|cffffffffW|r)",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff75|cffced4da ед. здоровья всем союзникам в радиусе |cffffffff300|cffced4da.|n|nРасход маны: |cff6090e0100|cffced4da. Перезарядка: |cff60b8d010|cffced4da сек.|r",
    },
    # --- Паладин (Свет): Регенерация ---
    {
        "id": "A0XY",
        "name": "|cffe4cfa3Регенерация|r",
        "tip1": "|cffe4cfa3Регенерация|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Священная аура пассивно восстанавливает союзникам в радиусе |cffffffff500|cffced4da по |cffffffff2%|cffced4da здоровья.|r",
    },
    # --- Сторожевая башня: Мультишот ---
    {
        "id": "A0ZM",
        "name": "|cffe4cfa3Мультишот|r",
        "tip1": "|cffe4cfa3Мультишот|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Башня выпускает стрелы сразу в |cffffffff6|cffced4da дополнительных целей поблизости, нанося по |cffffffff30|cffced4da ед. урона каждой.|r",
    },
    # --- Магический котел: Аура отравления (4 уровня / 4 объекта) ---
    {
        "id": "A0ZR",
        "name": "|cffe4cfa3Аура отравления|r",
        "tip1": "|cffe4cfa3Аура отравления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ядовитые испарения котла наносят всем противникам в радиусе |cffffffff900|cffced4da урон в размере |cffffffff2%|cffced4da от их максимального запаса здоровья.|r",
    },
    {
        "id": "A1O6",
        "name": "|cffe4cfa3Аура отравления|r",
        "tip1": "|cffe4cfa3Аура отравления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ядовитые испарения котла наносят всем противникам в радиусе |cffffffff900|cffced4da урон в размере |cffffffff2%|cffced4da от их максимального запаса здоровья.|r",
    },
    {
        "id": "A1O7",
        "name": "|cffe4cfa3Аура отравления|r",
        "tip1": "|cffe4cfa3Аура отравления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ядовитые испарения котла наносят всем противникам в радиусе |cffffffff900|cffced4da урон в размере |cffffffff2%|cffced4da от их максимального запаса здоровья.|r",
    },
    {
        "id": "A1O8",
        "name": "|cffe4cfa3Аура отравления|r",
        "tip1": "|cffe4cfa3Аура отравления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ядовитые испарения котла наносят всем противникам в радиусе |cffffffff900|cffced4da урон в размере |cffffffff2%|cffced4da от их максимального запаса здоровья.|r",
    },
    # --- Магический котел: Аура исцеления (4 уровня / 4 объекта) ---
    {
        "id": "A0ZS",
        "name": "|cffe4cfa3Аура исцеления|r",
        "tip1": "|cffe4cfa3Аура исцеления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Целебные пары котла восстанавливают здоровье находящимся поблизости союзникам в радиусе |cffffffff450|cffced4da.|r",
    },
    {
        "id": "A0ZT",
        "name": "|cffe4cfa3Аура исцеления|r",
        "tip1": "|cffe4cfa3Аура исцеления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Целебные пары котла восстанавливают здоровье находящимся поблизости союзникам в радиусе |cffffffff450|cffced4da.|r",
    },
    {
        "id": "A1O3",
        "name": "|cffe4cfa3Аура исцеления|r",
        "tip1": "|cffe4cfa3Аура исцеления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Целебные пары котла восстанавливают здоровье находящимся поблизости союзникам в радиусе |cffffffff450|cffced4da.|r",
    },
    {
        "id": "A1O4",
        "name": "|cffe4cfa3Аура исцеления|r",
        "tip1": "|cffe4cfa3Аура исцеления|r",
        "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Целебные пары котла восстанавливают здоровье находящимся поблизости союзникам в радиусе |cffffffff450|cffced4da.|r",
    },
]

# 2. Buffs
BUFFS = [
    {
        "id": "B08B",
        "editorname": "|cffe4cfa3Сторожевая башня|r",
        "bufftip": "|cffe4cfa3Сторожевая башня|r",
        "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Временная башня, возведённая генералом для контроля территории и обстрела врагов.|r"
    },
    {
        "id": "B06R",
        "editorname": "|cffe4cfa3Аура защиты|r",
        "bufftip": "|cffe4cfa3Аура защиты|r",
        "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Броня увеличена на |cffffffff+3|cffced4da ед. под воздействием ауры защиты.|r"
    },
    {
        "id": "B01B",
        "editorname": "|cffe4cfa3Массовая защита|r",
        "bufftip": "|cffe4cfa3Массовая защита|r",
        "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Броня увеличена на |cffffffff+2|cffced4da ед. под воздействием благословения паладина.|r"
    },
    {
        "id": "B085",
        "editorname": "|cffe4cfa3Жгучая кровь|r",
        "bufftip": "|cffe4cfa3Жгучая кровь|r",
        "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Регенерация здоровья ускорена под воздействием боевого ража генерала.|r"
    },
    {
        "id": "B04X",
        "editorname": "|cffe4cfa3Всплеск ярости|r",
        "bufftip": "|cffe4cfa3Всплеск ярости|r",
        "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость боя и входящий урон увеличены под воздействием всплеска ярости.|r"
    }
]

def main():
    operations = []
    registry = {
        "race": "Стромгард",
        "category": "Способности и эффекты",
        "batch": "02_unit_summon_abilities_and_buffs",
        "abilities_count": len(UNIT_ABILITIES),
        "buffs_count": len(BUFFS),
        "abilities": {},
        "buffs": {}
    }

    # Abilities
    for ab in UNIT_ABILITIES:
        ab_id = ab["id"]
        ab_entry = {"name": ab["name"]}
        for field in ["name", "tip1", "ubertip1", "tip2", "ubertip2", "untip1", "unubertip1"]:
            if field in ab:
                val = ab[field]
                ab_entry[field] = val
                operations.append({
                    "type": "ability",
                    "id": ab_id,
                    "field": field,
                    "value": val
                })
        registry["abilities"][ab_id] = ab_entry

    # Buffs
    for bf in BUFFS:
        bf_id = bf["id"]
        bf_entry = {}
        for field in ["editorname", "bufftip", "buffubertip"]:
            if field in bf:
                val = bf[field]
                bf_entry[field] = val
                operations.append({
                    "type": "buff",
                    "id": bf_id,
                    "field": field,
                    "value": val
                })
        registry["buffs"][bf_id] = bf_entry

    plan_file = ROOT / "docs/ui_text/stromgard_unit_abilities_plan.json"
    registry_file = ROOT / "docs/ui_text/stromgard_unit_abilities.json"

    with open(plan_file, "w", encoding="utf-8") as f:
        json.dump({"operations": operations}, f, ensure_ascii=False, indent=2)

    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(operations)} operations across {len(UNIT_ABILITIES)} abilities and {len(BUFFS)} buffs.")
    print(f"Saved plan to {plan_file}")
    print(f"Saved registry to {registry_file}")

if __name__ == "__main__":
    main()
