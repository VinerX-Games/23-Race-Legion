import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    abils = [
        'A01N', 'A01R', 'A01S', 'A0CE', 'A0I3', 'A0OZ', 'A0PG', 'A0PH', 'A0Q8', 'A0Q9',
        'A0QA', 'A0QC', 'A0QD', 'A0QE', 'A0QF', 'A0QG', 'A0QH', 'A0QI', 'A0QM',
        'A0W7', 'A0W8', 'A0W9', 'A0WA', 'A18B', 'A1MQ', 'Adis'
    ]
    data = hw.run_cli_json([
        'get-objects-bulk',
        '--map', str(hw.DEFAULT_MAP),
        '--warcraft', str(hw.DEFAULT_WARCRAFT),
        '--type', 'ability',
        '--ids', ','.join(abils)
    ])
    wts = hw.load_wts_strings()
    resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    results = {}
    for obj in data.get("objects", []):
        aid = obj["id"]
        f = obj.get("fields", {})
        results[aid] = {k: resolve(v) for k, v in f.items()}

    out = ROOT / "docs/ui_text/elements_unit_abils_mechanics.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Dumped mechanics to {out}")

    for aid in abils:
        f = results.get(aid, {})
        print(f"[{aid}] {f.get('name')}")
        interesting = {k: v for k, v in f.items() if any(x in k.lower() for x in ('data', 'dur', 'cool', 'cost', 'rng', 'area', 'targ'))}
        for k, v in sorted(interesting.items()):
            print(f"    {k}: {v}")

if __name__ == "__main__":
    main()
