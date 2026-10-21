"""Clear inherited Ghoul Frenzy requirements on custom passive markers, preserving v3 bytes."""
import argparse
import json
from pathlib import Path

from apply_faceless_object_text import patch_blob
from implement_draenei_rework import object_records
from wc3_object_tools import cli, require
from wc3_project import CACHE, settings


def passive_ids():
    rows = require(cli(['dump-objects', '--type', 'ability', '--fields',
                        'requires,code', '--max', '100000']))['objects']
    return [row['id'] for row in rows if row['id'] != 'Augf'
            and row.get('fields', {}).get('code') == 'APai'
            and row['fields'].get('requires') == 'Rugf']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    targets = passive_ids()
    root = Path(settings()['map'])
    originals, updated, changes = {}, {}, {}
    for name in ('war3map.w3a', 'war3mapSkin.w3a'):
        path = root / name
        if not path.exists():
            continue
        original = path.read_bytes()
        _, tables = object_records(original, True)
        present = {record['id'] for table in tables for record in table}
        operations = [dict(id=code, field='requires', value='') for code in targets if code in present]
        patched, modified = patch_blob(original, operations, 'ability', True)
        if patched != original:
            originals[name], updated[name], changes[name] = original, patched, modified
    report = dict(ok=True, applied=False, targets=targets, changes=changes)
    backup = CACHE / 'passive-requirements-backup'
    if args.apply and updated:
        backup.mkdir(parents=True, exist_ok=True)
        for name, original in originals.items():
            assert (root / name).read_bytes() == original, 'Map changed during preparation'
            (backup / name).write_bytes(original)
        try:
            for name, patched in updated.items():
                (root / name).write_bytes(patched)
            assert not passive_ids(), 'Effective readback still contains false requirements'
            actual = require(cli(['get-object', '--type', 'ability', '--id', 'Augf', '--fields', 'requires']))
            assert actual['fields']['requires'] == 'Rugf', 'Real Ghoul Frenzy requirement changed'
        except Exception:
            for name, original in originals.items():
                (root / name).write_bytes(original)
            raise
        report['applied'] = True
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / 'passive-requirements-result.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Passive requirements: targets={len(targets)} files={len(updated)} applied={report['applied']}")


if __name__ == '__main__':
    main()
