---
name: wc3-tools
description: Компактный поиск Lua-символов, ссылок и контекста, точный маппинг строк сборки, диагностика окружения и проверка карты 23 Race Forever.
---

# Source tools

Run from the repository root. Edit manifest-listed split sections and rebuild; never edit generated war3map.lua.

```powershell
python scripts/wc3_tools.py doctor
python scripts/wc3_tools.py symbol AiBrainArmyTick --limit 5
python scripts/wc3_tools.py refs AiBrainArmyTick --limit 10
python scripts/wc3_tools.py context AiBrainArmyTick --max-lines 40
python scripts/wc3_tools.py line 34512 -c 3
python scripts/wc3_tools.py rawcode h014 -l 10
```

Prefer bounded queries before reading large files. symbol/refs/context support JSON; the index cache is keyed by source content. Line mapping includes shared boundary lines and rejects source/build mismatch. Old probe logs require the source map and hash of that particular build.

After edits run build, then check --kind lua or check --kind ai. verify/check do not rebuild implicitly. Required failures return nonzero; migration warnings remain visible in .cache/wc3 reports.

Use audit --baseline docs/audit-baseline.json for handle/callback changes. A baseline records known findings, not proof of safety. Update it only after evaluating findings. Paths: wc3.local.example.json; overrides: gitignored wc3.local.json. See docs/TOOLING_WORKFLOW.md.

