"""Способности огров: Пригвоздить, Нарастающая ярость, Поступь гронна, Пиршество.

Object data и иконки. Использует узкую публикацию из implement_draenei_rework.py: HiveWE
правит копию карты, в живую карту попадают только новые объекты и явно изменённые поля юнитов.
--dry-run печатает новые описания юнитов, ничего не записывая;
--rebuild-upgrades пересоздаёт только исследования ROg2/ROg4;
--update-stride обновляет только замедление Поступи гронна.
"""
import hashlib
import json
import os
import re
import shutil
import struct
import sys
import tempfile
from pathlib import Path

from implement_draenei_rework import (MAP, digest, run, clone, fields, register_imports,
                                      object_records, preserve_unrelated)
from wc3_icons import icon_set

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'Assets'
OUT = ROOT / '.cache/wc3/ogre-abilities'
OBJECT_FILES = ['war3map.w3a', 'war3mapSkin.w3a', 'war3map.w3q', 'war3mapSkin.w3q',
                'war3map.w3u', 'war3mapSkin.w3u', 'war3map.w3h', 'war3mapSkin.w3h',
                'war3map.wts', 'war3map.imp']
NEW = {'.w3a': {'AOg1', 'AOg2', 'AOg3', 'AOg4', 'AOg5', 'AOg6'}, '.w3q': {'ROg2', 'ROg4'},
       '.w3u': {'nOg1'}, '.w3h': {'BOg1', 'BOg2'}}

ICONS = {'Pin': 'OgronSpell4.png', 'Rage': 'OgronSpell.png',
         'Stomp': 'OgronSpell2.png', 'Feast': 'OgronSpell3.png'}
BTN = 'ReplaceableTextures\\CommandButtons\\BTNOgre{}.blp'
PAS = 'ReplaceableTextures\\PassiveButtons\\PASBTNOgre{}.blp'

# Пиршество получают все боевые юниты огров; строитель и герои — нет.
WARRIORS = ['o03F', 'o03G', 'o03H', 'o03I', 'o03K', 'o03L', 'o03M', 'o03N',
            'o03O', 'o03P', 'o03Q', 'o03R', 'o03S', 'o03T', 'o03U', 'o03V']
OGRONS = ['o03Q', 'o03S']
GRONNS = ['o03T', 'o03U', 'o03V']
BASH = 'A176'

TEXT, LABEL, NAME, NUM, BONUS = 'ced4da', 'b99d66', 'ebc56c', 'ffffff', 'c8e087'


def c(color, text):
    return f'|cff{color}{text}|cff{TEXT}'


def title(name):
    return f'|cff{NAME}{name}|r'


def ability_tip(body):
    return f'|cff{LABEL}СПОСОБНОСТЬ:|cff{TEXT} {body}|r'


PIN_BODY = (f'Каждый {c(NUM, "5")}-й бросок копья по вражескому юниту пригвождает цель к земле '
            f'на {c(NUM, "1")} сек., героя — на {c(NUM, "0.2")} сек. Цель не может двигаться, '
            f'но может атаковать и применять способности.|n|n'
            f'Броски по зданиям и невосприимчивым к магии целям не засчитываются.')
RAGE_BODY = (f'Атаки огрона наносят {c(BONUS, "+2%")} урона за каждые {c(NUM, "10%")} '
             f'потерянного здоровья, до {c(BONUS, "+18%")}.')
STRIDE_BODY = (f'Раз в {c(NUM, "6")} сек., когда рядом есть наземные враги, гронн топает: '
               f'вражеские здания в радиусе {c(NUM, "250")} получают {c(NUM, "30")} урона, '
               f'остальные наземные враги замедляются на {c(NUM, "30%")} по скорости бега '
               f'на {c(NUM, "3")} сек.')
FEAST_BODY = (f'Каждое убийство вражеского юнита навсегда увеличивает максимальный запас '
              f'здоровья огра на {c(BONUS, "+15")}, до {c(BONUS, "+150")}.|n|n'
              f'Здания, иллюзии и стражи не засчитываются.')


def pin_tip(level):
    left = 6 - level
    state = ('Следующий бросок пригвоздит цель.' if left == 1
             else f'Осталось бросков до пригвождения: {c(NUM, left)}.')
    return ability_tip(f'{PIN_BODY}|n|n{state}')


