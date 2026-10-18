# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
with open(ROOT / 'scripts/draenei_raw_dump.json', encoding='utf-8') as f:
    d = json.load(f)

with open(ROOT / 'scripts/draenei_analysis.txt', 'w', encoding='utf-8') as out:
    def p(*args):
        out.write(' '.join(str(a) for a in args) + '\n')

    p('=== BUILDINGS ===')
    for b in d['buildings']:
        p(f"[{b['id']}] {b.get('name')} (hotkey: {b.get('hotkey')})")
        p(f"  raw_name: {b.get('raw_name')}, raw_tip: {b.get('raw_tip')}, raw_ubertip: {b.get('raw_ubertip')}")
        p(f"  tip: {b.get('tip')}")
        p(f"  ubertip: {b.get('ubertip')}")
        p(f"  trains: {b.get('trains')}, researches: {b.get('researches')}, upg: {b.get('upgrades_to')}")

    p('\n=== UNITS ===')
    for u in d['units']:
        p(f"[{u['id']}] {u.get('name')} (hotkey: {u.get('hotkey')})")
        p(f"  raw_name: {u.get('raw_name')}, raw_tip: {u.get('raw_tip')}, raw_ubertip: {u.get('raw_ubertip')}")
        p(f"  tip: {u.get('tip')}")
        p(f"  ubertip: {u.get('ubertip')}")
        p(f"  abils: {u.get('abils')}, upgs: {u.get('upgrades')}, targs1: {u.get('targs1')}, targs2: {u.get('targs2')}")

    p('\n=== HEROES ===')
    for h in d['heroes']:
        p(f"[{h['id']}] {h.get('name')} (hotkey: {h.get('hotkey')})")
        p(f"  raw_name: {h.get('raw_name')}, raw_tip: {h.get('raw_tip')}, raw_ubertip: {h.get('raw_ubertip')}")
        p(f"  tip: {h.get('tip')}")
        p(f"  ubertip: {h.get('ubertip')}")
        p(f"  propernames: {h.get('propernames')} (raw: {h.get('raw_propernames')})")
        p(f"  heroabils: {h.get('heroabils')}, abils: {h.get('abils')}")

    p('\n=== UPGRADES ===')
    for up in d['upgrades']:
        p(f"[{up['id']}] levels={up.get('levels')}")
        for lvl, n in up.get('names', {}).items():
            p(f"  {lvl}: {n.get('val')} ({n.get('raw')})")
        for lvl, t in up.get('tips', {}).items():
            p(f"  {lvl} tip: {t.get('val')} ({t.get('raw')})")
        for lvl, u in up.get('ubertips', {}).items():
            p(f"  {lvl} ubertip: {u.get('val')} ({u.get('raw')})")

    p('\n=== ABILITIES ===')
    for ab in d['abilities']:
        p(f"[{ab['id']}] {ab.get('name')} ({ab.get('raw_name')}) levels={ab.get('levels')} hotkey={ab.get('hotkey')}")
        if ab.get('researchtip'):
            p(f"  researchtip: {ab.get('researchtip')} ({ab.get('raw_researchtip')})")
            p(f"  researchubertip: {ab.get('researchubertip')} ({ab.get('raw_researchubertip')})")
        for lvl, t in ab.get('tips', {}).items():
            p(f"  {lvl} tip: {t.get('val')} ({t.get('raw')})")
        for lvl, u in ab.get('ubertips', {}).items():
            p(f"  {lvl} ubertip: {u.get('val')} ({u.get('raw')})")
