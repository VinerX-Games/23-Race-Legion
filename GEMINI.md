# 23 Race Forever — Project Guidelines & Antigravity Rules

## Название карты

С версии 1.6.515 карта называется **23 Race Forever** (раньше — 23 Race Legion). Нумерация версий
продолжает линию Legion без сброса: 1.6.514 (последняя Legion) → 1.6.515 (первая Forever) → 1.6.516 …

- Название в игре — WTS `STRING 003`: `23 Race Forever 1.6.NNN` (из неё же берётся версия для приветственной панели).
- `version.txt` — по-прежнему `23_race_1_6_NNN`; файл релиза — `23_Race_Forever_v1_6_NNN.w3x`, тег — `v23_race_1_6_NNN`.
- Во всех новых текстах, доках, релиз-нотах и коммитах писать «23 Race Forever». Репозиторий на GitHub пока
  `VinerX-Games/23-Race-Legion`, локальные пути вида `23-Race-Legion` не трогать. «Legion» в коде расы
  Демонов (Пылающий Легион, `Fin7Legion`, токен `legion`) к названию карты не относится.

## Главное правило исходников
- Источник истины — файлы секций в `map.w3x/_lua/monolith_split/sections/**`.
- Файл `map.w3x/war3map.lua` — собранный монолит (69 000+ строк). **НИКОГДА не редактировать его вручную**.
- После любых правок в секциях: запустить `python build_map_lua.py` (или `python scripts/wc3_tools.py build`).
- Для проверки целостности перед фиксацией: `python scripts/wc3_tools.py verify`.

## Экономия токенов и инструменты поиска
- **Поиск ошибки по номеру строки**:
  При ошибках рантайма или крашах с указанием строки в `war3map.lua:NNNN` — использовать:
  `python scripts/wc3_tools.py line NNNN`
  Скрипт мгновенно выведет файл секции, относительную строку, функцию и контекст без чтения десятков тысяч строк.
- **Поиск функций и определений**:
  `python scripts/wc3_tools.py find <имя_функции>` — компактный список сигнатур и файлов вместо раздувания контекста.
- **Поиск FourCC rawcode**:
  `python scripts/wc3_tools.py rawcode <id>` — точечные вхождения юнита/здания/спелла.
- **Инспекция объектов и рас карты**:
  - Объект по ID (с разрешением русских имен): `python scripts/wc3_hivewe.py object <id>`
  - Поиск по имени: `python scripts/wc3_hivewe.py search "<запрос>"`
  - Дерево и юниты расы: `python scripts/wc3_hivewe.py race "<суффикс>"`
  - Список всех рас: `python scripts/wc3_hivewe.py races`
- **Текстовый поиск по репозиторию**:
  Всегда использовать `rg` (ripgrep) с флагами ограничения вывода. Никогда не загружать монолит целиком через `view_file`.

## Инварианты WC3 Lua
- **UnitAlive**: В WC3 Lua натив `UnitAlive` возвращает `nil` для pre-placed юнитов. Всегда использовать `GetUnitState(u, UNIT_STATE_LIFE) > 0.405`.
- **IsTerrainPathable**: Инвертирован (`true` = непроходимо). Для проверки суши: `not IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY)`.
- **Детерминизм и мультиплеер**: В синхронной игровой логике не использовать `pairs()` по нечисловым ключам, `os.time()`, `math.random()`. Использовать `ipairs()` или числовые циклы, `GetRandomInt/Real`.
- **Глобальные группы**: Избегать вложенных `GroupEnum*`/`GroupClear` на глобальных скретч-группах (`gGroup` и т.д.) — вызывает C++ crash 0x6C.
- **Фильтры**: В `GroupEnum*` и триггерах передавать кэшированный `Filter(f)` / `Condition(f)`, а не голую функцию.