def feast_tip(level):
    return ability_tip(f'{FEAST_BODY}|n|nНакоплено: {c(BONUS, "+" + str(15 * (level - 1)))} '
                       f'из {c(NUM, "150")} здоровья.')


RESEARCH_RAGE = (f'|cff{LABEL}ИССЛЕДОВАНИЕ:|cff{TEXT} Огроны наносят {c(BONUS, "+2%")} урона '
                 f'атаками за каждые {c(NUM, "10%")} потерянного здоровья, до {c(BONUS, "+18%")}.'
                 f'|n|nПрименяется к:|n- {c(NAME, "Огрон")}.|n- {c(NAME, "Огрон Красный")}.|r')
RESEARCH_FEAST = (f'|cff{LABEL}ИССЛЕДОВАНИЕ:|cff{TEXT} Каждое убийство вражеского юнита навсегда '
                  f'увеличивает максимальный запас здоровья огра на {c(BONUS, "+15")}, '
                  f'до {c(BONUS, "+150")}. Здания, иллюзии и стражи не засчитываются.'
                  f'|n|nПрименяется к:|n- {c(NAME, "Всем воинам армии Огров")}.|r')

BULLET_PIN = (f'- {c(NAME, "Пригвоздить")}: каждый {c(NUM, "5")}-й бросок обездвиживает цель на '
              f'{c(NUM, "1")} сек. (героя — на {c(NUM, "0.2")} сек.).')
BULLET_RAGE = (f'- {c(NAME, "Нарастающая ярость")}: {c(BONUS, "+2%")} урона за каждые '
               f'{c(NUM, "10%")} потерянного здоровья (требует исследования).')
BULLET_STRIDE = (f'- {c(NAME, "Поступь гронна")}: раз в {c(NUM, "6")} сек. наносит '
                 f'{c(NUM, "30")} урона вражеским зданиям рядом и замедляет наземных врагов.')
BULLET_FEAST = (f'- {c(NAME, "Пиршество")}: каждое убийство даёт {c(BONUS, "+15")} к здоровью, '
                f'до {c(BONUS, "+150")} (требует исследования).')
BASH_LINE = re.compile(r'\|n- \|cffebc56cСильный удар\|cffced4da:[^|]*(?:\|cff[0-9a-f]{6}[^|]*)*?\.(?=\|n)')


def unit_tip(code, text):
    """Заменить пункт «Сильный удар» и дописать новые пункты в список способностей."""
    replacement = {'o03H': BULLET_PIN, **{g: BULLET_STRIDE for g in GRONNS}}.get(code)
    if replacement is not None:
        text, count = BASH_LINE.subn('|n' + replacement, text)
        assert count == 1, (code, text)
    added = ([BULLET_RAGE] if code in OGRONS else []) + [BULLET_FEAST]
    if code == 'o03H':
        # Оружие 1 бьёт только наземные цели; старый текст ошибочно упоминал воздушные.
        text = text.replace(f'|cff{NUM}наземные|cff{TEXT} и |cff{NUM}воздушные|cff{TEXT} цели',
                            f'|cff{NUM}наземные|cff{TEXT} цели')
    anchor = '|n|nАтакует'
    assert text.count(anchor) == 1 and 'Способности:' in text, (code, text)
    return text.replace(anchor, ''.join('|n' + x for x in added) + anchor)


def building_tip(text, research):
    tail = f'|cff{TEXT}.|r'
    assert text.endswith(tail), text
    return text[:-len(tail)] + f'|cff{TEXT}|n- {c(NAME, research)}.|r'


def resolve(stage, kind, ids, column):
    strings = {int(k): v.strip() for k, v in re.findall(
        r'STRING (\d+)[^{]*\{(.*?)\}', (stage / 'war3map.wts').read_text(encoding='utf-8-sig'), re.S)}
    objects = run(stage, 'get-objects-bulk', '--type', kind, '--ids', ','.join(ids),
                  '--fields', column)['objects']
    result = {}
    for obj in objects:
        value = obj['fields'][column]
        if value.startswith('TRIGSTR_'):
            # set-field выделяет новую строку WTS, общие строки других объектов не меняются.
            value = strings[int(value[8:])]
        result[obj['id']] = value
    return result


