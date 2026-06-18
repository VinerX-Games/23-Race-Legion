# AI Brain Optimization & Improvement Vectors

## Текущее состояние (после unified brain tick)

**Архитектура**: один `TimerSmall2` → `PlayerGet1` → `PlayerArmy` (N ботов/тик) → `AiBrainArmyTick`.
В brain-режиме (`race.brain="objective"`) активны только 2 таймера:
- `TimerSmall2` — планировщик (feed PlayerGet1 раз в ~2с)
- `TimerSmall3` — только PereborNavalBases (флот)
- `TimerSmall`, `TimerSmall4` — отключены

**Проблема**: раз в ~4 секунды сильный пролаг (пиковая нагрузка), вместо распределённых микролагов.

---

## 1. Build Pipeline — ускорение стройки

### 1.1 Pre-computed Building Grid (самое важное)

**Сейчас**: `AiFindBuildSpot` делает 6 колец × 12 секторов = 72 луча на каждую попытку стройки.
Каждый луч вызывает `IsTerrainPathable` + `EnumDestructablesInRange` + проверку occupied.

**Предложение**: предвычислить сетку строительных клеток.

```
Карта: например 256×256 клеток.
Шаг сетки: AiBuildingRadius × 2 (~512 единиц).
При загрузке (или on-demand): для каждой клетки храним:
  - pathable: bool (террайн проходим?)
  - water: bool (вода?)
  - occupied: unit|nil (здание на клетке)

При старте бота: от его столицы делаем BFS по сетке, помечаем "свободные строительные пятна".
При постройке здания: помечаем клетку + соседние как occupied.
При разрушении: обратно.

TryBuild: берём ближайшее свободное пятно из кеша → O(1).
```

**Выигрыш**: 72 луча → 1 lookup. ~70× быстрее на операцию стройки.

**Нюансы**:
- Размеры зданий разные (2×2, 4×4, 6×6 клеток). Кеш должен учитывать footprint.
- Collision с destructables (деревья, камни) — нужен EnumDestructablesInRange при первом проходе.
- Можно сделать lazy: не всю карту, а expanding ring от капитала, кешировать по мере расширения.

**Реализация**: создать модуль `AiBuildingGrid`:
```lua
AiBuildingGrid = {
    cellSize = 512,
    -- [cellKey] = { pathable=true, water=false, occupiedBy=nil, footprint=0 }
    -- cellKey = math.floor(x/cellSize) * 10000 + math.floor(y/cellSize)
}
```

### 1.2 Batch TryBuild

**Сейчас**: `BrainBuild` вызывает `TryBuildWithType` для 1 здания за раз, ждёт завершения.

**Предложение**: за один тик слать ордера на 3-5 зданий разным рабочим.
- `AiFindFreeWorker` → возвращает не одного, а N свободных рабочих.
- Для первых N непостроенных зданий из `buildOrder`: рабочий + тип → `IssueBuildOrderById`.
- Не ждать завершения — стройка идёт параллельно.

**Текущий лимит**: `AiBrainMaxBuild = 3` — достаточно.

### 1.3 Expansion State Machine

**Сейчас**: `BrainExpandDecision` раз в 30 тиков шлёт рабочего в случайную точку на `AiBuildingRadius * 7` от столицы. Без гарантии что там можно строиться.

**Предложение**: FSM экспансии:
```
Состояния: idle → scouting → seeding → growing → established
- idle: нет нужды в экспансии (достаточно ресурсов у столицы)
- scouting: послать разведчика проверить регион (проверка grid)
- seeding: послать 3-5 рабочих + построить seed building (town hall)
- growing: строить production buildings у нового кластера
- established: кластер самостоятельный, можно следующий
```

**Триггеры перехода**:
- `idle → scouting`: armyCount > 50 ИЛИ gold > 10000 ИЛИ все локальные пятна заняты
- `scouting → seeding`: grid показывает ≥10 свободных клеток в радиусе 2000
- `seeding → growing`: seed building построен
- `growing → established`: ≥5 production buildings у кластера

### 1.4 Worker Routing

**Сейчас**: `AiFindFreeWorker` берёт первого попавшегося из `builders/buildersT/harvest`.

**Предложение**: nearest-worker-to-build-spot.
```lua
function AiFindNearestWorker(pi, x, y)
    -- ищем в builders, buildersT, harvest
    -- возвращаем ближайшего к (x,y)
end
```
Выигрыш: рабочий быстрее доходит до места стройки → быстрее начинает строить.

---

