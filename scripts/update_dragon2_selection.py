# -*- coding: utf-8 -*-
"""Update Dragon Union (Dragon2) selection ability A1MZ with SD/HD validation."""
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

    # Target strings
    strings_to_update = {
        39558: "|cffe4cfa3Драконий Союз|r",
        39559: "|cffe4cfa3Драконий Союз|r (|cffffffffQ|r)",
        28525: "|cffa6afb8РАСА:|cffced4da Альянс четырёх благородных стай драконов.|r|n|n|cffa6afb8Создатель расы:|r |cffa9c7deEscanor|r|n|cffa6afb8Переработал:|r |cffa9c7deVinerX|r|n|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8●|r|n|cffa6afb8Период:|r |cffa9c7de«Катаклизм»|r|n|n|cffced4daКрасная, зелёная, бронзовая и синяя стаи объединяются в союз, чтобы противостоять угрозам новых времён. Чёрная стая исключена из союза, а её гнездо и особые мутации недоступны.|r"
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
        bulk_res = require(cli(["get-objects-bulk", "--type", "ability", "--ids", "A1MZ"] + hd_flag))
        obj = bulk_res["objects"][0]["fields"]

        act_name = resolve(obj.get("name", ""))
        act_tip = resolve(obj.get("tip1", ""))
        act_ubertip = resolve(obj.get("ubertip1", ""))

        assert act_name == strings_to_update[39558], f"Name mismatch (hd={hd}): {act_name!r}"
        assert act_tip == strings_to_update[39559], f"Tip mismatch (hd={hd}): {act_tip!r}"
        assert act_ubertip == strings_to_update[28525], f"Ubertip mismatch (hd={hd}): {act_ubertip!r}"

        checks.append({
            "id": "A1MZ",
            "type": "ability",
            "variant": "HD" if hd else "SD",
            "fields_verified": ["name", "tip1", "ubertip1"]
        })

    registry = {
        "scope": "Драконий Союз (Dragon2): подсказка выбора расы A1MZ",
        "object": "A1MZ",
        "variants": ["SD", "HD"],
        "hotkey": {"reference": "TRIGSTR_28741", "value": "Q"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:383-401: InitTrig_Race_Dragon2 фильтрует A1MZ; выбор создаёт 5 o01D.",
            "Dragons.lua:128-144: Trig_DragonUnionStart_Actions отключает n044, R0A7, R0AZ при применении A1MZ.",
            "A1MZ находится на драконьем стартовом маркере dra1 (Выбор Стаи).",
            "Автор Escanor, переработал VinerX, куратор VinerX, сложность 4/5, период «Катаклизм» и клавиша Q сохранены."
        ],
        "consumers": [
            {"file": "war3mapSkin.w3a", "id": "A1MZ", "field": ["anam", 0, 0], "wts_id": 39558},
            {"file": "war3mapSkin.w3a", "id": "A1MZ", "field": ["atp1", 1, 0], "wts_id": 39559},
            {"file": "war3mapSkin.w3a", "id": "A1MZ", "field": ["aub1", 1, 0], "wts_id": 28525}
        ],
        "in_game_checked": False,
        "strings": [
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A1MZ",
                "field": "name",
                "reference_before": "TRIGSTR_39558",
                "before": "|cff8080ffДраконий Союз|r",
                "after": strings_to_update[39558]
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A1MZ",
                "field": "tip1",
                "reference_before": "TRIGSTR_39559",
                "before": "|cff8080ffДраконий Союз|r",
                "after": strings_to_update[39559]
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A1MZ",
                "field": "ubertip1",
                "reference_before": "TRIGSTR_28525",
                "before": original_wts.split("STRING 28525")[1].split("{")[1].split("}")[0].strip(),
                "after": strings_to_update[28525]
            }
        ]
    }
    (folder / "dragon2_selection.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Dragon2",
        "category": "selection",
        "wts_keys_updated": [39558, 39559, 28525],
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "dragon2_selection_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Successfully updated Dragon2 selection ability A1MZ.")
    print("Updated 3 WTS keys. Verified 6 SD/HD values.")

if __name__ == "__main__":
    main()
