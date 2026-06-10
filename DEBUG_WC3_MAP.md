# Практики дебага WC3-карты (vJASS -> Lua конвертация)

## Инструментарий

| Инструмент | Команда |
|---|---|
| Сборка Lua-скрипта | `python build_map_lua.py` |
| Проверка синтаксиса | `python -c "from luaparser import ast; ast.parse(open('map.w3x/war3map.lua','rb').read())"` |
| Запуск карты | `HiveWE_cli run-map --map map.w3x --warcraft "F:/Games/Warcraft III"` |
| Автотест с логами | `HiveWE_cli probe-map --map map.w3x --warcraft "F:/..." --click-after 60 --wait 220 --bridge-script "140:create_ai:2" --probe-log 23Race_probe_log.pld` |

Параметры probe-map:
- `--click-after 60` — клик в окно WC3 через 60с (пропускает меню)
- `--wait 220` — общее время ожидания (клик + 2×Enter по 5с + загрузка + игра)
- `--bridge-script "140:create_ai:2"` — создать AI игрока 2 через bridge на 140й секунде
- `--probe-log file.pld` — куда писать preload-лог

Лог лежит в `%USERPROFILE%\Documents\Warcraft III\CustomMapData\23Race_probe_log.pld`.

---

## Универсальное логирование (preload + War3Log)

В `00_prelude.lua`:

```lua
function ProbeLogWrite(message)
    ProbeLogLines[#ProbeLogLines + 1] = sanitize(message)
    if #ProbeLogLines > 2000 then table.remove(ProbeLogLines, 1) end
    pcall(function() BJDebugMsg(tostring(message)) end)  -- в War3Log.txt
    if not ProbeLogFlushEnabled then return end
    pcall(function()
        PreloadGenClear(); PreloadGenStart()
        for _, line in ipairs(ProbeLogLines) do Preload(line) end
        PreloadGenEnd(ProbeLogFile)
    end)
end
```

`BJDebugMsg` пишет в `War3Log.txt` (читается probe-map отдельно), `PreloadGenEnd` пишет в `.pld` (CustomMapData). Два независимых канала = логи не теряются.

---

## Типичные баги vJASS -> Lua конвертации

### 1. UnitAlive возвращает nil для pre-placed юнитов

В JASS `UnitAlive(u)` возвращает `boolean`. В WC3 Lua — **nil** для юнитов, созданных через `CreateNUnitsAtLoc`. `not nil = true`, поэтому любой фильтр `if not UnitAlive(u) then return false end` отвергает ВСЕ юниты.

**Фикс**: везде заменить на `GetUnitState(u, UNIT_STATE_LIFE) > 0.405`.

**Как искать**: grep по всем `.lua` на `UnitAlive`, проверить каждый в контексте `if not` или `return UnitAlive(...) and ...`.

### 2. tArray[0] vs tArray0 — индексация массива

В JASS `tArray[tArray[0]]` — это «элемент массива tArray по индексу, равному значению в tArray[0]». Конвертер ошибочно дал `tArray[tArray0]`, где `tArray0` — отдельная неинициализированная переменная (всегда 0). Все данные пишутся в слот-счётчик.

**Фикс**: вернуть `tArray[tArray[0]]`.

**Как искать**: grep на `tArray\[tArray0\]`, `tArray\[tB\]`, любые `tArray[<не-число>]`.

### 3. ExecuteFunc ненадёжен в Lua

`ExecuteFunc("FuncName")` запускает функцию в **новом потоке** с микроскопическим стеком. Логирование внутри такой функции может крашить поток молча.

**Фикс**: заменить на прямой вызов `FuncName()`.

### 4. GroupAddUnitSimple не работает для pre-placed юнитов

`GroupAddUnitSimple(unit, group)` в WC3 Lua не добавляет здания, созданные через `CreateNUnitsAtLoc`. `GroupAddGroup` и `GroupAddUnit` — работают.

**Фикс**: `GroupAddUnit(group, unit)` (обратный порядок аргументов!).

### 5. Пропущенные/закомментированные глобалы

Конвертер может не создать глобал (`tArray0`), либо закомментировать (`-- tB`). Функция использует nil вместо числа — краш.

**Как искать**: сравнить глобалы в `01_globals.lua` с оригинальным JASS `globals` блоком. Проверить, что все переменные, используемые в коде, инициализированы.

---

## Методика дебага (пошагово)

### Шаг 1: Добавить trace-логи в критические точки

Не угадывать — измерить. Минимальный набор:
- Вход/выход ключевых функций с параметрами
- Результаты фильтров (сколько юнитов нашлось)
- Первый вызов каждого таймер-колбэка (через `LoadBoolean(AiData, -1, ...)` — одноразовый флаг)

Формат: `[ТЕГ] что_происходит параметры`. Пример: `[AIBUILD] TryBuild ENTER pi=1 race=Naga unitId=1852665957`.

### Шаг 2: Запустить probe-map

```bash
HiveWE_cli probe-map --map map.w3x --warcraft "F:/..." --click-after 60 --wait 220 --bridge-script "140:create_ai:2" --probe-log 23Race_probe_log.pld
```

### Шаг 3: Читать лог

```bash
cat "%USERPROFILE%\Documents\Warcraft III\CustomMapData\23Race_probe_log.pld"
```

