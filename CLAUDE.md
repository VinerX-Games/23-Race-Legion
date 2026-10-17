# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Проект

23 Race Legion — карта Warcraft III: Reforged (Altered Melee, Risk-жанр, до 24 игроков, ~37 рас).
Карта хранится распакованной в `map.w3x/` (object data, ландшафт, тысячи импортов). Скрипт карты —
Lua 5.3 (WC3-рантайм), автоконвертированный из vJASS; ~69 000 строк. Язык кода, комментариев,
документации и коммитов — русский (коммиты в стиле conventional commits: `fix(ai): ...`, `chore(release): ...`).

Документация — в `docs/` (индекс: `docs/README.md`). Перед работой над подсистемой читать профильный док:
`PROJECT_MAP.md` (карта проекта), `DEBUG_WC3_MAP.md` (дебаг), `LIVE_AGENT_BRIDGE.md` (мост),
`AI_*.md` (ИИ), `SCRIPTS_ANALYSIS.md` (игровые системы исходного vJASS).
Текущий аудит кода и список найденных, но не исправленных багов — `docs/AUDIT_TODO.md`
(анализаторы — `scripts/audit/`).

## Сборка и проверки

```bash
python build_map_lua.py                 # собрать map.w3x/war3map.lua из split-исходников
python build_map_lua.py --check-only    # сверить SHA256 собранного файла с исходниками (ничего не пишет)
build.bat                               # сборка + синтаксис-проверка luaparser
python -c "from luaparser import ast; ast.parse(open('map.w3x/war3map.lua', encoding='utf-8').read()); print('OK')"

python -m pip install -r tests/requirements.txt   # lupa (Lua 5.3 в Python)
python -m unittest discover -s tests -v            # все тесты
python -m unittest tests.test_ai_teleport -v       # один модуль
python -m unittest tests.test_ai_teleport.AiTeleportTests.test_empty_army_does_not_spawn_or_order  # один тест
```

Тесты исполняют split-секции в Lua 5.3 (`lupa.lua53`) с моделью нативов WC3, заданной фикстурой
прямо в тесте. Это не замена проверке в игре.

Запуск в игре (нужны Warcraft III и `HiveWE_cli` из HiveWE_VinerX_Edition; пути в `_run.bat`):
`HiveWE_cli probe-map --map map.w3x --warcraft "F:/Games/Warcraft III" --args "-window -nowfpause" --click-after 60 --wait 360 --probe-log 23Race_probe_log.pld --keep-open`.
Путь `--warcraft` всегда в кавычках (пробел). Без `-nowfpause` игра встаёт на паузу при потере фокуса.

## Главное правило сборки

- Источник истины — `map.w3x/_lua/monolith_split/sections/**`. `map.w3x/war3map.lua` — артефакт:
  **никогда не править его руками**, только секции + `python build_map_lua.py`, и коммитить оба.
- `build_map_lua.py` просто конкатенирует файлы в порядке `manifest.json` (`sections[].file`).
  Новый файл секции не попадёт в сборку, пока его не добавить в манифест; порядок в манифесте =
  порядок определения глобалов/функций в итоговом скрипте.
- Ошибки рантайма приходят с номером строки собранного `war3map.lua`; искать её там, чинить в секции.
- Релиз: правка `version.txt` (формат `23_race_1_6_NNN`) и строки версии в `docs/PROJECT_MAP.md`.

## Архитектура Lua-скрипта

Порядок секций в манифесте:

- `00_prelude.lua` — инфраструктура: `ProbeLogWrite` (лог в `.pld` через Preload + `BJDebugMsg`),
  `LogFilter`/теги логов, `ProbeStep`, `safeCall`, очередь отложенной инициализации `OnInit`,
  Preloader-мост и eval-канал для живой отладки, чат-команды `-bridge:`, `-log`, `-handle`.
- `01_globals.lua`, `02_pre_library_functions.lua` — глобалы и полифиллы нативов (например,
  `UnitAlive` переопределён через проверку жизни: в WC3-Lua натив отдаёт nil).
