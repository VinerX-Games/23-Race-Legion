"""Read-only model diagnostics and previews through the existing MDLxL engine."""
import argparse
import json
import os
import hashlib
import subprocess
from pathlib import Path

from wc3_project import CACHE, settings, digest


def inspect(command, model, limit=8, no_casc=False, output=None):
    config = settings()
    args = ["node", config["model_cli"], command, str(model)]
    if command in ("textures", "render"):
        args += ["--textures", config["map"]]
        if no_casc:
            args += ["--no-casc"]
    if command == "scan":
        args += ["--limit", str(limit)]
    if command == "render":
        args += ["-o", str(output), "--size", "384", "--views", "front,34"]
    env = {**os.environ, "MDLXL_HOME": config["mdlxl_home"], "WC3_DIR": config["warcraft"]}
    proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=120, env=env)
    try:
        data = json.loads(proc.stdout)
    except ValueError:
        return {"ok": False, "error": (proc.stderr or proc.stdout)[:2000]}
    errors = []
    diagnostics = data.get("diagnostics", [])
    if isinstance(diagnostics, list):
        errors = [d for d in diagnostics if d.get("severity") == "error"]
    elif isinstance(diagnostics, dict) and diagnostics.get("errors", 0):
        errors = diagnostics.get("first", [])
    return {"ok": proc.returncode == 0 and data.get("ok", True) and not errors,
            "sha256": hashlib.sha256(Path(model).read_bytes()).hexdigest() if Path(model).is_file() else None,
            "result": data, "errors": errors}


def compact(value, limit):
    if isinstance(value, list):
        if len(value) > limit:
            return {"count": len(value), "head": [compact(v, limit) for v in value[:limit]]}
        return [compact(v, limit) for v in value]
    if isinstance(value, dict):
        return {key: compact(item, limit) for key, item in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("info", "validate", "textures", "render", "scan"))
    parser.add_argument("model")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--no-casc", action="store_true")
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("limit must be positive")
    CACHE.mkdir(parents=True, exist_ok=True)
    output = args.out or CACHE / "model-preview.png"
    if args.command == "render" and output.exists():
        parser.error("Preview output exists; choose a new --out path")
    try:
        report = inspect(args.command, args.model, args.limit, args.no_casc, output)
    except (OSError, subprocess.TimeoutExpired) as exc:
        report = {"ok": False, "error": str(exc)}
    artifact = args.artifact or CACHE / f"model-{args.command}.json"
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    short = compact(report, args.limit)
    if args.command == "info" and "result" in short:
        short["result"] = {key: short["result"][key] for key in
                           ("name", "version", "format", "counts", "triangles", "vertices", "diagnostics")
                           if key in short["result"]}
    short["artifact"] = str(artifact)
    print(json.dumps(short, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
