"""Economy boundaries and agreement between previews and actual payouts."""
import math
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


RUNTIME = (Path(__file__).resolve().parents[1] / 'map.w3x/_lua/'
           'monolith_split/sections/80_runtime')


class EconomyBalanceTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            income, disincome, logistic, corruption, additional = {}, {}, {}, {}, {}
            incomeW, AllyTax, udg_UnitsCount, udg_MainPrice = {}, {}, {}, {}
            gold, lumber = {}, {}
            for i = 0, 23 do
                income[i], disincome[i], logistic[i] = 1000, 100, 0
                corruption[i], additional[i] = 0, 0
                incomeW[i], AllyTax[i], udg_UnitsCount[i], udg_MainPrice[i] = 50, 0.1, 49, 0
                gold[i], lumber[i] = 10000, 1000
            end
            balance = {}; IncomeMod = 0.75; DisOn = true; EcLog = false
            PLAYER_STATE_RESOURCE_GOLD = 'gold'; PLAYER_STATE_RESOURCE_LUMBER = 'lumber'
            function Player(i) return i end
            function FourCC(id) return id end
            function GetPlayerTechCount() return 0 end
            function R2I(value) return math.modf(value) end
            function GetPlayerState(p, state) return state == 'gold' and gold[p] or lumber[p] end
            function SetPlayerState(p, state, amount)
                if state == 'gold' then gold[p] = amount else lumber[p] = amount end
            end
            function ArmyExpSetBonus() end
            function EnsureMultiboardPlayerRow() return nil end
        ''')
        for source in ('_lib/51_update_graph.lua', 'triggers/01_core_economy.lua'):
            self.lua.execute((RUNTIME / source).read_text(encoding='utf-8'))

    def test_logistics_preserves_bracket_anchors(self):
        calculate = self.lua.globals().CalculateLogistics
        for count, expected in [(0, 0), (25, 250), (50, 600), (75, 1050),
                                (100, 1600), (200, 4800)]:
            with self.subTest(count=count):
                self.assertEqual(calculate(count), expected)
        self.assertEqual(calculate(-1), 0)
        self.assertEqual(calculate(None), 0)

    def test_logistics_has_no_boundary_jumps(self):
        calculate = self.lua.globals().CalculateLogistics
        for count in range(1, 501):
            # Each unit pays only its marginal share of the next bracket.
            expected_step = 10 + 4 * ((count - 1) // 25)
            self.assertAlmostEqual(calculate(count) - calculate(count - 1), expected_step)
        self.assertEqual(calculate(49), 586)
        self.assertEqual(calculate(99), 1578)

    def test_preview_and_payout_agree_with_tax_and_expenses(self):
        state = self.lua.globals()
        for modifier in (0.75, 1, 1.2):
            for tax in (0, 0.1, 0.3):
                for expenses in (False, True):
                    with self.subTest(modifier=modifier, tax=tax, expenses=expenses):
                        state.IncomeMod = modifier
                        state.AllyTax[0] = tax
                        state.DisOn = expenses
                        # Existing faction bonuses must remain part of the net amount.
                        state.corruption[0] = 15
                        state.additional[0] = 20
                        expected = 1000 * modifier * (1 - tax)
                        if expenses:
                            expected += -100 - 586 + 15 + 20
                        state.UpdateGraf(0)
                        self.assertAlmostEqual(state.balance[0], expected)
                        previous_gold = state.gold[0]
                        previous_lumber = state.lumber[0]
                        state.Trig_TimerIncome_Actions()
                        self.assertAlmostEqual(state.balance[0], expected)
                        self.assertEqual(state.gold[0] - previous_gold, math.trunc(expected))
                        self.assertEqual(state.lumber[0] - previous_lumber, 50)


if __name__ == '__main__':
    unittest.main()