- `libraries/*.lua` — бывшие vJASS-библиотеки (`Global`, `LibNewFunctions`, `AI0` с фильтрами
  `f_*`, `LibDifferentAiStuff` с ТП-логистикой, `Races` с процедурным ИИ рас).
- `80_runtime/**` — автоконвертированный GUI/vJASS-код, нарезанный по границам функций:
  `_infra`, `_lib` (экономика), `_player`, `_ui`, `_races`, `_ai` (legacy-ИИ: атака, флот, стройка),
  `_continental`, `_features`, `_data` (CreateAllUnits/регионы/камеры), `triggers/` (доменные бандлы
  `01_core_economy`…`15_ai_portals_cities`) и `triggers/races/<Race>.lua` (триггеры конкретных рас).
- `81_ai.lua` — реестр ИИ-рас (`RegisterAiRace`, `AiRaceOf(pi)`, токены для `-aiN <token>`) и
  generic-движки, исполняющие декларативные данные рас (buildings / production / gates / branches /
  worker / compTarget). Диспетч всех legacy-хуков идёт через реестр.
- `82_ai_races.lua` + `82_ai_races/NN_<race>.lua` — по одному `RegisterAiRace("Key", {...})` на расу.
  Добавление ИИ-расы = новый файл + запись в манифесте; сайты диспетча не трогать.
- `83_ai_brain.lua` — «мозг» ИИ: единый round-robin тик (`PlayerGet1` → `PlayerArmy` →
  `AiBrainArmyTick`: Perceive → Produce → Build → Objectives → Focus → Naval → Diplomat).
  World model в `AiData[pi].wm`, отряды трекаются без FSM. Режим per-race `brain="objective"|"swarm"`,
  swarm (`AiArmyLegacyTick`) — фоллбэк. Профайлер `AiProfileData`.
- `84_ai_diplomat.lua` (союзы/предательства ботов), `85_ai_portal_graph.lua` (граф порталов
  между континентами, см. `docs/PORTAL_GRAPH.md`).
- `90_InitCustomTriggers.lua` → `91_RunInitializationTriggers.lua` → `92_map_setup.lua`/`93_main.lua`
  (`main()`, `config()`). `main()` создаёт карту через `ProbeStep`, остальное регистрирует в `OnInit`
  и выполняет отложенно на старте игры.

Ключевые состояния: группы ИИ на игрока `udg_Ai_army/navy/units/builders/buildings/harvest[pi]`,
KV-хранилище `AiData[pi][key]` (счётчики `getAiCount`/`NumberAdd`), `playerCapital[pi]`,
`udg_StolicaGroups` (столицы), `udg_ZahvatBuildings` (точки захвата). Экономика тикает раз в 25 с;
формулы и прочие системы описаны в `docs/SCRIPTS_ANALYSIS.md`.

## Подводные камни WC3-Lua (важно при любых правках)

- **Мультиплеер детерминирован.** Не вводить `math.random`/`os.time` в игровую логику (только
  `GetRandomInt/Real`); не создавать хендлы и не менять игровое состояние внутри
  `GetLocalPlayer()`-веток; `pairs()` в синхронной логике — только по таблицам с целыми ключами.
  `os.clock()` допустим лишь для профайлера.
- **Глобальные скретч-группы** (`gGroup`, `gUnit`, `gX`…) нельзя переиспользовать вложенно:
  enum/`GroupClear` той же группы внутри `ForGroup`/фильтра даёт жёсткий C++-краш
  `ACCESS_VIOLATION 0x6C` (pcall его не ловит). Во вложенных путях — локальная группа.
- **boolexpr ≠ функция.** Параметры `GroupEnum*`/`TriggerAddCondition` ждут `Filter(f)`/`Condition(f)`,
  кэшированный в переменной; скрипт `scripts/group_condition_to_direct.py` когда-то заменил часть
  на голые функции — такие места считать багом.
