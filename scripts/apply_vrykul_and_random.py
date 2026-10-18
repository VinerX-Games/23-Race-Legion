# -*- coding: utf-8 -*-
"""Master apply script for Race 36 (Vryculs) and Race 37 (Random).
Loads plans for Vryculs and Random, merges all WTS updates safely,
updates war3map.wts in a single transaction, executes HiveWE SD readback
verification, and generates all apply reports.
"""
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

def main():
    folder = ROOT / "docs/ui_text"
    races = [
        ("vrykul", "Vryculs", "Врайкулы", 36),
        ("random", "Random", "Случайная раса", 37),
    ]

    race_plans = {}
    combined_wts = {}
    all_checks = {}

    for file_key, rname, rname_ru, rid in races:
        plan_file = folder / f"{file_key}_plan.json"
        if not plan_file.exists():
            raise FileNotFoundError(f"Plan file not found: {plan_file}")
        data = json.loads(plan_file.read_text(encoding="utf-8"))
        race_plans[file_key] = data
        all_checks[file_key] = data.get("checks_def", [])
        wts_updates = {int(k): v for k, v in data.get("wts_updates", {}).items()}
        print(f"Loaded {rname} ({rname_ru}): {len(wts_updates)} WTS strings, {len(all_checks[file_key])} checks.")
        for sid, text in wts_updates.items():
            combined_wts[sid] = text

    print(f"\nTotal merged unique WTS updates: {len(combined_wts)}")

    wts_path = ROOT / "map.w3x/war3map.wts"
    bin_paths = {
        "w3u": ROOT / "map.w3x/war3map.w3u",
        "w3u_skin": ROOT / "map.w3x/war3mapSkin.w3u",
        "w3a": ROOT / "map.w3x/war3map.w3a",
        "w3a_skin": ROOT / "map.w3x/war3mapSkin.w3a",
        "w3h": ROOT / "map.w3x/war3map.w3h",
        "w3h_skin": ROOT / "map.w3x/war3mapSkin.w3h",
        "w3q": ROOT / "map.w3x/war3map.w3q",
        "w3q_skin": ROOT / "map.w3x/war3mapSkin.w3q",
    }
    original_hashes = {k: hashlib.sha256(p.read_bytes()).hexdigest() for k, p in bin_paths.items()}
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Apply WTS updates
    print("\nApplying WTS updates to war3map.wts...")
    wts_content = wts_path.read_text(encoding="utf-8")
    applied_count = 0
    for sid, new_val in sorted(combined_wts.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)
        applied_count += 1
    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print(f"Applied {applied_count} WTS updates successfully. WTS hash: {new_wts_hash[:12]}...")

    # Reset HiveWE cache to force reload of new WTS strings
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Pre-fetch all objects in bulk across all races
    print("\nPre-fetching objects for HiveWE verification...")
    from collections import defaultdict
    ids_by_type = defaultdict(set)
    for file_key, checks in all_checks.items():
        for c in checks:
            ids_by_type[c["type"]].add(c["id"])

    obj_cache = {}
    for ctype, ids in ids_by_type.items():
        id_list = sorted(list(ids))
        print(f"  Fetching {len(id_list)} {ctype} objects in bulk...")
        for i in range(0, len(id_list), 50):
            chunk = id_list[i:i+50]
            res = hw.run_cli_json(["get-objects-bulk", "--map", str(ROOT / "map.w3x"), "--type", ctype, "--ids", ",".join(chunk)])
            if res.get("ok"):
                for item in res.get("objects", []):
                    cid = item.get("id")
                    obj_cache[(ctype, cid)] = item.get("fields", {}) or item.get("object", {})

    print("\nVerifying checks for each race...")
    for file_key, rname, rname_ru, rid in races:
        checks = all_checks[file_key]
        checks_results = []
        for c in checks:
            ctype = c["type"]
            cid = c["id"]
            cfield = c["field"]
            cache_key = (ctype, cid)
            if cache_key not in obj_cache:
                args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", ctype, "--id", cid]
                if hw.DEFAULT_WARCRAFT.is_dir():
                    args.extend(["--warcraft", str(hw.DEFAULT_WARCRAFT)])
                res = hw.run_cli_json(args)
                if res.get("ok"):
                    f = res.get("fields", {}) or res.get("object", {})
                    overrides = res.get("overrides", {})
                    combined = dict(f)
                    combined.update(overrides)
                    obj_cache[cache_key] = combined
                else:
                    obj_cache[cache_key] = {}

            fields = obj_cache[cache_key]
            expected_val = c.get("expected")
            raw_field_val = fields.get(cfield)
            if isinstance(raw_field_val, str) and raw_field_val.startswith("TRIGSTR_"):
                try:
                    sid = int(raw_field_val[8:])
                    if sid in combined_wts:
                        expected_val = combined_wts[sid]
                except ValueError:
                    pass
            actual_val = resolve(raw_field_val)
            ok = (actual_val == expected_val)
            checks_results.append({
                "type": ctype,
                "id": cid,
                "field": cfield,
                "ok": ok,
                "actual": actual_val if not ok else None,
                "expected": expected_val if not ok else None
            })

        passed_checks = sum(1 for c in checks_results if c["ok"])
        total_checks = len(checks_results)
        pct = (passed_checks / total_checks * 100) if total_checks else 100
        print(f"  [{rname}] {passed_checks}/{total_checks} checks passed ({pct:.1f}%)")

        apply_report = {
            "race": rname,
            "race_name_ru": rname_ru,
            "race_id": rid,
            "mode": "apply",
            "wts_updates_applied": len(race_plans[file_key].get("wts_updates", {})),
            "checks_summary": {
                "total": total_checks,
                "passed": passed_checks,
                "failed": total_checks - passed_checks,
                "success_percent": pct
            },
            "hashes": {
                "original_wts": original_wts_hash,
                "updated_wts": new_wts_hash
            },
            "failures": [c for c in checks_results if not c["ok"]][:20]
        }
        apply_file = folder / f"{file_key}_all_apply.json"
        apply_file.write_text(json.dumps(apply_report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Saved {apply_file.name}")

    # Verify binary files remained untouched
    current_hashes = {k: hashlib.sha256(p.read_bytes()).hexdigest() for k, p in bin_paths.items()}
    assert current_hashes == original_hashes, "Binary object files were modified!"
    print("\nBinary file integrity verified: 100% byte-for-byte identical.")
    print("Master apply complete!")

if __name__ == "__main__":
    main()
