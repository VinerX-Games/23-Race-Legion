"""Лорд друид воргенов (H0J6): Семя Тал'дорена, Тропа корней, Проклятие Гоэмона, Полнолуние.

Object data. Использует узкую публикацию из implement_draenei_rework.py: HiveWE правит копию
карты, в живую карту попадают только новые объекты и у героя — список способностей и описание.
Старые способности A11L/A11M/A11N/A11O остаются в object data без изменений, герой их больше
не получает. Механики — Lua, WorgenDruid в races/Worgens.lua.
--dry-run печатает тексты, ничего не записывая.
"""
import json
import shutil
import sys

from implement_draenei_rework import MAP, ROOT, digest, run, clone, fields, preserve_unrelated
from implement_ogre_abilities import publish, verify

OUT = ROOT / '.cache/wc3/worgen-druid'
OBJECT_FILES = ['war3map.w3a', 'war3mapSkin.w3a', 'war3map.w3u', 'war3mapSkin.w3u',
                'war3map.w3h', 'war3mapSkin.w3h', 'war3map.wts']
NEW = {'.w3a': {'AWd1', 'AWd2', 'AWd3', 'AWd4', 'AWd5', 'AWd6'},
       '.w3h': {'BWd1', 'BWd2', 'BWd3'}, '.w3u': {'nWd1'}}
HERO = 'H0J6'
# Кроме стандартного набора узкой публикации у героя меняется список геройских способностей.
HERO_FIELDS = ('uabi', 'upgr', 'ures', 'utub', 'uhab')

TEXT, LABEL, NAME, NUM, BONUS, MINUS = 'ced4da', 'b99d66', 'ebc56c', 'ffffff', 'c8e087', 'ef8173'
BTN = 'ReplaceableTextures\\CommandButtons\\{}.blp'
SUFFIX = '(Воргены)'
SERVICE_SUFFIX = '(Воргены: служебное)'

# Числа должны совпадать с WorgenDruid в Worgens.lua.
SEED_HEAL = [120, 190, 260, 330]
SEED_COST, SEED_COOL, SEED_RANGE = [75, 80, 85, 90], [10, 9, 8, 7], 700
TRAIL_SPEED = [30, 35, 40, 45]
TRAIL_DAMAGE = [5, 8, 11, 14]
TRAIL_COST, TRAIL_COOL = [60, 65, 70, 75], [14, 13, 12, 11]
CURSE_COST, CURSE_COOL, CURSE_RANGE = [70, 65, 60, 55], [16, 14, 12, 10], [600, 650, 700, 750]
MOON_MISS, MOON_DUR, MOON_HERO_DUR = [40, 50], [20, 30], [4, 5]
MOON_HEAL, MOON_COST, MOON_COOL = [150, 250], [150, 200], [120, 100]


def c(color, text):
    return f'|cff{color}{text}|cff{TEXT}'


def n(text):
    return c(NUM, text)


def title(name):
    return f'|cff{NAME}{name}|r'


def ability_tip(body):
    return f'|cff{LABEL}СПОСОБНОСТЬ:|cff{TEXT} {body}|r'


def effect_tip(body):
    return f'|cff{LABEL}ЭФФЕКТ:|cff{TEXT} {body}|r'


def levels_list(lines):
    return '|n'.join(f'Уровень {i}: {line}' for i, line in enumerate(lines, 1))


def seed_body(heal=None):
    amount = f'{c(BONUS, heal)} ед. здоровья' if heal is not None else 'здоровье'
    return (f'Друид сажает семя в выбранной точке. За {n(3)} сек. семя вырастает и взрывается, '
            f'восстанавливая {amount} союзникам в радиусе {n(200)}.|n|nНе лечит здания.')


def trail_body(speed=None, damage=None):
    boost = f' на {c(BONUS, f"+{speed}%")}' if speed is not None else ''
    hit = f'по {n(damage)} урона' if damage is not None else 'урон'
    return (f'На {n(3)} сек. ускоряет передвижение друида{boost}. Каждые {n("0.5")} сек. '
            f'за ним вырастают колючие лозы: {n(5)} сек. они наносят {hit} раз в {n("0.5")} сек. '
            f'наземным врагам в радиусе {n(120)}.|n|n'
            f'Лозы одной тропы ранят каждого врага не чаще раза в {n("0.5")} сек.')


