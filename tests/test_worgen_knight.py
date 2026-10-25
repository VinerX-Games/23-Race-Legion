"""Spell Scent charges a researched knight once and augments only his next hit."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


SOURCE = (Path(__file__).resolve().parents[1] /
          'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/WorgenKnight.lua')
FIXTURE = r'''
UNIT_STATE_LIFE='hp'
EVENT_PLAYER_UNIT_SPELL_EFFECT='effect'; EVENT_PLAYER_UNIT_DAMAGING='damaging'
EVENT_PLAYER_UNIT_DEATH='death'; EVENT_PLAYER_UNIT_CHANGE_OWNER='owner'
function FourCC(s) return s end
function GetUnitTypeId(u) return u and u.id or 0 end
function GetUnitState(u,s) return u[s] end
function GetOwningPlayer(u) return u.owner end
function IsUnitIllusion(u) return u.illusion==true end
function IsUnitHidden(u) return u.hidden==true end
function IsUnitLoaded(u) return u.loaded==true end
function GetUnitAbilityLevel(u,a) return u.abilities[a] or 0 end
function SetUnitAbilityLevel(u,a,l) u.abilities[a]=l end
tech={[1]=1,[2]=0,[3]=1}
function GetPlayerTechCount(p,id,complete) assert(id=='RWkn' and complete); return tech[p] or 0 end
function IsUnitEnemy(u,p) return u.owner~=p and not u.allied end
function GetUnitX(u) return u.x end
function GetUnitY(u) return u.y end
function GetTriggerUnit() return eventUnit end
function GetEventDamageSource() return source end
function BlzGetEventDamageTarget() return target end
function BlzGetEventIsAttack() return isAttack end
function GetEventDamage() return amount end
function BlzSetEventDamage(v) amount=v; changes=changes+1 end
function CreateGroup() return {} end
function GroupEnumUnitsInRange(g,x,y,r,f)
    assert(r==600)
    for i,u in ipairs(nearby) do g[i]=u end
end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
destroyed=0
function DestroyGroup(g) destroyed=destroyed+1 end
triggers={}; triggerCount=0
function CreateTrigger() triggerCount=triggerCount+1; return {} end
function TriggerRegisterAnyUnitEventBJ(t,e) triggers[e]=t end
function TriggerAddAction(t,fn) t.action=fn end
knight={id='h0IW',owner=1,x=0,y=0,hp=885,abilities={AWkn=1}}
caster={id='mage',owner=2,x=0,y=0,hp=300,abilities={}}
target={id='hfoo',owner=2,x=20,y=0,hp=500,abilities={}}
nearby={knight}; eventUnit=caster; source=knight; amount=40; isAttack=true; changes=0
function charge() WorgenKnight.Spell(); assert(knight.abilities.AWkn==2) end
'''


class WorgenKnightTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        self.lua.execute(SOURCE.read_text(encoding='utf-8'))

    def check(self, code):
        self.lua.execute(code)

    def test_enemy_spell_charges_every_eligible_knight(self):
        self.check('''
            local other={id='h0IW',owner=3,x=250,y=0,hp=885,abilities={AWkn=1}}
            nearby={knight,other}; charge()
            assert(other.abilities.AWkn==2 and destroyed==1)
        ''')

    def test_radius_includes_600_but_excludes_points_outside_circle(self):
        self.check('knight.x=600; charge()')
        self.check('knight.abilities.AWkn=1; knight.x=600.01; WorgenKnight.Spell(); assert(knight.abilities.AWkn==1)')
        self.check('knight.x=500; knight.y=500; WorgenKnight.Spell(); assert(knight.abilities.AWkn==1)')

    def test_own_and_allied_spells_do_not_charge(self):
        self.check('caster.owner=1; WorgenKnight.Spell(); assert(knight.abilities.AWkn==1)')
        self.check('caster.owner=2; knight.allied=true; WorgenKnight.Spell(); assert(knight.abilities.AWkn==1)')

    def test_research_is_required_for_charging_and_damage(self):
        self.check('''
            tech[1]=0; WorgenKnight.Spell(); assert(knight.abilities.AWkn==1)
            knight.abilities.AWkn=2; WorgenKnight.Damage(); assert(amount==40 and changes==0)
        ''')

    def test_repeated_spells_do_not_accumulate_bonus(self):
        self.check('''
            for i=1,8 do WorgenKnight.Spell() end
            WorgenKnight.Damage(); assert(amount==60 and knight.abilities.AWkn==1)
            amount=40; WorgenKnight.Damage(); assert(amount==40 and changes==1)
        ''')

    def test_charge_is_consumed_by_single_ordinary_enemy_hit(self):
        self.check('charge(); WorgenKnight.Damage(); assert(amount==60 and changes==1 and knight.abilities.AWkn==1)')

    def test_uncharged_attack_is_unchanged(self):
        self.check('WorgenKnight.Damage(); assert(amount==40 and changes==0)')

    def test_spell_damage_does_not_consume_charge(self):
        self.check('charge(); isAttack=false; WorgenKnight.Damage(); assert(amount==40 and knight.abilities.AWkn==2 and changes==0)')

    def test_zero_and_negative_damage_do_not_consume_charge(self):
        self.check('''
            charge(); amount=0; WorgenKnight.Damage(); assert(knight.abilities.AWkn==2)
            amount=-1; WorgenKnight.Damage(); assert(knight.abilities.AWkn==2 and changes==0)
        ''')

    def test_ally_attack_does_not_consume_charge(self):
        self.check('charge(); target.owner=1; WorgenKnight.Damage(); assert(knight.abilities.AWkn==2 and amount==40)')

    def test_building_attack_can_use_charge(self):
        self.check("target.id='hbar'; charge(); WorgenKnight.Damage(); assert(amount==60 and knight.abilities.AWkn==1)")

    def test_invalid_knights_neither_charge_nor_deal_bonus(self):
        for change in ("knight.id='hfoo'", 'knight.hp=0', 'knight.illusion=true',
                       'knight.hidden=true', 'knight.loaded=true', 'knight.abilities.AWkn=nil'):
            with self.subTest(change=change):
                self.setUp()
                self.check(change + '; WorgenKnight.Spell(); assert(knight.abilities.AWkn~=2)')
                if 'AWkn=nil' not in change:
                    self.check('knight.abilities.AWkn=2; WorgenKnight.Damage(); assert(amount==40 and changes==0)')

    def test_missing_caster_and_missing_damage_participants_are_safe(self):
        self.check('eventUnit=nil; WorgenKnight.Spell(); assert(destroyed==0)')
        self.check('source=nil; WorgenKnight.Damage(); assert(amount==40)')
        self.check('source=knight; knight.abilities.AWkn=2; target=nil; WorgenKnight.Damage(); assert(amount==40 and knight.abilities.AWkn==2)')

    def test_death_and_owner_change_clear_charge(self):
        self.check('''
            InitTrig_WorgenKnight(); charge(); eventUnit=knight
            knight.hp=0; triggers.death.action(); assert(knight.abilities.AWkn==1)
            knight.hp=885; knight.abilities.AWkn=2; knight.owner=3
            triggers.owner.action(); assert(knight.abilities.AWkn==1)
        ''')

    def test_only_actual_spell_effect_is_registered_and_init_is_idempotent(self):
        self.check('''
            InitTrig_WorgenKnight(); InitTrig_WorgenKnight()
            assert(triggerCount==3 and triggers.effect and triggers.damaging and triggers.death and triggers.owner)
            assert(triggers.cast==nil)
        ''')


if __name__ == '__main__':
    unittest.main()
