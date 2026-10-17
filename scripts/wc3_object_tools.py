"""Compact HiveWE adapters, semantic object diff, validation and staged edits."""
from __future__ import annotations

import json
import hashlib
import os
import shutil
import tempfile
import math
from pathlib import Path

from wc3_project import ROOT, CACHE, settings, read

TYPES = {"unit": "w3u", "ability": "w3a", "item": "w3t", "upgrade": "w3q",
         "buff": "w3h", "doodad": "w3d", "destructible": "w3b"}
EDIT_FILES = ({f"war3map.{extension}" for extension in TYPES.values()} |
              {f"war3mapSkin.{extension}" for extension in TYPES.values()} | {"war3map.wts"})
REFERENCES = {"builds": "unit", "trains": "unit", "sellunits": "unit", "sellitems": "item",
              "researches": "upgrade", "upgrades": "upgrade", "abillist": "ability",
              "heroabillist": "ability"}


def cli(command, map_path=None):
    from wc3_hivewe import run_cli_json
    config = settings()
    return run_cli_json(command + ["--map", str(Path(map_path or config["map"]).resolve()),
                                   "--warcraft", config["warcraft"]])


def require(data):
    if not data.get("ok"):
        raise RuntimeError(data.get("error") or data.get("raw") or "CLI failed")
    return data


def compact_output(value, limit, budget=None):
    budget = budget if budget is not None else [max(80, limit * 40)]
    budget[0] -= 1
    if budget[0] < 0:
        return "<output budget exceeded; see artifact>"
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if budget[0] < 0:
                result["output_truncated"] = True
                break
            result[key] = compact_output(item, limit, budget)
            if isinstance(item, list) and len(item) > limit:
                result[key + "_total"] = len(item)
        return result
    if isinstance(value, list):
        if len(value) <= 4 and all(isinstance(item, (int, float)) for item in value):
            return value  # preserve complete coordinate/bounding-box tuples
        return [compact_output(item, limit, budget) for item in value[:limit] if budget[0] >= 0]
    if isinstance(value, str):
        from wc3_hivewe import clean_wc3_string
        return clean_wc3_string(value)[:1000]
    return value


def snapshot(map_path, fields=None):
    result = {}
    for kind in TYPES:
        command = ["dump-objects", "--type", kind, "--max", "100000"]
        selected = fields
        if selected is None:
            metadata = require(cli(["list-fields", "--type", kind], map_path))
            selected = ",".join(sorted(field["column"] for field in metadata["fields"]))
        command += ["--fields", selected]
        data = require(cli(command, map_path))
        objects = data.get("objects")
        if not isinstance(objects, list):
            raise ValueError("dump-objects response has no objects list")
        for obj in objects:
            obj["fields"] = {key: value for key, value in obj.get("fields", {}).items() if value != ""}
        result[kind] = {obj["id"]: obj for obj in objects}
    return result


def validate_state(map_path, assets=False):
    from wc3_hivewe import run_cli_json
    capabilities = run_cli_json(["capabilities"])
    if capabilities.get("features", {}).get("validate_map"):
        command = ["validate-map", "--limit", "100000"]
        if assets:
            command += ["--assets"]
        result = cli(command, map_path)
        if not isinstance(result.get("findings"), list):
            raise RuntimeError(result.get("error", "Native validation returned no findings list"))
        return result
    if assets:
        raise RuntimeError("Asset validation needs the patched native CLI; configure HIVEWE_CLI")
    data = snapshot(map_path, ",".join(REFERENCES))
    findings = validate(data)
    return {"ok": not findings, "findings": findings,
            "objects": {kind: len(objects) for kind, objects in data.items()},
            "limitations": ["Fallback checks train/build/research/ability references; WTS/CASC assets require patched CLI."]}


def semantic_diff(before, after):
    changes = []
    for kind in sorted(set(before) | set(after)):
        left, right = before.get(kind, {}), after.get(kind, {})
        for rawcode in sorted(set(left) | set(right)):
            if rawcode not in left or rawcode not in right:
                changes.append({"type": kind, "id": rawcode,
                                "change": "added" if rawcode in right else "removed",
                                "before": left.get(rawcode), "after": right.get(rawcode)})
                continue
            # Names are resolved by CLI; retain them even if WTS is the only changed file.
            a = {**left[rawcode].get("fields", {}), "$name": left[rawcode].get("name"),
                 "$suffix": left[rawcode].get("editor_suffix")}
            b = {**right[rawcode].get("fields", {}), "$name": right[rawcode].get("name"),
                 "$suffix": right[rawcode].get("editor_suffix")}
            for field in sorted(set(a) | set(b)):
                if a.get(field) != b.get(field):
                    changes.append({"type": kind, "id": rawcode, "field": field,
                                    "name": right[rawcode].get("name"),
                                    "before": a.get(field), "after": b.get(field)})
    return changes


