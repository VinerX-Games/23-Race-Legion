# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

objects = [
    # Selection
    ('ability', 'A0HV'),
    # Buildings
    ('unit', 'n014'), ('unit', 'u00F'), ('unit', 'u00G'), ('unit', 'u00H'),
    ('unit', 'u00I'), ('unit', 'u00J'), ('unit', 'u00K'), ('unit', 'u00L'),
    ('unit', 'u00M'), ('unit', 'u00N'), ('unit', 'n012'), ('unit', 'u03B'),
    ('unit', 'u017'), ('unit', 'h0D1'),
    # Units
    ('unit', 'u00P'), ('unit', 'n011'), ('unit', 'n013'), ('unit', 'u03E'), ('unit', 'u02B'),
    ('unit', 'u00A'), ('unit', 'u00B'), ('unit', 'u00D'), ('unit', 'u00C'),
    ('unit', 'u008'), ('unit', 'u00E'), ('unit', 'u034'),
    ('unit', 'ft00'), ('unit', 'ft01'), ('unit', 'n07H'), ('unit', 'u03D'),
    ('unit', 'n016'), ('unit', 'n017'), ('unit', 'CM00'), ('unit', 'FL00'),
    # Heroes
    ('unit', 'U00O'), ('unit', 'U00V'), ('unit', 'U00U'), ('unit', 'U030'), ('unit', 'U014'),
    # Researches
    ('upgrade', 'R0DQ'), ('upgrade', 'R05I'), ('upgrade', 'R05J'), ('upgrade', 'R05N'),
    ('upgrade', 'R05O'), ('upgrade', 'R05P'), ('upgrade', 'R05Q'), ('upgrade', 'R05L'),
    ('upgrade', 'R05H'), ('upgrade', 'R05E'), ('upgrade', 'R05F'), ('upgrade', 'R05G'),
    ('upgrade', 'R05A'), ('upgrade', 'R05R'), ('upgrade', 'R05D'), ('upgrade', 'R05C'),
    ('upgrade', 'R07I'), ('upgrade', 'R0J5'),
    # Abilities
    ('ability', 'A0CO'), ('ability', 'A0CP'), ('ability', 'A0CR'), ('ability', 'A0CN'),
    ('ability', 'AQ95'), ('ability', 'UN99'), ('ability', 'A0CS'), ('ability', 'AQ11'),
    ('ability', 'A0CK'), ('ability', 'A0CM'), ('ability', 'A0BW'), ('ability', 'A1Q7'),
    ('ability', 'A1LI'), ('ability', 'A1LJ'), ('ability', 'A1LL'), ('ability', 'A1LM'),
    ('ability', 'A0WD'), ('ability', 'A0CX'), ('ability', 'A0WE'), ('ability', 'A0CZ'),
    ('ability', 'CM01'), ('ability', 'CM02'), ('ability', 'CM04'), ('ability', 'CM05'),
    ('ability', 'FL01'), ('ability', 'FL02'), ('ability', 'FL03'), ('ability', 'FL04'),
    ('ability', 'A0BO'), ('ability', 'A0BP'), ('ability', 'A0C5'), ('ability', 'Sch2'),
    ('ability', 'Amel'), ('ability', 'Amed'), ('ability', 'A0C7'), ('ability', 'A0C8'),
    ('ability', 'A0BT'), ('ability', 'A0BU'), ('ability', 'A1PV'), ('ability', 'A0C4'),
    ('ability', 'Arpl'), ('ability', 'Arpm'), ('ability', 'A0BX'), ('ability', 'unA5'),
    ('ability', 'A1PY'), ('ability', 'A0C0'), ('ability', 'A0C2'), ('ability', 'A1PX'),
    ('ability', 'unA0'), ('ability', 'Aspa'), ('ability', 'A1N8'), ('ability', 'Arst'),
    ('ability', 'Auns'), ('ability', 'Afra'), ('ability', 'A0BR'), ('ability', 'Agyd'),
    ('ability', 'Arlm'), ('ability', 'A15N'), ('ability', 'A0CA'), ('ability', 'A0CC'),
    ('ability', 'A1ND'), ('ability', 'A0CG'), ('ability', 'A0WB'), ('ability', 'kel0'),
    ('ability', 'A1LK')
]

print("=== INSPECTING OVERRIDES AND WTS STRINGS ===")
results = []
for otype, oid in objects:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid])
    overrides = res.get('overrides', {})
    fields = res.get('object', {}) or res.get('fields', {})
    
    # Collect text keys
    text_fields = {}
    for k, v in overrides.items():
        if any(tk in k.lower() for tk in ['name', 'tip', 'ubertip', 'propernames', 'hotkey']):
            resolved = resolve(v)
            text_fields[k] = {'raw': v, 'resolved': resolved}
    results.append({'type': otype, 'id': oid, 'overrides_text': text_fields, 'all_overrides': overrides})

(ROOT / "scripts/undead_overrides.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {len(results)} object overrides to scripts/undead_overrides.json")
