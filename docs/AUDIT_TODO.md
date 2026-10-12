# TODO: аудит Lua-кода карты (сессия 2026-10-11)

Задача: просмотреть весь Lua-код карты и найти баги, причины фаталов, места для оптимизации
и улучшения архитектуры. Аудит выполнен частично. Ниже то, что найдено и **проверено по коду**,
и то, что ещё осталось сделать.

**Статус (сессия 2026-10-12):** раздел A исправлен (коммит `7bb5143`), плюс найденное по ходу
(раздел A+ ниже). Коммиты сессии: `7bb5143`, `472a451`, `a40acde`, `87614db`, `b47225b`, `3a5ea68`, `cc149f4`
(локально, **не запушены**). В игре (probe-map) пока **не проверено**. `scripts/audit/`, `CLAUDE.md`,
`.claude/`, этот файл — по-прежнему untracked (решение о коммите за пользователем).

Формат ссылок: `секция:строка` (относительно `map.w3x/_lua/monolith_split/sections/`) и строка
собранного `war3map.lua` (`wl:N`) на коммите `4df89dd`. После любых правок номера строк `wl` сместятся.

Оригинальный vJASS для сверки сигнатур: `git show ea6d45d^:map.w3x/war3map.j > war3map.j`.

---

## Инструменты аудита (`scripts/audit/`)

Нужны `pip install luaparser lupa` и сигнатуры нативов:
```bash
mkdir jass && for f in common.j Blizzard.j common.ai; do curl -sfL -o jass/$f https://raw.githubusercontent.com/lep/jassdoc/master/$f; done
git show ea6d45d^:map.w3x/war3map.j > war3map.j
```
| Скрипт | Что ищет | Запуск |
|---|---|---|
| `globals_audit.py` | чтение необъявленных глобалов, дубли функций, несовпадение числа аргументов и параметров | `python -I scripts/audit/globals_audit.py map.w3x/war3map.lua jass out.json` |
| `boolexpr_audit.py` | голая функция передана в параметр `boolexpr` | `... boolexpr_audit.py map.w3x/war3map.lua jass war3map.j` |
| `reentry_audit.py` | `ForGroup`/enum по глобальной группе, колбэк которого перечисляет/чистит ту же группу | `... reentry_audit.py map.w3x/war3map.lua` |
| `leak_audit.py` | дисбаланс создания/удаления локаций, групп, эффектов, таймеров по функциям (эвристика) | `... leak_audit.py map.w3x/war3map.lua` |
| `intdiv_audit.py` | float-деление `/` в integer-параметрах нативов (результат: 0 находок) | `... intdiv_audit.py map.w3x/war3map.lua jass war3map.j` |
| `closure_nil_audit.py` | `x = nil` во внешней функции после создания замыкания, использующего `x` | `... closure_nil_audit.py map.w3x/war3map.lua` |
| `scope_leak_audit.py` | чтение имени после закрытия блока, где оно было `local` | `... scope_leak_audit.py map.w3x/war3map.lua` |
| `init_smoke.py` | прогон `config()`/`main()`/колбэков на авто-заглушках нативов (**не доделан**, см. ниже) | `... init_smoke.py map.w3x/war3map.lua jass` |

Ложные срабатывания `globals_audit`: имена, объявленные через `_G.X = ...` (`Bridge*`, `LogFilter`,
`InitErrors`, `ProbeLog*`), `FourCC`, метки `goto` (`continue`, `cont`, `found`, `skip*`, `next*`).

---

## A. Подтверждённые баги — ИСПРАВЛЕНО (`7bb5143`)

### A1. Потерянные параметры функций (17 функций) — Lua-ошибка при каждом вызове
Конвертер выдал `function F()`, а вызовы идут с аргументами; тело читает несуществующие глобалы
(`nil`) → арифметика на nil / неверная логика. Восстановить сигнатуры из `war3map.j`:

