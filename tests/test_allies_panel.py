"""Окно «Союзники» (65_allies_panel.lua) на модели нативов союзов и фреймов."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / 'map.w3x/_lua/monolith_split/sections'
FRAME_PARK = (SECTIONS / '80_runtime/_ui/58_frame_park.lua').read_text(encoding='utf-8')
LOCALIZATION = (SECTIONS / '03_localization.lua').read_text(encoding='utf-8')
PANEL = (SECTIONS / '80_runtime/_ui/65_allies_panel.lua').read_text(encoding='utf-8')

FIXTURE = r'''
FRAMEPOINT_TOPLEFT='tl'; FRAMEPOINT_TOPRIGHT='tr'; FRAMEPOINT_BOTTOMLEFT='bl'; FRAMEPOINT_BOTTOMRIGHT='br'
FRAMEPOINT_TOP='t'; FRAMEPOINT_BOTTOM='b'; FRAMEPOINT_LEFT='l'
TEXT_JUSTIFY_TOP=1; TEXT_JUSTIFY_LEFT=2; TEXT_JUSTIFY_MIDDLE=3; TEXT_JUSTIFY_CENTER=4; TEXT_JUSTIFY_RIGHT=5
FRAMEEVENT_CONTROL_CLICK='click'; FRAMEEVENT_MOUSE_WHEEL='wheel'; FRAMEEVENT_SLIDER_VALUE_CHANGED='slider'
ORIGIN_FRAME_GAME_UI='gameui'; OSKEY_F11='F11'
PLAYER_SLOT_STATE_PLAYING='playing'
PLAYER_STATE_RESOURCE_GOLD='gold'; PLAYER_STATE_RESOURCE_LUMBER='lumber'
ALLIANCE_SHARED_CONTROL='control'; ALLIANCE_SHARED_ADVANCED_CONTROL='adv'
bj_ALLIANCE_UNALLIED=0; bj_ALLIANCE_ALLIED_VISION=2; bj_ALLIANCE_ALLIED_UNITS=3; bj_ALLIANCE_ALLIED_ADVUNITS=4
function Player(i) return i end
function GetPlayerId(p) return p end
localPlayer=0
function GetLocalPlayer() return localPlayer end
function ProbeLogWrite() end
function GetPlayerName(p) return 'P' .. p end
function GetPlayerColor(p) return p end
function GetHandleId(h) return h end

-- Участники и игровые данные.
playing={}
function GetPlayerSlotState(p) return playing[p] and 'playing' or 'empty' end
udg_AiControl={}; Observers=nil
Senior={}; Vassals={}; playerCapital={}; CityPlayerCount={}; AllyTax={}
DipMode=2
races={}
function CustomHudPlayerRaceName(pi) return races[pi] end
StandardUIHidden=false
AiDiplomatEnabled=false

res={}
function GetPlayerState(p, s) res[p]=res[p] or {gold=0, lumber=0}; return res[p][s] end
function SetPlayerState(p, s, v) res[p]=res[p] or {gold=0, lumber=0}; res[p][s]=v end
said={}
function DisplayTimedTextToPlayer(p, _, _, _, text) said[#said+1]={p=p, text=text} end

-- Союзы: флаги на пару (a → b).
ally={}
local function flags(a, b) ally[a]=ally[a] or {}; ally[a][b]=ally[a][b] or {}; return ally[a][b] end
function SetPlayerAllianceStateBJ(a, b, st)
    local f=flags(a, b)
    f.passive = st >= 2; f.vision = st >= 2; f.control = st >= 3; f.adv = st >= 4
end
function SetPlayerAlliance(a, b, kind, on) flags(a, b)[kind]=on end
function GetPlayerAlliance(a, b, kind) return flags(a, b)[kind] == true end
function IsPlayerAlly(a, b) return a == b or flags(a, b).passive == true end
-- ForceEnumAllies, как в игре, включает самого игрока.
function CreateForce() return {set={}} end
function ForceEnumAllies(f, p) for j=0,23 do if IsPlayerAlly(j, p) then f.set[j]=true end end end
function CountPlayersInForceBJ(f) local n=0; for _ in pairs(f.set or {}) do n=n+1 end; return n end
function ForceClear(f) f.set={} end

-- Фреймы и события.
frames={}
local function frame(kind, name) local f={kind=kind, name=name, visible=true, handlers={}, value=0}; frames[#frames+1]=f; return f end
function BlzLoadTOCFile() return true end
function BlzGetOriginFrame() return frame('origin') end
function BlzGetFrameByName(name) return frame('named', name) end
function BlzCreateFrame(tpl, parent) local f=frame('tpl', tpl); f.parent=parent; return f end
function BlzCreateFrameByType(kind, name, parent, inherit) local f=frame(kind, name); f.parent=parent; f.inherit=inherit; return f end
function BlzFrameSetAllPoints() end
function BlzFrameClearAllPoints() end
function BlzFrameSetSize(f, w, h) f.w=w; f.h=h end
function BlzFrameSetAbsPoint(f, pt, x, y) f.x=x; f.y=y end
function BlzFrameSetPoint() end
function BlzFrameSetTexture(f, t) f.tex=t end
function BlzFrameSetText(f, t) f.text=t end
function BlzFrameGetWidth() return 0 end
function BlzFrameSetTextAlignment() end
function BlzFrameSetTooltip(b, t) b.tip=t end
function BlzFrameSetVisible(f, v) f.visible=v end
function BlzFrameSetLevel() end
function BlzFrameSetAlpha() end
function BlzFrameSetEnable() end
function BlzFrameSetMinMaxValue(f, a, b) f.min=a; f.max=b end
function BlzFrameSetStepSize() end
function BlzFrameSetValue(f, v) f.value=v end
function BlzFrameGetValue(f) return f.value end
function CreateTrigger() return {} end
function BlzTriggerRegisterFrameEvent(t, f, ev) t.frame=f; t.ev=ev end
keyTrig=nil
function BlzTriggerRegisterPlayerKeyEvent(t) keyTrig=t end
function TriggerAddAction(t, fn) if t.frame then t.frame.handlers[t.ev]=fn end; t.fn=fn end
function CreateTimer() return {} end
function TimerStart(t, _, _, fn) tickFn=fn end
trigPlayer=0; trigFrame=nil; trigValue=0
function GetTriggerPlayer() return trigPlayer end
function BlzGetTriggerFrame() return trigFrame end
function BlzGetTriggerFrameValue() return trigValue end
function fire(f, ev, player, value)
    trigPlayer=player; trigFrame=f; trigValue=value or 0
    f.handlers[ev]()
end
'''


class AlliesPanelTests(unittest.TestCase):
    def setUp(self, players=4):
        lua = LuaRuntime()
        self.lua = lua
        lua.execute(FIXTURE)
        lua.execute(LOCALIZATION)
        lua.execute(FRAME_PARK)
        lua.execute(PANEL)
        lua.execute(f'for i=0,{players - 1} do playing[i]=true; races[i]="R"; playerCapital[i]={{}} end')
        lua.execute('assert(AlliesPanel_Create()); AP=AlliesPanelState')

    def click_row(self, player, row, kind):
        self.lua.execute(f'fire(AP.rows[{row}].btn["{kind}"], "click", {player})')

    def toggle(self, player):
        self.lua.execute(f'fire(AP.button, "click", {player})')

    def allied(self, a, b):
        return self.lua.eval(f'AP.Allied({a}, {b})')

    def tick(self, seconds):
        self.lua.execute(f'for _=1,{int(seconds / 0.5)} do tickFn() end')

    def test_proposal_accepted_from_toast_makes_mutual_alliance(self):
        self.toggle(0)
        self.click_row(0, 1, 'propose')        # строка 1 у игрока 0 — игрок 1
        self.assertTrue(self.lua.eval('AP.Pending(0, 1)'))
        self.assertFalse(self.allied(0, 1))
        self.lua.execute('fire(AP.toastAccept, "click", 1)')
        self.assertTrue(self.allied(0, 1))
        self.assertFalse(self.lua.eval('AP.Pending(0, 1)'))
        self.assertEqual(self.lua.eval('AP.log[0][#AP.log[0]].key'), 'allies.log.accepted_by')

    def test_limit_blocks_second_alliance(self):
        # DipMode=2: игрок и один союзник.
        self.lua.execute('SetPlayerAllianceStateBJ(0,1,2); SetPlayerAllianceStateBJ(1,0,2)')
        self.toggle(0)
        self.click_row(0, 2, 'propose')
        self.assertFalse(self.lua.eval('AP.Pending(0, 2)'))
        self.assertEqual(self.lua.eval('AP.log[0][#AP.log[0]].key'), 'allies.log.limit_self')

    def test_stale_button_is_ignored(self):
        self.toggle(0)
        self.click_row(0, 1, 'break')            # союза нет — кнопка устарела
        self.click_row(0, 1, 'archont')
        self.assertFalse(self.allied(0, 1))
        self.assertFalse(self.lua.eval('GetPlayerAlliance(0, 1, ALLIANCE_SHARED_ADVANCED_CONTROL)'))

    def test_closed_panel_ignores_row_clicks(self):
        self.click_row(0, 1, 'propose')
        self.assertFalse(self.lua.eval('AP.Pending(0, 1)'))

    def test_offer_expires_after_timeout(self):
        self.toggle(0)
        self.click_row(0, 1, 'propose')
        self.tick(29.5)
        self.assertTrue(self.lua.eval('AP.Pending(0, 1)'))
        self.tick(1)
        self.assertFalse(self.lua.eval('AP.Pending(0, 1)'))
        self.assertEqual(self.lua.eval('AP.log[0][#AP.log[0]].key'), 'allies.log.expired_out')

    def test_break_and_archont(self):
        self.lua.execute('SetPlayerAllianceStateBJ(0,1,2); SetPlayerAllianceStateBJ(1,0,2)')
        self.toggle(0)
        self.click_row(0, 1, 'archont')
        self.assertTrue(self.lua.eval('GetPlayerAlliance(0, 1, ALLIANCE_SHARED_ADVANCED_CONTROL)'))
        self.assertTrue(self.lua.eval('GetPlayerAlliance(0, 1, ALLIANCE_SHARED_CONTROL)'))
        self.click_row(0, 1, 'archont')
        self.assertFalse(self.lua.eval('GetPlayerAlliance(0, 1, ALLIANCE_SHARED_ADVANCED_CONTROL)'))
        self.assertFalse(self.lua.eval('GetPlayerAlliance(0, 1, ALLIANCE_SHARED_CONTROL)'))
        self.click_row(0, 1, 'break')
        self.assertFalse(self.allied(0, 1))
        self.assertFalse(self.allied(1, 0))

    def test_resources_are_clamped_to_stock(self):
        self.lua.execute('res[0]={gold=300, lumber=100}; res[2]={gold=0, lumber=0}')
        self.toggle(0)
        self.click_row(0, 2, 'res')
        self.assertEqual(self.lua.eval('AP.resTarget[0]'), 2)
        self.lua.execute('fire(AP.goldSlider, "slider", 0, 1000); fire(AP.lumberSlider, "slider", 0, 50)')
        self.lua.execute('fire(AP.dialogSend, "click", 0)')
        self.assertEqual(self.lua.eval('res[0].gold'), 0)
        self.assertEqual(self.lua.eval('res[2].gold'), 300)
        self.assertEqual(self.lua.eval('res[2].lumber'), 50)
        self.assertIsNone(self.lua.eval('AP.resTarget[0]'))

    def test_bot_declines_while_diplomat_disabled(self):
        self.lua.execute('udg_AiControl[3]=true')
        self.toggle(0)
        self.click_row(0, 3, 'propose')
        self.assertFalse(self.allied(0, 3))
        self.assertFalse(self.lua.eval('AP.Pending(0, 3)'))
        self.assertEqual(self.lua.eval('AP.log[0][#AP.log[0]].key'), 'allies.log.bot_declines')

    def test_ffa_has_no_actions(self):
        self.lua.execute('DipMode=1')
        self.assertEqual(self.lua.eval('#AP.Actions(0, 1)'), 0)

    def test_vassal_cannot_be_broken_off(self):
        self.lua.execute('Senior[1]=0; SetPlayerAllianceStateBJ(1,0,3); SetPlayerAllianceStateBJ(0,1,2)')
        self.assertEqual(self.lua.eval('AP.Relation(0, 1)'), 'vassal')
        self.assertFalse(self.lua.eval('AP.Has(AP.Actions(0, 1), "break")'))

    def test_eliminated_player_has_no_actions(self):
        self.lua.execute('playerCapital[2]=nil')
        self.assertEqual(self.lua.eval('AP.Relation(0, 2)'), 'out')
        self.assertEqual(self.lua.eval('#AP.Actions(0, 2)'), 0)


class AlliesPanelScrollTests(AlliesPanelTests):
    def setUp(self):
        super().setUp(players=24)

    def test_wheel_and_slider_scroll_rows_to_the_right_player(self):
        self.toggle(0)
        self.lua.execute('fire(AP.rows[1].btn.propose, "wheel", 0, -120)')   # колесо вниз
        self.assertEqual(self.lua.eval('AP.offset[0]'), 1)
        self.click_row(0, 1, 'propose')                                        # теперь строка 1 — игрок 2
        self.assertTrue(self.lua.eval('AP.Pending(0, 2)'))
        # Ползунок: максимум сверху; 23 игрока, 9 строк — смещение до 14.
        self.lua.execute('fire(AP.slider, "slider", 0, 0)')
        self.assertEqual(self.lua.eval('AP.offset[0]'), 14)
        self.lua.execute('fire(AP.slider, "wheel", 0, 120)')
        self.assertEqual(self.lua.eval('AP.offset[0]'), 13)

    def test_render_with_full_lobby(self):
        self.toggle(0)
        self.tick(1)
        self.assertTrue(self.lua.eval('AP.root.visible'))
        self.assertIn('P1', self.lua.eval('AP.rows[1].name.text'))
        self.assertIn('23', self.lua.eval('AP.range.text'))

        self.assertFalse(self.lua.eval('AP.empty.visible'))
        self.assertIn('P0', self.lua.eval('AP.selfRow.name.text'))


class AlliesPanelSoloTests(unittest.TestCase):
    setUp = lambda self: AlliesPanelTests.setUp(self, players=1)
    toggle = AlliesPanelTests.toggle
    tick = AlliesPanelTests.tick

    def test_solo_player_sees_self_row_and_empty_hint(self):
        self.toggle(0)
        self.tick(1)
        self.assertIn('P0', self.lua.eval('AP.selfRow.name.text'))
        self.assertTrue(self.lua.eval('AP.empty.visible'))
        self.assertFalse(self.lua.eval('AP.range.visible'))
        self.assertFalse(self.lua.eval('AP.rows[1].name.visible'))


if __name__ == '__main__':
    unittest.main()