## 2. Кеширование (CPU)

### 2.1 Production Mapping Cache

**Сейчас**: `BrainProduce` для каждого unitId из `compTarget` сканирует ВЕСЬ `race.production` в поисках здания.

**Предложение**: построить обратный индекс ОДИН раз при старте расы:
```lua
AiUnitToBuilding[raceKey] = {
    [unitId] = { bldType, row },  -- "какое здание + какая строка производит этого юнита"
}
```

**Выигрыш**: N×M lookup → O(1) на каждый unit.

### 2.2 Objective Distance Cache

**Сейчас**: `AiObjScore` пересчитывает расстояния каждый тик для всех objective.

**Предложение**: кешировать `obj.dist` при сборе objectives, обновлять только при движении капитала/армии.
- При `AiBrainCollectObjectives`: вычислить dist один раз.
- На следующих тиках: `if capMoved then recalc end`.
- Для proximity bonus (capture): тоже кешировать `obj.nearbyEnemyCount`.

### 2.3 Squad Centroid Cache

**Сейчас**: `AiGroupCentroid(sq.members)` пересчитывается при каждом доступе.

**Предложение**: хранить `sq._cx, sq._cy` в самом squad, обновлять при:
- `GroupAddUnit` / `GroupRemoveUnit` → флаг dirty
- При чтении: если dirty → пересчитать, иначе вернуть кеш.

### 2.4 Что НЕЛЬЗЯ кешировать

- **AiFindBuildSpot успехи**: если место занято — оно занято навсегда (пока здание не снесут). Не кешируем успехи, только pre-computed grid (см 1.1).
- **Живые unit handles**: становятся невалидными при смерти юнита. Всегда проверять `GetUnitState > 0.405`.

---

## 3. Production Intelligence

### 3.1 Resource Guard

**Сейчас**: `BrainProduce` не проверяет золото/дерево. Может заказать юнита, на которого нет ресурсов → ордер молча фейлится.

**Предложение**:
```lua
local gold = GetPlayerState(Player(pi), PLAYER_STATE_RESOURCE_GOLD)
local lumber = GetPlayerState(Player(pi), PLAYER_STATE_RESOURCE_LUMBER)
if gold < unitGoldCost or lumber < unitLumberCost then
    goto skipUnit  -- не тратим ордер впустую
end
```

Нужна таблица стоимостей юнитов (`AiUnitCosts[unitId] = {gold, lumber}`) — либо вычислять через `BlzGetUnitGoldCost` / `BlzGetUnitWoodCost`.

### 3.2 Dynamic compTarget

**Сейчас**: `compTarget` статичен (задан в коде расы).

**Предложение**: адаптировать под врага.
- Сканировать вражескую армию (юнит-типы в радиусе от фронта).
- Если враг имеет много ranged → увеличить долю щитов/кавалерии.
- Если враг имеет много воздуха → увеличить долю anti-air.
- Формула: `adjustedTarget = baseTarget + enemyBias * 0.3`.

**Частота обновления**: раз в 30-60 brain-тиков (не каждый тик).

### 3.3 Building Queue Depth

**Сейчас**: один ордер = один юнит, тут же.

**Предложение**: здание может иметь очередь глубиной до 3.
- Если здание уже тренирует юнита — не слать новый ордер (он проигнорируется).
- Отслеживать `g_AiOrdered[key]` но с тайм-аутом (когда юнит дотренируется, сбросить).

### 3.4 Tech Gate

**Сейчас**: tier2 юниты в `production` имеют `gate = "tier2"`. В старом Perebor проверялось через `def.gates[row.gate](pi)`.

**Предложение**: в `BrainProduce` добавить проверку gate:
```lua
if row.gate then
    local gateFn = race.gates and race.gates[row.gate]
    if gateFn and not gateFn(pi) then goto skipUnit end
end
```

---

## 4. Combat Intelligence

### 4.1 Split Focus

**Сейчас**: `BrainFocus` шлёт ВСЮ армию на ОДНУ точку (best objective). Тратит силы впустую если 200 юнитов бегут убивать 3 крипов.

**Предложение**: распределить армию на top-2 или top-3 objectives.
- `BrainPickFocuses(pi, wm, 3)` → возвращает топ-3 цели.
- Разделить `udg_Ai_army[pi]` пропорционально score:
  - 60% на цель №1, 25% на №2, 15% на №3.
- Или: отправить ближайшие N юнитов на каждую цель.

### 4.2 Retreat Logic

