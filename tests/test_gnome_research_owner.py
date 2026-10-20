"""Gnome production research must unlock units for the researching player."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SOURCE = (Path(__file__).resolve().parents[1] /
          'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Gnomes.lua')


class GnomeResearchOwnerTests(unittest.TestCase):
    def test_mass_production_unlocks_units_for_research_owner_in_any_slot(self):
        source = SOURCE.read_text(encoding='utf-8')
        action = source.split('function Trig_Klap_Klap_War_small_Actions()', 1)[1]
        action = 'function Trig_Klap_Klap_War_small_Actions()' + action.split(
            'function InitTrig_Klap_Klap_War_small()', 1)[0]
        for owner in (0, 1, 7, 23):
            with self.subTest(owner=owner):
                lua = LuaRuntime()
                lua.execute('''
                    limits = {}
                    function FourCC(code) return code end
                    function Player(slot) return slot end
                    function GetTriggerUnit() return 'research-building' end
                    function GetOwningPlayer(unit)
                        assert(unit == 'research-building')
                        return researchOwner
                    end
                    function SetPlayerTechMaxAllowedSwap(code, limit, player)
                        limits[player] = limits[player] or {}
                        limits[player][code] = limit
                    end
                    gg_trg_All_Gnomes = 'refresh-research'
                    function TriggerExecute(trigger)
                        assert(trigger == gg_trg_All_Gnomes)
                        refreshedOwner = udg_LocalPlayer
                    end
                ''')
                state = lua.globals()
                state.researchOwner = owner
                lua.execute(action)
                state.Trig_Klap_Klap_War_small_Actions()
                self.assertEqual(state.limits[owner]['h0FX'], 0)
                self.assertEqual(state.limits[owner]['h0G4'], -1)
                self.assertEqual(state.limits[owner]['R0BO'], 0)
                self.assertEqual(state.limits[owner]['R0B7'], 0)
                self.assertEqual(state.refreshedOwner, owner)
                if owner != 0:
                    self.assertIsNone(state.limits[0])


if __name__ == '__main__':
    unittest.main()
