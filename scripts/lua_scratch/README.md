# Lua Scratch — одноразовые bridge-сниппеты

**Все файлы в этой папке — временные скрипты**, запускаемые через `agent_bridge.py exec --file <имя>`.
Не участвуют в сборке карты. Хранятся для истории и возможности переиспользования.

Отсортированы по группам.

---

## ДИАГНОСТИКА

| Файл | Описание |
|---|---|
| `_diag.lua` | Общая диагностика: volume армии (food), недостроенные/застрявшие здания, возможности захвата. |
| `_diag_p5_cross.lua` | Где физически находятся юниты армии P5? Пересекают ли портал в EK? |
| `_diag_p5_portal.lua` | Диагностика P5: размер армии vs лимит, почему портал не применяется. |
| `_diag_p5_push.lua` | Контролируемый тест: 3 юнита P5 у портала → приказ идти за гейт, проверка пересечения. |
| `_diag_qtun.lua` | Есть ли боты в Ankirag (Qtun dungeon)? Могут ли оттуда выйти? |
| `_diag_webportals.lua` | Резолв всех web-порталов: позиция, континент-источник, dest-rect, статус (жив/мёртв). |
| `_kalim_diag.lua` | Боты с армией в Kalimdor: group health (size/nil/alive/dead). |
| `_sili_diag.lua` | Экономика Силитидов для P1..P4. |
| `_grade_probe.lua` | Диагностика grade-пайплайна: запускается ли Strateg, есть ли GradeUnit-здания, завершены ли исследования. |
| `_prod_probe.lua` | Пробник production для конкретного бота (P11): что может тренировать. |
| `_val_probe.lua` | Валидатор расы: проверяет структуру `AiRaces[rk]` на соответствие. |
| `_trace_naval.lua` | Трассировка naval-пути для P11 от столицы до берега. |

---

## МЕТРИКИ И СНИМКИ

| Файл | Описание |
|---|---|
| `_snap.lua` | Per-bot AI diagnostic snapshot: компактная строка + полный дамп в probe-log (тег SNAP). |
| `_metrics.lua` | Per-race метрики для чекпоинта 4:30: units, army, navy, transport, grade/cap, tier, ecoI, capture, cities, struct, stalled, food, capAlive. |
| `_metrics2.lua` | Per-race AI metrics snapshot — одна строка на каждого AI-контролируемого игрока. |
| `_eco_snap.lua` | Снимок экономики для выбранных ботов (pi=8,9,11,12,16,19,22). |
| `_capture.lua` | Per-bot замер захвата нейтральных зданий + реальный eco-счёт Strateg (i = ZahType + ecoWeights). |

---

## ХОТФИКСЫ (переопределение функций вживую)

| Файл | Описание |
|---|---|
| `_hotfix_continent.lua` | Фикс детекции континента: Northrend проверяется ДО EasternKingdoms (перекрытие → правильный континент). |
| `_hotfix_cont2.lua` | Переопределение `AiContinentOf` с EK-last приоритетом + перепроверка pi=11. |
| `_hotfix_gate.lua` | BrainProduce: gate-aware фильтрация `isTrainable`/`trainableSum` — скипать юнитов с невыполненным gate. |
| `_hotfix_groups.lua` | Фикс `GroupAddUnitSimple`/`GroupRemoveUnitSimple` + чистка мёртвых юнитов + пересборка пулов. |

---

## ХОТПАТЧИ (объёмные live-патчи)

| Файл | Описание |
|---|---|
| `_hotpatch_f1.lua` | F1 patch: build pipeline (footprint + anti-thrash + recycle + anchor). |
| `_hotpatch_naval.lua` | Naval-патч: `AiNavalBuildUntil`, `AiNavalBuildGrace`. |
| `_hotpatch_prod.lua` | Production-патч: `AiFindProdBuilding` — поиск здания по bldType. |
| `_hotpatch_r5.lua` | R5 patch: не дёргать канализующих рабочих + возобновление застрявших строек. |
| `_hotpatch_r5b.lua` | R5b: Fix 1 (no yank) + Fix 2 (resume с приоритетом столицы) + REVERT Fix 3. |
| `_hotpatch_r5c.lua` | R5c: критический фикс — `AiFindFreeWorker` выбирает idle рабочих из buildersT даже с неистекшим claim. |
| `_hotpatch_recycle.lua` | `AiWorkerIsBuilding` — проверка, строит ли рабочий в данный момент. |
| `_inject_webtp.lua` | Загрузка функций web-портального mass-TP в живую игру + запуск. |
| `_inject_webtp2.lua` | Улучшенный web-портальный mass-TP (cluster-based, web-route) + запуск. |
| `_live_patch_hordew2_builders.lua` | `AiEnsureBuilderReserve` — гарантировать резерв строителей для HordeW2. |