**Сейчас**: `wm.defendHome` форсирует retreat всех squads к столице. Но нет retreat от проигрышного боя.

**Предложение**: перед фокус-ордером проверить соотношение сил у цели:
```lua
local enemyPower = AiEnemyPowerAround(p, focus.x, focus.y, 1500)
local myPower = wm.armyCount * avgUnitPower
if enemyPower > myPower * 1.5 then
    -- цель слишком сильная — ищем более слабую
    focus = nextBestFocus
end
```

### 4.3 Squad-Level Focus

**Сейчас**: squads только трекаются (назначение + reaping), но не используются для ордеров.

**Предложение**: вернуть per-squad ордера БЕЗ FSM (только прямая директива из мозга):
```lua
for _, sq in pairs(AiSquadsOf(pi)) do
    local target = AiPickSquadTarget(pi, sq, wm)  -- ближайшая цель
    if target then
        AiSquadOrderAtk(sq.members, target.x, target.y)
    end
end
```

Нет стейт-машины (muster/march/engage/retreat) → нет краша. Просто назначаем каждой группе свою цель.

### 4.4 Capture Point Priority

**Сейчас**: capture имеет score `60 + 4000/dist`. Не учитывает HP точки.

**Предложение**: приоритет точкам с низким HP (почти захваченным):
```lua
if o.kind == "capture" then
    local hpPct = o.hp / o.maxHp
    o.score = (60 + 4000 / dist) * (1 + (1 - hpPct))  -- ×2 если HP=0
end
```

---

## 5. Остатки GroupEnum → добить до нуля

### 5.1 AiBrainPerceive (угрозы)

**Сейчас**: `GroupEnumUnitsInRange` для enemy power у столицы и фронта.

**Предложение**: power-map кеш.
- Разбить карту на зоны (например 3000×3000).
- При perceiving: обновить зоны где есть враги.
- При чтении enemyPower: сумма по зонам в радиусе.
- `GroupEnumUnitsInRange` → lookup в power-map (для чтения), но всё ещё нужен для записи.

### 5.2 AiBrainCollectObjectives

**Сейчас**: `GroupEnumUnitsOfPlayer(neutralPassive, nil)` для поиска capture points.

**Предложение**: кешировать список capture points при старте карты.
- Все точки известны заранее (предрасставлены на карте).
- Обновлять только при смене владельца (событие захвата).
- `GroupEnumUnitsOfPlayer` → итерация статического списка + проверка владельца.

### 5.3 AiBuyPirateFleet

**Сейчас**: 3× `GroupEnumUnitsOfPlayer(p, nil)` для:
- hasUnitNear (есть ли юнит у порта)
- отправить ближайшего юнита к порту
- найти купленный корабль

**Предложение**: итерация `udg_Ai_units[pi]` вместо enum.
- hasUnitNear: итерация по `udg_Ai_units[pi]`, проверка дистанции до порта.
- send nearest: та же итерация, `IssuePointOrder`.
- find bought ship: `GroupEnumUnitsOfPlayer` всё равно нужен для поиска нового юнита (он только что создан). Альтернатива: events.

---

## 6. Архитектурное

### 6.1 Per-bot Throttle

**Проблема**: когда все N ботов обрабатываются в одном `PlayerGet1` fire, пиковая нагрузка создаёт пролаг.

**Предложение**: ввести паузу между ботами в батче.
```lua
for each bot in batch:
    AiBrainArmyTick(pi, p)
    TriggerSleepAction(0.0)  -- yield to engine (1 frame)
```

Или: уменьшить `AiBrainBatchSize` если CPU высокий (адаптивно).

### 6.2 Слить Strateg в мозг

**Сейчас**: `AiTimerStrateg` (период ~15с) отдельно инжектит золото/дерево и делает grade bonuses.

**Предложение**: перенести инжект в `AiBrainArmyTick` по модулю:
```lua
if wm.tick % strategInterval == 0 then
    AiInjectResources(pi, wm)
end
```

Убрать отдельный таймер. Один источник истины для всех AI-операций.

### 6.3 Дипломат батчинг

**Сейчас**: `AiDiplomatTick(pi)` вызывается каждый 4-й brain-тик ПЛЮС в `PlayerArmy` для swarm-ботов.

**Предложение**: вынести дипломата на глобальный цикл (не per-bot).
- Раз в N секунд: обработать ВСЕХ ботов дипломата за один проход.
- Не привязано к brain-тику конкретного бота.

### 6.4 AiBrainPerceive Throttle

