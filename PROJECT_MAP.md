# 23 Race Legion — Карта проекта

Warcraft III: Reforged — кастомная карта Altered Melee с 30+ фракциями, поддержкой до 24 игроков.

| | |
|---|---|
| **Версия** | `23_race_1_6_504` |
| **Репозиторий** | https://github.com/VinerX-Games/23-Race-Legion |
| **Язык** | Русский (скрипты, комментарии, строки) |
| **Скрипт** | Lua (сконвертирован из vJASS), ~65 000 строк |
| **Файлов** | ~5 000+ |
| **Статус** | Lua-конвертация, активно дорабатывается |
| **Сборка** | `python build_map_lua.py` — собирает `war3map.lua` из `_lua/monolith_split/` |
| **Тестирование** | `HiveWE_cli run-map --map map.w3x --warcraft "F:/Games/Warcraft III"` |

---

## 1. Структура корня

```
23-Race-Legion/
├── .git/                   # Git-репозиторий
├── .gitattributes          # LF-нормализация
├── version.txt             # "23_race_1_6_504"
├── PROJECT_MAP.md          # Этот файл
└── map.w3x/                # РАСПАКОВАННАЯ КАРТА (основное содержимое)
```

Карта распакована из `.w3x` для версионного контроля. Это не исходники TypeScript/Lua — это прямой экспорт World Editor.

---

## 2. Ключевые файлы карты

### 2.1 Объектные данные (World Editor)

| Файл | Назначение |
|---|---|
| `war3map.w3a` | Кастомные способности |
| `war3map.w3b` | Кастомные баффы/эффекты |
| `war3map.w3h` | Данные героев |
| `war3map.w3u` | Кастомные юниты |
| `war3map.w3t` | Кастомные предметы |
| `war3map.w3d` | Разрушаемые объекты |
| `war3map.w3q` | Апгрейды/исследования |
| `war3map.w3i` | Инфо карты / загрузочный экран |
| `war3map.w3c` | Кампания |
| `war3map.w3s` | Звуки |

### 2.2 Данные ландшафта

| Файл | Назначение |
|---|---|
| `war3map.doo` | Декорации (doodads) |
| `war3map.w3e` | Окружение/террейн |
| `war3map.wpm` | Pathing map |
| `war3map.mmp` | Миникарта |
| `war3map.shd` | Карта теней |
| `war3map.wct` | Вода/клифы |
| `war3map.w3r` | Регионы |

### 2.3 Скрипты и строки

| Файл | Назначение |
|---|---|
| `war3map.lua` | **Основной скрипт** (Lua) — продукт сборки, ~65 000 строк. Собирается из `_lua/monolith_split/` |
| `_lua/monolith_split/` | **Исходники Lua** — разбиты на модули (см. раздел 3) |
| `war3map.j` | Оригинальный vJASS (устарел, заменён Lua) |
| `war3map.wts` | **Таблица строк** — локализация, имена юнитов, тултипы (~262 000 строк) |
| `war3map.wtg` | Триггеры GUI (бинарный формат) |

### 2.4 Конфигурация

| Файл | Назначение |
|---|---|
| `war3mapExtra.txt` | JassHelper включён |
| `war3mapMisc.txt` | Игровые константы: 24 игрока, макс. уровень героя 25, еда 999, таблицы XP, матрицы урона |
| `war3mapSkin.txt` | Кастомные скины UI (иконки еды, миникарты, текст фреймов) |
| `conversation.json` | Пустые диалоги/катсцены |
| `war3mapSkin.*` | Skin-оверрайды способностей, баффов, юнитов |

### 2.5 Импорты

| Файл | Назначение |
|---|---|
| `war3map.imp` | Список импортированных файлов |
| `war3mapImported/` | Импортированные модели HiveWorkshop (+ `readme.html` с копирайтами) |

---

## 3. Архитектура Lua-скрипта (`_lua/monolith_split/`)

