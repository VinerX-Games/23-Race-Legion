# 23 Race Legion — Анализ скриптов (`war3map.j`)

**Файл**: `map.w3x/war3map.j`  
**Размер**: ~62 500 строк  
**Язык**: vJASS (JASS с препроцессорными расширениями) + GUI-триггеры World Editor  
**Карта**: 60 000 × 60 000 игровых единиц (120×120 клеток), 24 игрока, 30+ рас

---

## 1. Архитектурный обзор

Скрипт представляет собой гибрид:
- **vJASS-библиотеки** (`library`/`scope`) — игровая логика, AI, экономика, спеллы
- **GUI-триггеры** (сгенерированы World Editor) — `InitTrig_*`, расовые триггеры, UI
- Комментарии и имена функций на русском языке

---

## 2. Библиотеки vJASS

### 2.1 Ядро

| Библиотека | Строки | Назначение |
|---|---|---|
| `LIBRARY_A1` | ~2545 | Фильтр `EnemEl()` — юнит не принадлежит `udg_LocalPlayer` |
| `LIBRARY_AA` | ~2553 | Пустая оболочка: глобалы `Counter`, `EnemyCapital` |
| `LIBRARY_Global` | ~2919 | Геометрия: `GetPosZ/GetUnitZ/SetUnitZ`, `DistanceBetween*`, `AngleBetween*`, `PolarProjection*`, кривые Безье 2–4 порядка, `AngleDifference`, фильтры `AvalibleUnit/Ally/Enemy`, `GroupCountUnits`, `GroupRandomUnit`, `KillDestructablesInRange`, шаблон стека через struct |
| `LIBRARY_LibNewFunctions` | ~3105 | `R2SW_Polyfill`, `DistanceBetweenUnits/Coords2/UnitsXY`, операции с группами, `Random(chance,fromAll)`, `RemoveAbilityTimed`, `AddAbilityTimed`, `RemoveEffectTimed`, `OwnCapitalInRange`, `isCapital` |
| `LIBRARY_RandomLocs` | ~3303 | `SetStartLocations()` — находит юниты `h0O1` (маркеры старта), сохраняет локации; `RandomLoc()` — возвращает случайную стартовую локацию |
| `LIBRARY_common` | ~3403 | `isEnemy()` — простой фильтр врага через `udg_LocalPlayer` |

### 2.2 AI

| Библиотека | Строки | Назначение |
|---|---|---|
| `LIBRARY_AI` | ~2556 | `turnOffAi(pi)` — отключает AI игроку, убирает из force ботов |
| `LIBRARY_AI0` | ~2572 | **Базовая AI-фильтрация**: ~20 фильтров (`f_EnemyUnit`, `f_Lazy`, `f_LazyF`, `f_LazyN`, `f_LazyW`, `f_OnlyNeaded`, `f_NavalBases`, `f_Worker`, `f_Harwest`, `f_Altars`, `f_Hero`, `f_PortB`), `MakeHash()`, `SetPortalGroup()`, `AiLimitsSet()`, расовые ID зданий для экономики |
| `LIBRARY_LibDifferentAiStuff` | ~3411 | **AI-утилиты**: `getAiCount`, `aiHasUnit`, операции `NumberAdd/Rem/Reset/ResetAll` с хешем `AiData`, `HasEnemyNear`, `ChoseRandomSpot`, `MakeTPMage` (создаёт мага массового телепорта `h07A`), `PortTo/PortToFast` (телепорт армии), `WalkPortTo`, `TryPort`, `RequestPort`, `warRace(grades,p)`, `BuildT(before,after)`, `TryBuy(p,points)`, расовые функции для BloodElves: `startBloodElves`, `Join/Attacked/Attacker/Strateg/ChooseBuildings` |
| `LIBRARY_Races` | ~3910 | **Расовая AI-система**: `AddBuilding/CheckAndAddBuilding` (выбор зданий AI), `AddUnit/CheckAndAddUnit` (тренировка юнитов), `aiOrderUnit`, `MakeGrade/CheckCap` (исследования), `aiUnitJoinsArmy/CapitalGuard`, `aiNavalTrain_Common`, `strategFleetGrades`, расовые функции для Scarlet, Goblins, Naga, Horde |

