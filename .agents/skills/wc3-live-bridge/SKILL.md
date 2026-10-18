---
name: wc3-live-bridge
description: Live Agent Bridge — исполнение произвольного Lua в уже запущенной карте 23 Race Forever через agent_bridge.py (чтение состояния, горячий патч функций, спавн ботов, логи без перезапуска игры).
---

# Live Agent Bridge

Документация: `docs/LIVE_AGENT_BRIDGE.md`.
Код канала: `sections/00_prelude.lua` (eval-канал, `BridgeConsumeEval`, тик 0.25 с).
Утилита: `agent_bridge.py` в корне проекта.

## Старт отладочной сессии
1. При закрытой игре очистить старые файлы:
   `python agent_bridge.py reset`
   (Удаляет `%USERPROFILE%\Documents\Warcraft III\CustomMapData\23race_eval_*.pld`, иначе игра переиграет старые команды).
2. Запустить карту: `_run.bat` или `python scripts/wc3_hivewe.py probe`.
3. В игре ввести: `-bridge:eval:on` (включить мост). В консоли появится heartbeat `hb|1`.
4. Проверить связь: `python agent_bridge.py exec "return 1"`.

## Полезные команды моста
```bash
# Чтение состояния игры
python agent_bridge.py exec "return AiRace[15]"
python agent_bridge.py exec "return udg_Continents[1]"

# Горячий патч функции без пересборки карты
python agent_bridge.py exec "function Foo() ... end"

# Спавн ботов
python agent_bridge.py exec "createAiPlayer(2, 'token')"
python agent_bridge.py exec "for pi=2,23 do createAiPlayer(pi) end; return 'done'" --timeout 30

# Включение логов определенной подсистемы
python agent_bridge.py exec "LogFilterAll=false; LogEnable('AI'); LogEnable('BRAIN')"

# Исполнение скрипта из файла
python agent_bridge.py exec --file test_script.lua
```

Ответы: `OK <значение>` / `ERR <сообщение>` / `TIMEOUT`.

## Если мост не отвечает (TIMEOUT)
В чате игры: `-bridge:restart:`, затем в терминале `python agent_bridge.py reset` и `python agent_bridge.py exec "return 1"`.
`EvalNextSeq` нельзя откатывать вручную (Preloader кэширует файлы).
