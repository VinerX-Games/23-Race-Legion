# -*- coding: utf-8 -*-
"""Update Demon researches (14 technologies) with complete SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    plan_path = folder / "demon_research_plan.json"
    plan_data = json.loads(plan_path.read_text(encoding="utf-8"))

    wts_updates = {int(k): v for k, v in plan_data["wts_updates"].items()}
    skin_w3q_ops = plan_data["skin_w3q_ops"]
    checks_def = plan_data["checks_def"]

    wts_path = ROOT / "map.w3x/war3map.wts"
    w3a_path = ROOT / "map.w3x/war3map.w3a"
    w3a_skin_path = ROOT / "map.w3x/war3mapSkin.w3a"
    w3h_path = ROOT / "map.w3x/war3map.w3h"
    w3h_skin_path = ROOT / "map.w3x/war3mapSkin.w3h"
    w3u_path = ROOT / "map.w3x/war3map.w3u"
    w3u_skin_path = ROOT / "map.w3x/war3mapSkin.w3u"
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

    print(f"Applying {len(wts_updates)} WTS updates for Demon researches...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    # Patch war3mapSkin.w3q
    print(f"Patching {len(skin_w3q_ops)} operations into war3mapSkin.w3q...")
    w3q_skin_bytes = w3q_skin_path.read_bytes()
    new_w3q_skin_bytes, changed_q = patch_blob(w3q_skin_bytes, skin_w3q_ops, "upgrade", add_missing=True)
    w3q_skin_path.write_bytes(new_w3q_skin_bytes)
    new_w3q_skin_hash = hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest()
    print(f"war3mapSkin.w3q updated successfully ({len(changed_q)} mods).")

    # Verify base binary files untouched
    assert original_hashes["w3u"] == hashlib.sha256(w3u_path.read_bytes()).hexdigest(), "w3u altered!"
    assert original_hashes["w3a"] == hashlib.sha256(w3a_path.read_bytes()).hexdigest(), "w3a altered!"
    assert original_hashes["w3h"] == hashlib.sha256(w3h_path.read_bytes()).hexdigest(), "w3h altered!"
    assert original_hashes["w3q"] == hashlib.sha256(w3q_path.read_bytes()).hexdigest(), "w3q altered!"
    assert original_hashes["w3u_skin"] == hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest(), "w3u_skin altered!"
    assert original_hashes["w3a_skin"] == hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest(), "w3a_skin altered!"
    assert original_hashes["w3h_skin"] == hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest(), "w3h_skin altered!"

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Collect upgrade IDs for bulk query
    res_ids = sorted(list({c["id"] for c in checks_def}))
    bulk = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(res_ids)]))
    objects_q = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

    checks = []
    mismatches = []

    for c in checks_def:
        oid = c["id"]
        field = c["field"]
        expected = c["expected"]

        fields = objects_q.get(oid, {})
        actual = resolve(fields.get(field, ""))
        matched = (actual == expected)

        checks.append({
            "id": oid,
            "field": field,
            "matched": matched,
            "expected": expected,
            "actual": actual
        })

        if not matched:
            mismatches.append((oid, field, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for oid, f, exp, act in mismatches:
            print(f"  [{oid}] {f}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    print("All checks passed successfully!")

    # Write report and registry
    apply_report = {
        "scope": "Пылающий Легион (Demon): Категория 5 — Исследования (14 технологий, 73 поля)",
        "total_checks": len(checks),
        "passed_checks": len(checks) - len(mismatches),
        "all_matched": len(mismatches) == 0,
        "wts_updates_count": len(wts_updates),
        "skin_w3q_ops_count": len(skin_w3q_ops),
        "hashes": {
            "wts": {"before": original_hashes["wts"], "after": new_wts_hash},
            "w3q_skin": {"before": original_hashes["w3q_skin"], "after": new_w3q_skin_hash}
        },
        "base_binaries_untouched": True,
        "checks": checks
    }

    registry = {
        "scope": "Пылающий Легион (Demon): Реестр исследований (14 технологий)",
        "researches_count": len(res_ids),
        "researches": res_ids,
        "checks_def": checks_def
    }

    (folder / "demon_researches_apply.json").write_text(json.dumps(apply_report, indent=2, ensure_ascii=False), encoding="utf-8")
    (folder / "demon_researches.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Artifacts generated:")
    print("  - docs/ui_text/demon_researches.json")
    print("  - docs/ui_text/demon_researches_apply.json")

if __name__ == "__main__":
    main()