### 2.3 Спеллы и механики

| Библиотека | Строки | Назначение |
|---|---|---|
| `LIBRARY_SpellSleepAOE` | ~3342 | **Массовый сон**: дамми-юнит `u000` у `NEUTRAL_PASSIVE`, спелл героя `A06P`, дамми-каст `A06O`. Радиус по уровням: 185/275/365/430. Итерирует врагов в AoE, кастует сон на каждого |
| `LIBRARY_SanctifiedEnchantment` | ~3725 | **Система баффов**: бафф `B07Z`, скилл `A1K0`, книга `A1JU`, статус `A1JW`, сплэш `A1JX`. MAXLVL=4, длительность 40с. Использует `Global_Hash` через модуль `BindTemplate`. Отслеживает цели, длительность, смерть |
| `LIBRARY_ArmyBonus` | ~2907 | `CreateArmyBonusUnit(p)` — скрытый юнит со способностями `arb0`/`arb1` для бонусов армейского опыта |

---

## 3. Глобальные переменные (по системам)

### Экономика
```
income[24]              — золото за тик
incomeW[24]             — дерево за тик
disincome[24]           — базовое потребление (расход)
logistic[24]            — логистический налог: (500 + 100*(r-1)) / 2 * r, где r = floor(UnitsCount/25)
corruption[24]          — коррупция от технологии R04O: disincome * ((t-1) * 0.15)
balance[24]             — итоговый доход = income*(IncomeMod - AllyTax) - disincome - logistic + corruption + additional
additional[24]          — доп. расходы от техов R0DV / R0GZ
IncomeMod (real, 1.0)   — глобальный модификатор дохода
Tax (real, 0.15)        — базовый налог за юнита
AllyTax[24]             — налог союзникам
DisOn (bool)            — включено ли потребление
EcLog (bool)            — логирование экономики
udg_SET_TimerTime (25)  — интервал тика дохода в секундах
```

### Столицы / Территории
```
playerCapital[24]       — юнит-столица игрока
Capital[24]             — альтернативная ссылка на столицу
udg_StolicaGroups       — группа всех столиц
cap_time[24]            — тайминг столицы
Vassals[24]             — force вассалов на сюзерена
Senior[24]              — сюзерен игрока
CityCount               — всего контрольных точек
CityPlayerCount[24]     — точек у игрока
PercentWin (65)         — процент для победы по доминации
DipMode (2)             — режим дипломатии (1=FFA, 2=Свободная)
udg_GameMode            — режим игры (0=классика, 1=стандарт, 3/5=доминация)
```

### AI
```
udg_AiControl[24]       — управляет ли AI игроком
udg_Bots / BotsActive / BotsActiveB — force ботов
udg_Ai_units[24]        — все юниты игрока
udg_Ai_builders[24]     — рабочие
udg_Ai_buildings[24]    — здания
udg_Ai_army[24]         — боевые юниты
udg_Ai_navy[24]         — флот
udg_Ai_harvest[24]      — сборщики ресурсов
AiCapitalGuard[24]      — стража столицы (≤15)
AiCapitalBuildigs[24]   — здания у столицы
AiUnitsToPort[24]       — юниты для телепорта
AiMoney/AiMass/AiRepeat/AiRadius/AiLimit — сложность AI (7/5/5/6/150)
```

### Континенты
```
udg_Continents[8]       — флаги континентов (0=открытый мир, 1=континенты):
                        [1]=Eastern Kingdoms, [2]=Kalimdor, [3]=Outland,
                        [4]=Northrend, [5]=Pandaria, [6]=Argus, [7]=BrokenIsles+Oceania
```

### Порталы
```
udg_Portal_*            — ~40 переменных: индексы, радиус, задержка, скорость снаряда,
                          высота, активность, FX-строки, локации, конфиги, preventAllies
```

---

## 4. Хеш-таблицы

