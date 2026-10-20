"""Reincarnation resets require an enemy kill without summoned victims."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SOURCE = (Path(__file__).resolve().parents[1] /
          'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Bezlikie.lua')


class FacelessReincarnationTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            UNIT_TYPE_SUMMONED = 'summoned'
            killer = {owner=7, reincarnation=1}
            victim = {owner=8, summoned=false, allied=false}
            resets = 0
            function FourCC(code) return code end
            function GetKillingUnit() return killer end
            function GetKillingUnitBJ() return killer end
            function GetTriggerUnit() return victim end
            function GetOwningPlayer(unit) return unit.owner end
            function GetUnitAbilityLevel(unit, ability)
                assert(ability == 'A123')
                return unit and unit.reincarnation or 0
            end
            function GetUnitAbilityLevelSwapped(ability, unit) return GetUnitAbilityLevel(unit, ability) end
            function IsUnitEnemy(unit, player) return unit.owner ~= player and not unit.allied end
            function IsUnitType(unit, kind)
                assert(kind == UNIT_TYPE_SUMMONED)
                return unit.summoned
            end
            function BlzEndUnitAbilityCooldown(unit, ability)
                assert(unit == killer and ability == 'A123')
                resets = resets + 1
            end
        ''')
        source = SOURCE.read_text(encoding='utf-8')
        block = source.split('function Trig_SpellRes_Conditions()', 1)[1]
        block = block.split('function InitTrig_SpellRes()', 1)[0]
        self.lua.execute('function Trig_SpellRes_Conditions()' + block)

    def try_kill(self):
        self.lua.execute('if Trig_SpellRes_Conditions() then Trig_SpellRes_Actions() end')
        return self.lua.globals().resets

    def test_regular_enemy_resets_reincarnation(self):
        self.assertEqual(self.try_kill(), 1)

    def test_summoned_enemy_does_not_reset(self):
        self.lua.globals().victim.summoned = True
        self.assertEqual(self.try_kill(), 0)

    def test_allied_and_own_units_do_not_reset(self):
        self.lua.globals().victim.allied = True
        self.assertEqual(self.try_kill(), 0)
        self.lua.globals().victim.allied = False
        self.lua.globals().victim.owner = 7
        self.assertEqual(self.try_kill(), 0)

    def test_missing_killer_or_ability_does_not_reset(self):
        self.lua.globals().killer.reincarnation = 0
        self.assertEqual(self.try_kill(), 0)
        self.lua.globals().killer = None
        self.assertEqual(self.try_kill(), 0)


if __name__ == '__main__':
    unittest.main()