| Функция | Секция | Оригинальная сигнатура |
|---|---|---|
| `UnUgolMT`, `UnRastMT` | `80_runtime/triggers/07_mixed_heroes.lua:324` (wl:24209) | `(x1, x2, y1, y2)` |
| `JSTRUgolMT`, `JSTRRastMT`, `JSTRParabolaZ` | `80_runtime/triggers/races/Bezlikie.lua:484` (wl:25692) | `(x1,x2,y1,y2)`, `(x1,x2,y1,y2)`, `(h,d,x)` |
| `ManabombaMissle` | `80_runtime/triggers/06_transport_portals.lua:764` (wl:22348) | `(caster, destination)` |
| `EndBranch` | `80_runtime/triggers/races/Alliance.lua:2347` (wl:30870) | `(p)` |
| `AllowedPosition` | `80_runtime/triggers/03_continents_diplomacy.lua:208` (wl:17982) | `(u)` |
| `CorrectNumber` | `80_runtime/triggers/14_misc_system.lua:626` (wl:47922) | `(pi2)` |
| `isShip`, `aiShipJoins`, `isNavalBase`, `aiNavalBaseJoin`, `aiRep`, `aiRepUnvul` | `80_runtime/triggers/15_ai_portals_cities.lua:1572–1738` (wl:50526–50692) | `(id)`, `(u, pi)`, `(id)`, `(u)`, `(pi)`, `(pi)` |
| `CheckNearCapitals` | `15_ai_portals_cities.lua:1958` (wl:50912) | `(city)` |
| `CheckPosition` | `15_ai_portals_cities.lua:3289` (wl:52243) | `(x, y, add)` |

Затронуто: снаряды/прыжки Безликих и героев, манабомба, ветки Альянса, позиция на континентах,
режим «Архонт», флот и ремонт ИИ, проверка позиции столиц (Даларан/Наксрамас/Черепаха).

### A2. Реентерабельность `gGroup` → жёсткий краш 0x6C
`TeleportUnits`/`TeleportUnitsED` (`15_ai_portals_cities.lua:2006`, wl:50960): `ForGroup(gGroup, TeleportUnitsEach)`
→ `EnterGreen(u)` → `WakeGreenUp()` (`_features/105_emerald_dream.lua:30`) делает
`GroupEnumUnitsInRect(gGroup, ...)` и `GroupClear(gGroup)` посреди перебора той же группы.
Фикс: локальная группа в `WakeGreenUp`/`SleepGreen` (или в `TeleportUnits`), либо собрать юниты,
а `EnterGreen` вызвать после цикла. Перепроверить `Trig_Kill_Actions` (`14_misc_system.lua:147`) →
`HandleVassalization` → `ClearPlayer`: детектор отметил группу `g` (возможно, false positive — локальная).

### A3. Голые функции вместо boolexpr (11 мест)
Обернуть в кэшированный `Filter(f)` (как в коммите `a126683`):
`typeBool` (`01_core_economy.lua:394`), `OwnUnit`+`IsCityEnemy` (`06_transport_portals.lua:1540`),
`F2_targets` ×4 (`06_transport_portals.lua:1744` и далее, wl:23328/23480/23627/23775), `Adal`
(`07_mixed_heroes.lua:448`), `Talisra` (`races/Scourge.lua:312`), `PortalConditions`/`PortalConditionsED`
(`15_ai_portals_cities.lua:2012`, wl:50966/50992). Вероятный источник — `scripts/group_condition_to_direct.py`.
Портальные фильтры критичны: в них проверка владельца (`PortalTeleportOwner`), без фильтра
портал может перемещать чужие юниты.

### A4. Дипломат: локальные переменные вне области видимости
`84_ai_diplomat.lua:889` (wl:66355), `AiDiplomatConsiderBreak`: `otherPower`/`myPower` объявлены
`local` внутри `if allyAge >= AiDiplomatMinAllyAge then`, а читаются в блоке предательства →
`attempt to compare nil`, как только бот-предатель выигрывает бросок. Вынести расчёт силы выше.

### A5. Массовая утечка хендлов в `RRR` (25 раз/с)
`01_core_economy.lua:246` (wl:14171), триггер `RRR` с периодом 0.04 с (аура Груула): каждый тик
`GetUnitsInRangeOfLocMatching(..., GetUnitLoc(Gruul[pi]), Condition(...))` — утекают группа,
локация и boolexpr; на каждого врага — ещё 2 локации, причём `l = nil` стоит **перед**
`RemoveLocation(l)`. Переписать на координаты (`GetUnitX/Y`, `GroupEnumUnitsInRange` с постоянной
группой и кэшированным фильтром, `SetUnitPosition`).

### A6. Прочие nil-баги
- `s__SanctifiedEnchantment_Levelthis` (`libraries/12_SanctifiedEnchantment.lua:160`) → должно быть
  `s__SanctifiedEnchantment_Level[this]` (бафф не снимается по длительности).
