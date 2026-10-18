# -*- coding: utf-8 -*-
"""Generate complete plan and registry for Stromgard hero abilities."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HERO_ABILITIES = [
    # --- Генерал (H0HB) ---
    {
        "id": "A0XW",
        "name": "|cffe4cfa3Ударная волна|r",
        "hotkey": "Q",
        "levels": 4,
        "is_passive": False,
        "desc": "Выпускает силовую волну энергии, наносящую урон наземным войскам на прямой линии.",
        "levels_data": [
            {"damage": "125", "mana": "90"},
            {"damage": "175", "mana": "90"},
            {"damage": "220", "mana": "90"},
            {"damage": "300", "mana": "100"}
        ],
        "format_level_ub": lambda d: f"Выпускает силовую волну энергии, наносящую |cffffffff{d['damage']}|cffced4da ед. урона наземным войскам на линии.",
        "format_research_ub": lambda d: f"Наносит |cffffffff{d['damage']}|cffced4da ед. урона."
    },
    {
        "id": "A0XM",
        "name": "|cffe4cfa3Сторожевая башня|r",
        "hotkey": "W",
        "levels": 4,
        "is_passive": False,
        "desc": "Возводит временную сторожевую башню на 30 сек., атакующую всех врагов в радиусе действия.",
        "levels_data": [
            {"hp": "500", "dmg": "12", "cd": "60"},
            {"hp": "650", "dmg": "18", "cd": "50"},
            {"hp": "800", "dmg": "24", "cd": "40"},
            {"hp": "950", "dmg": "30", "cd": "30"}
        ],
        "format_level_ub": lambda d: f"Возводит сторожевую башню с запасом здоровья |cffffffff{d['hp']}|cffced4da и уроном |cffffffff{d['dmg']}|cffced4da на |cffffffff30|cffced4da сек. Перезарядка: |cff60b8d0{d['cd']}|cffced4da сек.",
        "format_research_ub": lambda d: f"Башня с |cffffffff{d['hp']}|cffced4da ед. здоровья и |cffffffff{d['dmg']}|cffced4da ед. урона, перезарядка |cff60b8d0{d['cd']}|cffced4da сек."
    },
    {
        "id": "A0Y8",
        "name": "|cffe4cfa3Жгучая кровь|r",
        "hotkey": "E",
        "levels": 4,
        "is_passive": True,
        "desc": "Особая закалка полководца ускоряет регенерацию его здоровья, позволяя дольше сражаться на передовой.",
        "levels_data": [
            {"regen": "6"},
            {"regen": "8"},
            {"regen": "10"},
            {"regen": "12"}
        ],
        "format_level_ub": lambda d: f"Пассивно увеличивает скорость восстановления здоровья героя на |cffffffff+{d['regen']}|cffced4da ед. в секунду.",
        "format_research_ub": lambda d: f"Восстановление здоровья |cffffffff+{d['regen']}|cffced4da ед./сек."
    },
    {
        "id": "A0XZ",
        "name": "|cffe4cfa3Генеральская забава|r",
        "hotkey": "R",
        "levels": 2,
        "is_passive": False,
        "desc": "Генерал произносит воодушевляющую речь, делая союзные войска в области неуязвимыми на 15 сек.",
        "levels_data": [
            {"radius": "800", "cd": "90"},
            {"radius": "1000", "cd": "70"}
        ],
        "format_level_ub": lambda d: f"Дарует союзным войскам в радиусе |cffffffff{d['radius']}|cffced4da полную неуязвимость на |cffffffff15|cffced4da сек. Перезарядка: |cff60b8d0{d['cd']}|cffced4da сек.",
        "format_research_ub": lambda d: f"Радиус |cffffffff{d['radius']}|cffced4da, перезарядка |cff60b8d0{d['cd']}|cffced4da сек."
    },

    # --- Казначей (H0HL) ---
    {
        "id": "A0ZO",
        "name": "|cffe4cfa3Золотая ручка|r",
        "hotkey": "Q",
        "levels": 4,
        "is_passive": False,
        "desc": "Мгновенно уничтожает вражеского воина, обращая его стоимость в чистое золото. Не действует на героев.",
        "levels_data": [
            {"mult": "2.5", "cd": "120", "mana": "150"},
            {"mult": "3.0", "cd": "100", "mana": "200"},
            {"mult": "5.0", "cd": "80", "mana": "250"},
            {"mult": "7.0", "cd": "60", "mana": "300"}
        ],
        "format_level_ub": lambda d: f"Мгновенно уничтожает цель, принося золото в размере |cffffffff{d['mult']}x|cffced4da от её стоимости. Расход маны: |cff6090e0{d['mana']}|cffced4da, перезарядка: |cff60b8d0{d['cd']}|cffced4da сек.",
        "format_research_ub": lambda d: f"Золото |cffffffff{d['mult']}x|cffced4da стоимости цели, перезарядка |cff60b8d0{d['cd']}|cffced4da сек."
    },
    {
        "id": "A0ZP",
        "name": "|cffe4cfa3Налоги|r",
        "hotkey": "W",
        "levels": 4,
        "is_passive": True,
        "desc": "Каждая атака казначея изымает золото у поражённого противника и передаёт его в вашу казну.",
        "levels_data": [
            {"gold": "0.7"},
            {"gold": "0.9"},
            {"gold": "1.1"},
            {"gold": "1.3"}
        ],
        "format_level_ub": lambda d: f"Пассивно изымает |cffffffff{d['gold']}|cffced4da ед. золота при каждой атаке по вражескому юниту.",
        "format_research_ub": lambda d: f"Изымает |cffffffff{d['gold']}|cffced4da ед. золота за атаку."
    },
    {
        "id": "A0XV",
        "name": "|cffe4cfa3Казначейский талант|r",
        "hotkey": "E",
        "levels": 4,
        "is_passive": True,
        "desc": "Мастерство управления финансами увеличивает регулярный золотой доход государства каждые 25 сек.",
        "levels_data": [
            {"income": "200"},
            {"income": "300"},
            {"income": "400"},
            {"income": "500"}
        ],
        "format_level_ub": lambda d: f"Пассивно увеличивает периодический доход казны на |cffffffff+{d['income']}|cffced4da золота каждые |cffffffff25|cffced4da сек.",
        "format_research_ub": lambda d: f"Доход казны |cffffffff+{d['income']}|cffced4da золота каждые 25 сек."
    },
    {
        "id": "A0ZN",
        "name": "|cffe4cfa3Прибавка к золоту|r",
        "hotkey": "R",
        "levels": 2,
        "is_passive": False,
        "desc": "Казначей достаёт накопленные средства и единовременно пополняет государственную казну.",
        "levels_data": [
            {"gold": "1500"},
            {"gold": "3000"}
        ],
        "format_level_ub": lambda d: f"Мгновенно добавляет в государственную казну |cffffffff{d['gold']}|cffced4da ед. золота. Перезарядка: |cff60b8d060|cffced4da сек.",
        "format_research_ub": lambda d: f"Единовременно даёт |cffffffff{d['gold']}|cffced4da золота."
    },

    # --- Верховный маг (H0HA) ---
    {
        "id": "A0XK",
        "name": "|cffe4cfa3Огненная стрела|r",
        "hotkey": "Q",
        "levels": 4,
        "is_passive": False,
        "desc": "Выпускает сгусток концентрированного пламени, наносящий урон и оглушающий противника.",
        "levels_data": [
            {"dmg": "75", "stun": "2"},
            {"dmg": "150", "stun": "3"},
            {"dmg": "270", "stun": "4"},
            {"dmg": "350", "stun": "5"}
        ],
        "format_level_ub": lambda d: f"Наносит цели |cffffffff{d['dmg']}|cffced4da ед. урона и оглушает её на |cffffffff{d['stun']}|cffced4da сек. (героев на |cffffffff2|cffced4da сек.). Расход маны: |cff6090e075|cffced4da.",
        "format_research_ub": lambda d: f"Наносит |cffffffff{d['dmg']}|cffced4da ед. урона, оглушение на |cffffffff{d['stun']}|cffced4da сек."
    },
    {
        "id": "A0ZQ",
        "name": "|cffe4cfa3Магический котел|r",
        "hotkey": "W",
        "levels": 4,
        "is_passive": False,
        "desc": "Призывает неподвижный невосприимчивый к магии котёл на 20 сек., исцеляющий союзников и обжигающий врагов.",
        "levels_data": [
            {"heal": "5", "burn": "4", "cd": "80"},
            {"heal": "7", "burn": "6", "cd": "70"},
            {"heal": "9", "burn": "8", "cd": "50"},
            {"heal": "11", "burn": "10", "cd": "40"}
        ],
        "format_level_ub": lambda d: f"Призывает котёл на |cffffffff20|cffced4da сек.: восстанавливает союзникам |cffffffff{d['heal']}%|cffced4da здоровья в сек. и наносит врагам |cffffffff{d['burn']}%|cffced4da урона. Перезарядка: |cff60b8d0{d['cd']}|cffced4da сек.",
        "format_research_ub": lambda d: f"Исцеление |cffffffff{d['heal']}%|cffced4da, урон врагам |cffffffff{d['burn']}%|cffced4da, перезарядка |cff60b8d0{d['cd']}|cffced4da сек."
    },
    {
        "id": "A0Y6",
        "name": "|cffe4cfa3Аура гениальности|r",
        "hotkey": "E",
        "levels": 4,
        "is_passive": True,
        "desc": "Магическое присутствие чародея ускоряет восполнение маны у ближайших союзных войск.",
        "levels_data": [
            {"mana": "0.75", "desc": "незначительный бонус"},
            {"mana": "1.50", "desc": "средний бонус"},
            {"mana": "2.25", "desc": "значительный бонус"},
            {"mana": "3.00", "desc": "большой бонус"}
        ],
        "format_level_ub": lambda d: f"Пассивно увеличивает скорость восстановления маны у союзников поблизости на |cffffffff+{d['mana']}|cffced4da ед. в секунду.",
        "format_research_ub": lambda d: f"Восстановление маны |cffffffff+{d['mana']}|cffced4da ед./сек. ({d['desc']})."
    },
    {
        "id": "A0Y7",
        "name": "|cffe4cfa3Огненный ливень|r",
        "hotkey": "R",
        "levels": 2,
        "is_passive": False,
        "desc": "Обрушивает на указанную область сокрушительный дождь огненных метеоров, наносящих урон при падении и поджигающих землю.",
        "levels_data": [
            {"dmg": "30", "dot": "12", "waves": "9"},
            {"dmg": "40", "dot": "17", "waves": "12"}
        ],
        "format_level_ub": lambda d: f"Вызывает |cffffffff{d['waves']}|cffced4da волн огня: каждая наносит |cffffffff{d['dmg']}|cffced4da ед. урона и |cffffffff{d['dot']}|cffced4da ед. урона от горения. Расход маны: |cff6090e0125|cffced4da.",
        "format_research_ub": lambda d: f"|cffffffff{d['waves']}|cffced4da волн по |cffffffff{d['dmg']}|cffced4da ед. урона и |cffffffff{d['dot']}|cffced4da ед. горения."
    },

    # --- Данат Троллебой (H0L4) ---
    {
        "id": "A1LH",
        "name": "|cffe4cfa3Аура ветерана|r",
        "hotkey": None,
        "levels": 1,
        "is_passive": True,
        "is_innate": True,
        "desc": "Врождённый полководческий опыт вдохновляет бойцов, повышая урон всех союзных войск поблизости.",
        "levels_data": [
            {"bonus": "10"}
        ],
        "format_level_ub": lambda d: f"Врождённая аура: увеличивает силу атаки находящихся рядом союзников на |cffffffff+{d['bonus']}%|cffced4da."
    },
    {
        "id": "A17V",
        "name": "|cffe4cfa3Всплеск ярости|r",
        "hotkey": "Q",
        "levels": 4,
        "is_passive": False,
        "desc": "Впадает в боевое безумие, резко увеличивая скорость атаки ценой повышенного входящего урона на 12 сек.",
        "levels_data": [
            {"vuln": "50"},
            {"vuln": "45"},
            {"vuln": "40"},
            {"vuln": "35"}
        ],
        "format_level_ub": lambda d: f"Повышает скорость боя на |cffffffff+400%|cffced4da, но увеличивает получаемый урон на |cffffffff{d['vuln']}%|cffced4da на |cffffffff12|cffced4da сек. Перезарядка: |cff60b8d030|cffced4da сек.",
        "format_research_ub": lambda d: f"+400% скорости боя, входящий урон |cffffffff+{d['vuln']}%|cffced4da."
    },
    {
        "id": "A17X",
        "name": "|cffe4cfa3Боевой клич|r",
        "hotkey": "W",
        "levels": 4,
        "is_passive": False,
        "desc": "Издаёт громогласный клич, временно увеличивающий силу атаки окружающих союзных войск на 35 сек.",
        "levels_data": [
            {"bonus": "15", "mana": "110"},
            {"bonus": "20", "mana": "120"},
            {"bonus": "25", "mana": "130"},
            {"bonus": "30", "mana": "140"}
        ],
        "format_level_ub": lambda d: f"Увеличивает урон союзных войск в радиусе |cffffffff500|cffced4da на |cffffffff+{d['bonus']}%|cffced4da на |cffffffff35|cffced4da сек. Расход маны: |cff6090e0{d['mana']}|cffced4da.",
        "format_research_ub": lambda d: f"Бонус к урону союзников |cffffffff+{d['bonus']}%|cffced4da."
    },
    {
        "id": "A17W",
        "name": "|cffe4cfa3Ярость Трол'калар|r",
        "hotkey": "E",
        "levels": 4,
        "is_passive": True,
        "desc": "Легендарный клинок Трол'калар даёт шанс нанести сокрушительный удар в ближнем бою.",
        "levels_data": [
            {"mult": "2.0"},
            {"mult": "2.5"},
            {"mult": "3.0"},
            {"mult": "3.5"}
        ],
        "format_level_ub": lambda d: f"Даёт |cffffffff20%|cffced4da шанс нанести удар с множителем урона |cffffffff{d['mult']}x|cffced4da при атаке.",
        "format_research_ub": lambda d: f"Множитель урона |cffffffff{d['mult']}x|cffced4da (шанс 20%)."
    },
    {
        "id": "A17S",
        "name": "|cffe4cfa3Аватар|r",
        "hotkey": "R",
        "levels": 2,
        "is_passive": False,
        "desc": "Данат преисполняется титанической мощи, получая броню, здоровье, урон и невосприимчивость к магии на 60 сек.",
        "levels_data": [
            {"armor": "5", "hp": "500", "dmg": "15"},
            {"armor": "7", "hp": "1000", "dmg": "25"}
        ],
        "format_level_ub": lambda d: f"Дарует невосприимчивость к магии, бонус |cffffffff+{d['armor']}|cffced4da к броне, |cffffffff+{d['hp']}|cffced4da к здоровью и |cffffffff+{d['dmg']}|cffced4da к урону на |cffffffff60|cffced4da сек. Расход маны: |cff6090e0150|cffced4da, перезарядка: |cff60b8d0180|cffced4da сек.",
        "format_research_ub": lambda d: f"+{d['armor']} к броне, +{d['hp']} к здоровью, +{d['dmg']} к урону."
    }
]

def main():
    folder = ROOT / "docs" / "ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    operations = []
    registry_abils = []

    for a in HERO_ABILITIES:
        aid = a["id"]
        name = a["name"]
        hotkey = a["hotkey"]
        levels = a["levels"]
        is_passive = a.get("is_passive", False)
        is_innate = a.get("is_innate", False)

        # Name
        operations.append({
            "type": "ability",
            "id": aid,
            "field": "name",
            "value": name
        })

        # Research tip and ubertip (if not innate)
        if not is_innate:
            rtip = f"{name} (|cffffffff{hotkey}|r)" if hotkey else name
            lines = [f"- |cffffffff{lvl}|cffced4da: {a['format_research_ub'](a['levels_data'][lvl-1])}" for lvl in range(1, levels + 1)]
            rubertip = (
                f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da {a['desc']}|n|n"
                f"|cffa6afb8Уровни:|cffced4da|n" + "|n".join(lines) + "|r"
            )
            operations.append({
                "type": "ability",
                "id": aid,
                "field": "researchtip",
                "value": rtip
            })
            operations.append({
                "type": "ability",
                "id": aid,
                "field": "researchubertip",
                "value": rubertip
            })

        # Active levels
        for lvl in range(1, levels + 1):
            tip = f"{name} (|cffffffff{hotkey}|r)" if (hotkey and not is_passive) else name
            level_ub = a["format_level_ub"](a["levels_data"][lvl - 1])
            if levels > 1:
                ubertip = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da {level_ub}|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/{levels}|cffced4da.|r"
            else:
                ubertip = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da {level_ub}|r"

            operations.append({
                "type": "ability",
                "id": aid,
                "field": f"tip{lvl}",
                "value": tip
            })
            operations.append({
                "type": "ability",
                "id": aid,
                "field": f"ubertip{lvl}",
                "value": ubertip
            })

        registry_abils.append({
            "id": aid,
            "name": name,
            "hotkey": hotkey,
            "levels": levels,
            "is_passive": is_passive,
            "is_innate": is_innate
        })

    plan = {"operations": operations}
    registry = {
        "race": "Стромгард",
        "category": "Способности и эффекты: способности героев (партия 1)",
        "scope": "Все 17 способностей героев Стромгарда",
        "hero_abilities": registry_abils,
        "total_operations": len(operations),
        "in_game_checked": False
    }

    (folder / "stromgard_hero_abilities_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "stromgard_hero_abilities.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(operations)} operations across {len(HERO_ABILITIES)} hero abilities.")

if __name__ == "__main__":
    main()
