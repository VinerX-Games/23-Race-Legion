# -*- coding: utf-8 -*-
"""Update Demon hero abilities with complete SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

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
    plan_path = folder / "demon_hero_abils_plan.json"
    plan_data = json.loads(plan_path.read_text(encoding="utf-8"))
    wts_updates = {int(k): v for k, v in plan_data["wts_updates"].items()}
    checks_def = plan_data["checks_def"]

    wts_path = ROOT / "map.w3x/war3map.wts"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
    }

    print(f"Applying {len(wts_updates)} WTS updates for Demon hero abilities...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Verify abilities via HiveWE
    checks = []
    abil_cache = {}
    for aid, field, sid_val, expected in checks_def:
        if aid not in abil_cache:
            res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", aid])
            if not res.get("ok"):
                raise RuntimeError(f"Failed to read {aid} via HiveWE: {res}")
            abil_cache[aid] = res.get("object", {}) or res.get("fields", {})
        
        f = abil_cache[aid]
        raw_val = f.get(field)
        if raw_val is None:
            if field == "tip1": raw_val = f.get("tip") or f.get("tip1")
            elif field == "ubertip1": raw_val = f.get("ubertip") or f.get("ubertip1")
        actual = resolve(raw_val)
        ok = (actual == expected)
        checks.append({
            "ability": aid,
            "field": field,
            "wts_id": sid_val,
            "expected": expected,
            "actual": actual,
            "ok": ok
        })

    passed_cnt = sum(1 for c in checks if c["ok"])
    print(f"Verification checks passed: {passed_cnt} / {len(checks)}")
    if passed_cnt < len(checks):
        for c in checks:
            if not c["ok"]:
                print(f"MISMATCH in {c['ability']} {c['field']} (WTS {c['wts_id']}):")
                print(f"  expected: {repr(c['expected'])}")
                print(f"  actual:   {repr(c['actual'])}")

    apply_payload = {
        "race": "Demons",
        "category": "HeroAbilities",
        "abilities_count": 28,
        "fields_checked": len(checks),
        "wts_updated": sorted(list(wts_updates.keys())),
        "hashes_before": original_hashes,
        "hashes_after": {
            "wts": new_wts_hash,
            "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
            "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
            "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
            "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
            "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
        },
        "binary_files_unchanged": (
            original_hashes["w3u"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest() and
            original_hashes["w3u_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest() and
            original_hashes["w3a"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest() and
            original_hashes["w3a_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest() and
            original_hashes["w3h"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest() and
            original_hashes["w3h_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest() and
            original_hashes["w3q"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest() and
            original_hashes["w3q_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest()
        ),
        "checks": checks,
        "all_checks_passed": (passed_cnt == len(checks))
    }

    with open(folder / "demon_hero_abils_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    with open(folder / "demon_hero_abils.json", "w", encoding="utf-8") as f:
        json.dump({"scope": "Пылающий Легион (Demon): Категория 4, Партия 1 — Способности героев (28 способностей, 275 полей)", "abilities": checks_def}, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