def passive(stage, code, name, icon, levels, tips, pos, requires, operations):
    clone(stage, 'ability', 'AOcr', code)
    values = {'name': title(name), 'editorsuffix': '(огры)', 'art': PAS.format(icon),
              'hero': 0, 'item': 0, 'race': 'orc', 'levels': levels, 'reqlevel': 0,
              'requires': requires, 'buttonpos': pos[0], 'buttonpos2': pos[1],
              'targetart': '', 'casterart': '', 'effectart': '', 'hotkey': ''}
    for level in range(1, levels + 1):
        values.update({f'tip{level}': title(name), f'ubertip{level}': tips(level),
                       f'dataa{level}': 0, f'datab{level}': 1, f'datac{level}': 0,
                       f'datad{level}': 0})
    fields(stage, 'ability', code, values, operations)


def objects(stage, operations):
    passive(stage, 'AOg1', 'Пригвоздить', 'Pin', 5, pin_tip, (1, 1), '', operations)
    passive(stage, 'AOg2', 'Нарастающая ярость', 'Rage', 1, lambda _: ability_tip(RAGE_BODY),
            (2, 2), 'ROg2', operations)
    passive(stage, 'AOg3', 'Поступь гронна', 'Stomp', 1, lambda _: ability_tip(STRIDE_BODY),
            (1, 1), '', operations)
    passive(stage, 'AOg4', 'Пиршество', 'Feast', 11, feast_tip, (3, 2), 'ROg4', operations)

    service = ability_tip('Служебная способность для Lua-механик огров.')
    clone(stage, 'buff', 'Beng', 'BOg1')
    fields(stage, 'buff', 'BOg1', {
        'bufftip': title('Пригвождение'), 'editorsuffix': '(огры)', 'buffart': BTN.format('Pin'),
        'buffubertip': f'|cff{LABEL}ЭФФЕКТ:|cff{TEXT} Цель |cffef8173не может двигаться|cff{TEXT}, '
                       f'но может атаковать и применять способности.|r'}, operations)
    clone(stage, 'buff', 'BHtc', 'BOg2')
    fields(stage, 'buff', 'BOg2', {
        'bufftip': title('Поступь гронна'), 'editorsuffix': '(огры)', 'buffart': BTN.format('Stomp'),
        'buffubertip': f'|cff{LABEL}ЭФФЕКТ:|cff{TEXT} Скорость передвижения и атаки '
                       f'|cffef8173снижена|cff{TEXT}.|r'}, operations)

    clone(stage, 'ability', 'Aens', 'AOg5')
    fields(stage, 'ability', 'AOg5', {
        'name': title('Пригвоздить'), 'editorsuffix': '(огры: служебное)', 'art': BTN.format('Pin'),
        'hero': 0, 'item': 0, 'race': 'orc', 'levels': 1, 'tip1': title('Пригвоздить'),
        'ubertip1': service, 'dur1': 1, 'herodur1': 0.2, 'rng1': 1200, 'cool1': 0, 'cost1': 0,
        'missilespeed': 100000, 'missilehoming': 1, 'buffid1': 'BOg1,BOg1',
        'targs1': 'ground,air,enemy,neutral,vulnerable'}, operations)
    clone(stage, 'ability', 'AHtc', 'AOg6')
    fields(stage, 'ability', 'AOg6', {
        'name': title('Поступь гронна'), 'editorsuffix': '(огры: служебное)', 'art': BTN.format('Stomp'),
        'hero': 0, 'item': 0, 'race': 'orc', 'levels': 1, 'tip1': title('Поступь гронна'),
        'ubertip1': service, 'area1': 250, 'dataa1': 0, 'datab1': 0, 'datac1': 0.3, 'datad1': 0,
        'dur1': 3, 'herodur1': 3, 'cool1': 0, 'cost1': 0, 'casterart': '',
        'buffid1': 'BOg2', 'targs1': 'ground,enemy,neutral'}, operations)

    # Нулевая точка каста: общий даммик карты h05P кастует с задержкой 0,3 с.
    clone(stage, 'unit', 'h05P', 'nOg1')
    fields(stage, 'unit', 'nOg1', {
        'name': title('Заклинатель огров'), 'editorsuffix': '(огры: служебное)',
        'abillist': 'Aloc,Avul,AOg5,AOg6', 'abilskinlist': '', 'upgrades': '',
        'castpt': 0, 'castbsw': 0, 'weapson': 0, 'acquire': 0, 'sight': 0, 'nsight': 0,
        'ubertip': f'|cff{LABEL}ЮНИТ:|cff{TEXT} Служебный источник способностей огров. '
                   f'Не атакует.|r'}, operations)
    upgrades(stage, operations)


