# -*- coding: utf-8 -*-
"""Inspect detailed mechanics and fields of Elements hero abilities."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

hero_raw = json.loads((ROOT / "docs/ui_text/elements_hero_abils_raw.json").read_text(encoding="utf-8"))

for aid, fields in hero_raw.items():
    print(f"\n==================== {aid} ====================")
    for k in sorted(fields.keys()):
        v = fields[k]
        if isinstance(v, dict):
            raw = v.get("raw")
            text = v.get("text")
            wts_id = v.get("wts_id")
            if wts_id:
                print(f"  {k}: WTS_{wts_id} -> {repr(text[:80])}")
            else:
                print(f"  {k}: raw={raw} text={repr(str(text)[:80])}")
        else:
            print(f"  {k}: {repr(str(v)[:80])}")