CURSE_BODY = (f'Метит вражеского юнита на {n(10)} сек. Цель атакует на {c(MINUS, "30%")} быстрее, '
              f'но получает на {c(BONUS, "50%")} больше урона из любых источников.|n|n'
              f'Если цель погибает под меткой, метка с полной длительностью переходит '
              f'на ближайшего вражеского юнита в радиусе {n(300)}.|n|n'
              f'Не действует на героев, механизмы и здания.')


def moon_body(level=None):
    if level is None:
        return (f'Враги в радиусе {n(1200)} начинают промахиваться при атаке, союзники в том же '
                f'радиусе, включая друида, восстанавливают здоровье.|n|n'
                f'Не действует на механизмы и здания.')
    i = level - 1
    return (f'Враги в радиусе {n(1200)} промахиваются при атаке с вероятностью '
            f'{c(BONUS, f"{MOON_MISS[i]}%")} в течение {n(MOON_DUR[i])} сек., герои — '
            f'{n(MOON_HERO_DUR[i])} сек. Союзники в том же радиусе, включая друида, восстанавливают '
            f'{c(BONUS, MOON_HEAL[i])} ед. здоровья.|n|nНе действует на механизмы и здания.')


ABILITIES = [
    # code, base, name, icon, hotkey, column, levels, reqlevel
    ('AWd1', 'ANcl', "Семя Тал'дорена", 'BTNTalDorenSeed', 'Q', 0, 4, 1),
    ('AWd2', 'Absk', 'Тропа корней', 'BTNRootTrail', 'W', 1, 4, 1),
    ('AWd3', 'ANcl', 'Проклятие Гоэмона', 'BTNGoemonCurse', 'E', 2, 4, 1),
    ('AWd4', 'ANcl', 'Полнолуние', 'BTNFullMoon', 'R', 3, 2, 6),
]

RESEARCH_TIPS = {
    'AWd1': ability_tip(seed_body() + '|n|n' + levels_list(
        [f'{c(BONUS, h)} ед. здоровья.' for h in SEED_HEAL])),
    'AWd2': ability_tip(trail_body() + '|n|n' + levels_list(
        [f'скорость {c(BONUS, f"+{s}%")}, урон лоз {n(d)}.'
         for s, d in zip(TRAIL_SPEED, TRAIL_DAMAGE)])),
    'AWd3': ability_tip(CURSE_BODY + '|n|n' + levels_list(
        [f'дальность {n(r)}, восстановление {n(cd)} сек.'
         for r, cd in zip(CURSE_RANGE, CURSE_COOL)])),
    'AWd4': ability_tip(moon_body() + '|n|n' + levels_list(
        [f'промах {c(BONUS, f"{m}%")} на {n(d)} сек. (герои — {n(hd)} сек.), '
         f'лечение {c(BONUS, h)}.'
         for m, d, hd, h in zip(MOON_MISS, MOON_DUR, MOON_HERO_DUR, MOON_HEAL)])),
}


def level_tip(code, level):
    i = level - 1
    return {
        'AWd1': lambda: ability_tip(seed_body(SEED_HEAL[i])),
        'AWd2': lambda: ability_tip(trail_body(TRAIL_SPEED[i], TRAIL_DAMAGE[i])),
        'AWd3': lambda: ability_tip(CURSE_BODY),
        'AWd4': lambda: ability_tip(moon_body(level)),
    }[code]()


HERO_TIP = (f'|cff{LABEL}ГЕРОЙ:|cff{TEXT} Друид Тал\'дорена, обративший силу природы и проклятие '
            f'воргенов против врагов. Лечит союзников и изматывает вражеские отряды.|n|n'
            f'|cff{LABEL}Способности:|cff{TEXT}|n'
            f'- {c(NAME, "Семя Тал\'дорена")}: вырастает за {n(3)} сек. и взрывается, '
            f'исцеляя союзников рядом.|n'
            f'- {c(NAME, "Тропа корней")}: ускоряет друида и оставляет за ним колючие лозы.|n'
            f'- {c(NAME, "Проклятие Гоэмона")}: цель атакует быстрее, но получает больше урона; '
            f'после её смерти метка переходит на соседа.|n'
            f'- {c(NAME, "Полнолуние")}: враги вокруг промахиваются, союзники исцеляются.|n|n'
            f'Атакует наземные цели.|r')

TRAIL_BUFF = effect_tip('Скорость передвижения повышена. За юнитом вырастают колючие лозы.')
CURSE_BUFF = effect_tip(f'Юнит атакует быстрее, но {c(MINUS, "получает больше урона")}. '
                        f'Если он погибнет, проклятие перейдёт на соседнего юнита.')
