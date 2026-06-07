# Конвертация vJASS → Lua: План и статус

## Статистика исходного кода

| Категория | Количество |
|---|---|
| Всего функций vJASS | 4 810 |
| Библиотек (library) | 14 |
| Scope'ов | 4 |
| Struct'ов | 3 |
| InitTrig-триггеров | 1 294 |
| Глобалов (toplevel + udg_) | 519 |
| Триггер-глобалов (gg_trg_*) | 1 542 |
| Hashtable-операций | 543 |
| Таймеров (TimerStart) | 52 |
| ExecuteFunc вызовов | 19 |
| Региональных переменных (gg_rct_*) | 154 |

## Слои конвертации

| Слой | Статус | Функций | % |
|------|--------|---------|---|
| 0 — Фундамент | ⬜ pending | — | — |
| 1 — Экономика | ⬜ pending | — | — |
| 2 — Столицы/доминация | ⬜ pending | — | — |
| 3 — AI-ядро | ⬜ pending | — | — |
| 4 — AI-стратегии | ⬜ pending | — | — |
| 5 — Спеллы общие | ⬜ pending | — | — |
| 6 — Спеллы расовые | ⬜ pending | — | — |
| 7 — Расовые InitTrig | ⬜ pending | — | — |
| 8 — Лобби/UI | ⬜ pending | — | — |
| 9 — main() и сборка | ⬜ pending | — | — |

## Принцип конвертации

Каждый vJASS-функции соответствует ровно одна Lua-функция с тем же именем (или префиксом слоя).
Глобалы переносятся в таблицу `G`.
Хеш-таблицы заменяются на Lua-таблицы.

## Файлы слоя 0 (фундамент)

```
lua_rewrite/
├── CONVERSION_PLAN.md          ← этот файл
├── function_index.json         ← индекс всех vJASS-функций
├── globals_index.json          ← индекс глобалов и хеш-операций
├── triggers_index.json         ← индекс триггеров и событий
├── check_progress.lua          ← скрипт верификации
└── output/
    ├── main.lua                ← финальный main()
    ├── globals.lua             ← все глобалы
    ├── tables.lua              ← замена хеш-таблиц
    ├── utils.lua               ← утилиты из библиотек A1, Global, LibNewFunctions, common
    ├── ui.lua                  ← UISetup, Face2
    ├── lobby.lua               ← StartLobby, EndLobby_and_Start_game
    └── init.lua                ← SetStartLocations, InitGlobals, инициализация
```
