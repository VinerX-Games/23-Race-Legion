# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

def s(raw):
    if not raw:
        return ""
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        sid = int(raw[8:])
        return f"[{sid}] {wts.get(sid, '').strip()}"
    return str(raw).strip()

lines = []
lines.append("=== ALL ABILITIES IN PANDARENS DUMP ===")
for ab in dump["abilities"]:
    aid = ab["id"]
    name = s(ab.get("raw_name"))
    rtip = s(ab.get("raw_researchtip"))
    rub = s(ab.get("raw_researchubertip"))
    lvls = ab.get("levels", 1)
    lines.append(f"\n--- Ability {aid} (lvls={lvls}) ---")
    lines.append(f"Name: {name}")
    if rtip or rub:
        lines.append(f"Researchtip: {rtip}")
        lines.append(f"Researchubertip: {rub}")
    for lvl in range(1, lvls + 1):
        t = s(ab.get("tips", {}).get(f"tip{lvl}", {}).get("raw"))
        u = s(ab.get("ubertips", {}).get(f"ubertip{lvl}", {}).get("raw"))
        lines.append(f"  L{lvl} Tip: {t}")
        lines.append(f"  L{lvl} Ubertip: {u}")

(ROOT / "scripts/pandarens_abilities_detail.txt").write_text("\n".join(lines), encoding="utf-8")
print("Wrote scripts/pandarens_abilities_detail.txt")
