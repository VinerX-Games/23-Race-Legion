# Рабочий цикл инструментов карты

## Окружение

Команды выполнять из корня репозитория. Установить `python -m pip install -r tests/requirements-dev.txt`. Проверить пути и зависимости: `python scripts/wc3_tools.py doctor`. Если нужны другие пути, скопировать `wc3.local.example.json` в gitignored `wc3.local.json`. Переменные `HIVEWE_CLI`, `WC3_MAP`, `WC3_WARCRAFT`, `WC3_CUSTOM_DATA`, `WC3_MODEL_CLI`, `MDLXL_HOME` имеют приоритет над файлом. Настройка `map` относится к инспекции object data и запуску; Lua исходники этого репозитория определяет manifest.

## Поиск и проверка Lua

```powershell
python scripts/wc3_tools.py symbol AiBrainArmyTick --limit 5 --json
python scripts/wc3_tools.py refs AiBrainArmyTick --limit 10
python scripts/wc3_tools.py context AiBrainArmyTick --max-lines 30
python scripts/wc3_tools.py line 9874 -c 3
python scripts/wc3_tools.py build
python scripts/wc3_tools.py check --kind ai
```

`symbol` индексирует именованные функции, в том числе `local F = function`. `refs` показывает использования токена без строк и комментариев; это лексические ссылки, не граф разрешённых вызовов. Для переменных остаётся `find <name> -t var`. Контекст функций учитывает вложенные блоки. Индекс хранится по SHA256 содержимого, без повторного парсинга неизменённого монолита.

Build создаёт `.cache/wc3/source-map.json`. Сборщик сохраняет исходную конкатенацию и не добавляет переводы строк между секциями. Поэтому одна строка может соответствовать двум файлам. Для старого лога:

```powershell
python scripts/wc3_tools.py line 9874 --source-map saved-source-map.json --build-hash HASH
```

Если исходник изменился после снимка, выводится исходное расположение без контекста текущего файла. Обычный маппинг отказывается работать при рассинхронизации сборки и исходников.

`verify` и `check` не пересобирают карту. Обязательные сбои дают ненулевой exit code; подробности сохраняются в `.cache/wc3/verify.json` или `check.json`. AI-валидатор читает manifest и разделяет ошибки схемы и замечания миграции; `--strict-warnings` запрещает также предупреждения. `check --kind docs` оставляет проверку ссылок и примеров автору.

## Статический аудит

```powershell
python scripts/wc3_tools.py audit --baseline docs/audit-baseline.json
```

Аудиторы используют один AST вместо четырёх полных разборов Lua. Baseline содержит известные находки, а не доказательство их безопасности. Новые находки или сбой аудитора дают ненулевой код. Для осознанного обновления: та же команда с `--update-baseline`. Полные результаты и исчезнувшие находки сохраняются в отчёте.

## Object data

```powershell
python scripts/wc3_hivewe.py search "Работник" --limit 5
python scripts/wc3_hivewe.py bulk h014,h05U --fields name,hp,builds --limit 5
python scripts/wc3_hivewe.py tree h014 --depth 2
python scripts/wc3_hivewe.py validate-map --limit 5
python scripts/wc3_hivewe.py diff before-map after-map --limit 10
```

Diff сравнивает поля всех типов объектов и разрешённые названия/суффиксы WTS. Полные JSON сохраняются в `.cache/wc3/hivewe-*.json`; stdout ограничен. Базовая проверка ссылок не исправляет существующие ошибки карты автоматически.

Пакет правок задаётся файлом:

```json
{"operations":[{"type":"unit","id":"h014","field":"hp","value":241}]}
```

`transaction plan.json` выполняет preview на временной копии, включая `war3mapSkin.*`; проверяются повторное чтение значения, новые ошибочные ссылки и отсутствие посторонних изменений effective fields. `--apply` записывает проверенный результат. Перед записью закрыть карту в GUI HiveWE. Журнал сохраняет исходные object data, Skin-таблицы и WTS. `recover <journal.json>` восстанавливает их, если не было посторонних изменений. Это журналируемая запись нескольких файлов, а не одна атомарная операция для всего набора. Текущие транзакции поддерживают изменения полей; создание/удаление объектов выполнять отдельными нативными командами с preview.

## Игровые сценарии

```powershell
python scripts/wc3_scenarios.py tests/scenarios/ready.json --launch
python scripts/wc3_scenarios.py tests/scenarios/ai-growth.json --slot 2 --token scarlet
python scripts/wc3_scenarios.py tests/scenarios/ai-build-caps.json --slot 2
```

Новый запуск требует закрытой игры и сначала пакует карту в отдельный MPQ для `-loadfile`; attach — работающей карты с `-bridge:eval:on`. Сценарий содержит `schema_version: 1`, `steps`, а каждый шаг — `name`, `lua` либо `file`, необязательные `expected`, `timeout` (до 60 секунд), `poll_for` (до 300 секунд). Повторять можно только assertions без побочных эффектов. Сценарий роста создаёт бота; выбирать свободный слот.

Раннер ждёт свежий heartbeat, подтверждает nonce, проверяет ответы и сохраняет отчёт/source map/новые строки лога в `.cache/wc3/scenarios/<session>/`. Тайм-аут и несовпадение результата являются провалом. Хеш отчёта относится к запрошенному локальному скрипту; attach не доказывает идентичность байтов уже загруженной карты. ОС-блокировка моста исключает параллельную отправку одной последовательности. Перед новым запуском старые eval-файлы удаляются; не делать reset во время чужой команды.

В текущем Lua `BridgeStart` отключает старые scheduled command files и работает в live-only режиме. Поэтому `--bridge-script create_ai` не заменяет включение eval через чат и последующий вызов live bridge.

## Модели

`scripts/wc3_models.py info|validate|textures|render|scan <model>` использует существующий MDLxL CLI. Обёртка сохраняет модели и создаёт отдельные превью. Для рендера указывать новый `--out`; для диагностики ограничивать `--limit`. `--no-casc` не подтверждает отсутствие стандартных текстур. Проверять источники найденных текстур: внешний CLI может искать в соседних картах.

## Изменения HiveWE

Исходный форк: [VinerX/HiveWE](https://github.com/VinerX/HiveWE), базовый коммит указан в `patches/README.md`. Исследованный код CLI находится в `src/cli`, GUI моделей — в `src/model_editor`; MDLxL используется отдельно. В `patches/` сохранён воспроизводимый патч; `scripts/wc3_build_hivewe.py` собирает CLI без Qt. Установленный exe сохраняется; `--activate` выбирает новую сборку через локальную конфигурацию.

Нативный `validate-map` дополнительно проверяет WTS; `--assets` проверяет ассеты изменённых/созданных объектов, учитывая варианты имени и формата. Эти предупреждения требуют оценки замен и режима SD/HD. Для размещённых препятствий использовать `python scripts/wc3_pathing.py islands --limit 5` или `path --from=0,0 --to=1000,1000`. Скрипт читает `.doo`, запрашивает footprints пакетно, берёт текстуры из карты/CASC и вызывает HiveWE с временным WPM. Кеш учитывает содержимое данных карты, локальных footprints, версию игры и CLI. Сохраняются статические flags, проверяются повороты и границы. Произвольный поворот асимметричной footprint отклоняется. Состояние во время игры — уничтоженные деревья, открытые ворота, движущиеся юниты — этим снимком не проверяется.
