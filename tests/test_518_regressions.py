"""World-region reuse and Horde production/research regressions reported on 518."""
import sys
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from l10n_fixture import install_loc  # noqa: E402
from test_player_commands_and_research import FIXTURE as CHAT_FIXTURE

SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'
RACES = SECTIONS / '80_runtime/triggers/races'


class WorldRegionTests(unittest.TestCase):
    def test_race_initializers_reuse_early_world_region(self):
        lua = LuaRuntime()
        lua.execute('''
            Allmap = {}; entries = {}; triggers = 0
            function FourCC(s) return s end
            function CreateTrigger() triggers=triggers+1; return {} end
            function TriggerRegisterAnyUnitEventBJ() end
            function TriggerAddAction(t, f) t.action=f end
            function TriggerRegisterEnterRegion(t, region)
                assert(region == Allmap)
                entries[#entries+1]=t
            end
            function CreateRegion() error('late world region') end
            function RegionAddRect() error('repeated world population') end
            function GetWorldBounds() error('extra world rectangle') end
        ''')
        for name in ('Ogres.lua', 'Naga.lua', 'Pandarens.lua'):
            lua.execute((RACES / name).read_text(encoding='utf-8-sig'))
        lua.execute('''
            OgreCombat.Init(); NagaCombat.Init(); PandarenBrew.Init()
            local count = triggers
            OgreCombat.Init(); NagaCombat.Init(); PandarenBrew.Init()
            assert(triggers == count and #entries == 3)
        ''')


class HordeTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            function FourCC(s) return s end
            CommonHash=setmetatable({}, {__index=function(t,k) local v={}; t[k]=v; return v end})
            tech={}; limits={}; pending={}; triggers={}
            udg_AiControl={}; udg_MainPrice=setmetatable({}, {__index=function() return 0 end})
            function GetPlayerId(p) return p end
            function Player(p) return p end
            function GetOwningPlayer(u) assert(u); return u.owner end
            function GetUnitTypeId(u) return u.id end
            function GetPlayerTechCount(p,id) return tech[p..id] or 0 end
            function SetPlayerTechResearched(p,id,n) tech[p..id]=n end
            function SetPlayerTechMaxAllowed(p,id,n) limits[p..id]=n end
            function SetPlayerTechMaxAllowedSwap(id,n,p) SetPlayerTechMaxAllowed(p,id,n) end
            function GetPlayerTechMaxAllowedSwap(id,p) return limits[p..id] or -1 end
            function SetPlayerAbilityAvailable() end
            function GetTriggerUnit() return building end
            function GetTrainedUnit() return trained end
            function GetResearched() return research end
            function GetUnitRallyPoint() return {} end
            function GetRandomInt(a,b) assert(b>=a); return b end
            function ReplaceUnit(u,id)
                assert(id~=nil and id~=0)
                u.removed=true; replacement={id=id,owner=u.owner}; return replacement
            end
            function UnitAddAbility() end
            function IssuePointOrderLoc() end
            function RemoveLocation() end
            function CreateGroup() return {} end
            function DestroyGroup() end
            function CreateTrigger() return {} end
            function TriggerRegisterAnyUnitEventBJ(t,kind)
                triggers[kind]=triggers[kind] or {}; table.insert(triggers[kind],t)
            end
            function TriggerAddAction(t,f) t.action=f end
            function fire(kind,p,id)
                building={owner=p}; research=id
                for _,t in ipairs(triggers[kind] or {}) do t.action() end
            end
            EVENT_PLAYER_UNIT_RESEARCH_START='start'
            EVENT_PLAYER_UNIT_RESEARCH_CANCEL='cancel'
            EVENT_PLAYER_UNIT_RESEARCH_FINISH='finish'
        ''')
        self.lua.execute((RACES / 'Horde.lua').read_text(encoding='utf-8-sig'))

    def test_first_random_recruit_without_cached_roster(self):
        for player in (0, 23):
            for trigger, rawcode in (
                ('K1T1', 'ogru'), ('K1T2', 'o01N'), ('K1T2b', 'o029'),
                ('K1TCav', 'orai'), ('K1T4', 'otau'), ('K2T1', 'ohun'),
                ('K2T2', 'o01P'), ('K2T2b', 'o02B'), ('K2T3', 'okod'),
            ):
                with self.subTest(player=player, trigger=trigger):
                    self.lua.execute(f'''
                        CommonHash[{player}]={{}}; building={{owner={player}}}
                        trained={{id='{rawcode}',owner={player}}}; replacement=nil
                        assert(Trig_{trigger}_Conditions())
                        Trig_{trigger}_Actions()
                        assert(replacement and replacement.owner=={player} and trained.removed)
                    ''')

    def test_start_limits_populate_every_roster_for_new_player(self):
        self.lua.execute('''
            HordeStartLimitsFor(23)
            for _,key in ipairs({'T1','T2','T2b','TCav','T3','K1','K2','K2b','K3'}) do
                assert(CommonHash[23][key..'_0']>0)
            end
        ''')

    def test_final_branches_lock_while_researching_and_restore_on_cancel(self):
        self.lua.execute('''
            InitTrig_HordeResearch()
            tech['23R0EE']=1; tech['23R0E0']=1
            for _,chosen in ipairs({'R0EH','R0E9','R0EI'}) do
                fire('start',23,chosen)
                for _,other in ipairs({'R0EH','R0E9','R0EI'}) do
                    assert(limits['23'..other]==(other==chosen and 1 or 0))
                end
                assert(limits['0R0EH']==nil)
                fire('cancel',23,chosen)
                assert(limits['23R0EH']==1 and limits['23R0E9']==1 and limits['23R0EI']==1)
            end
            tech['23R0EH']=1; fire('finish',23,'R0EH')
            assert(limits['23R0E9']==0 and limits['23R0EI']==0)
        ''')

    def test_reject_unrelated_research_and_preserve_prerequisites(self):
        self.lua.execute('''
            InitTrig_HordeResearch()
            fire('finish',23,'Rxxx'); assert(next(limits)==nil)
            fire('finish',23,'R0D1')
            assert(limits['23R0EH']==0 and limits['23R0E9']==0 and limits['23R0EI']==0)
            fire('start',23,'R0EE')
            assert(limits['23R0EH']==0 and limits['23R0EI']==0)
        ''')

    def test_expansion_refusal_and_iron_sha_choices(self):
        self.lua.execute('''
            InitTrig_HordeResearch()
            fire('start',23,'R0DW')
            assert(limits['23R0DX']==0 and limits['23R0DY']==0 and limits['23R0DZ']==0)
            fire('cancel',23,'R0DW')
            assert(limits['23R0DX']==1 and limits['23R0DY']==1 and limits['23R0DZ']==1)
            fire('start',23,'R0DX'); assert(limits['23R0DW']==0)
            tech['23R0DX']=1; fire('finish',23,'R0DX'); assert(limits['23R0DW']==0)
            tech['23R0E9']=1
            for _,chosen in ipairs({'R0EA','R0KO'}) do
                local other=chosen=='R0EA' and 'R0KO' or 'R0EA'
                fire('start',23,chosen); assert(limits['23'..other]==0)
                fire('cancel',23,chosen); assert(limits['23'..other]==1)
            end
            tech['23R0EA']=1; fire('finish',23,'R0EA'); assert(limits['23R0KO']==0)
        ''')

    def test_related_research_uses_its_own_id(self):
        for trigger, research, unrelated in (
            ('NightBorn', 'R0F4', 'R0F3'), ('Magnatavrs', 'R0E5', 'R0E4'),
            ('CanselCommonHome', 'R0EH', 'R0E9'),
        ):
            self.lua.execute(f"research='{research}'; assert(Trig_{trigger}_Conditions()); "
                             f"research='{unrelated}'; assert(not Trig_{trigger}_Conditions())")


class ChatRegressionTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute(CHAT_FIXTURE)
        install_loc(self.lua)
        self.lua.execute('''
            Observers={}; udg_Visibl={}; cleared={}; alliances={}; cameras={}; DipMode=0
            function SetCameraFieldForPlayer(p,field,distance) cameras[p]=distance end
            function DisplayTextToForce() end
            function DisplayTextToPlayer() end
            function ClearPlayer(p) cleared[p]=(cleared[p] or 0)+1 end
            function IsPlayerInForce(p,f) return f[p] or false end
            function ForceAddPlayer(f,p) f[p]=true end
            function ForceRemovePlayer(f,p) f[p]=nil end
            function CreateFogModifierRectBJ() return {} end
            function FogModifierStop(f) f.stopped=true end
            function DestroyFogModifier(f) f.destroyed=true end
            function ForForce() end
            function SetPlayerAllianceStateBJ(p,q) alliances[#alliances+1]={p,q,true} end
            function SetPlayerAllianceBJ(p,kind,on,q) alliances[#alliances+1]={p,q,on} end
            function MultiboardAllowDisplayBJ() end
        ''')
        self.lua.execute((SECTIONS / '80_runtime/triggers/14_misc_system.lua').read_text(encoding='utf-8-sig'))
        self.lua.execute('''
            InitTrig_Camera_command_O(); InitTrig_GG(); InitTrig_Observer(); InitTrig_ObserverOff()
            InitTrig_ArchontMode(); InitTrig_ArchontModeOff()
        ''')

    def test_camera_preserves_full_argument_and_rejects_invalid_commands(self):
        self.lua.execute('''
            Dispatch(23,'-cam 12000'); assert(cameras[23]==12000)
            Dispatch(23,' - CAM 2500 '); assert(cameras[23]==2500)
            for _,message in ipairs({'-cam nope','-cam -1','-camera 100','hello -cam 100','-cam 1e999'}) do
                Dispatch(23,message); assert(cameras[23]==2500)
            end
        ''')

    def test_surrender_and_observer_commands_for_all_players(self):
        self.lua.execute('''
            for p=0,23 do
                Dispatch(p,'-gg'); assert(cleared[p]==1)
                Dispatch(p,'-observer'); assert(Observers[p] and cleared[p]==2)
                Dispatch(p,'-observer'); assert(cleared[p]==2)
                Dispatch(p,'-observeroff'); assert(not Observers[p] and udg_Visibl[p].destroyed)
                Dispatch(p,'-observeroff')
            end
        ''')

    def test_shared_control_rejects_neutral_slots_and_partial_player_numbers(self):
        self.lua.execute('''
            Dispatch(23,'-arhont 1'); assert(#alliances==1 and alliances[1][2]==0)
            Dispatch(0,'-arhoff 24'); assert(#alliances==2 and alliances[2][2]==23 and not alliances[2][3])
            for _,message in ipairs({'-arhont 25','-arhont 0','-arhont 2.5','-arhont 2oops',
                '-arhoff 25','-arhoff 0','hello -arhont 2'}) do
                Dispatch(0,message); assert(#alliances==2)
            end
        ''')


if __name__ == '__main__':
    unittest.main()