Скрипт сконвертирован из vJASS в Lua. Исходники хранятся в `_lua/monolith_split/` и собираются через `manifest.json` → `build_map_lua.py` → `war3map.lua`.

### 3.1 Структура секций (`sections/`)

| Файл | Назначение | Строк |
|---|---|---|
| `00_prelude.lua` | Фреймворк: `ProbeLogWrite`, `OnInit`, `Bridge`, eval-канал | 559 |
| `01_globals.lua` | Ручные глобалы (не сгенерированные) | ~2400 |
| `02_pre_library_functions.lua` | Функции до библиотек | ~80 |
| `libraries/01_A1.lua` | | 6 |
| `libraries/02_AA.lua` | | 2 |
| `libraries/03_AI.lua` | AI-система | 16 |
| `libraries/04_AI0.lua` | AI-система | 341 |
| `libraries/05_ArmyBonus.lua` | Бонусы армии | 14 |
| `libraries/06_Global.lua` | Центральный хеш, таймеры, группы | 309 |
| `libraries/07_LibNewFunctions.lua` | Кастомные утилиты | 246 |
| `libraries/08_RandomLocs.lua` | Случайные локации | 39 |
| `libraries/09_SpellSleepAOE.lua` | AoE-сон | 75 |
| `libraries/10_common.lua` | Общие утилиты | 8 |
| `libraries/11_LibDifferentAiStuff.lua` | Данные AI, портирование юнитов | 356 |
| `libraries/12_SanctifiedEnchantment.lua` | Система апгрейдов | 268 |
| `libraries/13_Races.lua` | Выбор расы, `AiRace` конфигурация | 2867 |
| `libraries/14_AI2.lua` | AI-система (часть 2) | 166 |
| `80_runtime/` | **Сгенерированный код** — 66 файлов (см. 3.2) | 47K |
| `81_ai.lua` | AI-регистр рас | 276 |
| `82_ai_races.lua` | AI-стратегии рас | 1298 |
| `90_InitCustomTriggers.lua` | `InitCustomTriggers()` — регистрация всех триггеров | 1302 |
| `91_RunInitializationTriggers.lua` | | 25 |
| `92_map_setup.lua` | `main()`, `config()` | 325 |
| `93_main.lua` | | 43 |
| `94_config.lua` | | 37 |

### 3.2 Сгенерированный runtime (`80_runtime/`)

66 файлов в 10 подпапках. Все — продукт автоконвертации vJASS→Lua.
Файлы нарезаны по границам функций (`resplit_runtime.py`): каждый файл содержит
только целые функции и парсится самостоятельно.

| Папка | Содержание | Файлов |
|---|---|---|
| `_infra/` | `InitGlobals()`, HandleCounter, ReplaceUnit, boolexprs | 4 |
| `_lib/` | Экономика: `addArmyExp`, `AddCountDis`, `TimedUpdate`, графы | 9 |
| `_player/` | Управление игроками: `ClearPlayer`, вассалы, города | 6 |
| `_ui/` | `UISetup()`, IncomeTooltip | 2 |
| `_races/` | Enabler-функции: `HordeW2On`, `CultOn`, `DragonsOn`, etc. | 12 |
| `_ai/` | AI-ядро: `TryAttack`, `TryBuild`, порталы, вода | 8 |
| `_continental/` | Континенты: boolexprs, dungeons, `ProcessContinentalStuff` | 4 |
| `_features/` | Emerald Dream, Item Drops, Sounds | 3 |
| `_data/` | Статика: Unit Creation (943 строки), Regions (166), Cameras (107) | 3 |
| `triggers/` | **15 файлов** — вся игровая логика (42K строк) | 15 |

### 3.3 Триггеры (`80_runtime/triggers/`)