MOON_BUFF = effect_tip(f'Юнит {c(MINUS, "может промахнуться")} при атаке.')
SERVICE = ability_tip('Служебная способность для Lua-механик Лорда друида.')
CURSE_TARGETS = 'air,ground,enemy,nonhero,organic,neutral,vulnerable'


def common(code, name, icon, hotkey, column, levels, reqlevel):
    values = {'name': title(name), 'editorsuffix': SUFFIX, 'hero': 1, 'item': 0, 'race': 'human',
              'levels': levels, 'reqlevel': reqlevel, 'levelskip': 0,
              'art': BTN.format(icon), 'researchart': BTN.format(icon),
              'buttonpos': column, 'buttonpos2': 2, 'researchbuttonpos': column,
              'researchbuttonpos2': 0, 'hotkey': hotkey, 'researchhotkey': hotkey,
              'researchtip': title(name), 'researchubertip': RESEARCH_TIPS[code]}
    for level in range(1, levels + 1):
        values[f'tip{level}'] = title(f'{name} — уровень {level}')
        values[f'ubertip{level}'] = level_tip(code, level)
    return values


def channel(values, levels, target_type, options, order, art=''):
    """Channel без своих эффектов: вся механика в Lua по событию SPELL_EFFECT."""
    values.update({'casterart': art, 'effectart': '', 'targetart': '', 'specialart': ''})
    for level in range(1, levels + 1):
        values.update({f'dataa{level}': 0, f'datab{level}': target_type,
                       f'datac{level}': options, f'datad{level}': 0, f'datae{level}': 0,
                       f'dataf{level}': order, f'cast{level}': 0, f'dur{level}': 0,
                       f'herodur{level}': 0})


