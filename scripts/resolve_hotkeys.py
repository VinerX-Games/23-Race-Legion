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
        return wts.get(sid, "").strip()
    return str(raw).strip()

lines = []
lines.append("=== ABILITY HOTKEYS ===")
for ab in dump["abilities"]:
    aid = ab["id"]
    f = ab.get("fields", {})
    ov = ab.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    hk = s(gv("hotkey") or ab.get("hotkey"))
    rhk = s(gv("researchhotkey") or ab.get("researchhotkey"))
    if hk or rhk:
        lines.append(f"{aid}: hk='{hk}', rhk='{rhk}'")

lines.append("\n=== UPGRADE HOTKEYS ===")
for up in dump["upgrades"]:
    uid = up["id"]
    f = up.get("fields", {})
    ov = up.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lvls = up.get("levels", 1)
    hks = [s(gv(f"hotkey{l}") or gv("hotkey")) for l in range(1, lvls + 1)]
    lines.append(f"{uid}: hks={hks}")

lines.append("\n=== BUILDING HOTKEYS ===")
for b in dump["buildings"]:
    bid = b["id"]
    f = b.get("fields", {})
    ov = b.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lines.append(f"{bid}: name='{s(b.get('raw_name'))}', hk='{s(gv('hotkey'))}'")

lines.append("\n=== HERO HOTKEYS ===")
for h in dump["heroes"]:
    hid = h["id"]
    f = h.get("fields", {})
    ov = h.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lines.append(f"{hid}: name='{s(h.get('raw_name'))}', hk='{s(gv('hotkey'))}'")

lines.append("\n=== UNIT HOTKEYS ===")
for u in dump["units"]:
    uid = u["id"]
    f = u.get("fields", {})
    ov = u.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lines.append(f"{uid}: name='{s(u.get('raw_name'))}', hk='{s(gv('hotkey'))}'")

(ROOT / "scripts/pandarens_hotkeys.txt").write_text("\n".join(lines), encoding="utf-8")
print("Wrote scripts/pandarens_hotkeys.txt")
