# -*- coding: utf-8 -*-
"""Comprehensive inspection and inventory dump for Race 12: Scarlet Crusade (Алый Орден).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

buildings = [
    'h05U', 'h05V', 'h05W', 'h05X', 'h05Y', 'h05Z', 'h060', 'h061',
    'h062', 'h063', 'h064', 'h068'
]

heroes = ['H03H', 'H06C', 'H06B']

units = [
    'h014', 'h039', 'h03A', 'h03B', 'h03C', 'h03D', 'h03F', 'h03G',
    'h03I', 'h065', 'h066', 'h067', 'n007', 'n008', 'o00I'
]

hero_abils = [
    'A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M',
    'A09G', 'A09F', 'A09I', 'A09J'
]

unit_abils = [
    'A09O', 'A081', 'A080', 'A07Z', 'A07X', 'A0OY', 'A08E', 'A08D',
    'A085', 'A08Y', 'A08X', 'A08P', 'A08O', 'A08F', 'A08G', 'A07I',
    'A08K', 'A083', 'A08J', 'A08L', 'A08M', 'A084', 'A08N', 'A082',
    'A08C', 'A088', 'A089', 'A07Y', 'A087', 'A08B', 'A08A', 'ANha', 'Ahrp'
]

upgrades = [
    'R040', 'R03Z', 'R03W', 'R03V', 'R03K', 'R03L', 'R03M', 'R048',
    'R049', 'R04A', 'R04B', 'R04C', 'R03X', 'R03Y', 'R0KG', 'R0KH',
    'R047', 'R046', 'R045', 'R03S', 'R03T', 'R044', 'R043', 'R042',
    'R041', 'R07B', 'R03U'
]

dump = {
    "selection": {},
    "buildings": {},
    "heroes": {},
    "units": {},
    "abilities": {},
    "upgrades": {},
    "discovered_abils": set(),
    "discovered_buffs": set(),
    "discovered_trains": set(),
    "discovered_researches": set()
}

# 1. Selection spell A0HM
res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', 'A0HM'])
dump["selection"] = res.get('object', {}) or res.get('fields', {})

# 2. Buildings
for b in buildings:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', b])
    f = res.get('object', {}) or res.get('fields', {})
    dump["buildings"][b] = f
    trains = f.get('trains', '')
    if trains:
        for t in trains.split(','):
            t = t.strip()
            if t: dump["discovered_trains"].add(t)
    researches = f.get('researches', '')
    if researches:
        for r in researches.split(','):
            r = r.strip()
            if r: dump["discovered_researches"].add(r)
    abils = f.get('abillist', '')
    if abils:
        for a in abils.split(','):
            a = a.strip()
            if a: dump["discovered_abils"].add(a)

# 3. Heroes
for h in heroes:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', h])
    f = res.get('object', {}) or res.get('fields', {})
    dump["heroes"][h] = f
    habils = f.get('heroabils', '') or f.get('heroabillist', '')
    if habils:
        for a in habils.split(','):
            a = a.strip()
            if a: dump["discovered_abils"].add(a)
    abils = f.get('abillist', '')
    if abils:
        for a in abils.split(','):
            a = a.strip()
            if a: dump["discovered_abils"].add(a)

# 4. Units
for u in units:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', u])
    f = res.get('object', {}) or res.get('fields', {})
    dump["units"][u] = f
    abils = f.get('abillist', '')
    if abils:
        for a in abils.split(','):
            a = a.strip()
            if a: dump["discovered_abils"].add(a)

# Also check worker builds
worker_builds = dump["units"].get('h014', {}).get('builds', '')
print(f"Worker h014 builds: {worker_builds}")

all_abils = set(hero_abils) | set(unit_abils) | dump["discovered_abils"]
for a in sorted(all_abils):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', a])
    f = res.get('object', {}) or res.get('fields', {})
    dump["abilities"][a] = f
    buffs = f.get('buffid', '') or f.get('buffs', '')
    if buffs:
        for bf in buffs.split(','):
            bf = bf.strip()
            if bf: dump["discovered_buffs"].add(bf)

all_upgrades = set(upgrades) | dump["discovered_researches"]
for upg in sorted(all_upgrades):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', upg])
    f = res.get('object', {}) or res.get('fields', {})
    dump["upgrades"][upg] = f

# Convert sets to sorted lists for json serialization
dump["discovered_abils"] = sorted(dump["discovered_abils"])
dump["discovered_buffs"] = sorted(dump["discovered_buffs"])
dump["discovered_trains"] = sorted(dump["discovered_trains"])
dump["discovered_researches"] = sorted(dump["discovered_researches"])

out_path = ROOT / "scripts/scarlet_raw_dump.json"
out_path.write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Dump saved to {out_path}")
print(f"Discovered trains: {dump['discovered_trains']}")
print(f"Discovered researches: {dump['discovered_researches']}")
print(f"Discovered abils: {dump['discovered_abils']}")
print(f"Discovered buffs: {dump['discovered_buffs']}")