---

## ТЕСТЫ

| Файл | Описание |
|---|---|
| `_test_hkee.lua` | Тест: может ли P10 построить/апгрейднуть Keep (hkee)? |
| `_test_naval.lua` | Тест размещения верфи (shipyard=h0D1) для Undead ботов. |
| `_test_research.lua` | Сравнение принятия исследований: Horde (работает) vs Forsaken (застрял). |
| `_test_ship3.lua` | Тест water/land-тайлов: `IsTerrainPathable` для WALKABILITY/FLOATABILITY. |
| `_test_ship4.lua` | То же — ship-тест 4. |
| `_test_ship5.lua` | То же — ship-тест 5. |
| `_test_shore.lua` | Сканирование колец вокруг столицы P11 на береговую точку (суша с водой в ~300), попытка постройки верфи. |
| `_test_shore2.lua` | Water tile: WALKABILITY=true, FLOATABILITY=false. Land: WALKABILITY=false, FLOATABILITY=true. |
| `_test_mytele.lua` | Тест телепорта P5 через портал n003. |
| `_test_teledirect.lua` | Тест прямого телепорта P5 через портал n003. |
| `_test_webcast.lua` | Валидация: cast "web" на BlackMountain→EK портал, проверка пересечения армии P5. |
| `_test_webcheck.lua` | Проверка армии P5 после web-каста. |
| `_test_hordew2_subraces.lua` | Быстрое сравнение 3 ботов HordeW2 (подрасы). |
| `_hc_test.lua` | Эмпирический тест `SetPlayerHandicap` на HP юнита бота. |
| `_ally_hero_check.lua` | Проверка героев союзников (P10, P11, P12). |
| `_ally_train_test.lua` | Поиск алтаря P11, попытка тренировки Paladin, отчёт по gold/food. |
| `_dbg_web.lua` | Дебаг web-портала: жив ли n003_0941? |

---

## СПАВН / СБРОС / ОСТАНОВКА

| Файл | Описание |
|---|---|
| `_spawn.lua` | Спавн ботов по фиксированному ростера (4 силитида). |
| `_spawn16.lua` | Small-but-strong: выставить параметры + спавн 16 ботов случайных рас. |
| `_smallarmy.lua` | Применить настройки «small but strong» к живой игре. |
| `_del_players.lua` | Удалить ВСЕ юниты указанных игроков (верфи уже захвачены в `_verf_data.txt`). |
| `_ai_stop.lua` | Остановить ВСЕ Army AI (brain + legacy) — опустошить round-robin список `PlayerArmy`. |
| `_ai_stop_timers.lua` | Отключить все периодические AI-триггеры для ручного строительства верфей хостом. |

---

## ВЕРИФИКАЦИЯ

| Файл | Описание |
|---|---|
| `_verf_baseline.lua` | Базовые типы верфей для верификации (`h0D8`, `h0D1`, `h0D3`). |
| `_verf_capture.lua` | Захват всех верфей на карте: владелец, тип, x, y, континент. |
| `_verf_table.lua` | Курированные точки верфей: точные координаты успешного ручного размещения на открытой воде. |

---

## ИНФРАСТРУКТУРА МОСТА

| Файл | Описание |
|---|---|
| `_crumb.lua` | **Хлебные крошки.** Оборачивает подозрительные функции; каждая пишет своё имя в `23race_crumb.pld` немедленно (unbuffered `PreloadGenEnd`) перед выполнением. После жёсткого C++-краша файл содержит последнюю вызванную функцию. |
| `ai_portal_graph_probe.lua` | **Граф порталов.** Запускается через bridge, собирает все порталы (73 шт.), строит рёбра continent→continent. Результат — [PORTAL_GRAPH.md](../docs/PORTAL_GRAPH.md). |

---

## ПРОЧЕЕ

| Файл | Описание |
|---|---|
| `temp_original.lua` | Временный оригинальный дамп куска war3map.lua (до правок). |
