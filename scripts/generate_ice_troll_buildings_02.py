import hashlib
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from wc3_object_tools import cli, require
from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent
stage = ROOT / "map.w3x"
wts = load_wts_strings(stage / "war3map.wts")

bld_ids = ["h0HO", "o06H", "o06I", "o06J", "o06K"]
unit_ids = ["o05B", "n062", "n061", "h0D4", "h0HN", "h0HK"]
upg_ids = ["R0AI", "R0AJ", "R0AD"]

bld_fields = ["name", "tip", "ubertip", "hotkey", "trains", "researches", "upgrade", "abillist", "sellunits", "sellitems", "fmade", "isbldg", "reqs", "reqslevels"]
unit_fields = ["name", "tip", "ubertip", "hotkey", "abillist", "trains", "researches", "reqs", "reqslevels"]
upg_fields = ["name1", "tip1", "name2", "tip2", "name3", "tip3", "ubertip1", "ubertip2", "ubertip3"]

objects_before = {}
for hd in (False, True):
    key = "HD" if hd else "SD"
    hd_flag = ["--hd"] if hd else []
    bld_data = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(bld_ids), "--fields", ",".join(bld_fields)] + hd_flag, stage))
    unit_data = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(unit_ids), "--fields", ",".join(unit_fields)] + hd_flag, stage))
    upg_data = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(upg_ids), "--fields", ",".join(upg_fields)] + hd_flag, stage))
    objects_before[key] = {
        "buildings": bld_data["objects"],
        "units": unit_data["objects"],
        "upgrades": upg_data["objects"]
    }

