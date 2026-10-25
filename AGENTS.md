# Repository Guidelines

## Map Name

Since 1.6.515 the map is called **23 Race Forever** (formerly 23 Race Legion). Version numbers continue the Legion
line without reset: 1.6.514 (last Legion) → 1.6.515 (first Forever) → 1.6.516 …

- In-game name: WTS `STRING 003` = `23 Race Forever 1.6.NNN` (the welcome panel reads the version from it).
- `version.txt` stays `23_race_1_6_NNN`; release file `23_Race_Forever_v1_6_NNN.w3x`, tag `v23_race_1_6_NNN`.
- Use "23 Race Forever" in all new texts, docs, release notes and commits. The GitHub repo is still
  `VinerX-Games/23-Race-Legion`; keep local `23-Race-Legion` paths. "Legion" in Demon race code
  (Burning Legion, `Fin7Legion`, AI token `legion`) is unrelated to the map name.

## Выбор рас и подфракций

Основной интерфейс — кастомная панель `80_runtime/_ui/63_race_picker.lua`.
Для драконов, наг/мурлоков и Старой Орды используется второй экран этой панели
до выдачи стартовых юнитов. Страницы способностей кольца — резервный старый путь.
Не описывать основной выбор как исследование в главном здании или выбор через
`dra1`. Читать [docs/RACE_SELECTION.md](docs/RACE_SELECTION.md): там актуальный
путь игрока, общие обработчики игроков/AI и реализованный состав Старой Орды.

## Project Structure & Module Organization

23 Race Forever is a Warcraft III: Reforged map using Lua 5.3. The unpacked `map.w3x/` directory contains map data, imported models, textures, and other assets.

- `map.w3x/_lua/monolith_split/sections/`: canonical Lua sources, including runtime triggers, AI modules, and race definitions.
- `map.w3x/_lua/monolith_split/manifest.json`: section inclusion and concatenation order.
- `map.w3x/war3map.lua`: generated map script. Edit sections, rebuild, and commit both sources and generated output; never edit this file directly.
- `tests/`: Python regression tests and live Lua checks.
- `scripts/`: source transformations, audits, and Warcraft inspection tools.
- `docs/`: subsystem documentation; start with `docs/README.md` and `docs/PROJECT_MAP.md`.
- `jass/` and `war3map.j`: legacy JASS material.

## Build, Test, and Development Commands

Run commands from the repository root:

```powershell
python -m pip install -r tests/requirements.txt
python -m pip install luaparser
python build_map_lua.py
python build_map_lua.py --check-only
python -m unittest discover -s tests -v
python scripts/wc3_tools.py verify
```

These install test/syntax dependencies, rebuild Lua, report source/output hash agreement, run regressions, and perform combined verification. Check `matches_current=True` in the hash report. `build.bat` rebuilds and parses Lua interactively. For in-game testing, use `.\_run.bat` after adjusting its local HiveWE and Warcraft paths; it launches a probe session with bot creation configured.

## Coding Style & Naming Conventions

Use four-space indentation in Python and follow surrounding Lua indentation. Preserve existing Warcraft globals and function names. Python helpers use `snake_case`; Lua AI functions commonly use `Ai` prefixes. Register new sections in the manifest in dependency order. Keep files UTF-8; Russian comments, documentation, and commit descriptions are common. Syntax validation uses `luaparser`; preserve local formatting.

Для создания новых иконок использовать [wc3-icon-authoring](.agents/skills/wc3-icon-authoring/SKILL.md): там сохранены утверждённый пользователем рисованный стиль Warcraft III Classic, образец и шаблон запросов.

## Обязательный стандарт игровых текстов

При добавлении или изменении юнитов, героев, зданий, способностей, исследований и интерфейсных текстов обязательно применять [docs/UI_TEXT_STYLE.md](docs/UI_TEXT_STYLE.md) и единую палитру [docs/UI_COLOR_PALETTE.md](docs/UI_COLOR_PALETTE.md). Эти правила действуют для всех рас, object data и текстов, формируемых Lua.

