# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

spells = ["A0KS", "A0LD", "A0LE", "A0BK", "A0LH", "A0LJ", "A0LI", "A0IQ", "A0AS", "A0AT", "Argl", "A15N"]
units = ["h0G8", "h07A", "h07R"]

print("=== SPELLS ===")
for s in spells:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", s])
    if res.get("ok"):
        f = res.get("object", {}) or res.get("fields", {})
        print(f"[{s}] {resolve(f.get('name'))} -> tip={resolve(f.get('tip1'))}, code={f.get('code')}")
    else:
        print(f"[{s}] NOT FOUND")

print("\n=== UNITS ===")
for u in units:
    res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", u])
    if res.get("ok"):
        f = res.get("object", {}) or res.get("fields", {})
        print(f"[{u}] {resolve(f.get('name'))} ({resolve(f.get('editorsuffix'))}) -> isbldg={f.get('isbldg')}")
    else:
        print(f"[{u}] NOT FOUND")
