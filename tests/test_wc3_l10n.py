"""Localization catalog, WTS generation and translation validation."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

import wc3_l10n  # noqa: E402


class WtsTests(unittest.TestCase):
    def test_roundtrip_preserves_bom_order_and_crlf(self):
        raw = ('\ufeffSTRING 000\r\n{\r\nПривет\r\n}\r\n\r\n'
               'STRING 10000\r\n{\r\nВторой|nблок\r\n}\r\n\r\n'
               'STRING 101\r\n{\r\nТретий\r\n}\r\n\r\n').encode('utf-8')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'war3map.wts'
            path.write_bytes(raw)
            strings, meta = wc3_l10n.load_wts(path)
            self.assertEqual([0, 10000, 101], meta['order'])
            output = (wc3_l10n.codecs.BOM_UTF8 if meta['bom'] else b'') + \
                     wc3_l10n.dump_wts(strings, meta).encode('utf-8')
            self.assertEqual(raw, output)


class TranslationTests(unittest.TestCase):
    def test_format_drift_is_rejected(self):
        source = '|cffff000010 damage|r'
        self.assertIn('numbers differ', wc3_l10n.check_text(source, '|cffff000020 damage|r'))
        self.assertIn('color sequence differs', wc3_l10n.check_text(source, '|cff00ff0010 damage|r'))
        self.assertIn('Cyrillic text remains', wc3_l10n.check_text(source, '|cffff000010 урона|r'))

    def test_ability_data_reference_drift_is_rejected(self):
        source = 'Deals <ANbf,DataA1> damage for <ANbf,Dur1> sec.'
        self.assertEqual([], wc3_l10n.check_text(source, source))
        broken = 'Deals <ANbf,DataA2> damage for <ANbf,Dur1> sec.'
        self.assertIn('ability data references differ', wc3_l10n.check_text(source, broken))

    def test_shared_wts_id_rejects_conflicting_translations(self):
        catalog = {'entries': [
            {'key': 'A/unit/name', 'sid': 7, 'skin': False, 'text': 'Имя'},
            {'key': 'B/unit/name', 'sid': 7, 'skin': False, 'text': 'Имя'},
        ]}
        resolved, conflicts = wc3_l10n.resolve_translations(
            catalog, {'A/unit/name': 'Name A', 'B/unit/name': 'Name B'})
        self.assertTrue(conflicts)
        self.assertEqual(resolved[7], 'Name A')

    def test_hd_entry_falls_back_to_sd_translation(self):
        catalog = {'entries': [
            {'key': 'A/unit/name@hd', 'sid': 7, 'skin': True, 'text': 'Имя'},
        ]}
        resolved, conflicts = wc3_l10n.resolve_translations(
            catalog, {'A/unit/name': 'Name'})
        self.assertEqual([], conflicts)
        self.assertEqual('Name', resolved[7])

    def test_ui_lua_escapes_strings_and_selects_english(self):
        lua = wc3_l10n.render_ui_lua({'ruRU': {'k': 'строка'}, 'enUS': {'k': 'line "quoted"'}})
        self.assertIn('MapLocale = "ruRU"', lua)
        self.assertIn('["k"] = "line \\"quoted\\"",', lua)
        self.assertIn('function Loc(key)', lua)


class PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = wc3_l10n.extract_catalog()
        cls.temp = tempfile.TemporaryDirectory()
        path = Path(cls.temp.name) / 'catalog.json'
        path.write_text(wc3_l10n.format_catalog(cls.catalog), encoding='utf-8')
        cls.previous = wc3_l10n.CATALOG_PATH
        wc3_l10n.CATALOG_PATH = path

    @classmethod
    def tearDownClass(cls):
        wc3_l10n.CATALOG_PATH = cls.previous
        cls.temp.cleanup()

    def test_catalog_covers_stromgard_selection_and_units(self):
        entries = {(e['id'], e['field']): e for e in self.catalog['entries']}
        self.assertIn(('A0Y0', 'ubertip'), entries)
        self.assertIn(('h0GS', 'ubertip'), entries)
        self.assertIn(('h0GZ', 'ubertip'), entries)

    def test_command_strings_match_base_sections(self):
        overlap = wc3_l10n.command_sections(
            ROOT / 'localization/locales/enUS/overlay/Units/CommandStrings.txt')
        base = wc3_l10n.command_sections(ROOT / 'map.w3x/Units/CommandStrings.txt')
        self.assertEqual(set(base), set(overlap))
        self.assertEqual(set(base['CmdMove']), set(overlap['CmdMove']))

    def test_pilot_translations_validate(self):
        self.assertEqual(0, wc3_l10n.validate('enUS', check_output=False))


if __name__ == '__main__':
    unittest.main()
