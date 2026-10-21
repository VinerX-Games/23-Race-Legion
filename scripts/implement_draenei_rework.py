"""Stage the five Draenei abilities/researches and import their reference assets.

Uses HiveWE for object edits; preserves a pre-edit snapshot and verifies that
unrelated workspace changes were not overwritten before publishing the stage.
"""
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
from pathlib import Path

from wc3_project import settings
from wc3_object_binary import object_records


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / 'map.w3x'
SOURCE = ROOT / '.cache/wc3/bane-burrow'
OUT = ROOT / '.cache/wc3/draenei-rework'
CLI = settings()['cli']
OBJECT_FILES = ['war3map.w3a', 'war3mapSkin.w3a', 'war3map.w3q',
                'war3mapSkin.w3q', 'war3map.w3u', 'war3mapSkin.w3u', 'war3map.wts', 'war3map.imp']
NAMES = ['Призматические наконечники', 'Озарённый клинок', 'Обет защитника',
         'Спасительный свет', 'Идол памяти']
ICON_NAMES = ['Prismatic', 'Blade', 'Vow', 'Salvation', 'Memory']
ICON_SOURCES = ['BTNExodar Draenei - Exiled Arrowhead.blp',
                'BTNLightforged - NovaFire.blp', 'BTNExodar Draenei - Shield of Argus.blp',
                'BTNExodar Draenei - Harmonized.blp', 'BTNExodar Draenei - Arkonite Radiance.blp']
