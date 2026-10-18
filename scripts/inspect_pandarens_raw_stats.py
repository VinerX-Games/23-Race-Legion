# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

lines = []

lines.append("=== ABILITY STATS ===")
for ab in dump["abilities"]:
    aid = ab["id"]
    f = ab.get("fields", {})
    ov = ab.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    hk = gv("hotkey") or ab.get("hotkey")
    rhk = gv("researchhotkey") or ab.get("researchhotkey")
    lvls = ab.get("levels", 1)
    lines.append(f"\nAbility {aid}: name={gv('name')}, hotkey={hk}, rhk={rhk}, lvls={lvls}")
    for l in range(1, lvls + 1):
        mana = gv(f"cost{l}") or gv("cost") or gv(f"mana{l}")
        cool = gv(f"cool{l}") or gv("cool")
        rng = gv(f"castrange{l}") or gv(f"rng{l}")
        dur = gv(f"dur{l}")
        hero_dur = gv(f"herodur{l}")
        d_a = gv(f"dataa{l}")
        d_b = gv(f"datab{l}")
        d_c = gv(f"datac{l}")
        d_d = gv(f"datad{l}")
        d_e = gv(f"datae{l}")
        lines.append(f"  L{l}: mana={mana}, cool={cool}, range={rng}, dur={dur}/{hero_dur}, Data=(A:{d_a}, B:{d_b}, C:{d_c}, D:{d_d}, E:{d_e})")

lines.append("\n=== UPGRADE STATS ===")
for up in dump["upgrades"]:
    uid = up["id"]
    f = up.get("fields", {})
    ov = up.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lvls = up.get("levels", 1)
    lines.append(f"\nUpgrade {uid}: lvls={lvls}")
    for l in range(1, lvls + 1):
        hk = gv(f"hotkey{l}") or gv("hotkey")
        gold = gv(f"gold{l}") or gv("gold")
        lumb = gv(f"lumber{l}") or gv("lumber")
        time = gv(f"time{l}") or gv("time")
        eff = gv(f"effect{l}")
        lines.append(f"  L{l}: hotkey={hk}, cost={gold}/{lumb}, time={time}")

lines.append("\n=== UNIT & HERO STATS ===")
for cat in ["heroes", "units"]:
    for u in dump[cat]:
        uid = u["id"]
        f = u.get("fields", {})
        ov = u.get("overrides", {})
        def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
        lines.append(f"\n{cat[:-1].upper()} {uid}: name={gv('name')}, hotkey={gv('hotkey')}")
        lines.append(f"  cost={gv('goldcost')}/{gv('lumbercost')}, food={gv('fmade') or gv('fuse')}, hp={gv('realhp') or gv('hp')}, mana={gv('mana0') or gv('manan')}")
        lines.append(f"  armor={gv('def')}, atk1={gv('mindmg1')}-{gv('maxdmg1')} (cool={gv('cool1')}, range={gv('rangen1')})")
        if cat == "heroes":
            lines.append(f"  primary={gv('primary')}, STR={gv('str')}+{gv('strplus')}, AGI={gv('agi')}+{gv('agiplus')}, INT={gv('int')}+{gv('intplus')}")

lines.append("\n=== BUILDING STATS ===")
for b in dump["buildings"]:
    bid = b["id"]
    f = b.get("fields", {})
    ov = b.get("overrides", {})
    def gv(k): return ov.get(k) if ov.get(k) is not None else f.get(k)
    lines.append(f"\nBUILDING {bid}: name={gv('name')}, hotkey={gv('hotkey')}")
    lines.append(f"  cost={gv('goldcost')}/{gv('lumbercost')}, food={gv('fmade')}, hp={gv('realhp') or gv('hp')}, armor={gv('def')}")

(ROOT / "scripts/pandarens_raw_stats.txt").write_text("\n".join(lines), encoding="utf-8")
print("Wrote scripts/pandarens_raw_stats.txt")
