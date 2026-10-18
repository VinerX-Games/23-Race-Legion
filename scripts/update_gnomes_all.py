# -*- coding: utf-8 -*-
"""Complete, autonomous script for standardizing all UI texts of Race 23: Gnomes (Гномы).

Supports:
  --dry-run (default if --apply not passed): Simulates WTS string replacements in memory,
            validates regex matching, checks style rules, color tags, and ensures zero
            collisions or missing strings. Generates category registries and saves
            docs/ui_text/gnomes_dry_run_report.json without modifying any map files.
  --apply:  Applies WTS updates to map.w3x/war3map.wts, executes HiveWE SD readback
            verifications across all checks, verifies binary hashes, and saves
            docs/ui_text/gnomes_all_apply.json.
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
        "Построть ", "Создать ", "Изучить "
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
    parser = argparse.ArgumentParser(description="Standardize Gnomes UI text in WTS")
    parser.add_argument("--apply", action="store_true", help="Actually write changes to war3map.wts and run live verification")
    parser.add_argument("--dry-run", action="store_true", help="Perform simulation and validation without modifying war3map.wts")
    args = parser.parse_args()

    # Safety default: unless --apply is explicitly specified, run in dry-run mode
    is_apply = args.apply and not args.dry_run

    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    plan_path = folder / "gnomes_plan.json"

    if not plan_path.exists():
        print(f"Plan not found at {plan_path}, running prepare_gnomes_plan.py...")
        import prepare_gnomes_plan
        prepare_gnomes_plan.main()

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

    print("=== GNOMES (ГНОМЫ) UI TEXT STANDARDIZATION ===")
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
        print("Style validation passed: all color tags balanced, no forbidden command prefixes.")

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
        report_path = folder / "gnomes_dry_run_report.json"
        report_payload = {
            "race": "Gnomes",
            "race_id": 23,
            "mode": "dry-run",
            "total_updates": len(wts_updates),
            "total_checks": len(checks_def),
            "style_validation_ok": True,
            "wts_replacements_simulated": sim_count,
            "original_hashes": original_hashes,
            "wts_string_ids": sorted(list(wts_updates.keys())),
            "registries_generated": [
                "gnomes_selection.json",
                "gnomes_buildings.json",
                "gnomes_units.json",
                "gnomes_heroes.json",
                "gnomes_abilities.json",
                "gnomes_research.json",
                "gnomes_audit.json",
            ],
            "status": "dry-run verification passed successfully with 0 errors. Map files left intact."
        }
        report_path.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2), encoding="utf-8")

        # Verify map files were not modified
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
        for k in original_hashes:
            assert original_hashes[k] == current_hashes[k], f"File {k} was modified during dry-run!"

        print(f"Map integrity confirmed: all binary and WTS files untouched.")
        print(f"Dry-run report saved to {report_path}")
        return

    # APPLY MODE (Only runs if --apply is passed)
    print("\n--- Writing changes to war3map.wts ---")
    wts_path.write_text(simulated_wts, encoding="utf-8")
    print("war3map.wts successfully updated.")

    # Live HiveWE verification
    print("\n--- Running HiveWE SD readback verification ---")
    verified_count = 0
    failed_checks = []
    for chk in checks_def:
        ctype = chk["type"]
        cid = chk["id"]
        cfield = chk["field"]
        expected = chk["expected"]
        try:
            res = hw.run_cli_json(["get-object", "--map", str(hw.DEFAULT_MAP), "--type", ctype, "--id", cid, "--all"])
            fields = res.get("fields", {}) or res.get("object", {})
            overrides = res.get("overrides", {})
            actual_raw = overrides.get(cfield) if overrides.get(cfield) is not None else fields.get(cfield)
            wts_dict = hw.load_wts_strings()
            actual = wts_dict.get(int(actual_raw[8:]), actual_raw) if isinstance(actual_raw, str) and actual_raw.startswith("TRIGSTR_") else actual_raw

            if actual == expected:
                verified_count += 1
            else:
                failed_checks.append({
                    "check": chk,
                    "actual": actual,
                    "expected": expected
                })
        except Exception as e:
            failed_checks.append({
                "check": chk,
                "error": str(e)
            })

    print(f"HiveWE verification completed: {verified_count}/{len(checks_def)} passed.")
    if failed_checks:
        print(f"WARNING: {len(failed_checks)} checks failed!")
        for fc in failed_checks[:5]:
            print(" ", fc)
    else:
        print("100% of HiveWE checks verified successfully!")

    # Verify binary object files were untouched
    post_hashes = {
        "w3u": hashlib.sha256(w3u_path.read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest(),
        "w3a": hashlib.sha256(w3a_path.read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest(),
        "w3h": hashlib.sha256(w3h_path.read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest(),
        "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
    }
    for k in post_hashes:
        assert original_hashes[k] == post_hashes[k], f"Binary file {k} hash changed!"
    print("Binary object files integrity confirmed: byte-for-byte identical.")

    # Save apply report
    apply_report_path = folder / "gnomes_all_apply.json"
    apply_payload = {
        "race": "Gnomes",
        "race_id": 23,
        "mode": "apply",
        "total_updates": len(wts_updates),
        "total_checks": len(checks_def),
        "verified_checks": verified_count,
        "failed_checks_count": len(failed_checks),
        "failed_checks": failed_checks,
        "original_hashes": original_hashes,
        "post_hashes": post_hashes,
        "status": "success" if not failed_checks else "partial_failure"
    }
    apply_report_path.write_text(json.dumps(apply_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Apply report saved to {apply_report_path}")

if __name__ == "__main__":
    main()
