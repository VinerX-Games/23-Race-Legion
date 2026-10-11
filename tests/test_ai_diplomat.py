import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / 'map.w3x/_lua/monolith_split/sections'

FIXTURE = r'''
function Player(i) return i end
function IsPlayerAlly(a, b) return true end
function GetRandomReal(a, b) return ROLL end
function ProbeLogWrite(s) LOG[#LOG + 1] = s end
LOG = {}
Grades = {}
AiDiplomatTicks = {}
RACE = { key = "Test", diplomat = {} }
function AiRaceOf(pi) return RACE end
'''


class AiDiplomatBreakTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute((SECTIONS / '84_ai_diplomat.lua').read_text(encoding='utf-8'))

    def test_betrayal_roll_on_young_alliance_does_not_crash(self):
        # Регрессия: otherPower/myPower были local внутри `if allyAge >= MinAllyAge`,
        # а читались в блоке предательства -> "attempt to compare nil".
        self.lua.execute(r'''
            RACE.diplomat = { betrayalChance = 1.0, betrayTimeMin = 1, breakChanceBase = 0.0 }
            Grades[0] = 10; Grades[1] = 5
            AiDiplomatTicks[0] = 5
            local st = AiDiplomatState(0)
            st.relations[1] = { sharedEnemies = 1 }
            st.alliedAt = { [1] = 4 }
            ROLL = 0.0
        ''')
        brk, reason = self.lua.eval('AiDiplomatConsiderBreak(0, 1)')
        self.assertFalse(brk)
        self.assertIsNotNone(self.lua.eval('AiDiplomatState(0).betrayTargets[1]'))


if __name__ == '__main__':
    unittest.main()
