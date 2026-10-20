"""Ночнорождённые: Лунный снаряд глефомёта (пассивка AMn1 + исследование RMn1 в Казармах).

Тот же порядок публикации, что в implement_unit_mechanics.py: HiveWE правит копию карты,
в живую карту попадают только новые объекты и разрешённые поля e01B/h0CF.
--dry-run печатает новые описания, ничего не записывая.
"""
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

from implement_draenei_rework import MAP, digest, run, clone, fields, register_imports
from implement_unit_mechanics import (ASSETS, BTN, NAME, NUM, LABEL, TEXT, UNIT_FIELDS, c, title, tip,
                                      passive, resolve, replace_once, preserve, verify, publish,
                                      OBJECT_FILES)
from wc3_icons import icon_set

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.cache/wc3/nightborne-glaive'
NEW = {'.w3a': {'AMn1'}, '.w3q': {'RMn1'}}
EDITED = {'.w3u': {'e01B': UNIT_FIELDS, 'h0CF': UNIT_FIELDS}}

MOON_BODY = (f'Ночью после попадания глефа дважды отскакивает в ближайших врагов в радиусе '
             f'{c(NUM, "450")}. Каждый отскок теряет {c(NUM, "20%")} урона.|n|nОтскакивает только '
             f'в наземные юниты, не в здания.')
RESEARCH_MOON = tip('ИССЛЕДОВАНИЕ', f'Ночью глефы глефомётов после попадания дважды отскакивают '
                    f'в ближайших врагов; каждый отскок теряет {c(NUM, "20%")} урона.'
                    f'|n|n|cff{LABEL}Применяется к:|cff{TEXT}|n- {c(NAME, "Глефомет")}.')
BULLET_MOON = (f'- {c(NAME, "Лунный снаряд")}: ночью глефа дважды отскакивает в ближайших врагов '
               f'(требует исследования).')


def unit_tip(code, text):
    if code == 'e01B':
        anchor = '|n|nАтакует наземные цели.'
        return replace_once(text, anchor, '|n' + BULLET_MOON + anchor, code)
    head, sep, tail = text.partition(f'|cff{LABEL}Исследования:|cff{TEXT}')
    names = re.findall(r'\|cffebc56c([^|]+)\|cffced4da', tail)
    assert sep and names[-1] == 'Стальные снаряды', (code, text)
    return head + sep + ''.join(f'|n- {c(NAME, n)}.' for n in names + ['Лунный снаряд']) + '|r'


def objects(stage, operations):
    passive(stage, 'AMn1', 'Лунный снаряд', 'NightborneMoonGlaive', MOON_BODY, (2, 2), 'RMn1',
            'ночнорождённые', operations)
    clone(stage, 'upgrade', 'R0GU', 'RMn1')
    fields(stage, 'upgrade', 'RMn1', {
        'name1': title('Лунный снаряд'), 'editorsuffix1': '(ночнорождённые)',
        'art1': BTN.format('NightborneMoonGlaive'), 'tip1': title('Лунный снаряд'),
        'ubertip1': RESEARCH_MOON, 'maxlevel': 1, 'goldbase': 250, 'lumberbase': 250,
        'timebase': 45, 'requires1': 'h0CC', 'race': 'nightelf', 'buttonpos': 3, 'buttonpos2': 1,
        'hotkey1': 'F'}, operations)


def units(stage, operations, dry_run=False):
    ids = list(EDITED['.w3u'])
    tips = resolve(stage, 'unit', ids, 'ubertip')
    current = {o['id']: o['fields'] for o in run(stage, 'get-objects-bulk', '--type', 'unit', '--ids',
               ','.join(ids), '--fields', 'abillist,upgrades,researches')['objects']}
    changes = {code: {'ubertip': unit_tip(code, tips[code])} for code in ids}
    changes['e01B']['abillist'] = current['e01B']['abillist'] + ',AMn1'
    changes['e01B']['upgrades'] = current['e01B']['upgrades'] + ',RMn1'
    changes['h0CF']['researches'] = current['h0CF']['researches'] + ',RMn1'
    if dry_run:
        for code, values in changes.items():
            print(code, json.dumps(values, ensure_ascii=False), '\n')
        return
    for code, values in changes.items():
        fields(stage, 'unit', code, values, operations)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    stage = OUT / 'stage'
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir()
    hashes = {name: digest(MAP / name) for name in OBJECT_FILES}
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, stage / name)
    if '--dry-run' in sys.argv:
        units(stage, [], dry_run=True)
        return

    payload, report = {}, []
    with tempfile.TemporaryDirectory() as tmp:
        for relative in icon_set(ASSETS / 'NightborneSpell.jpg', 'NightborneMoonGlaive', tmp):
            data = (Path(tmp) / relative).read_bytes()
            if (MAP / relative).exists() and (MAP / relative).read_bytes() != data:
                raise RuntimeError(f'Asset conflict: {relative}')
            payload[relative] = data
            report.append({'source': 'NightborneSpell.jpg', 'path': relative,
                           'sha256': hashlib.sha256(data).hexdigest()})

    operations = []
    objects(stage, operations)
    units(stage, operations)
    original = OUT / 'current-original'
    original.mkdir(exist_ok=True)
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, original / name)
    for name in OBJECT_FILES:
        suffix = Path(name).suffix
        if suffix in ('.w3a', '.w3q', '.w3u', '.w3h') and (original / name).exists():
            preserve(original / name, stage / name, NEW.get(suffix, set()), EDITED.get(suffix, {}))
    verify(stage, operations)
    register_imports(stage / 'war3map.imp', payload)
    changed = publish(stage, hashes)
    for relative, data in payload.items():
        path = MAP / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
    (OUT / 'implementation.json').write_text(json.dumps(
        {'objects': operations, 'assets': report, 'before_hashes': hashes, 'changed_files': changed},
        ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Published {len(operations)} verified fields; {len(payload)} assets; changed: {changed}')


if __name__ == '__main__':
    main()
