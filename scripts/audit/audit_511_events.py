"""Stateful offline event comparison of the Git 510/511 snapshots.

Models groups, forces, trigger actions and unit entrance. It deliberately does
not model Warcraft collision/pathfinding or claim engine gameplay validation.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.fix_naga_buildings import parse_w3u

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '.cache/wc3/audit-511'

MOCK = r'''
print=function() end
WORLD={};MUTATIONS={};EVENT_ERRORS={};NULL_READS={};STAGE='load';ENTER_REG={};BOT_SET={};TECH_MAX={};RESEARCH={}
function record(name,...)
    local a={}
    for i=1,select('#',...) do
        local v=select(i,...)
        if type(v)=='table' then
            a[i]=v.__pid~=nil and ('player:'..v.__pid) or (v.ordinal and ('unit:'..v.ordinal) or v.__kind)
        else a[i]=v end
    end
    MUTATIONS[#MUTATIONS+1]={stage=STAGE,name=name,args=a}
end
local function valid(g) assert(g~=nil,'NULL group');assert(not g.dead,'DESTROYED group');return g end
function CreateGroup() local g=__handle('group');g.members={};return g end
function DestroyGroup(g) valid(g).dead=true end
function GroupClear(g) valid(g).members={} end
function GroupAddUnit(g,u)
    valid(g);assert(u~=nil,'NULL unit added');
    for _,v in ipairs(g.members) do if v==u then return end end
    g.members[#g.members+1]=u
end
function GroupRemoveUnit(g,u) valid(g);for i,v in ipairs(g.members) do if v==u then table.remove(g.members,i);return end end end
function IsUnitInGroup(u,g) valid(g);for _,v in ipairs(g.members) do if v==u then return true end end return false end
function BlzGroupGetSize(g) return #valid(g).members end
function BlzGroupUnitAt(g,i) return valid(g).members[i+1] end
function FirstOfGroup(g) return valid(g).members[1] end
function GroupAddUnitSimple(u,g) GroupAddUnit(g,u) end
function GroupRemoveUnitSimple(u,g) GroupRemoveUnit(g,u) end
function GroupAddGroup(a,b) for _,u in ipairs(valid(a).members) do GroupAddUnit(b,u) end end
function GetFilterUnit() return FILTER_UNIT end
function GetEnumUnit() return ENUM_UNIT end
function GetEnumPlayer() return ENUM_PLAYER end
function GetTriggeringTrigger() return CURRENT_TRIGGER end
function GetTriggerUnit() return CURRENT_UNIT end
function GetEnteringUnit() return CURRENT_UNIT end
function GetTriggerPlayer() return CURRENT_UNIT and CURRENT_UNIT.owner or Player(0) end
function Condition(f) local h=__handle('conditionfunc');h.__fn=f;return h end
Filter=Condition
local function fn(f) return type(f)=='function' and f or (f and f.__fn) end
local function accepts(f,u)
    if f==nil then return true end
    local old=FILTER_UNIT;FILTER_UNIT=u
    local ok,v=pcall(fn(f));FILTER_UNIT=old
    if not ok then error(v) end
    return v==true
end
local function enumerate(g,test,f)
    GroupClear(g)
    for _,u in ipairs(WORLD) do if not u.removed and test(u) and accepts(f,u) then GroupAddUnit(g,u) end end
end
function GroupEnumUnitsOfPlayer(g,p,f) enumerate(g,function(u) return u.owner==p end,f) end
function GroupEnumUnitsInRect(g,r,f) enumerate(g,function(u) return u.x>=r.minx and u.x<=r.maxx and u.y>=r.miny and u.y<=r.maxy end,f) end
function GroupEnumUnitsInRange(g,x,y,r,f) enumerate(g,function(u) return (u.x-x)^2+(u.y-y)^2<=r*r end,f) end
function GroupEnumUnitsInRangeOfLoc(g,l,r,f) return GroupEnumUnitsInRange(g,l.x,l.y,r,f) end
function GroupEnumUnitsInRangeCounted(g,x,y,r,f,n) GroupEnumUnitsInRange(g,x,y,r,f);while #g.members>n do table.remove(g.members) end end
function ForGroup(g,f)
    local list={};for _,u in ipairs(valid(g).members) do list[#list+1]=u end
    local old=ENUM_UNIT;for _,u in ipairs(list) do ENUM_UNIT=u;f() end;ENUM_UNIT=old
end
function ForGroupBJ(g,f) local destroy=bj_wantDestroyGroup;bj_wantDestroyGroup=false;ForGroup(g,f);if destroy then DestroyGroup(g) end end
function GetUnitsInRectAll(r) local g=CreateGroup();GroupEnumUnitsInRect(g,r,nil);return g end
function GetUnitsInRectMatching(r,f) local g=CreateGroup();GroupEnumUnitsInRect(g,r,f);return g end
function GetUnitsOfPlayerAll(p) local g=CreateGroup();GroupEnumUnitsOfPlayer(g,p,nil);return g end
function GetUnitsOfPlayerMatching(p,f) local g=CreateGroup();GroupEnumUnitsOfPlayer(g,p,f);return g end
function GetUnitsOfTypeIdAll(id) local g=CreateGroup();enumerate(g,function(u) return u.typeId==id end,nil);return g end
function GetUnitsOfPlayerAndTypeId(p,id) local g=CreateGroup();enumerate(g,function(u) return u.owner==p and u.typeId==id end,nil);return g end
function GroupPickRandomUnit(g) return FirstOfGroup(g) end
function CountUnitsInGroup(g) return BlzGroupGetSize(g) end
function CreateForce() local f=__handle('force');f.members={};return f end
function ForceAddPlayer(f,p) assert(f~=nil,'NULL force');for _,v in ipairs(f.members) do if v==p then return end end;f.members[#f.members+1]=p end
ForceAddPlayerSimple=function(p,f) ForceAddPlayer(f,p) end
function ForceRemovePlayer(f,p) for i,v in ipairs(f.members) do if v==p then table.remove(f.members,i);return end end end
function ForceClear(f) f.members={} end
function IsPlayerInForce(p,f) if not f then return false end;for _,v in ipairs(f.members) do if v==p then return true end end return false end
function ForForce(f,cb) assert(f~=nil,'NULL force');local old=ENUM_PLAYER;for _,p in ipairs(f.members) do ENUM_PLAYER=p;cb() end;ENUM_PLAYER=old end
function CountPlayersInForceBJ(f) return #f.members end
function GetPlayersAll() return ALL_PLAYERS end
function GetPlayersAllies(p) return CreateForce() end
function GetPlayersMatching(f)
    local g=CreateForce();local old=FILTER_PLAYER
    for i=0,23 do FILTER_PLAYER=Player(i);if fn(f)() then ForceAddPlayer(g,Player(i)) end end
    FILTER_PLAYER=old;return g
end
function GetFilterPlayer() return FILTER_PLAYER end
function GetPlayerSlotState(p) return (GetPlayerId(p)==0 or BOT_SET[GetPlayerId(p)]) and PLAYER_SLOT_STATE_PLAYING or PLAYER_SLOT_STATE_EMPTY end
function GetPlayerController(p) return BOT_SET[GetPlayerId(p)] and MAP_CONTROL_COMPUTER or MAP_CONTROL_USER end
function IsPlayerAlly(a,b) return a==b end
function IsPlayerEnemy(a,b) return a~=b end
function IsUnitAlly(u,p) return u and u.owner==p or false end
function IsUnitEnemy(u,p) return u and u.owner~=p or false end
function SetPlayerTechMaxAllowed(p,id,n) local pi=GetPlayerId(p);TECH_MAX[pi]=TECH_MAX[pi] or {};TECH_MAX[pi][id]=n end
function SetPlayerTechMaxAllowedSwap(id,n,p) SetPlayerTechMaxAllowed(p,id,n) end
function GetPlayerTechMaxAllowed(p,id) return TECH_MAX[GetPlayerId(p)] and TECH_MAX[GetPlayerId(p)][id] or -1 end
function GetPlayerTechMaxAllowedSwap(id,p) return GetPlayerTechMaxAllowed(p,id) end
function SetPlayerTechResearched(p,id,n) local pi=GetPlayerId(p);RESEARCH[pi]=RESEARCH[pi] or {};RESEARCH[pi][id]=n end
function SetPlayerTechResearchedSwap(id,n,p) SetPlayerTechResearched(p,id,n) end
function GetPlayerTechCount(p,id,completed) return RESEARCH[GetPlayerId(p)] and RESEARCH[GetPlayerId(p)][id] or 0 end
function GetPlayerTechCountSimple(id,p) return GetPlayerTechCount(p,id,true) end
function GetConvertedPlayerId(p) return GetPlayerId(p)+1 end
function ConvertedPlayer(i) return Player(i-1) end
function GetUnitX(u) assert(u~=nil,'NULL GetUnitX');return u.x end
function GetUnitY(u) assert(u~=nil,'NULL GetUnitY');return u.y end
function GetOwningPlayer(u) if not u then NULL_READS[#NULL_READS+1]={name='GetOwningPlayer',stage=STAGE};return Player(0) end;return u.owner end
function GetUnitTypeId(u) return u and not u.removed and u.typeId or 0 end
function GetUnitState(u,s) if not u then NULL_READS[#NULL_READS+1]={name='GetUnitState',stage=STAGE};return 0 end;return u.life or 1000 end
function UnitAlive(u) return u~=nil and not u.removed and (u.life or 1000)>0.405 end
function GetUnitAbilityLevel(u,id) return u and u.abilities[id] or 0 end
function GetUnitUserData(u) return u.userdata end
function SetUnitUserData(u,i) u.userdata=i end
function GetUnitCurrentOrder(u) return u.order or 0 end
function IsUnitType(u,t)
    if not u then return false end
    if t==UNIT_TYPE_PEON then return PEON_TYPES and PEON_TYPES[u.typeId] or false end
    if t==UNIT_TYPE_STRUCTURE then
        local flag=OBJECT_BUILDING[u.typeId]
        if flag~=nil then return flag end
        return BUILDING_TYPES and BUILDING_TYPES[u.typeId] or false
    end
    if t==UNIT_TYPE_HERO then local byte=(u.typeId>>24)&255;return byte>=65 and byte<=90 end
    return false
end
function GetUnitStatePercent(u,a,b) return 100 end
function BlzGetUnitMaxHP(u) return u.maxlife or 1000 end
function GetUnitFoodMade(u) return u and OBJECT_FOOD[u.typeId] or 0 end
function IsUnitPaused(u) return u.paused or false end
function UnitAddAbility(u,id) u.abilities[id]=1;record('UnitAddAbility',u,id);return true end
function UnitRemoveAbility(u,id) u.abilities[id]=nil;record('UnitRemoveAbility',u,id);return true end
function SetUnitPathing(u,v) u.pathing=v;record('SetUnitPathing',u,v) end
function PauseUnit(u,v) u.paused=v;record('PauseUnit',u,v) end
function SetUnitMoveSpeed(u,v) record('SetUnitMoveSpeed',u,v) end
function SetUnitPosition(u,x,y) u.x=x;u.y=y;record('SetUnitPosition',u,x,y) end
function SetUnitPositionLoc(u,l) SetUnitPosition(u,l.x,l.y) end
function SetUnitX(u,x) u.x=x;record('SetUnitX',u,x) end
function SetUnitY(u,y) u.y=y;record('SetUnitY',u,y) end
function RemoveUnit(u) if u then u.removed=true;record('RemoveUnit',u) end end
function KillUnit(u) if u then u.life=0;record('KillUnit',u) end end
function SetUnitOwner(u,p,v) u.owner=p;record('SetUnitOwner',u,p) end
function ShowUnit(u,v) u.hidden=not v;record('ShowUnit',u,v) end
function IssueImmediateOrder(u,o) record('IssueImmediateOrder',u,o);return true end
function IssuePointOrder(u,o,x,y) record('IssuePointOrder',u,o,x,y);return true end
function IssueImmediateOrderById(u,o) record('IssueImmediateOrderById',u,o);return true end
function IssueBuildOrderById(u,id,x,y) record('IssueBuildOrderById',u,id,x,y);return true end
function GroupPointOrder(g,o,x,y) for _,u in ipairs(valid(g).members) do IssuePointOrder(u,o,x,y) end;return true end
function GroupPointOrderLoc(g,o,l) return GroupPointOrder(g,o,l.x,l.y) end
function GroupImmediateOrder(g,o) for _,u in ipairs(valid(g).members) do IssueImmediateOrder(u,o) end;return true end
function Location(x,y) local l=__handle('location');l.x=x;l.y=y;return l end
function GetLocationX(l) assert(l~=nil,'NULL location');return l.x end
function GetLocationY(l) assert(l~=nil,'NULL location');return l.y end
function GetUnitLoc(u) return Location(GetUnitX(u),GetUnitY(u)) end
function MoveLocation(l,x,y) l.x=x;l.y=y end
function Rect(a,b,c,d) local r=__handle('rect');r.minx=a;r.miny=b;r.maxx=c;r.maxy=d;return r end
function GetWorldBounds() return Rect(-30720,-30720,30720,30720) end
function GetPlayableMapRect() return bj_mapInitialPlayableArea end
function GetRectCenterX(r) return (r.minx+r.maxx)/2 end
function GetRectCenterY(r) return (r.miny+r.maxy)/2 end
function GetRectCenter(r) return Location(GetRectCenterX(r),GetRectCenterY(r)) end
function GetRandomLocInRect(r) return GetRectCenter(r) end
function GetRandomLocInRectBJ(r) return GetRectCenter(r) end
function RectContainsUnit(r,u) return u.x>=r.minx and u.x<=r.maxx and u.y>=r.miny and u.y<=r.maxy end
function GetRectMinX(r) return r.minx end
function GetRectMaxX(r) return r.maxx end
function GetRectMinY(r) return r.miny end
function GetRectMaxY(r) return r.maxy end
function InitBlizzard()
    bj_lastCreatedGroup=CreateGroup();bj_mapInitialPlayableArea=GetWorldBounds()
    ALL_PLAYERS=CreateForce();for i=0,23 do ForceAddPlayer(ALL_PLAYERS,Player(i)) end
    bj_FORCE_ALL_PLAYERS=ALL_PLAYERS
end
function CreateTrigger() local t=__handle('trigger');t.actions={};t.conditions={};t.enabled=true;return t end
function TriggerAddAction(t,f) t.actions[#t.actions+1]=f;return __handle('triggeraction') end
function TriggerAddCondition(t,f) t.conditions[#t.conditions+1]=f;return __handle('triggercondition') end
function TriggerEvaluate(t) for _,f in ipairs(t.conditions) do if not fn(f)() then return false end end;return true end
function TriggerExecute(t)
    local old=CURRENT_TRIGGER;CURRENT_TRIGGER=t
    for _,f in ipairs(t.actions) do
        local ok,err=pcall(f)
        if not ok then EVENT_ERRORS[#EVENT_ERRORS+1]={stage=STAGE,error=tostring(err)} end
    end
    CURRENT_TRIGGER=old
end
function ConditionalTriggerExecute(t) if t.enabled and TriggerEvaluate(t) then TriggerExecute(t) end end
function ExecuteFunc(name) return _G[name]() end
function DisableTrigger(t) if t then t.enabled=false end end
function EnableTrigger(t) if t then t.enabled=true end end
function IsTriggerEnabled(t) return t and t.enabled or false end
function TriggerRegisterEnterRectSimple(t,r) ENTER_REG[#ENTER_REG+1]={t=t,r=r};return __handle('event') end
function TriggerRegisterEnterRegion(t,r,f) ENTER_REG[#ENTER_REG+1]={t=t,f=f};return __handle('event') end
local function entrance(u)
    local old=CURRENT_UNIT;local oldfilter=FILTER_UNIT;CURRENT_UNIT=u;FILTER_UNIT=u
    for _,e in ipairs(ENTER_REG) do
        if (not e.r or RectContainsUnit(e.r,u)) and (not e.f or fn(e.f)()) then ConditionalTriggerExecute(e.t) end
    end
    CURRENT_UNIT=old;FILTER_UNIT=oldfilter
end
function CreateUnit(p,id,x,y,face)
    local u=__handle('unit');u.owner=p;u.typeId=id;u.x=x;u.y=y;u.userdata=0;u.abilities={};u.life=1000;u.ordinal=#WORLD+1
    for ability in pairs(OBJECT_ABILITIES[id] or {}) do u.abilities[ability]=1 end
    WORLD[#WORLD+1]=u;record('CreateUnit',p,id,x,y);entrance(u);return u
end
function BlzCreateUnitWithSkin(p,id,x,y,face,skin) return CreateUnit(p,id,x,y,face) end
function CreateUnitAtLoc(p,id,l,face) return CreateUnit(p,id,l.x,l.y,face) end
function CreateNUnitsAtLoc(n,id,p,l,face)
    GroupClear(bj_lastCreatedGroup)
    for i=1,n do bj_lastCreatedUnit=CreateUnitAtLoc(p,id,l,face);GroupAddUnit(bj_lastCreatedGroup,bj_lastCreatedUnit) end
    return bj_lastCreatedGroup
end
function GetLastCreatedUnit() return bj_lastCreatedUnit end
function GetLastCreatedGroup() return bj_lastCreatedGroup end
function GetUnitFacing(u) return 0 end
function CreateDestructableLoc(id,l,face,scale,var) record('CreateDestructableLoc',id,l.x,l.y);return __handle('destructable') end
function CreateItem(id,x,y) record('CreateItem',id,x,y);return __handle('item') end
function GetSpellAbilityUnit() return CURRENT_UNIT end
'''


def to_python(value):
    if hasattr(value, 'items'):
        items = list(value.items())
        if sorted(k for k, _ in items if isinstance(k, int)) == list(range(1, len(items) + 1)):
            return [to_python(v) for k, v in sorted(items)]
        return {str(k): to_python(v) for k, v in items}
    return value


def setup_runtime(rev, bots=0):
    fixture = (ROOT / 'tests/fixtures/lobby_smoke.py').read_text(encoding='utf-8')
    setup = fixture.split("code = (ROOT / 'map.w3x/war3map.lua')")[0]
    env = {'__file__': str(ROOT / 'tests/fixtures/lobby_smoke.py')}
    exec(compile(setup, '<mock-setup>', 'exec'), env)
    lua = env['lua']
        # Event getters have no unit outside a relevant event. The generic
        # fixture returned arbitrary handles, which invents impossible units.
    for name, return_type in env['natives'].items():
        if return_type == 'unit' and name.startswith('Get'):
            lua.globals()[name] = lua.eval('function() return nil end')
    lua.execute(MOCK)
    _, originals, custom = parse_w3u((ROOT / '.cache/wc3/compare-510/war3map.w3u').read_bytes())
    ability_map = {}
    food_map = {}
    building_map = {}
    for obj in originals + custom:
        code = obj['cust'] if obj['cust'].strip('\0') else obj['orig']
        mods = {m['id']: m['val'] for m in obj['mods']}
        type_id = int.from_bytes(code.encode('latin1'), 'big')
        if 'ufma' in mods:
            food_map[type_id] = mods['ufma']
        if 'ubdg' in mods:
            building_map[type_id] = bool(mods['ubdg'])
        elif mods.get('upat'):
            building_map[type_id] = True
        if 'uabi' in mods:
            ability_map[int.from_bytes(code.encode('latin1'), 'big')] = {
                int.from_bytes(a.encode('latin1'), 'big'): True
                for a in mods['uabi'].split(',') if len(a) == 4
            }
    lua.globals().OBJECT_ABILITIES = lua.table_from(
        {key: lua.table_from(value) for key, value in ability_map.items()})
    lua.globals().OBJECT_FOOD = lua.table_from(food_map)
    lua.globals().OBJECT_BUILDING = lua.table_from(building_map)
    for player in range(1, bots + 1):
        lua.globals().BOT_SET[player] = True
    lua.execute((OUT / (rev + '.lua')).read_text(encoding='utf-8-sig'))
        # Type classifications from unchanged race declarations, rather than
        # assuming that all units are neither buildings nor workers.
    lua.execute('''
            PEON_TYPES={};BUILDING_TYPES={}
            for _,race in pairs(AiRaces) do
                if race.buildings then
                    if race.buildings.seed then BUILDING_TYPES[race.buildings.seed]=true end
                    for _,row in ipairs(race.buildings) do BUILDING_TYPES[row[1]]=true end
                end
                local w=race.production and race.production.worker
                if w and w.id then PEON_TYPES[w.id]=true end
            end
    ''')
    return lua


def run_stages(lua, stages):
    status = []
    for name, code in stages:
        lua.globals().STAGE = name
        ok, err = lua.globals().__guarded(lua.eval('function() ' + code + ' end'), 20000000)
        status.append({'stage': name, 'ok': ok, 'error': str(err) if err else None})
    return {'stages': status, 'event_errors': to_python(lua.globals().EVENT_ERRORS),
            'init_errors': to_python(lua.globals().InitErrors),
            'mutations': to_python(lua.globals().MUTATIONS),
            'null_reads': to_python(lua.globals().NULL_READS),
            'bot_list': to_python(lua.globals().AiBrainBotList),
            'tech_max': to_python(lua.globals().TECH_MAX),
            'research': to_python(lua.globals().RESEARCH)}


def main():
    result = {}
    for bots in [0, 1, 3]:
        for rev in ['53d6b95', '4df89dd']:
            lua = setup_runtime(rev, bots)
            stages = [('main', 'main()'), ('lobby_start', 'Trig_StartLobby_Actions()'),
                  ('lobby_end', 'Trig_EndLobby_and_Start_game_Actions()'),
                  ('human_alliance_choice', "CURRENT_UNIT=CreateUnit(Player(0),FourCC('h0HJ'),-3632,29264,0);Trig_Race_Alliance_Actions();CURRENT_UNIT=nil"),
                  ('alliance_bot_create', "createAiPlayer(1,'alliance')"),
                  ('alliance_bot_tick', 'AiBrainArmyTickInner(1,Player(1))'),
                  ('alliance_bot_20_ticks', 'for i=1,20 do AiBrainArmyTickInner(1,Player(1)) end')]
            result[f'{rev}:bots={bots}'] = run_stages(lua, stages)
    (OUT / 'event-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    for rev, data in result.items():
        print(json.dumps({'rev': rev, 'stages': data['stages'], 'event_errors': data['event_errors'],
                         'init_errors': data['init_errors'], 'mutation_count': len(data['mutations'])}, ensure_ascii=False))

    races = list(setup_runtime('4df89dd').globals().AiRaces.keys())
    race_result = {}
    for race in sorted(races):
        for rev in ['53d6b95', '4df89dd']:
            lua = setup_runtime(rev)
            lua.globals().TEST_RACE = race
            stages = [('main', 'main()'),
                      ('race_bot_create', 'local r=AiRaces[TEST_RACE]; createAiPlayer(1,r.tokens and r.tokens[1] or TEST_RACE)'),
                      ('race_bot_tick', 'AiBrainArmyTickInner(1,Player(1))')]
            race_result[f'{rev}:{race}'] = run_stages(lua, stages)
    (OUT / 'race-event-results.json').write_text(json.dumps(race_result, ensure_ascii=False, indent=2), encoding='utf-8')
    different = []
    for race in sorted(races):
        a, b = race_result[f'53d6b95:{race}'], race_result[f'4df89dd:{race}']
        # Stack traces contain different generated line numbers; compare success
        # separately from physical mutations rather than normalizing away errors.
        if a['mutations'] != b['mutations'] or [x['ok'] for x in a['stages']] != [x['ok'] for x in b['stages']]:
            different.append(race)
    tech_differences = [race for race in sorted(races)
        if race_result[f'53d6b95:{race}']['tech_max'] != race_result[f'4df89dd:{race}']['tech_max']]
    print(json.dumps({'races_checked':len(races), 'races_with_behavior_differences':different,
        'races_with_tech_limit_differences': tech_differences,
        'failed_stages': {key:[x for x in data['stages'] if not x['ok']] for key,data in race_result.items() if any(not x['ok'] for x in data['stages'])}}, ensure_ascii=False))

    commits = ['53d6b95','9d80391','fb77906','fec12de','e9d9b62','e1eddf1','83d3fbf','4df89dd']
    isolated = {}
    for rev in commits:
        lua = setup_runtime(rev, 3)
        isolated[rev] = run_stages(lua, [
            ('main', 'main()'), ('lobby_start', 'Trig_StartLobby_Actions()'),
            ('lobby_end', 'Trig_EndLobby_and_Start_game_Actions()'),
            ('human_alliance_choice', "CURRENT_UNIT=CreateUnit(Player(0),FourCC('h0HJ'),-3632,29264,0);Trig_Race_Alliance_Actions();CURRENT_UNIT=nil"),
            ('alliance_bot_create', "createAiPlayer(1,'alliance')"),
            ('alliance_bot_tick', 'AiBrainArmyTickInner(1,Player(1))')])
    (OUT / 'isolated-commit-events.json').write_text(json.dumps(isolated, ensure_ascii=False, indent=2), encoding='utf-8')
    changes = [rev for rev in commits[1:] if isolated[rev]['mutations'] != isolated['53d6b95']['mutations']]
    print(json.dumps({'individual_source_snapshots':len(isolated),'different_physical_traces':changes}))
    # All tested stages must actually execute without hidden callback faults.
    for data in list(result.values()) + list(race_result.values()) + list(isolated.values()):
        assert all(stage['ok'] for stage in data['stages']), data['stages']
        assert not data['event_errors'] and not data['init_errors'], data['init_errors']


if __name__ == '__main__':
    main()
