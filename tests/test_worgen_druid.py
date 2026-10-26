"""Лорд друид воргенов: Семя Тал'дорена, Тропа корней, Проклятие Гоэмона, Полнолуние."""
import re
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'
UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_MAGIC_IMMUNE='immune'; UNIT_TYPE_FLYING='flying'
UNIT_TYPE_HERO='hero'; UNIT_TYPE_MECHANICAL='mechanical'
ATTACK_TYPE_NORMAL='normal'; DAMAGE_TYPE_MAGIC='magic'; WEAPON_TYPE_WHOKNOWS='unknown'
EVENT_PLAYER_UNIT_DAMAGING='damaging'; EVENT_PLAYER_UNIT_DEATH='death'
EVENT_PLAYER_UNIT_SPELL_EFFECT='spell'
function FourCC(s) return s end
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u,s) return u[s] end
function SetUnitState(u,s,v) u[s]=math.min(v,u.maxhp) end
function GetOwningPlayer(u) return u.owner end
function IsUnitEnemy(u,p) return u.owner~=p and not (allies[u.owner] and allies[u.owner][p]) end
function IsUnitAlly(u,p) return not IsUnitEnemy(u,p) end
function IsUnitType(u,t) return u[t]==true end
function IsUnitVisible(u,p) return true end
function BlzIsUnitInvulnerable(u) return u.invulnerable==true end
function GetUnitAbilityLevel(u,a) return u.abilities[a] or 0 end
function SetUnitAbilityLevel(u,a,l) u.abilities[a]=l end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function GetHandleId(u) return u.handle end
allies={}; nextHandle=0; now=0
timers={}; casters={}; removed=0; damage={}; effects={}; destroyed=0; orders={}
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,dt,r,fn) t.dt=dt; t.fn=fn end
function TimerGetElapsed(t) return now end
function DestroyTimer(t) assert(not t.destroyed); t.destroyed=true end
function CreateUnit(p,id,x,y,f)
    nextHandle=nextHandle+1
    local u={id=id,owner=p,x=x,y=y,hp=1,maxhp=1,abilities={},handle=nextHandle}
    casters[#casters+1]=u
    return u
end
function IssueTargetOrder(u,o,t) u.order=o; u.target=t; orders[#orders+1]={u=u,o=o,t=t}; return not rejectOrder end
function IssuePointOrder(u,o,x,y) orders[#orders+1]={u=u,o=o,x=x,y=y}; return true end
function IssueImmediateOrder(u,o) orders[#orders+1]={u=u,o=o}; return true end
function RemoveUnit(u) u.id=0; removed=removed+1 end
function RemoveUnitTimed(u,t) end
function AddSpecialEffect(m,x,y) local e={model=m,x=x,y=y,scale=1}; effects[#effects+1]=e; return e end
function AddSpecialEffectTarget(m,u,a) local e={model=m,unit=u}; effects[#effects+1]=e; return e end
function BlzSetSpecialEffectScale(e,s) e.scale=s end
function DestroyEffect(e) e.destroyed=true; destroyed=destroyed+1 end
function UnitDamageTarget(source,target,amount,attack,ranged,at,dt,wt)
    damage[#damage+1]={source=source,target=target,amount=amount,dt=dt}
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
function GetEventDamage() return event.amount end
function BlzSetEventDamage(v) event.amount=v end
function BlzGetEventDamageTarget() return event.target end
function GetTriggerUnit() return event.unit end
function GetSpellAbilityId() return event.ability end
function GetSpellTargetUnit() return event.target end
function GetSpellTargetX() return event.x end
function GetSpellTargetY() return event.y end
triggers={}
function CreateTrigger() return {} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=t end
function TriggerAddAction(t,fn) t.action=fn end

function unit(id,owner,x,y,extra)
    nextHandle=nextHandle+1
    local u={id=id,owner=owner,x=x or 0,y=y or 0,hp=1000,maxhp=1000,abilities={},handle=nextHandle}
    for k,v in pairs(extra or {}) do u[k]=v end
    world[#world+1]=u
    return u
end
function cast(u,ability,target,x,y)
    event={unit=u,ability=ability,target=target,x=x,y=y}
    triggers.spell.action()
end
-- Даммик сразу применяет способность: так ведёт себя nWd1 с нулевой точкой каста.
function resolveDummies()
    for _,c in ipairs(casters) do
        if c.target and not c.resolved then
            c.resolved=true
            if c.order=='bloodlust' then c.target.abilities.BWd2=1; cast(c,'AWd5',c.target) end
            if c.order=='curse' then c.target.abilities.BWd3=c.abilities.AWd6 end
        end
    end
end
function hit(target,amount)
    event={target=target,amount=amount}
    triggers.damaging.action()
    return event.amount
end
function kill(victim)
    victim.hp=0; victim.abilities.BWd2=nil
    event={unit=victim}
    triggers.death.action()
end
function tick(seconds) for i=1,math.floor(seconds/0.05+0.5) do WorgenDruid.timer_fn() end end
'''


def druid_block():
    text = (SECTIONS / '80_runtime/triggers/races/Worgens.lua').read_text(encoding='utf-8')
    match = re.search(r'^WorgenDruid = \{.*?^function InitTrig_WorgenDruid\(\).*?^end', text,
                      re.S | re.M)
    assert match, 'WorgenDruid block not found'
    return match.group(0)


class WorgenDruidTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute(druid_block())
        self.lua.execute('''
            local start = TimerStart
            TimerStart = function(t,dt,r,fn) start(t,dt,r,fn); if t == WorgenDruid.timer then WorgenDruid.timer_fn = fn end end
            InitTrig_WorgenDruid()
        ''')

    def check(self, code):
        self.lua.execute(code)

    def test_init_is_idempotent(self):
        self.check('''
            local spell = triggers.spell
            WorgenDruid.Init()
            assert(triggers.spell == spell)
        ''')

    def test_seed_grows_three_seconds_then_heals_allies_in_200(self):
        self.check('''
            allies[1]={[3]=true}; allies[3]={[1]=true}
            druid = unit('H0J6',1,0,0,{abilities={AWd1=2}})
            near = unit('hfoo',1,100,0,{hp=100}); ally = unit('hfoo',3,0,150,{hp=100})
            far = unit('hfoo',1,300,0,{hp=100}); foe = unit('hfoo',2,50,0,{hp=100})
            tower = unit('htow',1,0,50,{hp=100,structure=true})
            cast(druid,'AWd1',nil,0,0)
            local seed = effects[1]
            assert(seed.scale==0.5 and seed.model:find('TalDorenSeed'))
            tick(1.5)
            assert(math.abs(seed.scale-0.75)<1e-9 and near.hp==100)
            tick(1.5)
            assert(seed.destroyed and near.hp==290 and ally.hp==290)
            assert(far.hp==100 and foe.hp==100 and tower.hp==100)
            assert(#WorgenDruid.seeds==0 and WorgenDruid.timer==nil)
            assert(effects[2].model:find('NECancelDeath'))
        ''')

    def test_seed_heals_at_most_eight_heroes_first_then_most_wounded(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd1=1}})
            hero = unit('Hpal',1,10,0,{hp=990,hero=true})
            wounded = {}
            for i = 1, 12 do wounded[i] = unit('hfoo',1,i,0,{hp=1000-i*10}) end
            cast(druid,'AWd1',nil,0,0)
            tick(3)
            assert(hero.hp==1000)
            for i = 6, 12 do assert(wounded[i].hp==math.min(1000,1000-i*10+120), i) end
            for i = 1, 5 do assert(wounded[i].hp==1000-i*10, i) end
            local fx = 0
            for _,e in ipairs(effects) do if e.unit and e.model:find('Rejuvenation') then fx = fx + 1; assert(not e.destroyed) end end
            assert(fx==8)
        ''')

    def test_trail_drops_six_vines_and_damages_once_per_step(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd2=3}})
            foe = unit('hfoo',2,0,0); bird = unit('hgry',2,0,0,{flying=true})
            cast(druid,'AWd2')
            assert(#effects==1 and #damage==0)
            tick(0.5)
            -- Две лозы под одним врагом: урон один раз за шаг.
            assert(#effects==2 and #damage==1 and damage[1].target==foe and damage[1].amount==11)
            for i=1,4 do druid.x = druid.x + 1000; tick(0.5) end
            assert(#effects==6)
            druid.x = druid.x + 1000; tick(0.5)
            assert(#effects==6)
            -- Лозы шагов 0 и 1 живут по 5 сек.: вместе ранят foe на шагах 1..11.
            tick(2.5)
            assert(#damage==11)
            tick(3)
            assert(#WorgenDruid.trails==0 and destroyed==6 and WorgenDruid.timer==nil)
        ''')

    def test_trail_stops_dropping_when_druid_dies(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd2=1}})
            cast(druid,'AWd2'); druid.hp=0
            tick(5.5)
            assert(#effects==1 and #WorgenDruid.trails==0)
        ''')

    def test_curse_amplifies_damage_and_jumps_on_death(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd3=1}})
            target = unit('hfoo',2,500,0); near = unit('hfoo',2,700,0); closer = unit('hfoo',2,600,0)
            unit('Hpal',2,550,0,{hero=true}); unit('hmtm',2,520,0,{mechanical=true})
            cast(druid,'AWd3',target); resolveDummies()
            assert(casters[1].id=='nWd1' and casters[1].owner==1 and casters[1].order=='bloodlust')
            assert(hit(target,100)==150 and hit(near,100)==100)
            kill(target); resolveDummies()
            assert(casters[2].target==closer and casters[2].owner==1)
            assert(hit(closer,100)==150)
        ''')

    def test_expired_curse_does_not_jump(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd3=1}})
            target = unit('hfoo',2,0,0); unit('hfoo',2,100,0)
            cast(druid,'AWd3',target); resolveDummies()
            now = 10.5
            kill(target)
            assert(#casters==1 and WorgenDruid.markCount==0)
        ''')

    def test_moon_curses_enemies_and_heals_allies_except_mechanical(self):
        self.check('''
            druid = unit('H0J6',1,0,0,{abilities={AWd4=2},hp=500})
            ally = unit('hfoo',1,1000,0,{hp=100}); golem = unit('hmtm',1,100,0,{hp=100,mechanical=true})
            foe = unit('hfoo',2,800,0); hero = unit('Hpal',2,0,900,{hero=true})
            robot = unit('hmtm',2,100,0,{mechanical=true}); far = unit('hfoo',2,1300,0)
            immune = unit('hfoo',2,0,100,{immune=true})
            cast(druid,'AWd4')
            assert(druid.hp==750 and ally.hp==350 and golem.hp==100)
            assert(#casters==2 and casters[1].order=='curse' and casters[1].abilities.AWd6==2)
            local targets = {[casters[1].target]=true, [casters[2].target]=true}
            assert(targets[foe] and targets[hero])
        ''')

    def test_ai_seed_targets_most_wounded_ally(self):
        self.check('''
            druid = unit('H0J6',1,0,0)
            unit('hfoo',1,100,0,{hp=950}); hurt = unit('hfoo',1,200,0,{hp=300})
            assert(WorgenDruid.AiSeed(druid))
            assert(orders[1].o=='channel' and orders[1].x==200)
        ''')

    def test_ai_curse_skips_heroes_and_moon_needs_crowd(self):
        self.check('''
            druid = unit('H0J6',1,0,0)
            hero = unit('Hpal',2,100,0,{hero=true}); big = unit('hkni',2,200,0,{maxhp=1500})
            assert(WorgenDruid.AiCurse(druid, hero) and orders[1].t==big and orders[1].o=='curse')
            assert(not WorgenDruid.AiMoon(druid))
            for i=1,6 do unit('hfoo',2,i*10,0) end
            assert(WorgenDruid.AiMoon(druid) and orders[2].o=='starfall')
        ''')


if __name__ == '__main__':
    unittest.main()
