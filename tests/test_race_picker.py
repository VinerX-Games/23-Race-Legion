"""Панель выбора расы (63_race_picker.lua) на модели нативов фреймов."""
import re
import sys
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from l10n_fixture import install_loc  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / 'map.w3x/_lua/monolith_split/sections'
FRAME_PARK = (SECTIONS / '80_runtime/_ui/58_frame_park.lua').read_text(encoding='utf-8')
LOCALIZATION = (SECTIONS / '03_localization.lua').read_text(encoding='utf-8')

FIXTURE = r'''
FRAMEPOINT_TOPLEFT='tl'; FRAMEPOINT_BOTTOMLEFT='bl'; FRAMEPOINT_BOTTOMRIGHT='br'; FRAMEPOINT_TOP='t'
TEXT_JUSTIFY_TOP=1; TEXT_JUSTIFY_LEFT=2; TEXT_JUSTIFY_MIDDLE=3; TEXT_JUSTIFY_CENTER=4
FRAMEEVENT_CONTROL_CLICK='click'; ORIGIN_FRAME_GAME_UI='gameui'
bj_MAX_PLAYER_SLOTS=24
MINIMAP_W=0.16; MINIMAP_H=0.141   -- из 59_ui_setup.lua
function FourCC(s) return s end
function Player(i) return i end
function GetPlayerId(p) return p end
localPlayer=0
function GetLocalPlayer() return localPlayer end
function ProbeLogWrite() end
function ProbeStep(_, f) f() end

-- Подсказки: сложность задаётся числом «●».
diff={}
function BlzGetAbilityExtendedTooltip(a) return 'РАСА: x|nСложность: ' .. string.rep('●', diff[a] or 3) end
function GetObjectName(a) return a end
function BlzGetAbilityIcon(a) return 'icon:' .. a end

frames={}; hidden={}; uiHidden=nil; buttons={}; clicks={}
local function frame(kind, name) local f={kind=kind,name=name,visible=true}; frames[#frames+1]=f; return f end
function BlzLoadTOCFile() return true end
function BlzGetOriginFrame() return frame('origin') end
function BlzGetFrameByName(n) hidden[n]=hidden[n] or frame('named', n); return hidden[n] end
function BlzCreateFrameByType(kind, name, parent) local f=frame(kind, name); f.parent=parent; if kind=='GLUEBUTTON' then buttons[#buttons+1]=f end; return f end
function BlzCreateFrame(name) return frame('tpl', name) end
function BlzFrameSetAllPoints() end
function BlzFrameClearAllPoints(f) f.x=nil; f.y=nil end
function BlzFrameSetSize(f,w,h) f.w=w; f.h=h end
function BlzFrameSetAbsPoint(f,pt,x,y) f.x=x; f.y=y end
function BlzFrameSetPoint() end
function BlzFrameSetTexture(f,t) f.tex=t; if f.parent then f.parent.iconTex=t end end
function BlzFrameSetText(f,t) f.text=t end
function BlzFrameSetTextAlignment() end
function BlzFrameSetTooltip(b,t) b.tip=t end
function BlzFrameSetVisible(f,v) f.visible=v end
function BlzFrameGetChild(f,i) f.kids=f.kids or {}; f.kids[i]=f.kids[i] or frame('child', i); return f.kids[i] end
function BlzFrameSetScale(f,v) f.scale=v end
function BlzFrameSetLevel(f,v) f.level=v end
function BlzFrameGetParent(f) return frame('cell') end
function BlzFrameSetEnable() end
function BlzHideOriginFrames(v) uiHidden=v end
function CreateTrigger() return {} end
function BlzTriggerRegisterFrameEvent(t,f) t.frame=f end
function TriggerAddAction(t,fn) if t.frame then t.frame.onClick=fn end; t.fn=fn end
function CreateTimer() return {} end
function TimerStart(t,_,_,fn) t.fn=fn end
function DestroyTimer() end
-- Регион на всю карту ломает пути юнитов: модуль не должен его создавать.
function CreateRegion() error('CreateRegion запрещён в панели выбора расы') end

-- Юниты и событие клика.
function GetUnitTypeId(u) return (u and not u.removed) and u.id or 0 end
function GetOwningPlayer(u) return u.owner end
function UnitRemoveAbility(u,a) u.abil[a]=nil end
trigPlayer=0; trigFrame=nil
function GetTriggerPlayer() return trigPlayer end
function GetTriggerFrame() return trigFrame end
BlzGetTriggerFrame=GetTriggerFrame
function UISetup() uiSetupCalls=(uiSetupCalls or 0)+1 end
picked={}
function makeAction(name) _G[name]=function(c) picked[#picked+1]={name=name,caster=c}; c.removed=true end end
function Trig_Units_Actions(c) picked[#picked+1]={name='Trig_Units_Actions',caster=c} end
noted={}
function CustomHudNoteRace(pi,a) noted[pi]=a end
function IncomeUISetVisible(v) incomeShown=v end
'''


