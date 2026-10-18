import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'

FIXTURE = r'''
AiData = {[2] = {wm={}, combatTick=0}}
udg_AiControl = {[2]=true}
UNIT_STATE_LIFE='hp'; UNIT_STATE_MAX_LIFE='maxhp'
UNIT_STATE_MANA='mana'; UNIT_STATE_MAX_MANA='maxmana'
UNIT_TYPE_STRUCTURE='building'; UNIT_TYPE_HERO='hero'
EVENT_PLAYER_UNIT_SPELL_CHANNEL=1; EVENT_PLAYER_UNIT_SPELL_EFFECT=2
EVENT_PLAYER_UNIT_SPELL_ENDCAST=3; EVENT_PLAYER_UNIT_DEATH=4
function FourCC(s) return s end
function Player(i) return i end
function GetPlayerId(p) return p end
function GetOwningPlayer(u) return u.owner end
function GetUnitTypeId(u) return u.id end
function GetUnitState(u, s) return u[s] or 0 end
function GetUnitStatePercent(u, s, max) return 100*u[s]/u[max] end
function GetUnitX(u) return u.x or 0 end
function GetUnitY(u) return u.y or 0 end
function GetUnitAbilityLevel(u, a) return u.abilities[a] or 0 end
function GetRandomInt(a,b) return a end
function SquareRoot(v) return math.sqrt(v) end
function IsUnitType(u,t) return u[t] == true end
function IsUnitAlly(u,p) return u.owner==p end
function IsUnitEnemy(u,p) return u.owner~=p end
function IsUnitVisible(u,p) return not u.hidden end
orders={}; nearby={}; destroyed=0
function issue(u,o,target)
    orders[#orders+1]={u=u,order=o,target=target}
    return o~='rejected'
end
function IssueImmediateOrder(u,o) return issue(u,o) end
function IssueImmediateOrderById(u,o) return issue(u,o) end
function IssueTargetOrder(u,o,t) return issue(u,o,t) end
function IssuePointOrder(u,o,x,y) return issue(u,o,{x=x,y=y}) end
function CreateGroup() return {} end
function GroupEnumUnitsInRange(g,x,y,r,f) for i,u in ipairs(nearby) do g[i]=u end end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
function DestroyGroup(g) destroyed=destroyed+1 end
function GetHeroLevel(u) return u.level end
function GetHeroSkillPoints(u) return u.points end
function SelectHeroSkill(u,s)
    if s~='blocked' and (u.abilities[s] or 0)<1 and u.points>0 then
        u.abilities[s]=1; u.points=u.points-1
    end
end
function UnitInventorySize(u) return #u.items end
function UnitItemInSlot(u,s) return u.items[s+1] end
function GetItemTypeId(i) return i.id end
function UnitUseItem(u,i) u.hp=u.maxhp; used=i.id; return true end
function GetTriggerUnit() return triggerUnit end
function GetTriggerEventId() return event end
function GetSpellAbilityId() return 'spell' end
function hero(hp)
    return {id='hero',owner=2,hp=hp or 100,maxhp=100,mana=100,maxmana=100,
        hero=true,abilities={},items={},level=6,points=3}
end
u=hero(); enemy=hero(); enemy.owner=3
'''


class AiCombatTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        source = (SECTIONS / '81_ai.lua').read_text(encoding='utf-8')
        self.lua.execute(source[source.index('function AiRunAttacker('):source.index('function AiDispatchUpgrade(')])
        self.lua.execute(source[source.index('function AiCombatState('):])

    def test_rejected_order_tries_next_skill(self):
        self.lua.execute('''
            AiRunAttacker('hero',u,enemy,2,{attackerData={hero={
                {order='rejected',chance=1},{order='frostnova',chance=1}}}})
            assert(#orders==2 and orders[2].order=='frostnova')
            assert(AiData[2].castAccepted==1)
        ''')

    def test_draenei_wave_ignores_mechanisms_illusions_and_trivial_wounds(self):
        self.lua.execute('''
            UNIT_TYPE_MECHANICAL='mechanical'; UNIT_TYPE_WARD='ward'
            function IsUnitIllusion(unit) return unit.illusion==true end
            local machine=hero(1); machine.mechanical=true
            local illusion=hero(1); illusion.illusion=true
            local small=hero(95)
            local wounded=hero(60)
            nearby={machine,illusion,small,wounded}
            assert(_castAbility(u,{order='healingwave',type='heal',organicOnly=true,minLostHP=20},enemy,2))
            assert(#orders==1 and orders[1].target==wounded)
        ''')

    def test_accepted_cast_is_not_overwritten_by_post(self):
        self.lua.execute('''
            AiRunAttacker('hero',u,enemy,2,{attackerData={hero={{order='frostnova',chance=1}},
                post={{order='roar',chance=1}}}})
            assert(#orders==1)
            assert(not _castAbility(u,{order='another'},enemy,2))
        ''')

    def test_heal_selects_wounded_ally_and_releases_group(self):
        self.lua.execute('''
            ally=hero(25); enemy.hp=1; nearby={enemy,u,ally}
            assert(_castAbility(u,{order='heal',type='heal'},enemy,2))
            assert(orders[1].target==ally and destroyed==1)
        ''')

    def test_no_heal_for_healthy_allies(self):
        self.lua.execute("nearby={u,enemy}; assert(not _castAbility(u,{order='heal',type='heal'},enemy,2)); assert(#orders==0 and destroyed==1)")

    def test_missing_ability_is_skipped(self):
        self.lua.execute("assert(not _castAbility(u,{order='roar',needAbil='missing'},enemy,2)); assert(#orders==0)")

    def test_numeric_summon_order(self):
        self.lua.execute("assert(_castAbility(u,{orderId=852667,type='immediate'},enemy,2)); assert(orders[1].order==852667)")

    def test_saved_points_and_rejected_skill(self):
        self.lua.execute('''
            assert(AiRunGetLvl(u,{getLvlData={hero={ult='ultimate',skills={'blocked','one','two'}}}}))
            assert(u.points==0 and u.abilities.ultimate==1 and u.abilities.two==1)
        ''')

    def test_all_skills_blocked_terminates(self):
        self.lua.execute("AiRunGetLvl(u,{getLvlData={hero={skills={'blocked'}}}}); assert(u.points==3)")

    def test_retreat_hysteresis_and_potion(self):
        self.lua.execute('''
            u.hp=20; AiHeroCombatTick(2,u,{capX=10,capY=20},nil)
            assert(AiCombatProtected(u) and orders[1].order=='move')
            u.hp=50; AiHeroCombatTick(2,u,{capX=10,capY=20},nil)
            assert(AiCombatProtected(u))
            u.items={{id='phea'}}; AiHeroCombatTick(2,u,{capX=10,capY=20},nil)
            assert(used=='phea' and not AiCombatProtected(u))
        ''')

    def test_only_effect_event_counts_real_casts(self):
        self.lua.execute('''
            triggerUnit=u; event=1; AiCombatSpellEvent(); assert(AiCombatProtected(u))
            assert(AiData[2].castEffects==nil)
            event=2; AiCombatSpellEvent(); assert(AiData[2].castEffects.spell==1)
            event=3; AiCombatSpellEvent(); assert(not AiCombatProtected(u))
            event=4; AiCombatSpellEvent(); assert(AiData[2].combat[u]==nil)
        ''')

    def test_round_robin_targets_visible_enemy_hero(self):
        self.lua.execute('''
            hidden=hero(1); hidden.owner=3; hidden.hidden=true
            weak=hero(70); weak.owner=3; weak.hero=false
            nearby={hidden,weak,enemy}; udg_Ai_army={[2]={u}}
            AiCombatTick(2,{}, {attackerData={hero={{order='frostnova',chance=1}}}})
            assert(orders[1].target==enemy and destroyed==1)
        ''')

    def test_support_heals_after_combat_ends(self):
        self.lua.execute('''
            ally=hero(20); nearby={u,ally}; udg_Ai_army={[2]={u}}
            AiCombatTick(2,{}, {attackerData={hero={{order='heal',type='heal',chance=1}}}})
            assert(orders[1].target==ally and destroyed==2)
        ''')

    def test_pending_order_expires_if_no_spell_event_arrives(self):
        self.lua.execute('''
            assert(_castAbility(u,{order='queued'},enemy,2))
            assert(AiCombatProtected(u))
            AiData[2].combatTick=2
            assert(not AiCombatProtected(u))
        ''')

    def test_idle_army_cannot_recall_retreating_hero(self):
        source = (SECTIONS / 'libraries/04_AI0.lua').read_text(encoding='utf-8')
        start = source.index('function IsAiCombatRetaskable(')
        self.lua.execute(source[start:source.index('\nend', start) + 4])
        self.lua.execute('''
            function GetUnitCurrentOrder(u) return 0 end
            assert(IsAiCombatRetaskable(u))
            AiCombatState(u).retreat=true
            assert(not IsAiCombatRetaskable(u))
        ''')


if __name__ == '__main__':
    unittest.main()
