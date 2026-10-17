"""Bounded live scenarios with fresh handshake, assertions and build-tagged reports."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import uuid
from pathlib import Path

from wc3_project import ROOT, CACHE, settings, read, digest, load_sections, source_map


def heartbeat_path(config):
    return Path(config["custom_data"]) / "23race_eval_hb.pld"


def execute(code, timeout=10):
    proc = subprocess.run([sys.executable, str(ROOT / "agent_bridge.py"), "exec", code,
                           "--timeout", str(timeout)], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout + 5)
    return {"ok": proc.returncode == 0, "exit_code": proc.returncode, "output": proc.stdout.strip(),
            "error": proc.stderr.strip()}


def resolve_file(name, scenario_path):
    path = (scenario_path.parent / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("Scenario files must be inside this repository")
    return path


def run(path, launch=False, ready_timeout=180, slot=2, token="scarlet"):
    path = Path(path).resolve()
    scenario = json.loads(read(path))
    if scenario.get("schema_version") != 1 or not isinstance(scenario.get("steps"), list):
        raise ValueError("Scenario requires schema_version=1 and steps list")
    config = settings()
    text = read(ROOT / "map.w3x/war3map.lua")
    if digest(text) != digest("".join(s["text"] for s in load_sections())):
        raise ValueError("Build is out of sync; run build then check before launching")
    if not 0 <= slot <= 23:
        raise ValueError("slot must be 0..23")
    session = uuid.uuid4().hex
    report_dir = CACHE / "scenarios" / session
    report_dir.mkdir(parents=True)
    (report_dir / "source-map.json").write_text(json.dumps(source_map(load_sections()), indent=2), encoding="utf-8")
    report = {"schema_version": 1, "session": session, "scenario": scenario.get("name", path.stem),
              "sha256": digest(text), "ok": False, "steps": [], "launched": launch}
    process = None
    probe_stream = None
    log = Path(config["custom_data"]) / "23Race_probe_log.pld"
    log_offset = log.stat().st_size if log.exists() else 0
    started = time.time()
    try:
        if launch:
            # A new session requires a closed game; never terminate an existing user session.
            proc = subprocess.run(["tasklist", "/FO", "CSV", "/NH"], capture_output=True, text=True)
            if '"Warcraft III.exe"' in proc.stdout or '"Warcraft.exe"' in proc.stdout:
                raise ValueError("Warcraft is already running; use attach mode without --launch")
            reset = subprocess.run([sys.executable, str(ROOT / "agent_bridge.py"), "reset"], capture_output=True, text=True)
            if reset.returncode:
                raise RuntimeError("Bridge reset failed: " + reset.stdout)
            launch_map = report_dir / "map.w3x"
            print("Packaging the requested map for Warcraft -loadfile", flush=True)
            package = subprocess.run([config["cli"], "build-map", "--map", config["map"],
                                      "--out", str(launch_map)], capture_output=True, text=True,
                                     encoding="utf-8", errors="replace", timeout=240)
            (report_dir / "package.json").write_text(package.stdout + package.stderr, encoding="utf-8")
            if package.returncode:
                raise RuntimeError("Map packaging failed; see package.json")
            report["launch_map"] = str(launch_map)
            probe_stream = (report_dir / "probe-output.json").open("w", encoding="utf-8")
            process = subprocess.Popen([config["cli"], "probe-map", "--map", str(launch_map),
                                        "--warcraft", config["warcraft"], "--args", "-window -nowfpause",
                                        "--click-after", "60", "--chat-after", "95", "--chat-text", "-bridge:eval:on",
                                        "--wait", str(ready_timeout), "--probe-log", log.name, "--keep-open",
                                        "--ready-file", str(heartbeat_path(config)), "--stop-when-ready"],
                                       stdout=probe_stream, stderr=subprocess.STDOUT,
                                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            started = time.time()  # readiness timeout starts after packaging
        heartbeat = Path(config["custom_data"]) / "23race_eval_hb.pld"
        deadline = time.monotonic() + ready_timeout
        print(f"Waiting for fresh bridge heartbeat; session={session}", flush=True)
        while time.monotonic() < deadline:
            if heartbeat.exists() and heartbeat.stat().st_mtime >= started - 2:
                break
            if process and process.poll() is not None and process.returncode:
                raise RuntimeError("probe-map exited before readiness; see probe-output.json")
            time.sleep(0.25)
        else:
            raise TimeoutError("No fresh bridge heartbeat; enable -bridge:eval:on in the loaded map")
        # A nonce response proves that this is a fresh result, not a stale outbox.
        handshake = execute(f"__AgentScenarioSession={json.dumps(session)}; "
                            f"ScenarioSlot={slot}; ScenarioToken={json.dumps(token)}; return __AgentScenarioSession")
        report["steps"].append({"name": "handshake", **handshake})
        if not handshake["ok"] or handshake["output"].split(None, 1)[-1] != session:
            raise RuntimeError("Fresh bridge handshake failed")
        for step in scenario["steps"]:
            name = step.get("name", "step")
            timeout = float(step.get("timeout", 10))
            if not 0 < timeout <= 60:
                raise ValueError("Step timeout must be 0..60 seconds")
            code = read(resolve_file(step["file"], path)) if "file" in step else step["lua"]
            wrapped = f"assert(__AgentScenarioSession=={json.dumps(session)}, 'session changed'); " + code
            poll = float(step.get("poll_for", 0))
            if not 0 <= poll <= 300:
                raise ValueError("poll_for must be 0..300 seconds")
            deadline = time.monotonic() + poll
            print(f"Running {name}", flush=True)
            while True:
                result = execute(wrapped, timeout)
                if result["ok"] or time.monotonic() >= deadline:
                    break
                time.sleep(1)
            if "expected" in step and result["ok"]:
                result["ok"] = result["output"].split(None, 1)[-1] == str(step["expected"])
            report["steps"].append({"name": name, **result})
            if not result["ok"]:
                raise RuntimeError(f"Scenario assertion failed: {name}: {result['output']}")
        report["ok"] = True
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired, TimeoutError) as exc:
        report["error"] = str(exc)
    finally:
        if process and process.poll() is None:
            # Stop only our probe supervisor; --keep-open preserves the game for inspection.
            try:
                process.wait(timeout=12)
            except subprocess.TimeoutExpired:
                process.terminate(); process.wait(timeout=5)
        if probe_stream:
            probe_stream.close()
        if log.exists():
            data = log.read_bytes()
            new = data[log_offset:] if len(data) >= log_offset else data
            (report_dir / "probe-log.pld").write_bytes(new)
            errors = [line for line in new.decode("utf-8", errors="replace").splitlines()
                      if "[CALLBACK-ERR]" in line or "[BRAINERR]" in line]
            report["log_errors"] = errors
            if errors:
                report["ok"] = False
        report["seconds"] = round(time.time() - started, 2)
        report["artifact"] = str(report_dir / "report.json")
        (report_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", type=Path)
    parser.add_argument("--launch", action="store_true")
    parser.add_argument("--ready-timeout", type=int, default=180)
    parser.add_argument("--slot", type=int, default=2)
    parser.add_argument("--token", default="scarlet")
    args = parser.parse_args()
    if not 1 <= args.ready_timeout <= 600:
        parser.error("ready-timeout must be 1..600 seconds")
    report = run(args.scenario, args.launch, args.ready_timeout, args.slot, args.token)
    print(json.dumps(report, ensure_ascii=False), flush=True)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