| Хеш-таблица | Назначение | Ключи |
|---|---|---|
| `Global_Hash` | Основной: таймерные эффекты, SanctifiedEnchantment, стек-шаблон | `GetHandleId(h)`, child: `10000 + JASS_MAX_ARRAY_SIZE * Key + i` |
| `AiData` | AI: учёт обученных юнитов | `(playerId, unitTypeId)` → count; `"Number"`, `"NumberGuard"`, `"NumberN"`, `"Race"` |
| `CommonHash` | Не используется (закомментирован) | — |
| `Hash` | Общий: `RemoveAbilityTimed`, `AddAbilityTimed`, `RemoveEffectTimed`, `TotalProduction` | `(pi, "Pfarm")` → счёт ферм; `(pi, "Ptier")` → тир-юнит |
| `udg_LCode` | Лобби-коды | — |

---

## 5. Игровые системы (подробно)

### 5.1 Экономика

**Поток дохода**:
1. Тикает каждые 25 секунд (`udg_IncomeTimerSecond`)
2. Первые 600 секунд: потребление отключено (`DisOn = false`)
3. После 600с: включается потребление, логистика, коррупция
4. Формула баланса:
   ```
   balance = income × (IncomeMod − AllyTax) − disincome − logistic + corruption + additional
   ```
5. **Логистика**: прогрессивный налог — чем больше юнитов, тем выше ставка (шаг 25 юнитов)
6. **Коррупция**: каждая технология `R04O` добавляет 15% от базового потребления
7. Дерево не облагается потреблением — зачисляется напрямую

**Модификаторы**: хост может установить `IncomeMod = 0.75` или `1.0` через способности

**Отслеживание**: `UnitEnterMap`, `UnitBuilded`, `UnitUpgraded` — добавляют расходы; `UnitDead` — убирает; `UnitRevive` — восстанавливает (герои: 100 золота + бонус от способности `A0ZT`)

### 5.2 Столицы (Stolica)

- **Создание**: каст `A0IQ` (MakeCapital) → `MakeCapital(u)`
- Столица получает: 10 000 HP, 30 брони, радиус обзора 750, способности `A0I6` и `A145`
- Префикс имени: `|cffd45e19Столица:|r`
- Все игроки получают shared vision на столицу
- **Особые**: Даларан (`e00C`), Наксрамас (`e00D`), Черепаха (`e00E`) — летающие/плавающие города
- **Смерть столицы**: `StolicaDead` — удаление из группы, оповещение

### 5.3 Вассалитет (Feoda)

- Игроки могут стать вассалами сюзерена
- `DoNotAttackSenior` — запрет атаки сюзерена
- `AllPlayers_and_vassals` — общее видение и договоры

### 5.4 Доминация

- Режим при `udg_GameMode == 3 or 5`
- Здания с `AHad` = контрольные точки
- Победа при захвате `PercentWin%` (по умолчанию 65%) от `CityCount`
- При 75% — предупреждение всем
- Команда `-domck` — проверка текущего счёта
- Мультиборд расширяется до 3 колонок с процентами

### 5.5 Выбор расы

**Механика**: хост кастует способность из spellbook → `EVENT_PLAYER_UNIT_SPELL_FINISH` → создаются стартовые рабочие → разблокируются технологии → селектор удаляется

**37 рас** (каждая со своим триггером `InitTrig_Race_*`):

