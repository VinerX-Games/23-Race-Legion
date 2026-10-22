"""Bear grip keeps victims active, restores weapons and never pulls through obstacles."""
import sys
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from l10n_fixture import install_loc  # noqa: E402


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_MECHANICAL='mechanical'
UNIT_TYPE_FLYING='flying'; UNIT_TYPE_WARD='ward'; UNIT_TYPE_HERO='hero'
UNIT_WEAPON_BF_ATTACKS_ENABLED='attacks'; PATHING_TYPE_WALKABILITY='walk'
ATTACK_TYPE_NORMAL='normal'; DAMAGE_TYPE_NORMAL='physical'; WEAPON_TYPE_WHOKNOWS='unknown'
EVENT_PLAYER_UNIT_SPELL_EFFECT='spell'; EVENT_PLAYER_UNIT_DEATH='death'
function FourCC(s) return s end
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u,s) return u[s] end
function GetOwningPlayer(u) return u.owner end
function GetPlayerId(p) return p end
function IsUnitEnemy(u,p) return u.owner~=p and not u.allied end
function IsUnitType(u,t) return u[t]==true end
function IsUnitHidden(u) return u.hidden==true end
function IsUnitPaused(u) return u.paused==true end
function IsUnitLoaded(u) return u.loaded==true end
function BlzIsUnitInvulnerable(u) return u.invulnerable==true end
function GetUnitAbilityLevel(u,a) return u.abilities[a] or 0 end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function BlzGetUnitWeaponBooleanField(u,f,i) assert(f=='attacks'); return u.weapons[i] end
function BlzSetUnitWeaponBooleanField(u,f,i,v) assert(f=='attacks'); u.weapons[i]=v end
timers={}; destroyed=0; removed=0; itemsRemoved=0; damage={}; orders={}; positions=0; triggers={}
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,dt,r,fn) t.dt=dt; t.fn=fn end
function PauseTimer(t) t.paused=true end
function DestroyTimer(t) assert(not t.destroyed); t.destroyed=true; destroyed=destroyed+1 end
function CreateUnit(p,id,x,y,f)
    if failCreate then return nil end
    return {id=id,owner=p,x=x,y=y,hp=1,abilities={ARbg=1},weapons={}}
