"""Exercise Draenei mechanics with real Lua and stateful Warcraft native mocks."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Draenei.lua'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'; UNIT_STATE_MANA='mana'
UNIT_TYPE_HERO='hero'; UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_MECHANICAL='mechanical'
UNIT_TYPE_MAGIC_IMMUNE='immune'; UNIT_TYPE_WARD='ward'; UNIT_TYPE_RANGED_ATTACKER='ranged'
ATTACK_TYPE_NORMAL='normal'; DAMAGE_TYPE_MAGIC='magic'; WEAPON_TYPE_WHOKNOWS='unknown'
world={}; effects={}; timers={}; tech={}; damageLog={}; orders={}; groupsCreated=0; groupsDestroyed=0
function FourCC(s) return s end
function unit(id,owner,hp,maxhp,x,y)
    local u={id=id,owner=owner,hp=hp or 100,maxhp=maxhp or 100,x=x or 0,y=y or 0,
             mana=1000,abilities={},handle=#world+1}
    world[#world+1]=u; return u
end
function GetHandleId(u) return u.handle end
function GetUnitTypeId(u) return u.id end
function GetOwningPlayer(u) return u.owner end
function GetUnitState(u,s) return u[s] end
function SetUnitState(u,s,v) u[s]=v end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function IsUnitType(u,t) return u[t]==true end
function IsUnitIllusion(u) return u.illusion==true end
function BlzIsUnitInvulnerable(u) return u.invulnerable==true end
function IsUnitEnemy(u,p) return u.owner~=p end
function IsUnitAlly(u,p) return u.owner==p end
function GetPlayerTechCount(p,id,flag) return tech[p..id] and 1 or 0 end
function GetUnitAbilityLevel(u,id) return u.abilities[id] or 0 end
function SetUnitAbilityLevel(u,id,lvl) u.abilities[id]=lvl end
function BlzGetUnitAbilityCooldownRemaining(u,id) return (u.cooldown or {})[id] or 0 end
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,delay,periodic,callback) t.delay=delay; t.periodic=periodic; t.callback=callback end
function DestroyTimer(t) assert(not t.destroyed); t.destroyed=true end
function AddSpecialEffectTarget(path,u,attach)
    local e={path=path,unit=u,attach=attach}; effects[#effects+1]=e; return e
end
function DestroyEffect(e) assert(not e.destroyed); e.destroyed=true end
function BlzSetSpecialEffectScale(e,s) e.scale=s end
function CreateGroup() groupsCreated=groupsCreated+1; return {} end
function GroupEnumUnitsInRange(g,x,y,r,filter)
    for _,u in ipairs(world) do
        if (u.x-x)^2+(u.y-y)^2<=r*r then g[#g+1]=u end
    end
end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
function DestroyGroup(g) groupsDestroyed=groupsDestroyed+1 end
function GetEventDamage() return eventDamage end
function GetEventDamageSource() return eventSource end
function BlzGetEventDamageTarget() return eventTarget end
function BlzGetEventIsAttack() return eventAttack end
function BlzSetEventDamage(v) eventDamage=v end
function attack(src,target,amount,isAttack)
    eventSource=src; eventTarget=target; eventDamage=amount; eventAttack=isAttack~=false
    DraeneiCombat.Damage(); return eventDamage
end
function UnitDamageTarget(src,target,amount,isAttack,...)
    damageLog[#damageLog+1]={target=target,amount=amount,attack=isAttack}
    local oldSource,oldTarget,oldDamage,oldAttack=eventSource,eventTarget,eventDamage,eventAttack
    attack(src,target,amount,isAttack)
    target.hp=target.hp-eventDamage
    eventSource,eventTarget,eventDamage,eventAttack=oldSource,oldTarget,oldDamage,oldAttack
end
function CreateUnit(p,id,x,y,facing) local u=unit(id,p,5,5,x,y); u.ward=true; return u end
function RemoveUnit(u) u.id=0; u.hp=0 end
function UnitApplyTimedLife(u,buff,time) u.timedLife=time end
function ticks(n) for i=1,n do DraeneiCombat.Tick() end end
function flush()
    local pending={}
    for _,t in ipairs(timers) do
        if not t.periodic and not t.destroyed then pending[#pending+1]=t end
    end
    for _,t in ipairs(pending) do t.callback() end
end
function IssueTargetOrder(u,o,target) orders[#orders+1]={caster=u,order=o,target=target}; return true end
function IssuePointOrder(u,o,x,y) orders[#orders+1]={caster=u,order=o,x=x,y=y}; return true end
'''


class DraeneiCombatTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute(SOURCE.read_text(encoding='utf-8'))

    def run_lua(self, code):
        self.lua.execute(code)
        self.lua.execute('assert(groupsCreated==groupsDestroyed, "temporary group leak")')

    def test_prismatic_charges_research_gate_and_bounded_enemy_shards(self):
        self.run_lua('''
            local ranger=unit('e000',1); ranger.abilities.ADr1=1
            local main=unit('enemy',2,100,100,100)
            local other=unit('enemy',2,100,100,101)
            local second=unit('enemy',2,100,100,102)
            local third=unit('enemy',2,100,100,103)
            local ally=unit('ally',1,100,100,100)
            local immune=unit('immune',2,100,100,100); immune.immune=true
            assert(attack(ranger,main,20)==20 and #effects==0)
            tech['1RDr1']=true
            assert(attack(ranger,main,20)==28)
            assert(DraeneiCombat.units[ranger].charges==1 and ranger.abilities.ADr1==2)
            flush()
            assert(#damageLog==2 and other.hp==85 and second.hp==85)
            assert(third.hp==100 and ally.hp==100 and immune.hp==100)
            assert(not damageLog[1].attack)
            assert(attack(ranger,main,20)==28)
            assert(attack(ranger,main,20)==20 and ranger.abilities.ADr1==3)
        ''')

    def test_prismatic_restock_and_memory_field_do_not_stack(self):
        self.run_lua('''
            local ranger=unit('e000',1); ranger.abilities.ADr1=1; tech['1RDr1']=true
            local enemy=unit('enemy',2)
            attack(ranger,enemy,20); attack(ranger,enemy,20)
            ticks(71); assert(DraeneiCombat.units[ranger].charges==0)
            ticks(1); assert(DraeneiCombat.units[ranger].charges==1)
            local caster=unit('n005',1)
            DraeneiCombat.SummonIdol(caster,0,0)
            DraeneiCombat.SummonIdol(unit('n005',1),0,0)
            ticks(47); assert(DraeneiCombat.units[ranger].charges==1)
            ticks(1); assert(DraeneiCombat.units[ranger].charges==2)
        ''')

    def test_illusions_buildings_spells_and_invulnerable_targets_do_not_spend_charges(self):
        self.run_lua('''
            local ranger=unit('e000',1); ranger.abilities.ADr1=1; tech['1RDr1']=true
            local enemy=unit('enemy',2)
            ranger.illusion=true; assert(attack(ranger,enemy,20)==20)
            ranger.illusion=false; enemy.structure=true; assert(attack(ranger,enemy,20)==20)
            enemy.structure=false; enemy.invulnerable=true; assert(attack(ranger,enemy,20)==20)
            enemy.invulnerable=false; assert(attack(ranger,enemy,20,false)==20)
            assert(DraeneiCombat.units[ranger]==nil)
        ''')

    def test_blade_health_threshold_and_actual_healing_reduce_cooldown(self):
        self.run_lua('''
            local sword=unit('h059',1,84,100); sword.abilities.ADr2=1; tech['1RDr2']=true
            local enemy=unit('enemy',2)
            assert(attack(sword,enemy,35)==35)
            sword.hp=85; assert(attack(sword,enemy,35)==65)
            assert(attack(sword,enemy,35)==35)
            assert(DraeneiCombat.Heal(sword,200)==15)
            assert(DraeneiCombat.units[sword].bladeRemaining==8)
            sword.hp=70; assert(DraeneiCombat.Heal(sword,30)==30)
            assert(DraeneiCombat.units[sword].bladeRemaining==6)
            ticks(24); assert(attack(sword,enemy,35)==65)
        ''')

    def test_vow_is_weaker_on_heroes_and_does_not_block_spell_damage(self):
        self.run_lua('''
            local paladin=unit('h01O',1)
            local target=unit('ally',1)
            local hero=unit('hero',1); hero.hero=true
            local enemy=unit('enemy',2)
            assert(DraeneiCombat.ApplyVow(paladin,target))
            assert(DraeneiCombat.ApplyVow(paladin,hero))
            assert(attack(enemy,target,100)==70)
            assert(attack(enemy,hero,100)==85)
            assert(attack(enemy,hero,100,false)==100)
            attack(enemy,hero,100)
            assert(attack(enemy,hero,100)==100)
            assert(DraeneiCombat.protection[target].vowExpires==12)
            assert(DraeneiCombat.protection[hero].vowExpires==8)
        ''')

    def test_vow_and_blessing_refresh_without_stacking(self):
        self.run_lua('''
            local paladin=unit('h01O',1); local target=unit('ally',1); local enemy=unit('enemy',2)
            DraeneiCombat.ApplyVow(paladin,target)
            local first=effects[#effects]
            DraeneiCombat.ApplyVow(paladin,target); assert(first.destroyed)
            DraeneiCombat.ApplyBlessing(paladin,target)
            assert(attack(enemy,target,100)==70)
            assert(attack(enemy,target,100,false)==90)
            ticks(16)
            assert(attack(enemy,target,100,false)==100)
            ticks(32)
            assert(attack(enemy,target,100)==100)
            assert(DraeneiCombat.protection[target]==nil)
            for _,e in ipairs(effects) do assert(e.destroyed) end
        ''')

    def test_wave_keeps_bounces_and_only_blesses_primary_after_research(self):
        self.run_lua('''
            local priest=unit('h01R',1)
            local primary=unit('ally',1,100,300,100)
            local next=unit('ally',1,100,300,200)
            local last=unit('ally',1,100,300,300)
            local extra=unit('ally',1,100,300,400)
            local machine=unit('machine',1,10,100,110); machine.mechanical=true
            local enemy=unit('enemy',2,10,100,105)
            tech['1RDr4']=true
            assert(DraeneiCombat.Wave(priest,primary))
            assert(primary.hp==230 and next.hp==197.5 and last.hp==173.125 and extra.hp==100)
            assert(machine.hp==10 and enemy.hp==10)
            assert(DraeneiCombat.protection[primary].blessingReduction==0.10)
            assert(DraeneiCombat.protection[next]==nil)
        ''')

    def test_wave_overheal_does_not_grant_blessing_and_hero_bonus_is_halved(self):
        self.run_lua('''
            local priest=unit('h01R',1); local target=unit('hero',1,90,100); target.hero=true
            tech['1RDr4']=true
            DraeneiCombat.Wave(priest,target)
            assert(target.hp==100 and DraeneiCombat.protection[target]==nil)
            target.hp=50; DraeneiCombat.Wave(priest,target)
            assert(DraeneiCombat.protection[target].blessingReduction==0.05)
            assert(DraeneiCombat.protection[target].blessingExpires==3)
        ''')

    def test_idol_preserves_lifetime_limits_healing_and_excludes_enemy_wards_machines(self):
        self.run_lua('''
            local caster=unit('n005',1)
            local ward=DraeneiCombat.SummonIdol(caster,0,0)
            assert(ward.timedLife==25)
            local targets={}
            for i=1,7 do targets[i]=unit('ally',1,100,1000,i) end
            local enemy=unit('enemy',2,10,100,1)
            local machine=unit('machine',1,10,100,1); machine.mechanical=true
            ticks(4)
            for i=1,6 do assert(targets[i].hp==120) end
            assert(targets[7].hp==100 and machine.hp==10 and enemy.hp==10)
            local old=ward
            ward=DraeneiCombat.SummonIdol(caster,0,0)
            assert(old.id==0 and #DraeneiCombat.wards==1)
            ticks(100); assert(ward.id==0 and #DraeneiCombat.wards==0)
        ''')

    def test_idol_healing_does_not_stack_and_hero_healing_is_halved(self):
        self.run_lua('''
            DraeneiCombat.SummonIdol(unit('n005',1),0,0)
            DraeneiCombat.SummonIdol(unit('n005',1),0,0)
            local target=unit('hero',1,10,1000); target.hero=true
            ticks(4); assert(target.hp==20)
        ''')

    def test_dead_and_transferred_units_release_effects_and_timer(self):
        self.run_lua('''
            local caster=unit('h01O',1); local target=unit('ally',1)
            DraeneiCombat.ApplyVow(caster,target); local e=effects[#effects]
            target.owner=2; ticks(1)
            assert(e.destroyed and DraeneiCombat.protection[target]==nil)
            assert(DraeneiCombat.timer==nil)
            local sword=unit('h059',1); sword.abilities.ADr2=1
            local state=DraeneiCombat.State(sword); sword.hp=0
            ticks(1); assert(DraeneiCombat.units[sword]==nil and DraeneiCombat.timer==nil)
        ''')

    def test_transferred_idol_does_not_buff_its_old_owner(self):
        self.run_lua('''
            local caster=unit('n005',1)
            local ward=DraeneiCombat.SummonIdol(caster,0,0)
            ward.owner=2
            assert(not DraeneiCombat.InMemoryField(caster))
            ticks(1); assert(ward.id==0 and #DraeneiCombat.wards==0)
        ''')

    def test_ai_targets_frontline_and_uses_idol_only_when_useful(self):
        self.run_lua('''
            local paladin=unit('h01O',1); tech['1RDr3']=true
            local ranger=unit('e000',1,10,100); ranger.ranged=true
            local sword=unit('h059',1,60,100)
            assert(DraeneiCombat.AiVow(paladin) and orders[1].target==sword)
            local caster=unit('n005',1); tech['1RDr5']=true
            assert(DraeneiCombat.AiIdol(caster))
            DraeneiCombat.SummonIdol(caster,0,0)
            assert(not DraeneiCombat.AiIdol(caster))
        ''')


if __name__ == '__main__':
    unittest.main()
