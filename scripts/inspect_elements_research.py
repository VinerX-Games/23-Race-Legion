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
    wts = hw.load_wts_strings()
    resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    results = {}
    for obj in data.get("objects", []):
        rid = obj["id"]
        f = obj.get("fields", {})
        max_lvl = int(f.get("maxlevel", 1))
        names = [resolve(f.get(f"name{i}", "")) for i in range(1, max_lvl + 1)]
        raw_names = [f.get(f"name{i}", "") for i in range(1, max_lvl + 1)]
        tips = [resolve(f.get(f"tip{i}", "")) for i in range(1, max_lvl + 1)]
        raw_tips = [f.get(f"tip{i}", "") for i in range(1, max_lvl + 1)]
        ubertips = [resolve(f.get(f"ubertip{i}", "")) for i in range(1, max_lvl + 1)]
        raw_ubertips = [f.get(f"ubertip{i}", "") for i in range(1, max_lvl + 1)]
        hotkeys = [f.get(f"hotkey{i}", "") for i in range(1, max_lvl + 1)]

        effects = []
        for i in range(1, 5):
            eff = f.get(f"effect{i}")
            if eff:
                effects.append({
                    "effect": eff,
                    "base": f.get(f"base{i}"),
                    "mod": f.get(f"mod{i}"),
                    "code": f.get(f"code{i}"),
                    "target": f.get(f"target{i}")
                })

        results[rid] = {
            "id": rid,
            "maxlevel": max_lvl,
            "names": names,
            "raw_names": raw_names,
            "tips": tips,
            "raw_tips": raw_tips,
            "ubertips": ubertips,
            "raw_ubertips": raw_ubertips,
            "hotkeys": hotkeys,
            "buttonpos": f.get("buttonpos"),
            "buttonpos2": f.get("buttonpos2"),
            "requires": [f.get(f"requires{i}") for i in range(1, 4) if f.get(f"requires{i}")],
            "effects": effects,
            "all_fields": {k: resolve(v) for k, v in f.items()}
        }

    out = ROOT / "docs/ui_text/elements_research_raw.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Dumped {len(results)} researches to {out}")

    lines = []
    for rid, r in sorted(results.items()):
        lines.append(f"=== [{rid}] MaxLevel: {r['maxlevel']} Pos: ({r['buttonpos']}, {r['buttonpos2']}) Req: {r['requires']} ===")
        for lvl in range(1, r["maxlevel"] + 1):
            idx = lvl - 1
            lines.append(f"  Level {lvl}:")
            lines.append(f"    Name: {r['names'][idx]} (Raw: {r['raw_names'][idx]})")
            lines.append(f"    Tip:  {r['tips'][idx]} (Raw: {r['raw_tips'][idx]})")
            lines.append(f"    Uber: {r['ubertips'][idx]} (Raw: {r['raw_ubertips'][idx]})")
            lines.append(f"    HK:   {r['hotkeys'][idx]}")
        if r["effects"]:
            lines.append("  Effects:")
            for e in r["effects"]:
                lines.append(f"    {e}")
        lines.append("")

    (ROOT / "docs/ui_text/elements_research_detail.txt").write_text("\n".join(lines), encoding="utf-8")
    print("Written detailed summary to docs/ui_text/elements_research_detail.txt")

if __name__ == "__main__":
    main()