EFFECTS = {
    'NetherArrow.mdx': 'Exodar Draenei - Nether Arrow.mdx',
    'BlazingSpecialArt.mdx': 'Lightforged - BlazingSpecialArt.mdx',
    'GlowShield.mdx': 'Lightforged - GlowShield026.mdx',
    'Reconstitute.mdx': 'Exodar Draenei - Reconstitute.mdx',
    'HolyAura.mdx': 'Lightforged - Runical-Holy Aura.mdx',
}
TIPS = [
    'Два заряда. Обычная атака по вражескому юниту расходует заряд, наносит ещё 8 урона '
    'основной цели и по 15 магического урона двум ближайшим врагам в радиусе 220. '
    'Не срабатывает у иллюзий и против зданий. Один заряд восстанавливается за 18 сек.; '
    'в поле собственного Идола памяти — за 12 сек. Усиленный выстрел не расходует ману.',
    'При здоровье не ниже 85% следующая обычная атака по вражескому юниту наносит ещё 30 урона. '
    'Восстановление: 8 сек. В поле собственного Идола памяти восстанавливается на 50% быстрее. '
    'Получение не менее 20 реальных HP от Спасительного света или Идола памяти сокращает '
    'оставшееся восстановление на 2 сек. Не срабатывает у иллюзий и против зданий.',
    'На 12 сек. даёт союзному юниту 3 заряда: каждая вражеская обычная атака расходует '
    'заряд и наносит на 30% меньше урона. На герое: 2 заряда, снижение урона 15%, '
    'длительность 8 сек. Не действует на здания и иллюзии. Повторное применение обновляет '
    'обет, эффекты не складываются. С благословением Спасительного света действует '
    'большее снижение урона. Дальность 600; 70 маны; восстановление 24 сек.',
    'Исцеляет раненую союзную органическую цель на 130 HP, затем до двух ближайших '
    'раненых союзников на 97,5 и 73,125 HP. Радиус каждого перехода 500. '
    'После исследования Благословение Наару первая цель, получившая не менее 20 HP, '
    'получает на 4 сек. снижение вражеского урона на 10%; герой — на 3 сек. и 5%. '
    'Благословения не складываются. Не лечит здания, механизмы и иллюзии. '
    'Дальность 600; 90 маны; восстановление 30 сек.',
    'Создаёт Идол памяти на 25 сек. В радиусе 400 раз в секунду лечит до шести '
    'наиболее раненых собственных органических юнитов на 2% максимального HP '
    '(героев — на 1%), максимум 40 HP за импульс на цель. Ускоряет восстановление '
    'Призматических наконечников и Озарённого клинка на 50%. Поля и лечение идолов '
    'не складываются. Один идол на провидца. Не лечит здания, механизмы и иллюзии. '
    'Дальность 500; 150 маны; восстановление 30 сек.',
]
UNIT_TIPS = {
    'e000': 'Дренейка-охотница дальнего боя. После исследования Призматических наконечников '
            'готовит два заряженных выстрела с осколками. Идол памяти ускоряет восстановление зарядов.',
    'h059': 'Воин Озарённых ближнего боя. Сохраняет Посвященное оружие. После исследования '
            'Озарённого клинка при высоком здоровье готовит усиленный удар. Лечение и Идол памяти '
            'помогают быстрее подготовить следующий удар.',
    'h01O': 'Элитный воин дренеев. Сохраняет Свет небес, Ауру света и Возрождение. После '
            'исследования Обета защитника прикрывает одного союзника зарядами защиты от атак. '
            'Защита героев слабее и длится меньше.',
    'h01R': 'Жрица Наару лечит до трёх раненых союзников Спасительным светом. Благословение Наару '
            'позволяет кратко защищать первую существенно исцелённую цель. Сохраняет Внутреннее '
            'жжение и Воскрешение.',
    'n005': 'Сломленный провидец дальнего боя. Сохраняет Щит молний, Поле слома и способности '
            'Сломленных. После исследования Памяти предков создаёт Идол памяти: лечит собственный '
            'отряд и ускоряет восстановление Призматических наконечников и Озарённого клинка.',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def run(map_path, *args):
    proc = subprocess.run([CLI, *map(str, args), '--map', str(map_path)],
                          capture_output=True, timeout=60)
    raw = proc.stdout.decode('utf-8', errors='replace')
    data = json.loads(raw[raw.index('{'):])
    if proc.returncode or not data.get('ok'):
        raise RuntimeError(f'{args}: {data}')
    return data


def fields(stage, kind, code, values, operations):
    for field, value in values.items():
        run(stage, 'set-field', '--type', kind, '--id', code, '--field', field, '--value', value)
        operations.append({'type': kind, 'id': code, 'field': field, 'value': value})


def clone(stage, kind, source, code):
    found = run(stage, 'get-objects-bulk', '--type', kind, '--ids', code)
    if not found['objects']:
        run(stage, 'copy-object', '--type', kind, '--source', source, '--new-id', code)


def textures(path):
    blob = path.read_bytes()
    assert blob[:4] == b'MDLX', path
    offset, result = 4, []
    while offset + 8 <= len(blob):
        tag, size = blob[offset:offset + 4], struct.unpack_from('<I', blob, offset + 4)[0]
        chunk = blob[offset + 8:offset + 8 + size]
        assert len(chunk) == size
        if tag == b'TEXS':
            assert size % 268 == 0
            for start in range(0, size, 268):
                name = chunk[start + 4:start + 264].split(b'\0')[0].decode('utf-8')
                if name:
                    result.append(name)
        offset += 8 + size
    return result


def register_imports(path, assets):
    """Append custom-path imports without rewriting existing names/flags."""
    blob = path.read_bytes()
    version, count = struct.unpack_from('<II', blob)
    pos, existing = 8, set()
    for _ in range(count):
        end = blob.index(0, pos + 1)
        existing.add(blob[pos + 1:end].decode('utf-8').replace('\\', '/').lower())
        pos = end + 1
    assert pos == len(blob), 'Unexpected trailing bytes in import table'
    additions = []
    for relative in sorted(set(assets)):
        if relative.replace('\\', '/').lower() not in existing:
            additions.append(b'\x0d' + relative.replace('/', '\\').encode('utf-8') + b'\0')
    if additions:
        path.write_bytes(struct.pack('<II', version, count + len(additions)) + blob[8:] + b''.join(additions))
    return len(additions)


def preserve_unrelated(original_path, edited_path, new_ids, unit_ids=()):
    """Keep existing records byte-for-byte; publish only the explicitly edited fields."""
    extended = original_path.suffix in ('.w3a', '.w3q')
    original = original_path.read_bytes()
    edited = edited_path.read_bytes()
    version, before = object_records(original, extended)
    _, after = object_records(edited, extended)
    lookup = {x['id']: x for table in after for x in table}
    output = bytearray(struct.pack('<I', version))
    allowed = {'uabi', 'upgr', 'ures', 'utub'}
    for index, table in enumerate(before):
        result = []
        for record in table:
            if record['id'] in new_ids:
                result.append(lookup[record['id']]['raw'])
            elif record['id'] in unit_ids:
                current = lookup[record['id']]
                replacements = {key: raw for key, raw in current['mods'] if key[0] in allowed}
                mods = [(key, replacements.pop(key, raw)) for key, raw in record['mods']]
                mods += list(replacements.items())
                result.append(record['header'] + struct.pack('<I', len(mods)) + b''.join(raw for _, raw in mods))
            else:
                result.append(record['raw'])
        known = {x['id'] for x in table}
        for record in after[index]:
            if record['id'] in new_ids and record['id'] not in known:
                result.append(record['raw'])
        output += struct.pack('<I', len(result)) + b''.join(result)
    edited_path.write_bytes(output)
    _, verified = object_records(bytes(output), extended)
    for index, table in enumerate(before):
        by_id = {x['id']: x for x in verified[index]}
        for record in table:
            if record['id'] not in unit_ids and record['id'] not in new_ids:
                assert by_id[record['id']]['raw'] == record['raw'], record['id']


def preserve_stage(stage, original):
    for name in OBJECT_FILES:
        if name.endswith(('.w3a', '.w3q', '.w3u')) and (original / name).exists():
            new = {f'ADr{i}' for i in range(1, 6)} if name.endswith('.w3a') else (
                {f'RDr{i}' for i in range(1, 6)} if name.endswith('.w3q') else {'nDr1'})
            units = {'e000','h059','h01O','h01R','n005','h033','h058','h05A'} if name.endswith('.w3u') else set()
            preserve_unrelated(original / name, stage / name, new, units)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    before, stage = OUT / 'before', OUT / 'stage'
    before.mkdir(exist_ok=True)
    stage.mkdir(exist_ok=True)
    hashes = {name: digest(MAP / name) for name in OBJECT_FILES}
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            if not (before / name).exists():
                shutil.copy2(MAP / name, before / name)
            shutil.copy2(MAP / name, stage / name)
    operations, assets, payload = [], [], {}

    def asset(source, destination):
        data = (SOURCE / source).read_bytes()
        target = MAP / destination
        if target.exists() and target.read_bytes() != data:
            raise RuntimeError(f'Asset conflict: {destination}')
        payload[destination] = data
        assets.append({'source': source, 'path': destination, 'bytes': len(data),
                       'sha256': hashlib.sha256(data).hexdigest()})

    for short, source in zip(ICON_NAMES, ICON_SOURCES):
        asset(source, f'ReplaceableTextures/CommandButtons/BTNDraenei{short}.blp')
        asset('ReplaceableTextures/CommandButtonsDisabled/DIS' + source,
              f'ReplaceableTextures/CommandButtonsDisabled/DISBTNDraenei{short}.blp')
    # Passive icons preserve the reference artwork and its disabled counterpart.
    for short, source in zip(ICON_NAMES[:2], ICON_SOURCES[:2]):
        passive = 'PAS' + source[3:]
        asset(passive, f'ReplaceableTextures/PassiveButtons/PASBTNDraenei{short}.blp')
        asset('ReplaceableTextures/CommandButtonsDisabled/DIS' + passive,
              f'ReplaceableTextures/CommandButtonsDisabled/DISPASBTNDraenei{short}.blp')
    for target, source in EFFECTS.items():
        asset(source, 'Draenei/Effects/' + target)
        for name in textures(SOURCE / source):
            relative = name.replace('\\', '/')
            if (SOURCE / relative).is_file():
                asset(relative, relative)
            else:
                assert run(MAP, 'asset-exists', '--path', name)['found'], name

    for i, name in enumerate(NAMES, 1):
        code = f'ADr{i}'
        passive = i <= 2
        clone(stage, 'ability', 'AOcr' if passive else 'ANcl', code)
        icon = (f'ReplaceableTextures\\PassiveButtons\\PASBTNDraenei{ICON_NAMES[i-1]}.blp'
                if passive else f'ReplaceableTextures\\CommandButtons\\BTNDraenei{ICON_NAMES[i-1]}.blp')
        values = {'name': name, 'editorsuffix': '(дренеи: переработка)', 'art': icon,
                  'hero': 0, 'item': 0, 'race': 'human', 'levels': 3 if i == 1 else 1,
                  'reqlevel': 0, 'requires': '' if i == 4 else f'RDr{i}',
                  'buttonpos': [0, 3, 1, 0, 3][i-1], 'buttonpos2': 1 if i == 2 else 2,
                  'targetart': '', 'casterart': '', 'effectart': '', 'hotkey': ['P','L','B','W','E'][i-1]}
        for level in range(1, 4 if i == 1 else 2):
            values[f'tip{level}'] = name + (f' ({3-level}/2)' if i == 1 else '')
            values[f'ubertip{level}'] = TIPS[i-1]
            values[f'cost{level}'] = 0
            values[f'dataa{level}'] = 0
            values[f'datab{level}'] = 1 if passive else 0
            values[f'datac{level}'] = 0
            values[f'datad{level}'] = 0
            values[f'datae{level}'] = 0
            values[f'dataf{level}'] = 0 if passive else 'channel'
        if not passive:
            values.update({'datab1': 2 if i == 5 else 1, 'datac1': 17, 'datae1': 0,
                           'dataf1': ['spiritlink', 'healingwave', 'healingward'][i-3],
                           'order': ['spiritlink', 'healingwave', 'healingward'][i-3],
                           'cost1': [70,90,150][i-3], 'cool1': [24,30,30][i-3],
                           'rng1': 500 if i == 5 else 600, 'cast1': 0,
                           'targs1': '' if i == 5 else 'air,ground,friend,self,organic',
                           'animnames': 'spell'})
        fields(stage, 'ability', code, values, operations)

    research_names = NAMES[:3] + ['Благословение Наару', 'Память предков']
    for i, name in enumerate(research_names, 1):
        code = f'RDr{i}'
        clone(stage, 'upgrade', 'R02O', code)
        values = {'name1': name, 'editorsuffix1': '(дренеи: переработка)',
                  'art1': f'ReplaceableTextures\\CommandButtons\\BTNDraenei{ICON_NAMES[i-1]}.blp',
                  'tip1': 'Изучить ' + name, 'ubertip1': TIPS[i-1],
                  'maxlevel': 1, 'goldbase': [250,350,300,300,350][i-1],
                  'lumberbase': [200,300,250,250,300][i-1], 'goldmod': 0, 'lumbermod': 0,
                  'timebase': 45, 'timemod': 0, 'requires1': 'h016' if i == 1 else 'h017',
                  'requires2': '', 'requires3': '', 'race': 'human', 'class': '',
                  'buttonpos': [1,0,1,2,2][i-1], 'buttonpos2': 1 if i == 1 else 2,
                  'hotkey1': ['P','L','B','W','I'][i-1]}
        for n in range(1, 5):
            values[f'effect{n}'] = ''
            values[f'base{n}'] = 0
            values[f'mod{n}'] = 0
        fields(stage, 'upgrade', code, values, operations)

    replacements = [('e000','A05U','ADr1','R02A','RDr1'),
                    ('h059','A05S','ADr2','R02O','RDr2'),
                    ('h01O','A04V','ADr3',None,'RDr3'),
                    ('h01R','A053','ADr4',None,'RDr4'),
                    ('n005','A062','ADr5',None,'RDr5')]
    for code, old, new, old_tech, tech in replacements:
        obj = run(stage, 'get-object', '--type', 'unit', '--id', code)['fields']
        abilities = [new if a == old else a for a in obj['abillist'].split(',')]
        if code == 'n005':
            abilities = [a for a in abilities if a != 'A064']
        if new not in abilities:
            raise RuntimeError(f'Expected original or replacement ability on {code}')
        upgrades = [a for a in obj.get('upgrades','').split(',') if a and a != old_tech]
        if tech not in upgrades:
            upgrades.append(tech)
        fields(stage, 'unit', code, {'abillist': ','.join(abilities), 'upgrades': ','.join(upgrades),
                                     'ubertip': UNIT_TIPS[code]}, operations)
    fields(stage, 'unit', 'h033', {'researches': 'R029,RDr1,R02B,R02C'}, operations)
    fields(stage, 'unit', 'h058', {'researches': 'R022,R02M,R02L,R02N,RDr2,RDr3,RDr4'}, operations)
    fields(stage, 'unit', 'h05A', {'researches': 'R02J,R02K,R02G,R02H,R02I,RDr5'}, operations)

    # Copy the original ward, retaining its model, sound, scale and fragile HP.
    clone(stage, 'unit', 'ohwd', 'nDr1')
    fields(stage, 'unit', 'nDr1', {'name': 'Идол памяти', 'editorsuffix': '(дренеи)',
                                 'abillist': 'ACmi', 'abilskinlist': '', 'upgrades': '',
                                 'ubertip': TIPS[4]}, operations)
    original_model = run(stage, 'get-object', '--type', 'unit', '--id', 'ohwd', '--fields', 'file')['fields']['file']
    assert run(stage, 'get-object', '--type', 'unit', '--id', 'nDr1', '--fields', 'file')['fields']['file'] == original_model

    # HiveWE normalizes old ability/skin fields on save. Keep that normalization
    # out of the published map: only new objects and explicit unit fields survive.
    original = OUT / 'current-original'
    original.mkdir(exist_ok=True)
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, original / name)
    preserve_stage(stage, original)
    # Verify every setter against the staged data before any live file is replaced.
    strings = {int(k): v.strip() for k, v in re.findall(r'STRING (\d+)[^{]*\{(.*?)\}',
               (stage / 'war3map.wts').read_text(encoding='utf-8-sig'), re.S)}
    for kind in ['ability','upgrade','unit']:
        relevant = [op for op in operations if op['type'] == kind]
        ids = sorted({op['id'] for op in relevant})
        columns = sorted({op['field'] for op in relevant})
        objects = run(stage, 'get-objects-bulk', '--type', kind, '--ids', ','.join(ids),
                      '--fields', ','.join(columns))['objects']
        actual = {x['id']: x['fields'] for x in objects}
        for op in relevant:
            value = actual[op['id']][op['field']]
            if value.startswith('TRIGSTR_'):
                value = strings[int(value[8:])]
            expected = str(op['value'])
            if value != expected:
                try:
                    assert float(value) == float(expected)
                except (ValueError, AssertionError):
                    raise AssertionError((op, value))
    register_imports(stage / 'war3map.imp', payload)
    for name, previous in hashes.items():
        if digest(MAP / name) != previous:
            raise RuntimeError(f'Concurrent change: {name}')
    for relative, data in payload.items():
        path = (MAP / relative).resolve()
        assert path.is_relative_to(MAP.resolve())
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
    changed = []
    for name in OBJECT_FILES:
        source = stage / name
        if source.exists() and digest(source) != hashes[name]:
            tmp = MAP / (name + '.draenei.tmp')
            shutil.copy2(source, tmp)
            os.replace(tmp, MAP / name)
            changed.append(name)
    report = {'source': 'WL - Bane Burrow v1.63.w3x', 'objects': operations,
              'assets': assets, 'before_hashes': hashes, 'changed_files': changed,
              'ward_model_preserved': original_model}
    (OUT / 'implementation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Published {len(operations)} verified fields; {len(payload)} assets; changed files: {changed}', flush=True)


if __name__ == '__main__':
    main()
