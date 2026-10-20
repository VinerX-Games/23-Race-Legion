"""Мутация и Гарпун (наги), Пьянящая настойка (пандарены), Память Аргуса (дренеи), Делёж добычи (бандиты)."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
RACES = SECTIONS / '80_runtime/triggers/races'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'
UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_FLYING='flying'; UNIT_TYPE_WARD='ward'
UNIT_TYPE_HERO='hero'; UNIT_TYPE_RANGED_ATTACKER='ranged'; UNIT_TYPE_SUMMONED='summoned'
ATTACK_TYPE_NORMAL='normal'; DAMAGE_TYPE_NORMAL='normal'; WEAPON_TYPE_WHOKNOWS='unknown'
PATHING_TYPE_FLOATABILITY='float'; PATHING_TYPE_WALKABILITY='walk'
PLAYER_STATE_RESOURCE_GOLD='gold'
EVENT_PLAYER_UNIT_SPELL_EFFECT='spell'; EVENT_PLAYER_UNIT_DEATH='death'
EVENT_PLAYER_UNIT_DAMAGING='damaging'
function FourCC(s) return s end
gDummy='h05P'
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u,s) return u[s] end
function SetUnitState(u,s,v) u[s]=math.min(v,u.maxhp) end
function GetOwningPlayer(u) return u.owner end
function IsUnitEnemy(u,p) return u.owner~=p end
function IsUnitVisible(u,p) return true end
function IsUnitType(u,t) return u[t]==true end
function IsUnitIllusion(u) return u.illusion==true end
function IsUnitHidden(u) return false end
function IsUnitLoaded(u) return false end
function BlzIsUnitInvulnerable(u) return false end
function GetUnitAbilityLevel(u,a) return u.abilities[a] or 0 end
function UnitAddAbility(u,a) u.abilities[a]=1 end
function UnitRemoveAbility(u,a) u.abilities[a]=nil end
function UnitAddType(u,t) u[t]=true end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function SetUnitX(u,x) u.x=x end
function SetUnitY(u,y) u.y=y end
function GetUnitFacing(u) return 0 end
function GetHandleId(u) return u.handle end
function BlzGetUnitBaseDamage(u,i) return u.damage end
function BlzSetUnitBaseDamage(u,v,i) u.damage=v end
function BlzGetUnitArmor(u) return u.armor end
function BlzSetUnitArmor(u,v) u.armor=v end
function BlzGetUnitAbilityCooldownRemaining(u,a) return 0 end
function BlzEndUnitAbilityCooldown(u,a) u.cooldownReset=true end
water=false; blocked=false
function IsTerrainPathable(x,y,t)
    if t=='float' then return not water end
    return blocked
end
function CreateItem(id,x,y) return {x=x,y=y} end
function SetItemVisible(i,v) end
function SetItemPosition(i,x,y) i.x=x; i.y=y end
function GetItemX(i) return i.x end
function GetItemY(i) return i.y end
function AddLightning() return {} end
function MoveLightning() end
function DestroyLightning(l) l.destroyed=true end
tech={}
function GetPlayerTechCount(p,id,s) return (tech[p] and tech[p][id]) or 0 end
rolls={}
function GetRandomInt(a,b) return table.remove(rolls,1) or a end
timers={}
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,dt,r,fn) t.dt=dt; t.fn=fn end
function DestroyTimer(t) t.destroyed=true end
damage={}; created={}; orders={}; gold={}
function UnitDamageTarget(s,t,a) damage[#damage+1]={source=s,target=t,amount=a}; t.hp=t.hp-a; return true end
function AddSpecialEffect() return {} end
function AddSpecialEffectTarget() return {} end
function DestroyEffect(e) end
function BlzSetSpecialEffectZ() end
function BlzSetSpecialEffectYaw() end
function BlzSetSpecialEffectPosition() end
function Location(x,y) return {} end
function MoveLocation() end
function GetLocationZ() return 0 end
function Atan2(y,x) return 0 end
function SetUnitVertexColor() end
function UnitApplyTimedLife(u,b,d) u.timed=d end
function IssuePointOrder(u,o,x,y) orders[#orders+1]={u=u,o=o}; return true end
function IssueTargetOrder(u,o,t) u.order=o; u.target=t; return true end
function IssueImmediateOrder(u,o) u.order=o; return true end
function RemoveUnitTimed() end
function CreateUnit(p,id,x,y,f)
    local u=unit(id,p,x,y); created[#created+1]=u; return u
end
function GetPlayerState(p,s) return gold[p] or 0 end
function SetPlayerState(p,s,v) gold[p]=v end
function CreateTextTag() return {} end
function SetTextTagText() end
function SetTextTagPos() end
function SetTextTagVelocity() end
function SetTextTagPermanent() end
function SetTextTagLifespan() end
function SetTextTagFadepoint() end
function SetTextTagVisibility() end
function GetLocalPlayer() return 1 end
world={}
function CreateGroup() return {} end
function DestroyGroup(g) end
function GroupEnumUnitsInRange(g,x,y,r,f)
    for _,u in ipairs(world) do if (u.x-x)^2+(u.y-y)^2<=r*r then g[#g+1]=u end end
end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
triggers={}
function CreateTrigger() return {actions={}} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=triggers[e] or {}; table.insert(triggers[e],t) end
function TriggerRegisterEnterRegion(t) triggers.enter=triggers.enter or {}; table.insert(triggers.enter,t) end
function TriggerAddAction(t,fn) t.action=fn end
function GetWorldBounds() return {} end
function RemoveRect() end
function CreateRegion() return {} end
function RegionAddRect() end
function GetTriggerUnit() return event.unit end
function GetKillingUnit() return event.killer end
function GetSpellAbilityId() return event.ability end
function GetSpellTargetUnit() return event.target end
function fire(kind) for _,t in ipairs(triggers[kind] or {}) do t.action() end end
handles=0
function unit(id,owner,x,y,extra)
    handles=handles+1
    local u={id=id,owner=owner,x=x or 0,y=y or 0,hp=500,maxhp=1000,abilities={},damage=30,armor=1,handle=handles}
    for k,v in pairs(extra or {}) do u[k]=v end
    world[#world+1]=u
    return u
end
function kill(killer,victim) victim.hp=0; event={killer=killer,unit=victim}; fire('death') end
function cast(caster,ability,target) event={unit=caster,ability=ability,target=target}; fire('spell') end
function enter(u) event={unit=u}; fire('enter') end
DraeneiCombat={}
GAME_STATE_TIME_OF_DAY='tod'; ATTACK_TYPE_SIEGE='siege'; daytime=0
function GetFloatGameState(s) return daytime end
function BlzGetUnitDiceNumber(u,i) return 1 end
function BlzGetUnitDiceSides(u,i) return 3 end
function GetEventDamageSource() return event.source end
function BlzGetEventDamageTarget() return event.target end
function BlzGetEventIsAttack() return event.attack end
function hit(source,target) event={source=source,target=target,attack=true}; fire('damaging') end
'''


class UnitMechanicsTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        for name in ['Naga.lua', 'Pandarens.lua', 'Bandits.lua', 'Nightborne.lua']:
            source = (RACES / name).read_text(encoding='utf-8')
            if name in ('Naga.lua', 'Bandits.lua'):
                # Берём только новые модули: legacy-триггеры файлов зависят от GUI-нативов.
                marker = {'Naga.lua': 'NagaCombat = {', 'Bandits.lua': 'BanditLoot = {'}[name]
                source = source[source.index(marker):]
            self.lua.execute(source)
        draenei = (RACES / 'Draenei.lua').read_text(encoding='utf-8')
        start = draenei.index('DraeneiCombat = {')
        self.lua.execute(draenei[start:draenei.index('\nfunction DraeneiCombat.InMemoryField')])
        argus = draenei.index('function DraeneiCombat.ArgusDeath()')
        self.lua.execute(draenei[argus:draenei.index('\nfunction DraeneiCombat.AiVow')])
        self.lua.execute('''
            NagaCombat.Init(); PandarenBrew.Init(); BanditLoot.Init(); NightborneGlaive.Init()
            TriggerRegisterAnyUnitEventBJ(CreateTrigger(), 'death')
            triggers.death[#triggers.death].action = DraeneiCombat.ArgusDeath
        ''')

    def check(self, code):
        self.lua.execute(code)

    def test_mutation_rolls_once_and_applies_bonus(self):
        self.check('''
            rolls={1}; local a=unit('n050',1,0,0,{abilities={AMu1=1}}); enter(a)
            assert(a.abilities.AMu2==1 and a.abilities.AMu1==nil and a.damage==38)
            enter(a); assert(a.damage==38)
            rolls={2}; local b=unit('n050',1,0,0,{abilities={AMu1=1}}); enter(b)
            assert(b.abilities.AMu3==1 and b.armor==4)
        ''')

    def test_gills_heal_only_in_water(self):
        self.check('''
            rolls={3}; local m=unit('n050',1,0,0,{abilities={AMu1=1}}); enter(m)
            local t=timers[#timers]; assert(t.dt==0.5)
            water=false; t.fn(); assert(m.hp==500)
            water=true; t.fn(); assert(m.hp==504)
            m.id=0; t.fn(); assert(t.destroyed and NagaCombat.regenTimer==nil)
        ''')

    def test_harpoon_damages_and_pulls_with_hero_cap(self):
        self.check('''
            local h=unit('n056',1,0,0); local foe=unit('hfoo',2,500,0)
            cast(h,'AMh1',foe)
            assert(damage[1].amount==40 and damage[1].target==foe)
            local t=timers[#timers]
            for i=1,20 do if not t.destroyed then t.fn() end end
            assert(math.abs(foe.x-200)<0.01 and t.destroyed)
            local hero=unit('Hpal',2,500,0,{hero=true})
            cast(h,'AMh1',hero); t=timers[#timers]
            for i=1,20 do if not t.destroyed then t.fn() end end
            assert(math.abs(hero.x-350)<0.01)
            local near=unit('hfoo',2,120,0)
            cast(h,'AMh1',near); assert(near.x==120)  -- не ближе зазора
        ''')

    def test_harpoon_rejects_buildings_and_resets_cooldown(self):
        self.check('''
            local h=unit('n056',1,0,0); local b=unit('hbar',2,300,0,{structure=true})
            cast(h,'AMh1',b); assert(#damage==0 and h.cooldownReset)
        ''')

    def test_ai_harpoon_prefers_far_hero(self):
        self.check('''
            local h=unit('n056',1,0,0); tech[1]={R0FP=1}
            unit('hfoo',2,100,0); local far=unit('hfoo',2,400,0); local hero=unit('Hpal',2,0,450,{hero=true})
            assert(NagaCombat.AiHarpoon(h) and h.target==hero and h.order=='acidbomb')
            tech[1]={}; h.target=nil; assert(not NagaCombat.AiHarpoon(h))
        ''')

    def test_barrel_applies_effect_on_impact(self):
        self.check('''
            local p=unit('pa22',1,0,0,{abilities={APb1=1}}); enter(p); assert(p.order=='curseon')
            local foe=unit('hfoo',2,600,0)
            cast(p,'APb1',foe); assert(#created==0)
            local t=timers[#timers]
            for i=1,40 do if not t.destroyed then t.fn() end end
            local d=created[1]
            assert(d.id=='h05P' and d.abilities.APb2==1 and d.order=='curse' and d.target==foe)
        ''')

    def test_argus_spirit_needs_tech_and_does_not_chain(self):
        self.check('''
            local killer=unit('hfoo',2,0,0)
            local a=unit('h05D',1,10,10,{abilities={ADr6=1,A1C6=1}})
            rolls={1}; kill(killer,a); assert(#created==0)
            tech[1]={RDr6=1}
            local b=unit('h05D',1,10,10,{abilities={ADr6=1,A1C6=1}})
            rolls={16}; kill(killer,b); assert(#created==0)
            local c=unit('h05E',1,10,10,{abilities={ADr6=1,A1C6=1}})
            rolls={15}; kill(killer,c)
            local s=created[1]
            assert(s.id=='h05E' and s.summoned and s.timed==5 and s.abilities.ADr6==nil and s.abilities.A1C6==nil)
            rolls={1}; kill(killer,s); assert(#created==1)
            local gone=unit('h05D',1,0,0,{abilities={ADr6=1}}); gone.id=0
            rolls={1}; kill(killer,gone); assert(#created==1)
        ''')

    def test_loot_once_per_kill_near_own_ataman(self):
        self.check('''
            local a1=unit('h00Q',1,0,0,{abilities={ABn1=1}}); unit('h00Q',1,50,0,{abilities={ABn1=1}})
            local killer=unit('hfoo',1,0,0)
            kill(killer, unit('hfoo',2,700,0)); assert((gold[1] or 0)==0)
            tech[1]={RBn1=1}
            kill(killer, unit('hfoo',2,700,0)); assert(gold[1]==1)
            kill(killer, unit('hfoo',2,900,0)); assert(gold[1]==1)
            kill(killer, unit('hbar',2,10,0,{structure=true})); assert(gold[1]==1)
            kill(unit('hfoo',3,0,0), unit('hfoo',2,10,0)); assert(gold[1]==1)
        ''')

    def test_moon_glaive_bounces_twice_at_night_only(self):
        self.check('''
            local g=unit('e01B',1,0,0,{abilities={AMn1=1},damage=40}); tech[1]={RMn1=1}
            local a=unit('hfoo',2,800,0); local b=unit('hfoo',2,900,0); local c=unit('hfoo',2,1000,0)
            unit('hfoo',2,2000,0)
            daytime=12; hit(g,a); assert(#NightborneGlaive.flights==0)
            daytime=22; hit(g,a); hit(g,b)  -- второе событие того же выстрела (сплэш) пропускается
            assert(#NightborneGlaive.flights==1)
            local t=timers[#timers]
            for i=1,40 do if not t.destroyed then t.fn() end end
            assert(#damage==2 and damage[1].target==b and damage[2].target==c)
            assert(math.abs(damage[1].amount-33.6)<1e-6 and math.abs(damage[2].amount-26.88)<1e-6)
        ''')


if __name__ == '__main__':
    unittest.main()
