"""Новые механики юнитов: Мутация и Гарпун (наги), Пьянящая настойка (пандарены),
Память Аргуса (Сломленные дренеи) и новые иконки улучшений оружия/брони дренеев.

Object data и иконки. Использует узкую публикацию из implement_draenei_rework.py: HiveWE
правит копию карты, в живую карту попадают только новые объекты и явно изменённые поля
существующих объектов (список кодов полей — EDITED).
--dry-run печатает новые описания юнитов и зданий, ничего не записывая.
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

from implement_draenei_rework import MAP, digest, run, clone, fields, register_imports, object_records
from wc3_icons import icon_set

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'Assets'
OUT = ROOT / '.cache/wc3/unit-mechanics'
OBJECT_FILES = ['war3map.w3a', 'war3mapSkin.w3a', 'war3map.w3q', 'war3mapSkin.w3q',
                'war3map.w3u', 'war3mapSkin.w3u', 'war3map.w3h', 'war3mapSkin.w3h',
                'war3map.wts', 'war3map.imp']
NEW = {'.w3a': {'AMu1', 'AMu2', 'AMu3', 'AMu4', 'AMh1', 'APb1', 'APb2', 'ADr6'},
       '.w3q': {'RDr6'}, '.w3h': {'BPb1'}}
# Существующие объекты и коды полей, которые скрипт имеет право менять.
UNIT_FIELDS = {'uabi', 'upgr', 'ures', 'utub'}
EDITED = {
    '.w3u': {code: UNIT_FIELDS for code in ['n050', 'n056', 'pa22', 'h05D', 'h05E', 'n005', 'h05A', 'n055']},
    '.w3a': {'PA68': {'abpx', 'abpy'}},
    '.w3q': {'R0FP': {'gnam', 'gtp1', 'gub1', 'gar1'},
             'R023': {'gar1'}, 'R024': {'gar1'}, 'R02P': {'gar1'}},
}

# Нарисованные иконки: BTN/PAS и их неактивные варианты создаёт wc3_icons.icon_set.
ICONS = {'NagaMutation': 'MurlocSpell.png', 'NagaHarpoon': 'MurlocSpell2.png',
         'PandarenBarrel': 'PandarenSpell.png', 'DraeneiArgusMemory': 'DraeneiSpell1.jpg'}
BTN = 'ReplaceableTextures\\CommandButtons\\BTN{}.blp'
PAS = 'ReplaceableTextures\\PassiveButtons\\PASBTN{}.blp'
# Готовые BLP пользователя: исследование -> базовое имя иконки, уровни 1-2/3-4/5-6 -> Upg1/2/3.
UPGRADE_ICONS = {'R024': 'DraeneiArmorUpg', 'R023': 'LightHammerUpg', 'R02P': 'LightBowUpg'}

TEXT, LABEL, NAME, NUM, BONUS, MALUS = 'ced4da', 'b99d66', 'ebc56c', 'ffffff', 'c8e087', 'ef8173'
BROKEN = ['h05D', 'h05E', 'n005']


def c(color, text):
    return f'|cff{color}{text}|cff{TEXT}'


def title(name):
    return f'|cff{NAME}{name}|r'


def tip(label, body):
    return f'|cff{LABEL}{label}:|cff{TEXT} {body}|r'


MUTATIONS = [
    ('AMu2', 'клешни', f'Мутировавшие клешни увеличивают урон атаки на {c(BONUS, "+8")}.'),
    ('AMu3', 'панцирь', f'Мутировавший панцирь увеличивает броню на {c(BONUS, "+3")}.'),
    ('AMu4', 'жабры', f'Жабры восстанавливают {c(BONUS, "8")} ед. здоровья в секунду, '
                      f'пока мурлок находится в воде.'),
]
MUTATION_BODY = (f'При появлении мурлок получает одну случайную мутацию:|n'
                 f'- {c(NAME, "Клешни")}: {c(BONUS, "+8")} к урону атаки.|n'
                 f'- {c(NAME, "Панцирь")}: {c(BONUS, "+3")} к броне.|n'
                 f'- {c(NAME, "Жабры")}: {c(BONUS, "8")} ед. здоровья в секунду в воде.')
HARPOON_BODY = (f'Бросает гарпун во вражеского наземного юнита: наносит {c(NUM, "40")} урона и '
                f'притягивает цель на {c(NUM, "300")} к охотнику. Героя притягивает лишь на '
                f'{c(NUM, "150")}.|n|nНе действует на здания и воздушные цели. Непроходимая '
                f'местность прерывает притягивание.')
BARREL_BODY = (f'Бросает во врага бочку хмельной настойки. Поражённая цель промахивается при атаке '
               f'с вероятностью {c(NUM, "25%")} в течение {c(NUM, "15")} сек., герой — '
               f'{c(NUM, "3")} сек.|n|nПрименяется автоматически. Не действует на механизмы и '
               f'невосприимчивых к магии.')
ARGUS_BODY = (f'При гибели Сломленного с вероятностью {c(NUM, "15%")} на его месте встаёт дух '
              f'этого же воина и сражается {c(NUM, "5")} сек.|n|nДух — призванный юнит: его можно '
              f'рассеять. Дух не порождает новых духов.')

RESEARCH_HARPOON = tip('ИССЛЕДОВАНИЕ', f'Обучает Морских охотников способности {c(NAME, "Гарпун")}: '
                       f'бросок наносит {c(NUM, "40")} урона и притягивает врага на {c(NUM, "300")} '
                       f'(героя — на {c(NUM, "150")}).|n|n|cff{LABEL}Применяется к:|cff{TEXT}|n'
                       f'- {c(NAME, "Морской охотник")}.')
RESEARCH_ARGUS = tip('ИССЛЕДОВАНИЕ', f'Павший Сломленный с вероятностью {c(NUM, "15%")} возвращается '
                     f'духом на {c(NUM, "5")} сек. и продолжает сражаться. Дух можно рассеять.'
                     f'|n|n|cff{LABEL}Применяется к:|cff{TEXT}|n- {c(NAME, "Сломленный страж")}.|n'
                     f'- {c(NAME, "Сломленный мастер")}.|n- {c(NAME, "Сломленный провидец")}.')

BULLET_MUTATION = (f'- {c(NAME, "Мутация")}: при появлении случайно получает клешни ({c(BONUS, "+8")} '
                   f'к урону), панцирь ({c(BONUS, "+3")} к броне) или жабры ({c(BONUS, "8")} HP/сек. '
                   f'в воде).')
BULLET_HARPOON = (f'- {c(NAME, "Гарпун")}: наносит {c(NUM, "40")} урона и притягивает врага на '
                  f'{c(NUM, "300")}, героя — на {c(NUM, "150")} (требует исследования).')
BULLET_BARREL = (f'- {c(NAME, "Пьянящая настойка")}: бочка заставляет цель промахиваться '
                 f'({c(NUM, "25%")}) {c(NUM, "15")} сек., героя — {c(NUM, "3")} сек.; '
                 f'применяется автоматически.')
BULLET_ARGUS = (f'- {c(NAME, "Память Аргуса")}: при гибели с вероятностью {c(NUM, "15%")} встаёт '
                f'духом на {c(NUM, "5")} сек. (требует исследования).')
SEER_TIP = tip('ЮНИТ', f'Шаман Сломленных дальнего боя. Защищает союзников молниями и лечит '
               f'собственный отряд.|n|n|cff{LABEL}Способности:|cff{TEXT}|n'
               f'- {c(NAME, "Щит молний")}: молнии вокруг цели наносят урон находящимся рядом войскам.|n'
               f'- {c(NAME, "Поле слома")}: снижает скорость дальнобойной атаки врагов в области.|n'
               f'- {c(NAME, "Идол памяти")}: лечит собственный отряд и ускоряет восстановление '
               f'{c(NAME, "Призматических наконечников")} и {c(NAME, "Озарённого клинка")} '
               f'(требует исследования).|n'
               f'- {c(NAME, "Ускользание")}: даёт шанс уклониться от вражеской атаки.|n'
               f'- {c(NAME, "Спасение в тени")}: при гибели может возродиться у логова Сломленных.|n'
               f'{BULLET_ARGUS}|n|nАтакует наземные и воздушные цели.')


def replace_once(text, old, new, code):
    assert text.count(old) == 1, (code, old, text)
    return text.replace(old, new)


def unit_tip(code, text):
    if code == 'n050':
        text = replace_once(text, 'Поедает трупы для регенерации и уклоняется от ударов.',
                            'Поедает трупы для регенерации, а при появлении получает случайную мутацию.', code)
        return replace_once(text, f'- {c(NAME, "Уклонение")}: даёт шанс избежать вражеской атаки.',
                            BULLET_MUTATION, code)
    if code == 'n056':
        text = replace_once(text, 'Наносит оглушающие удары и усиливает',
                            'Притягивает врагов гарпуном и усиливает', code)
        return replace_once(text, f'- {c(NAME, "Сокрушение")}: даёт шанс нанести дополнительный урон '
                                  f'и оглушить противника.', BULLET_HARPOON, code)
    if code == 'pa22':
        anchor = 'вызывая промахи и замедление.'
        return replace_once(text, anchor, anchor + '|n' + BULLET_BARREL, code)
    if code in ('h05D', 'h05E'):
        anchor = f'|n|n|cff{LABEL}Цели атаки:'
        return replace_once(text, anchor, '|n' + BULLET_ARGUS + anchor, code)
    if code == 'n005':
        return SEER_TIP
    if code == 'n055':
        return replace_once(text, c(NAME, 'Сокрушительный удар') + '.', c(NAME, 'Гарпун') + '.', code)
    if code == 'h05A':
        head, sep, tail = text.partition(f'|cff{LABEL}Исследования:|cff{TEXT}')
        assert sep, (code, text)
        names = re.findall(r'\|cffebc56c([^|]+)\|cffced4da', tail)
        assert names[-1] == 'Отравленное оружие', (code, names)
        names += ['Память предков', 'Память Аргуса']
        return head + sep + ''.join(f'|n- {c(NAME, n)}.' for n in names) + '|r'
    raise KeyError(code)


def passive(stage, code, name, icon, body, pos, requires, race, operations):
    clone(stage, 'ability', 'AOcr', code)
    fields(stage, 'ability', code, {
        'name': title(name), 'editorsuffix': f'({race})', 'art': PAS.format(icon),
        'hero': 0, 'item': 0, 'race': {'наги': 'naga', 'ночнорождённые': 'nightelf'}.get(race, 'human'), 'levels': 1,
        'reqlevel': 0, 'requires': requires, 'checkdep': 1 if requires else 0,
        'buttonpos': pos[0], 'buttonpos2': pos[1], 'hotkey': '',
        'tip1': title(name), 'ubertip1': tip('СПОСОБНОСТЬ', body),
        'dataa1': 0, 'datab1': 1, 'datac1': 0, 'datad1': 0}, operations)


def objects(stage, operations):
    passive(stage, 'AMu1', 'Мутация', 'NagaMutation', MUTATION_BODY, (2, 2), '', 'наги', operations)
    for code, kind, body in MUTATIONS:
        passive(stage, code, f'Мутация: {kind}', 'NagaMutation',
                f'{body}|n|nМутация выпадает случайно при появлении мурлока.', (2, 2), '', 'наги',
                operations)

    # ADr5 — чистый клон Канала без эффектов DeathPact; приказ свой, чтобы не делить
    # его с «Своей стихией» (A1LT, blight) на том же юните.
    clone(stage, 'ability', 'ADr5', 'AMh1')
    fields(stage, 'ability', 'AMh1', {
        'name': title('Гарпун'), 'editorsuffix': '(наги)', 'art': BTN.format('NagaHarpoon'),
        'hero': 0, 'item': 0, 'race': 'naga', 'levels': 1, 'reqlevel': 0,
        'requires': 'R0FP', 'checkdep': 1, 'buttonpos': 1, 'buttonpos2': 2, 'hotkey': 'X',
        'tip1': title('Гарпун'), 'ubertip1': tip('СПОСОБНОСТЬ', HARPOON_BODY),
        'animnames': 'attack', 'dataa1': 0, 'datab1': 1, 'datac1': 1, 'datad1': 0, 'datae1': 0,
        'dataf1': 'acidbomb', 'rng1': 500, 'cool1': 12, 'cost1': 0, 'cast1': 0,
        'targs1': 'ground,enemy,neutral,vulnerable'}, operations)
    fields(stage, 'upgrade', 'R0FP', {
        'name1': title('Гарпун'), 'tip1': title('Гарпун'), 'ubertip1': RESEARCH_HARPOON,
        'art1': BTN.format('NagaHarpoon')}, operations)

    clone(stage, 'buff', 'Bcrs', 'BPb1')
    fields(stage, 'buff', 'BPb1', {
        'bufftip': title('Пьянящая настойка'), 'editorsuffix': '(пандарены)',
        'buffart': BTN.format('PandarenBarrel'),
        'targetart': 'Abilities\\Spells\\Other\\StrongDrink\\BrewmasterTarget.mdl',
        'buffubertip': tip('ЭФФЕКТ', f'Юнит пьян и {c(MALUS, "промахивается при атаке")} '
                                     f'с вероятностью {c(NUM, "25%")}.')}, operations)
    # APb1 выбирает цель автокастом; короткий баф без промахов держится, пока летит бочка.
    clone(stage, 'ability', 'Acrs', 'APb1')
    fields(stage, 'ability', 'APb1', {
        'name': title('Пьянящая настойка'), 'editorsuffix': '(пандарены)',
        'art': BTN.format('PandarenBarrel'), 'unart': BTN.format('PandarenBarrel'),
        'hero': 0, 'item': 0, 'race': 'human', 'levels': 1, 'reqlevel': 0,
        'buttonpos': 3, 'buttonpos2': 2, 'unbuttonpos': 3, 'unbuttonpos2': 2,
        'hotkey': 'V', 'unhotkey': 'V', 'tip1': title('Пьянящая настойка'),
        'ubertip1': tip('СПОСОБНОСТЬ', BARREL_BODY),
        'dataa1': 0, 'dur1': 2, 'herodur1': 2, 'cool1': 10, 'cost1': 25, 'rng1': 600,
        'buffid1': 'BPb1'}, operations)
    clone(stage, 'ability', 'Acrs', 'APb2')
    fields(stage, 'ability', 'APb2', {
        'name': title('Пьянящая настойка'), 'editorsuffix': '(пандарены: служебное)',
        'art': BTN.format('PandarenBarrel'), 'hero': 0, 'item': 0, 'race': 'human', 'levels': 1,
        'tip1': title('Пьянящая настойка'),
        'ubertip1': tip('СПОСОБНОСТЬ', 'Служебная способность: эффект бочки хмелевара.'),
        'dataa1': 0.25, 'dur1': 15, 'herodur1': 3, 'cool1': 0, 'cost1': 0, 'rng1': 99999,
        'buffid1': 'BPb1'}, operations)
    # Две способности с кнопкой (2,2) у хмелевара: пассивку баланса переносим на свободное место.
    fields(stage, 'ability', 'PA68', {'buttonpos': 3, 'buttonpos2': 1}, operations)

    passive(stage, 'ADr6', 'Память Аргуса', 'DraeneiArgusMemory', ARGUS_BODY, (3, 1), 'RDr6',
            'дренеи', operations)
    # У R0GU нет класса, эффектов и базового требования ostr (см. implement_ogre_abilities.py).
    clone(stage, 'upgrade', 'R0GU', 'RDr6')
    fields(stage, 'upgrade', 'RDr6', {
        'name1': title('Память Аргуса'), 'editorsuffix1': '(дренеи)',
        'art1': BTN.format('DraeneiArgusMemory'), 'tip1': title('Память Аргуса'),
        'ubertip1': RESEARCH_ARGUS, 'maxlevel': 1, 'goldbase': 350, 'lumberbase': 300,
        'timebase': 50, 'requires1': 'h017', 'race': 'human', 'buttonpos': 3, 'buttonpos2': 0,
        'hotkey1': 'R'}, operations)

    for code, icon in UPGRADE_ICONS.items():
        fields(stage, 'upgrade', code, {f'art{level}': BTN.format(f'{icon}{(level + 1) // 2}')
                                        for level in range(1, 7)}, operations)


def resolve(stage, kind, ids, column):
    strings = {int(k): v.strip() for k, v in re.findall(
        r'STRING (\d+)[^{]*\{(.*?)\}', (stage / 'war3map.wts').read_text(encoding='utf-8-sig'), re.S)}
    objects_ = run(stage, 'get-objects-bulk', '--type', kind, '--ids', ','.join(ids),
                   '--fields', column)['objects']
    result = {}
    for obj in objects_:
        value = obj['fields'][column]
        if value.startswith('TRIGSTR_'):
            value = strings[int(value[8:])]
        result[obj['id']] = value
    return result


def units(stage, operations, dry_run=False):
    ids = list(EDITED['.w3u'])
    tips = resolve(stage, 'unit', ids, 'ubertip')
    current = {o['id']: o['fields'] for o in run(
        stage, 'get-objects-bulk', '--type', 'unit', '--ids', ','.join(ids),
        '--fields', 'abillist,upgrades,researches')['objects']}

    def listed(code, column):
        return [x for x in current[code][column].split(',') if x]

    changes = {code: {'ubertip': unit_tip(code, tips[code])} for code in ids}
    for code, old, new in [('n050', 'A14K', 'AMu1'), ('n056', 'ACpv', 'AMh1')]:
        abilities = listed(code, 'abillist')
        abilities[abilities.index(old)] = new
        changes[code]['abillist'] = ','.join(abilities)
    changes['pa22']['abillist'] = ','.join(listed('pa22', 'abillist') + ['APb1'])
    for code in BROKEN:
        changes[code]['abillist'] = ','.join(listed(code, 'abillist') + ['ADr6'])
        changes[code]['upgrades'] = ','.join(listed(code, 'upgrades') + ['RDr6'])
    changes['h05A']['researches'] = ','.join(listed('h05A', 'researches') + ['RDr6'])
    if dry_run:
        for code, values in changes.items():
            print(code, json.dumps(values, ensure_ascii=False), '\n')
        return
    for code, values in changes.items():
        fields(stage, 'unit', code, values, operations)


def preserve(original_path, edited_path, new_ids, edited):
    """Существующие записи — байт в байт; у EDITED-объектов заменяются только разрешённые поля."""
    extended = original_path.suffix in ('.w3a', '.w3q')
    version, before = object_records(original_path.read_bytes(), extended)
    _, after = object_records(edited_path.read_bytes(), extended)
    lookup = {x['id']: x for table in after for x in table}
    output = bytearray(struct.pack('<I', version))
    for index, table in enumerate(before):
        result = []
        for record in table:
            if record['id'] in new_ids:
                result.append(lookup[record['id']]['raw'])
            elif record['id'] in edited:
                old = dict(record['mods'])
                changed = {key: raw for key, raw in lookup[record['id']]['mods'] if old.get(key) != raw}
                # HiveWE при сохранении нормализует и чужие поля записи (выносит строки в WTS,
                # переносит поля между таблицами) — такие изменения отбрасываются.
                ignored = sorted({key[0] for key in changed} - edited[record['id']])
                if ignored:
                    print(f'{original_path.name} {record["id"]}: ignored HiveWE changes {ignored}')
                changed = {key: raw for key, raw in changed.items() if key[0] in edited[record['id']]}
                mods = [(key, changed.pop(key, raw)) for key, raw in record['mods']]
                mods += list(changed.items())
                result.append(record['header'] + struct.pack('<I', len(mods))
                              + b''.join(raw for _, raw in mods))
            else:
                result.append(record['raw'])
        known = {x['id'] for x in table}
        result += [x['raw'] for x in after[index] if x['id'] in new_ids and x['id'] not in known]
        output += struct.pack('<I', len(result)) + b''.join(result)
    edited_path.write_bytes(output)


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


def publish(stage, hashes):
    for name, previous in hashes.items():
        if digest(MAP / name) != previous:
            raise RuntimeError(f'Concurrent change: {name}')
    changed = []
    for name in OBJECT_FILES:
        source = stage / name
        if source.exists() and digest(source) != hashes[name]:
            tmp = MAP / (name + '.mechanics.tmp')
            shutil.copy2(source, tmp)
            os.replace(tmp, MAP / name)
            changed.append(name)
    return changed


def assets():
    payload, report = {}, []

    def add(relative, data, source):
        target = MAP / relative
        if target.exists() and target.read_bytes() != data:
            raise RuntimeError(f'Asset conflict: {relative}')
        payload[relative] = data
        report.append({'source': source, 'path': relative, 'sha256': hashlib.sha256(data).hexdigest()})

    with tempfile.TemporaryDirectory() as tmp:
        for name, source in ICONS.items():
            for relative in icon_set(ASSETS / source, name, tmp):
                add(relative, (Path(tmp) / relative).read_bytes(), source)
    for icon in UPGRADE_ICONS.values():
        for tier in (1, 2, 3):
            for prefix, folder in [('BTN', 'CommandButtons'), ('DISBTN', 'CommandButtonsDisabled')]:
                source = f'{prefix}{icon}{tier}.blp'
                data = (ASSETS / source).read_bytes()
                assert data[:4] in (b'BLP1', b'BLP2'), source
                add(f'ReplaceableTextures/{folder}/{source}', data, source)
    return payload, report


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

    payload, report = assets()
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
        path = (MAP / relative).resolve()
        assert path.is_relative_to(MAP.resolve())
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
    (OUT / 'implementation.json').write_text(json.dumps(
        {'objects': operations, 'assets': report, 'before_hashes': hashes, 'changed_files': changed},
        ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Published {len(operations)} verified fields; {len(payload)} assets; changed: {changed}')


if __name__ == '__main__':
    main()
