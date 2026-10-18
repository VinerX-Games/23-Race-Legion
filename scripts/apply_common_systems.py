# -*- coding: utf-8 -*-
"""
Apply and verify Common Systems (Общие объекты и системы) standardization plan:
1. Applies WTS updates into map.w3x/war3map.wts.
2. Verifies that all non-text binary files (.w3u, .w3a, .w3q, etc.) remain 100% byte-for-byte identical.
3. Pre-fetches objects via HiveWE CLI bulk API for fast, robust verification.
4. Performs SD readback checks on all modified fields.
5. Generates detailed verification report in docs/ui_text/common_systems_all_apply.json.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from wc3_hivewe import run_cli_json, clean_wc3_string, DEFAULT_MAP, DEFAULT_WARCRAFT, load_wts_strings

WTS_PATH = ROOT / "map.w3x/war3map.wts"

BINARY_EXTS = [
    "war3map.w3u", "war3mapSkin.w3u",
    "war3map.w3a", "war3mapSkin.w3a",
    "war3map.w3q", "war3mapSkin.w3q",
    "war3map.w3t", "war3mapSkin.w3t",
    "war3map.w3h", "war3mapSkin.w3h",
    "war3map.w3b", "war3mapSkin.w3b",
    "war3map.w3d", "war3mapSkin.w3d"
]

def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""

def read_wts_raw(path: Path) -> str:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode("cp1251")

def update_wts_content(content: str, updates: dict[int, str]) -> str:
    pattern = re.compile(r"(STRING\s+(\d+)\s*\{)(.*?)(\n\})", re.DOTALL)
    def replacer(match):
        header = match.group(1)
        sid = int(match.group(2))
        footer = match.group(4)
        if sid in updates:
            return f"{header}\n{updates[sid]}{footer}"
        return match.group(0)
    return pattern.sub(replacer, content)

def main():
    print("Starting Common Systems apply process...")

    plan_path = ROOT / "docs/ui_text/common_systems_plan.json"
    if not plan_path.exists():
        print(f"Error: {plan_path} does not exist!")
        sys.exit(1)

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    wts_updates = {int(k): v for k, v in plan["wts_updates"].items()}
    checks = plan["checks"]
    print(f"Loaded Common Systems: {len(wts_updates)} WTS strings, {len(checks)} checks.")

    # 1. Snapshot binary hashes
    initial_hashes = {}
    for bfile in BINARY_EXTS:
        p = ROOT / "map.w3x" / bfile
        if p.exists():
            initial_hashes[bfile] = hash_file(p)

    orig_wts_hash = hash_file(WTS_PATH)

    # 2. Apply WTS updates
    print("\nApplying WTS updates to war3map.wts...")
    wts_content = read_wts_raw(WTS_PATH)
    updated_wts = update_wts_content(wts_content, wts_updates)
    WTS_PATH.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hash_file(WTS_PATH)
    print(f"Applied {len(wts_updates)} WTS updates successfully. WTS hash: {new_wts_hash[:12]}...")

    # Load fresh WTS dictionary from updated war3map.wts
    fresh_wts = load_wts_strings(WTS_PATH)
    resolve = lambda s: fresh_wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # 3. Pre-fetch objects in bulk for fast verification
    print("\nPre-fetching objects for HiveWE verification...")
    items_to_fetch = set()
    units_to_fetch = set()
    for chk in checks:
        if chk["type"] == "item":
            items_to_fetch.add(chk["id"])
        elif chk["type"] == "unit":
            units_to_fetch.add(chk["id"])

    bulk_cache = {"item": {}, "unit": {}}
    if items_to_fetch:
        print(f"  Fetching {len(items_to_fetch)} item objects in bulk...")
        cmd = ["get-objects-bulk", "--map", str(DEFAULT_MAP.resolve()), "--warcraft", str(DEFAULT_WARCRAFT.resolve()),
               "--type", "item", "--ids", ",".join(sorted(items_to_fetch))]
        res = run_cli_json(cmd)
        if res.get("ok"):
            for obj in res.get("objects", []):
                bulk_cache["item"][obj["id"]] = obj.get("fields", {})

    if units_to_fetch:
        print(f"  Fetching {len(units_to_fetch)} unit objects in bulk...")
        cmd = ["get-objects-bulk", "--map", str(DEFAULT_MAP.resolve()), "--warcraft", str(DEFAULT_WARCRAFT.resolve()),
               "--type", "unit", "--ids", ",".join(sorted(units_to_fetch))]
        res = run_cli_json(cmd)
        if res.get("ok"):
            for obj in res.get("objects", []):
                bulk_cache["unit"][obj["id"]] = obj.get("fields", {})

    # 4. Verify checks
    print("\nVerifying checks for Common Systems...")
    failures = []
    passed = 0

    for chk in checks:
        otype = chk["type"]
        oid = chk["id"]
        field = chk["field"]
        expected = chk["expected"]

        fields = bulk_cache.get(otype, {}).get(oid)
        if not fields:
            # Fallback single fetch
            cmd = ["get-object", "--map", str(DEFAULT_MAP.resolve()), "--warcraft", str(DEFAULT_WARCRAFT.resolve()),
                   "--type", otype, "--id", oid]
            single_res = run_cli_json(cmd)
            fields = single_res.get("object", {}) or single_res.get("fields", {})

        raw_val = fields.get(field, "") if fields else ""
        actual = resolve(raw_val)

        if actual == expected:
            passed += 1
        else:
            failures.append({
                "type": otype,
                "id": oid,
                "field": field,
                "expected": expected,
                "actual": actual
            })

    total_checks = len(checks)
    pct = (passed / total_checks * 100) if total_checks else 100.0
    print(f"  [Common Systems] {passed}/{total_checks} checks passed ({pct:.1f}%)")

    if failures:
        print(f"  FAILURES ({len(failures)}):")
        for f in failures[:10]:
            print(f"    - {f['type']} {f['id']} [{f['field']}]: expected {f['expected'][:40]!r}, got {f['actual'][:40]!r}")

    report = {
        "system": "CommonSystems",
        "system_name_ru": "Общие объекты и системы",
        "mode": "apply",
        "wts_updates_applied": len(wts_updates),
        "checks_summary": {
            "total": total_checks,
            "passed": passed,
            "failed": len(failures),
            "success_percent": round(pct, 2)
        },
        "hashes": {
            "original_wts": orig_wts_hash,
            "updated_wts": new_wts_hash
        },
        "failures": failures
    }

    out_file = ROOT / "docs/ui_text/common_systems_all_apply.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"  Saved {out_file.name}")

    # 5. Check binary integrity
    print("\nVerifying binary file integrity...")
    binary_ok = True
    for bfile, orig_hash in initial_hashes.items():
        curr_hash = hash_file(ROOT / "map.w3x" / bfile)
        if curr_hash != orig_hash:
            print(f"ERROR: Binary file {bfile} was modified! Hash mismatch: {orig_hash} != {curr_hash}")
            binary_ok = False

    if binary_ok:
        print("Binary file integrity verified: 100% byte-for-byte identical.")
    else:
        print("CRITICAL: Binary integrity check FAILED!")
        sys.exit(1)

    print("Master apply for Common Systems complete!")

if __name__ == '__main__':
    main()
