"""Import four Exodar buildings and adjust the Draenei seer's command card.

HiveWE edits a private stage; only the requested raw fields are merged back.
Unused old assets are backed up before removal, with reference evidence saved.
"""
import hashlib
import json
import math
import os
import shutil
import struct
from pathlib import Path

from implement_draenei_rework import object_records, register_imports, run, fields, textures
from implement_draenei_rework import UNIT_TIPS
from wc3_hivewe import load_wts_strings


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / 'map.w3x'
DONOR = ROOT / '.cache/wc3/bane-burrow'
OUT = ROOT / '.cache/wc3/draenei-buildings'
BUILDINGS = [
    ('h057', 'h053', 'Altar', 'Exodar Draenei - DraeneiAltar.mdx', 'BTNExodar Draenei - Altar New.blp', 1.0),
    ('h055', 'h057', 'Workshop', 'Exodar Draenei - DraeneiWorkshopV1.mdx', 'BTNExodar Draenei - Workshop New.blp', 0.65),
    ('h056', 'h058', 'ArcaneCluster', 'Exodar Draenei - DraeneiTemple.mdx', 'BTNExodar Draenei - Hall New.blp', 0.75),
    ('h033', 'h055', 'Barracks', 'Exodar Draenei - DraeneiBarracks.mdx', 'BTNExodar Draenei - Casern New.blp', 1.0),
]
BUILDING_NAMES = {
    'h033': ('Казармы Аргуса', 'Обучает рангари, лазутчиков и всадников на элекках. '
             'Здесь исследуются Призматические наконечники и другие воинские навыки дренеев.'),
    'h057': ('Алтарь Наару', 'Призывает и воскрешает героев дренеев.'),
}
SEER_TIP = ('Сломленный провидец дальнего боя. Сохраняет Щит молний, Поле слома и способности '
            'Сломленных. После исследования Памяти предков создаёт Идол памяти (E): лечит '
            'собственный отряд и ускоряет восстановление Призматических наконечников и Озарённого клинка.')
FILES = ['war3map.w3u', 'war3mapSkin.w3u', 'war3map.w3a', 'war3mapSkin.w3a', 'war3map.wts', 'war3map.imp']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def merge_fields(original, stage, kind, allowed):
    names = [f'war3map.w3{kind}', f'war3mapSkin.w3{kind}']
    extended = kind == 'a'
    strings = load_wts_strings(stage / 'war3map.wts')
    wanted = {}
    for name in names:
        _, tables = object_records((stage / name).read_bytes(), extended)
        for table in tables:
            for record in table:
                if record['id'] in allowed:
                    for key, raw in record['mods']:
                        if key[0] in allowed[record['id']]:
                            value_type = struct.unpack_from('<I', raw, 4)[0]
                            offset = 16 if extended else 8
                            if value_type == 3:
                                value = raw[offset:-5].decode('utf-8')
                                if value.startswith('TRIGSTR_'):
                                    # Inline only our changed values. Do not publish
                                    # HiveWE's wholesale rewrite of the existing WTS.
                                    value = strings[int(value[8:])]
                                    raw = raw[:offset] + value.encode('utf-8') + b'\0' + raw[-4:]
                            wanted.setdefault(record['id'], {})[key] = raw
    for name in names:
        blob = (original / name).read_bytes()
        version, tables = object_records(blob, extended)
        output = bytearray(struct.pack('<I', version))
        for table in tables:
            output += struct.pack('<I', len(table))
            for record in table:
                code = record['id']
                if code not in allowed:
                    output += record['raw']
                    continue
                mods = [(key, raw) for key, raw in record['mods'] if key[0] not in allowed[code]]
                # Canonical requested values live in the main object file. Clear
                # just their old skin overrides so they cannot mask the new data.
                if name == names[0]:
                    mods += list(wanted.get(code, {}).items())
                output += record['header'] + struct.pack('<I', len(mods)) + b''.join(raw for _, raw in mods)
        (stage / name).write_bytes(output)
        _, actual = object_records(bytes(output), extended)
        for before_table, after_table in zip(tables, actual):
            assert [x['id'] for x in before_table] == [x['id'] for x in after_table]
            for before, after in zip(before_table, after_table):
                if before['id'] not in allowed:
                    assert before['raw'] == after['raw'], before['id']
                else:
                    untouched = lambda rec: [(k,v) for k,v in rec['mods'] if k[0] not in allowed[rec['id']]]
                    assert untouched(before) == untouched(after), before['id']


def import_entries(blob):
    version, count = struct.unpack_from('<II', blob)
    pos, entries = 8, []
    for _ in range(count):
        end = blob.index(0, pos + 1)
        raw = blob[pos:end+1]
        name = raw[1:-1].decode('utf-8').replace('\\', '/')
        if raw[0] not in (10, 13):
            name = 'war3mapImported/' + name
        entries.append((name, raw))
        pos = end + 1
    assert pos == len(blob)
    return version, entries


