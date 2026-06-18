# Хендофф: дорефакторить AI (Phase 3) и добрать расы

Карта: `C:\Games\23 Race\23-Race-Legion\map.w3x`. ИИ-расы переводятся на
**данные** (декларативные таблицы) + один generic-движок. Phase 1 (реестр) и
часть Phase 3 (ChooseBuildings) готовы. Ниже — что делать дальше.

## ⚠️ ПЕРВЫМ ДЕЛОМ (незакоммиченное!)
Я только что перевёл `ChooseBuildings` всех 6 рас на данные в `81_ai.lua`, но
**НЕ успел пересобрать/проверить/закоммитить**. Сделай немедленно:
```
cd "C:\Games\23 Race\23-Race-Legion"
python build_map_lua.py
python -c "import luaparser.ast as a; a.parse(open(r'map.w3x/war3map.lua',encoding='utf-8').read()); print('LUA OK')"
```
Если LUA OK — проверь паритет (см. «Мост» ниже): для каждой расы набор
кандидатов из движка `AiRunChooseBuildings(pi, AiRaces.<Race>)` должен совпадать
с процедурной `ChooseBuildings_<...>(pi)`. Затем `git add -A && git commit`.

## Канон сборки (НЕ нарушать)
- Правки ТОЛЬКО в `map.w3x/_lua/monolith_split/sections/**`, потом
  `python build_map_lua.py` → собирает `map.w3x/war3map.lua`. Собранный монолит
  руками не трогать.
- После каждого шага: rebuild → luaparser → (по возможности) проверка мостом.
- Расы регистрируются в `sections/81_ai.lua` через `RegisterAiRace(key, def)`.
  Тела процедур пока в `sections/libraries/13_Races.lua`.

## ГЛАВНЫЙ ИНСТРУМЕНТ: живой мост (без перезапуска карты!)
Исполняет произвольный Lua в УЖЕ запущенной игре и возвращает значения. Это
ускоряет всё в разы. Подробно: `LIVE_AGENT_BRIDGE.md`. Кратко:
```
# поднять карту (держать открытой), один раз:
"C:\Games\HiveWE_VinerX_Edition\build\Release\Release\HiveWE_cli.exe" probe-map \
  --map "C:\Games\23 Race\23-Race-Legion\map.w3x" --warcraft "F:/Games/Warcraft III" \
  --keep-open --wait 90 --click-after 50 --probe-log 23Race_probe_log.pld
cd "C:\Games\23 Race" && python agent_bridge.py reset
# гнать любой Lua и читать результат:
python agent_bridge.py exec "return AiRace[6]"
python agent_bridge.py exec --file snippet.lua
```
Печатает `OK <val>` / `ERR <msg>` / `TIMEOUT` (таймаут на тяжёлой игре бывает —
просто повтори). Спавн бота расы: `python agent_bridge.py exec "createAiPlayer(8, 'jt')"`.
**Можно горячо переопределять функции** в работающей игре (проверить фикс до
пересборки): `exec "function Foo() ... end"`.

Шаблон паритет-проверки (сравнить движок с процедуркой):
```lua
local pi=20
local function snap() local t={} for k=1,tArray[0] do t[#t+1]=tArray[k] end table.sort(t) return table.concat(t,',') end
ChooseBuildings_BloodElves(pi); local a=snap()
AiRunChooseBuildings(pi, AiRaces.BloodElves); local b=snap()
return 'match='..tostring(a==b)
-- для рас с гейтом сначала выстави условие через SaveInteger(AiData, pi, FourCC('...'), 1)
```

## Что уже сделано (контекст)
- Починены 4 сломанных натива (vJASS→Lua пустые stub'ы, тенили движковые
  нативы → nil): `UnitAlive` (реальное тело по жизни) + `GetUnitGoldCost`/
  `GetUnitWoodCost`/`GetPlayerUnitTypeCount` (через `X = X or fallback`) — в
  `sections/02_pre_library_functions.lua`. ⚠️ Если встретишь ещё `function Имя() end`
  с комментом `(native)` — это тот же баг, чини так же.
- Армия больше не «дёргается»: вернул whitelist лени (ордера 851972/851976/0) в
  `IsAiCombatRetaskable`/`f_LazyN` (`sections/libraries/04_AI0.lua`).
