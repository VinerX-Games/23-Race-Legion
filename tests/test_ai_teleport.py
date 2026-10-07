import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tmp' / 'teleport-test-runtime'))
from lupa.lua53 import LuaRuntime

SECTIONS = ROOT / 'map.w3x/_lua/monolith_split/sections'

FIXTURE = r'''
function FourCC(s) return s end
function Player(i) return i end
function GetPlayerId(p) return p end
function GetOwningPlayer(u) return u.owner end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function GetUnitTypeId(u) return u.id end
function UnitAlive(u) return u ~= nil and not u.dead end
function GetUnitAbilityLevel(u, id) return u.abilities[id] or 0 end
function UnitAddAbility(u, id) u.abilities[id] = 1 end
function AddAbilityTimed(u, id) UnitAddAbility(u, id) end
function GetRandomInt(a, b) assert(b >= a, 'empty random range'); return a end
function Random() return false end
function CreateGroup() return {} end
function DestroyGroup() end
function GroupClear(g) for k in pairs(g) do g[k] = nil end end
function GroupAddUnit(g, u) assert(u); g[#g+1] = u end
function GroupRemoveUnit(g, u) for i=#g,1,-1 do if g[i]==u then table.remove(g,i) end end end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g, i) return g[i+1] end
function FirstOfGroup(g) return g[1] end
function GroupPickRandomUnit2(g) return g[1] end
function IsUnitInGroup(u, g) for _,v in ipairs(g) do if v==u then return true end end; return false end
function IsUnitType(u) return u.building end
UNIT_TYPE_STRUCTURE = 1
function Condition(f) return f end
function newUnit(owner, id, x, y, building)
    local u={owner=owner,id=id,x=x or 100,y=y or 200,building=building,abilities={}}
    units[#units+1]=u; return u
end
function CreateUnit(p,id,x,y) local u=newUnit(p,id,x,y); created[#created+1]=u; return u end
function GroupEnumUnitsInRange(g,x,y,r,filter)
    GroupClear(g)
    for _,u in ipairs(units) do
        filterUnit=u
        if not filter or filter() then GroupAddUnit(g,u) end
    end
end
function GetFilterUnit() return filterUnit end
function GroupEnumUnitsOfPlayer(g,p,filter)
    GroupClear(g)
    for _,u in ipairs(units) do
        if u.owner==p then
            filterUnit=u
            if not filter or filter() then GroupAddUnit(g,u) end
        end
    end
end
function IssuePointOrder(u,order,x,y)
    assert(u); orders[#orders+1]={u=u,order=order,x=x,y=y}
    gUnit=foreign; gPi=0; gPlayer=0; gUnit2=foreign
end
function AddSpecialEffect() end
function RemoveEffectTimed() end
function NumberAdd(pi,id) counts[pi]=(counts[pi] or 0)+1 end
units={}; created={}; orders={}; counts={}
udg_AiControl={[0]=false,[3]=true}
udg_Ai_army={[0]={},[3]={}}; AiUnitsToPort={[0]={},[3]={}}
udg_ZahvatBuildings={}; gGroup={}; AiData={[0]={},[3]={}}
gMageTP='h07A'; AiRace={}; AiRaces={}
function lazy() if GetFilterUnit().combat then LazyCount=(LazyCount or 0)+1; return true end; return false end
B_Lazy=lazy; B_InAiArmy=lazy; Altars=function() return GetFilterUnit().building end
dest=newUnit(3,'town',100,200,true)
target=newUnit(3,'soldier',900,1000); target.combat=true
udg_Ai_army[3]={target}
function IsAiCombatRetaskable(u) return u.combat == true end
foreign=newUnit(0,'human',150,250)
gUnit=foreign; gAttacked=dest; TryPort_pi=3
'''


class AiTeleportTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute((SECTIONS / '80_runtime/_infra/40_bool_exprs.lua').read_text('utf-8'))
        self.lua.execute('b_OwnBuldingsInRange=Condition(f_OwnBuildingsInRange)')
        self.lua.execute((SECTIONS / 'libraries/11_LibDifferentAiStuff.lua').read_text('utf-8'))
        self.lua.execute('function NumberAdd(pi,id) counts[pi]=(counts[pi] or 0)+1 end')

    def check(self, code):
        self.lua.execute(code)

    def test_building_is_spawn_location_not_caster_and_foreign_unit_is_untouched(self):
        self.check('''MakeTPMage(dest,target,3)
            assert(#created==1, 'must create a mage even when a building exists')
            assert(created[1].owner==3 and created[1].id=='h07A')
            assert(orders[1].u==created[1])
            assert(IsUnitInGroup(created[1],udg_Ai_army[3]) and AiUnitsToPort[3][1]==created[1])
            assert(not IsUnitInGroup(foreign,udg_Ai_army[3]))''')

    def test_human_destination_cannot_spawn_mage_or_issue_orders(self):
        self.check('PortTo(foreign); PortToFast(foreign); MakeTPMage(foreign,target,0); MakeMageTp(0); assert(#created==0 and #orders==0)')

    def test_empty_army_does_not_spawn_or_order(self):
        self.check('udg_Ai_army[3]={}; PortTo(dest); PortToFast(dest); assert(#created==0 and #orders==0)')

    def test_mage_cap_and_destination_cooldown_prevent_extra_spawns(self):
        self.check("g_AiCounts[3]={h07A=10}; MakeTPMage(dest,target,3); assert(#created==0); g_AiCounts[3]={}; dest.abilities.A1RD=1; MakeTPMage(dest,target,3); assert(#created==0)")

    def test_foreign_summon_target_is_rejected(self):
        self.check('MakeTPMage(dest,foreign,3); assert(#created==0 and #orders==0)')

    def test_fast_teleport_uses_passed_city_not_global_attacked_unit(self):
        self.check("udg_ZahvatBuildings={dest}; gAttacked=foreign; PortToFast(dest); assert(#orders==1 and orders[1].u==dest and #created==0)")

    def test_no_enemy_does_not_start_teleport(self):
        self.check('AiUnitsToPort[3]={dest}; function HasEnemyNear() return false end; TryPort(); RequestPort(dest); assert(#created==0 and #orders==0)')

    def test_contaminated_group_cannot_teleport_human_units(self):
        self.check('AiUnitsToPort[3]={foreign}; function HasEnemyNear() return true end; TryPort(); RequestPort(dest); assert(#created==0 and #orders==0)')

    def test_city_teleport_keeps_bot_context_during_nested_orders(self):
        self.check('''udg_ZahvatBuildings={dest}; function Random() return true end; PortTo(dest)
            assert(#created==1 and created[1].owner==3)
            assert(#udg_Ai_army[0]==0 and #AiUnitsToPort[0]==0)
            assert(orders[2].u==created[1] and orders[2].x==900)''')


class BridgeDefaultTests(unittest.TestCase):
    def test_default_bridge_does_not_start_timer_or_touch_preload_channel(self):
        lua = LuaRuntime()
        lua.execute('function FourCC(s) return s end; function Player(i) return i end; touched=0; function BlzGetAbilityTooltip() touched=touched+1; return "baseline" end; function CreateTimer() touched=touched+1; return {} end; function TimerStart() end; function ProbeLogWrite() end; function GetLocalPlayer() return 0 end; function GetPlayerId(p) return p end; function PreloadGenClear() touched=touched+1 end; function PreloadGenStart() end; function Preload() end; function PreloadGenEnd() end; function CreateTrigger() return {} end; function BlzTriggerRegisterPlayerSyncEvent() end; function TriggerAddAction() end')
        lua.execute((SECTIONS / '00_prelude.lua').read_text('utf-8'))
        lua.execute('function BlzSetAbilityTooltip() touched=touched+1 end')
        lua.execute('BridgeStart(); assert(BridgePollTimer==nil and touched==0, "release bridge must be dormant")')


if __name__ == '__main__':
    unittest.main()