def validate(snapshot_data):
    findings = []
    for kind, objects in snapshot_data.items():
        for rawcode, obj in objects.items():
            for field, target in REFERENCES.items():
                value = str(obj.get("fields", {}).get(field, ""))
                for referenced in value.split(","):
                    referenced = referenced.strip()
                    if referenced and referenced not in ("_", "0") and referenced not in snapshot_data.get(target, {}):
                        findings.append({"severity": "error", "type": kind, "id": rawcode,
                                         "field": field, "reference": referenced,
                                         "message": f"Unknown {target} reference"})
    return findings


def hash_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest() if Path(path).exists() else None


def atomic_copy(source, target):
    target = Path(target)
    temp = target.with_name(target.name + f".{os.getpid()}.tmp")
    shutil.copy2(source, temp)
    os.replace(temp, target)


def recover(journal_path, force=False):
    path = Path(journal_path)
    journal = json.loads(read(path))
    if journal.get("schema_version") != 1 or journal.get("state") not in ("prepared", "applying", "committed", "failed"):
        raise ValueError("Journal not recoverable")
    root = Path(journal["map"]).resolve()
    # Validate every target and concurrent modification before restoring anything.
    for entry in journal["files"]:
        target = (root / entry["file"]).resolve()
        if target.parent != root or entry["file"] not in EDIT_FILES:
            raise ValueError("Unsafe recovery path")
        backup = (path.parent / entry["backup"]).resolve()
        if backup.parent != path.parent.resolve():
            raise ValueError("Unsafe backup path")
        if not force and hash_file(target) not in (entry["before_sha256"], entry["after_sha256"]):
            raise ValueError(f"Concurrent change: {target}")
        if entry["before_sha256"] and hash_file(path.parent / entry["backup"]) != entry["before_sha256"]:
            raise ValueError("Backup hash mismatch")
    for entry in journal["files"]:
        target = root / entry["file"]
        if entry["before_sha256"] is None:
            target.unlink(missing_ok=True)
        else:
            atomic_copy(path.parent / entry["backup"], target)
    journal["state"] = "rolled-back"
    path.write_text(json.dumps(journal, indent=2), encoding="utf-8")
    return {"ok": True, "state": journal["state"], "files": len(journal["files"])}


def transaction(plan_path, apply=False, map_path=None):
    root = Path(map_path or settings()["map"]).resolve()
    operations = json.loads(read(plan_path)).get("operations", [])
    if not operations:
        raise ValueError("Plan must contain operations")
    for op in operations:
        if op.get("type") not in TYPES or len(op.get("id", "")) != 4 or not op.get("field") or "value" not in op:
            raise ValueError("Each operation needs type, four-character id, field and value")
        op["field"] = op["field"].lower()
        if isinstance(op["value"], bool):
            op["value"] = int(op["value"])
        if isinstance(op["value"], float) and not math.isfinite(op["value"]):
            raise ValueError("Non-finite object values are not allowed")
    CACHE.mkdir(parents=True, exist_ok=True)
    initial_hashes = {name: hash_file(root / name) for name in EDIT_FILES}
    existing_errors = [f for f in validate_state(root)["findings"] if f["severity"] == "error"]
    original_snapshot = snapshot(root)
    with tempfile.TemporaryDirectory(prefix="wc3-stage-", dir=CACHE) as temporary:
        stage = Path(temporary)
        for source in root.glob("war3map*"):
            if source.is_file():
                shutil.copy2(source, stage / source.name)
        previews = []
        fields_by_type = {}
        for op in operations:
            if op["type"] not in fields_by_type:
                metadata = require(cli(["list-fields", "--type", op["type"]], stage))
                fields_by_type[op["type"]] = {field["column"] for field in metadata["fields"]}
            if op["field"].lower() not in fields_by_type[op["type"]]:
                raise ValueError(f"Unknown {op['type']} field: {op['field']}")
            obj = require(cli(["get-object", "--type", op["type"], "--id", op["id"], "--fields", op["field"]], stage))
            before = obj.get("fields", {}).get(op["field"])
            require(cli(["set-field", "--type", op["type"], "--id", op["id"], "--field", op["field"],
                         "--value", str(op["value"])], stage))
            obj = require(cli(["get-object", "--type", op["type"], "--id", op["id"], "--fields", op["field"]], stage))
            after = obj.get("fields", {}).get(op["field"])
            from wc3_hivewe import load_wts_strings
            decoded = after
            if isinstance(after, str) and after.startswith("TRIGSTR_"):
                decoded = load_wts_strings(stage / "war3map.wts").get(int(after[8:]), after)
            wanted = str(op["value"])
            equal = str(decoded) == wanted
            if not equal:
                try:
                    equal = float(decoded) == float(wanted)
                except (TypeError, ValueError):
                    pass
            if not equal:
                raise ValueError(f"Readback mismatch for {op['id']}.{op['field']}: wanted {wanted}, got {decoded}")
            previews.append({**op, "before": before, "after": after, "resolved_after": decoded})
        # Validate references on final staged state before touching the original map.
        errors = [error for error in validate_state(stage)["findings"] if error["severity"] == "error"
                  if error not in existing_errors]
        if errors:
            return {"ok": False, "applied": False, "changes": previews, "findings": errors}
        semantic = semantic_diff(original_snapshot, snapshot(stage))
        allowed = {(op["type"], op["id"], op["field"]) for op in operations}
        allowed |= {(op["type"], op["id"], "$name" if op["field"] == "name" else "$suffix")
                    for op in operations if op["field"] in ("name", "editorsuffix")}
        unexpected = [change for change in semantic if
                      (change["type"], change["id"], change.get("field")) not in allowed]
        if unexpected:
            return {"ok": False, "applied": False, "changes": previews,
                    "error": "Staged serialization changed unrelated effective fields", "unexpected": unexpected}
        changed = sorted(name for name in EDIT_FILES if hash_file(root / name) != hash_file(stage / name))
        if not apply:
            return {"ok": True, "applied": False, "changes": previews, "files": changed,
                    "existing_findings": len(existing_errors)}
        journal_dir = Path(tempfile.mkdtemp(prefix="transaction-", dir=CACHE))
        journal_path = journal_dir / "journal.json"
        journal = {"schema_version": 1, "state": "prepared", "map": str(root), "files": []}
        for name in changed:
            before_hash = initial_hashes[name]
            if hash_file(root / name) != before_hash:
                raise ValueError("Map changed while staging edits")
            if before_hash is not None:
                shutil.copy2(root / name, journal_dir / name)
            journal["files"].append({"file": name, "backup": name, "before_sha256": before_hash,
                                     "after_sha256": hash_file(stage / name)})
        journal_path.write_text(json.dumps(journal, indent=2), encoding="utf-8")
        try:
            journal["state"] = "applying"
            journal_path.write_text(json.dumps(journal, indent=2), encoding="utf-8")
            for entry in journal["files"]:
                if hash_file(root / entry["file"]) != entry["before_sha256"]:
                    raise ValueError("Map changed during transaction")
                atomic_copy(stage / entry["file"], root / entry["file"])
            journal["state"] = "committed"
            journal_path.write_text(json.dumps(journal, indent=2), encoding="utf-8")
        except Exception as exc:
            journal["state"] = "failed"
            journal_path.write_text(json.dumps(journal, indent=2), encoding="utf-8")
            try:
                recover(journal_path)
            except Exception as recovery_error:
                raise RuntimeError(f"Edit failed ({exc}); recovery blocked ({recovery_error}); journal={journal_path}") from exc
            raise RuntimeError(f"Edit failed and was rolled back ({exc}); journal={journal_path}") from exc
        return {"ok": True, "applied": True, "changes": previews, "journal": str(journal_path)}


