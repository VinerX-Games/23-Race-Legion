"""Взаимоисключающие ветки Орды: вторая ветка из очереди отменяется при старте."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
function FourCC(s) return s end
function GetOwningPlayer(u) return u.owner end
function GetPlayerId(p) return p end
function GetTriggerUnit() return building end
function GetResearched() return research end
limits={}; tech={}; orders={}; triggers={}
udg_MainPrice=setmetatable({}, {__index=function() return 0 end})
function SetPlayerTechMaxAllowed(p,id,n) limits[id]=n end
function SetPlayerTechMaxAllowedSwap(id,n,p) limits[id]=n end
function GetPlayerTechMaxAllowedSwap(id,p) return limits[id] or -1 end
function GetPlayerTechCount(p,id,s) return tech[id] or 0 end
function IssueImmediateOrderById(u,o) orders[#orders+1]=o; return true end
function CreateTrigger() return {} end
function TriggerRegisterAnyUnitEventBJ(t,kind)
    triggers[kind]=triggers[kind] or {}; table.insert(triggers[kind],t)
end
function TriggerAddAction(t,f) t.action=f end
function fire(kind,id)
    building={owner=0}; research=id
    for _,t in ipairs(triggers[kind] or {}) do t.action() end
end

EVENT_PLAYER_UNIT_RESEARCH_START='start'
EVENT_PLAYER_UNIT_RESEARCH_CANCEL='cancel'
EVENT_PLAYER_UNIT_RESEARCH_FINISH='finish'
'''


class HordeBranchTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute(FIXTURE)
        self.lua.execute((SECTIONS / '80_runtime/triggers/races/Horde.lua').read_text(encoding='utf-8-sig'))
        self.lua.execute("function countAll(p) end; InitTrig_HordeResearch(); tech['R0EE']=1; tech['R0E0']=1")

    def test_queued_rival_is_cancelled_after_first_branch_finishes(self):
        self.lua.execute('''
            fire('start','R0EH'); tech['R0EH']=1; fire('finish','R0EH')
            fire('start','R0E9')
            assert(#orders==1 and orders[1]==851976)
            assert(HordeResearch.pending[0]['R0E9']==nil)
            fire('cancel','R0E9')
            assert(limits['R0E9']==0 and limits['R0EI']==0)
        ''')

    def test_queued_rival_is_cancelled_while_first_is_researching(self):
        self.lua.execute('''
            fire('start','R0E9'); fire('start','R0EI')
            assert(#orders==1)
            assert(HordeResearch.pending[0]['R0E9']==true)
        ''')

    def test_iron_and_sha_are_rivals(self):
        self.lua.execute('''
            tech['R0E9']=1; tech['R0EA']=1; fire('finish','R0EA')
            fire('start','R0KO')
            assert(#orders==1 and limits['R0KO']==0)
        ''')

    def test_first_branch_starts_without_cancel(self):
        self.lua.execute('''
            fire('start','R0EH')
            assert(#orders==0 and HordeResearch.pending[0]['R0EH']==true)
            assert(limits['R0E9']==0 and limits['R0EI']==0)
        ''')


if __name__ == '__main__':
    unittest.main()