class RacePickerTests(unittest.TestCase):
    def setUp(self):
        lua = LuaRuntime()
        self.lua = lua
        lua.execute(FIXTURE)
        lua.execute(LOCALIZATION)
        lua.execute(FRAME_PARK)
        src = (SECTIONS / '80_runtime/_ui/63_race_picker.lua').read_text(encoding='utf-8')
        for name in set(re.findall(r'"(Trig_Race_[A-Za-z0-9_]+_Actions)"', src)):
            lua.execute(f'makeAction("{name}")')
        lua.execute(src)
        lua.execute('RacePicker_Init(); RacePicker_Create()')

    def spawn_circle(self, owner):
        self.lua.execute(f'''
            circle={{id='h0HJ', owner={owner}, abil={{A02A=1, A0I1=1, A12Q=1, Apiv=1}}}}
            RacePickerAdopt(circle)''')

    def test_hidden_panel_is_parked_off_screen(self):
        # Скрытая панель не должна ловить клики по миру: кнопки уведены вниз за экран.
        self.assertLess(self.lua.eval('buttons[1].y'), 0.0)
        self.spawn_circle(0)
        self.assertGreaterEqual(self.lua.eval('buttons[1].y'), 0.0)
        self.pick('A02A')
        self.assertLess(self.lua.eval('buttons[1].y'), 0.0)

    def test_dead_zone_shrunk_while_picking_and_restored(self):
        # ConsoleUI child 5 блокирует клики над командной картой даже скрытым.
        self.lua.execute('deadZone = BlzFrameGetChild(BlzGetFrameByName("ConsoleUI", 0), 5)')
        self.spawn_circle(0)
        self.assertEqual(self.lua.eval('deadZone.scale'), 0.001)
        self.pick('A02A')
        self.assertEqual(self.lua.eval('deadZone.scale'), 1.0)

    def test_layout_fits_4_3_and_odd_groups_are_staggered(self):
        self.spawn_circle(0)
        self.lua.execute('''
            minX, maxX = 1, 0
            for _,b in ipairs(buttons) do
                minX=math.min(minX,b.x); maxX=math.max(maxX,b.x+b.w)
            end''')
        self.assertGreaterEqual(self.lua.eval('minX'), 0.0)
        self.assertLessEqual(self.lua.eval('maxX'), 0.8)
        # 35 рас + случайная + камера.
        self.assertEqual(self.lua.eval('#buttons'), 37)
        # Эльфы (5): нижний ряд сдвинут на пол-иконки; Альянс (8): ряды ровно друг под другом.
        self.lua.execute('''
            function rowsOf(ids)
                local set={}; for _,a in ipairs(ids) do set['icon:'..a]=true end
                local hi, lo = {}, {}
                for _,b in ipairs(buttons) do if set[b.iconTex] then
                    if b.y > 0.03 then hi[#hi+1]=b.x else lo[#lo+1]=b.x end
                end end
                table.sort(hi); table.sort(lo); return hi, lo
            end
            elfHi, elfLo = rowsOf({'A0HQ','A0HL','A0HU','A0OK','A14O'})
            allyHi, allyLo = rowsOf({'A02A','A0Y0','A0HN','A0HO','A121','A0HM','A0HS','A0SD'})''')
        self.assertEqual((self.lua.eval('#elfHi'), self.lua.eval('#elfLo')), (3, 2))
        self.assertAlmostEqual(self.lua.eval('elfLo[1] - elfHi[1]'), (0.032 + 0.0032) / 2)
        self.assertAlmostEqual(self.lua.eval('allyLo[1] - allyHi[1]'), 0.0)

    def test_group_sorted_by_difficulty_stable(self):
        self.lua.execute('''
            diff={A0HQ=3, A0HL=3, A0HU=2, A0OK=3, A14O=1}
            local list={}
            for _,id in ipairs({'A0HQ','A0HL','A0HU','A0OK','A14O'}) do list[#list+1]={abil=id} end
            RacePickerSortGroup(list)
            order={}; for i,e in ipairs(list) do order[i]=e.abil end''')
        self.assertEqual(list(self.lua.eval('order').values()), ['A14O', 'A0HU', 'A0HQ', 'A0HL', 'A0OK'])

    def test_circle_created_before_panel_is_stripped_when_ready(self):
        lua = LuaRuntime()
        lua.execute(FIXTURE)
        install_loc(lua)
        lua.execute(FRAME_PARK)
        lua.execute((SECTIONS / '80_runtime/_ui/63_race_picker.lua').read_text(encoding='utf-8'))
        lua.execute('''
            circle={id='h0HJ', owner=0, abil={A02A=1, A0I1=1, Apiv=1}}
            RacePicker_Init(); RacePickerAdopt(circle)''')
        self.assertEqual(lua.eval('circle.abil.A02A'), 1)
        lua.execute('RacePicker_Create()')
        self.assertIsNone(lua.eval('circle.abil.A02A'))
        self.assertTrue(lua.eval('uiHidden'))

    def test_circle_strips_old_menu_and_hides_ui(self):
        self.spawn_circle(0)
        self.assertIsNone(self.lua.eval('circle.abil.A02A'))
        self.assertIsNone(self.lua.eval('circle.abil.A0I1'))
        self.assertIsNone(self.lua.eval('circle.abil.A12Q'))
        self.assertEqual(self.lua.eval('circle.abil.Apiv'), 1)
        self.assertTrue(self.lua.eval('uiHidden'))
        self.assertFalse(self.lua.eval('incomeShown'))

    def pick(self, abil, player=0):
        self.lua.execute(f'''
            local target
            for _,b in ipairs(buttons) do if b.iconTex=='icon:{abil}' then target=b end end
            trigPlayer={player}; trigFrame=target; target.onClick()''')

    def test_pick_calls_race_action_with_circle_and_restores_ui(self):
        self.spawn_circle(0)
        self.pick('A0QN')
        self.assertEqual(self.lua.eval('picked[1].name'), 'Trig_Units_Actions')
        self.assertEqual(self.lua.eval('picked[2].name'), 'Trig_Race_Elements_O_Actions')
        self.assertTrue(self.lua.eval('picked[2].caster == circle'))
        self.assertEqual(self.lua.eval('noted[0]'), 'A0QN')
        self.assertFalse(self.lua.eval('uiHidden'))
        self.assertTrue(self.lua.eval('incomeShown'))
        self.assertEqual(self.lua.eval('uiSetupCalls'), 1)

    def test_other_player_cannot_pick_with_foreign_circle(self):
        self.spawn_circle(0)
        self.pick('A02A', player=1)
        self.assertEqual(self.lua.eval('#picked'), 0)
        self.assertTrue(self.lua.eval('uiHidden'))


if __name__ == '__main__':
    unittest.main()
