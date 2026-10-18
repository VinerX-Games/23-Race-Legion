---
name: wc3-map-systems
description: Справочник игровых систем и структуры карты 23 Race Forever — экономика, столицы, вассалитет, доминация, выбор рас, континенты, порталы, лобби, движущиеся города, подрасы HordeW2; где лежат файлы карты и ассеты. Использовать при правке геймплея, баланса, триггеров рас или object data.
---

# Игровые системы и структура карты

- `docs/PROJECT_MAP.md` — файлы карты (`war3map.w3u/w3a/w3t/w3q/...`), раскладка Lua-секций,
  37 рас, ассеты, инструменты.
- `docs/SCRIPTS_ANALYSIS.md` — разбор исходного vJASS: библиотеки, глобалы по системам,
  хеш-таблицы, экономика (формула баланса, логистика, коррупция, доход каждые 25 с, потребление
  после 600 с), столицы (`A0IQ`), вассалитет, доминация (`PercentWin`), выбор расы (spell → старт),
  тиры T1→T3, лобби и порядок инициализации, континенты (`udg_Continents`), порталы.
- `docs/PORTAL_GRAPH.md` — какие порталы соединяют какие континенты (rect'ы `gg_rct_*`).
- `docs/HORDew2_SUBRACES_PROPOSAL.md` — дизайн подрас HordeW2 (research-флаги по образцу
  Naga/Murloc, заглушки `xd01..xd07`).

## Где искать код системы
- Экономика, индексатор, события юнитов — `80_runtime/triggers/01_core_economy.lua`, `80_runtime/_lib/*`.
- Лобби, столицы, феоды, доминация — `80_runtime/triggers/02_game_modes.lua`.
- Континенты, дипломатия, доход — `80_runtime/triggers/03_continents_diplomacy.lua`, `80_runtime/_continental/*`.
- Выбор расы — `80_runtime/triggers/04_race_selection.lua`; триггеры расы — `80_runtime/triggers/races/<Race>.lua`.
- Транспорт, корабли, порталы — `80_runtime/triggers/06_transport_portals.lua`.
- Порталы городов, Даларан/Наксрамас/Черепаха, Изумрудный сон — `80_runtime/triggers/15_ai_portals_cities.lua`.

Object data (юниты/способности/предметы) — бинарные `war3map.w3*`; читать через
`HiveWE_cli get-object/search-objects/dump-objects` (см. `docs/DEBUG_WC3_MAP.md`).
Строки и тултипы — `war3map.wts`.