- `BlzGetEventDamageSource()` (`02_game_modes.lua:1042`, wl:17493) — такого натива нет, нужен
  `GetEventDamageSource()`. Падает вассализация при смертельном уроне по столице.
- `Trig_RazvedEnd_Actions` (`01_core_economy.lua:2445`): `Boolexpr` не определён (в JASS был
  `local boolexpr Boolexpr = Condition(Trig_RazvedEnd_Func002001003)`) → enum без фильтра,
  `RemoveUnit(FirstOfGroup(g))` удаляет случайный юнит в радиусе 1500.
- `f_PortB` (`libraries/04_AI0.lua:150`): `CheckId` нигде не задаётся (`PortB` не используется — мёртвый код).
- Мёртвый код с ошибками: `s__StackTemplate_destroy/create` (`libraries/06_Global.lua:236`),
  `ReturnFPS` (`_infra/20_custom_script.lua:80`) — удалить или починить.

### A7. Отладочные чат-команды доступны всем игрокам в релизе
`00_prelude.lua:430+`: `-bridge:<op>:<arg>` (включая `ally`, `create_ai`, `race_select`, eval),
`-handle`, `-log`, `-codexping` зарегистрированы для всех 24 игроков. Любой игрок в мультиплеере
может менять союзы и создавать ИИ. Ограничить (флаг отладки / только одиночная игра / только хост).
Там же: `-log` никогда не работает — паттерн `(on|off|...)` в Lua не поддерживает `|`
(`00_prelude.lua:551`); разобрать слово и сравнить вручную.

---

## A+. Найдено и исправлено в сессии 2026-10-12

- **`BlzGroupUnitAt` индексируется с 0**: циклы `for i = 1, size` / `while i >= 1` после
  идиоматизации. Legacy-атака ИИ (`94_ai_attack.lua`, режимы group-fast/group-wide) на первой же
  итерации получала `nil` (индекс `size`), отдавала приказ пустой группе и выходила — армия не
  атаковала. Флот (`95_ai_attack_naval.lua`), F2, экономика, Орда — терялся юнит с индексом 0.
- **Ещё 52 голых фильтра**: `udg_Boolexpr = <функция>` (40) и `bex = <функция>` (12) — анализатор
  `boolexpr_audit.py` их не видит (передача через переменную). Введён `CachedFilter(f)`
  (`02_pre_library_functions.lua`, ленивый кэш, без хендлов на корневом уровне).
- **Потерянные фильтры (ошибки ещё в JASS, `local boolexpr b` без значения)**: `MeatDeal`/`BoneDeal`
  (Нежить — сливали и удаляли ЛЮБЫХ юнитов в радиусе, в т.ч. врагов), `Help`/`HelpButton`/`BrokenBlood`
  (Тролли джунглей), `ReturnDamage` (Лесные тролли — фильтра не было вовсе, добавлен `ReturnDamageEnemy`),
  `NoDeath` (Красный орден).
- **`x = nil` после создания замыкания** (35 мест, детектор `closure_nil_audit.py`): upvalue общий,
  колбэки таймеров получали `nil` — периодические таймеры спеллов не уничтожались и работали вечно
  (SpellArrow создавал даммиков каждые 0.35 с), кастер мог остаться спрятанным/на паузе,
  `SecondChance` вызывал `CheckAndCreateCapital(nil)`.
- `BrainBuild` → `BrainStrategTick(pi, p, ...)` с необъявленным `p` (исследования грейдов ИИ с nil-игроком).
- Sand Strike (Иллидари): урон по `udg_SSpicked[udg_SSinteger[3]]` (nil) — способность не наносила урон.
- `IsCityEnemy`: `>= 0` всегда истинно → `> 0`; `F2 Attack Point`: `GroupRemoveGroup` с перепутанными
  аргументами; `isNavalBase` читал глобал `gId`; утечка группы в `CheckNearCapitals`.
