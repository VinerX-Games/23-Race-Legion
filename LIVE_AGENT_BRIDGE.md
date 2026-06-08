# Live Agent Bridge — исполнение Lua в работающей карте (БЕЗ перезапуска)

> **Это имба.** Агент (ИИ) шлёт произвольный Lua в **уже запущенную** игру, читает
> возвращаемые значения, меняет состояние мира на лету. Карту не надо перезапускать
> ради каждой проверки переменной/гипотезы. Основа для будущего **режима ГМ-нейронки**:
> агент как живой ведущий — спавнит юнитов, реагирует на события, правит логику в рантайме.

## Что это даёт
- Дебаг ИИ за минуты вместо «правка → пересборка → минута загрузки → смотреть»:
  читаем `AiRace[pi]`, размеры групп `udg_Ai_army[pi]`, ордера юнитов, и т.д.
- **Горячий патч**: переопределить функцию в рантайме (`function Foo() ... end`),
  сразу замерить эффект, и только потом править исходник. Так найден баг `UnitAlive`.
- ГМ-режим: `CreateUnit`, `PanCameraToTimedForPlayer`, выдача приказов, спавн волн —
  всё из агента в реальном времени.

## Как устроено (канал eval, v2)
Поверх Preloader-моста (см. ниже). Код/результат ходят **hex-кодированными** —
в JASS-строке `.pld` не бывает кавычек/переносов/`|`, поэтому **крашей нет**.
- **IN**: последовательные файлы `<CustomMapData>/23race_eval_NNNN.pld`,
  читаются в игре через `Preloader` (обязательно последовательные — WC3 **кэширует
  Preloader по имени файла**, переиспользовать одно имя нельзя).
  Агент пишет файл **атомарно** (`*.tmp` + `os.replace`) — игра не прочитает полуфайл.
  Флаг загрузки в тултипе `AHbz` — **per-seq токен** `l<seq>` (не константа), детект
  «тултип ≠ baseline» не ломается из-за совпадения. payload: `eval|<seq>|<i>|<total>|<hex>`
- **HB** (v2): игра публикует `<CustomMapData>/23race_eval_hb.pld` → `hb|<seq>` —
  тот seq, который она сейчас ждёт. Агент (`next_seq`) берёт номер **отсюда**, а не
  угадывает по файлам → счётчики агента и игры **не могут разойтись**. Это убирает
  «вечный затык» (раньше один пропущенный eval пиннил мост навсегда).
- **OUT**: **per-seq** `<CustomMapData>/23race_eval_out_NNNN.pld`, пишется `PreloadGenEnd`,
  агент читает обычным файловым чтением. Результаты не затирают друг друга. Результат
  **разбит на чанки** (≤200 hex/строку), т.к. WC3 режет строку в `Preload(...)` (~259).
  payload строки: `<seq>|<ok 0/1>|<idx>|<total>|<hexchunk>`
- В игре: `EvalRun` пробует `load("return "..code)` (голые выражения возвращают значение),
  иначе `load(code)`; всё в `pcall`; результат сериализуется (таблицы, глубина 5) и hex'ится.

Код канала: `map.w3x/_lua/monolith_split/sections/00_prelude.lua`
(`EvalHexDec/EvalHexEnc/EvalSerialize/EvalRun/EvalWriteResult/BridgeConsumeEval`, тик 0.25с).
Собирается в `war3map.lua` через `build_map_lua.py`. **Никогда не править собранный
war3map.lua руками** — только split-секции + пересборка.

## Как пользоваться
Хелпер агента: `C:\Games\23 Race\agent_bridge.py`
```
# 1) поднять карту (держать открытой)
HiveWE_cli probe-map --map "<...>\map.w3x" --warcraft "F:/Games/Warcraft III" \
  --keep-open --wait 95 --click-after 50 --probe-log 23Race_probe_log.pld

# 2) один раз после запуска
python agent_bridge.py reset

# 3) гнать Lua сколько угодно
python agent_bridge.py exec "return AiRace[15]"
python agent_bridge.py exec --file snippet.lua
```
Печатает `OK <значение>` / `ERR <сообщение>` / `TIMEOUT`. Первый exec сразу после
загрузки может словить таймаут (heartbeat ещё не записан) — просто повторить, seq
самосинхронизируется (v2: повтор больше не уводит счётчик в рассинхрон).