**Сейчас**: `AiBrainPerceive` вызывается каждый brain-тик. Обновляет wm.armyCount, wm.enemyPower, и т.д.

**Предложение**: полный perceive раз в 2-3 тика, лёгкий — каждый тик.
- Полный: обновить enemy power map, пересчитать objectives.
- Лёгкий: только `armyCount = BlzGroupGetSize(udg_Ai_army[pi])`.

---

## Приоритеты (что делать в каком порядке)

| № | Вектор | Влияние на лаг | Влияние на ум | Сложность |
|---|--------|----------------|---------------|-----------|
| 1 | Pre-computed build grid (1.1) | **-70% build CPU** | стройка в 10× быстрее | средняя |
| 2 | Prod mapping cache (2.1) | -5% tick CPU | — | низкая |
| 3 | Per-bot throttle (6.1) | **убирает пролаг** | — | низкая |
| 4 | Objective cache (2.2) | -10% perceive CPU | — | низкая |
| 5 | Resource guard (3.1) | — | не тратит ордера впустую | низкая |
| 6 | Split focus (4.1) | — | армия эффективнее | средняя |
| 7 | Expansion FSM (1.3) | — | expansion умный | высокая |
| 8 | Pirate enum → local group (5.3) | -5% naval CPU | — | низкая |
| 9 | Dynamic compTarget (3.2) | — | контрит врага | средняя |
| 10 | Merge Strateg (6.2) | -1 таймер | — | низкая |

---

## Профайлер: замеры времени в лайве

### Как это работает

`AiBrainArmyTick` оборачивает каждую секцию в замер через `os.clock()`:

```lua
local t0 = os.clock()
AiBrainPerceive(pi)    -- perceive
d.s[1] += (os.clock() - t0) * 1000

t0 = os.clock()
BrainProduce(...)      -- produce
BrainBuild(...)        -- build
d.s[2] += (os.clock() - t0) * 1000

t0 = os.clock()
AiSquadReapDead(pi)    -- squad
d.s[5] += (os.clock() - t0) * 1000

t0 = os.clock()
BrainFocus(...)        -- focus
d.s[6] += (os.clock() - t0) * 1000
```

Каждые `AiProfileEvery` (30) тиков бота — дамп в лог через `AiBrainLogAppend`.

### Секции профайлера

| Индекс | Секция | Что измеряет |
|--------|--------|-------------|
| s[1] | perceive | AiBrainPerceive (wm, dead cleanup, power count) |
| s[2] | produce+build | BrainProduce + BrainBuild |
| s[3] | objectives | AiBrainCollectObjectives |
| s[4] | legacy | AiArmyLegacyTick (fallback) |
| s[5] | squad | AiSquadReapDead + orphan assign |
| s[6] | focus | BrainFocus (army group iterate + orders) |
| s[7] | other | naval, pirate, diplomat |

### Чтение через бридж

```python
# сбросить данные
agent_bridge.py exec "AiProfileData={}; return'ok'"

# через N секунд — снять
agent_bridge.py exec "local d=AiProfileData[8]; if d then local s=d.s; return string.format('t=%d P=%d PB=%d SQ=%d F=%d O=%d', d.ticks, (s[1]or 0)/d.ticks, (s[2]or 0)/d.ticks, (s[5]or 0)/d.ticks, (s[6]or 0)/d.ticks, (s[7]or 0)/d.ticks) end"
# → "t=12 P=0 PB=2 SQ=1 F=4 O=0"
```

### Лог-буфер

`AiBrainLogBuf` аккумулирует сообщения через `AiBrainLogAppend(msg)`. 
Flush — в конце `PlayerArmy` через `AiBrainLogFlush()`. 
Максимум строк до принудительного flush: `AiBrainLogMaxLines` (64).

Заменяет прямой `ProbeLogWrite` — убирает накладные расходы на частые записи в прелоадер.

### Результаты замеров (batch=1, период=1с, 16 ботов)

| Секция | ms/тик | Примечание |
|--------|--------|-----------|
| perceive | ~0 | быстрый, только group size |
| produce+build | ~2 | compTarget lookup + building scan |
| objectives | ~7 | кластеризация целей |
| squad | ~1 | reaping dead units |
| focus | ~3 | итерация army group + order |
| **Итого** | **~12** | влезает в кадр (16ms) |

**Исторически** (с SQDBG логами + GroupEnumUnitsOfPlayer): **115ms** на бота.
Логи съедали ~100ms.


**Первая фаза (ближайшая)**: №1 + №2 + №3 — максимальный прирост производительности.
