"""Check construction procs and deferred effect cleanup with mocked natives."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]


class DraeneiConstructionTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            UNIT_STATE_LIFE = 0
            building = {id = 1, life = 100}
            researched, succeeds = true, true
            timers, effects = {}, {}
            function FourCC(id) return id end
            function GetConstructingStructure() return building end
            function GetOwningPlayer(u) return 0 end
            function GetPlayerTechCount(...) return researched and 1 or 0 end
            function Random(a, b) return succeeds end
            function GetUnitTypeId(u) return u.id end
            function GetUnitState(u, state) return u.life end
            function CreateTimer()
                local t = {}; table.insert(timers, t); return t
            end
            function TimerStart(t, delay, repeating, callback)
                assert(delay == 0 and not repeating)
                t.callback = callback
            end
            function DestroyTimer(t) t.destroyed = true end
            function UnitSetConstructionProgress(u, value) u.progress = value end
            function UnitRemoveAbility(u, id) u.removed = id end
            function AddSpecialEffectTarget(path, u, attachment)
                assert(u.progress == 20 and attachment == 'origin')
                local e = {unit = u, path = path}
                table.insert(effects, e); return e
            end
            function DestroyEffect(e) e.destroyed = true end
        ''')
        source = ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Draenei.lua'
        self.lua.execute(source.read_text(encoding='utf-8'))

    def test_success_defers_progress_and_effect_and_cleans_handles(self):
        self.lua.execute('''
            Trig_Draenei_Build_Abill_Actions()
            assert(building.progress == nil and #effects == 0)
            assert(building.removed == 'A0Z3' and #timers == 1)
            timers[1].callback()
            assert(building.progress == 20 and #effects == 1)
            assert(effects[1].destroyed and timers[1].destroyed)
        ''')

    def test_no_proc_without_research_or_successful_roll(self):
        for researched, succeeds in [(False, True), (True, False), (False, False)]:
            with self.subTest(researched=researched, succeeds=succeeds):
                self.lua.globals().researched = researched
                self.lua.globals().succeeds = succeeds
                self.lua.execute('''
                    Trig_Draenei_Build_Abill_Actions()
                    assert(#timers == 0 and #effects == 0)
                    assert(building.progress == nil and building.removed == 'A0Z3')
                ''')

    def test_dead_or_removed_building_skips_proc_and_cleans_timer(self):
        for change in ['building.life = 0', 'building.id = 0']:
            with self.subTest(change=change):
                self.setUp()
                self.lua.execute('Trig_Draenei_Build_Abill_Actions()')
                self.lua.execute(change)
                self.lua.execute('''
                    timers[1].callback()
                    assert(building.progress == nil and #effects == 0)
                    assert(timers[1].destroyed)
                ''')

    def test_concurrent_procs_keep_each_building(self):
        self.lua.execute('''
            local first = building
            Trig_Draenei_Build_Abill_Actions()
            building = {id = 2, life = 100}
            Trig_Draenei_Build_Abill_Actions()
            timers[2].callback()
            timers[1].callback()
            assert(first.progress == 20 and building.progress == 20)
            assert(effects[1].unit == building and effects[2].unit == first)
        ''')


if __name__ == '__main__':
    unittest.main()