- Логи приглушены: `AiProbeLogLimited` — no-op.
- **Phase 3 движок ChooseBuildings** в `81_ai.lua`: `AiRunChooseBuildings(pi,def)`
  читает `def.buildings` (строки `{id, limit, power}` + опц. `gate="имя"`) и
  `def.gates` (предикаты `function(pi)`). `AiDispatchChooseBuild` использует движок
  если есть `def.buildings`, иначе старую `chooseBuild` (безопасный фоллбэк).
  JungleTrolls уже проверен на паритет (off=21, on=34 — совпало).

---

## 2. СЛЕДУЮЩЕЕ: движок Perebor (найм) — ПОДРОБНО
`Perebor` = что КАЖДОЕ здание нанимает. Процедурки: `PereborBuildings*_<Race>(id, pi, u)`
в `13_Races.lua`. Логика везде одинаковая:
- по `id` (тип здания) собрать взвешенный список `a[]` юнит-ид (через циклы
  `for _=1,N do добавить unitId end` — N это «вес»),
- иногда условные добавления (`if getAiCount(...) >= 1`), иногда ветка расы
  (напр. `JungleTrollsBranchIsBlack(pi)` → чёрные/обычные юниты),
- спец-кейс рабочего: для зданий-ратуш `if getAiCount(worker) < cap then train worker`,
- `IssueImmediateOrderById(u, a[GetRandomInt(1,#a)])`.

### Схема данных (добавить в def расы)
```lua
production = {
  -- ключ = id здания; значение = список строк найма
  [FourCC('h0MY')] = {
    { FourCC('o04M'), 5 }, { FourCC('o04L'), 4 },
    { FourCC('o05E'), 1, gate = "tier2" },
  },
  [FourCC('h0MX')] = {
    { FourCC('o04O'), 3 }, { FourCC('o04R'), 3 },
    { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },
  },
  [FourCC('h0N0')] = { hero = true,            -- алтарь: равновероятный выбор
    { FourCC('O054') }, { FourCC('O05A') }, { FourCC('O05D') },
    { branch = "jt", black = FourCC('O05L'), other = FourCC('O055') } },
  worker = { id = FourCC('o04Q'), cap = 18,    -- ратуши тренят рабочего
            from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },
}
branches = { jt = function(pi) return JungleTrollsBranchIsBlack(pi) end }  -- хук ветки
```

### Generic-движок (в 81_ai.lua) — эскиз
```lua
function AiRunProduction(id, pi, u, def)
  local prod = def.production; if not prod then return false end
  -- рабочий
  local w = prod.worker
  if w and w.from then for _,b in ipairs(w.from) do if id==b then
    if getAiCount(pi, w.id) < w.cap then IssueImmediateOrderById(u, w.id) end
    return true end end end
  local rows = prod[id]; if not rows then return false end
  tArray[0]=0                              -- переиспользуем взвешенный буфер
  for _,row in ipairs(rows) do
    local ok=true
    if row.gate then local g=def.gates and def.gates[row.gate]; ok=(g==nil) or g(pi) end
    if ok then
      if row.branch then
        local f=def.branches and def.branches[row.branch]
        local pick = (f and f(pi)) and row.black or row.other
        AddUnit(pick, row.weight or 1)
      else
        AddUnit(row[1], row[2] or 1)
      end
    end
  end
  if tArray[0] > 0 then IssueImmediateOrderById(u, tArray[GetRandomInt(1, tArray[0])]) end
  return true
end
```
Диспетч `AiDispatchPerebor(id,pi,u)`: если `race.production` есть → `AiRunProduction(...)`,
иначе старая `race.perebor(id,pi,u)`. (`AddUnit(id, power)` уже есть в 13_Races.lua —
кладёт power копий в tArray; `tArray` глобальный.)

**Порядок:** написать движок → перевести JungleTrolls `production` (эталон,
PereborBuildings2_JungleTrolls строки 2988-3066 в 13_Races.lua) → паритет мостом
(спавни JT-бота, дай зданию приказ, сравни распределение) → остальные расы по одной.
Спец-логику, что не лезет в данные, оставляй процедурным хуком в def.