| Файл | Описание | ~Строк |
|---|---|---|
| `01_core_economy.lua` | Индексатор юнитов, AI-счёт, экономика, ивенты юнитов | 2637 |
| `02_game_modes.lua` | Лобби, столицы, феоды, доминация, fast test | 1530 |
| `03_continents_diplomacy.lua` | 7 континентов, дипломатия, income, туман войны | 1598 |
| `04_race_selection.lua` | Выбор расы (37 рас), 4 страницы UI | 1529 |
| `05_common_spells.lua` | Spell-система, предметы, флагманы, Fireball | 1009 |
| `06_transport_portals.lua` | Транспорт, корабли, порталы, F2, телепорты | 2671 |
| `07_hero_bezlikie_horde.lua` | Deathwing, элементали, Безликие, Horde W2 (дуэли, руны) | 3066 |
| `08_undead_trolls.lua` | Нежить (скелеты, чума), Forest/Jungle тролли | 2079 |
| `09_alliance.lua` | Альянс: Stormwind, Gilneas, Kultiras, Stromgarde, Dalaran | 3706 |
| `10_forsaken_gnomes.lua` | Forsaken (Banshee, MassMindControl), Gnomes (танки) | 3670 |
| `11_horde.lua` | Орда: TrueHorde, IronHorde, Sha, нейтралы, герои | 2984 |
| `12_silitid_goblin_bloodelf_bandit.lua` | Силитиды, Гоблины, Blood Elves, Бандиты | 5617 |
| `13_subraces_nightelf_naga_illidari_dragon.lua` | Night Elf, Naga, Worgens, Red Orden, Draenei, Illidari, Vryculs, Dragons | 2856 |
| `14_demon_elemental_undead_boss.lua` | Демоны, Элементали, Undead, Ice Trolls, Lords, камера/команды, Old Gods | 3787 |
| `15_ai_portals_cities.lua` | AI-триггеры, порталы городов, Dalaran/Naxx/Turtle, Emerald Dream | 3742 |

### 3.5 Список рас (37 `InitTrig_Race_*` в `80_runtime/triggers/04_race_selection.lua`)

1. Bezlikie (Безликие / Faceless Ones)
2. IceTrols (Ледяные тролли / Drakkari)
3. Stromgard (Стромгард)
4. Dragon (Драконы / Dragonflight)
5. Dragon2 (Драконы — альтернативные)
6. Argvinol
7. Elements (Элементали)
8. Goblins (Гоблины)
9. Demon (Легион / Burning Legion)
10. Illidari (Иллидари)
11. Bandits (Бандиты / Westfall)
12. Red Orden (Алый Орден / Scarlet Crusade)
13. Undead (Нежить / Scourge)
14. Horde (Орда)
15. Blood Elves (Эльфы крови)
16. Dalaran (Даларан)
17. KulTiras (Кул-Тирас)
18. Nocnorogdennue
19. Draeneis (Дренеи)
20. Vryculs (Врайкулы)
21. Kult Sum Molota (Культ Проклятых?)
22. Nerubs (Нерубы)
23. Silitids (Силитиды / Qiraji)
24. Gnomes (Гномы)
25. Gilneas (Воргены / Гилнеас)
26. Nagi (Наги)
27. Night Elf (Ночные эльфы)
28. Forsaken (Отрекшиеся)
29. Ogres (Огры)
30. Alliance (Альянс)
31. JungleTrolls (Лесные тролли)
32. FelOrk (Орки Скверны)
33. ForestTrolls (Лесные тролли)
34. CultOfDamned (Культ Проклятых)
35. Pandarens (Пандарены)
36. HordeW2 (Орда WC2)
37. Random (Случайная раса)

### 3.6 Инструменты сборки и дебага

