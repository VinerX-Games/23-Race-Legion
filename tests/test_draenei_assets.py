"""Verify research wiring, asset imports and the original memory idol model."""
import re
import struct
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from implement_draenei_rework import object_records, preserve_unrelated
from replace_draenei_buildings import protect_implicit_references


def object_mods(filename):
    _, tables = object_records((ROOT / 'map.w3x' / filename).read_bytes(), filename.endswith(('.w3a','.w3q')))
    result = {}
    for table in tables:
        for record in table:
            values = {}
            for (field, level, pointer), blob in record['mods']:
                value_type = struct.unpack_from('<I', blob, 4)[0]
                offset = 16 if filename.endswith(('.w3a','.w3q')) else 8
                value = (blob[offset:-5].decode('utf-8') if value_type == 3 else
                         struct.unpack_from('<i' if value_type == 0 else '<f', blob, offset)[0])
                values[(field,level,pointer)] = value
            result[record['id']] = values
    return result


class DraeneiAssetTests(unittest.TestCase):
    def test_shared_icons_keep_their_implicitly_loaded_disabled_variant(self):
        normal='ReplaceableTextures/CommandButtons/BTNdbase2.blp'
        disabled='ReplaceableTextures/CommandButtonsDisabled/DISBTNdbase2.blp'
        refs={normal:['war3map.w3u: h017'],disabled:[]}
        protect_implicit_references(refs)
        self.assertTrue(refs[disabled])

    def test_seer_replaces_mana_aura_with_idol_on_e_without_conflicting_hotkey(self):
        units=object_mods('war3map.w3u')
        abilities=units['n005'][('uabi',0,0)].split(',')
        self.assertNotIn('A064',abilities)
        self.assertEqual(abilities.count('ADr5'),1)
        spells=object_mods('war3map.w3a')
        if 'ADr5' in spells:
            self.assertEqual(spells['ADr5'][('ahky',0,0)],'E')
            self.assertEqual(spells['ADr5'][('abpx',0,0)],3)
            self.assertEqual(spells['ADr5'][('abpy',2,0)],2)
        if 'A063' in spells and ('ahky',0,0) in spells['A063']:
            self.assertEqual(spells['A063'][('ahky',0,0)],'L')

    def test_object_merge_preserves_unknown_fields_and_unrelated_records(self):
        def mod(field, value):
            return field.encode('ascii') + struct.pack('<I',3) + value.encode('utf-8') + b'\0' + b'TEST'

        def record(code, abilities, opaque):
            return b'hfoo' + code.encode('ascii') + struct.pack('<III',1,0,2) + mod('uabi',abilities) + mod('zzzz',opaque)

        def table(records):
            return struct.pack('<III',3,0,len(records)) + b''.join(records)

        before = table([record('e000','A05U','preserve'),record('hfoo','old','unrelated')])
        after = table([record('e000','ADr1','normalized'),record('hfoo','changed','changed')])
        with tempfile.TemporaryDirectory() as directory:
            original=Path(directory)/'before.w3u'; edited=Path(directory)/'after.w3u'
            original.write_bytes(before); edited.write_bytes(after)
            preserve_unrelated(original,edited,set(),{'e000'})
            expected=table([record('e000','ADr1','preserve'),record('hfoo','old','unrelated')])
            self.assertEqual(edited.read_bytes(),expected)

    def test_new_research_is_available_at_the_correct_building(self):
        units = object_mods('war3map.w3u')
        upgrades = object_mods('war3map.w3q')
        for building, expected in [('h033',['RDr1']),('h058',['RDr2','RDr3','RDr4']),('h05A',['RDr5'])]:
            available = units[building][('ures',0,0)].split(',')
            for code in expected:
                self.assertIn(code, available)
                self.assertEqual(upgrades[code][('glvl',0,0)], 1)
        self.assertNotIn('R02A',units['h033'][('ures',0,0)])
        self.assertNotIn('R02O',units['h058'][('ures',0,0)])

    def test_five_units_equip_replacements_and_keep_other_abilities(self):
        units = object_mods('war3map.w3u')
        for unit,old,new in [('e000','A05U','ADr1'),('h059','A05S','ADr2'),('h01O','A04V','ADr3'),
                             ('h01R','A053','ADr4'),('n005','A062','ADr5')]:
            actual = units[unit][('uabi',0,0)].split(',')
            self.assertIn(new,actual)
            self.assertNotIn(old,actual)
            self.assertGreater(len(actual),1)

    def test_reference_icons_and_effects_are_files_and_registered_imports(self):
        blob = (ROOT / 'map.w3x/war3map.imp').read_bytes()
        _, count = struct.unpack_from('<II',blob)
        pos, imports = 8, set()
        for _ in range(count):
            end = blob.index(0,pos+1)
            imports.add(blob[pos+1:end].decode('utf-8').replace('\\','/'))
            pos = end+1
        for short in ['Prismatic','Blade','Vow','Salvation','Memory']:
            for path in [f'ReplaceableTextures/CommandButtons/BTNDraenei{short}.blp',
                         f'ReplaceableTextures/CommandButtonsDisabled/DISBTNDraenei{short}.blp']:
                self.assertIn(path,imports)
                self.assertTrue((ROOT / 'map.w3x' / path).is_file())
        source = (ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Draenei.lua').read_text(encoding='utf-8')
        paths = re.findall(r'"(Draenei\\\\Effects\\\\[^"\n]+)"',source)
        self.assertEqual(len(paths),5)
        for path in paths:
            relative = path.replace('\\\\','/')
            self.assertIn(relative,imports)
            self.assertTrue((ROOT/'map.w3x'/relative).is_file())

    def test_memory_idol_keeps_original_ward_base_and_has_no_duplicate_heal_aura(self):
        _, tables = object_records((ROOT/'map.w3x/war3map.w3u').read_bytes(),False)
        ward = next(x for table in tables for x in table if x['id']=='nDr1')
        self.assertEqual(ward['header'][:4],b'ohwd')
        mods = object_mods('war3map.w3u')['nDr1']
        self.assertNotIn(('umdl',0,0),mods)
        self.assertEqual(mods[('uabi',0,0)],'ACmi')


if __name__ == '__main__':
    unittest.main()