- Мост: `op == "log"` с тем же `|`-паттерном (`15_ai_portals_cities.lua`).
- Отладочные чат-команды: `DebugChatAllowed()` — только при ≤1 человеке в слотах или `DebugChatForce`.
- `ProbeLogWrite`: кольцевой буфер (C5).
- **Восстановлены пути моделей/эффектов (42 пути в 17 файлах)**: при vJASS→Lua конвертации были вырезаны обратные слэши в путях стандартных моделей (Sand Strike, Lava Spawn, Mass Teleport, War Stomp, Volcano, Blood, DNC и др.).
- **Восстановлены имена Колодцев Кровавых Эльфов**: русские названия цветов в `BloodElves.lua` («Колодец арканы», «Колодец скверны», «Колодец бездны», «Колодец света»).
- **Баги способностей и логики Лордов (`Lords.lua`)**: в `Trig_LordWave`, `Trig_MassBaff`, `Trig_LordsAssist` вызов `DestroyGroup(udg_AllLords)` происходил внутри первого шага `ForGroup`, ломая перебор остальных лордов; утекали группы `udg_MellLord`, таргетинг-локации, а в `LordsAssist` читался `GetSpellTargetLoc()` после 3-секундного ожидания. Переписано на замыкания таймеров и координаты. В `NaxramasKills`/`DalaranKills` использован `ForGroupDestroy`.
- **Утечка дамми-юнитов в `MassHEX` (`14_misc_system.lua`)**: `Trig_MassHEX` спавнил `repD` для каждого юнита без таймера жизни/удаления, забивая карту даммиками; теперь фильтрует живых врагов, удаляет даммика через 2 секунды и работает по координатам.
- **Утечки `DestroyTrain` (`14_misc_system.lua`)**: устранены 8 утечек локаций и 7 утечек Rect (`GetRectCenter(OffsetRectBJ(...))`), декорации создаются сразу по координатам.
- **Баг спавна щупалец Йогг-Сарона (`OldGods.lua`)**: `Trig_Qogg_HP_24k_O` и `17k_O` спавнили все 4 щупальца в `gg_rct_Yog1_5` вместо `Yog1_1..4`, скапливая их в одной точке; исправлено на раздельные координаты `Yog1_1..4` и `Yog1_5..8` без создания `location`.
- **Утечки `PortalFix` (`15_ai_portals_cities.lua`)**: `WaygateSetDestinationLocBJ` заменён на прямой `WaygateSetDestination` с `GetRectCenterX/Y`.
- **Утечки и блокирующие ожидания в спеллах (`05_common_spells.lua`)**: `Fireball` и `Fire Arrow` избавлены от `PolledWait` и утечек `GetUnitLoc`; переведены на таймерные замыкания и расчет дистанции по координатам. `Research_Ot` избавлен от `RectFromCenterSizeBJ` и утечки `location`. Поле астрала и `Spell_Copy` переписаны без утечек проекций и групп.
- **Защита от nil в `HandleVassalization` (`02_game_modes.lua`)**: добавлена проверка `if not capital or not attacker then return end` перед обращением к `GetPlayerId`.
- **Инициализация `AiDiplomatProposalTimeout` (`84_ai_diplomat.lua`)**: задан дефолт на уровне модуля (`30`), предотвращающий nil при чтении без явной конфигурации.

Замечания (не исправлено, решение за автором):
- `aiRep`/`aiFixAll` теперь получает `pi` и работает, но достижим только чат-командой хоста
  `" - airep"` (таймер `aiFixer` в Lua не запускается). Он обнуляет `AiData[pi]` (world model мозга)
  и спамит `BJDebugMsg` — не использовать в игре с brain-ботами.
- `Trig_Kill_Actions` → `ClearPlayer` в `reentry_audit.py` — ложное срабатывание (группа `g` локальная).
- `ReturnDamage` (Лесные тролли) раньше не срабатывала вовсе; фильтр врагов `ReturnDamageEnemy` —
  реконструкция по смыслу, проверить баланс в игре. То же для MeatDeal/BoneDeal (фильтры cDa6/cDat).

Также сделано (perf): `ForGroupBJ(GetUnits…)` → `ForGroupDestroy` (41), `SetUnitPositionLoc(u,
PolarProjectionBJ(...))` → `SetUnitPolarLoc` (7), утечка `udg_To4kaCaster` в тике Spell_Dvij,
`Condition/Filter` в аргументах enum → `CachedFilter` (31 + ItIsHive), отладочный вывод в Bezlikie,
регрессионный тест `tests/test_ai_diplomat.py`.

## B. Проверено — проблем нет
- Целочисленное деление: в integer-параметры нативов дробь не попадает (везде `R2I`). Есть только
  смысловые расхождения с JASS в сравнениях вида `count < i / 35` (низкий приоритет).