| Команда | Назначение |
|---|---|
| `python build_map_lua.py` | Собрать `war3map.lua` из split-файлов |
| `python build_map_lua.py --check-only` | Проверить соответствие SHA256 |
| `python resplit_runtime.py [--write]` | Пересечь `80_runtime/*` по границам функций (byte-identical) |
| `idiom_engine.py` | Движок AST-идиоматизации: конкат секций, парс, замены по офсетам, AST-guard |
| `python idiom_conditions.py --write` | Свернуть condition-функции `if not(E) then return false…` → `return E` |
| `python idiom_strconcat.py --write` | Строковый `+` → `..` (фикс рантайм-краша) |
| `python idiom_booltrue.py --write` | Убрать `== true`/`== false`/`~=` |
| `python idiom_parens.py --write` | Снять лишние скобки в return/if/while/until (AST-guard) |
| `python -c "from luaparser import ast; ast.parse(...)"` | Проверка синтаксиса Lua |
| `HiveWE_cli run-map --map map.w3x --warcraft "..."` | Запуск карты |
| `HiveWE_cli probe-map ...` | Автотест с логами |
| `python agent_bridge.py exec "..."` | Bridge-команды в живой игре |

Подробные инструкции дебага: [DEBUG_WC3_MAP.md](DEBUG_WC3_MAP.md).

---

## 4. Модели и ассеты (111+ директорий)

### 4.1 Фракции и их ассеты