### Восстановление зависшего моста (v2)
Если пошли сплошные `TIMEOUT` — обычно мост сам выправится со следующего exec
(heartbeat-синхронизация). Если нет (например, отравлен Preloader-кэш конкретного
имени файла) — out-of-band сброс через чат, он **не** использует eval-канал:
```
# в игре (или чат-инъекцией): -bridge:restart:   -> EvalNextSeq=1 + ре-baseline
python agent_bridge.py reset                      # чистит inbox/out/hb
python agent_bridge.py exec "return 1"            # проверка
```
Крайний случай — рестарт карты. **`agent_bridge.py reset` сам по себе НЕ ресинхронит**
старую (до-v2) карту: он не трогает `EvalNextSeq` в игре; в v2 это лечит heartbeat.

## Управление выводом логов (LogFilter)
По умолчанию все разделы `[TAG]` выводятся в чат/экран (`LogFilterAll = true`).
Можно глушить конкретные разделы, чтобы не забивать экран — буфер и `.pld`-файл
пишутся **всегда**, независимо от фильтра. Теги: `BOOT`, `LOG`, `INIT`, `BRIDGE`,
`EVAL`, `STEP`, `CALLBACK-ERR`, `PING`, `MAIN`, `AI`, `AIARMY`, `CHAT`, `UI`.

### Через bridge-канал (из агента или Preloader-скрипта)

```
HiveWE_cli probe-map ... --bridge-script "0:log:alloff"        # выключить всё на экране
HiveWE_cli probe-map ... --bridge-script "0:log:on:AI"         # включить [AI]
HiveWE_cli probe-map ... --bridge-script "0:log:off:AIARMY"    # заглушить [AIARMY]
HiveWE_cli probe-map ... --bridge-script "0:log:toggle:BRIDGE" # переключить [BRIDGE]
HiveWE_cli probe-map ... --bridge-script "0:log:list"          # дамп статуса в probe-log
```

### Через live eval (agent_bridge.py)

```
python agent_bridge.py exec "LogFilterAll = false"         # всё на буфер
python agent_bridge.py exec "LogEnable('AI')"              # включить [AI]
python agent_bridge.py exec "LogDisable('BRIDGE')"         # заглушить [BRIDGE]
python agent_bridge.py exec "LogToggle('AIARMY')"          # переключить
python agent_bridge.py exec "return LogList()"             # дамп фильтров
python agent_bridge.py exec "return LogFilterAll"          # узнать глобальный статус
```

### Через чат в игре

```
-log alloff          # выключить всё
-log on BRIDGE       # включить [BRIDGE]
-log off AIARMY      # заглушить [AIARMY]
-log toggle AI       # переключить [AI]
-log list            # показать статус всех тегов
-log allon           # вернуть всё обратно
```

### Типичный сценарий отладки ИИ

```
# 1) Карта запущена, начинаем сессию
python agent_bridge.py reset
python agent_bridge.py exec "LogFilterAll = false"
python agent_bridge.py exec "LogEnable('AI')"

# 2) Работаем — видим только [AI] сообщения на экране,
#    но ВСЁ пишется в 23Race_probe_log.pld для полного анализа

# 3) Нужна детализация армии:
python agent_bridge.py exec "LogEnable('AIARMY')"

# 4) Закончили — вернуть всё:
python agent_bridge.py exec "LogFilterAll = true"
```

## Подводные камни (важно)
- **Preloader кэширует по имени файла** → inbox строго последовательный, новое имя каждый раз.
- **Запись inbox атомарна** (`*.tmp`+`os.replace`) → не отдавать игре полуфайл.
- **Seq берётся из heartbeat игры**, агент не угадывает → нет рассинхрона (v2).
- **Preload режет строку ~259 символов** → большой результат разбивать на чанки (сделано).
- **Не все нативы работают в Lua-рантайме!** Проверять, а не верить:
  `ExecuteFunc` — работает; `UnitAlive` — **возвращает nil** (полифилл в прелюдии).
- RU-консоль cp1251 — хелпер форсит UTF-8 на stdout.

## Идея «ГМ-нейронка» (направление)
Агент подписывается на события карты через мост (загрузка, смерть героя, таймер),
и в ответ генерит/шлёт Lua: подкручивает сложность, спавнит подмогу/боссов, ведёт
сюжет, комментирует. Двусторонний цикл уже есть — событие в probe-log → агент читает →
шлёт eval. Осталось формализовать события-триггеры на стороне карты.
