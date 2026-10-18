---
name: wc3-lua-debug
description: Методика отладки Lua-скрипта карты 23 Race Forever — Lua-ошибки колбэков, жёсткие C++-краши WC3 (ACCESS_VIOLATION 0x6C), логи probe-map, типичные баги конвертации vJASS→Lua. Использовать при любом баге, краше, фатале, "не работает триггер/спелл/ИИ".
---

# Отладка карты 23 Race Forever

Полные инструкции: `docs/DEBUG_WC3_MAP.md`, история краша 0x6C: `docs/AI_CRASH_HANDOFF.md`.

## Цикл
1. Не гадать — измерить. Добавить `ProbeLogWrite("[TAG] ...")` в точки входа/выхода, результаты
   фильтров, первый вызов колбэков. Не логировать внутри condition-фильтров `GroupEnum*`.
   Для записи в `.pld` нужен `ProbeLogEnableFlush()` (по умолчанию выключен).
2. Править только `map.w3x/_lua/monolith_split/sections/**`, затем `python build_map_lua.py`
   и проверка синтаксиса luaparser.
3. Закрыть старый WC3, удалить `Documents\Warcraft III\CustomMapData\23race_eval_*.pld`,
   запустить `HiveWE_cli probe-map ... --args "-window -nowfpause"` (см. `_run.bat`).
4. Читать `23Race_probe_log.pld`: `[CALLBACK-ERR]` даёт строку собранного `war3map.lua` —
   найти её (`sed -n 'Np' map.w3x/war3map.lua`) и соответствующую секцию.

## Жёсткие C++-краши (не ловятся pcall)
- Дамп: `%USERPROFILE%\Documents\Warcraft III\Errors\<дата>\Crash.txt`, секция `Exception.Summary`.
  Маленький адрес чтения (0x6C) = null/освобождённый юнит; младшие биты инструкции (`…CC59`)
  постоянны для одного бага — так сравнивают дампы между запусками.
- Повторяющийся цикл адресов в стеке = реентерабельность: вложенный enum/`GroupClear` той же
  глобальной группы (`gGroup` и т.п.) внутри `ForGroup`/фильтра/события.
- Локализация: бисекция подсистем тумблерами через мост (`AiDiplomatEnabled=false`, …), затем
  небуферизованные breadcrumb'ы (последний записанный перед крашем = виновник). Буферизованный
  хвост `.pld` после краша недостоверен.

## Типичные баги vJASS→Lua (проверять первыми)
- Функция потеряла параметры (`function F()` вызывается как `F(a, b)`) — тело читает nil-глобалы.
  Сигнатуры восстанавливать по оригиналу: `git show ea6d45d^:map.w3x/war3map.j`.
- `local x` объявлен внутри `if`, а используется после блока → nil.
- Голая функция вместо boolexpr в `GroupEnum*` → нужен кэшированный `Filter(f)`.
- Пустой стаб `function Native() end` затеняет натив → `Native = Native or fallback`.
- `UnitAlive` в WC3-Lua возвращает nil → в проекте полифилл через `GetUnitState(u, UNIT_STATE_LIFE) > 0.405`.
- `IsTerrainPathable` инвертирован: `true` = тип проходимости ЗАБЛОКИРОВАН.
- `tArray[tArray0]` вместо `tArray[tArray[0]]`; строковый `+` вместо `..`; Lua-паттерн с `|`.
- `DisplayTimedTextToPlayer` не пишет в War3Log — для логов только `BJDebugMsg`/`ProbeLogWrite`.