| Директория | Фракция | Файлов |
|---|---|---|
| `Alliance/` | Альянс (Штормград) | 25+ |
| `Alliance/heros/` | Герои (Anduin Wrynn) | 1 |
| `Bandits and Westfall/` | Бандиты (Defias/Westfall) | 1+ |
| `BloodElf/`, `BloodElves/` | Эльфы крови | 19+ |
| `CultOfDamned/` | Культ Проклятых | 18+ |
| `Dalaran/` | Даларан | 1 |
| `DemonsOrLegion/` | Пылающий Легион | 1 |
| `Dragon/`, `Dragons/` | Драконы (Alexstrasza, Ysera, Malygos, Nozdormu) | 13 |
| `Dwarfes/` | Дворфы | 53 |
| `ent/Corrupted/` | Порченные Ночные эльфы | 32 |
| `E_Elementals/` | Элементали (Ragnaros, Al'Akir, Neptulon) | 84+ |
| `Faceless/` | Безликие / Old Gods | ~30 |
| `FelOrk/` | Орки Скверны | 8 |
| `Forsaken/` | Отрекшиеся (Sylvanas, тёмные следопыты) | 84 |
| `Gnomes/` | Гномы (Gelbin Mekkatorque, танки) | 35 |
| `Goblins/` | Гоблины (шреддеры, ракеты, цеппелины) | 41 |
| `Horde/` | Орда (Garrosh, Saurfang) | 26 |
| `Horde2/` | Орда WC2-вариант | 27 |
| `HordeSha/` | Орда — шаманские эффекты | 3 |
| `IceTrolls/` | Ледяные тролли / Drakkari | 48 |
| `Kul-Tiras/`, `Kultiras/` | Кул-Тирас (морские люди, корабли) | 33 |
| `Murlocs/` | Мурлоки | 4 |
| `Naga/` | Наги (медузы, порталы) | 4 |
| `Nightelfs/` | Ночные эльфы | 3 |
| `Ogre/` | Огры (Gruul, Cho'gall) | 54 |
| `Orden/`, `Silverhand/` | Серебряная Длань / Scarlet Crusade | 22 |
| `Orgrimmar/` | Оргриммар (здания) | 6 |
| `Pandarens/` | Пандарены (brewmasters, монахи) | 67 |
| `Silitids/` | Силитиды / Qiraji (Анубисаты, скарабеи) | 21 |
| `SkeletsDifferent/` | Варианты скелетов | 14 |
| `Sromgard/` | Стромгард | 17 |
| `Stalgorn/` | Дворфийские/гномьи замки | 5 |
| `Trolls/` | Тролли (лесные/джунгли/кровавые) | 101 |
| `Undead/` | Нежить / Scourge (Lich King) | 19+ |
| `Worgens/` | Воргены / Гилнеас (Genn Greymane) | 25 |

### 4.2 Эффекты и снаряды

| Директория | Содержание |
|---|---|
| `Auras/` | Ауры (63 вариации Shocking Wave) |
| `Aurass/` | Аура эльфов крови |
| `Effects/` | Эффекты заклинаний (12 файлов) |
| `NewEffects/` | Эффекты заклинаний (36 файлов) |
| `Missiles/` | Снаряды (68 файлов + Arcane Tower recolors) |
| `Lava/` | Лава-эффекты (9 вариаций) |
| `ForUnits/` | Наложения на юнитов (2) |

### 4.3 Декорации и текстуры

| Директория | Содержание |
|---|---|
| `Doodads/` | Декорации: пирс, расщелины |
| `Fromlta/` | Декорации (8 файлов) |
| `Walls/` | Маленькие стены (5) |
| `Stone Walls/` | Каменные стены по тирам (12) |
| `Pandaria/` | Пандария декорации (1) |
| `Common/` | Общие здания (5) |
| `PathTextures/` | Текстуры pathing (3) |
| `Textures/` | Общие текстуры (4) |
| `TerrainArt/Outland/` | Текстура Outland (1) |

### 4.4 Иконки

| Директория | Содержание |
|---|---|
| `CommonIcons/` | Общие иконки (14) |
| `ReplaceableTextures/CommandButtons/` | Кнопки способностей BTN/PAS/ATC/SSC (1 118+) |
| `ReplaceableTextures/CommandButtonsDisabled/` | Disabled-иконки DISBTN/DISPAS (1 348+) |

### 4.5 UI

| Директория | Содержание |
|---|---|
| `UI/Console/Human/` | Плитки UI (7 DDS) |
| `UI/Feedback/Resources/` | Иконки ресурсов (3 DDS) |

### 4.6 Локализация

| Директория | Описание |
|---|---|
| `_Locales/deDE/` | Немецкий (пусто) |
| `_Locales/enUS/` | Английский (пусто) |
| `_Locales/esES/` | Испанский (пусто) |
| `_Locales/esMX/` | Испанский (Мексика) (пусто) |
| `_Locales/frFR/` | Французский (пусто) |
| `_Locales/itIT/` | Итальянский (пусто) |
| `_Locales/koKR/` | Корейский (пусто) |
| `_Locales/plPL/` | Польский (пусто) |
| `_Locales/ptBR/` | Португальский (пусто) |
| `_Locales/ruRU/` | Русский (пусто) |
| `_Locales/zhCN/` | Китайский упрощённый (пусто) |
| `_Locales/zhTW/` | Китайский традиционный (пусто) |

---

## 5. Игровые константы (`war3mapMisc.txt`)

- **Макс. игроков**: 24
- **Макс. уровень героя**: 25
- **Food ceiling**: 999
- **Таблицы опыта**: кастомные
- **Матрицы урона**: модификаторы для Chaos и Magic типов атаки против всех типов брони
- **Матрицы защиты**: свои модификаторы для всех типов атаки

---

## 6. Git

- **Remote**: `https://github.com/VinerX-Games/23-Race-Legion.git`
- **Ветка по умолчанию**: `main`
- **Другие ветки**: `23-Расы-Без-Краша-12.03.23`, `Landscape`, `RO_Units`, `Triggers`, `TryToFix`, `bk`, `Еще-раньше-попытка`, `Мб-без-краща`, `Проверка-олегиной-версы`
- **Коммиты**: на русском языке, упоминают колодцы, дворфов, архонтов, правки всего

---

## 7. Ключевые особенности проекта

- **30+ играбельных фракций** (против 4 в оригинале)
- **24 игрока** на одной карте
- **Огромная карта** с несколькими континентами
- **Система столиц / вассалитета / доминации**
- **Кастомная система предметов** (шлемы, броня, оружие, кольца, обувь)
- **Продвинутый AI** с отслеживанием вражеских столиц
- **Тир-апгрейды** (T1 → T2 → T3) для каждой расы
- **Тысячи кастомных моделей** с HiveWorkshop
- **Полная локализация** на русском языке (через `war3map.wts`)

---

## 8. Разработчики

Согласно строке TRIGSTR_005: **Reptile, Nicamchik, Modus, Capral, Ageron**.

Проект заброшен. Discord: https://discord.gg/Cc3tq5UyWH
