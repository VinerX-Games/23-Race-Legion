"""Скрытие фреймов с уводом за нижний край экрана (58_frame_park.lua)."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/_ui/58_frame_park.lua'

FIXTURE = r'''
FRAMEPOINT_TOP='t'; FRAMEPOINT_TOPLEFT='tl'; FRAMEPOINT_BOTTOMRIGHT='br'
function BlzFrameClearAllPoints(f) f.pts={} end
function BlzFrameSetAbsPoint(f,pt,x,y) f.pts[pt]={x=x, y=y} end
function BlzFrameSetPoint(f,pt,rel,relPt,x,y) f.pts[pt]={rel=rel, relPt=relPt, x=x, y=y} end
function BlzFrameSetVisible(f,v) f.visible=v end
function frame() return {pts={}, visible=true} end
'''


class FrameParkTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute(FIXTURE)
        self.lua.execute(SECTION.read_text(encoding='utf-8'))

    def test_hidden_frame_goes_below_screen_and_comes_back(self):
        self.lua.execute('''
            parent=frame(); f=frame()
            FrameSetAbsPoint(f, FRAMEPOINT_TOPLEFT, 0.1, 0.5)
            FrameSetPoint(f, FRAMEPOINT_BOTTOMRIGHT, parent, FRAMEPOINT_BOTTOMRIGHT, -0.01, 0.02)
            FrameSetShown(f, false)''')
        self.assertFalse(self.lua.eval('f.visible'))
        self.assertIsNone(self.lua.eval('f.pts.tl'))
        self.assertEqual(self.lua.eval('f.pts.t.x'), 0.4)
        self.assertLess(self.lua.eval('f.pts.t.y'), 0.0)
        self.lua.execute('FrameSetShown(f, true)')
        self.assertTrue(self.lua.eval('f.visible'))
        self.assertIsNone(self.lua.eval('f.pts.t'))
        self.assertEqual(self.lua.eval('f.pts.tl.y'), 0.5)
        self.assertTrue(self.lua.eval('f.pts.br.rel == parent'))

    def test_moving_hidden_frame_keeps_it_below_screen(self):
        self.lua.execute('''
            f=frame()
            FrameSetAbsPoint(f, FRAMEPOINT_TOPLEFT, 0.1, 0.5)
            FrameSetShown(f, false)
            FrameClearAllPoints(f)
            FrameSetAbsPoint(f, FRAMEPOINT_TOPLEFT, 0.2, 0.3)''')
        self.assertLess(self.lua.eval('f.pts.t.y'), 0.0)
        self.lua.execute('FrameSetShown(f, true)')
        self.assertEqual(self.lua.eval('f.pts.tl.x'), 0.2)
        self.assertEqual(self.lua.eval('f.pts.tl.y'), 0.3)

    def test_park_keeps_visibility_and_repeated_calls_are_noop(self):
        self.lua.execute('''
            f=frame(); FramePark(f, true); f.visible='engine'
            FramePark(f, true); FramePark(nil, true); FrameSetShown(nil, false)''')
        self.assertEqual(self.lua.eval('f.visible'), 'engine')
        self.assertLess(self.lua.eval('f.pts.t.y'), 0.0)
        # Без запомненных точек фрейм возвращается без привязки: его ставит вызывающий.
        self.lua.execute('FramePark(f, false)')
        self.assertIsNone(self.lua.eval('next(f.pts)'))


if __name__ == '__main__':
    unittest.main()