- Короткая подсказка содержит только название. Убирать «Нанять», «Обучить», «Призвать», «Исследовать», «Улучшить до», «Построить» и аналогичные командные слова, включая английские варианты. Горячую клавишу в название не писать — игра выводит её сама; клавишу задавать полем хоткея. Явно указанный уровень многоуровневого исследования допустим.
- Подробное описание обязательно начинается с метки типа прописными буквами и двоеточием: «ЮНИТ:», «ГЕРОЙ:», «ЗДАНИЕ:», «ИССЛЕДОВАНИЕ:», «СПОСОБНОСТЬ:», «ПРЕДМЕТ:» и т. п. После метки — пробел и описание назначения. Метка второстепенного цвета B99D66, затем основной цвет CED4DA; в короткое название её не добавлять.
- Герой: роль, затем список «Способности:» с кратким описанием каждой; в конце допустимые цели атаки, если герой атакует.
- Юнит: роль, затем его способности и их эффекты; в конце допустимые цели атаки, если юнит атакует.
- Исследование: точный эффект, явный список затрагиваемых юнитов/зданий/способностей, уровень для многоуровневых исследований.
- Здание: назначение, списки «Обучает:» и/или «Исследования:» по фактическому содержимому; отмечать дополнительные функции. Пункты списков здания — только названия, без пояснений. Пустые разделы не добавлять.
- Описания и списки должны соответствовать текущим object data и Lua: не придумывать доступные способности, юнитов, эффекты или числа. При изменении механики обновлять связанные тексты.
- Всегда использовать цвета по утверждённым семантическим ролям; цвета со скриншотов не копировать. Перед завершением проверять короткие названия, списки, цветовые сбросы и соответствие механике.

## База зависимостей рас — обновлять обязательно

[docs/techtree/](docs/techtree/README.md) — сгенерированная база: что каждая раса строит, обучает, исследует, какие у объектов способности, требования, стоимость, хоткеи. Для вопросов о зависимостях читать её, а не разбирать object data карты. JSON руками не править.

Любое изменение зависимостей или свойств объектов рас (добавление/удаление/переименование юнита, героя, здания, способности, исследования, предмета; списки строит/обучает/исследует/способности; требования, стоимость, ОЗ, время, хоткеи, уровни; стартовые юниты и технологии в Lua) сопровождать в том же коммите перегенерацией: `python scripts/export_techtree.py`, затем `python scripts/export_techtree.py --check` должен вывести `OK`. Если HiveWE_cli недоступен — указать это в коммите/PR.

## Экономия контекста и токенов

Для задач игровых текстов соблюдать [docs/UI_TEXT_WORKFLOW.md](docs/UI_TEXT_WORKFLOW.md): фиксировать исходный охват, читать и править пакетно, переиспользовать подтверждённые факты и запускать только проверки, необходимые по изменённым источникам. Общая зависимость не расширяет задачу автоматически до всей карты. Не создавать дублирующие скрипты/отчёты на каждый объект; использовать существующие инструменты и краткую контрольную запись в TODO. Повторное исследование или повтор успешной проверки должно иметь конкретное основание: изменившиеся входные данные, ошибка либо новое противоречие.

Markdown-правки проверять по diff и ссылкам; игровые и полные регрессионные проверки ради изменения документации не запускать. Если пользователь берёт игровые проверки на себя, агент не запускает игру и не оставляет свою статическую работу открытой только из-за отсутствия игрового прогона. Это не отменяет требований к достоверности и полноте оставшегося охвата.

## Testing Guidelines

Tests use `unittest` and `lupa.lua53` with mocked Warcraft natives. Name files `test_*.py` and methods `test_<behavior>`. Add regression coverage for changed behavior; no numeric coverage target is documented. Run the suite and validate gameplay changes in Warcraft III, since mocks cannot verify engine behavior.

## Commit & Pull Request Guidelines

Follow existing Conventional Commits, such as `fix(ai): ...`, `feat(nightelf): ...`, and `chore(release): ...`. Keep changes focused. PRs should explain gameplay effects, link relevant issues, report automated and in-game validation, and include screenshots for visible changes.

## Warcraft Runtime Constraints

Keep multiplayer logic deterministic: use Warcraft random natives and avoid local-player state mutations. Release temporary groups and locations; avoid nested reuse of global scratch groups. Consult `docs/DEBUG_WC3_MAP.md` before changing native callbacks.
