---
name: wc3-map-systems
description: Справочник игровых систем и структуры карты 23 Race Forever — экономика (баланс, доход каждые 25с), столицы, вассалитет, доминация, выбор рас, континенты, порталы, триггеры рас и object data.
---

# Игровые системы и структура карты 23 Race Forever

Документация:
- `docs/PROJECT_MAP.md` — структура файлов карты, 37 рас, ассеты, инструменты.
- `docs/SCRIPTS_ANALYSIS.md` — анализ vJASS: библиотеки, хештаблицы, глобалы, формулы экономики, столицы (`A0IQ`), вассалитет, доминация (`PercentWin`), тиры Т1-Т3, континенты (`udg_Continents`), порталы.
- `docs/PORTAL_GRAPH.md` — соединения континентов через порталы (rect'ы `gg_rct_*`).
- `docs/HORDew2_SUBRACES_PROPOSAL.md` — дизайн подрас HordeW2 (флаги исследований `xd01..xd07`).

## Где искать код подсистем
- **Экономика, таймеры дохода, индексы юнитов**: `80_runtime/triggers/01_core_economy.lua`, `80_runtime/_lib/*`.
- **Режимы игры, столицы, феоды, доминация**: `80_runtime/triggers/02_game_modes.lua`.
- **Континенты, дипломатия, доход**: `80_runtime/triggers/03_continents_diplomacy.lua`, `80_runtime/_continental/*`.
- **Выбор расы**: `80_runtime/triggers/04_race_selection.lua`.
- **Триггеры конкретных рас**: `80_runtime/triggers/races/<Race>.lua`.
- **Морской транспорт и порталы**: `80_runtime/triggers/06_transport_portals.lua`.
- **Порталы городов и особые локации**: `80_runtime/triggers/15_ai_portals_cities.lua`.

## Работа с Object Data (юниты, спеллы, предметы)
Бинарные файлы `war3map.w3*` инспектируются через обертку `scripts/wc3_hivewe.py`:
- Инспекция юнита/здания/спелла: `python scripts/wc3_hivewe.py object <id>`
- Поиск объекта: `python scripts/wc3_hivewe.py search "<имя>"`
- Просмотр дерева и состава расы: `python scripts/wc3_hivewe.py race "<суффикс>"`
- Строки и тултипы карты хранятся в `map.w3x/war3map.wts`.
