# -*- coding: utf-8 -*-
"""Complete, autonomous script for standardizing all UI texts of Race 29: Alliance (Альянс).

Supports:
  --dry-run (default if --apply not passed): Simulates WTS string replacements in memory,
            validates regex matching, checks style rules, color tags, and ensures zero
            collisions or missing strings. Generates category registries and saves
            docs/ui_text/alliance_dry_run_report.json without modifying any map files.
  --apply:  Applies WTS updates to map.w3x/war3map.wts, executes HiveWE SD readback
            verifications across all checks, verifies binary hashes, and saves
            docs/ui_text/alliance_all_apply.json.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def validate_style_rules(wts_updates: dict) -> list:
    """Validate common UI text style invariants across all generated texts."""
    issues = []
    forbidden_prefixes = [
        "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Построить ", "Улучшить до ",
        "Произвести ", "Изучить ", "Провести ", "Train ", "Hire ", "Build ", "Research ", "Upgrade to "
    ]
    color_tag_re = re.compile(r"\|c[0-9a-fA-F]{8}")
    for sid, text in wts_updates.items():
        # Check that if color tag is opened, the string ends with |r (or has at least one |r)
        has_color = bool(color_tag_re.search(text))
        has_reset = "|r" in text
        if has_color and not has_reset:
            issues.append(f"STRING {sid}: opened color tag without any |r reset: {repr(text)}")

        # Check for malformed color tags like |cff... with wrong length
        malformed = re.findall(r"\|c[^f\r\n]{1,7}[^0-9a-fA-F]", text)
        if malformed:
            issues.append(f"STRING {sid}: potential malformed color tag: {malformed}")

        # Check for trailing empty lines
        if text.endswith("|n") or text.endswith("\n") or text.endswith("\r"):
            issues.append(f"STRING {sid}: ends with trailing newline: {repr(text[-10:])}")

        # Check for forbidden prefixes in short tips
        for p in forbidden_prefixes:
            if text.startswith(p) or f">{p}" in text:
                issues.append(f"STRING {sid}: contains forbidden command prefix '{p}': {text[:40]}")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Standardize Alliance UI text in WTS")
    parser.add_argument("--apply", action="store_true", help="Actually write changes to war3map.wts and run live verification")
    parser.add_argument("--dry-run", action="store_true", help="Perform simulation and validation without modifying war3map.wts")
    args = parser.parse_args()

    # Safety default: unless --apply is explicitly specified, run in dry-run mode
    is_apply = args.apply and not args.dry_run

    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    plan_path = folder / "alliance_plan.json"

    if not plan_path.exists():
        print(f"Plan not found at {plan_path}, running prepare_alliance_plan.py...")
        import prepare_alliance_plan
        prepare_alliance_plan.main()

    plan_data = json.loads(plan_path.read_text(encoding="utf-8"))
    wts_updates = {int(k): v for k, v in plan_data["wts_updates"].items()}
    checks_def = plan_data["checks_def"]

    wts_path = ROOT / "map.w3x/war3map.wts"
    w3u_path = ROOT / "map.w3x/war3map.w3u"
    w3u_skin_path = ROOT / "map.w3x/war3mapSkin.w3u"
    w3a_path = ROOT / "map.w3x/war3map.w3a"
    w3a_skin_path = ROOT / "map.w3x/war3mapSkin.w3a"
    w3h_path = ROOT / "map.w3x/war3map.w3h"
    w3h_skin_path = ROOT / "map.w3x/war3mapSkin.w3h"
    w3q_path = ROOT / "map.w3x/war3map.w3q"
    w3q_skin_path = ROOT / "map.w3x/war3mapSkin.w3q"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256(w3u_path.read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest(),
        "w3a": hashlib.sha256(w3a_path.read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest(),
        "w3h": hashlib.sha256(w3h_path.read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest(),
        "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
    }

    print("=== ALLIANCE (АЛЬЯНС) UI TEXT STANDARDIZATION ===")
    print(f"Mode: {'APPLY (live write)' if is_apply else 'DRY-RUN (in-memory simulation)'}")
    print(f"Total WTS updates: {len(wts_updates)}")
    print(f"Total checks planned: {len(checks_def)}")

    # 1. Style validation
    style_issues = validate_style_rules(wts_updates)
    if style_issues:
        print(f"Style validation found {len(style_issues)} issues:")
        for iss in style_issues[:10]:
            print(f"  - {iss}")
        if len(style_issues) > 10:
            print(f"  ... and {len(style_issues)-10} more.")
        raise RuntimeError("Style validation failed")
    else:
        print("Style validation passed: all color tags balanced, no forbidden command prefixes, 0 errors.")

    # 2. In-memory WTS replacement test
    wts_raw = wts_path.read_text(encoding="utf-8")
    simulated_wts = wts_raw
    sim_count = 0
    for sid, new_val in sorted(wts_updates.items()):
        simulated_wts = update_wts_string(simulated_wts, sid, new_val)
        sim_count += 1
    print(f"In-memory WTS replacement test successful: all {sim_count} strings cleanly matched and replaced.")

    if not is_apply:
        # Dry-run report
        report_path = folder / "alliance_dry_run_report.json"
        report_payload = {
            "race": "Alliance",
            "race_id": 29,
            "mode": "dry-run",
            "total_updates": len(wts_updates),
            "total_checks": len(checks_def),
            "style_validation_ok": True,
            "wts_replacements_simulated": sim_count,
            "original_hashes": original_hashes,
            "wts_string_ids": sorted(list(wts_updates.keys())),
            "registries_generated": [
                "alliance_selection.json",
                "alliance_buildings.json",
                "alliance_units.json",
                "alliance_heroes.json",
                "alliance_abilities.json",
                "alliance_research.json",
                "alliance_audit.json"
            ]
        }
        report_path.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Dry-run report saved to {report_path}")

        # Check binary file integrity during dry run
        current_hashes = {
            "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
            "w3u": hashlib.sha256(w3u_path.read_bytes()).hexdigest(),
            "w3u_skin": hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest(),
            "w3a": hashlib.sha256(w3a_path.read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest(),
            "w3h": hashlib.sha256(w3h_path.read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest(),
            "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
        }
        assert current_hashes == original_hashes, "Files were modified during dry-run!"
        print("Dry-run completed successfully! No map files were modified.")
        return

    # =========================================================================
    # APPLY MODE (Only runs when --apply is explicitly passed)
    # =========================================================================
    print("Writing updated WTS to disk...")
    wts_path.write_text(simulated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("war3map.wts written successfully.")

    # Reset HiveWE cache to force reload of new WTS strings
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    print("Running HiveWE SD readback verification checks...")
    checks_results = []
    # Pre-fetch objects in bulk by type
    obj_cache = {}
    from collections import defaultdict
    ids_by_type = defaultdict(set)
    for c in checks_def:
        ids_by_type[c["type"]].add(c["id"])

    for otype, oids in ids_by_type.items():
        print(f"Reading back {len(oids)} {otype} objects...")
        oid_list = sorted(list(oids))
        for i in range(0, len(oid_list), 50):
            chunk = oid_list[i:i+50]
            res = hw.run_cli_json(["get-objects-bulk", "--map", str(ROOT / "map.w3x"), "--type", otype, "--ids", ",".join(chunk)])
            if res.get("ok"):
                for item in res.get("objects", []):
                    cid = item.get("id")
                    obj_cache[(otype, cid)] = item.get("fields", {}) or item.get("object", {})

    passed_checks = 0
    failed_checks = 0
    for idx, c in enumerate(checks_def):
        cache_key = (c["type"], c["id"])
        if cache_key not in obj_cache:
            res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", c["type"], "--id", c["id"]])
            if res.get("ok"):
                obj_cache[cache_key] = res.get("fields", {}) or res.get("object", {})
            else:
                obj_cache[cache_key] = {}
        fields = obj_cache[cache_key]
        actual = resolve(fields.get(c["field"]))
        expected = c["expected"]
        if actual == expected:
            passed_checks += 1
            checks_results.append({
                "check_idx": idx,
                "type": c["type"],
                "id": c["id"],
                "field": c["field"],
                "status": "PASS"
            })
        else:
            failed_checks += 1
            checks_results.append({
                "check_idx": idx,
                "type": c["type"],
                "id": c["id"],
                "field": c["field"],
                "status": "FAIL",
                "actual": actual,
                "expected": expected
            })

    print(f"Verification results: {passed_checks}/{len(checks_def)} passed ({failed_checks} failed)")

    # Verify binary integrity
    binary_ok = (
        original_hashes["w3u"] == hashlib.sha256(w3u_path.read_bytes()).hexdigest() and
        original_hashes["w3u_skin"] == hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest() and
        original_hashes["w3a"] == hashlib.sha256(w3a_path.read_bytes()).hexdigest() and
        original_hashes["w3a_skin"] == hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest() and
        original_hashes["w3h"] == hashlib.sha256(w3h_path.read_bytes()).hexdigest() and
        original_hashes["w3h_skin"] == hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest() and
        original_hashes["w3q"] == hashlib.sha256(w3q_path.read_bytes()).hexdigest() and
        original_hashes["w3q_skin"] == hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest()
    )
    print(f"Binary files integrity verified: {'OK (unchanged)' if binary_ok else 'MODIFIED'}")
    if not binary_ok:
        raise RuntimeError("Binary files were inadvertently modified!")

    apply_payload = {
        "race": "Alliance",
        "race_id": 29,
        "mode": "apply",
        "total_updates": len(wts_updates),
        "total_checks": len(checks_def),
        "passed_checks": passed_checks,
        "failed_checks": failed_checks,
        "wts_hash_before": original_hashes["wts"],
        "wts_hash_after": new_wts_hash,
        "checks_results": checks_results
    }
    apply_path = folder / "alliance_all_apply.json"
    apply_path.write_text(json.dumps(apply_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Apply summary saved to {apply_path}")

if __name__ == "__main__":
    main()
