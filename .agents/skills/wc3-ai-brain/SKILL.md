---
name: wc3-ai-brain
description: Архитектура ИИ ботов 23 Race Forever — реестр рас RegisterAiRace, декларативные данные рас, единый brain-тик, отряды, дипломат, флот, порталы; как добавить/починить ИИ-расу и что запланировано.
---

# ИИ ботов (AI Brain)

Документация:
- `docs/AI_OVERHAUL_PLAN.md` — актуальный статус, цели (24 бота без просадок FPS, челлендж, стабильность).
- `docs/AI_BRAIN_DESIGN.md` — дизайн и реализация мозга (§19 — реализация, §20 — вектор развития).
- `docs/AI_BRAIN_OPTIMIZATION.md` — оптимизации и профайлер `AiProfileData`.
- `docs/PORTAL_GRAPH.md` — граф межконтинентальных порталов.

## Где расположен код ИИ
- `map.w3x/_lua/monolith_split/sections/81_ai.lua` — `RegisterAiRace`, `AiRaceOf(pi)`, токены, data-driven движки (`AiRunChooseBuildings`, `AiRunProduction`), диспетчеризация legacy-хуков.
- `sections/82_ai_races/NN_<race>.lua` — конфигурация расы: `tokens`, `weight`, `altar`, `start`, `buildings`, `gates`, `branches`, `production`, `worker`, `compTarget`, хуки (`attacker/attacked/upgrade/naval`), `wall`, `brain`.
- `sections/83_ai_brain.lua` — единый round-robin тик `PlayerGet1` → `PlayerArmy` → `AiBrainArmyTick` (Perceive → BrainProduce → BrainBuild → Objectives → Focus → Naval → Pirates → Diplomat). World model хранится в `AiData[pi].wm`.
- `sections/84_ai_diplomat.lua`, `sections/85_ai_portal_graph.lua`.

## Алгоритм: Добавить или починить ИИ-расу
1. Получить rawcode'ы расы и дерево технологий:
   `python scripts/wc3_hivewe.py race "<суффикс>"`
2. Создать или исправить `sections/82_ai_races/NN_<race>.lua` и проверить функцию `start<Race>(pi)` в `libraries/13_Races.lua`.
3. Добавить файл в `map.w3x/_lua/monolith_split/manifest.json` (если создан новый файл).
4. Проверить валидатором:
   `python scripts/validate_ai_races.py`
5. Собрать и проверить синтаксис:
   `python scripts/wc3_tools.py build`, затем `python scripts/wc3_tools.py check --kind ai`
6. Заспавнить бота в игре через чат `-aiN <token>` или через мост: `python agent_bridge.py exec "createAiPlayer(2, 'token')"`
7. Убедиться, что: армия растёт, `harvest > 0`, золото расходуется, грейды исследуются.

## Инварианты
- Сбой одного бота изолирован в `pcall` (карантин `AiBotFaults`), общий тик не падает.
- Состояние хранится исключительно в `AiData[pi]` и `AiSquads`.
- Запрещены тяжелые полнокартовые `GroupEnum` на каждом тике; сенсинг выполняется редко и round-robin.
- Лог-теги мозга: `BRAIN`, `BRAINOBJ`, `BRAINFOC`, `BRAINDEF`, `BRAINTP`, `BRAINBLD`, `BRAINERR`, `BRAINVALID`.

Повторяемая проверка бота: `python scripts/wc3_scenarios.py tests/scenarios/ai-growth.json --slot 2 --token scarlet`; выбрать свободный slot и токен нужной расы.