def objects(stage, operations):
    for code, base, name, icon, hotkey, column, levels, reqlevel in ABILITIES:
        clone(stage, 'ability', base, code)
        values = common(code, name, icon, hotkey, column, levels, reqlevel)
        if code == 'AWd1':
            # Опции 1+2: кнопка видна, при выборе точки показан круг радиуса area.
            channel(values, levels, 2, 3, 'channel')
            for level in range(1, levels + 1):
                values.update({f'area{level}': 200, f'rng{level}': SEED_RANGE,
                               f'cost{level}': SEED_COST[level - 1],
                               f'cool{level}': SEED_COOL[level - 1]})
        elif code == 'AWd2':
            # Берсерк требует ванильное Robk, которое живому игроку не выдаётся.
            values.update({'buffid1': 'BWd1', 'requires': ''})
            for level in range(1, levels + 1):
                values.update({f'dataa{level}': TRAIL_SPEED[level - 1] / 100, f'datab{level}': 0,
                               f'datac{level}': 0, f'dur{level}': 3, f'herodur{level}': 3,
                               f'cost{level}': TRAIL_COST[level - 1],
                               f'cool{level}': TRAIL_COOL[level - 1],
                               f'buffid{level}': 'BWd1'})
        elif code == 'AWd3':
            channel(values, levels, 1, 1, 'curse')
            for level in range(1, levels + 1):
                values.update({f'targs{level}': CURSE_TARGETS, f'rng{level}': CURSE_RANGE[level - 1],
                               f'cost{level}': CURSE_COST[level - 1],
                               f'cool{level}': CURSE_COOL[level - 1]})
        else:
            channel(values, levels, 0, 1, 'starfall',
                    'Abilities\\Spells\\NightElf\\Starfall\\StarfallCaster.mdl')
            for level in range(1, levels + 1):
                values.update({f'area{level}': 1200, f'cost{level}': MOON_COST[level - 1],
                               f'cool{level}': MOON_COOL[level - 1]})
        fields(stage, 'ability', code, values, operations)

    clone(stage, 'buff', 'Bbsk', 'BWd1')
    fields(stage, 'buff', 'BWd1', {
        'bufftip': title('Тропа корней'), 'editorsuffix': SUFFIX, 'buffart': BTN.format('BTNRootTrail'),
        'buffubertip': TRAIL_BUFF, 'race': 'human',
        'targetart': 'Abilities\\Spells\\NightElf\\Rejuvenation\\RejuvenationTarget.mdl',
        'targetattach': 'origin', 'targetattachcount': 1}, operations)
    clone(stage, 'buff', 'Bblo', 'BWd2')
    fields(stage, 'buff', 'BWd2', {
        'bufftip': title('Проклятие Гоэмона'), 'editorsuffix': SUFFIX,
        'buffart': BTN.format('BTNGoemonCurse'), 'buffubertip': CURSE_BUFF, 'race': 'human',
        'targetart': 'Abilities\\Weapons\\DruidoftheTalonMissile\\DruidoftheTalonMissile.mdl',
        'targetattach': 'head', 'targetattachcount': 1}, operations)
    clone(stage, 'buff', 'Bcrs', 'BWd3')
    fields(stage, 'buff', 'BWd3', {
        'bufftip': title('Полнолуние'), 'editorsuffix': SUFFIX,
        'buffart': BTN.format('BTNFullMoon'), 'buffubertip': MOON_BUFF, 'race': 'human'},
        operations)

    # Метка Проклятия Гоэмона: и первое наложение, и перескок кастует даммик.
    clone(stage, 'ability', 'Ablo', 'AWd5')
    fields(stage, 'ability', 'AWd5', {
        'name': title('Проклятие Гоэмона'), 'editorsuffix': SERVICE_SUFFIX,
        'art': BTN.format('BTNGoemonCurse'), 'hero': 0, 'item': 0, 'race': 'human', 'levels': 1,
        'tip1': title('Проклятие Гоэмона'), 'ubertip1': SERVICE, 'dataa1': 0.3, 'datab1': 0,
        'datac1': 0, 'dur1': 10, 'herodur1': 10, 'rng1': 1500, 'cool1': 0, 'cost1': 0,
        'buffid1': 'BWd2', 'targs1': CURSE_TARGETS}, operations)
    clone(stage, 'ability', 'Acrs', 'AWd6')
    values = {'name': title('Полнолуние'), 'editorsuffix': SERVICE_SUFFIX,
              'art': BTN.format('BTNFullMoon'), 'hero': 0, 'item': 0, 'race': 'human',
              'levels': 2}
    for level in (1, 2):
        values.update({f'tip{level}': title('Полнолуние'), f'ubertip{level}': SERVICE,
                       f'dataa{level}': MOON_MISS[level - 1] / 100,
                       f'dur{level}': MOON_DUR[level - 1], f'herodur{level}': MOON_HERO_DUR[level - 1],
                       f'rng{level}': 1500, f'cool{level}': 0, f'cost{level}': 0,
                       f'buffid{level}': 'BWd3', f'targs{level}': 'air,ground,enemy,organic,neutral'})
    fields(stage, 'ability', 'AWd6', values, operations)

    # Копия даммика огров: нулевая точка каста, неуязвим, без модели.
    clone(stage, 'unit', 'nOg1', 'nWd1')
    fields(stage, 'unit', 'nWd1', {
        'name': title('Заклинатель друида'), 'editorsuffix': SERVICE_SUFFIX,
        'tip': title('Заклинатель друида'), 'abillist': 'Aloc,Avul,AWd5,AWd6', 'abilskinlist': '',
        'ubertip': f'|cff{LABEL}ЮНИТ:|cff{TEXT} Служебный источник способностей Лорда друида. '
                   f'Не атакует.|r'}, operations)

    fields(stage, 'unit', HERO, {'heroabillist': 'AWd1,AWd2,AWd3,AWd4', 'ubertip': HERO_TIP},
           operations)


def main():
    if '--dry-run' in sys.argv:
        for code, *_ in ABILITIES:
            print(code, RESEARCH_TIPS[code], '\n')
        print(HERO_TIP)
        return
    OUT.mkdir(parents=True, exist_ok=True)
    stage, original = OUT / 'stage', OUT / 'current-original'
    for path in (stage, original):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir()
    hashes = {name: digest(MAP / name) for name in OBJECT_FILES}
    for name in OBJECT_FILES:
        if (MAP / name).exists():
            shutil.copy2(MAP / name, stage / name)
            shutil.copy2(MAP / name, original / name)

    operations = []
    objects(stage, operations)
    for name in OBJECT_FILES:
        suffix = '.' + name.rsplit('.', 1)[-1]
        if suffix in NEW and (original / name).exists():
            preserve_unrelated(original / name, stage / name, NEW[suffix],
                               {HERO} if suffix == '.w3u' else set(), HERO_FIELDS)
    verify(stage, operations)
    changed = publish(stage, hashes, OBJECT_FILES)
    report = {'objects': operations, 'before_hashes': hashes, 'changed_files': changed}
    (OUT / 'implementation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2),
                                             encoding='utf-8')
    print(f'Published {len(operations)} verified fields; changed: {changed}')


if __name__ == '__main__':
    main()
