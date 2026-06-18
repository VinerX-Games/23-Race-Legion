# Python-скрипты проекта

Все скрипты — `.py` файлы в корне, `scripts/` и поддиректориях.
Объединены в группы по назначению.

---

## СБОРКА — канонический build-chain

| Файл | Описание |
|---|---|
| `build_map_lua.py` | **Основной сборочный скрипт.** Собирает `map.w3x/war3map.lua` из split-исходников (`_lua/monolith_split/`) по `manifest.json`. Флаги: `--check-only` — проверка SHA256 без перезаписи. |
| `split_bundle.py` | Разрезает multi-race триггерные бандлы (`80_runtime/triggers/`) на per-race файлы (`races/*.lua`) по границам триггеров `InitTrig_Race_*`. Byte-identical после конкатенации. |
| `resplit_runtime.py` | Пересекает файлы `80_runtime/` по границам функций. Авто-разрез оставлял файлы с середины функции → не парсились. Этот скрипт гарантирует, что каждый файл начинается с целой функции. Флаг `--write`. |

---

## СКРИПТЫ В SCRIPTS/ — AI-данные и валидация

| Файл | Описание |
|---|---|
| `scripts/validate_ai_races.py` | **Валидатор определений AI-рас.** Читает `82_ai_races.lua` + `82_ai_races/*.lua` и проверяет: required fields (tokens, weight, altar, start), дубликаты FourCC ID, gate/branch-ссылки (определены ли в таблице `gates`/`branches`), production-здания (есть ли в buildings), ecoWeights, legacy-фоллбэки, неиспользуемые gates, конфликты токенов. Выдаёт сводную таблицу. |
| `scripts/split_ai_races_bundle.py` | **Раcщепляет `82_ai_races.lua`** на отдельные per-race файлы в `82_ai_races/`. Извлекает блоки `RegisterAiRace("Имя", {...})`, сохраняет в `NN_имя.lua`, обновляет `manifest.json`. |
| `scripts/migrate_workers.py` | **Мигрирует 22 AI-расы** с процедурного production-table worker на декларативную секцию `worker = { id, cap, from }`. Удаляет старые production-записи для town-hall зданий, вставляет новый worker-блок. Пропускает сложные расы (Scarlet, ForestTrolls, Goblins). |

---

## ИДИОМАТИЗАЦИЯ — приведение vJASS→Lua к идиоматичному Lua

| Файл | Описание |
|---|---|
| `idiom_engine.py` | **Движок AST-идиоматизации.** Конкатенирует split-файлы как `build_map_lua.py`, парсит монолит через `luaparser`, применяет трансформы (offset→замена), верифицирует AST-перепарсом. Используется всеми `idiom_*.py` скриптами. |
| `idiom_conditions.py` | Схлопывает condition-функции: `if not(E) then return false end ... return true` → `return E`. |
| `idiom_conditions_pos.py` | Позитивная форма: `if E then return true end ... return false` → `return E1 or E2`. |
| `idiom_strconcat.py` | Фикс строковой конкатенации: `+` → `..`. В JASS `+` работает для строк, в Lua — арифметика, вызывает рантайм-краш. |
| `idiom_booltrue.py` | Убирает `== true`/`== false`/`~= true`/`~= false`. Код пришёл из статически типизированного JASS. |
| `idiom_parens.py` | Снимает лишние скобки в `return (X)`, `if (X)`, `while (X)`, `until (X)` через AST-guard. |
| `idiom_emptyelse.py` | Убирает пустые else-ветки: `if X then ... else end` → `if X then ... end`. Детект через AST. |

---

## КОНВЕРТАЦИЯ — механические исправления vJASS→Lua артефактов

| Файл | Описание |
|---|---|
| `null_to_nil.py` | Заменяет `null` на `nil` во всех split-файлах. |
| `inline_condition_vars.py` | Заменяет присваивания `Condition(func)` в переменные на прямые ссылки. Обрабатывает `b`, `bex`, `Boolexpr`, `udg_Boolexpr` с учётом скоупа. |
| `inline_spell_conditions.py` | Инлайнит проверки `GetSpellAbilityId` из Condition в Action — удаляет разделение Condition+Action. |
| `group_condition_to_direct.py` | Заменяет `GroupEnum* + Condition(func)` на прямую ссылку на функцию. Line-based подход. |
| `for_loop_convert.py` | Конвертирует `bj_forLoopA/B` GUI-циклы в идиоматичные Lua `for`-циклы. |
| `timer_to_closure.py` | Конвертирует таймер+хештаблицу утилиты в замыкания. Line-based парсинг. |
| `timer_closure_batch2.py` | Второй проход: 5 простых one-shot таймеров → замыкания. |
| `fix_orphaned_vars.py` | Чинит осиротевшие `udg_Boolexpr` ссылки и битые bex-присваивания. |
| `fix_cleanup.py` | Одноразовая чистка артефактов в `80_generated_runtime.lua`. |
| `fix_encodings.py` | Фикс кодировок: перезаписывает скрипты с явным указанием кодировки. |
| `check_colors.py` | Поиск строк чат-команд, используемых в colour-триггерах. |
| `collapse_colors.py` | Схлопывает 24 colour-триггера в одну функцию с таблицей. |

---

## МОСТ — живая отладка

| Файл | Описание |
|---|---|
| `agent_bridge.py` | **Live Agent Bridge.** Исполняет произвольный Lua в работающей карте WC3 через eval-канал (Preloader-файлы). Режимы: `exec "code"`, `exec --file`, `--watch` (мгновенный ответ), `reset` (очистка inbox/out/hb). Использует heartbeat-синхронизацию v2. |
| `audit.py` | Анализирует паттерны `Condition()` в runtime-файле. |
| `_find_error.py` | Утилита бинарного поиска ошибки парсинга в Lua-файлах через `luaparser`. |

---

## СКРИПТЫ В ПОДДИРЕКТОРИЯХ

| Файл | Описание |
|---|---|
| `lua_rewrite/build_lua_map.py` | Совместимая обёртка над `build_map_lua.py` (устаревшая). |
| `lua_rewrite/normalize_converted_lua.py` | Механическая нормализация JASS→Lua артефактов: `Condition(function Foo)` → `Condition(Foo)`, `//` → `--`, `!=` → `~=`, `local array` → `local = {}`, `loop` → `while true do`. Плюс FourCC-нормализация строковых rawcode'ов. |
| `lua_rewrite/split_war3map.py` | Детерминированно разбивает `war3map.lua` на split-файлы и обратно. |
| `lua_rewrite/set_w3i_lua_flag.py` | Устанавливает Lua-флаг в `war3map.w3i`. |
| `map.w3x/_lua/monolith_split/sections/update_manifest.py` | Обновляет `manifest.json` при изменениях в секциях. |
| `map.w3x/_lua/monolith_split/sections/update_manifest2.py` | Вторая версия. |
| `map.w3x/_lua/monolith_split/sections/update_manifest3.py` | Третья версия. |
