import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    raw = json.load(open(ROOT / "docs/ui_text/elements_unit_abils_raw.json", encoding="utf-8"))
    out_lines = []
    for aid, info in sorted(raw.items()):
        out_lines.append(f"=== Ability ID: {aid} ===")
        out_lines.append(f"Carriers: {', '.join(info['carriers'])}")
        out_lines.append(f"Name: {info['name']} (Raw: {info['raw_name']})")
        out_lines.append(f"Hotkey: {info['hotkey']}")
        out_lines.append(f"ButtonPos: ({info['buttonpos']}, {info['buttonpos2']})")
        out_lines.append(f"Tip1: {info['tip1']} (Raw: {info['raw_tip1']})")
        out_lines.append(f"Ubertip1: {info['ubertip1']} (Raw: {info['raw_ubertip1']})")
        out_lines.append(f"Buffs: {info['buff1']}")
        out_lines.append("")

    (ROOT / "docs/ui_text/elements_unit_abils_detail.txt").write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Written detailed info to docs/ui_text/elements_unit_abils_detail.txt")

if __name__ == "__main__":
    main()