def references(root, candidates):
    """Conservative byte search includes object/GUI data, Lua, MDX and UTF-16."""
    names = {name: [] for name in candidates}
    needles = {}
    excluded = {name.lower().replace('\\','/') for name in candidates}
    for name in candidates:
        variants = {name.lower()}
        if name.lower().endswith('.mdx'):
            variants.add(name[:-4].lower() + '.mdl')
        needles[name] = [v.encode(encoding) for v in variants for encoding in ('utf-8','utf-16-le')]
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative.lower() in excluded or relative.lower() == 'war3map.imp':
            continue
        data = path.read_bytes().lower().replace(b'\\', b'/')
        for name, variants in needles.items():
            if any(needle in data for needle in variants):
                names[name].append(relative)
    return names


def protect_implicit_references(found):
    """Disabled icons and portraits are loaded by naming convention, not literals."""
    for name in list(found):
        base_names = []
        if name.lower().startswith('replaceabletextures/commandbuttonsdisabled/dis'):
            icon = Path(name).name[3:]
            base_names = ['ReplaceableTextures/CommandButtons/' + icon,
                          'ReplaceableTextures/PassiveButtons/' + icon]
        elif name.lower().endswith('_portrait.mdx'):
            base_names = [name[:-len('_Portrait.mdx')] + '.mdx']
        for base in base_names:
            actual = next((candidate for candidate in found if candidate.lower() == base.lower()), None)
            if actual is not None and found[actual]:
                found[name].append('implicit dependency of ' + actual)
                break


