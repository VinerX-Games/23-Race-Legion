"""Offline checks of ONLY the seven commits leading from release 510 to 511.

Writes evidence under .cache/wc3/audit-511. Does not edit or launch the map.
Mock traces establish Lua behavior only, not Warcraft pathfinding correctness.
"""
import json
from pathlib import Path
import re
import subprocess
from lupa.lua53 import LuaRuntime
from luaparser import ast, astnodes as N

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '.cache/wc3/audit-511'
COMMITS = ['9d80391', 'fb77906', 'fec12de', 'e9d9b62', 'e1eddf1', '83d3fbf', '4df89dd']
PREFIX = 'map.w3x/_lua/monolith_split/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8-sig')


def section(rev, path):
    return git('show', rev + ':' + PREFIX + 'sections/' + path)


def function(rev, path, name):
    text = section(rev, path)
    tree = ast.parse(text)
    for node in tree.body.body:
        if isinstance(node, N.Function) and isinstance(node.name, N.Name) and node.name.id == name:
            return ast.to_lua_source(node)
    raise ValueError(name)


def build(rev):
    manifest = json.loads(git('show', rev + ':' + PREFIX + 'manifest.json'))
    return ''.join(section(rev, s['file']) for s in manifest['sections'])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    result = {'scope': COMMITS, 'syntax': {}, 'timer_equivalence': [], 'mock_init': {}, 'focused': {}}
    snapshots = {}
    compile_lua = LuaRuntime().eval('function(s) local f,e=load(s); return f~=nil,e end')
    for rev in ['53d6b95'] + COMMITS:
        text = build(rev)
        snapshots[rev] = text
        ok, error = compile_lua(text)
        assert ok, (rev, error)
        path = OUT / (rev + '.lua')
        path.write_text(text, encoding='utf-8')
        historical = git('show', rev + ':map.w3x/war3map.lua')
        result['syntax'][rev] = {'lua53_compile': ok, 'generated_matches_sources': historical == text}
    # Check every BJ timer replacement in source diffs for literal equivalence.
    for rev in COMMITS:
        diff = git('show', '--format=', rev, '--', 'map.w3x/_lua')
        old = re.findall(r'^-\s*StartTimerBJ\((.*), (true|false), (.*?)\)\s*$', diff, re.M)
        new = re.findall(r'^\+\s*TimerStart\((.*), (.*?), (true|false), nil\)\s*$', diff, re.M)
        if old:
            normalized = [(timer, periodic, period) for timer, period, periodic in new]
            assert sorted(old) == sorted(normalized), (rev, old, new)
            result['timer_equivalence'].append({'commit': rev, 'sites': len(old), 'equivalent': True})
    # Reuse fixture's engine-stub setup only. Do not run its current-worktree test.
    fixture = (ROOT / 'tests/fixtures/lobby_smoke.py').read_text(encoding='utf-8')
    setup = fixture.split("code = (ROOT / 'map.w3x/war3map.lua')")[0]
    for rev in ['53d6b95', '4df89dd']:
        env = {'__file__': str(ROOT / 'tests/fixtures/lobby_smoke.py')}
        exec(compile(setup, '<mock-engine-setup>', 'exec'), env)
        lua = env['lua']
        lua.execute('TRACE={}; print=function() end')
        lua.execute(r'''
            for _, name in ipairs({'CreateUnit','BlzCreateUnitWithSkin','CreateNUnitsAtLoc',
                'CreateUnitAtLoc','CreateDestructable','CreateDestructableLoc','CreateItem',
                'SetUnitPathing','SetUnitMoveSpeed','SetTerrainPathable','PauseUnit','RemoveUnit',
                'ShowUnit','IssuePointOrder','IssueImmediateOrder'}) do
                local original=_G[name]
                if original then _G[name]=function(...)
                    local args={}
                    for i=1,select('#',...) do
                        local v=select(i,...)
                        if type(v)=='table' then
                            args[i]=v.__pid~=nil and ('player:'..v.__pid) or v.__kind
                        elseif type(v)=='function' then args[i]='callback'
                        else args[i]=v end
                    end
                    TRACE[#TRACE+1]={name=name,args=args}
                    return original(...)
                end end
            end
        ''')
        lua.execute(snapshots[rev])
        ok, error = lua.globals().__guarded(lua.globals().main, 200000000)
        assert ok, (rev, error)
        errors = [lua.globals().InitErrors[i] for i in range(1, len(lua.globals().InitErrors) + 1)]
        trace = [dict(name=row['name'], args=[row['args'][i] for i in range(1, len(row['args'])+1)]) for row in lua.globals().TRACE.values()]
        result['mock_init'][rev] = {'errors': errors, 'trace': trace, 'timer_callbacks_executed': False}
    result['mock_init_same_physical_trace'] = result['mock_init']['53d6b95']['trace'] == result['mock_init']['4df89dd']['trace']
    # Focused actual-function scenarios, with explicit controlled inputs.
    for rev in ['53d6b95', '4df89dd']:
        lua = LuaRuntime(unpack_returned_tuples=True)
        lua.execute('AiUnitsToPort={};AiCapitalGuard={};AiCapitalBuildigs={};Grades={}; function CreateGroup() return {} end')
        lua.execute(function(rev, 'libraries/04_AI0.lua', 'SetPortalGroup'))
        preserve = lua.eval('function() SetPortalGroup();local g=AiUnitsToPort[0];Grades[0]=7;SetPortalGroup();return g==AiUnitsToPort[0],Grades[0] end')()
        result['focused'][rev] = {'portal_groups_preserved_on_second_call': preserve[0], 'grades_after_second_call': preserve[1]}
        lua.execute(r'''
            udg_Ai_buildings={[0]={{id=10,pct=99,x=0,y=0,h=1},{id=10,pct=100,x=100,y=0,h=2}}}
            UNIT_STATE_LIFE=1;UNIT_STATE_MAX_LIFE=2
            function BlzGroupGetSize(g) return #g end
            function BlzGroupUnitAt(g,i) return g[i+1] end
            function GetUnitTypeId(u) return u.id end
            function GetUnitState(u,s) return 100 end
            function GetUnitStatePercent(u,a,b) return u.pct end
            function GetHandleId(u) return u.h end
            function GetUnitX(u) return u.x end
            function GetUnitY(u) return u.y end
        ''')
        lua.execute(function(rev, '83_ai_brain.lua', 'AiFindProdBuilding'))
        u = lua.globals().AiFindProdBuilding(0, 10, lua.table())
        result['focused'][rev]['production_choice_hp_pct'] = u['pct']
        lua.execute(r'''
            tArray={}; function AiCountBuildingOrders() return 0 end
            function AddBuilding(id,n) for i=1,n do tArray[0]=tArray[0]+1;tArray[tArray[0]]=id end end
            function GetRandomInt(a,b) return a end
        ''')
        lua.execute(function(rev, '81_ai.lua', 'AiRunChooseBuildings'))
        chosen = lua.eval('function() return AiRunChooseBuildings(0,{buildings={{20,1,1},{10,1,1}}}) end')()
        result['focused'][rev]['weighted_build_choice_fixed_random_index'] = chosen
        # Reproduce a real UI-local stale-variable defect in PercentGraph (511 only).
        lua.execute(r'''
            MultiboardItemOwnerIndex={};ThirdColumn={};CityPlayerCount={[0]=1};CityCount=2
            Multiboard={};UI_CALLS=0
            function EnsureMultiboardPlayerRow(pi) MultiboardItemOwnerIndex[pi]=1;return 1 end
            function MultiboardGetItem(...) return {} end
            function MultiboardSetItemValue(...) UI_CALLS=UI_CALLS+1 end
            function I2R(x) return x end
            function R2SW_Polyfill(x) return tostring(x) end
        ''')
        lua.execute(function(rev, '80_runtime/_lib/51_update_graph.lua', 'PercentGraph'))
        lua.globals().PercentGraph(0)
        result['focused'][rev]['percent_graph_first_call_updates'] = lua.globals().UI_CALLS
        lua.execute(r'''
            g_AiOrdered={}; AiBrainMaxProduce=3;AiBrainTickCounter=100
            AiLimitedBuildTicks=10;AiMaxHeroes=3;HERO_ORDERS={}
            function AiFindProdBuilding(pi,id,used)
                if used[100] then return nil end
                used[100]=true;return 100
            end
            function IssueImmediateOrderById(b,id) HERO_ORDERS[#HERO_ORDERS+1]=id end
        ''')
        lua.execute(function(rev, '83_ai_brain.lua', 'BrainProduce'))
        hero_orders = lua.eval('function() return BrainProduce(0,{acount={[201]=1}},{maxHeroes=1,altar=100,production={[100]={{201,1},{202,1},{203,1}}}}) end')()
        result['focused'][rev]['hero_orders_with_existing_hero_and_race_cap_one'] = hero_orders
        # The new PercentGraph/ArmyExpGraph can need a second call to use a newly
        # created owner index. Record the persistent local variable, not a pathing claim.
        lua.execute(r'''
            COLOR_REGISTRATIONS={};COLOR_ACTION=nil;COLOR_CHANGES=0;CHAT='-colorred'
            PLAYER_COLOR_RED=1
            function CreateTrigger() return {} end
            function Player(i) return i end
            function TriggerRegisterPlayerChatEvent(t,p,text,exact)
                COLOR_REGISTRATIONS[#COLOR_REGISTRATIONS+1]={text=text,exact=exact}
            end
            function TriggerAddAction(t,f) COLOR_ACTION=f end
            function GetEventPlayerChatString() return CHAT end
            function GetTriggerPlayer() return 0 end
            function SetPlayerColorBJ(...) COLOR_CHANGES=COLOR_CHANGES+1 end
        ''')
        lua.execute(function(rev, '80_runtime/triggers/04_race_selection.lua', 'InitColorCommands'))
        lua.globals().InitColorCommands()
        result['focused'][rev]['color_command_registered_for_exact_color_only'] = lua.eval('function() for _,e in ipairs(COLOR_REGISTRATIONS) do if e.text=="color" and e.exact then return true end end return false end')()
        lua.globals().COLOR_ACTION()
        result['focused'][rev]['color_handler_direct_call_with_colorred_changes_color'] = lua.globals().COLOR_CHANGES
    old, new = result['focused']['53d6b95'], result['focused']['4df89dd']
    assert not old['portal_groups_preserved_on_second_call'] and new['portal_groups_preserved_on_second_call']
    assert (old['production_choice_hp_pct'], new['production_choice_hp_pct']) == (99, 100)
    assert (old['weighted_build_choice_fixed_random_index'], new['weighted_build_choice_fixed_random_index']) == (20, 10)
    assert (old['hero_orders_with_existing_hero_and_race_cap_one'], new['hero_orders_with_existing_hero_and_race_cap_one']) == (0, 1)
    assert new['percent_graph_first_call_updates'] == 0
    assert new['color_command_registered_for_exact_color_only']
    assert new['color_handler_direct_call_with_colorred_changes_color'] == 1
    (OUT / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'syntax_snapshots': len(result['syntax']),
        'timer_equivalence': result['timer_equivalence'],
        'mock_init_errors': {r:len(v['errors']) for r,v in result['mock_init'].items()},
        'mock_init_same_physical_trace':result['mock_init_same_physical_trace'],
        'focused':result['focused']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
