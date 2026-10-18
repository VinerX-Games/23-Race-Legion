# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

data = json.loads((ROOT / "scripts/undead_raw_dump.json").read_text(encoding="utf-8"))

lines = []

def p(s=""):
    lines.append(s)

p("=== 1. SELECTION ===")
for aid, obj in data['selection'].items():
    p(f"ID: {aid}")
    p(f"  Name: {obj.get('raw_name')} -> {obj.get('name')}")
    p(f"  Tip: {obj.get('tips', {}).get('tip1', {}).get('raw')} -> {obj.get('tips', {}).get('tip1', {}).get('val')}")
    p(f"  Ubertip: {obj.get('ubertips', {}).get('ubertip1', {}).get('raw')} -> {obj.get('ubertips', {}).get('ubertip1', {}).get('val')}")
    p(f"  Hotkey: {obj.get('hotkey')}")

p("\n=== 2. BUILDINGS ===")
for bid, obj in data['buildings'].items():
    p(f"ID: {bid}")
    p(f"  Name: {obj.get('raw_name')} -> {obj.get('name')}")
    p(f"  Tip: {obj.get('raw_tip')} -> {obj.get('tip')}")
    p(f"  Ubertip: {obj.get('raw_ubertip')} -> {obj.get('ubertip')}")
    p(f"  Hotkey: {obj.get('hotkey')}")
    p(f"  Trains: {obj.get('trains')}")
    p(f"  Researches: {obj.get('researches')}")
    p(f"  Upgrades_to: {obj.get('upgrades_to')}")
    p(f"  Abils: {obj.get('abils')}")

p("\n=== 3. UNITS ===")
for uid, obj in data['units'].items():
    p(f"ID: {uid}")
    p(f"  Name: {obj.get('raw_name')} -> {obj.get('name')}")
    p(f"  Tip: {obj.get('raw_tip')} -> {obj.get('tip')}")
    p(f"  Ubertip: {obj.get('raw_ubertip')} -> {obj.get('ubertip')}")
    p(f"  Hotkey: {obj.get('hotkey')}")
    p(f"  Trains: {obj.get('trains')}")
    p(f"  Abils: {obj.get('abils')}")
    p(f"  Upgrades: {obj.get('upgrades')}")
    p(f"  Targs1: {obj.get('targs1')} | Weap1: {obj.get('weaptype1')}")
    p(f"  Targs2: {obj.get('targs2')} | Weap2: {obj.get('weaptype2')}")

p("\n=== 4. HEROES ===")
for hid, obj in data['heroes'].items():
    p(f"ID: {hid}")
    p(f"  Name: {obj.get('raw_name')} -> {obj.get('name')}")
    p(f"  Propernames: {obj.get('propernames')}")
    p(f"  Tip: {obj.get('raw_tip')} -> {obj.get('tip')}")
    p(f"  Ubertip: {obj.get('raw_ubertip')} -> {obj.get('ubertip')}")
    p(f"  Hotkey: {obj.get('hotkey')}")
    p(f"  HeroAbils: {obj.get('heroabils')}")
    p(f"  Abils: {obj.get('abils')}")
    p(f"  Targs1: {obj.get('targs1')} | Weap1: {obj.get('weaptype1')}")

p("\n=== 5. RESEARCHES ===")
for rid, obj in data['researches'].items():
    p(f"ID: {rid} | Levels: {obj.get('levels')} | Class: {obj.get('class')}")
    p(f"  Applies: {obj.get('applies_to')}")
    p(f"  Effects: {obj.get('effects')}")
    for i in range(1, obj.get('levels', 1) + 1):
        n = obj.get('names', {}).get(f'name{i}', {})
        t = obj.get('tips', {}).get(f'tip{i}', {})
        u = obj.get('ubertips', {}).get(f'ubertip{i}', {})
        hk = obj.get('hotkeys', {}).get(f'hotkey{i}', {})
        p(f"  L{i}: name={n.get('raw')} -> {n.get('val')}")
        p(f"       tip={t.get('raw')} -> {t.get('val')}")
        p(f"       ub={u.get('raw')} -> {u.get('val')}")
        p(f"       hk={hk.get('raw')} -> {hk.get('val')}")

p("\n=== 6. ABILITIES ===")
for aid, obj in data['abilities'].items():
    p(f"ID: {aid} | Levels: {obj.get('levels')} | Name: {obj.get('raw_name')} -> {obj.get('name')} | HK: {obj.get('hotkey')} | ResHK: {obj.get('researchhotkey')}")
    for i in range(1, obj.get('levels', 1) + 1):
        t = obj.get('tips', {}).get(f'tip{i}', {})
        u = obj.get('ubertips', {}).get(f'ubertip{i}', {})
        p(f"  L{i}: tip={t.get('raw')} -> {t.get('val')}")
        p(f"       ub={u.get('raw')} -> {u.get('val')}")
    if obj.get('raw_researchtip') or obj.get('raw_researchubertip'):
        p(f"  Res: tip={obj.get('raw_researchtip')} -> {obj.get('researchtip')}")
        p(f"       ub={obj.get('raw_researchubertip')} -> {obj.get('researchubertip')}")

(ROOT / "scripts/undead_details.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"Details written to scripts/undead_details.txt ({len(lines)} lines)")
