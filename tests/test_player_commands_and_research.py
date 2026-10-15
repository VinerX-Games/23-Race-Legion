import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tmp/teleport-test-runtime'))
from lupa.lua53 import LuaRuntime

SECTIONS = ROOT / 'map.w3x/_lua/monolith_split/sections'

FIXTURE = r'''
triggers = {}; colors = {}; names = {}; board = {}; selected = {}
function Player(i) return i end
function GetPlayerId(p) return p end
function GetConvertedPlayerId(p) return p + 1 end
function GetTriggerPlayer() return sender end
function GetEventPlayerChatString() return message end
function CreateTrigger() local t={events={}}; triggers[#triggers+1]=t; return t end
function TriggerRegisterPlayerChatEvent(t,p,s,exact) t.events[#t.events+1]={p,s,exact} end
function TriggerAddAction(t,f) t.action=f end
function TriggerAddCondition(t,f) t.condition=f end
function Condition(f) return f end
function Dispatch(p,s)
    sender=p; message=s
    for _,t in ipairs(triggers) do
        for _,e in ipairs(t.events) do
            if e[1]==p and ((e[3] and s==e[2]) or (not e[3] and string.find(s,e[2],1,true))) then
                if not t.condition or t.condition() then t.action() end
                break
            end
        end
    end
end
function SetPlayerColorBJ(p,c,units) colors[p]=c; assert(units) end
function SetPlayerName(p,s) names[p]=s end
function GetPlayerName(p) return names[p] or 'Player' end
function I2S(n) return tostring(n) end
function EnsureMultiboardPlayerRow(p) if noBoard then return nil end; return p+1 end
MultiboardItem=setmetatable({}, {__index=function(t,k) return k end})
function MultiboardSetItemValue(item,s) board[item]=s end
function PlayerColorHexWrap(p,s) return tostring(colors[p] or 0)..':'..s end
function GetPlayerNameCut(p) return GetPlayerName(p) end
function CreateGroup() return {} end
function DestroyGroup() end
function SyncSelections() end
function GroupEnumUnitsSelected(g,p) for _,u in ipairs(selected) do g[#g+1]=u end end
function FirstOfGroup(g) return g[1] end
function GroupRemoveUnit(g,u) table.remove(g,1) end
function GetOwningPlayer(u) return u.owner end
function BlzSetUnitName(u,s) u.name=s end
function GetRandomInt(a,b) assert(a<=b); return a end
function GetUnitTypeId(u) return u.id end
function GetUnitState() return 100 end
function BlzGroupGetSize(g) return #g end
function BlzGroupUnitAt(g,i) return g[i+1] end
units={}; udg_ZahvatBuildings={}
function GroupEnumUnitsOfPlayer(g,p,filter)
    for _,u in ipairs(units) do
        filterUnit=u
        if u.owner==p and (not filter or filter()) then g[#g+1]=u end
    end
end
function IsUnitInGroup(u,g) return g[u] or false end
function GetFilterUnit() return filterUnit end
function DestroyBoolExpr() end
function GetPlayerTechCount(p,id,queued) return tech[id] or 0 end
function SetPlayerTechResearched(p,id,n) tech[id]=n end
function IssueImmediateOrderById(u,id) orders[#orders+1]=id end
AiData={[0]={}}; udg_AiControl={[0]=true}; Grades={[0]=0}; tech={}; orders={}; gGroup={}
'''


def section(name):
    return (SECTIONS / name).read_text(encoding='utf-8-sig')


class PlayerCommandTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        color_names = ['RED', 'BLUE', 'PURPLE', 'CYAN', 'YELLOW', 'ORANGE', 'GREEN',
                       'PINK', 'LIGHT_GRAY', 'LIGHT_BLUE', 'AQUA', 'BROWN', 'MAROON',
                       'NAVY', 'TURQUOISE', 'VIOLET', 'WHEAT', 'PEACH', 'MINT',
                       'LAVENDER', 'COAL', 'SNOW', 'EMERALD', 'PEANUT']
        for i, name in enumerate(color_names):
            self.lua.globals()['PLAYER_COLOR_' + name] = i
        source = section('80_runtime/triggers/04_race_selection.lua')
        self.lua.execute(source[source.index('function InitColorCommands()'):source.index('-- Trigger: StartTableCode')])
        source = section('80_runtime/triggers/14_misc_system.lua')
        self.lua.execute(source[source.index('function ChatCommandArgument('):source.index('-- Trigger: SecondChance')])
        self.lua.execute('InitColorCommands(); InitTrig_Name_command_O(); InitTrig_UName_command()')

    def test_color_forms_and_all_players(self):
        for player in range(24):
            for text in ['-color red', '-colorred', 'color red', ' - COLOR red ']:
                with self.subTest(player=player, text=text):
                    self.lua.globals().Dispatch(player, text)
                    self.assertEqual(self.lua.globals().colors[player], 0)

    def test_all_colors_and_invalid_commands(self):
        self.lua.execute('Dispatch(23,"-color peanut"); assert(colors[23]==23)')
        self.lua.execute('Dispatch(23,"-color light-blue"); assert(colors[23]==9)')
        self.lua.execute('Dispatch(23,"hello color red"); assert(colors[23]==9)')
        self.lua.execute('Dispatch(23,"-color unknown"); assert(colors[23]==9)')
        self.lua.execute('Dispatch(23,"-color blue"); assert(board[48]=="1:24.Player")')

    def test_player_name_unicode_spaces_and_quotes(self):
        for text in ['-name Орда Тралла', ' - name Орда Тралла ', '-NAME "Орда Тралла"']:
            self.lua.globals().Dispatch(23, text)
            self.assertEqual(self.lua.globals().names[23], 'Орда Тралла')
        self.lua.execute('assert(board[48]=="0:24.Орда Тралла")')

    def test_name_rejects_empty_and_similar_command(self):
        self.lua.execute('Dispatch(0,"-name "); Dispatch(0,\'-name ""\'); Dispatch(0,"-names Bob"); assert(names[0]==nil)')

    def test_name_before_multiboard(self):
        self.lua.execute('noBoard=true; Dispatch(0,"-name New"); assert(names[0]=="New")')

    def test_unit_name_preserves_full_argument_and_ownership(self):
        self.lua.execute('selected={{owner=23},{owner=0}}; Dispatch(23,"-uname Мой воин"); assert(selected[1].name=="Мой воин"); assert(selected[2].name==nil)')


class ResearchProgressionTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.lua.execute(FIXTURE)
        source = section('libraries/13_Races.lua')
        self.lua.execute(source[source.index('function ThisType()'):source.index('-- *  JoinArmyUnit')])

    def test_economy_level_boundaries_and_missing_host(self):
        for economy, cap in [(0, 0), (24, 0), (25, 1), (39, 1), (40, 2),
                             (54, 2), (55, 3), (70, 4), (85, 5), (99, 5), (100, 6), (500, 6)]:
            with self.subTest(economy=economy):
                self.lua.execute(f'AiData[0].researchEconomy={economy}; tech={{}}; Grades[0]=0; gGroup={{}}; for i=1,12 do MakeGradeCheckCap(0,"smith","attack",6) end; assert((tech.attack or 0)=={cap}); assert(Grades[0]=={cap})')

    def test_queued_level_blocks_duplicate_orders(self):
        self.lua.execute('AiData[0].researchEconomy=40; units={{owner=0,id="smith"}}; tech.attack=2; MakeGradeCheckCap(0,"smith","attack",6); assert(#orders==0)')
        self.lua.execute('tech.attack=1; MakeGradeCheckCap(0,"smith","attack",6); assert(#orders==1)')

    def test_single_level_research_stops_at_cap(self):
        self.lua.execute('for i=1,4 do MakeGradeCheckCap(0,"smith","skill",1) end; assert(tech.skill==1); assert(Grades[0]==1)')

    def test_legacy_dispatch_refreshes_economy_before_research(self):
        source = section('81_ai.lua')
        self.lua.execute(source[source.index('function AiDispatchStrateg('):source.index('function AiResearchEconomy(')])
        self.lua.execute('function AiRaceOf() return {strateg=function() MakeGradeCheckCap(0,"smith","attack",6) end} end; AiData[0].researchEconomy=500; AiDispatchStrateg(24,0,0); assert(tech.attack==nil); AiDispatchStrateg(25,0,0); assert(tech.attack==1)')

    def test_brain_uses_economy_instead_of_elapsed_ticks(self):
        source = section('81_ai.lua')
        self.lua.execute(source[source.index('function AiResearchEconomy('):source.index('function AiDispatchStrategEC(')])
        source = section('83_ai_brain.lua')
        start = source.index('function BrainStrategTick(')
        end = source.index('\nend', start) + 4
        self.lua.execute(source[start:end])
        self.lua.execute('race={ecoWeights={farm=1,hall=5},strategData={steps={{at=17,action="research",rows={{"smith","attack",6}}}}}}; units={{owner=0,id="farm"},{owner=0,id="hall"}}; BrainStrategTick(0,0,race,{tick=10000}); assert(tech.attack==nil); assert(AiData[0].researchEconomy==6)')
        self.lua.execute('captured={owner=0,id="city"}; units[#units+1]=captured; udg_ZahvatBuildings[captured]=true; assert(AiResearchEconomy(0,0,race)==14)')
        self.lua.execute('units={}; for i=1,40 do units[i]={owner=0,id="farm"} end; for i=1,12 do BrainStrategTick(0,0,race,{tick=10000}) end; assert(tech.attack==2)')

    def test_brain_tier_up_and_research_gates(self):
        source = section('81_ai.lua')
        self.lua.execute(source[source.index('function AiResearchEconomy('):source.index('function AiDispatchStrategEC(')])
        source = section('83_ai_brain.lua')
        start = source.index('function BrainStrategTick(')
        self.lua.execute(source[start:source.index('\nend', start) + 4])
        self.lua.execute('function getAiCount() return 0 end; units={{owner=0,id="hall"}}; udg_Ai_buildings={[0]=units}; race={ecoWeights={hall=25},strategData={steps={{at=25,action="techUp",from="hall",to="keep"},{at=17,gate="locked",action="research",rows={{"smith","attack",6}}}}},gates={locked=function() return false end}}; BrainStrategTick(0,0,race,{tick=10000}); assert(#orders==0 and tech.attack==nil); race.ecoWeights.hall=26; BrainStrategTick(0,0,race,{tick=10000}); assert(#orders==1 and orders[1]=="keep" and tech.attack==nil)')


class AiCommandAliasTests(unittest.TestCase):
    def test_bare_and_hyphenated_ai_commands(self):
        lua = LuaRuntime(unpack_returned_tuples=True)
        lua.execute(FIXTURE + 'spawned={}; function ProbeLogWrite() end; function createAiPlayer(p,race) spawned[#spawned+1]=p end')
        source = section('80_runtime/triggers/15_ai_portals_cities.lua')
        lua.execute(source[source.index('function Trig_CreateAi_Conditions('):source.index('function BridgeDispatchCommand(')])
        lua.execute('InitTrig_CreateAi(); Dispatch(0,"ai5"); Dispatch(0,"-ai6"); assert(#spawned==2 and spawned[1]==4 and spawned[2]==5); Dispatch(1,"-ai7"); assert(#spawned==2)')


if __name__ == '__main__':
    unittest.main()
