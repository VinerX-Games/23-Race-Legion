# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def search():
    found = {'ability': {}, 'upgrade': {}, 'buff': {}}
    for t in ['ability', 'upgrade', 'buff']:
        for q in ['Наги', 'Вайш', 'Мурлок', 'Murloc', 'Naga']:
            res = hw.run_cli_json(['search-objects', '--map', str(hw.DEFAULT_MAP), '--type', t, '--query', q])
            for m in res.get('matches', []):
                oid = m.get('id')
                if oid:
                    found[t][oid] = m
    for t, objs in found.items():
        print(f"=== {t.upper()} ({len(objs)}) ===")
        for oid, m in sorted(objs.items()):
            print(f"  {oid}: {m.get('name')} | suffix: {m.get('editorsuffix')}")

if __name__ == '__main__':
    search()
