"""Run existing auditors with one shared Lua AST, retaining individual diagnostics."""
import contextlib
import io
import json
import runpy
import sys
import time
from pathlib import Path

from luaparser import ast

ROOT = Path(__file__).resolve().parents[1]
(ROOT / ".cache/wc3").mkdir(parents=True, exist_ok=True)
original_parse = ast.parse
cached = {}


def shared_parse(source, *args, **kwargs):
    if source not in cached:
        cached[source] = original_parse(source, *args, **kwargs)
    return cached[source]


ast.parse = shared_parse
results = []
for name in sys.argv[1:]:
    (ROOT / ".cache/wc3/audit-progress.txt").write_text(name, encoding="utf-8")
    output = io.StringIO()
    started = time.monotonic()
    sys.argv = [str(ROOT / f"scripts/audit/{name}.py"), str(ROOT / "map.w3x/war3map.lua")]
    if name in ("boolexpr_audit", "intdiv_audit"):
        sys.argv += [str(ROOT / "jass"), str(ROOT / "war3map.j")]
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            runpy.run_path(sys.argv[0], run_name="__main__")
        ok = True
    except Exception as exc:
        output.write(f"{type(exc).__name__}: {exc}")
        ok = False
    results.append({"name": name, "ok": ok, "output": output.getvalue(),
                    "seconds": round(time.monotonic() - started, 3)})
print(json.dumps({"ok": all(r["ok"] for r in results), "results": results}, ensure_ascii=False))
raise SystemExit(0 if all(r["ok"] for r in results) else 1)