Искать:
- `[CALLBACK-ERR]` — ошибки с номером строки в `war3map.lua`
- Пропущенные логи (функция не вызвалась)
- Неожиданные nil/0/пустые значения

### Шаг 4: Локализовать ошибку по строке

```bash
# Найти строку в собранном war3map.lua
python -c "lines=open('map.w3x/war3map.lua','rb').read().split(b'\n'); print(lines[XXXX].decode())"
```

### Шаг 5: Починить в split-исходнике, пересобрать, перепроверить

```bash
python build_map_lua.py
python -c "from luaparser import ast; ast.parse(open('map.w3x/war3map.lua','rb').read())"
HiveWE_cli probe-map ...
```

---

## Антипаттерны (чего не делать)

- **Не гадать.** Без логов невозможно понять, вызывается ли функция вообще.
- **Не править war3map.lua напрямую.** Только split-исходники. `war3map.lua` — продукт сборки.
- **Не использовать DisplayTimedTextToPlayer для логов** — в Reforged не пишет в War3Log. Только `BJDebugMsg`.
- **Не ставить ProbeLogWrite внутрь Condition-фильтров** — `GroupEnumUnits*` с фильтрами может не вызвать логирование в condition-контексте.
- **Не запускать probe-map пока WC3 уже открыт** — второй экземпляр не стартует.
- **Не слать чат-команды через `--chat-script`** если между кликом и игрой долгая загрузка — команда потеряется. Использовать `--bridge-script` (preload-based), он буферизуется и выполняется когда игра загрузится.
- **Не дебажить без `-nowfpause`** — WC3 по умолчанию ставит игру на паузу при потере фокуса окна. Без `-nowfpause` таймеры и AI замирают как только переключаешься в редактор/терминал, дебаг невозможен. Всегда передавать `--args "-window -nowfpause"`.
- **Не перезапускать probe-map, не вычистив старые eval-файлы моста.** Мост (см. LIVE_AGENT_BRIDGE.md) читает **последовательные** inbox-файлы `23race_eval_NNNN.pld` через Preloader. Свежезагруженная карта стартует с `EvalNextSeq=1` и **проигрывает все оставшиеся на диске `23race_eval_*.pld` от прошлой сессии как «новые» команды** — твои прошлые хот-патчи/спавны/правки выполняются на новой игре сами собой. Симптом: «как будто сработали команды с предыдущего моста»; в `23race_eval_hb.pld` видно `hb|N` с N сильно >1 сразу после загрузки (игра уже сожрала N-1 старых eval). Это отравляет «чистый» тест: поверх свежего `war3map.lua` ложатся старые (часто багованные) версии функций. **Фикс — перед КАЖДЫМ запуском probe-map удалять все eval-файлы:**
  ```bash
  rm -f "/c/Users/<USER>/Documents/Warcraft III/CustomMapData/23race_eval_"*.pld
  ```
  (inbox `23race_eval_NNNN.pld`, out `23race_eval_out_NNNN.pld`, heartbeat `23race_eval_hb.pld`). `agent_bridge.py reset` чистит часть, но надёжнее снести шаблоном перед стартом. После этого `hb|1` на свежей карте = чисто.

---

## Быстрый старт для нового бага

```bash
# 1. Пересобрать
cd "C:\Games\23 Race\23-Race-Legion"
python build_map_lua.py

# 2. Синтаксис
python -c "from luaparser import ast; ast.parse(open('map.w3x/war3map.lua','rb').read()); print('OK')"

# 3. Закрыть старый WC3 если открыт
#    taskkill //F //IM "Warcraft III.exe"

# 3b. ОБЯЗАТЕЛЬНО вычистить старые eval-файлы моста, иначе свежая карта
#     проиграет их как «новые» команды (см. антипаттерны выше):
rm -f "$env:USERPROFILE\Documents\Warcraft III\CustomMapData\23race_eval_"*.pld

# 4. Probe (важно: detached-запуск чтобы WC3 не закрылся при Ctrl+C)
# Обычный запуск — WC3 умрёт если прервать процесс. Используй Start-Process:
$cli = "C:\Games\HiveWE_VinerX_Edition\build\Release\Release\HiveWE_cli.exe"
Start-Process -FilePath $cli -ArgumentList "probe-map --map `"C:\Games\23 Race\23-Race-Legion\map.w3x`" --warcraft `"F:\Games\Warcraft III`" --args `"-window -nowfpause`" --click-after 60 --wait 300 --bridge-script 140:create_ai:2 --probe-log 23Race_probe_log.pld --keep-open" -NoNewWindow

# -window -nowfpause = окно не паузится при потере фокуса, можно работать в фоне

# 5. Bridge-сессия (после загрузки карты)
# v2: seq синхронится через heartbeat игры — рассинхрона нет. Если пошли
# сплошные TIMEOUT и не выправляется: в игре -bridge:restart:, затем reset.
python agent_bridge.py reset

# Спавн всех AI-рас (pi=2..23):
python agent_bridge.py exec "for pi=2,23 do createAiPlayer(pi) end; return 'done'" --timeout 30

# Проверить расы:
python agent_bridge.py exec "local r={}; for pi=2,23 do r[#r+1]=AiRace[pi] or 'nil' end; return table.concat(r,', ')" --timeout 20

# 6. Читать логи
notepad "%USERPROFILE%\Documents\Warcraft III\CustomMapData\23Race_probe_log.pld"
```
