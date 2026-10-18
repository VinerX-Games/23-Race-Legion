---
name: wc3-live-scenarios
description: Повторяемые игровые проверки готовности карты, роста AI и лимитов зданий через live bridge с assertions и отчётами по сборке.
---

# Live scenarios

Use scripts/wc3_scenarios.py and tests/scenarios/*.json. See docs/TOOLING_WORKFLOW.md for the schema.

```powershell
python scripts/wc3_scenarios.py tests/scenarios/ready.json --launch
python scripts/wc3_scenarios.py tests/scenarios/ai-growth.json --slot 2 --token scarlet
python scripts/wc3_scenarios.py tests/scenarios/ai-build-caps.json --slot 2
```

--launch requires a closed game and clears old eval files. Attach mode requires -bridge:eval:on in the running map. Fresh heartbeat and nonce response establish readiness; an OS lock prevents concurrent sequence publication.

Execute action steps once. poll_for retries only explicitly repeatable assertions without side effects. Choose an unused bot slot; ai-growth creates a bot. Hot patches do not update split sources automatically.

Reports, build hash/source map and new log lines are stored under .cache/wc3/scenarios/<session>/. Timeout means failure. Reset old files before a new launch; the session nonce verifies fresh responses but does not replace a game-side session protocol. Never roll back EvalNextSeq.

