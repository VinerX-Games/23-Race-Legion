"""Цикл отталкивания Груула (gg_trg_RRR) работает только во время кастов и не обрывает чужие касты."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]
TRIGGERS = ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/triggers'


def load_function(lua, filename, name):
    source = (TRIGGERS / filename).read_text(encoding='utf-8')
    block = source.split('function ' + name + '()', 1)[1]
    block = block.split('\nfunction ', 1)[0]
    lua.execute('function ' + name + '()' + block)


class GruulAuraLoopTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            Gruul, GruulCast, GruulActive = {}, {}, 0
            function FourCC(s) return s end
            function I2R(x) return x end
            function GetPlayerId(p) return p end
            function GetOwningPlayer(u) return u.owner end
            function GetTriggerUnit() return caster end
            function GetSpellAbilityUnit() return caster end
            function GetUnitAbilityLevel() return 1 end
            function CreateTrigger() return {enabled=true} end
            function DisableTrigger(t) t.enabled=false end
            function EnableTrigger(t) t.enabled=true end
            function TriggerRegisterTimerEventPeriodic() end
            function TriggerAddAction() end
            function TriggerSleepAction() coroutine.yield() end
            function cast(u)
                caster = u
                local co = coroutine.create(Trig_GruulSpell_Actions)
                assert(coroutine.resume(co))
                return co
            end
            function finish(co) assert(coroutine.resume(co)); assert(coroutine.status(co) == 'dead') end
        ''')
        load_function(self.lua, '01_core_economy.lua', 'InitTrig_RRR')
        load_function(self.lua, '07_mixed_heroes.lua', 'Trig_GruulSpell_Actions')
        self.lua.execute('InitTrig_RRR()')

    def ev(self, code):
        return self.lua.eval(code)

    def test_loop_is_disabled_until_first_cast(self):
        self.assertFalse(self.ev('gg_trg_RRR.enabled'))

    def test_loop_runs_while_any_gruul_casts(self):
        self.lua.execute('a = {owner=1}; b = {owner=2}; ca = cast(a); cb = cast(b)')
        self.assertTrue(self.ev('gg_trg_RRR.enabled'))
        self.lua.execute('finish(ca)')
        self.assertTrue(self.ev('gg_trg_RRR.enabled'))
        self.assertTrue(self.ev('Gruul[1] == nil and Gruul[2] == b'))
        self.lua.execute('finish(cb)')
        self.assertFalse(self.ev('gg_trg_RRR.enabled'))
        self.assertTrue(self.ev('Gruul[2] == nil and GruulActive == 0'))

    def test_recast_by_same_player_is_not_cut_by_previous_cast(self):
        self.lua.execute('a1 = {owner=3}; a2 = {owner=3}; c1 = cast(a1); c2 = cast(a2); finish(c1)')
        self.assertTrue(self.ev('gg_trg_RRR.enabled and Gruul[3] == a2'))
        self.lua.execute('finish(c2)')
        self.assertTrue(self.ev('not gg_trg_RRR.enabled and Gruul[3] == nil'))


if __name__ == '__main__':
    unittest.main()