| # | Раса | Spell ID | Стартовые юниты | Технологии |
|---|------|----------|------------------|------------|
| 1 | Bezlikie (Безликие) | `A14Z` | 5 × `h0G` | — |
| 2 | IceTrols (Ледяные тролли) | `A1EG` | 5 × `o045` | `R0L1` |
| 3 | Stromgard (Стромгард) | `A0Y0` | 5 × `h0G9` | `R0H3`, `R0HY` |
| 4 | Dragon (Драконы) | `A0RQ` | 1 × `dra1` | `R0BY` |
| 5 | Dragon2 | — | — | — |
| 6 | Argvinol (Энты) | `A0QQ` | 1 × `efon` | `R0HH` |
| 7 | Elements (Элементали) | `A0QN` | 1 случайный | `R0HI` |
| 8 | Goblins (Гоблины) | `A0MY` | 5 × `n000` | `R0K1` |
| 9 | Demon (Легион) | `A0OK` | 4 × `u005` | `R07X`, `R07K`, `R07Y` |
| 10 | Illidari | `A0OR` | 4 × `n06A` | `R0K4` |
| 11 | Bandits (Бандиты) | `A0J7` | 5 × `h017` | Набор |
| 12 | Red Orden (Алый Орден) | `A0U7` | 5 × `h061` | `R0CG` |
| 13 | Undead (Нежить) | `A02A` | 3 × `u001` | `R03X` |
| 14 | Horde (Орда) | `A0YV` | 5 × `opeo` | `Ra00` |
| 15 | Blood Elves (Эльфы крови) | `A0HQ` | 5 × `h04K` | `R07C`, `R0L0` |
| 16 | Dalaran (Даларан) | `A0HN` | 3 × `u001` | `R0BW`, `R0KK` |
| 17 | KulTiras (Кул-Тирас) | `A0HO` | 5 × `h013` | `R07D`, `R0HX` |
| 18 | Nocnorogdennue | `A0HU` | 5 × `n00M` | `R0CJ` |
| 19 | Draeneis (Дренеи) | `A0HS` | 3 × `h0O` | `R0G3` |
| 20 | Vryculs (Врайкулы) | `A0IA` | 4 × `h0GN` | `R0HU` |
| 21 | Kult Sum Molota | `A0J6` | 4 × `o049` | `R07Z`, `R03X` |
| 22 | Nerubs (Нерубы) | `A0HT` | 4 × `u00N` | `R0CI` |
| 23 | Silitids (Силитиды) | `A0HR` | 5 × `u007` | `R0CF` |
| 24 | Gnomes (Гномы) | `A0J5` | 4 × `h0G9` | `R0G5` |
| 25 | Gilneas (Гилнеас) | `A0HV` | 2 × `h0BM` | Набор |
| 26 | Nagi (Наги) | `A14O` | 1 × `n055` | `R0CI`, `R0CF` |
| 27 | Night Elf (Ночные эльфы) | `A0HL` | 1 × `ewsp` | `R03V` |
| 28 | Forsaken (Отрекшиеся) | `A0HP` | 4 × `u002` | `R0CB`, `R0CC` |
| 29 | Ogres (Огры) | `A0OR` | 4 × `o04G` | `R0KA` |
| 30 | Alliance (Альянс) | `A0I0` | 3 × `h0A2` | `R0CB` |
| 31 | JungleTrolls | `A1DZ` | 5 × `o04Q` | `R0IH` |
| 32 | FelOrk | `A1JL` | 5 × `n06B` | `R0KA`, `R0KC` |
| 33 | ForestTrolls | `A1FN` | 5 × `o04V` | `R0J1` |
| 34 | CultOfDamned | `A1HA` | 3 × `cD02` | `R0J4`, `R0J5` |
| 35 | Pandarens | `A1JM` | 4 × `o04R` | `R0IZ` |
| 36 | HordeW2 (Орда WC2) | `A1JN` | 5 × `o04Y` | `R03I`, `R03J` |
| 37 | Random | `A1JO` | Случайный набор | Случайные |

**Пагинация меню**: 4 страницы (`Page1`–`Page4`) через способности `A0I1` → `A0HZ` → `A0I0` → `A0I2`, цикл через `NextMenu`

### 5.6 Система предметов

- Стандартный инвентарь WC3: 6 слотов
- `UnitAddPowerUpItem` — временная выдача предмета (грант/удаление `AInv`)
- AI покупает предметы через `TryBuy(p, points)`
- По иконкам: шлемы, броня, оружие, кольца, обувь

### 5.7 Система тиров (T1→T2→T3)

- `udg_TierLevel[24]` — текущий тир игрока
- Переход T2: 20 ферм → апгрейд зданий
- AI: `BuildT(before, after)` — случайное здание `before` → апгрейд в `after`
- `MakeGrade` / `MakeGradeCheckCap` — AI заказывает исследования с капами

