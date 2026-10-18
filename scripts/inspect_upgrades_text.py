# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

lines = []
for up in dump["upgrades"]:
    uid = up["id"]
    lvls = up.get("levels") or 1
    lines.append(f"\n=== Upgrade {uid} (lvls={lvls}) ===")
    for l in range(1, lvls + 1):
        n_raw = up.get("names", {}).get(f"name{l}", {}).get("raw")
        t_raw = up.get("tips", {}).get(f"tip{l}", {}).get("raw")
        u_raw = up.get("ubertips", {}).get(f"ubertip{l}", {}).get("raw")
        def psid(r):
            if isinstance(r, str) and r.startswith("TRIGSTR_"):
                try:
                    sid = int(r[8:])
                    return f"[{sid}] {wts.get(sid, '')}"
                except ValueError:
                    pass
            return str(r)
        lines.append(f"  L{l}: name={psid(n_raw)}")
        lines.append(f"       tip={psid(t_raw)}")
        lines.append(f"       ub={psid(u_raw)}")

(ROOT / "scripts/pandarens_upgrades_text.txt").write_text("\n".join(lines), encoding="utf-8")
print("Wrote scripts/pandarens_upgrades_text.txt")
