---
name: wc3-lua-debug
description: Методика отладки Lua-скрипта карты 23 Race Forever — ошибки колбэков [CALLBACK-ERR], C++ краши WC3 (ACCESS_VIOLATION 0x6C), логи probe-map, типичные баги vJASS→Lua. Использовать при любом баге, краше или сбое триггеров/спеллов.
---

# Отладка карты 23 Race Forever

Инструкции: `docs/DEBUG_WC3_MAP.md`, история краша 0x6C: `docs/AI_CRASH_HANDOFF.md`.

## Цикл отладки
1. **Локализация ошибки по строке**:
   Если ошибка выдает строку в `war3map.lua:NNNN`:
   ```bash
   python scripts/wc3_tools.py line NNNN
   ```
   Это мгновенно укажет на конкретный файл секции, локальную строку и функцию.
2. **Правка исходников**:
   Править ТОЛЬКО `map.w3x/_lua/monolith_split/sections/**`.
   Затем `python scripts/wc3_tools.py build`, после него `python scripts/wc3_tools.py verify`. Verify не пересобирает карту.
3. **Запуск и чтение логов**:
   Запустить игру через `_run.bat` или `python scripts/wc3_hivewe.py probe`.
   Лог пишется в `%USERPROFILE%\Documents\Warcraft III\CustomMapData\23Race_probe_log.pld`.
   Строки `[CALLBACK-ERR]` содержат номер строки `war3map.lua`.

## Жёсткие C++ краши (не перехватываются pcall)
- Дамп краша: `%USERPROFILE%\Documents\Warcraft III\Errors\<дата>\Crash.txt`, секция `Exception.Summary`.
  - Чтение по адресу `0x6C` = null / уничтоженный юнит.
  - Младшие биты адреса инструкции (например `...CC59`) стабильны для одной причины.
  - Повторяющийся стек адресов = реентерабельность: вложенный вызов `GroupEnum*` или `GroupClear` по той же глобальной группе (`gGroup`, `gUnit`) внутри `ForGroup` или фильтра.
- Локализация краша: отключение подсистем тумблерами через мост (`AiDiplomatEnabled=false` и т.д.) + небуферизованные хлебные крошки.

## Типичные ловушки vJASS→Lua
- **UnitAlive**: Натив возвращает `nil` для созданных юнитов. Заменять на `GetUnitState(u, UNIT_STATE_LIFE) > 0.405`.
- **IsTerrainPathable**: Инвертирован (`true` = непроходимо).
- **Потерянные аргументы**: `function F()` вызывается с параметрами `F(a, b)` — тело читает несуществующие глобалы. Сверять с оригинальным `map.w3x/war3map.j` (`git show ea6d45d^:map.w3x/war3map.j`).
- **Scope переменных**: `local x` объявлен внутри блока `if`, а используется снаружи → равен `nil`.
- **Фильтры**: В `GroupEnum*` передавать кэшированный `Filter(f)` / `Condition(f)`, а не голую функцию.
- **Массивы**: `tArray[tArray0]` вместо `tArray[tArray[0]]`; строковый `+` вместо `..`.

Для повторяемых проверок использовать `scripts/wc3_scenarios.py` и `tests/scenarios/`. Старые логи маппить по source map и хешу запускавшейся сборки из отчёта сценария.
