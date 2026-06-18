# План рефакторинга AI-блока (расы)

Статус: предложен, утверждён к исполнению (все 3 фазы). Исполняется по мере лимитов.

## Зачем

Добавление одной расы сейчас требует ~14 правок в разных местах: блок функций
расы + случайный выбор расы + 11 параллельных цепочек `if AiRace[pi]=="X" then
Fn_X(...)`. Все цепочки одинаковой формы, отличается только имя функции. Это
ручное копирование диспетча на каждую расу — легко забыть ветку (прошлый агент
определил функции Jungle Trolls, но не подключил ни одной ветки диспетча).

Цель: добавление расы = 1 правка (написать функции расы + один вызов
`RegisterAiRace`). Диспетч-сайты не трогаются никогда.

## Канонические факты сборки (не нарушать)

- Источник истины Lua: `map.w3x/_lua/monolith_split/sections/` + `manifest.json`.
- Сборка: `python build_map_lua.py` -> `map.w3x/war3map.lua` (конкатенация
  секций по манифесту). Правки только в split, не в собранном монолите.
- Проверка синтаксиса без WC3: `pip install luaparser`, затем
  `luaparser.ast.parse(open('map.w3x/war3map.lua').read())`.
- Проверка в игре: `HiveWE_cli probe-map --map map.w3x --warcraft "F:/Games/Warcraft III"
  --keep-open --click-after 45 --chat-script "120:-ai2 jt" --probe-log 23Race_probe_log.pld`.
- Каждый шаг рефактора: rebuild -> luaparser -> (по возможности) probe-map.

## Текущая архитектура AI (до рефактора)

- `libraries/13_Races.lua` — per-race функции: `start<Race>`,
  `ChooseBuildings_<Race>`, `PereborBuildings2_<Race>`, `Join_<Race>`,
  `Strateg_<Race>`, `Strateg_<Race>_EC`, `Attacker_<Race>`, `Attacked<Race>`,
  `GetLvl<Race>`, `Upgrade<Race>`, `aiNavalTrain_<Race>`.
- `libraries/14_AI2.lua` — `createAiPlayer(pi, raceToken)` (выбор расы),
  `StartAiRaceByToken`.
- `80_generated_runtime.lua` — диспетч-сайты (per-tick), привязанные к
  `AiRace[pi]` строковому ключу. Сайты:
  1. ChooseBuildings (`gInt = ChooseBuildings_<Race>(gPi)`)
  2. aiUnitJoins (`Join_<Race>(id, pi, u)`)
  3. blocked-wall (`IssueBuildOrderById(gUnit, FourCC('...'), gX2, gY2)`)
  4. PereborBuildings (`PereborBuildings2_<Race>(gId, gPi, gUnit)`)
  5. naval (`aiNavalTrain_<Race>(u, pi)`)
  6. Strateg_EC (`Strateg_<Race>_EC(id)`)
  7. Strateg (`Strateg_<Race>(i, pi, p)`)
  8. Attacker (`Attacker_<Race>(id, gAttacker, gTarget, gPlayer)`)
  9. Attacked (`Attacked<Race>(gAttacked)`)
  10. GetLvl (`GetLvl<Race>(u)`)
  11. Upgrade (`Upgrade<Race>(gPi, gId)`)

Расы: Scarlet, BloodElves, Goblins, Naga, Horde, JungleTrolls.
Заметки совместимости: Horde переиспользует `Attacker_Goblins`/`AttackedNaga`;
Scarlet+BloodElves делят wall `h011` и `aiNavalTrain_Common`. Реестр это
выражает через поля (поле просто указывает на общую функцию/значение).

---

## Фаза 1 — Реестр + табличный диспетч (низкий риск)

Новая секция `81_ai.lua` (манифест: после `80_generated_runtime`, до
`90_InitCustomTriggers`). Содержит реестр, резолвер и хелперы. Тела функций
остаются в `13_Races.lua`. Строковые ключи `AiRace[pi]` не меняются ->
поведение идентично.

### Структура записи расы

```lua
RegisterAiRace("JungleTrolls", {
    tokens      = {"jt", "jungletrolls", "trolls"}, -- для "-aiN <race>" / bridge
    weight      = 1,                                 -- вес в случайном пуле (0 = только вручную)
    start       = startJungleTrolls,                 -- (pi)
    chooseBuild = ChooseBuildings_JungleTrolls,      -- (pi) -> id
    perebor     = PereborBuildings2_JungleTrolls,    -- (id, pi, u)
    join        = Join_JungleTrolls,                 -- (id, pi, u)
    strateg     = Strateg_JungleTrolls,              -- (i, pi, p)
    strategEC   = Strateg_JungleTrolls_EC,           -- (id)
    attacker    = Attacker_JungleTrolls,             -- (id, u, target, p)
    attacked    = AttackedJungleTrolls,              -- (u)
    getLvl      = GetLvlJungleTrolls,                -- (u)
    upgrade     = UpgradeJungleTrolls,               -- (pi, id)
    naval       = aiNavalTrain_JungleTrolls,         -- (u, pi)   (опц.)
    wall        = FourCC('h0N2'),                    -- застройка перекрытого пути (опц.)
})
```

### Хелперы (81_ai.lua)