## 3. ПОТОМ: движок Strateg + ДОБОР РАС — ПОДРОБНО
### Strateg (исследования/апгрейды/тех-ап по времени)
Процедурки `Strateg_<Race>(i, pi, p)` и `Strateg_<Race>_EC(id)` — это в основном:
по тику `i` (счётчик времени) при достижении порога: выбрать здание, заказать
апгрейд/исследование или тех-ап (ратуша T1→T2→T3). Схема данных:
```lua
research = {  -- {after=порог i, from=зданиеId, pick={upgradeId,...}, cap=...}
  { after=17, from=FourCC('h0N3'), pick={FourCC('R0I8'),FourCC('R0I9')} },
},
techUp  = { { after=25, from=FourCC('h0N5'), to=FourCC('h0N1'), cap=3 },
            { after=55, from=FourCC('h0N1'), to=FourCC('h0N6'), cap=3 } },
```
Движок `AiRunStrateg(i,pi,p,def)` интерпретирует. Тех-ап делается приказом
`IssueImmediateOrderById(building, toId)`. Сначала прочитай 2-3 `Strateg_*` в
13_Races.lua и в 80_generated_runtime.lua (диспетч-сайты Strateg/Strateg_EC),
выведи общую форму, потом схему. Спец-скиллы героев (`GetLvl<Race>`) — отдельная
таблица `heroSkills` или оставить процедурным хуком `getLvl`.

### Добор рас (цель — 23 расы)
Когда все 3 подсистемы (buildings/production/research) — данные, НОВАЯ раса =
один `RegisterAiRace("Имя", { tokens=..., weight=1, start=startХ, buildings=..,
gates=.., production=.., research=.., techUp=.., wall=FourCC('..'),
attacker=.., attacked=.., getLvl=.., upgrade=.., naval=.. })`.
Шаги для каждой новой расы:
1. Узнать rawcode'ы расы. Через CLI редактора:
   `HiveWE_cli describe-race --map map.w3x --suffix "<суффикс расы из объектов>"
   --tokens "<RU>,<EN>" --warcraft "F:/Games/Warcraft III"` — выдаёт юнитов/здания
   расы (имена чинены, UTF-8). Суффикс — как у рас в object editor (напр. у троллей
   "Тролли джунглей"). Это и есть мост core-слоя к данным AI (`// TODO ui` — потом
   редактор будет рисовать дерево найма из этих же таблиц).
2. Написать `start<Раса>(pi)` (по образцу startJungleTrolls: спавн рабочих+ратуши,
   SaveInteger счётчиков, SaveStr Race).
3. Заполнить data-таблицы (buildings/production/research) rawcode'ами.
4. `RegisterAiRace`. Пересобрать. Спавнить `createAiPlayer(N,'токен')` мостом,
   смотреть: строит ли, нанимает ли, атакует ли (ордер 851983 = attack).

## Команды-памятка
- Спавн бота расы (в игре): чат `-aiN <токен>` (напр. `-ai2 jt`) ИЛИ мост
  `python agent_bridge.py exec "createAiPlayer(7,'jt')"`. Токены: jt, be, scarlet,
  goblins, naga, horde.
- Гистограмма ордеров армии (проверка, что атакует):
  `exec "local g=CreateGroup() GroupEnumUnitsOfPlayer(g,Player(N),nil) local h={} for k=0,BlzGroupGetSize(g)-1 do local u=BlzGroupUnitAt(g,k) if GetUnitMoveSpeed(u)>0 then local o=GetUnitCurrentOrder(u) h[o]=(h[o]or 0)+1 end end DestroyGroup(g) local r={} for k,v in pairs(h) do r[#r+1]=k..':'..v end return table.concat(r,' ')"`
  Ордера: 0=стоит, 851983=атака, 851986=движение, 852018=добыча.

## Уборка (низкий приоритет)
- После миграции удалить осиротевший `lua_rewrite/output/` (не в сборке).
- Когда раса полностью на данных и паритет подтверждён — можно удалить её
  процедурные `ChooseBuildings_*`/`Perebor*_*`/`Strateg_*` и поле-фоллбэк.
- Phase 2 (физpereнос тел в отдельные файлы) можно ПРОПУСТИТЬ — данные и так
  заменяют процедуры; смысла резать 47k-строчный файл нет.

## Память (важно сохранить контекст)
Заметки агента-редактора: `C:\Users\Dmitry\.claude\projects\C--Games-HiveWE-VinerX-Edition\memory\`
— особенно `live-lua-eval-bridge.md`, `ai-unitalive-bug.md`, `ai-refactor-plan.md`,
`lua-build-chain.md`, `probe-map-testing.md`.