def register(parsers):
    for name in ("bulk", "tree", "describe", "diff", "validate-map", "transaction", "recover", "capabilities"):
        parser = parsers.add_parser(name)
        parser.add_argument("--json", action="store_true")
        parser.add_argument("--limit", type=int, default=15)
        parser.add_argument("--artifact", type=Path)
        if name == "bulk":
            parser.add_argument("ids"); parser.add_argument("--type", choices=TYPES, default="unit")
            parser.add_argument("--fields", default="name,editorsuffix,hp,builds,trains,researches,abillist")
        elif name == "tree":
            parser.add_argument("id"); parser.add_argument("--depth", type=int, default=2)
        elif name == "describe":
            parser.add_argument("suffix")
        elif name == "diff":
            parser.add_argument("before", type=Path); parser.add_argument("after", type=Path)
        elif name == "transaction":
            parser.add_argument("plan", type=Path); parser.add_argument("--apply", action="store_true")
        elif name == "recover":
            parser.add_argument("journal", type=Path)
        elif name == "validate-map":
            parser.add_argument("--assets", action="store_true")


def dispatch(args):
    try:
        if args.limit < 1:
            raise ValueError("--limit must be positive")
        if args.command == "bulk":
            result = cli(["get-objects-bulk", "--type", args.type, "--ids", args.ids, "--fields", args.fields])
        elif args.command == "tree":
            result = cli(["trace-unit", "--id", args.id, "--depth", str(args.depth), "--format", "json"])
        elif args.command == "describe":
            result = cli(["describe-race", "--suffix", args.suffix])
        elif args.command == "diff":
            result = {"ok": True, "changes": semantic_diff(snapshot(args.before), snapshot(args.after))}
        elif args.command == "validate-map":
            result = validate_state(settings()["map"], args.assets)
        elif args.command == "transaction":
            result = transaction(args.plan, args.apply)
        elif args.command == "recover":
            result = recover(args.journal)
        else:
            from wc3_hivewe import run_cli_json
            result = run_cli_json(["capabilities"])
            if not result.get("ok"):
                result = run_cli_json(["--help"])
            result["wrapper_schema_version"] = 1
        artifact = args.artifact or CACHE / f"hivewe-{args.command}.json"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        compact = compact_output(result, args.limit)
        compact["artifact"] = str(artifact)
        print(json.dumps(compact, ensure_ascii=False, indent=None if args.json else 2))
        return 0 if result.get("ok") else 1
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1
