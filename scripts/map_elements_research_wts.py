import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    researches = [
        "R0DS", "R09G", "R09H", "R09I", "R09J",
        "R09Q", "R09R", "R09S",
        "R09T", "R09U", "R09V", "Resi",
        "R0A1", "R0A0", "R09Z",
        "R09X", "R09Y"
    ]
    data = hw.run_cli_json([
        "get-objects-bulk",
        "--map", str(hw.DEFAULT_MAP),
        "--warcraft", str(hw.DEFAULT_WARCRAFT),
        "--type", "upgrade",
        "--ids", ",".join(researches)
    ])
    wts_dict = hw.load_wts_strings()

    wts_map = {}
    total_fields = 0
    wts_count = 0
    inline_count = 0

    for obj in data.get("objects", []):
        rid = obj["id"]
        f = obj.get("fields", {})
        max_lvl = int(f.get("maxlevel", 1))
        wts_map[rid] = {"maxlevel": max_lvl, "levels": {}}

        for lvl in range(1, max_lvl + 1):
            wts_map[rid]["levels"][lvl] = {}
            for field in ("name", "tip", "ubertip"):
                total_fields += 1
                key = f"{field}{lvl}"
                raw_val = f.get(key)
                if raw_val and raw_val.startswith("TRIGSTR_"):
                    wid = int(raw_val[8:])
                    wts_map[rid]["levels"][lvl][field] = {
                        "raw": raw_val,
                        "wts_id": wid,
                        "val": wts_dict.get(wid, "")
                    }
                    wts_count += 1
                else:
                    wts_map[rid]["levels"][lvl][field] = {
                        "raw": raw_val,
                        "wts_id": None,
                        "val": raw_val or ""
                    }
                    inline_count += 1

    out = ROOT / "docs/ui_text/elements_research_wts_map.json"
    out.write_text(json.dumps(wts_map, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Total fields: {total_fields}, WTS: {wts_count}, Inline: {inline_count}")

    # Check for duplicate WTS within researches
    all_wids = []
    for rid, info in wts_map.items():
        for lvl, fields in info["levels"].items():
            for f, meta in fields.items():
                if meta["wts_id"]:
                    all_wids.append((meta["wts_id"], rid, lvl, f))

    print(f"Total WTS keys in researches: {len(all_wids)}, unique: {len(set(x[0] for x in all_wids))}")
    from collections import Counter
    c = Counter(x[0] for x in all_wids)
    for wid, count in c.items():
        if count > 1:
            print(f"Duplicate within research batch: WTS {wid} x{count}: {[x for x in all_wids if x[0]==wid]}")

if __name__ == "__main__":
    main()
