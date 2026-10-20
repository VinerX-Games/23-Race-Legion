"""Rescue retains the original patient and always releases it and its timer."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
FIXTURE = r'''
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'
UNIT_STATE_MANA='mana'; UNIT_STATE_MAX_MANA='maxmana'
UNIT_TYPE_STRUCTURE='structure'; UNIT_TYPE_MECHANICAL='mechanical'; UNIT_TYPE_HERO='hero'
EVENT_PLAYER_UNIT_SPELL_EFFECT='spell'; EVENT_PLAYER_UNIT_DEATH='death'
function FourCC(s) return s end
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u, s) return u[s] end
function SetUnitState(u, s, v) u[s]=v end
function GetOwningPlayer(u) return u.owner end
function IsUnitAlly(u,p) return u.owner==p or u.owner==2 end
function IsUnitIllusion(u) return u.illusion==true end
function IsUnitHidden(u) return u.hidden==true end
function IsUnitPaused(u) return u.paused==true end
function BlzIsUnitInvulnerable(u) return u.invulnerable==true end
function IsUnitType(u,t) return u[t]==true end
function GetUnitX(u) return u.x or 0 end
function GetUnitY(u) return u.y or 0 end
function GetUnitFacing(u) return 90 end
function CreateUnit(p,id,x,y,f)
    if failCreate then return nil end
    return {id=id,owner=p,x=x,y=y,hp=300,maxhp=300}
end
function SetUnitPathing(u,v) u.pathing=v end
function PauseUnit(u,v) u.paused=v end
function SetUnitInvulnerable(u,v) u.invulnerable=v end
function ShowUnit(u,v) u.hidden=not v end
function RemoveUnit(u) u.id=0; removed=removed+1 end
timers={}; destroyed=0; removed=0
function CreateTimer() local t={}; timers[#timers+1]=t; return t end
function TimerStart(t,dt,repeat_,fn) t.fn=fn; t.dt=dt end
function PauseTimer(t) t.paused=true end
function DestroyTimer(t) assert(not t.destroyed); t.destroyed=true; destroyed=destroyed+1 end
nearby={}; groupsDestroyed=0
function CreateGroup() return {} end
function GroupEnumUnitsInRange(g,x,y,r,f) assert(r==700); for i,u in ipairs(nearby) do g[i]=u end end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
function DestroyGroup(g) groupsDestroyed=groupsDestroyed+1 end
function IssueTargetOrder(u,order,target) lastTarget=target; lastOrder=order; return true end
triggers={}
function CreateTrigger() return {} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=t end
function TriggerAddAction(t,fn) t.action=fn end
function GetSpellAbilityId() return spellId or 'ASrc' end
function GetTriggerUnit() return eventUnit end
function GetSpellTargetUnit() return patient end
function BlzEndUnitAbilityCooldown(u,a) cooldownReset=a end
function DisplayTextToPlayer(...) messages=(messages or 0)+1 end
caster={id='e01R',owner=1,hp=800,maxhp=800,mana=100,maxmana=450}
patient={id='e01P',owner=1,hp=100,maxhp=1000,mana=30,maxmana=100}
function cast() assert(SilitidRescue.Cast(caster,patient)); state=SilitidRescue.targets[patient] end
function ticks(n) for i=1,n do if not state.finished then state.timer.fn() end end end
'''


class SilitidRescueTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute((SECTIONS / '80_runtime/triggers/races/Silitids.lua').read_text(encoding='utf-8'))

    def check(self, code):
        self.lua.execute(code)

    def test_full_duration_heals_64_percent_and_restores_same_unit(self):
        self.check('''
            cast()
            assert(patient.hidden and patient.paused and patient.invulnerable)
            assert(state.cocoon.id=='nSrc' and not state.cocoon.pathing)
            ticks(32)
            assert(patient.hp==740 and patient.mana==30 and patient.id=='e01P')
            assert(not patient.hidden and not patient.paused and not patient.invulnerable)
            assert(state.finished and destroyed==1 and removed==1)
            assert(SilitidRescue.targets[patient]==nil and next(SilitidRescue.cocoons)==nil)
        ''')

    def test_destroyed_cocoon_releases_immediately_without_bonus_heal(self):
        self.check('''
            SilitidRescue.Init(); cast(); ticks(8)
            state.cocoon.hp=0; eventUnit=state.cocoon; triggers.death.action()
            assert(patient.hp==260 and not patient.hidden and state.finished)
            SilitidRescue.Release(state); SilitidRescue.Tick(state)
            assert(patient.hp==260 and destroyed==1 and removed==1)
        ''')

    def test_full_health_releases_early_and_does_not_overheal(self):
        self.check('patient.hp=990; cast(); ticks(1); assert(patient.hp==1000 and state.finished)')

    def test_mother_death_does_not_interrupt_cocoon(self):
        self.check('cast(); caster.hp=0; ticks(32); assert(patient.hp==740 and state.finished)')

    def test_each_silitid_hero_is_released_after_two_seconds_with_6_percent_healing(self):
        for code in ('U023', 'U024', 'U025', 'U02R', 'U02S'):
            with self.subTest(hero=code):
                self.setUp()
                self.check("patient.id='" + code + "'; patient.hero=true; cast(); " + '''
                    assert(state.duration==2)
                    ticks(7); assert(not state.finished and patient.hidden and patient.hp==152.5)
                    ticks(1); assert(state.finished and patient.hp==160)
                    assert(not patient.hidden and not patient.paused and not patient.invulnerable)
                    assert(destroyed==1)
                ''')

    def test_ordinary_silitid_keeps_eight_second_duration(self):
        self.check('''
            cast(); assert(state.duration==8)
            ticks(31); assert(not state.finished and patient.hp==720)
            ticks(1); assert(state.finished and patient.hp==740)
        ''')

    def test_destroyed_hero_cocoon_keeps_only_received_healing(self):
        self.check('''
            SilitidRescue.Init(); patient.id='U025'; patient.hero=true; cast(); ticks(4)
            state.cocoon.hp=0; eventUnit=state.cocoon; triggers.death.action()
            assert(state.finished and patient.hp==130 and not patient.hidden)
            ticks(8); assert(patient.hp==130)
        ''')

    def test_target_death_or_removal_never_resurrects(self):
        for removal in ('patient.hp=0', 'patient.id=0'):
            with self.subTest(removal=removal):
                self.setUp()
                self.check('cast(); ' + removal + '; ticks(1); assert(state.finished and patient.hp<=100)')

    def test_missing_cocoon_and_ownership_changes_release(self):
        for change in ('state.cocoon.id=0', 'patient.owner=3', 'state.cocoon.owner=3'):
            with self.subTest(change=change):
                self.setUp()
                self.check('cast(); ' + change + '; ticks(1); assert(state.finished and not patient.hidden and destroyed==1)')

    def test_allied_species_and_self_target_are_valid(self):
        self.check('patient.owner=2; assert(SilitidRescue.ValidTarget(caster,patient))')
        self.check('caster.hp=400; assert(SilitidRescue.ValidTarget(caster,caster))')

    def test_rejects_invalid_species_states_and_enemies(self):
        for change in ("patient.id='e01G'", "patient.id='e01I'", "patient.id='e01N'",
                       "patient.id='hfoo'", "patient.id='Hpal'; patient.hero=true", 'patient.owner=3', 'patient.hp=1000',
                       'patient.hp=0', 'patient.illusion=true', 'patient.hidden=true',
                       'patient.paused=true', 'patient.invulnerable=true',
                       'patient.mechanical=true', 'patient.structure=true'):
            with self.subTest(change=change):
                self.setUp()
                self.check(change + '; assert(not SilitidRescue.Cast(caster,patient)); assert(#timers==0)')

    def test_duplicate_cast_does_not_create_another_cocoon(self):
        self.check('cast(); assert(not SilitidRescue.Cast(caster,patient)); assert(#timers==1)')

    def test_simultaneous_cocoons_have_independent_state(self):
        self.check('''
            cast(); local first=state; local oldPatient=patient
            patient={id='e01Q',owner=2,hp=100,maxhp=1000}; cast()
            first.cocoon.hp=0; SilitidRescue.Tick(first)
            assert(first.finished and not state.finished and patient.hidden and not oldPatient.hidden)
            ticks(32); assert(patient.hp==740 and destroyed==2)
        ''')

    def test_failed_creation_keeps_original_patient_active(self):
        self.check('failCreate=true; assert(not SilitidRescue.Cast(caster,patient)); assert(not patient.hidden and #timers==0)')

    def test_ai_chooses_valid_wounded_species_and_frees_group(self):
        self.check('''
            local enemy={id='e01P',owner=3,hp=1,maxhp=1000}
            local foreign={id='hfoo',owner=1,hp=1,maxhp=1000}
            nearby={enemy,foreign,caster,patient}
            assert(SilitidRescue.AiCast(caster) and lastTarget==patient)
            assert(lastOrder=='ancestralspirit' and groupsDestroyed==1)
            patient.hp=700
            assert(not SilitidRescue.AiCast(caster) and groupsDestroyed==2)
        ''')

    def test_invalid_spell_refunds_mana_and_cooldown(self):
        self.check('''
            SilitidRescue.Init(); eventUnit=caster; patient.id='hfoo'
            triggers.spell.action()
            assert(caster.mana==200 and cooldownReset=='ASrc' and messages==1)
            spellId='other'; triggers.spell.action(); assert(caster.mana==200)
        ''')

    def test_successful_spell_keeps_cost_and_init_is_idempotent(self):
        self.check('''
            SilitidRescue.Init(); local original=triggers.spell
            SilitidRescue.Init(); assert(triggers.spell==original)
            eventUnit=caster; triggers.spell.action()
            assert(patient.hidden and caster.mana==100 and cooldownReset==nil)
        ''')


if __name__ == '__main__':
    unittest.main()