```lua
AiRaces = AiRaces or {}
AiRaceTokens = AiRaceTokens or {}
function RegisterAiRace(key, def) ... end          -- кладёт в AiRaces, индексирует tokens
function AiRaceOf(pi) return AiRaces[AiRace[pi]] end
function AiRaceByToken(tok) ... end                -- nil/неизвестно -> nil
function AiRacePickRandom(pi) ... end              -- по weight
```

### Конверсия диспетч-сайтов

Каждая цепочка `if/elseif` -> 1-2 строки:
```lua
local r = AiRaceOf(pi)
if r and r.strateg then r.strateg(i, pi, p) end
```
blocked-wall/naval — через поля `r.wall` / `r.naval`, OR-группы исчезают.
`createAiPlayer` и `StartAiRaceByToken`/bridge резолвятся через реестр.

### Порядок исполнения Фазы 1

1. Создать `81_ai.lua` (реестр+хелперы), добавить в `manifest.json`.
2. `RegisterAiRace` для всех 6 рас.
3. Конвертировать 11 диспетч-сайтов на месте (по одному, rebuild+parse после
   каждого), затем `createAiPlayer`/token-резолв.
4. probe-map: `-ai2 jt`, `-ai3 be`, `-ai4 horde` — проверить старт и тик.

Результат: добавление расы становится O(1). Полностью обратимо.

---

## Фаза 2 — Перенос тел в AI-секцию

- Перенести per-race тела (`13_Races.lua`) и `createAiPlayer` в `81_ai.lua`
  (или в per-race файлы `libraries/races/<race>.lua`, подключённые манифестом).
- Ключи `AiRace[pi]` и сигнатуры функций не меняются -> поведение идентично.
- Риск: вырезание из 47k-строкового файла. Делать пофункционально, каждый
  перенос верифицировать rebuild+parse, в конце probe-map по каждой расе.

---

## Фаза 3 — Декларативные данные вместо процедур (крупная)

`ChooseBuildings`/`Perebor`/`Strateg` — в основном данные (списки зданий,
лимиты, веса юнитов, тех-пороги). Перевести в таблицы, исполняемые одним
generic-движком.

### Эскиз данных

```lua
RegisterAiRace("JungleTrolls", {
  ...
  buildings = {                       -- бывш. ChooseBuildings: id, limit, power
    { FourCC('h0N5'), 4, 4 }, { FourCC('h0N2'), 18, 4 },
    { FourCC('h0MY'), 10, 4 }, { FourCC('h0N3'), 5, 2 }, { FourCC('h0N0'), 3, 6 },
    -- условные: gate = function(pi) return getAiCount(...)>=1 end
  },
  production = {                      -- бывш. Perebor: что строит каждое здание
    [FourCC('h0MY')] = { {FourCC('o04M'),5}, {FourCC('o04L'),4},
                          {FourCC('o05E'),1, gate=...} },
    [FourCC('h0N0')] = { heroes = {FourCC('O054'),FourCC('O05A'),FourCC('O05D'),
                          branch={black=FourCC('O05L'), other=FourCC('O055')}} },
    ...
  },
  research = {                        -- бывш. Strateg: building -> {upgrades}, пороги по i
    { after=17, pick=1, from={ {FourCC('h0N3'), {FourCC('R0I8'),FourCC('R0I9'),...}}, ... } },
    { after=45, from={ {FourCC('h0D3'), {FourCC('R005'),...}} } },
  },
  techUp = { {after=25, from=FourCC('h0N5'), to=FourCC('h0N1'), cap=3},
             {after=55, from=FourCC('h0N1'), to=FourCC('h0N6'), cap=3} },
  heroSkills = { [FourCC('O054')] = {ult={6,10,FourCC('AOsw')}, pool={...}}, ... },
})
```

### Generic-движок (81_ai.lua)

`AiRunChooseBuildings(pi)`, `AiRunProduction(id,pi,u)`, `AiRunStrateg(i,pi,p)`,
`AiRunGetLvl(u)` — интерпретируют таблицы выше. Спец-логика (берсерк/хекс у
Attacker, кастомные ветки) остаётся функциями-хуками в записи расы.

### Порядок

1. Движок + конверсия эталонной расы (Jungle Trolls) -> данные. Сравнить
   поведение с процедурной версией (probe-map, лог действий AI).
2. По одной мигрировать остальные расы; held-out проверка каждой.
3. Удалить процедурные `ChooseBuildings_*`/`Perebor_*`/`Strateg_*` после
   подтверждения паритета.

### Выгода

- Авторинг AI = чистые данные.
- Прямая связка с `HiveWE_core` `RaceGraph` / `describe-race`: тот же граф
  найма/тех-дерева. `// TODO ui`: редактор сможет читать/рисовать/править эти
  таблицы напрямую (дерево найма в интерфейсе).

---

## Сопутствующая уборка

- Удалить осиротевший драфт `lua_rewrite/output/` (не участвует в сборке,
  не читается `build_map_lua.py`). Перед удалением — убедиться, что ничего из
  него не нужно перенести в split.

## Чек-лист на каждый шаг

- [ ] `python build_map_lua.py`
- [ ] luaparser parse OK
- [ ] probe-map: старт без Lua/init ошибок
- [ ] probe-map: целевые расы спавнятся и тикают (`-aiN <race>`)
