---
name: wc3-live-bridge
description: Live Agent Bridge — исполнение произвольного Lua в уже запущенной карте 23 Race Forever через agent_bridge.py (чтение состояния, горячий патч функций, спавн ботов, логи). Использовать, когда нужно проверить гипотезу или фикс в живой игре без пересборки.
---

# Live Agent Bridge

Полное описание: `docs/LIVE_AGENT_BRIDGE.md`. Код канала — `sections/00_prelude.lua`
(`EvalRun`, `BridgeConsumeEval`, `EvalWriteResult`, тик 0.25 с). Хелпер — только `agent_bridge.py`
в корне репозитория (v2, heartbeat).

## Запуск сессии
1. Пока игра закрыта: удалить `%USERPROFILE%\Documents\Warcraft III\CustomMapData\23race_eval_*.pld`
   и выполнить `python agent_bridge.py reset` — иначе свежая карта переиграет старые eval как новые.
2. Поднять карту: `HiveWE_cli probe-map ... --keep-open --args "-window -nowfpause"`.
3. В игре: `-bridge:eval:on` (в релизе мост выключен). Чистый старт = heartbeat `hb|1`.
4. `python agent_bridge.py exec "return 1"` — первый вызов может дать TIMEOUT, повторить.

## Команды
```
python agent_bridge.py exec "return AiRace[15]"
python agent_bridge.py exec --file snippet.lua
python agent_bridge.py exec "..." --watch --timeout 12      # ожидание через ReadDirectoryChangesW
python agent_bridge.py exec "for pi=2,23 do createAiPlayer(pi) end; return 'done'" --timeout 30
python agent_bridge.py exec "function Foo() ... end"         # горячий патч до правки исходника
python agent_bridge.py exec "LogFilterAll=false; LogEnable('AI')"
```
Ответ: `OK <значение>` / `ERR <сообщение>` / `TIMEOUT`.

## Если мост завис
Сплошные TIMEOUT: в игре `-bridge:restart:`, затем `python agent_bridge.py reset` и `exec "return 1"`.
`EvalNextSeq` никогда не откатывать: Preloader кэширует файлы по имени.

## Ограничения
- Preload режет строку ~259 символов (результат уже чанкуется).
- Горячий патч живёт только до перезапуска: после подтверждения фикс переносится в секции
  и карта пересобирается.