def upgrades(stage, operations):
    # У R0GU (Опутывание) нет класса, эффектов и базового требования. Клоны исследований
    # на основе Robk/Rome сохраняют ванильное требование ostr, которое выдаётся только ботам.
    for code, name, tip, pos, hotkey, gold, lumber, time, requires in [
            ('ROg2', 'Нарастающая ярость', RESEARCH_RAGE, (3, 0), 'R', 300, 200, 40, 'o03E'),
            ('ROg4', 'Пиршество', RESEARCH_FEAST, (2, 2), 'C', 400, 250, 50, 'o03D')]:
        clone(stage, 'upgrade', 'R0GU', code)
        fields(stage, 'upgrade', code, {
            'name1': title(name), 'editorsuffix1': '(огры)',
            'art1': BTN.format('Rage' if code == 'ROg2' else 'Feast'),
            'tip1': title(name), 'ubertip1': tip, 'maxlevel': 1, 'goldbase': gold,
            'lumberbase': lumber, 'timebase': time, 'requires1': requires, 'race': 'orc',
            'buttonpos': pos[0], 'buttonpos2': pos[1], 'hotkey1': hotkey}, operations)


def drop_records(path, ids):
    """Удалить записи объектов целиком, чтобы clone() пересоздал их от новой основы."""
    version, tables = object_records(path.read_bytes(), path.suffix in ('.w3a', '.w3q'))
    output = bytearray(struct.pack('<I', version))
    for table in tables:
        kept = [record['raw'] for record in table if record['id'] not in ids]
        output += struct.pack('<I', len(kept)) + b''.join(kept)
    path.write_bytes(output)


def publish(stage, hashes, names):
    for name, previous in hashes.items():
        if digest(MAP / name) != previous:
            raise RuntimeError(f'Concurrent change: {name}')
    changed = []
    for name in names:
        source = stage / name
        if source.exists() and digest(source) != hashes[name]:
            tmp = MAP / (name + '.ogre.tmp')
            shutil.copy2(source, tmp)
            os.replace(tmp, MAP / name)
            changed.append(name)
    return changed


def stride_fields(stage, operations):
    fields(stage, 'ability', 'AOg3', {'ubertip1': ability_tip(STRIDE_BODY)}, operations)
    fields(stage, 'ability', 'AOg6', {'datad1': 0, 'herodur1': 3}, operations)


def update_stride(stage, hashes):
    """Обновить только замедление Поступи гронна (AOg3/AOg6) в таблицах способностей и WTS."""
    operations = []
    stride_fields(stage, operations)
    ids = {'AOg3', 'AOg6'}
    for name in ('war3map.w3a', 'war3mapSkin.w3a'):
        preserve_unrelated(MAP / name, stage / name, ids)
    verify(stage, operations)
    changed = publish(stage, hashes, ['war3map.w3a', 'war3mapSkin.w3a', 'war3map.wts'])
    print(f'Stride updated: {len(operations)} verified fields; changed: {changed}')


def rebuild_upgrades(stage, hashes):
    """Пересоздать ROg2/ROg4, затрагивая только таблицы исследований и WTS."""
    for name in ('war3map.w3q', 'war3mapSkin.w3q'):
        drop_records(stage / name, NEW['.w3q'])
    operations = []
    upgrades(stage, operations)
    for name in ('war3map.w3q', 'war3mapSkin.w3q'):
        preserve_unrelated(MAP / name, stage / name, NEW['.w3q'])
    verify(stage, operations)
    changed = publish(stage, hashes, ['war3map.w3q', 'war3mapSkin.w3q', 'war3map.wts'])
    print(f'Rebuilt researches: {len(operations)} verified fields; changed: {changed}')


