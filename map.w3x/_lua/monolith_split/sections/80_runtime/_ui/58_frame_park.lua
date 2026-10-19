-- ***************************************************************************
-- *  FramePark
-- Скрытый фрейм может по-прежнему перекрывать игровое поле и ловить мышь.
-- Поэтому скрытие = BlzFrameSetVisible(false) + увод фрейма вниз за нижний
-- край экрана, а показ возвращает запомненные точки привязки. Точки, которые
-- нужно восстанавливать, ставятся через FrameSetAbsPoint/FrameSetPoint.
-- Позиции фреймов — только внешний вид: вызовы безопасны внутри
-- GetLocalPlayer()-веток, каждый клиент уводит фреймы у себя.
-- Только для своих фреймов карты: нативные фреймы игры лишь скрываются
-- (BlzFrameSetVisible) — их исходные привязки не прочитать и не восстановить.
-- Локалы — внутри do-блока: главный чанк war3map.lua упирается в лимит регистров Lua.
FRAME_PARK_Y = -0.5   -- верх уведённого фрейма: ниже нижнего края экрана (y = 0)

do
	local frameAnchors = {}   -- [frame] = { { point, x, y [, rel, relPoint] }, ... }
	local frameParked = {}    -- [frame] = true, пока фрейм уведён за экран

	local function FrameRemember(f, a)
		local list = frameAnchors[f]
		if list == nil then
			list = {}
			frameAnchors[f] = list
		end
		for i = 1, #list do
			if list[i].point == a.point then
				list[i] = a
				return
			end
		end
		list[#list + 1] = a
	end

	-- BlzFrameSetAbsPoint с запоминанием. Уведённый фрейм остаётся за экраном до показа.
	function FrameSetAbsPoint(f, point, x, y)
		FrameRemember(f, { point = point, x = x, y = y })
		if not frameParked[f] then BlzFrameSetAbsPoint(f, point, x, y) end
	end

	-- BlzFrameSetPoint с запоминанием.
	function FrameSetPoint(f, point, rel, relPoint, x, y)
		FrameRemember(f, { point = point, x = x, y = y, rel = rel, relPoint = relPoint })
		if not frameParked[f] then BlzFrameSetPoint(f, point, rel, relPoint, x, y) end
	end

	-- BlzFrameClearAllPoints с забыванием запомненных точек.
	function FrameClearAllPoints(f)
		frameAnchors[f] = nil
		if not frameParked[f] then BlzFrameClearAllPoints(f) end
	end

	-- Увести фрейм за экран или вернуть его, не трогая видимость (для фреймов, чью
	-- видимость ведёт движок). Без запомненных точек фрейм при возврате остаётся
	-- без привязки: такой фрейм расставляет вызывающий (например, UISetup).
	function FramePark(f, park)
		if f == nil or (frameParked[f] == true) == park then return end
		BlzFrameClearAllPoints(f)
		if park then
			frameParked[f] = true
			BlzFrameSetAbsPoint(f, FRAMEPOINT_TOP, 0.4, FRAME_PARK_Y)
			return
		end
		frameParked[f] = nil
		local list = frameAnchors[f] or {}
		for i = 1, #list do
			local a = list[i]
			if a.rel == nil then
				BlzFrameSetAbsPoint(f, a.point, a.x, a.y)
			else
				BlzFrameSetPoint(f, a.point, a.rel, a.relPoint, a.x, a.y)
			end
		end
	end

	-- Показать фрейм на месте или скрыть и увести за нижний край экрана.
	function FrameSetShown(f, show)
		if f == nil then return end
		BlzFrameSetVisible(f, show)
		FramePark(f, not show)
	end
end
