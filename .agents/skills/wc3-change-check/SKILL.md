---
name: wc3-change-check
description: Выбор и выполнение проверок изменений Lua, AI, object data и документации карты 23 Race Forever с кратким результатом и полными артефактами.
---

# Check a change

Inspect git diff --stat and git status --short, including untracked files.

- Lua/AI: edit split sections, run python scripts/wc3_tools.py build, then check --kind lua or check --kind ai.
- Object data: check --kind objects; review binary changes using wc3_hivewe.py diff between map snapshots.
- Documentation: verify links and actual commands; check --kind docs does not claim gameplay validation.
- Release: check --kind release plus relevant live scenarios.

check never rebuilds silently. Nonzero exit means failure. Report a compact status and relevant errors; full output is in .cache/wc3/check.json. AI migration warnings differ from schema errors.

For callback/group/timer/handle changes run audit --baseline docs/audit-baseline.json. Do not refresh a baseline just to obtain success. See docs/TOOLING_WORKFLOW.md for scenario commands. State which checks actually ran and the limits of mocks and static pathing.

