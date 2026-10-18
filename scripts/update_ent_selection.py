# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) selection ability A0QQ with SD/HD validation."""
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
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name != "war3map.wts"
    }

    # Target strings for A0QQ
    strings_to_update = {
        15815: "|cffe4cfa3Энты|r",
        15818: "|cffe4cfa3Энты|r (|cffffffffE|r)",
        15823: "|cffa6afb8РАСА:|cffced4da Первобытные древесные стражи и хранители природы.|r|n|n|cffa6afb8Создатель расы:|r |cffa9c7deNiCAmCHiK|r|n|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n|cffa6afb8Период:|r |cffa9c7de«Битва за Азерот»|r|n|n|cffced4daЭнты — могущественные первобытные древни и ожившие хранители лесов, служившие Кенарию на протяжении эпох. Тесно связанные с друидами и хранителями рощи, они оберегают священные чащи, черпая силу из живительных источников и пробуждая саму природу на защиту мира.|r"
    }

    wts_content = original_wts
    for str_id, new_text in strings_to_update.items():
        wts_content = update_wts_string(wts_content, str_id, new_text)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Invalidate wts cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    def resolve(val):
        if isinstance(val, str) and val.startswith("TRIGSTR_"):
            try:
                num = int(val[8:])
                return wts_dict.get(num, val)
            except ValueError:
                pass
        return val

    # Verification in SD and HD
    checks = []
    for hd in [False, True]:
        hd_flag = ["--hd"] if hd else []
        bulk_res = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A0QQ"] + hd_flag))
        obj = bulk_res["objects"][0]["fields"]

        act_name = resolve(obj.get("name", ""))
        act_tip = resolve(obj.get("tip1", ""))
        act_ubertip = resolve(obj.get("ubertip1", ""))

        assert act_name == strings_to_update[15815], f"Name mismatch (hd={hd}): {act_name!r}"
        assert act_tip == strings_to_update[15818], f"Tip mismatch (hd={hd}): {act_tip!r}"
        assert act_ubertip == strings_to_update[15823], f"Ubertip mismatch (hd={hd}): {act_ubertip!r}"

        checks.append({
            "id": "A0QQ",
            "type": "ability",
            "variant": "HD" if hd else "SD",
            "fields_verified": ["name", "tip1", "ubertip1"]
        })

    registry = {
        "scope": "Энты (Argvinol): подсказка выбора расы A0QQ",
        "object": "A0QQ",
        "variants": ["SD", "HD"],
        "hotkey": {"reference": "TRIGSTR_20465", "value": "E"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:402-419: InitTrig_Race_Argvinol_O фильтрует A0QQ; выбор создаёт 5 e02T и исследует R0BZ.",
            "A0QQ находится на стартовом алтаре/таверне выбора рас карты.",
            "Автор NiCAmCHiK, куратор NiCAmCHiK, сложность 3/5, период «Битва за Азерот» и клавиша E сохранены."
        ],
        "consumers": [
            {"file": "war3mapSkin.w3a", "id": "A0QQ", "field": ["anam", 0, 0], "wts_id": 15815},
            {"file": "war3mapSkin.w3a", "id": "A0QQ", "field": ["atp1", 1, 0], "wts_id": 15818},
            {"file": "war3mapSkin.w3a", "id": "A0QQ", "field": ["aub1", 1, 0], "wts_id": 15823}
        ],
        "in_game_checked": False,
        "strings": [
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0QQ",
                "field": "name",
                "reference_before": "TRIGSTR_15815",
                "before": "|cff228b22Энты|r",
                "after": strings_to_update[15815]
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0QQ",
                "field": "tip1",
                "reference_before": "TRIGSTR_15818",
                "before": "|cffa0dcc8Энты|r",
                "after": strings_to_update[15818]
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0QQ",
                "field": "ubertip1",
                "reference_before": "TRIGSTR_15823",
                "before": original_wts.split("STRING 15823")[1].split("{")[1].split("}")[0].strip(),
                "after": strings_to_update[15823]
            }
        ]
    }
    (folder / "ent_selection.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Ents",
        "category": "selection",
        "wts_keys_updated": [15815, 15818, 15823],
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "ent_selection_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Successfully updated Ents selection ability A0QQ.")
    print("Updated 3 WTS keys. Verified 6 SD/HD values.")

if __name__ == "__main__":
    main()
