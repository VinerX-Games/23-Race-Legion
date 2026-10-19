"""Exercise the income tooltip with mocked frame natives."""
import unittest
import re
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]


def plain_text(value):
    return re.sub(r"\|c[0-9a-fA-F]{8}|\|r", "", value)


class IncomeTooltipTests(unittest.TestCase):
    def setUp(self):
        lua = LuaRuntime()
        self.lua = lua
        lua.execute(r'''
            texts = {}
            visible = {}
            sizes = {}; points = {}
            FRAMEPOINT_TOPLEFT='topLeft'; FRAMEPOINT_TOPRIGHT='topRight'; FRAMEPOINT_BOTTOMRIGHT='bottomRight'
            IncomeTextFr, tooltipTitle, tooltipBody = 'amount', 'title', 'body'
            function BlzFrameSetText(frame, text) texts[frame] = text end
            function BlzGetFrameByName(name, context) return name .. context end
            function BlzGetOriginFrame() return 'gameUI' end
            function BlzCreateFrameByType(kind, name) return name end
            function BlzCreateFrame(name, parent, priority, context) return name .. context end
            function BlzFrameGetChild(frame, child) return frame .. 'child' .. child end
            function BlzFrameSetVisible(frame, value) visible[frame] = value end
            function BlzLoadTOCFile() end
            function BlzFrameSetAbsPoint() end
            function BlzFrameSetPoint(frame, point, relative, relativePoint, x, y)
                points[frame]=points[frame] or {}; points[frame][point]=relative
            end
            function BlzFrameSetSize(frame, width, height) sizes[frame]={width=width,height=height} end
            function BlzFrameClearAllPoints(frame) points[frame]={} end
            function BlzFrameGetHeight(frame)
                local size=sizes[frame]
                if size and size.height>0 then return size.height end
                local text=(texts[frame] or ''):gsub('|c%x%x%x%x%x%x%x%x',''):gsub('|r',''):gsub('|n','\n')
                local lines=0
                for line in (text..'\n'):gmatch('(.-)\n') do
                    lines=lines+math.max(1,math.ceil((utf8.len(line) or #line)/((size and size.width or 0.3)/0.005)))
                end
                return lines*0.01
            end
            function BlzFrameSetTextAlignment() end
            function BlzFrameSetEnable() end
            function BlzFrameSetScale() end
            function BlzFrameSetAllPoints() end
            function BlzFrameSetTooltip() end
            function BlzFrameSetTexture() end
            function BlzFrameSetLevel() end
            function GetLocalPlayer() return 0 end
            function GetPlayerId(p) return p end
            function FourCC(code) return code end
            function GetPlayerTechCount(p, code) return 1 end
            function I2S(value) return tostring(value) end
            function R2I(value) return math.modf(value) end
            function R2S(value) return tostring(value) end
            function TimerGetRemaining(timer) return 12.3 end
            function GetUnitState(unit) return unit.life end
            function GetOwningPlayer(unit) return unit.owner end
            function GetUnitName(unit) return unit.name end
            PLAYER_STATE_RESOURCE_FOOD_USED = 1
            function GetPlayerState(p, state) return state == 1 and 40 or 100 end
            balance = {[0] = 100}
            income = {[0] = 150}
            disincome = {[0] = 20}
            logistic = {[0] = 10}
            corruption = {[0] = 5}
            additional = {[0] = 7}
            AllyTax = {[0] = 0}
            IncomeMod = 1
            DisOn = true
            incomeW = {[0] = 15}
            udg_IncomeTimerSecond = 1
            CityPlayerCount = {[0] = 5}
            CityCount = 20
            PercentWin = 65
            udg_GameMode = 3
            playerCapital = {[0] = {life = 100, owner = 0, name = 'Столица'}}
            udg_UnitsCount = {[0] = 40}
        ''')
        lua.execute((ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/'
                     '_ui/58_frame_park.lua').read_text(encoding='utf-8'))
        ui = (ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/'
              '_ui/60_income_tooltip.lua').read_text(encoding='utf-8')
        lua.execute(ui)
        lua.globals().Face2()
        source = (ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/'
                  'triggers/02_game_modes.lua').read_text(encoding='utf-8')
        lua.execute(source.split('function InitTrig_ResoursesInterface_Copy()', 1)[0])

    def refresh(self):
        self.lua.globals().Trig_ResoursesInterface_Copy_Actions()
        return self.lua.globals().texts['BoxedTextValue0']

    def test_income_states_and_bonus_text(self):
        lua = self.lua
        for amount, title in [(100, 'Чистый доход'), (0, 'Доходы равны расходам'),
                              (-100, 'Чистый убыток')]:
            with self.subTest(balance=amount):
                lua.globals().balance[0] = amount
                lua.globals().Trig_ResoursesInterface_Copy_Actions()
                texts = lua.globals().texts
                self.assertIn(title, texts['BoxedTextTitle0'])
                body = texts['BoxedTextValue0']
                self.assertIn('Дополнительный доход: |cffc8e087+7|cffced4da', body)
                self.assertIn('Налог союзникам', body)
                self.assertIn('через 13 сек.', plain_text(body))
                self.assertNotIn('?', body)

    def test_no_expenses_mode_does_not_show_stale_deductions(self):
        self.lua.globals().DisOn = False
        body = self.refresh()
        self.assertNotIn('-20', body)
        self.assertNotIn('-10', body)
        self.assertNotIn('+7', body)
        self.assertIn('Расходы отключены', body)

    def test_tax_and_modifier_are_separate(self):
        self.lua.globals().IncomeMod = 1.2
        self.lua.globals().AllyTax[0] = 0.1
        body = self.refresh()
        self.assertIn('10% (-18)', plain_text(body))
        self.assertIn('|cffef8173-18|cffced4da', body)
        self.assertIn('налога: |cffc8e087+162|cffced4da', body)

    def test_top_counter_matches_integer_payout(self):
        self.lua.globals().balance[0] = 100.9
        self.refresh()
        self.assertEqual(self.lua.globals().texts['MyTextFrame'], '|cffc8e087+100|cffced4da|r')

    def test_state_replaces_food_hover_and_shows_domination(self):
        self.refresh()
        state = plain_text(self.lua.globals().texts['BoxedTextValue1'])
        self.assertIn('Города: 5 / 20', state)
        self.assertIn('25.0%', state)
        self.assertIn('Столица: Столица', state)
        self.assertIn('Осталось захватить: 8', state)
        self.assertNotIn('Пища', state)
        self.assertFalse(self.lua.globals().visible['ResourceBarFrame0child3'])
        self.assertIsNone(self.lua.globals().texts['ResourceBarSupplyText0'])

    def test_empty_map_and_lost_capital_outside_domination(self):
        self.lua.globals().CityCount = 0
        self.lua.globals().udg_GameMode = 1
        self.lua.globals().playerCapital[0].owner = 1
        self.refresh()
        state = plain_text(self.lua.globals().texts['BoxedTextValue1'])
        self.assertIn('Доля территории: 0.0%', state)
        self.assertIn('Столица: Не назначена', state)
        self.assertNotIn('Осталось захватить', state)

    def test_backgrounds_follow_automatic_text_height_and_shrink(self):
        self.refresh()
        lua = self.lua
        lua.execute('''
            for i=0,1 do
                local body='BoxedTextValue'..i
                assert(sizes[body].height==0, 'text must measure its natural height')
                assert(points[body].bottomRight==nil, 'text must not stretch to background bottom')
                assert(math.abs(sizes['BoxedText'..i].height-BlzFrameGetHeight(body)-0.025)<0.0001)
            end
            oldHeight=sizes.BoxedText1.height
        ''')
        lua.globals().udg_GameMode = 1
        self.refresh()
        lua.execute('assert(sizes.BoxedText1.height<oldHeight, "shorter state must shrink background")')

    def test_long_capital_name_wraps_and_expands_state_tooltip(self):
        self.refresh()
        lua = self.lua
        old = lua.globals().sizes['BoxedText1']['height']
        lua.globals().playerCapital[0].name = 'Очень длинное название столицы ' * 5
        self.refresh()
        self.assertGreater(lua.globals().sizes['BoxedText1']['height'], old)


if __name__ == '__main__':
    unittest.main()
