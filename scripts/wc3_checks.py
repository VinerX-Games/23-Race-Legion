"""Strict, bounded verification and baseline-aware audit runner."""
from __future__ import annotations

import json
import subprocess
import sys
import time
import re
from pathlib import Path

try:
    from .wc3_project import ROOT, CACHE, read, load_sections, digest
except ImportError:
    from wc3_project import ROOT, CACHE, read, load_sections, digest


def run_check(name, command, timeout=180):
    start = time.monotonic()
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout)
        return {"name": name, "ok": proc.returncode == 0, "exit_code": proc.returncode,
                "seconds": round(time.monotonic() - start, 3),
                "output": (proc.stdout + proc.stderr).strip()}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"name": name, "ok": False, "exit_code": -1,
                "seconds": round(time.monotonic() - start, 3), "output": str(exc)}


def verify(timeout=180):
    python = sys.executable
    checks = [run_check("source-sync", [python, str(ROOT / "build_map_lua.py"), "--check-only"], timeout),
              run_check("lua-syntax", [python, "-c", "from luaparser import ast; "
                        "ast.parse(open('map.w3x/war3map.lua',encoding='utf-8-sig').read())"], timeout),
              run_check("ai-races", [python, str(ROOT / "scripts/validate_ai_races.py"), "--json"], timeout),
              run_check("unittest", [python, "-m", "unittest", "discover", "-s", "tests", "-v"], timeout)]
    return {"schema_version": 1, "ok": all(c["ok"] for c in checks), "checks": checks}


def present(report, json_output=False, max_lines=12, artifact=None):
    if artifact:
        path = Path(artifact); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if json_output:
        compact = dict(report)
        compact["checks"] = [{**c, "output": "\n".join(line[:500] for line in c["output"].splitlines()[:max_lines])}
                             for c in report.get("checks", [])]
        for key in ("findings", "new", "resolved"):
            if isinstance(compact.get(key), list):
                compact[key + "_total"] = len(compact[key])
                compact[key] = compact[key][:max_lines]
        print(json.dumps(compact, ensure_ascii=False))
    else:
        for check in report.get("checks", []):
            print(f"[{'OK' if check['ok'] else 'FAIL'}] {check['name']} ({check['seconds']}s)")
            if not check["ok"] or check["name"] == "ai-races":
                if check["name"] == "ai-races":
                    try:
                        data = json.loads(check["output"])
                        print(f"races={data['races']} errors={data['errors']} warnings={data['warnings']}")
                    except (ValueError, KeyError):
                        print(check["output"][:500])
                else:
                    for line in check["output"].splitlines()[:max_lines]:
                        print(line[:500])
        if artifact:
            print(f"Full report: {artifact}")
        if "note" in report:
            print(report["note"])
        if "new" in report:
            print(f"Audit findings={len(report['findings'])}; new={len(report['new'])}; resolved={len(report['resolved'])}")
            for finding in report["new"][:max_lines]:
                print(finding[:500])
    return 0 if report["ok"] else 1


AUDITORS = ("scope_leak_audit", "closure_nil_audit", "boolexpr_audit", "reentry_audit",
            "leak_audit", "intdiv_audit")


def audit(baseline=None, update=False, timeout=180):
    checks, findings = [], []
    combined = run_check("audit-driver", [sys.executable, str(ROOT / "scripts/wc3_audit_driver.py"), *AUDITORS], timeout)
    try:
        results = json.loads(combined["output"])["results"]
    except (ValueError, KeyError):
        return {"ok": False, "checks": [combined], "findings": [], "new": [], "resolved": []}
    for result in results:
        name = result["name"]
        check = {**combined, **result, "exit_code": 0 if result["ok"] else 1}
        checks.append(check)
        for line in check["output"].splitlines():
            if line and line[0].isdigit():
                findings.append({"auditor": name, "text": line})
    keys = {f["auditor"] + "|" + re.sub(r"^\d+\s*[:|]?\s*", "", f["text"]) for f in findings}
    known = set()
    if baseline and Path(baseline).exists():
        known = set(json.loads(read(baseline))["findings"])
    if update:
        if not baseline:
            raise ValueError("--update-baseline requires --baseline")
        if not all(c["ok"] for c in checks):
            raise ValueError("Cannot update baseline when an auditor failed")
        path = Path(baseline); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"schema_version": 1, "sha256": digest(read(ROOT / 'map.w3x/war3map.lua')),
                                    "findings": sorted(keys)}, ensure_ascii=False, indent=2), encoding="utf-8")
        known = keys
    return {"schema_version": 1, "ok": all(c["ok"] for c in checks) and not (keys - known),
            "checks": checks, "findings": findings, "new": sorted(keys - known),
            "resolved": sorted(known - keys)}
