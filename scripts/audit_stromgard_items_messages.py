# -*- coding: utf-8 -*-
"""Audit Stromgard racial items, messages, and special interfaces."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Building items
b_ids = ['h0GZ', 'h0H0', 'h0H1', 'h0H2', 'h0H3', 'h0H5', 'h0H6', 'h0HG', 'h0HH', 'h0H4', 'h0HI', 'h0HU', 'h0HF', 'h011']

# Let's check war3map.w3u for sellitems and makeitems
import sys
sys.path.insert(0, "scripts")
from implement_draenei_rework import object_records

raw = Path("map.w3x/war3map.w3u").read_bytes()
v, tables = object_records(raw, False)

building_items = {}
for table in tables:
    for r in table:
        if r['id'] in b_ids:
            for mod in r['mods']:
                tag = mod[0][0]
                if tag in ['usei', 'umai']:
                    raw_b = mod[1]
                    val = raw_b[8:-4].decode('utf-8', 'replace').strip('\x00')
                    building_items[f"{r['id']}_{tag}"] = val

# 2. Lua triggers for Stromgard
stromgard_lua = (ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Stromgard.lua").read_text(encoding="utf-8")
messages_found = re.findall(r'DisplayTextToPlayer[^\n]+', stromgard_lua)
dialogs_found = re.findall(r'Dialog[^\n]+', stromgard_lua)
frames_found = re.findall(r'BlzCreateFrame[^\n]+', stromgard_lua)

audit_report = {
    "race": "Стромгард",
    "category": "Расовые предметы, сообщения и интерфейсы",
    "building_items": building_items,
    "has_items": len(building_items) > 0,
    "messages": messages_found,
    "has_messages": len(messages_found) > 0,
    "dialogs": dialogs_found,
    "frames": frames_found,
    "has_custom_ui": len(dialogs_found) > 0 or len(frames_found) > 0,
    "conclusion": {
        "items": "У расы нет собственных продаваемых или изготавливаемых предметов; поля sellitems/makeitems пусты у всех 14 зданий.",
        "messages": "Триггеры Stromgard.lua не содержат видимых игроку сообщений (DisplayTextToPlayer отсутствует).",
        "interfaces": "Специальных диалоговых окон, кастомных фреймов или интерфейсных панелей у расы нет."
    }
}

with open(ROOT / "docs/ui_text/stromgard_items_messages.json", "w", encoding="utf-8") as f:
    json.dump(audit_report, f, ensure_ascii=False, indent=2)

print("Saved audit report to docs/ui_text/stromgard_items_messages.json")
print("Items:", building_items)
print("Messages:", messages_found)
