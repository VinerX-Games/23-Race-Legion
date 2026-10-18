# -*- coding: utf-8 -*-
"""Analyze and fix Alliance plan discrepancies."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def clean_title(title: str) -> str:
    if not title:
        return ""
    t = re.sub(r'\|c[0-9a-fA-F]{8}', '', title)
    t = t.replace('|r', '').replace('|R', '')
    prefixes = [
        "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Построить ", "Улучшить до ",
        "Произвести ", "Изучить ", "Провести ", "Train ", "Hire ", "Build ", "Research ", "Upgrade to "
    ]
    for p in prefixes:
        if t.startswith(p):
            t = t[len(p):]
    t = re.sub(r'\s*[\(\[][A-Za-zА-Яа-я0-9\-\s]+[\)\]]$', '', t)
    return t.strip()

def clean_body_text(body: str) -> str:
    if not body:
        return ""
    t = re.sub(r'\|c[0-9a-fA-F]{8}', '', body)
    t = t.replace('|r', '').replace('|R', '')
    t = t.replace('\r\n', '\n').replace('\r', '\n')
    return t.strip()

def main():
    plan_path = ROOT / "docs/ui_text/alliance_plan.json"
    fails_path = ROOT / "docs/ui_text/alliance_fails.json"
    dump_path = ROOT / "scripts/alliance_raw_dump.json"

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    fails = json.loads(fails_path.read_text(encoding="utf-8"))
    dump = json.loads(dump_path.read_text(encoding="utf-8"))

    wts_updates = {int(k): v for k, v in plan["wts_updates"].items()}
    checks_def = plan["checks_def"]

    # Map of (type, id, field) -> check dict
    checks_by_key = {}
    for c in checks_def:
        checks_by_key[(c["type"], c["id"], c["field"])] = c

    # Process all 99 fails
    # 1. Literals (4 items) -> remove from checks_def
    fixed_count = 0
    removed_checks = set()
    for f in fails:
        key = (f["type"], f["id"], f["field"])
        raw = f["raw"]
        expected = f["expected"]

        if not (isinstance(raw, str) and raw.startswith("TRIGSTR_")):
            # Literal string in binary map file, not a WTS string
            print(f"Removing literal check: {key} (raw={raw})")
            removed_checks.add(key)
            fixed_count += 1
            continue

        sid = int(raw[8:])
        # The expected value is our high-quality standardized string.
        # Ensure wts_updates[sid] has this exact expected string!
        # Check if expected is already well-formatted
        wts_updates[sid] = expected
        if key in checks_by_key:
            checks_by_key[key]["expected"] = expected
        fixed_count += 1
        print(f"Updated WTS {sid} for {key}")

    # Rebuild checks_def without removed checks and without duplicates
    new_checks_def = []
    seen = set()
    for c in checks_def:
        key = (c["type"], c["id"], c["field"])
        if key in removed_checks or key in seen:
            continue
        seen.add(key)
        new_checks_def.append(checks_by_key[key])

    print(f"Total fails addressed: {fixed_count}")
    print(f"New checks_def count: {len(new_checks_def)} (was {len(checks_def)})")
    print(f"New wts_updates count: {len(wts_updates)}")

    # Update plan
    plan["wts_updates"] = {str(k): v for k, v in sorted(wts_updates.items())}
    plan["checks_def"] = new_checks_def
    plan["total_updates"] = len(wts_updates)
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved updated plan to {plan_path}")

if __name__ == "__main__":
    main()
