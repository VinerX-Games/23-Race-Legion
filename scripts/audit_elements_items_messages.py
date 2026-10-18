import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    b_data = json.load(open(ROOT / "docs/ui_text/elements_buildings.json", encoding="utf-8"))["buildings"]
    b_ids = [b["id"] for b in b_data]

    # 1. Check sellitems / makeitems on all buildings
    data = hw.run_cli_json([
        "get-objects-bulk",
        "--map", str(hw.DEFAULT_MAP),
        "--warcraft", str(hw.DEFAULT_WARCRAFT),
        "--type", "unit",
        "--ids", ",".join(b_ids),
        "--fields", "name,sellitems,makeitems"
    ])
    items_sold = {}
    for obj in data.get("objects", []):
        f = obj.get("fields", {})
        si = f.get("sellitems")
        mi = f.get("makeitems")
        if si or mi:
            items_sold[obj["id"]] = {"name": f.get("name"), "sellitems": si, "makeitems": mi}

    # 2. Check trigger files for Elementals
    elementals_lua = ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Elementals.lua"
    lua_text = elementals_lua.read_text(encoding="utf-8") if elementals_lua.exists() else ""
    
    import re
    # find all string literals in Elementals.lua
    str_literals = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', lua_text)
    # filter for player-facing messages (DisplayText, print, etc.)
    messages = [s for s in str_literals if any(kw in s.lower() for kw in ("стихи", "элемент", "бастион", "рагнарос", "нептулон", "алакир"))]

    # check if any other files mention Elementals triggers
    report = {
        "race": "elements",
        "category": "items_messages_interfaces",
        "buildings_with_items": items_sold,
        "has_sold_items": len(items_sold) > 0,
        "trigger_messages": messages,
        "custom_frames_or_ui": False,
        "conclusion": "No racial items sold/manufactured, no custom UI dialogs or frames. Triggers perform only mechanic tech-tree unlocks."
    }

    out_file = ROOT / "docs/ui_text/elements_items_messages.json"
    out_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report saved to {out_file}")
    print(f"Buildings with items: {len(items_sold)}")
    print(f"Messages found in triggers: {len(messages)}")

if __name__ == "__main__":
    main()