def main():
    OUT.mkdir(exist_ok=True, parents=True)
    before, stage = OUT / 'before', OUT / 'stage'
    before.mkdir(exist_ok=True)
    stage.mkdir(exist_ok=True)
    hashes = {name: digest(MAP / name) for name in FILES}
    for name in FILES:
        if not (before / name).exists():
            shutil.copy2(MAP / name, before / name)
        shutil.copy2(MAP / name, stage / name)
    operations, payload, assets, old_candidates, building_changes = [], {}, [], set(), []
    checked_textures = set()
    original_strings = load_wts_strings(MAP / 'war3map.wts')

    def asset(source, destination):
        source = Path(source)
        data = source.read_bytes()
        target = MAP / destination
        if target.exists() and target.read_bytes() != data:
            raise RuntimeError(f'Asset conflict: {destination}')
        payload[destination] = data
        assets.append({'source': source.relative_to(DONOR).as_posix(), 'path': destination,
                       'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})

    for code, donor_id, short, model, icon, scale in BUILDINGS:
        old = run(MAP, 'get-object', '--type', 'unit', '--id', code)['fields']
        model_path = f'Draenei/Buildings/{short}.mdx'
        icon_path = f'ReplaceableTextures/CommandButtons/BTNDraenei{short}.blp'
        asset(DONOR / model, model_path)
        portrait = Path(model).stem + '_Portrait.mdx'
        if (DONOR / portrait).is_file():
            asset(DONOR / portrait, f'Draenei/Buildings/{short}_Portrait.mdx')
        for texture in textures(DONOR / model):
            relative = texture.replace('\\','/')
            if (DONOR / relative).is_file():
                asset(DONOR / relative, relative)
            elif texture not in checked_textures:
                assert run(MAP, 'asset-exists', '--path', texture)['found'], texture
                checked_textures.add(texture)
        asset(DONOR / icon, icon_path)
        asset(DONOR / 'ReplaceableTextures/CommandButtonsDisabled' / ('DIS' + icon),
              f'ReplaceableTextures/CommandButtonsDisabled/DISBTNDraenei{short}.blp')
        values = {'file': model_path.replace('/','\\'),
                  'art': icon_path.replace('/','\\'), 'modelscale': scale}
        if code in BUILDING_NAMES:
            title, description = BUILDING_NAMES[code]
            values.update({'name': '|cffdcbef0' + title + '|r',
                           'tip': 'Построить |cffdcbef0' + title + '|r', 'ubertip': description})
        fields(stage, 'unit', code, values, operations)
        for extension in ('.mdx','.mdl'):
            name = str(Path(old['file'].replace('\\','/')).with_suffix(extension))
            if (MAP / name).is_file():
                old_candidates.add(name)
                portrait = str(Path(name).with_name(Path(name).stem + '_Portrait' + extension))
                if (MAP / portrait).is_file(): old_candidates.add(portrait)
        old_icon = old['art'].replace('\\','/')
        if (MAP / old_icon).is_file(): old_candidates.add(old_icon)
        disabled = 'ReplaceableTextures/CommandButtonsDisabled/DIS' + Path(old_icon).name
        if (MAP / disabled).is_file(): old_candidates.add(disabled)
        building_changes.append({'id':code, 'donor_id':donor_id, 'before':
            {k:old.get(k) for k in ['file','art','modelscale','collision','pathtex','researches','trains']},
            'after':{'file':model_path,'art':icon_path,'modelscale':scale}})

    seer = run(MAP, 'get-object', '--type', 'unit', '--id', 'n005')['fields']
    abilities = [x for x in seer['abillist'].split(',') if x != 'ADr5']
    abilities = ['ADr5' if x == 'A064' else x for x in abilities]
    if 'ADr5' not in abilities: abilities.insert(1,'ADr5')
    fields(stage, 'unit', 'n005', {'abillist': ','.join(abilities), 'ubertip': SEER_TIP}, operations)
    fields(stage, 'ability', 'ADr5', {'hotkey':'E','buttonpos':3,'buttonpos2':2,
                                    'tip1':'Идол памяти (|cffffcc00E|r)'}, operations)
    fields(stage, 'ability', 'A063', {'hotkey':'L','tip1':'Щит молний (|cffffcc00L|r)'}, operations)
    fields(stage, 'ability', 'A1C8', {'buttonpos':1,'buttonpos2':2}, operations)
    repaired = []
    # Earlier generated recruitment descriptions can contain dangling private
    # stage WTS IDs. Repair only such unresolved descriptions, keeping edits.
    for code in ['e000','h059','h01O','h01R']:
        value = run(MAP,'get-object','--type','unit','--id',code,'--fields','ubertip')['fields']['ubertip']
        if value.startswith('TRIGSTR_') and int(value[8:]) not in original_strings:
            fields(stage,'unit',code,{'ubertip':UNIT_TIPS[code]},operations)
            repaired.append(code)
    merge_fields(MAP, stage, 'u', {**{x[0]:{'umdl','uico','usca'} |
                                 ({'unam','utip','utub'} if x[0] in BUILDING_NAMES else set()) for x in BUILDINGS},
                                 **{code:{'utub'} for code in repaired},
                                 'n005':{'uabi','utub'}})
    merge_fields(MAP, stage, 'a', {'ADr5':{'ahky','abpx','abpy','atp1'},
                                 'A063':{'ahky','atp1'}, 'A1C8':{'abpx','abpy'}})
    for kind in ['unit','ability']:
        relevant = [op for op in operations if op['type']==kind]
        data = run(stage, 'get-objects-bulk', '--type',kind,'--ids',','.join(sorted({x['id'] for x in relevant})),
                   '--fields',','.join(sorted({x['field'] for x in relevant})))
        lookup = {x['id']:x['fields'] for x in data['objects']}
        for op in relevant:
            actual, expected = lookup[op['id']][op['field']], str(op['value'])
            if actual != expected:
                try: assert math.isclose(float(actual),float(expected),rel_tol=1e-6)
                except (ValueError,AssertionError): raise AssertionError((op,actual))
    for name, previous in hashes.items():
        if digest(MAP / name) != previous: raise RuntimeError(f'Concurrent edit: {name}')
    for relative, data in payload.items():
        path=(MAP/relative).resolve()
        assert path.is_relative_to(MAP.resolve())
        path.parent.mkdir(parents=True,exist_ok=True)
        if not path.exists(): path.write_bytes(data)
    changed=[]
    for name in FILES:
        if name in ['war3map.imp','war3map.wts']: continue
        if digest(stage/name) != hashes[name]:
            temporary=MAP/(name+'.buildings.tmp');shutil.copy2(stage/name,temporary)
            os.replace(temporary,MAP/name);changed.append(name)
    # All desired paths are in object data before scanning old references.
    found=references(MAP,old_candidates)
    protect_implicit_references(found)
    removed=[]
    backup=OUT/'removed-assets'
    for name in sorted(old_candidates):
        if found[name]: continue
        path=(MAP/name).resolve()
        assert path.is_relative_to(MAP.resolve()) and path.is_file()
        target=backup/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        path.unlink()
        removed.append(name)
    version, entries=import_entries((MAP/'war3map.imp').read_bytes())
    dead={x.lower() for x in removed}
    entries=[(name,raw) for name,raw in entries if name.lower() not in dead]
    (MAP/'war3map.imp').write_bytes(struct.pack('<II',version,len(entries))+b''.join(raw for _,raw in entries))
    register_imports(MAP/'war3map.imp',payload)
    report={'source':'WL - Bane Burrow v1.63.w3x','buildings':building_changes,
            'operations':operations,'assets':assets,'asset_files':sorted(payload),
            'removed':removed,'retained_references':{k:v for k,v in found.items() if v},
            'changed_files':changed+['war3map.imp'],'before_hashes':hashes}
    (OUT/'replacement.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'changed':changed,'imported':len(payload),'removed':removed,
                     'kept':report['retained_references']},ensure_ascii=True),flush=True)


if __name__=='__main__': main()