operations = [
    # h0HO (Верфь)
    {
        "type": "unit",
        "id": "h0HO",
        "field": "name",
        "value": "|cffe4cfa3Верфь|r"
    },
    {
        "type": "unit",
        "id": "h0HO",
        "field": "tip",
        "value": "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    },
    {
        "type": "unit",
        "id": "h0HO",
        "field": "ubertip",
        "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Строит корабли и исследует общие улучшения флота.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da.|n- |cffa9c7deЛегкий корабль Орды|cffced4da.|n- |cffa9c7deТяжелый корабль Орды|cffced4da.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбстрел|cffced4da.|n- |cffa9c7deДополнительные паруса|cffced4da.|n- |cffa9c7deПочинка|cffced4da.|n- |cffa9c7deОрудия флота|cffced4da.|n- |cffa9c7deУкреплённый корпус|cffced4da.|n|n|cffa9c7deЗона ремонта|cffced4da восстанавливает |cffc8e0872,5|cffced4da здоровья/сек. союзным наземным механическим войскам в радиусе |cffffffff550|cffced4da.|r",
        "marker": "ЗДАНИЕ:"
    },

    # o06H (Алтарь Лоа)
    {
        "type": "unit",
        "id": "o06H",
        "field": "name",
        "value": "|cffe4cfa3Алтарь Лоа|r"
    },
    {
        "type": "unit",
        "id": "o06H",
        "field": "tip",
        "value": "|cffe4cfa3Алтарь Лоа|r (|cffffffffX|r)"
    },
    {
        "type": "unit",
        "id": "o06H",
        "field": "ubertip",
        "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище для призыва великих Лоа или поглощения их сил. Обеспечивает |cffffffff3|cffced4da ед. пищи.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАкали|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n- |cffa9c7deМам'тот|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n- |cffa9c7deРунок|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПоглощение Акали|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Мам'Тота|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Рунока|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n|n|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deАлтарь Рунока|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n- |cffa9c7deАлтарь Акали|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n- |cffa9c7deАлтарь Мам'Тота|cffced4da (требуется: выбран путь «Ритуал поклонения»).|n|nШипастые укрепления наносят ответный урон атакующим в ближнем бою.|r",
        "marker": "ЗДАНИЕ:"
    },

    # o06I (Алтарь Рунока)
    {
        "type": "unit",
        "id": "o06I",
        "field": "name",
        "value": "|cffe4cfa3Алтарь Рунока|r"
    },
    {
        "type": "unit",
        "id": "o06I",
        "field": "tip",
        "value": "|cffe4cfa3Алтарь Рунока|r (|cffffffffA|r)"
    },
    {
        "type": "unit",
        "id": "o06I",
        "field": "ubertip",
        "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Специализированное святилище Лоа Рунока. Обеспечивает |cffffffff3|cffced4da ед. пищи и открывает способности Рунока: «Ярость» и «Аура Рунока».|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРунок|cffced4da.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПоглощение Акали|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Мам'Тота|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Рунока|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n|nШипастые укрепления наносят ответный урон атакующим в ближнем бою.|r",
        "marker": "ЗДАНИЕ:"
    },

    # o06J (Алтарь Акали)
    {
        "type": "unit",
        "id": "o06J",
        "field": "name",
        "value": "|cffe4cfa3Алтарь Акали|r"
    },
    {
        "type": "unit",
        "id": "o06J",
        "field": "tip",
        "value": "|cffe4cfa3Алтарь Акали|r (|cffffffffS|r)"
    },
    {
        "type": "unit",
        "id": "o06J",
        "field": "ubertip",
        "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Специализированное святилище Лоа Акали. Обеспечивает |cffffffff3|cffced4da ед. пищи и открывает способности Акали: «Аура Акали» и «Раздвоенная молния».|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАкали|cffced4da.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПоглощение Акали|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Мам'Тота|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Рунока|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n|nШипастые укрепления наносят ответный урон атакующим в ближнем бою.|r",
        "marker": "ЗДАНИЕ:"
    },

    # o06K (Алтарь Мам'Тота)
    {
        "type": "unit",
        "id": "o06K",
        "field": "name",
        "value": "|cffe4cfa3Алтарь Мам'Тота|r"
    },
    {
        "type": "unit",
        "id": "o06K",
        "field": "tip",
        "value": "|cffe4cfa3Алтарь Мам'Тота|r (|cffffffffD|r)"
    },
    {
        "type": "unit",
        "id": "o06K",
        "field": "ubertip",
        "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Специализированное святилище Лоа Мам'Тота. Обеспечивает |cffffffff3|cffced4da ед. пищи и открывает способности Мам'Тота: «Реинкарнация» и «Аура Мам'Тота».|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМам'тот|cffced4da.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПоглощение Акали|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Мам'Тота|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n- |cffa9c7deПоглощение Рунока|cffced4da (требуется: выбран путь «Чрезвычайные меры»).|n|nШипастые укрепления наносят ответный урон атакующим в ближнем бою.|r",
        "marker": "ЗДАНИЕ:"
    },

    # Units
    {"type": "unit", "id": "o05B", "field": "name", "value": "|cffe4cfa3Акали|r"},
    {"type": "unit", "id": "o05B", "field": "tip", "value": "|cffe4cfa3Акали|r (|cffffffffW|r)"},

    {"type": "unit", "id": "n062", "field": "name", "value": "|cffe4cfa3Мам'тот|r"},
    {"type": "unit", "id": "n062", "field": "tip", "value": "|cffe4cfa3Мам'тот|r (|cffffffffE|r)"},

    {"type": "unit", "id": "n061", "field": "name", "value": "|cffe4cfa3Рунок|r"},
    {"type": "unit", "id": "n061", "field": "tip", "value": "|cffe4cfa3Рунок|r (|cffffffffQ|r)"},

    {"type": "unit", "id": "h0D4", "field": "name", "value": "|cffe4cfa3Транспорт|r"},
    {"type": "unit", "id": "h0D4", "field": "tip", "value": "|cffe4cfa3Транспорт|r (|cffffffffQ|r)"},

    {"type": "unit", "id": "h0HN", "field": "name", "value": "|cffe4cfa3Легкий корабль Орды|r"},
    {"type": "unit", "id": "h0HN", "field": "tip", "value": "|cffe4cfa3Легкий корабль Орды|r (|cffffffffW|r)"},

    {"type": "unit", "id": "h0HK", "field": "name", "value": "|cffe4cfa3Тяжелый корабль Орды|r"},
    {"type": "unit", "id": "h0HK", "field": "tip", "value": "|cffe4cfa3Тяжелый корабль Орды|r (|cffffffffE|r)"},

    # Researches (R0AI, R0AJ, R0AD levels 1..3)
    {"type": "upgrade", "id": "R0AI", "field": "name1", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff1|r"},
    {"type": "upgrade", "id": "R0AI", "field": "tip1", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff1|r (|cffffffffW|r)"},
    {"type": "upgrade", "id": "R0AI", "field": "name2", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff2|r"},
    {"type": "upgrade", "id": "R0AI", "field": "tip2", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff2|r (|cffffffffW|r)"},
    {"type": "upgrade", "id": "R0AI", "field": "name3", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff3|r"},
    {"type": "upgrade", "id": "R0AI", "field": "tip3", "value": "|cffe4cfa3Поглощение Акали|r — уровень |cffffffff3|r (|cffffffffW|r)"},

    {"type": "upgrade", "id": "R0AJ", "field": "name1", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff1|r"},
    {"type": "upgrade", "id": "R0AJ", "field": "tip1", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff1|r (|cffffffffE|r)"},
    {"type": "upgrade", "id": "R0AJ", "field": "name2", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff2|r"},
    {"type": "upgrade", "id": "R0AJ", "field": "tip2", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff2|r (|cffffffffE|r)"},
    {"type": "upgrade", "id": "R0AJ", "field": "name3", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff3|r"},
    {"type": "upgrade", "id": "R0AJ", "field": "tip3", "value": "|cffe4cfa3Поглощение Мам'Тота|r — уровень |cffffffff3|r (|cffffffffE|r)"},

    {"type": "upgrade", "id": "R0AD", "field": "name1", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff1|r"},
    {"type": "upgrade", "id": "R0AD", "field": "tip1", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff1|r (|cffffffffQ|r)"},
    {"type": "upgrade", "id": "R0AD", "field": "name2", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff2|r"},
    {"type": "upgrade", "id": "R0AD", "field": "tip2", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff2|r (|cffffffffQ|r)"},
    {"type": "upgrade", "id": "R0AD", "field": "name3", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff3|r"},
    {"type": "upgrade", "id": "R0AD", "field": "tip3", "value": "|cffe4cfa3Поглощение Рунока|r — уровень |cffffffff3|r (|cffffffffQ|r)"},
]

input_files = [
    "map.w3x/war3map.wts",
    "map.w3x/war3map.w3u",
    "map.w3x/war3mapSkin.w3u",
    "map.w3x/war3map.w3q",
    "map.w3x/war3mapSkin.w3q",
    "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/IceTrolls.lua"
]
input_sha256 = {fn: hashlib.sha256((ROOT / fn).read_bytes()).hexdigest() for fn in input_files}

registry = {
    "scope": "Ледяные тролли: 5 оставшихся зданий (Верфь h0HO, Алтарь Лоа o06H и его ступени o06J/o06K/o06I) и прямые зависимости их меню",
    "in_game_checked": False,
    "variants": ["SD", "HD"],
    "building_ids": bld_ids,
    "objects_before": objects_before,
    "operations_count": len(operations),
    "input_sha256": input_sha256,
    "evidence": {
        "menus": "Все списки обучения, улучшений и исследований согласованы с object data и Lua (Trig_ServeLoa, Trig_KillLoa)",
        "altar_branches": "Алтарь Лоа o06H разветвляется на три специализированных алтаря o06I (Рунок, Q/A), o06J (Акали, W/S), o06K (Мам'Тот, E/D)",
        "abilities_unlocked": "Улучшение святилищ разблокирует areq способности Лоа: A1FY/A1P9 для Рунока, A1PA/A1PC для Акали, A1FX/S00F для Мам'Тота",
        "shipyard": "Верфь h0HO обучает h0D4, h0HN, h0HK и исследует 5 общих улучшений флота; имеет ауру Ремонта A15N",
        "preservation": "Нетекстовые поля и посторонние записи побайтово сохраняются patch_blob"
    },
    "remaining": [
        "Юниты ледяных троллей (полные карточки способностей и характеристик)",
        "Герои ледяных троллей (полные карточки, имена и способности)",
        "Способности и эффекты ледяных троллей",
        "Исследования ледяных троллей (полные карточки и описания эффектов)",
        "Игровые проверки в Warcraft III выполняет пользователь"
    ]
}

plan = {"operations": operations}

(ROOT / "docs/ui_text/ice_troll_buildings_02.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "docs/ui_text/ice_troll_buildings_02_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"Generated registry and plan with {len(operations)} operations successfully.")