- **Артефакты конвертации vJASS→Lua:** потерянные параметры функций (тело читает несуществующие
  глобалы), `local`, объявленные внутри `if` и используемые после, строковый `+` вместо `..`,
  `tArray[tArray0]` вместо `tArray[tArray[0]]`, пустые стабы `function Native() end`, затеняющие
  настоящие нативы (чинить через `X = X or fallback`), `IsTerrainPathable` инвертирован (`true` = нельзя).
- Утечки: каждую `Location`/`GetUnitLoc`/группу из `GetUnits*` освобождать (`RemoveLocation`,
  `DestroyGroup`), особенно в периодических триггерах (0.03–0.1 с).
- Lua-паттерны не поддерживают `|` (альтернацию).

## Игровые тексты и база зависимостей (обязательно)

- **Стандарт текстов.** Любые новые или изменяемые названия, подсказки, сообщения и UI-тексты (object data,
  WTS, Lua) — строго по `docs/UI_TEXT_STYLE.md` и палитре `docs/UI_COLOR_PALETTE.md`; порядок пакетной работы —
  `docs/UI_TEXT_WORKFLOW.md`. Кратко: короткое название без командных слов («Нанять», «Построить»…) и без
  горячей клавиши; подробное описание начинается с метки типа (`ЮНИТ:`, `ЗДАНИЕ:`, `ИССЛЕДОВАНИЕ:`…) цвета
  `B99D66`, основной текст `CED4DA`, названия `EBC56C`, числа `FFFFFF`; после цветного фрагмента явно
  восстанавливать основной цвет (`|r` его не восстанавливает); списки и числа — только по фактическим
  object data и Lua.
- **База зависимостей** `docs/techtree/` (README там же) — сгенерированное дерево технологий всех рас:
  строит/обучает/исследует/способности/требования/стоимость/хоткеи. Читать её вместо разбора object data;
  JSON руками не править. При любом изменении этих зависимостей или свойств (добавление, удаление,
  переименование объекта; списки, требования, стоимость, хоткеи, уровни; стартовые юниты/технологии рас
  в Lua) в том же коммите: `python scripts/export_techtree.py` → `python scripts/export_techtree.py --check`
  выводит `OK`. Нет HiveWE_cli — указать это в коммите/PR.

## Отладка

- Логи: `ProbeLogWrite("[TAG] ...")`; на экран выводятся по фильтру тегов. В `.pld` пишутся только
  после `ProbeLogEnableFlush()`: `%USERPROFILE%\Documents\Warcraft III\CustomMapData\23Race_probe_log.pld`.
  Для логов не использовать `DisplayTimedTextToPlayer`. Внутри condition-фильтров не логировать.
- Ошибки колбэков: `[CALLBACK-ERR]` в логе / `InitErrors`.
- Жёсткие краши: `Documents\Warcraft III\Errors\<дата>\Crash.txt`; локализация — бисекция подсистем
  тумблерами через мост + небуферизованные breadcrumb'ы (`docs/AI_CRASH_HANDOFF.md`).
- Живой мост: `python agent_bridge.py reset` / `exec "<lua>"` / `exec --file f.lua` / `--watch`
  исполняет Lua в запущенной игре (в игре сначала `-bridge:eval:on`). Перед каждым запуском карты
  удалять старые `CustomMapData\23race_eval_*.pld`, иначе они переиграются как новые команды.
  Подробно — `docs/LIVE_AGENT_BRIDGE.md`.
- Спавн бота: чат `-aiN <token>` или `exec "createAiPlayer(N, 'token')"`.

## Прочее

- `scripts/` — одноразовые/повторяемые Python-трансформы исходников (идиоматизация через
  `idiom_engine.py`, нарезка бандлов, валидатор ИИ-рас); описание — `scripts/README.md`.
- Мусор в секциях, не входящий в манифест (`82_ai_races.lua.tmp`, `*.ps1`, `update_manifest*.py`),
  в сборку не попадает.
- Файлы `_*.lua` в корне и `scripts/lua_scratch/*.lua` — gitignored черновики для моста.
