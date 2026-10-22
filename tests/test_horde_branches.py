"""«Истинная Орда» (R0E9) и «Орда — общий дом» (R0EH) взаимоисключающие."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
function FourCC(s) return s end
function GetOwningPlayer(u) return u.owner end
function GetPlayerId(p) return p end
function GetTriggerUnit() return eventUnit end
function GetResearched() return researched end
maxAllowed={}; techs={}; orders={}
function SetPlayerTechMaxAllowed(p,id,n) maxAllowed[id]=n end
function SetPlayerTechMaxAllowedSwap(id,n,p) maxAllowed[id]=n end
function GetPlayerTechMaxAllowedSwap(id,p) return maxAllowed[id] or -1 end
function GetPlayerTechCount(p,id,s) return techs[id] or 0 end
function IssueImmediateOrderById(u,o) orders[#orders+1]=o; return true end
udg_MainPrice={[0]=0}
building={owner=0}; eventUnit=building
'''


class HordeBranchTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute(FIXTURE)
        source = (SECTIONS / '80_runtime/triggers/races/Horde.lua').read_text(encoding='utf-8')
        self.lua.execute(source)
        self.lua.execute('function countAll(p) end')

    def g(self, name):
        return self.lua.globals()[name]

    def test_common_home_start_locks_true_horde(self):
        self.g('Trig_BeginCommonHome_Actions')()
        self.assertEqual(self.g('maxAllowed')['R0E9'], 0)

    def test_second_branch_in_queue_is_cancelled(self):
        self.g('Trig_BeginCommonHome_Actions')()
        self.g('Trig_StartTrueHorde_Actions')()
        self.assertEqual(list(self.g('orders').values()), [851976])
        # отмена второй ветки не снимает выбор первой
        self.g('Trig_CanselTrueHorde_Actions')()
        self.assertEqual(self.g('HordeBranchStarted')[0], 'R0EH')

    def test_cancel_restores_other_branch(self):
        self.g('techs')['R0E0'] = 1
        self.g('Trig_BeginCommonHome_Actions')()
        self.g('Trig_CanselCommonHome_Actions')()
        self.assertEqual(self.g('maxAllowed')['R0E9'], 1)
        self.assertIsNone(self.g('HordeBranchStarted')[0])

    def test_prerequisite_does_not_reopen_chosen_out_branch(self):
        self.g('Trig_StartTrueHorde_Actions')()
        self.g('techs')['R0EE'] = 1
        self.g('Trig_Pandarens_Actions')()
        self.assertEqual(self.g('maxAllowed')['R0EH'], 0)

    def test_cancel_condition_is_common_home(self):
        self.lua.globals()['researched'] = 'R0EH'
        self.assertTrue(self.g('Trig_CanselCommonHome_Conditions')())


if __name__ == '__main__':
    unittest.main()
