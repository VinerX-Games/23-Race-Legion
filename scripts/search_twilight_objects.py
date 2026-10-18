# -*- coding: utf-8 -*-
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

def search_text():
    output = {}
    queries = ["сумеречн", "культ", "бездн", "ksmolot", "молот"]
    for q in queries:
        output[q] = {}
        for t in ["unit", "ability", "upgrade", "buff", "item"]:
            res = hw.run_cli_json(['search-objects', '--map', str(hw.DEFAULT_MAP), '--type', t, '--query', q, '--limit', '100'])
            results = res.get('results', [])
            output[q][t] = results

    out_path = ROOT / "scripts/twilight_search_results.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved results to {out_path}")

if __name__ == '__main__':
    search_text()
