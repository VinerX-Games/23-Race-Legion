"""Огры: Пригвоздить, Нарастающая ярость, Поступь гронна и Пиршество."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'
UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_MAGIC_IMMUNE='immune'; UNIT_TYPE_FLYING='flying'
UNIT_TYPE_WARD='ward'
ATTACK_TYPE_CHAOS='chaos'; DAMAGE_TYPE_UNIVERSAL='universal'; WEAPON_TYPE_WHOKNOWS='unknown'
EVENT_PLAYER_UNIT_DAMAGING='damaging'; EVENT_PLAYER_UNIT_DEATH='death'
function FourCC(s) return s end
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u,s) return u[s] end
function SetUnitState(u,s,v) u[s]=math.min(v,u.maxhp) end
function BlzGetUnitMaxHP(u) return u.maxhp end
function BlzSetUnitMaxHP(u,v) u.maxhp=v end
function GetOwningPlayer(u) return u.owner end
function IsUnitEnemy(u,p) return u.owner~=p end
function IsUnitType(u,t) return u[t]==true end
function IsUnitIllusion(u) return u.illusion==true end
function IsUnitHidden(u) return u.hidden==true end
function IsUnitPaused(u) return u.paused==true end
function IsUnitLoaded(u) return u.loaded==true end
function BlzIsUnitInvulnerable(u) return u.invulnerable==true end
function GetUnitAbilityLevel(u,a) return u.abilities[a] or 0 end
function SetUnitAbilityLevel(u,a,l) u.abilities[a]=l end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
tech={}
function GetPlayerTechCount(p,id,s) return (tech[p] and tech[p][id]) or 0 end
timers={}; destroyedTimers=0; casters={}; removed=0; timedRemoved=0; damage={}; effects=0
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,dt,r,fn) t.dt=dt; t.fn=fn end
function DestroyTimer(t) assert(not t.destroyed); t.destroyed=true; destroyedTimers=destroyedTimers+1 end
function CreateUnit(p,id,x,y,f)
    local u={id=id,owner=p,x=x,y=y,hp=1,maxhp=1,abilities={}}
    casters[#casters+1]=u
    return u
end
function IssueTargetOrder(u,o,t) u.order=o; u.target=t; return not rejectOrder end
function IssueImmediateOrder(u,o) u.order=o; return not rejectOrder end
function RemoveUnit(u) u.id=0; removed=removed+1 end
function RemoveUnitTimed(u,t) assert(t==2.0); timedRemoved=timedRemoved+1 end
function AddSpecialEffect() effects=effects+1; return {} end
function AddSpecialEffectTarget() effects=effects+1; return {} end
function DestroyEffect(e) end
function UnitDamageTarget(source,target,amount,attack,ranged,at,dt,wt)
    damage[#damage+1]={source=source,target=target,amount=amount,attack=attack,at=at,dt=dt}
    return true
end
world={}
function CreateGroup() return {} end
function DestroyGroup(g) g.destroyed=true end
function GroupEnumUnitsInRange(g,x,y,r,f)
    assert(f==nil)
    for _,u in ipairs(world) do
        if (u.x-x)^2+(u.y-y)^2<=r*r then g[#g+1]=u end
    end
end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
-- Damage event state.
function GetEventDamage() return event.amount end
function BlzSetEventDamage(v) event.amount=v end
function GetEventDamageSource() return event.source end
function BlzGetEventDamageTarget() return event.target end
function BlzGetEventIsAttack() return event.attack end
function GetKillingUnit() return event.killer end
function GetTriggerUnit() return event.unit end
triggers={}
function CreateTrigger() return {} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=t end
function TriggerRegisterEnterRegion(t,r,f) triggers.enter=t end
function TriggerAddAction(t,fn) t.action=fn end
function GetWorldBounds() return {} end
function RemoveRect(r) end
function CreateRegion() return {} end
function RegionAddRect(g,r) end

function unit(id,owner,x,y,extra)
    local u={id=id,owner=owner,x=x or 0,y=y or 0,hp=1000,maxhp=1000,abilities={}}
    for k,v in pairs(extra or {}) do u[k]=v end
    world[#world+1]=u
    return u
end
function attack(source,target,amount,isAttack)
    event={source=source,target=target,amount=amount or 100,attack=isAttack~=false}
    triggers.damaging.action()
    return event.amount
end
function kill(killer,victim)
    event={killer=killer,unit=victim}
    triggers.death.action()
end
function enter(u) event={unit=u}; triggers.enter.action() end
function tick(seconds) for i=1,math.floor(seconds/0.25+0.5) do OgreCombat.timer_fn() end end
'''


class OgreCombatTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute((SECTIONS / '80_runtime/triggers/races/Ogres.lua').read_text(encoding='utf-8'))
        self.lua.execute('''
            InitTrig_OgreCombat()
            local start = TimerStart
            TimerStart = function(t,dt,r,fn) start(t,dt,r,fn); OgreCombat.timer_fn = fn end
        ''')

    def check(self, code):
        self.lua.execute(code)

    def test_init_is_idempotent(self):
        self.check('''
            local damaging = triggers.damaging
            OgreCombat.Init()
            assert(triggers.damaging == damaging)
        ''')

    def test_every_fifth_throw_pins_and_counter_restarts(self):
        self.check('''
            spear = unit('o03H',1,0,0,{abilities={AOg1=1}}); foe = unit('hfoo',2,500,0)
            for i=1,4 do attack(spear,foe) end
            assert(spear.abilities.AOg1==5 and #casters==0)
            attack(spear,foe)
            assert(spear.abilities.AOg1==1 and #casters==1)
            local c = casters[1]
            assert(c.id=='nOg1' and c.owner==1 and c.order=='ensnare' and c.target==foe)
            assert(c.x==0 and c.y==0 and timedRemoved==1)
        ''')

    def test_pin_ignores_buildings_immune_spells_and_allies(self):
        self.check('''
            spear = unit('o03H',1,0,0,{abilities={AOg1=1}})
            attack(spear, unit('o03A',2,100,0,{structure=true}))
            attack(spear, unit('hfoo',2,100,0,{immune=true}))
            attack(spear, unit('hfoo',1,100,0))
            attack(spear, unit('hfoo',2,100,0), 100, false)
            assert(spear.abilities.AOg1==1 and #casters==0)
        ''')

    def test_pin_failed_order_removes_caster_at_once(self):
        self.check('''
            rejectOrder=true
            spear = unit('o03H',1,0,0,{abilities={AOg1=5}}); foe = unit('hfoo',2,500,0)
            attack(spear,foe)
            assert(removed==1 and timedRemoved==0 and spear.abilities.AOg1==1)
        ''')

    def test_rage_scales_with_missing_life_only_after_research(self):
        self.check('''
            ogron = unit('o03Q',1,0,0,{abilities={AOg2=1},hp=500}); foe = unit('hfoo',2,100,0)
            assert(attack(ogron,foe,100)==100)
            tech[1]={ROg2=1}
            assert(math.abs(attack(ogron,foe,100)-110)<1e-9)
            ogron.hp=1000; assert(attack(ogron,foe,100)==100)
            ogron.hp=901; assert(attack(ogron,foe,100)==100)
            ogron.hp=900; assert(math.abs(attack(ogron,foe,100)-102)<1e-9)
            ogron.hp=1; assert(math.abs(attack(ogron,foe,100)-118)<1e-9)
            ogron.hp=500; assert(attack(ogron,foe,100,false)==100)
        ''')

    def test_feast_adds_life_per_enemy_kill_up_to_150(self):
        self.check('''
            ogre = unit('o03I',1,0,0,{abilities={AOg4=1},hp=900})
            kill(ogre, unit('hfoo',2))
            assert(ogre.abilities.AOg4==1 and ogre.maxhp==1000)
            tech[1]={ROg4=1}
            kill(ogre, unit('hfoo',2))
            assert(ogre.abilities.AOg4==2 and ogre.maxhp==1015 and ogre.hp==915)
            kill(ogre, unit('o03A',2,0,0,{structure=true}))
            kill(ogre, unit('hfoo',1))
            kill(ogre, unit('hfoo',2,0,0,{illusion=true}))
            kill(ogre, unit('oeye',2,0,0,{ward=true}))
            assert(ogre.abilities.AOg4==2)
            for i=1,20 do kill(ogre, unit('hfoo',2)) end
            assert(ogre.abilities.AOg4==11 and ogre.maxhp==1150)
        ''')

    def test_feast_skips_dead_killer(self):
        self.check('''
            tech[1]={ROg4=1}
            ogre = unit('o03I',1,0,0,{abilities={AOg4=1},hp=0})
            kill(ogre, unit('hfoo',2))
            assert(ogre.abilities.AOg4==1 and ogre.maxhp==1000)
        ''')

    def test_stride_damages_buildings_and_slows_units_every_six_seconds(self):
        self.check('''
            gronn = unit('o03T',1,0,0,{abilities={AOg3=1}}); enter(gronn)
            tower = unit('o038',2,200,0,{structure=true})
            foe = unit('hfoo',2,0,240)
            unit('hfoo',2,0,300); unit('o038',1,10,0,{structure=true})
            tick(0.25)
            assert(#damage==1 and damage[1].target==tower and damage[1].amount==30)
            assert(not damage[1].attack and damage[1].at=='chaos' and damage[1].dt=='universal')
            assert(#casters==1 and casters[1].order=='thunderclap' and casters[1].x==0)
            tick(5.75); assert(#damage==1)
            tick(0.25); assert(#damage==2 and #casters==2)
        ''')

    def test_stride_waits_for_ground_enemies(self):
        self.check('''
            gronn = unit('o03U',1,0,0,{abilities={AOg3=1}}); enter(gronn)
            unit('hgry',2,50,0,{flying=true}); unit('hfoo',1,50,0)
            tick(3); assert(#damage==0 and #casters==0 and effects==0)
            unit('hfoo',2,50,0)
            tick(0.25); assert(#casters==1 and #damage==0)
        ''')

    def test_stride_only_buildings_does_not_cast_slow(self):
        self.check('''
            gronn = unit('o03V',1,0,0,{abilities={AOg3=1}}); enter(gronn)
            unit('o038',2,100,0,{structure=true})
            tick(0.25); assert(#damage==1 and #casters==0 and effects==1)
        ''')

    def test_tracking_ignores_others_and_releases_timer(self):
        self.check('''
            enter(unit('o03I',1,0,0,{abilities={AOg4=1}}))
            assert(#OgreCombat.gronns==0 and OgreCombat.timer==nil)
            gronn = unit('o03T',1,0,0,{abilities={AOg3=1}}); enter(gronn); enter(gronn)
            assert(#OgreCombat.gronns==1 and OgreCombat.timer~=nil)
            gronn.hp=0; tick(1); assert(#OgreCombat.gronns==1)
            gronn.id=0; tick(0.25)
            assert(#OgreCombat.gronns==0 and OgreCombat.timer==nil and destroyedTimers==1)
        ''')

    def test_disabled_gronn_does_not_stomp(self):
        self.check('''
            gronn = unit('o03T',1,0,0,{abilities={AOg3=1},paused=true}); enter(gronn)
            unit('hfoo',2,50,0)
            tick(1); assert(#casters==0)
            gronn.paused=false; tick(0.25); assert(#casters==1)
        ''')


if __name__ == '__main__':
    unittest.main()