### 5.8 AI-система (подробно)

**Запуск**:
1. `aiStart()` → для каждого компьютерного игрока → `createAiPlayer(pi)`
2. Сложность обратно пропорциональна числу игроков: `AiLimit = max(70, 200-pi*5)`, `AiMass = max(8-pi, 4)`, `AiRepeat = 2+min(pi/2, 8)`
3. Таймер стратегии: каждые ~15с × `AiRepeat/5`

**Группы AI**:
| Группа | Содержимое |
|---|---|
| `Ai_units` | Все юниты |
| `Ai_builders` | Рабочие |
| `Ai_buildings` | Здания |
| `Ai_army` | Боевые юниты (кроме рабочих/зданий) |
| `Ai_navy` | Флот |
| `Ai_harvest` | Сборщики |
| `AiCapitalGuard` | Стража столицы (≤15, максимум `Number/5`) |
| `AiUnitsToPort` | Юниты для телепортации на фронт |

**AI Цикл стратегии** (по расам):
- **Выбор зданий**: `ChooseBuildings_*` — случайное следующее здание
- **Тренировка юнитов**: расовые функции + `aiNavalTrain_Common` для флота
- **Исследования**: `Strateg_*` — проверка золота, апгрейд T2/T3, покупка предметов
- **Боевые спеллы**: `Attacker_*` — каст заклинаний по типам юнитов
- **Защита**: при атаке зданий/столиц — шанс телепортировать армию
- **Телепорт**: AI создаёт TP-мага (`h07A`) у алтаря, телепортирует армию к столицам врагов
- **Grades**: `Grades[pi]` — военная мощь; `warRace` — устанавливает тех-уровень по Grades/75

**AI с полноценной поддержкой**: Scarlet, Blood Elves (наиболее полный), Goblins, Naga, Horde

### 5.9 Лобби / Стартовый поток

1. **`main()`** → `InitGlobals()` → `InitCustomTriggers()` → `RunInitializationTriggers()`
2. **`Initial_things`**: `AllPlayersStart()` — сбор игроков, `NeutralAggressive` получает 100M золота/дерева, вызов `StartInc()`, `InitThings()`, `SetStartLocations()`, скорость FASTEST
3. **`StartLobby`** (через 0.01с): случайная камера (5 вариантов), отсчёт 4с, игроки перемещаются в HostRegion, создаётся `h0GA` (лобби-юнит) на каждого, запуск 60с таймера лобби
4. **В лобби**: хост (P0) использует `NextMenu` (`A0Y5`) — 7 меню-зданий (0–6):
   - 0: `n04G` — основные настройки
   - 1: `n04D` — континенты
   - 2: `n04F` — игровые режимы
   - 3: `n04H` — дополнительные
   - 4: `n04I` — экономика (модификатор дохода)
   - 5: `n06Y` — разное
   - 6: `n074` — дипломатия
5. **`EndLobby_and_Start_game`** (по истечению `udg_LobbyTime`): создание кругов рас, очистка союзов, армейские бонусы, туман/видимость по континентам, очистка лобби-юнитов, `aiStart()`
6. Запускаются таймеры: `udg_IncomeTimerSecond` (доход), `udg_IncomeTimerFirst` (600с → потребление), `udg_TimerToDis` (диалог отсчёта)

### 5.10 Континенты

**Режимы**: Открытый мир / Континенты (выбор конкретных)

**7 континентов**:

| # | Континент | Rect | Механика |
|---|-----------|------|----------|
| 0 | Глобальный (0=открыто, 1=континенты) | — | Переключатель |
| 1 | Eastern Kingdoms | `gg_rct_EastenKingdoms` | |
| 2 | Kalimdor | `gg_rct_Kalim` | |
| 3 | Outland | `gg_rct_Outland` | |
| 4 | Northrend | `gg_rct_Nord` | |
| 5 | Pandaria | `gg_rct_Pandaria` | |
| 6 | Argus | `gg_rct_Argus` | |
| 7 | Broken Isles + Oceania | `gg_rct_BrokenIsles` | |

