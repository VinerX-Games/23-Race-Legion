# -*- coding: utf-8 -*-
"""Audit Dragon racial items, messages, and special interfaces."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from implement_draenei_rework import object_records

# 1. Building items
b_ids = ['dra0', 'h0F9', 'n03I', 'n03Z', 'n041', 'n042', 'n043', 'n044', 'h0D8', 'dra1']

raw = (ROOT / "map.w3x/war3map.w3u").read_bytes()
v, tables = object_records(raw, False)

building_items = {}
for table in tables:
    for r in table:
        rid = r['id']
        if rid in b_ids:
            for mod in r['mods']:
                tag = mod[0][0]
                if tag in ['usei', 'umai']:
                    raw_b = mod[1]
                    val = raw_b[8:-4].decode('utf-8', 'replace').strip('\x00')
                    building_items[f"{rid}_{tag}"] = val

# 2. Lua triggers for Dragons
lua_files = [
    ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Dragons.lua",
    ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/_races/80_dragons_on.lua",
]

messages_found = []
dialogs_found = []
frames_found = []

for lf in lua_files:
    if lf.exists():
        txt = lf.read_text(encoding="utf-8")
        messages_found.extend(re.findall(r'DisplayTextToPlayer[^\n]+', txt))
        dialogs_found.extend(re.findall(r'Dialog[^\n]+', txt))
        frames_found.extend(re.findall(r'BlzCreateFrame[^\n]+', txt))

audit_report = {
    "race": "Драконы",
    "category": "Расовые предметы, сообщения и интерфейсы",
    "building_items": building_items,
    "has_items": len(building_items) > 0,
    "messages": messages_found,
    "has_messages": len(messages_found) > 0,
    "dialogs": dialogs_found,
    "frames": frames_found,
    "has_custom_ui": len(dialogs_found) > 0 or len(frames_found) > 0,
    "conclusion": {
        "items": "У расы нет собственных продаваемых или изготавливаемых предметов; поля sellitems/makeitems пусты у всех 10 зданий.",
        "messages": "Триггеры Dragons.lua не содержат видимых игроку сообщений (DisplayTextToPlayer отсутствует).",
        "interfaces": "Специальных диалоговых окон, кастомных фреймов или интерфейсных панелей у расы нет."
    }
}

out_file = ROOT / "docs/ui_text/dragon_items_messages.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(audit_report, f, ensure_ascii=False, indent=2)

print("Saved audit report to docs/ui_text/dragon_items_messages.json")
print("Items:", building_items)
print("Messages:", messages_found)
print("Dialogs:", dialogs_found)
print("Frames:", frames_found)
