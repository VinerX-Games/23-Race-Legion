# -*- coding: utf-8 -*-
"""Inspect detailed fields and strings for all Night Elf objects."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
dump = json.loads((ROOT / 'scripts/nightelf_raw_dump.json').read_text(encoding='utf-8'))

out_lines = []

def p(s=""):
    out_lines.append(s)

p("=== 1. BUILDINGS ===")
for b in dump['buildings']:
    p(f"ID: {b['id']} (hotkey: {b.get('hotkey')})")
    p(f"  Name: [{b.get('raw_name')}] {b.get('name')}")
    p(f"  Tip: [{b.get('raw_tip')}] {b.get('tip')}")
    p(f"  Ubertip: [{b.get('raw_ubertip')}] {b.get('ubertip')}")
    p(f"  Trains: {b.get('train')}")
    p(f"  Researches: {b.get('researches')}")
    p(f"  Upgrades to: {b.get('upgrades_to')}")
    p(f"  HP: {b.get('hp')}, Def: {b.get('def')} ({b.get('deftype')}), Food: fmade={b.get('fmade')}, fused={b.get('fused')}")
    p(f"  Abilities: {b.get('abillist')}")
    p()

p("=== 2. WORKER & UNITS ===")
all_units = dump['workers'] + dump['units']
for u in all_units:
    p(f"ID: {u['id']} (hotkey: {u.get('hotkey')})")
    p(f"  Name: [{u.get('raw_name')}] {u.get('name')}")
    p(f"  Tip: [{u.get('raw_tip')}] {u.get('tip')}")
    p(f"  Ubertip: [{u.get('raw_ubertip')}] {u.get('ubertip')}")
    p(f"  HP: {u.get('hp')}, Mana: {u.get('mana')}, Def: {u.get('def')} ({u.get('deftype')})")
    p(f"  Atk1: type={u.get('atktype1')}, targets={u.get('targs1')}, weapon={u.get('weaptype1')}")
    p(f"  Atk2: type={u.get('atktype2')}, targets={u.get('targs2')}, weapon={u.get('weaptype2')}")
    p(f"  Abilities: {u.get('abillist')}")
    p(f"  Upgrades: {u.get('upgrades')}")
    p()

p("=== 3. HEROES ===")
for h in dump['heroes']:
    p(f"ID: {h['id']} (hotkey: {h.get('hotkey')})")
    p(f"  Name: [{h.get('raw_name')}] {h.get('name')}")
    p(f"  Tip: [{h.get('raw_tip')}] {h.get('tip')}")
    p(f"  Ubertip: [{h.get('raw_ubertip')}] {h.get('ubertip')}")
    p(f"  Awaken: [{h.get('raw_awakentip')}] {h.get('awakentip')}")
    p(f"  Revive: [{h.get('raw_revivetip')}] {h.get('revivetip')}")
    p(f"  Propernames: [{h.get('raw_propernames')}] {h.get('propernames')}")
    p(f"  Hero Abils: {h.get('heroabillist')}")
    p(f"  Abilities: {h.get('abillist')}")
    p(f"  Atk1: type={h.get('atktype1')}, targets={h.get('targs1')}")
    p()

p("=== 4. UPGRADES ===")
for upg in dump['upgrades']:
    p(f"ID: {upg['id']} (levels: {upg['levels']})")
    for i in range(1, upg['levels'] + 1):
        n = upg['names'].get(f'name{i}', {})
        t = upg['tips'].get(f'tip{i}', {})
        ub = upg['ubertips'].get(f'ubertip{i}', {})
        hk = upg['hotkeys'].get(f'hotkey{i}', {})
        p(f"  Lvl {i}: hotkey=[{hk.get('val')}]")
        p(f"    Name: [{n.get('raw')}] {n.get('val')}")
        p(f"    Tip: [{t.get('raw')}] {t.get('val')}")
        p(f"    Ubertip: [{ub.get('raw')}] {ub.get('val')}")
    p()

p("=== 5. ABILITIES ===")
for ab in dump['abilities']:
    p(f"ID: {ab['id']} (levels: {ab['levels']})")
    p(f"  Name: [{ab.get('raw_name')}] {ab.get('name')}")
    p(f"  Hotkey: [{ab.get('raw_hotkey')}] {ab.get('hotkey')}")
    if ab.get('researchtip'):
        p(f"  ResTip: [{ab.get('raw_researchtip')}] {ab.get('researchtip')}")
        p(f"  ResUbertip: [{ab.get('raw_researchubertip')}] {ab.get('researchubertip')}")
    for i in range(1, ab['levels'] + 1):
        t = ab['tips'].get(f'tip{i}', {})
        ub = ab['ubertips'].get(f'ubertip{i}', {})
        p(f"  Lvl {i} Tip: [{t.get('raw')}] {t.get('val')}")
        p(f"  Lvl {i} Ubertip: [{ub.get('raw')}] {ub.get('val')}")
    p()

p("=== 6. BUFFS ===")
for bf in dump['buffs']:
    p(f"ID: {bf['id']}")
    p(f"  Editor: [{bf.get('raw_editorname')}] {bf.get('editorname')}")
    p(f"  Bufftip: [{bf.get('raw_bufftip')}] {bf.get('bufftip')}")
    p(f"  Buffubertip: [{bf.get('raw_buffubertip')}] {bf.get('buffubertip')}")
    p()

out_file = ROOT / "scripts/nightelf_details_all.txt"
out_file.write_text("\n".join(out_lines), encoding='utf-8')
print(f"Wrote details to {out_file}")