**Механика**: порталы отключаются (`Awrp`), игроки ограничены выбранными континентами, выход за границу → штрафная способность `A0U6`

### 5.11 Движущиеся города

- **Даларан** (`e00C`): летающий город, посадка/высадка через `DalaranOut`
- **Наксрамас** (`e00D`): летающий некрополис, та же механика
- **Черепаха** (`e00E`): гигантская морская черепаха, плавает по воде
- Все три дают способности посадки/высадки (`Ap`/`Down`)

### 5.12 Дипломатия

- **Режимы**: FFA (заблокированные союзы), Свободная дипломатия
- `DipMode` управляет: `MAP_LOCK_ALLIANCE_CHANGES`, `MAP_ALLIANCE_CHANGES_HIDDEN`, `MAP_LOCK_RESOURCE_TRADING`
- Вассалитет: `Player2VassalTo1`, `AnyPlayerVassalToFirst`

---

## 6. Заклинания на триггерах

### 6.1 Общие

| Заклинание | Способности | Описание |
|---|---|---|
| **SpellSleepAOE** | `A06P` → `A06O` | Массовый сон, радиус 185–430 по уровню |
| **SanctifiedEnchantment** | `A1K0` + `A1JU` + `A1JW` + `A1JX` + `B07Z` | 40с бафф, книга заклинаний, сплэш, статус-иконка |
| **Порталы** | ~12+ локаций | Полная система телепортов: радиус, задержка, скорость снаряда, FX, запрет союзников |
| **Mass Teleport** | `h07A` + `darksummoning` | Массовый телепорт армии |
| **Manabomba** | ManabombaNewSystem | Цепная бомба маны |

### 6.2 Расовые заклинания

| Раса | Заклинания |
|------|------------|
| **Орда** | `MassBloodlust`, `IronStar`, `SiegeEffect`, `DragonFire`, `PandaSecondAttack`, `AutoShield` |
| **Бандиты** | `BlinkToUnit`, `DelAttackSpel`, `Edvin_Ult`, `VoevodaSpell`, `Dovorougenie` (перевооружение) |
| **Ночные эльфы** | `KrugBeg/Can/Fin` (система кругов), `ElfBeg/Can`, `malfurionPas` |
| **Наги** | `VaishBuria`, `VaishArrow`, `NagaPas`, `NagaCommonSpell`, `MurlokSystem` |
| **Гоблины** | `CorrupTrain/Plus/Minus` (коррупция/трафик), `Potreblenie` (топливо), `Adrenalin`, `GazloySpellheals`, `Pulimetchik`, `Ognemetchik`, `Raketchik`, `Medic`, `Sniper`, `Saper`, `Car`, `Vezdehod`, `Tank`, `FireTank`, `Arta`, `Meha`, `Submarina`, `Podlodka` |
| **Эльфы крови** | `Arcana`, `Fel`, `Void`, `Light` (ветки: Begin/Cansel/Spell), `ManaAura`, `AutoStrela*`, `Porcha`, `Souz` |
| **Гномы** | `GelbinSpell`, `MehaWar`, `NanoGnome`, `MehaGigant`, `Spider`, `Chahohod`, `Minitank`, `UniTank`, `Venec_Tank`, `Car`, `SGT`, `SAU`, `MEGA_SAU`, `URAN` |
| **Силитиды** | `SpellBook`, 10 типов призыва (war/bee/spider/common/phoc/sold/skar/sliz/no1/builders), `Antennu`, `AutoPolet`, `FastKokon`, автокаст: acid missile/parasite/plodovitost/krilia/delimost/slize/tank, `SlowAnimation` |
| **Легион** | `SargerasReturnDamage`, `SomeDemonSpell`, `Blood`-спеллы, ауры, `Sand_Strike` |
| **Ледяные тролли** | `KillLoa`, `ServeLoa`, 2 геройских спелла |
| **Воргены** | `SpellOpletenie`, `LegGer` |
| **Нежить** | `ArthasResurrection/Coils/Nova`, `DK_Blood_Auto_Attack`, `SummonSkeleltClad`, `PassiveTalisra` |
| **Отрекшиеся** | `Zagraz`, `Korroz`, `Safety`, `Rot`, `Infect`, `MassInvis`, `Banshee/MassMindControl` |
| **Лесные тролли** | `Charge`, `ZacliatieOfLive/Damage`, `Yarost` (берсерк), `MassSetca`, `MassFrenzy`, `ChutioVolka` |
| **Джунгли-тролли** | `BlackSpear`, `Gurubashy`, `BladeStorm`, `Bwonsamdy`, `Hakkar` |

