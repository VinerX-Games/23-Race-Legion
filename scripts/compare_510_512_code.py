"""Read-only, exhaustive comparison of the two release MPQs; writes reports only."""
from pathlib import Path
import ctypes as c
import difflib
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'comparison_510_512'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    dll = c.WinDLL(str(ROOT / '.cache/hivewe-build/Release/StormLib.dll'))
    handle = c.c_void_p
    dll.SFileOpenArchive.argtypes = [c.c_wchar_p, c.c_uint32, c.c_uint32, c.POINTER(handle)]
    dll.SFileOpenFileEx.argtypes = [handle, c.c_char_p, c.c_uint32, c.POINTER(handle)]
    dll.SFileGetFileSize.argtypes = [handle, c.POINTER(c.c_uint32)]
    dll.SFileGetFileSize.restype = c.c_uint32
    dll.SFileReadFile.argtypes = [handle, c.c_void_p, c.c_uint32, c.POINTER(c.c_uint32), c.c_void_p]
    dll.SFileCloseFile.argtypes = [handle]
    dll.SFileCloseArchive.argtypes = [handle]

    def read(archive, name):
        fh = handle()
        if not dll.SFileOpenFileEx(archive, name.encode('utf-8'), 0, c.byref(fh)):
            raise OSError(f'Cannot read {name}')
        try:
            high = c.c_uint32()
            size = dll.SFileGetFileSize(fh, c.byref(high))
            assert high.value == 0
            buf = c.create_string_buffer(size)
            got = c.c_uint32()
            if size and not dll.SFileReadFile(fh, buf, size, c.byref(got), None):
                raise OSError(f'Read failed: {name}')
            assert got.value == size
            return buf.raw
        finally:
            dll.SFileCloseFile(fh)

    archives = {}
    sources = {}
    names = {}
    hashes = {}
    for version, filename in [('510', '23_Race_Legion_v1_6_510.w3x'), ('512', '23_race_1_6_512.w3x')]:
        path = ROOT / filename
        hashes[version] = hashlib.sha256(path.read_bytes()).hexdigest()
        h = handle()
        if not dll.SFileOpenArchive(str(path), 0, 0x100, c.byref(h)):
            raise OSError(f'Cannot open {path}')
        archives[version] = h
        names[version] = {s.replace('/', '\\') for s in read(h, '(listfile)').decode('utf-8-sig').splitlines() if s}
        sources[version] = {}
    records = []
    try:
        for name in sorted(names['510'] | names['512']):
            entry = {'file': name}
            for version in archives:
                data = read(archives[version], name) if name in names[version] else None
                entry[version] = None if data is None else {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
                if data is not None and (name.lower().endswith(('.lua', '.j', '.ai', '.tmp', '.json', '.jsonl', '.txt', '.md', '.wts')) or name in ('war3map.wct', 'war3map.wtg')):
                    sources[version][name] = data
            records.append(entry)
    finally:
        for h in archives.values():
            dll.SFileCloseArchive(h)
    changed = [r for r in records if r['510'] != r['512']]
    (OUT / 'inventory.json').write_text(json.dumps({'archive_sha256': hashes, 'counts': {v: len(n) for v, n in names.items()}, 'files': records}, ensure_ascii=False, indent=2), encoding='utf-8')
    old_audit = json.loads((ROOT / '.cache/wc3/movement-code-audit-full.json').read_text(encoding='utf-8'))
    lines = ['# Полное сравнение кода 510 → 512', '', 'Сравниваются архивы `23_Race_Legion_v1_6_510.w3x` и `23_race_1_6_512.w3x`, а не текущая рабочая карта. Игра не запускалась, игровая логика не изменялась.', '', '## Полнота проверки', '', f"Прочитаны и проверены SHA256 всех файлов из MPQ listfile: {len(names['510'])} в 510 и {len(names['512'])} в 512. Отличаются {len(changed)} файлов (включая добавленные и удалённые). Полный реестр, в том числе неизменённых файлов: [inventory.json](comparison_510_512/inventory.json).", '', 'Далее приведены все изменения текстовых исходников с тремя строками контекста. Ничего не отфильтровано по связи с движением: включены комментарии, пути ресурсов, глобальные объявления и код вне функций. `-` — 510, `+` — 512; номера в `@@` относятся к указанным файлам.', '', 'Архивные Lua-секции проверены по manifest и сопоставлены с исполняемым `war3map.lua`; полный diff исполняемого скрипта также сохранён отдельно.', '']
    # Check actual archive manifests and concatenation, rather than cached extracts.
    for version in archives:
        manifest = json.loads(sources[version]['_lua\\monolith_split\\manifest.json'])
        section_names = ['_lua\\monolith_split\\sections\\' + s['file'].replace('/', '\\') for s in manifest['sections']]
        text = ''.join(sources[version][n].decode('utf-8-sig').replace('\r\n', '\n') for n in section_names)
        script = sources[version]['war3map.lua'].decode('utf-8-sig').replace('\r\n', '\n')
        assert text == script, f'{version}: sections differ from executable Lua'
        lines += [f"- {version}: {len(section_names)} секций; конкатенация точно совпадает с исполняемым Lua. SHA256 архива: `{hashes[version]}`."]
    lines += ['', '## Все изменённые файлы', '', '| Файл | Байты 510 | Байты 512 |', '|---|---:|---:|']
    for r in changed:
        lines.append('| `' + r['file'].replace('\\', '/') + '` | ' + ' | '.join(str(r[v]['size']) if r[v] else 'отсутствует' for v in ('510', '512')) + ' |')
    lines += ['', '## Индекс изменённых именованных функций', '', 'Навигационный индекс предыдущего разбора функций; полнота изменений обеспечивается файловыми diff ниже, включая изменения вне функций.', '', '| Функция | Секция | Строка Lua 510 | Строка Lua 512 |', '|---|---|---:|---:|']
    for f in old_audit['changed_functions']:
        before, after = f.get('before'), f.get('after')
        src = (after or before)['source']['file']
        lines.append(f"| `{f['function']}` | `{src}` | {before['line'] if before else '—'} | {after['line'] if after else '—'} |")
    lines += ['', '## Все построчные изменения', '']
    patches = []
    for r in changed:
        name = r['file']
        a = sources['510'].get(name, b'')
        b = sources['512'].get(name, b'')
        if name not in sources['510'] and name not in sources['512']:
            continue
        if name.endswith(('.wct', '.wtg')):
            # Preserve every binary edit too; these are editor containers, not Lua source.
            target = OUT / (name + '.510.bin')
            target.write_bytes(a)
            (OUT / (name + '.512.bin')).write_bytes(b)
            continue
        try:
            at, bt = a.decode('utf-8-sig'), b.decode('utf-8-sig')
        except UnicodeDecodeError:
            at, bt = a.decode('cp1251'), b.decode('cp1251')
        diff = ''.join(difflib.unified_diff(at.splitlines(keepends=True), bt.splitlines(keepends=True), fromfile='510/' + name.replace('\\', '/'), tofile='512/' + name.replace('\\', '/')))
        patches.append(diff)
        if name == 'war3map.lua':
            (OUT / 'war3map.lua.diff').write_text(diff, encoding='utf-8')
            continue
        lines += ['### `' + name.replace('\\', '/') + '`', '', '````diff', diff.rstrip(), '````', '']
    (OUT / 'all-text.diff').write_text('\n'.join(patches), encoding='utf-8')
    lines += ['## Полный diff исполняемого Lua', '', '[war3map.lua.diff](comparison_510_512/war3map.lua.diff) содержит все изменения итогового скрипта. [all-text.diff](comparison_510_512/all-text.diff) содержит все изменённые текстовые файлы одним diff.', '', '## Данные объектов (дополнение к коду)', '', 'Все различия полей из предыдущего object-data сравнения, без отбора по проходимости:', '', '| Файл | ID | База | Поле | Уровень / data | 510 | 512 |', '|---|---|---|---|---|---|---|']
    objects = json.loads((ROOT / '.cache/wc3/movement-object-diff.json').read_text(encoding='utf-8'))
    for r in objects:
        def value(v):
            return '`' + json.dumps(v, ensure_ascii=False).replace('|', '\\|') + '`'
        lines.append(f"| {r['file']} | {r['id']} | {r['base']} | {r['field']} | {r['level']} / {r['data']} | {value(r['510'])} | {value(r['512'])} |")
    # The newly added editor containers are tiny and contain no trigger code.
    wct = sources['512']['war3map.wct']
    assert struct.unpack_from('<II', wct) == (0x80000004, 1)
    end = wct.index(b'\0', 8)
    comment = wct[8:end].decode('utf-8')
    assert struct.unpack_from('<I', wct, end + 1)[0] == 0
    assert len(wct) == end + 5
    wtg = sources['512']['war3map.wtg']
    assert wtg[:4] == b'WTG!'
    words = struct.unpack_from('<' + 'I' * 23, wtg, 4)
    assert words[:2] == (0x80000004, 7)
    assert words[2:16] == (1, 0) + (0, 0) * 6
    assert words[16:20] == (0, 0, 2, 0)
    assert words[20:] == (1, 1, 0)
    assert wtg[96:] == b'23 Race Legion\0' + struct.pack('<III', 0, 1, 0xffffffff)
    lines += ['', '## Добавленные редакторские контейнеры WCT / WTG', '',
              'В 510 эти файлы отсутствуют (сохранённые `.510.bin` пусты). В 512:', '',
              '- `war3map.wct`: формат `0x80000004`, подформат 1, размер 138 байт. Глобальный скрипт имеет длину 0; пользовательских скриптов триггеров нет. Единственное текстовое содержимое — комментарий:', '',
              '```text', comment, '```', '',
              '- `war3map.wtg`: формат `0x80000004`, подформат 7, размер 123 байта. Одна запись карты `23 Race Legion` (ID 0, parent ID -1, open state 1, is_comment 0). Библиотек, категорий, триггеров, комментариев, скриптов, переменных и удалённых ID нет. Служебные значения unknown1=0, unknown2=0, trig_def_ver=2. Исполняемого кода контейнер не содержит.', '',
              'Структура проверена по парсеру HiveWE `src/base/triggers/triggers.ixx` (`load_version_31`, `load_scripts`); проверено полное потребление байтов. Точные двоичные файлы обеих версий сохранены в `docs/comparison_510_512/`.', '',
              '## Границы сравнения', '', 'Полнота реестра — относительно MPQ listfile. `war3map.j` пуст и одинаков в обеих версиях. Неисполняемые исходники и резервные файлы также охвачены реестром; отсутствие diff означает одинаковые байты. Manifest и порядок секций проверены непосредственно в архивах. Здесь не делается вывод о причине бага.']
    (ROOT / 'docs/CODE_DIFF_510_512.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'files': {v: len(n) for v, n in names.items()}, 'changed_files': len(changed), 'report': 'docs/CODE_DIFF_510_512.md', 'report_lines': len('\n'.join(lines).splitlines())}))


if __name__ == '__main__':
    main()