end
function RemoveUnit(u) u.id=0; removed=removed+1 end
function CreateItem(id,x,y) if failProbe then return nil end; return {id=id,x=x,y=y} end
function GetItemTypeId(i) return i.id end
function SetItemVisible(i,v) i.visible=v end
function RemoveItem(i) i.id=0; itemsRemoved=itemsRemoved+1 end
function SetItemPosition(i,x,y) i.x=x+(collisionShift or 0); i.y=y end
function GetItemX(i) return i.x end
function GetItemY(i) return i.y end
function UnitRemoveAbility(u,a) u.abilities[a]=nil end
function IssueTargetOrder(u,o,t)
    orders[#orders+1]={unit=u,order=o,target=t}
    if rejectRoot and u.id=='nBgr' then return false end
    if u.id=='nBgr' and not delayedRoot then t.abilities.BBgr=1 end
    return true
end
function IssuePointOrder(u,o,x,y) orders[#orders+1]={unit=u,order=o,x=x,y=y}; return true end
function IsTerrainPathable(x,y,t) assert(t=='walk'); return blocked and blocked(x,y) or false end
function SetUnitPosition(u,x,y) error('SetUnitPosition would cancel the victim attack/spell order') end
function SetUnitX(u,x) u.x=x end
function SetUnitY(u,y) u.y=y end
function UnitDamageTarget(source,target,amount,attack,ranged,at,dt,wt)
    damage[#damage+1]={source=source,target=target,amount=amount,attack=attack}
    assert(amount==30 and not attack and not ranged and at=='normal' and dt=='physical')
    target.hp=target.hp-amount
    if target.hp<=0 and triggers.death then eventUnit=target; triggers.death.action() end
    return true
end
function CreateTrigger() return {} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=t end
function TriggerAddAction(t,fn) t.action=fn end
function GetSpellAbilityId() return spellId or 'ABgr' end
function GetTriggerUnit() return eventUnit end
function GetSpellTargetUnit() return victim end
function BlzEndUnitAbilityCooldown(u,a) cooldownReset=a end
function DisplayTextToPlayer(...) messages=(messages or 0)+1 end
bear={id='n05V',owner=1,x=0,y=0,hp=900,abilities={ABgr=1},weapons={[0]=true,[1]=false}}
victim={id='hfoo',owner=2,x=100,y=0,hp=500,abilities={},weapons={[0]=true,[1]=true}}
function cast() assert(BearGrip.Cast(bear,victim)); state=BearGrip.bears[bear] end
function ticks(n) for i=1,n do if not state.finished then state.timer.fn() end end end
'''


class BearGripTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        install_loc(self.lua)
        self.lua.execute((SECTIONS / '80_runtime/triggers/races/IceTrolls.lua').read_text(encoding='utf-8'))

    def check(self, code):
        self.lua.execute(code)

    def test_damage_once_and_regular_grip_lasts_five_seconds(self):
        self.check('''
            cast(); assert(#damage==1 and victim.hp==470 and state.duration==5)
            ticks(159); assert(not state.finished)
            ticks(1); assert(state.finished and victim.hp==470 and #damage==1)
            assert(destroyed==1 and removed==1 and itemsRemoved==1 and next(BearGrip.bears)==nil and next(BearGrip.targets)==nil)
        ''')

    def test_hero_grip_lasts_one_second_and_still_deals_30(self):
        self.check('''
            victim.hero=true; cast(); assert(state.duration==1 and victim.hp==470)
            ticks(31); assert(not state.finished)
            ticks(1); assert(state.finished and victim.hp==470)
        ''')

    def test_victim_retains_attacks_spells_and_visibility(self):
        self.check('''
            cast()
            assert(not victim.paused and not victim.hidden and not victim.invulnerable)
            assert(victim.weapons[0] and victim.weapons[1] and victim.abilities.BBgr==1)
            assert(not bear.weapons[0] and not bear.weapons[1] and not bear.paused)
        ''')

    def test_release_restores_exact_original_weapon_states(self):
        self.check('''
            bear.weapons[0]=false; bear.weapons[1]=true; cast()
            BearGrip.Release(state); BearGrip.Release(state); BearGrip.Tick(state)
            assert(not bear.weapons[0] and bear.weapons[1] and destroyed==1)
        ''')

    def test_victim_follows_bear_without_extra_damage(self):
        self.check('''
            cast()
            for i=1,20 do bear.x=bear.x+7; ticks(1) end
            assert(math.abs(victim.x-240)<0.001 and not state.finished and #damage==1)
        ''')

    def test_dispelling_grip_releases_and_preserves_unrelated_buffs(self):
        self.check('''
            victim.abilities.Beng=1; cast(); ticks(1)
            victim.abilities.BBgr=nil; ticks(1)
            assert(state.finished and victim.abilities.Beng==1 and bear.weapons[0])
        ''')

    def test_blocked_terrain_cancels_without_moving_victim(self):
        self.check('''
            cast(); blocked=function(x,y) return x>101 end; bear.x=8; ticks(1)
            assert(state.finished and victim.x==100 and positions==0 and bear.weapons[0])
        ''')

    def test_dynamic_obstacle_detected_by_probe_prevents_displacement(self):
        self.check('''
            cast(); collisionShift=200; bear.x=8; ticks(1)
            assert(state.finished and victim.x==100 and victim.y==0)
        ''')

    def test_teleport_of_either_participant_breaks_grip(self):
        for move in ('bear.x=1000', 'victim.x=1000'):
            with self.subTest(move=move):
                self.setUp()
                self.check('cast(); ' + move + '; ticks(1); assert(state.finished and positions==0)')

    def test_death_of_either_participant_releases_immediately(self):
        for unit in ('bear', 'victim'):
            with self.subTest(unit=unit):
                self.setUp()
                self.check('BearGrip.Init(); cast(); ' + unit + '.hp=0; eventUnit=' + unit +
                           '; triggers.death.action(); assert(state.finished and destroyed==1 and victim.abilities.BBgr==nil)')

    def test_removal_hidden_loaded_paused_and_changed_owner_release(self):
        for change in ('bear.id=0', 'victim.id=0', 'bear.hidden=true', 'victim.hidden=true',
                       'bear.loaded=true', 'victim.loaded=true', 'bear.paused=true',
                       'victim.paused=true', 'bear.owner=3', 'victim.owner=3',
                       'victim.allied=true', 'victim.flying=true', 'victim.invulnerable=true',
                       'bear.abilities.ABgr=nil'):
            with self.subTest(change=change):
                self.setUp()
                self.check('cast(); '+change+'; ticks(1); assert(state.finished and destroyed==1)')

    def test_lethal_capture_hit_cleans_up_before_cast_returns(self):
        self.check('''
            BearGrip.Init(); victim.hp=20
            assert(BearGrip.Cast(bear,victim))
            assert(victim.hp==-10 and BearGrip.bears[bear]==nil and destroyed==1 and bear.weapons[0])
        ''')

    def test_rejects_invalid_targets_without_creating_handles(self):
        for change in ('victim.owner=1', 'victim.structure=true', 'victim.mechanical=true',
                       'victim.flying=true', 'victim.ward=true', 'victim.invulnerable=true',
                       'victim.hidden=true', 'victim.paused=true', 'victim.loaded=true',
                       'victim.hp=0', 'victim.x=200', "bear.id='hfoo'", 'bear.loaded=true',
                       'victim.abilities.BBgr=1'):
            with self.subTest(change=change):
                self.setUp()
                self.check(change+'; assert(not BearGrip.Cast(bear,victim)); assert(#timers==0 and #damage==0)')

    def test_duplicate_bear_and_duplicate_victim_are_rejected(self):
        self.check('''
            cast(); assert(not BearGrip.Cast(bear,victim))
            local other={id='n05V',owner=1,x=0,y=0,hp=900,abilities={ABgr=1},weapons={[0]=true,[1]=false}}
            assert(not BearGrip.Cast(other,victim) and #timers==1)
            assert(not BearGrip.Cast(victim,bear))
        ''')

    def test_failed_dummy_creation_or_root_order_is_clean(self):
        self.check('failCreate=true; assert(not BearGrip.Cast(bear,victim)); assert(#timers==0 and #damage==0)')
        self.check('failCreate=false; rejectRoot=true; assert(not BearGrip.Cast(bear,victim)); assert(#timers==0 and removed==1 and itemsRemoved==1 and bear.weapons[0])')

    def test_failed_probe_creation_removes_dummy(self):
        self.check('failProbe=true; assert(not BearGrip.Cast(bear,victim)); assert(removed==1 and #timers==0 and #damage==0)')

    def test_root_that_never_lands_cleans_up_after_grace_period(self):
        self.check('''
            delayedRoot=true; cast(); ticks(7); assert(not state.finished)
            ticks(1); assert(state.finished and destroyed==1 and bear.weapons[0])
        ''')

    def test_ai_casts_native_order_only_for_valid_targets(self):
        self.check('''
            assert(BearGrip.AiCast(bear,victim) and #orders==1 and orders[1].order=='ensnare')
            victim.flying=true; assert(not BearGrip.AiCast(bear,victim) and #orders==1)
        ''')

    def test_ai_bear_moves_away_after_capture(self):
        self.check('''
            udg_AiControl={[1]=true}; cast()
            assert(state.ai and orders[2].order=='move' and orders[2].x==-350)
            ticks(16); assert(#orders==3 and orders[3].order=='move')
        ''')

    def test_init_is_idempotent_and_other_spells_are_ignored(self):
        self.check('''
            BearGrip.Init(); local old=triggers.spell; BearGrip.Init(); assert(triggers.spell==old)
            eventUnit=bear; spellId='other'; triggers.spell.action(); assert(#damage==0)
        ''')

    def test_invalid_spell_restores_cooldown(self):
        self.check('''
            BearGrip.Init(); eventUnit=bear; victim.structure=true; triggers.spell.action()
            assert(cooldownReset=='ABgr' and messages==1 and #timers==0)
        ''')


if __name__ == '__main__':
    unittest.main()