### 6.3 Утилитарные заклинания

| Система | Описание |
|---|---|
| **Ремонт** | 8 типов юнитов (Kop/Strel/Rub/Sham/Chern/Kodo/Tel/Nale) с T3-вариантами и кросс-тренировкой |
| **Лорды/Даларан/Наксрамас** | `LordWave`, `MassBaff`, `LordsAssist`, `Lord/Death` для PvE-данжей |
| **Ритуал** | Комбинация элементалей |

---

## 7. Таймеры

| Таймер | Интервал | Назначение |
|---|---|---|
| `udg_LobbyTime` | 60с (разовый) | Отсчёт до старта игры |
| `udg_IncomeTimerSecond` | 25с (период.) | Доход золота/дерева + пересчёт армейского XP |
| `udg_IncomeTimerFirst` | 600с (разовый) | Включение системы потребления |
| `udg_TimerToDis` | 600с диалог | TimerDialog с отсчётом до потребления |
| `udg_AiTimerStrateg` | ~15с × AiRepeat/5 | AI-цикл стратегии |
| `udg_TimerSmall/2/3` | Периодические | AI: ленивые юниты, попытки портала |
| `udg_TimerSmall4` | Периодический | Дополнительный AI |
| `udg_PlayerGet1/2/4` | Периодические | AI: ресурсы/действия |
| `aiFixer` | Периодический | AI: застрявшие юниты |
| `udg_SilitidTimer` | Периодический | Спавн силитидов |
| `SecondChance[24]` | На игрока | Таймер возрождения героя |
| `Global_Timer` | 999999с | Заглушка, не используется |

---

## 8. Обработчики событий

### Юниты
| Триггер | Событие | Действие |
|---|---|---|
| `Unit_Indexer` | init | Индексация юнитов (UDex) |
| `UnitEnterMap` | `EVENT_PLAYER_UNIT_ENTER` | Добавление в экономику |
| `UnitBuilded` | `EVENT_PLAYER_UNIT_CONSTRUCT_FINISH` | Расход на постройку |
| `UnitUpgraded` | `EVENT_PLAYER_UNIT_UPGRADE_FINISH` | Тир-апгрейд, контрольные точки |
| `UnitDead` | `EVENT_PLAYER_UNIT_DEATH` | Удаление из экономики, TotalProduction |
| `UnitRevive` | `LIFE > 0.6` | Восстановление в экономике |
| `Unit_Loaded` | Transport load | Посадка в транспорт |
| `Unit_Death` | Transport death | Пассажиры транспорта |

### Спеллы
- `SpellSleepAOE` — все игроки, `EVENT_PLAYER_UNIT_SPELL_EFFECT` — массовый сон
- `SanctifiedEnchantment` — все игроки, `EVENT_PLAYER_UNIT_SPELL_EFFECT` — бафф
- 37 расовых триггеров — `EVENT_PLAYER_UNIT_SPELL_FINISH` — выбор расы
- `MakeStolica` — `EVENT_PLAYER_UNIT_SPELL_EFFECT` — создание столицы
- Десятки расовых спелл-триггеров: `SpellCast`, `SpellE`, `SpellQ`, `KrugBeg`, `ElfBeg`, `Arcana`, `Fel`, `Void`, `Light`, `Corrup`, `Potreblenie`, и т.д.

