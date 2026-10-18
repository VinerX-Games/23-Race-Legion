---
name: wc3-ai-brain
description: Архитектура ИИ ботов 23 Race Forever — реестр рас RegisterAiRace, декларативные данные рас, единый brain-тик, отряды, дипломат, флот, порталы; как добавить/починить ИИ-расу и что запланировано. Использовать при любой работе с ИИ, ботами, расами ИИ.
---

# ИИ ботов

Документы (читать по задаче):
- `docs/AI_OVERHAUL_PLAN.md` — актуальный статус, цели заказчика (не ломаться / FPS при 24 ботах /
  челлендж), треки R (надёжность), E (экономика), C (бой), P (перф), решения.
- `docs/AI_BRAIN_DESIGN.md` — дизайн мозга (§19 — фактическая реализация, §20 — векторы улучшения).
- `docs/AI_BRAIN_OPTIMIZATION.md` — оптимизации, профайлер `AiProfileData`.
- `docs/AI_REFACTOR_PLAN.md`, `docs/HANDOFF_AI_PHASE3.md` — реестр рас и data-driven движки.
- `docs/PORTAL_GRAPH.md` — граф порталов между континентами.

## Где код
- `sections/81_ai.lua` — `RegisterAiRace`, `AiRaceOf(pi)`, токены, движки (`AiRunChooseBuildings`,
  `AiRunProduction`, …), диспетч legacy-хуков.
- `sections/82_ai_races/NN_<race>.lua` — данные расы: `tokens`, `weight`, `altar`, `start`,
  `buildings` (`{id, limit, power, gate=}` + `seed`), `gates`, `branches`, `production`
  (`worker={id,cap,from}`), `compTarget`, хуки `attacker/attacked/getLvl/upgrade/naval`, `wall`, `brain`.
- `sections/83_ai_brain.lua` — единый round-robin тик `PlayerGet1` → `PlayerArmy` →
  `AiBrainArmyTick` (Perceive → BrainProduce → BrainBuild → Objectives → Focus → Naval →
  Pirates → Diplomat). World model — `AiData[pi].wm`. Squad-FSM отключён (жёсткий краш);
  отряды трекаются, ордера stateless.
- `sections/84_ai_diplomat.lua`, `sections/85_ai_portal_graph.lua`; legacy-ИИ — `80_runtime/_ai/*`,
  `libraries/04_AI0.lua` (фильтры `f_*`), `libraries/11_LibDifferentAiStuff.lua` (ТП-маги, `PortTo`).

## Добавить / починить расу
1. Rawcode'ы расы: `HiveWE_cli describe-race --map map.w3x --suffix "<суффикс>"`.
2. `start<Race>(pi)` по образцу существующих; данные в новом `82_ai_races/NN_<race>.lua`;
   добавить файл в `manifest.json`.
3. Валидатор: `scripts/validate_ai_races.py`; на старте `AiValidateRace` пишет `[BRAINVALID]`.
4. Пересобрать, заспавнить бота (`-aiN <token>` или мост `createAiPlayer(N,'token')`),
   проверить мостом: армия растёт, harvest > 0, золото тратится, грейды идут.

## Инварианты
- Ошибка одного бота не должна валить тик всех (тик в `pcall`, карантин `AiBotFaults`).
- Новый код ИИ — на локалках и параметрах, состояние только в `AiData[pi]`/`AiSquads`.
- Тяжёлый sensing — редко и round-robin; нельзя делать полно-картовые `GroupEnum` в каждом тике.
- Всё тюнингуемое — данные с дефолтами, проверяется мостом без пересборки.
- Лог-теги (тихо по умолчанию): `BRAIN`, `BRAINOBJ`, `BRAINFOC`, `BRAINDEF`, `BRAINTP`, `BRAINBLD`,
  `BRAINERR`, `BRAINVALID`.