def units(stage, operations, dry_run=False):
    tips = resolve(stage, 'unit', WARRIORS + ['o03A', 'o03C'], 'ubertip')
    current = {o['id']: o['fields'] for o in run(
        stage, 'get-objects-bulk', '--type', 'unit', '--ids', ','.join(WARRIORS + ['o03A', 'o03C']),
        '--fields', 'abillist,upgrades,researches')['objects']}
    changes = {}
    for code in WARRIORS:
        abilities = [a for a in current[code]['abillist'].split(',') if a]
        if code == 'o03H' or code in GRONNS:
            assert BASH in abilities, code
            abilities[abilities.index(BASH)] = 'AOg1' if code == 'o03H' else 'AOg3'
        abilities += (['AOg2'] if code in OGRONS else []) + ['AOg4']
        upgrades = [u for u in current[code]['upgrades'].split(',') if u]
        upgrades += (['ROg2'] if code in OGRONS else []) + ['ROg4']
        changes[code] = {'abillist': ','.join(abilities), 'upgrades': ','.join(upgrades),
                         'ubertip': unit_tip(code, tips[code])}
    for code, research in [('o03A', 'ROg4'), ('o03C', 'ROg2')]:
        changes[code] = {'researches': current[code]['researches'] + ',' + research,
                         'ubertip': building_tip(tips[code], 'Пиршество' if code == 'o03A'
                                                 else 'Нарастающая ярость')}
    if dry_run:
        for code, values in changes.items():
            print(code, json.dumps(values, ensure_ascii=False), '\n')
        return
    for code, values in changes.items():
        fields(stage, 'unit', code, values, operations)


def verify(stage, operations):
    strings = {int(k): v.strip() for k, v in re.findall(
        r'STRING (\d+)[^{]*\{(.*?)\}', (stage / 'war3map.wts').read_text(encoding='utf-8-sig'), re.S)}
    for kind in ['ability', 'upgrade', 'unit', 'buff']:
        relevant = [op for op in operations if op['type'] == kind]
        if not relevant:
            continue
        ids = sorted({op['id'] for op in relevant})
        columns = sorted({op['field'] for op in relevant})
        actual = {x['id']: x['fields'] for x in run(stage, 'get-objects-bulk', '--type', kind,
                  '--ids', ','.join(ids), '--fields', ','.join(columns))['objects']}
        for op in relevant:
            value = actual[op['id']][op['field']]
            if value.startswith('TRIGSTR_'):
                value = strings[int(value[8:])]
            expected = str(op['value'])
            if value != expected:
                try:
                    assert abs(float(value) - float(expected)) < 1e-6
                except (ValueError, AssertionError):
                    raise AssertionError((op, value))


def main():
    dry_run = '--dry-run' in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    stage = OUT / 'stage'
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir()
    hashes = {name: digest(MAP / name) for name in OBJECT_FILES}
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, stage / name)
    if dry_run:
        units(stage, [], dry_run=True)
        return
    if '--update-stride' in sys.argv:
        update_stride(stage, hashes)
        return
    if '--rebuild-upgrades' in sys.argv:
        rebuild_upgrades(stage, hashes)
        return

    payload, assets = {}, []
    with tempfile.TemporaryDirectory() as tmp:
        for name, source in ICONS.items():
            for relative in icon_set(ASSETS / source, 'Ogre' + name, tmp):
                data = (Path(tmp) / relative).read_bytes()
                target = MAP / relative
                if target.exists() and target.read_bytes() != data:
                    raise RuntimeError(f'Asset conflict: {relative}')
                payload[relative] = data
                assets.append({'source': source, 'path': relative,
                               'sha256': hashlib.sha256(data).hexdigest()})

    operations = []
    objects(stage, operations)
    units(stage, operations)

    original = OUT / 'current-original'
    original.mkdir(exist_ok=True)
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, original / name)
    edited_units = set(WARRIORS) | {'o03A', 'o03C'}
    for name in OBJECT_FILES:
        suffix = Path(name).suffix
        if suffix in NEW and (original / name).exists():
            preserve_unrelated(original / name, stage / name, NEW[suffix],
                               edited_units if suffix == '.w3u' else set())
    verify(stage, operations)
    register_imports(stage / 'war3map.imp', payload)

    changed = publish(stage, hashes, OBJECT_FILES)
    for relative, data in payload.items():
        path = (MAP / relative).resolve()
        assert path.is_relative_to(MAP.resolve())
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
    report = {'objects': operations, 'assets': assets, 'before_hashes': hashes,
              'changed_files': changed}
    (OUT / 'implementation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2),
                                             encoding='utf-8')
    print(f'Published {len(operations)} verified fields; {len(payload)} assets; changed: {changed}')


if __name__ == '__main__':
    main()
