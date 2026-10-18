# -*- coding: utf-8 -*-
"""Inspect detailed parameters of Elements hero abilities."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

hero_raw = json.loads((ROOT / "docs/ui_text/elements_hero_abils_raw.json").read_text(encoding="utf-8"))

heroes_order = [
    ("H0EZ", "Кристальный владыка", ["A1MR", "A0P4", "A0P2", "AEtq"]),
    ("H0F0", "Мастер ветра", ["A0P9", "A0PA", "A1LE", "AHpx"]),
    ("N037", "Повелитель огня", ["ANic", "AHfs", "ANlm", "A0P7"]),
    ("E029", "Владыка морей", ["A0OU", "A0OT", "A0QL", "A0OR", "A0YH"]),
    ("E027", "Владыка ветра", ["A0P0", "A0OX", "A0OW", "A0P1", "A0YI"]),
    ("E028", "Владыка Огня", ["A0OP", "A0ON", "A0QJ", "A0OQ", "A0YG"])
]

out = []
for hid, hname, abils in heroes_order:
    out.append(f"\n=======================================================")
    out.append(f"HERO: {hid} - {hname}")
    out.append(f"=======================================================")
    for aid in abils:
        f = hero_raw.get(aid, {})
        code = f.get("code", {}).get("text", "")
        name = f.get("name", {}).get("text", "")
        hotkey = f.get("hotkey", {}).get("text", "")
        rhotkey = f.get("researchhotkey", {}).get("text", "")
        levels = int(f.get("levels", {}).get("text", "1") or "1")
        rtip = f.get("researchtip", {}).get("text", "")
        rubertip = f.get("researchubertip", {}).get("text", "")
        
        out.append(f"\nAbility: {aid} (Base: {code}, Levels: {levels}, Hotkey: {hotkey}/{rhotkey})")
        out.append(f"  Name: {name}")
        out.append(f"  ResearchTip: {rtip}")
        out.append(f"  ResearchUbertip: {rubertip}")
        
        for lvl in range(1, levels + 1):
            tip = f.get(f"tip{lvl}", {}).get("text", "")
            utub = f.get(f"ubertip{lvl}", {}).get("text", "")
            cool = f.get(f"cool{lvl}", {}).get("text", "")
            cost = f.get(f"cost{lvl}", {}).get("text", "")
            dur = f.get(f"dur{lvl}", {}).get("text", "")
            hdur = f.get(f"herodur{lvl}", {}).get("text", "")
            dataa = f.get(f"dataa{lvl}", {}).get("text", "")
            datab = f.get(f"datab{lvl}", {}).get("text", "")
            datac = f.get(f"datac{lvl}", {}).get("text", "")
            datad = f.get(f"datad{lvl}", {}).get("text", "")
            out.append(f"  [Lvl {lvl}] Tip: {tip}")
            out.append(f"         Ubertip: {utub}")
            out.append(f"         Stats: Mana={cost}, Cool={cool}, Dur={dur}/{hdur}, DataA={dataa}, DataB={datab}, DataC={datac}, DataD={datad}")

detail_txt = "\n".join(out)
(ROOT / "docs/ui_text/elements_hero_abils_detail.txt").write_text(detail_txt, encoding="utf-8")
print("Saved detailed report to docs/ui_text/elements_hero_abils_detail.txt")