### Атаки
- `StolicaAttacked` — атака на столицу → оповещение
- `AttackerAi` — AI: каст спеллов юнитами
- `AttackedAI` — AI: телепорт/защита

---

## 9. `main()` — полный поток инициализации

```jass
function main takes nothing returns nothing
    // 1. Карта
    SetCameraBounds(-30720...30720)     // Границы 60k × 60k
    SetDayNightModels(...)              // Тема Lordaeron
    SetTerrainFogEx(0,4000,8000,0.5,0.706,1.0,1.0)  // Синий туман
    
    // 2. Ресурсы
    InitSounds()
    CreateRegions()
    CreateCameras()
    CreateAllUnits()                    // Предрасставленные юниты
    InitBlizzard()
    
    // 3. vJASS-инициализация
    ExecuteFunc("jasshelper__initstructs100223406")
    ExecuteFunc("Global___Init")
    ExecuteFunc("SpellSleepAOE___onInit")
    ExecuteFunc("SanctifiedEnchantment___Init")
    initBoolExprs___Init()
    UISetup()
    Face2()
    SetContinetsBooleprs()
    
    // 4. GUI-инициализация
    InitGlobals()                       // Все глобалы в 0/null
    InitCustomTriggers()                // ~400+ InitTrig_ вызовов
    RunInitializationTriggers()         // 16+ ключевых триггеров по порядку
endfunction
```

**Порядок RunInitializationTriggers**:
1. `Unit_Indexer` — индексация юнитов
2. `InitForEconomics` — boolexpr-фильтры экономики
3. `UnitUpgraded` — контрольные точки
4. `MainInfo` — мультиборд
5. `Initial_things` — сбор игроков, `StartInc()`, `InitThings()`, `SetStartLocations()`, скорость FASTEST
6. `Init` — транспорт
7. `LumberTest` — отслеживание дерева
8. `FelGolemStrike` — спец-триггер
9. `InitGlobals` — второй проход глобалов
10. `KillTestUnits___OFF_ME` — очистка тестовых юнитов
11. `PereborPlayerForArmy` — AI: перебор армии
12. `PereborPlayerForNavy` — AI: перебор флота
13. `PortalFix` — фикс порталов
14. `Owner` — Даларан
15. `OwnerNax` — Наксрамас
16. `OwnerTurtle` — Черепаха

---

## 10. Примечательные паттерны кода

1. **Русские комментарии**: весь код комментирован по-русски (`Столица`, `Залил хеш`, `Коррупция`, `Воровство`)

2. **`udg_`-глобалы из GUI**: ~2500+ переменных из GUI смешаны с чистыми vJASS-библиотеками

3. **Кеширование boolexpr**: все фильтры предкомпилированы и сохранены в глобалы (`B_Lazy`, `udg_B_EnemyUnit`, `Altars`, `LiveHero`) — не пересоздаются при вызовах

4. **Портальная AI-система**: AI создаёт TP-магов → добавляет в `AiUnitsToPort` → `TryPort`/`RequestPort` телепортирует свободную армию к столицам/зданиям под атакой

5. **Прогрессивная сложность AI**: `AiLimit`, `AiMass`, `AiRepeat` обратно пропорциональны числу игроков (больше людей = сильнее AI)

6. **Двухфазная экономика**: первые 10 минут без потребления, затем полная модель с логистикой и коррупцией

7. **Struct через module**: `SanctifiedEnchantment` использует vJASS-паттерн `BindTemplate` для хеш-привязки со смещением

8. **`g`-префиксные глобалы-скретч**: `gUnit`, `gInt`, `gX`, `gY`, `gPlayer`, `gPi` — для производительности в фильтрах (избегание `local`)

9. **Русская транслитерация ID**: сырые коды способностей без общей системы именования — часть стандартные (`'hfoo'`, `'opeo'`), часть кастомные с русским подтекстом

10. **Гибридная архитектура**: чистые vJASS-библиотеки (AI, спеллы, экономика, порталы) + GUI-триггеры (`InitTrig_*`) — карта развивалась добавлением GUI-триггеров параллельно с vJASS-кодом
