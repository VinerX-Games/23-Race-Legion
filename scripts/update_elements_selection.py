# -*- coding: utf-8 -*-
"""Update Elements race selection ability A0QN with complete SD/HD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
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

    wts_updates = {
        38889: "|cffe4cfa3Элементали|r",
        38890: "|cffe4cfa3Элементали|r (|cffffffffQ|r)",
        41061: "|cffa6afb8РАСА:|cffced4da Первобытные повелители четырёх стихий и энергий мироздания.|r|n|n|cffa6afb8Создатель расы:|r |cffa9c7deEscanor|r|n|cffa6afb8Переработка:|r |cffa9c7deDawnguard|r|n|cffa6afb8Куратор расы:|r |cffa9c7deDawnguard|r|n|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n|cffa6afb8Период:|r |cffa9c7de«Катаклизм»|r|n|n|cffced4daЭлементали — древнейшие владыки огня, воды, земли и воздуха, заточённые в Обители стихий ради спасения Азерота. Прорывая грань между мирами, духи первозданных стихий несут в мир неукротимую мощь стихийного хаоса.|r"
    }

    print(f"Applying {len(wts_updates)} WTS updates for Elements selection...")
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

    # Verify A0QN in SD and HD
    checks = []
    expected_fields = {
        "name": wts_updates[38889],
        "tip1": wts_updates[38890],
        "ubertip1": wts_updates[41061]
    }

    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A0QN", "--fields", "name,tip1,ubertip1"] + hd_flag))
        obj = bulk["objects"][0]["fields"]
        for f, expected in expected_fields.items():
            actual = resolve(obj.get(f, ""))
            assert actual == expected, f"{f} mismatch for A0QN (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"
            checks.append({
                "id": "A0QN",
                "field": f,
                "hd": hd,
                "status": "OK"
            })

    print(f"All {len(checks)} readback checks passed in SD and HD!")

    # Verify binary integrity
    current_hashes = {
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
    }
    for k in current_hashes:
        assert current_hashes[k] == original_hashes[k], f"Binary file {k} was unexpectedly modified!"

    print("All binary file hashes preserved exactly!")

    # Write artifacts
    out_data = {
        "scope": "Элементали (Elements): подсказка выбора расы A0QN",
        "object": "A0QN",
        "variants": ["SD", "HD"],
        "hotkey": {
            "reference": "TRIGSTR_16869",
            "value": "Q"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:436, 1467: InitTrig_Race_Elements_O фильтрует A0QN; выбор создаёт 5 e00F, исследует R0A2 и запускает ElemOn().",
            "A0QN находится на 4-й странице таверны выбора рас, позиция (0, 0), клавиша Q (TRIGSTR_16869).",
            "Создатель Escanor, переработка и куратор Dawnguard, сложность 3/5, период «Катаклизм» и клавиша Q сохранены."
        ],
        "strings": [
            {
                "field": "name",
                "wts_id": 38889,
                "after": wts_updates[38889]
            },
            {
                "field": "tip1",
                "wts_id": 38890,
                "after": wts_updates[38890]
            },
            {
                "field": "ubertip1",
                "wts_id": 41061,
                "after": wts_updates[41061]
            }
        ]
    }
    (folder / "elements_selection.json").write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_data = {
        "wts_updates_count": len(wts_updates),
        "total_checks": len(checks),
        "original_hashes": original_hashes,
        "new_wts_hash": new_wts_hash,
        "current_hashes": current_hashes
    }
    (folder / "elements_selection_apply.json").write_text(json.dumps(apply_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Artifacts generated in docs/ui_text/.")

if __name__ == "__main__":
    main()
