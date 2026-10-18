# -*- coding: utf-8 -*-
"""Inspect Elements hero abilities: current fields, WTS strings, levels, hotkeys."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

hero_abils = [
    # H0EZ Кристальный владыка
    'A1MR', 'A0P4', 'A0P2', 'AEtq',
    # H0F0 Мастер ветра
    'A0P9', 'A0PA', 'A1LE', 'AHpx',
    # N037 Повелитель огня
    'ANic', 'AHfs', 'ANlm', 'A0P7',
    # E029 Владыка морей
    'A0OU', 'A0OT', 'A0QL', 'A0OR', 'A0YH',
    # E027 Владыка ветра
    'A0P0', 'A0OX', 'A0OW', 'A0P1', 'A0YI',
    # E028 Владыка Огня
    'A0OP', 'A0ON', 'A0QJ', 'A0OQ', 'A0YG'
]

bulk = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(hero_abils)]))
wts_dict = hw.load_wts_strings()

result = {}
for obj in bulk.get("objects", []):
    aid = obj["id"]
    fields = obj.get("fields", {})
    resolved_fields = {}
    for k, v in fields.items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            try:
                wts_id = int(v[8:])
                resolved_fields[k] = {"raw": v, "wts_id": wts_id, "text": wts_dict.get(wts_id, "")}
            except ValueError:
                resolved_fields[k] = {"raw": v, "text": v}
        else:
            resolved_fields[k] = {"raw": v, "text": v}
    result[aid] = resolved_fields

out_path = ROOT / "docs/ui_text/elements_hero_abils_raw.json"
out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Dumped {len(result)} abilities to {out_path}")
for aid in hero_abils:
    f = result.get(aid, {})
    name_info = f.get("name", {})
    name_txt = name_info.get("text", "") if isinstance(name_info, dict) else name_info
    hotkey_info = f.get("hotkey", {})
    hotkey_txt = hotkey_info.get("text", "") if isinstance(hotkey_info, dict) else hotkey_info
    levels_info = f.get("levels", {})
    levels_txt = levels_info.get("text", "") if isinstance(levels_info, dict) else levels_info
    print(f"[{aid}] {name_txt} | Levels: {levels_txt} | Hotkey: {hotkey_txt}")
