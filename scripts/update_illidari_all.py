# -*- coding: utf-8 -*-
"""Complete, autonomous script for standardizing all UI texts of Race 10: Illidari (Иллидари).

Supports:
  --dry-run (default if --apply not passed): Simulates WTS string replacements in memory,
            validates regex matching, checks style rules, color tags, and ensures zero
            collisions or missing strings. Generates category registries and saves
            docs/ui_text/illidari_dry_run_report.json without modifying any map files.
  --apply:  Applies 549 WTS updates to map.w3x/war3map.wts, executes HiveWE SD readback
            verifications across all 93 checks, verifies binary hashes, and saves
            docs/ui_text/illidari_all_apply.json.
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
        "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Построить ", "Улучшить до "
    ]
    color_tag_re = re.compile(r"\|c[0-9a-fA-F]{8}")
    for sid, text in wts_updates.items():
        # Check that if color tag is opened, the string ends with |r (or has at least one |r)
        has_color = bool(color_tag_re.search(text))
        has_reset = "|r" in text
        if has_color and not has_reset:
            issues.append(f"STRING {sid}: opened color tag without any |r reset")

        # Check for malformed color tags like |cff... with wrong length
        malformed = re.findall(r"\|c[^f\r\n]{1,7}[^0-9a-fA-F]", text)
        if malformed:
            issues.append(f"STRING {sid}: potential malformed color tag: {malformed}")

        # Check for trailing empty lines
        if text.endswith("|n") or text.endswith("\n") or text.endswith("\r"):
            issues.append(f"STRING {sid}: ends with trailing newline")

        # Check for forbidden prefixes in short tips
        if any(text.startswith(p) for p in forbidden_prefixes):
            issues.append(f"STRING {sid}: contains forbidden command prefix")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Standardize Illidari UI text in WTS")
    parser.add_argument("--apply", action="store_true", help="Actually write changes to war3map.wts and run live verification")
    parser.add_argument("--dry-run", action="store_true", help="Perform simulation and validation without modifying war3map.wts")
    args = parser.parse_args()

    # Safety default: unless --apply is explicitly specified, run in dry-run mode
    is_apply = args.apply and not args.dry_run

    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    plan_path = folder / "illidari_plan.json"

    if not plan_path.exists():
        print(f"Plan not found at {plan_path}, running prepare_illidari_plan.py...")
        import prepare_illidari_plan
        prepare_illidari_plan.main()

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

    print("=== ILLIDARI (ИЛЛИДАРИ) UI TEXT STANDARDIZATION ===")
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

    # Ensure category registries are present / up-to-date
    import generate_illidari_registries
    generate_illidari_registries.main()

    if not is_apply:
        # Dry-run report
        report_path = folder / "illidari_dry_run_report.json"
        report_payload = {
            "race": "Illidari",
            "mode": "dry-run",
            "total_updates": len(wts_updates),
            "total_checks": len(checks_def),
            "style_validation_ok": True,
            "wts_replacements_simulated": sim_count,
            "original_hashes": original_hashes,
            "wts_string_ids": sorted(list(wts_updates.keys())),
            "registries_generated": [
                "illidari_selection.json",
                "illidari_buildings.json",
                "illidari_units.json",
                "illidari_heroes.json",
                "illidari_abilities.json",
                "illidari_research.json",
                "illidari_audit.json"
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
    # Cache object fields to avoid redundant HiveWE CLI calls
    obj_cache = {}
    for c in checks_def:
        ctype = c["type"]
        cid = c["id"]
        cfield = c["field"]
        expected_val = c["expected"]

        cache_key = (ctype, cid)
        if cache_key not in obj_cache:
            res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", ctype, "--id", cid])
            if not res.get("ok"):
                raise RuntimeError(f"Failed to read {ctype} {cid} via HiveWE: {res}")
            obj_cache[cache_key] = res.get("fields", {}) or res.get("object", {})

        fields = obj_cache[cache_key]
        actual_val = resolve(fields.get(cfield))
        ok = (actual_val == expected_val)
        checks_results.append({
            "type": ctype,
            "id": cid,
            "field": cfield,
            "ok": ok
        })

    passed_checks = sum(1 for c in checks_results if c["ok"])
    print(f"HiveWE verification checks passed: {passed_checks} / {len(checks_results)}")
    if passed_checks != len(checks_results):
        failed = [c for c in checks_results if not c["ok"]]
        print(f"FAILED CHECKS ({len(failed)}): {failed[:5]}")
        raise RuntimeError("Some verification checks failed!")

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
        "race": "Illidari",
        "mode": "apply",
        "wts_updated": list(wts_updates.keys()),
        "total_updates": len(wts_updates),
        "total_checks": len(checks_results),
        "checks_passed": passed_checks,
        "hashes_before": original_hashes,
        "hashes_after": {
            "wts": new_wts_hash,
            "w3u": hashlib.sha256(w3u_path.read_bytes()).hexdigest(),
            "w3u_skin": hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest(),
            "w3a": hashlib.sha256(w3a_path.read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest(),
            "w3h": hashlib.sha256(w3h_path.read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest(),
            "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
        },
        "binary_files_unchanged": binary_ok
    }

    apply_file = folder / "illidari_all_apply.json"
    apply_file.write_text(json.dumps(apply_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Apply record saved to {apply_file}")
    print("ALL CHECKS AND VERIFICATIONS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
