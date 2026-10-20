"""Бандиты: Делёж добычи атамана (пассивка ABn1 + исследование RBn1 в Бастионе воров).

Тот же порядок публикации, что в implement_unit_mechanics.py: HiveWE правит копию карты,
в живую карту попадают только новые объекты и разрешённые поля h00Q/h009.
--dry-run печатает новые описания, ничего не записывая.
"""
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

from implement_draenei_rework import MAP, digest, run, clone, fields, register_imports
from implement_unit_mechanics import (ASSETS, BTN, NAME, NUM, BONUS, LABEL, TEXT, UNIT_FIELDS,
                                      c, title, tip, passive, resolve, replace_once, preserve,
                                      verify, publish, OBJECT_FILES)
from wc3_icons import icon_set

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.cache/wc3/bandit-loot'
NEW = {'.w3a': {'ABn1'}, '.w3q': {'RBn1'}}
EDITED = {'.w3u': {'h00Q': UNIT_FIELDS, 'h009': UNIT_FIELDS}}

LOOT_BODY = (f'Когда войска владельца убивают вражеского юнита в радиусе {c(NUM, "800")} от атамана, '
             f'игрок получает {c(BONUS, "+1")} золота.|n|nЗдания, стражи и иллюзии не засчитываются. '
             f'Несколько атаманов рядом не увеличивают награду.')
RESEARCH_LOOT = tip('ИССЛЕДОВАНИЕ', f'Атаманы делят добычу: за каждого вражеского юнита, убитого '
                    f'войсками игрока в радиусе {c(NUM, "800")} от атамана, игрок получает '
                    f'{c(BONUS, "+1")} золота.|n|n|cff{LABEL}Применяется к:|cff{TEXT}|n'
                    f'- {c(NAME, "Атаман")}.')
BULLET_LOOT = (f'- {c(NAME, "Делёж добычи")}: {c(BONUS, "+1")} золота за каждого врага, убитого '
               f'вашими войсками в радиусе {c(NUM, "800")} (требует исследования).')


def unit_tip(code, text):
    if code == 'h00Q':
        anchor = '|n|nАтакует наземные цели.'
        return replace_once(text, anchor, '|n' + BULLET_LOOT + anchor, code)
    tail = c(NAME, 'Большой грабеж') + '.|r'
    return replace_once(text, tail, c(NAME, 'Большой грабеж') + '.|n- ' + c(NAME, 'Делёж добычи') + '.|r',
                        code)


def objects(stage, operations):
    passive(stage, 'ABn1', 'Делёж добычи', 'BanditLoot', LOOT_BODY, (3, 2), 'RBn1', 'бандиты',
            operations)
    clone(stage, 'upgrade', 'R0GU', 'RBn1')
    fields(stage, 'upgrade', 'RBn1', {
        'name1': title('Делёж добычи'), 'editorsuffix1': '(бандиты)', 'art1': BTN.format('BanditLoot'),
        'tip1': title('Делёж добычи'), 'ubertip1': RESEARCH_LOOT, 'maxlevel': 1, 'goldbase': 300,
        'lumberbase': 200, 'timebase': 45, 'race': 'human', 'buttonpos': 3, 'buttonpos2': 0,
        'hotkey1': 'R'}, operations)


def units(stage, operations, dry_run=False):
    ids = list(EDITED['.w3u'])
    tips = resolve(stage, 'unit', ids, 'ubertip')
    current = {o['id']: o['fields'] for o in run(stage, 'get-objects-bulk', '--type', 'unit', '--ids',
               ','.join(ids), '--fields', 'abillist,upgrades,researches')['objects']}
    changes = {code: {'ubertip': unit_tip(code, tips[code])} for code in ids}
    changes['h00Q']['abillist'] = current['h00Q']['abillist'] + ',ABn1'
    changes['h00Q']['upgrades'] = current['h00Q']['upgrades'] + ',RBn1'
    changes['h009']['researches'] = current['h009']['researches'] + ',RBn1'
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
        for relative in icon_set(ASSETS / 'BanditSpell.png', 'BanditLoot', tmp):
            data = (Path(tmp) / relative).read_bytes()
            if (MAP / relative).exists() and (MAP / relative).read_bytes() != data:
                raise RuntimeError(f'Asset conflict: {relative}')
            payload[relative] = data
            report.append({'source': 'BanditSpell.png', 'path': relative,
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