- `math.random`/`os.time` в логике нет; `os.clock` только в профайлере ИИ.
- `GetLocalPlayer` — только UI и запись файлов моста.
- `pairs()` — по таблицам с целыми ключами (детерминированно).
- Дубль `aiUnitJoinsArmy` (`libraries` + `83_ai_brain.lua`) — намеренная обёртка.
- `ExecuteFunc` (5 мест) — осмысленно; `UnitAlive` переопределён полифиллом.
- `Portal_Periodic` (1/32 с) — локации освобождаются, триггер выключается без путешественников.

---

## C. Что ещё не сделано в аудите

1. ~~`init_smoke.py`~~ — работает (лимит инструкций `__guarded`, ~15 мин): 2364 колбэка, 6 ошибок —
   все артефакты стенда (порядок инициализации массивов, циклы поиска позиций на заглушках).: стенд падал на `Player(PLAYER_NEUTRAL_PASSIVE)` — константы вида
   `= GetPlayerNeutralPassive()` не вычислялись. Подготовленный, но не применённый фикс: определить
   `GetPlayerNeutralPassive/Aggressive`, `GetBJMaxPlayers` и др. до констант и исполнять прочие
   константы как выражения (`null`→`nil`). Затем прогнать `main()` + все колбэки и разобрать ошибки.
2. **Утечки** — периодические разобраны (RRR, Spell_Dvij/E_Dvij, Sand Strike, ResoursesInterface,
   ItemLitter — ок). **Осталось:** ~71 разовая утечка `GetUnitLoc/PolarProjectionBJ/GetSpellTargetLoc`,
   переданных прямо в аргументы (больше всего: `05_common_spells`, `15_ai_portals_cities`,
   `14_misc_system`, `OldGods`, `Lords`). Исходное описание (`leak_audit.py`): 126 функций с дисбалансом (55 по локациям, 73 по группам). Разобрать
   те, что вызываются из периодических таймеров: `Sand_Strike_Loop` (0.04 с), `ResoursesInterface_Copy`
   (0.1 с), `HandleCounter` (0.05 с), таймеры спеллов 0.02–0.055 с (`07_mixed_heroes`, `Bezlikie`),
   `ItemLitterCleanup`. Остальное — разовые утечки на касте (средний приоритет).
3. Ручное чтение ключевых модулей на логику: `01_core_economy`, `02_game_modes`, `83_ai_brain.lua`
   (4100 строк), `84_ai_diplomat.lua`, `06_transport_portals.lua`.
4. ~~Детектор «`local` внутри блока, используется снаружи»~~ — сделан `scope_leak_audit.py`;
   на текущем коде только ложные срабатывания (11). Сделан `closure_nil_audit.py` (см. A+).
5. ~~Производительность~~ (кольцевой буфер сделан). Осталось: при включённом flush каждая запись
   переписывает весь `.pld` (2000 строк Preload) — дорого в горячих путях. Было: `ProbeLogWrite` делает `table.remove(lines, 1)` на массиве из 2000 строк при
   каждом вызове (O(n)) — заменить кольцевым буфером; проверить, сколько логов идёт в горячих путях ИИ.
6. Архитектура (рекомендации для отчёта): единый слой фильтров-boolexpr с кэшем, отказ от глобальных
   скретч-групп во вложенных вызовах, защита периодических триггеров через `safeCall`, удаление мёртвого
   кода конвертации, флаг отладки для моста. Сверить с планами в `docs/AI_OVERHAUL_PLAN.md`.
7. **Следующий шаг:** проверка в игре (probe-map) — особенно legacy-атака ИИ, флот, спеллы с таймерами,
   Изумрудный сон/порталы, MeatDeal/BoneDeal, Песчаный удар; затем `git push` (с согласия пользователя).
   Было: после исправлений: `python build_map_lua.py`, проверка luaparser, `python -m unittest discover -s tests`,
   повторный прогон анализаторов, проверка в игре (probe-map), коммиты и `git push`.

## D. Окружение (сделано в этой сессии)
- Репозиторий склонирован в `F:\Gemini_23Race`; git авторизован в GitHub (аккаунт Ageron-Vellani,
  push проверен `--dry-run`); автор коммитов `Ageron-Vellani <dragolegg@gmail.com>` (локально в репо).
- Созданы `CLAUDE.md` и проектные скиллы `.claude/skills/` (`wc3-lua-debug`, `wc3-live-bridge`,
  `wc3-ai-brain`, `wc3-map-systems`) — **не закоммичены**, как и этот файл и `scripts/audit/`.
