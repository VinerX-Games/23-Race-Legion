-- ***************************************************************************
-- *  RacePicker
-- Панель выбора расы на фреймах вместо командной карты кольца выбора (h0HJ).
-- Пока у игрока есть кольцо, у него локально скрыт стандартный интерфейс
-- (кроме кнопок «Меню» и «Чат») и показана панель. Клик по иконке — синхронное
-- событие фрейма; он вызывает тот же Trig_Race_*_Actions, что и способность
-- выбора, передавая кольцо вместо кастера. Старый путь через способности
-- отключён: при появлении кольца с него снимаются способности выбора и листания
-- страниц (если панель не создалась, кольцо остаётся со старой командной картой).
local RP_CIRCLE = FourCC('h0HJ')
local RP_ICON = 0.032          -- сторона иконки
local RP_GAP = 0.0032          -- зазор между иконками
local RP_GROUP_GAP = 0.0256    -- зазор между группами
local RP_BOTTOM = 0.013        -- нижний ряд иконок над краем экрана
local RP_LABEL_H = 0.012
local RP_TIP_W = 0.30
local RP_CAM_ICON = "ReplaceableTextures\\CommandButtons\\BTNRallyPoint.blp"

-- Группы и расы: { способность выбора, функция действий [, доп. обработчик SPELL_EFFECT] }.
-- Внутри группы порядок задаётся сложностью из подсказки (число «●»), см. RacePickerSortGroup.
local RP_GROUPS = {
	{ "АЛЬЯНС", {
		{ 'A02A', "Trig_Race_Alliance_Actions" },
		{ 'A0Y0', "Trig_Race_Stromgard_O_Actions" },
		{ 'A0HN', "Trig_Race_Dalaran_O_Actions" },
		{ 'A0HO', "Trig_Race_KulTiras_O_Actions" },
		{ 'A121', "Trig_Race_Gilneas_Actions" },
		{ 'A0HM', "Trig_Race_Red_Orden_O_Actions" },
		{ 'A0HS', "Trig_Race_Draeneis_O_Actions" },
		{ 'A0SD', "Trig_Race_Gnomes_Actions" },
	} },
	{ "ОРДА", {
		{ 'A0YV', "Trig_Race_Horde_Actions" },
		{ 'A1JN', "Trig_Race_HordeW2_Actions" },
		{ 'A1JL', "Trig_Race_FelOrk_Actions" },
		{ 'A17N', "Trig_Race_Ogres_Actions" },
		{ 'A1EG', "Trig_Race_IceTrols_Actions" },
		{ 'A1DZ', "Trig_Race_JungleTrolls_Actions" },
		{ 'A1FN', "Trig_Race_ForestTrolls_Actions" },
		{ 'A0AC', "Trig_Race_Goblins_O_Actions" },
	} },
	{ "ТЬМА", {
		{ 'A0HV', "Trig_Race_Undead_O_Actions" },
		{ 'A155', "Trig_Race_Forsaken_Actions" },
		{ 'A1HA', "Trig_Race_CultOfDamned_Actions" },
		{ 'A0MY', "Trig_Race_Demon_O_Actions" },
		{ 'A0HW', "Trig_Race_Bezlikie_O_Actions" },
		{ 'A0HT', "Trig_Race_Nerubs_O_Actions" },
		{ 'A0HX', "Trig_Race_Kult_Sum_Molota_O_Actions" },
		{ 'A0J7', "Trig_Race_Silitids_O_Actions" },
	} },
	{ "ЭЛЬФЫ", {
		{ 'A0HQ', "Trig_Race_Blood_Elves_O_Actions" },
		{ 'A0HL', "Trig_Race_nightelf_Actions" },
		{ 'A0HU', "Trig_Race_Nocnorogdennue_O_Actions" },
		{ 'A0OK', "Trig_Race_Illidari_O_Actions" },
		{ 'A14O', "Trig_Race_Nagi_Actions" },
	} },
	{ "НЕЙТРАЛЬНЫЕ", {
		{ 'A0HR', "Trig_Race_Bandits_O_Actions" },
		{ 'A0HP', "Trig_Race_Vryculs_O_Actions" },
		{ 'A0QQ', "Trig_Race_Argvinol_O_Actions" },
		{ 'A0QN', "Trig_Race_Elements_O_Actions", "Trig_Units_Actions" },
		{ 'A1I6', "Trig_Race_Pandarens_Actions" },
		{ 'A0RQ', "Trig_Race_Dragon_O_Actions" },
	} },
}
local RP_RANDOM = { 'A12Q', "Trig_Race_Random_Actions" }
-- Кнопки страниц старого меню и раса, которой нет в панели (Драконий Союз).
local RP_OLD_MENU = { 'A0I1', 'A0HZ', 'A1GW', 'A0QR', 'A1MZ' }

local rpCircle = {}      -- [pi] = кольцо выбора игрока
local rpShown = false    -- панель показана локальному игроку
local rpReady = false    -- панель создана (одинаково у всех клиентов)
local rpRoot, rpHint
local rpPlaced = {}      -- фреймы панели с абсолютной позицией

-- Скрытый фрейм может продолжать ловить мышь, поэтому при скрытии фреймы панели
-- ещё и уводятся вниз за экран, а при показе возвращаются. Только локально.
local function RpPlace(f, point, x, y)
	FrameSetAbsPoint(f, point, x, y)
	rpPlaced[#rpPlaced + 1] = f
end

local function RpSetShown(show)
	BlzFrameSetVisible(rpRoot, show)
	for i = 1, #rpPlaced do FramePark(rpPlaced[i], not show) end
end

-- Снять с кольца старое меню выбора, чтобы раса выбиралась только через панель.
local function RpStripOldMenu(u)
	for i = 1, #RP_OLD_MENU do UnitRemoveAbility(u, FourCC(RP_OLD_MENU[i])) end
	UnitRemoveAbility(u, FourCC(RP_RANDOM[1]))
	for g = 1, #RP_GROUPS do
		local list = RP_GROUPS[g][2]
		for i = 1, #list do UnitRemoveAbility(u, FourCC(list[i][1])) end
	end
end

local function RpValid(u, p)
	return u ~= nil and GetUnitTypeId(u) == RP_CIRCLE and GetOwningPlayer(u) == p
end

-- Сложность из подсказки выбора: число заполненных «●». Подсказки одинаковы у всех
-- клиентов, поэтому порядок детерминирован.
local function RpDifficulty(abil)
	local s = BlzGetAbilityExtendedTooltip(abil, 0) or ""
	local _, n = string.gsub(s, "●", "")
	return n
end

-- Устойчивая сортировка вставками: при равной сложности сохраняется порядок из таблицы.
function RacePickerSortGroup(list)
	for i = 1, #list do
		list[i].d = RpDifficulty(list[i].abil)
	end
	for i = 2, #list do
		local e, j = list[i], i - 1
		while j >= 1 and list[j].d > e.d do
			list[j + 1] = list[j]
			j = j - 1
		end
		list[j + 1] = e
	end
end

-- Стандартный интерфейс: скрыть всё, кроме «Меню» и «Чата». Только локально.
-- Общий для панелей выбора расы и настроек хоста.
-- Нативные фреймы консоли только скрываются, без увода за экран: их исходные
-- привязки не прочитать, и после возврата они перекрывали игровое поле.
function StandardUISetVisible(show)
	BlzHideOriginFrames(not show)
	local f = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	if f ~= nil then BlzFrameSetVisible(f, show) end
	f = BlzGetFrameByName("ResourceBarFrame", 0)
	if f ~= nil then BlzFrameSetVisible(f, show) end
	f = BlzGetFrameByName("UpperButtonBarFrame", 0)
	if f ~= nil then BlzFrameSetVisible(f, true) end
	f = BlzGetFrameByName("UpperButtonBarQuestsButton", 0)
	if f ~= nil then BlzFrameSetVisible(f, show) end
	f = BlzGetFrameByName("UpperButtonBarAlliesButton", 0)
	if f ~= nil then BlzFrameSetVisible(f, show) end
	if IncomeUISetVisible ~= nil then IncomeUISetVisible(show) end
	if CustomHudSetVisible ~= nil then CustomHudSetVisible(show) end
end

-- Показать или спрятать панель локальному игроку по наличию у него кольца.
local function RpApply()
	if rpRoot == nil then return end
	local p = GetLocalPlayer()
	local open = RpValid(rpCircle[GetPlayerId(p)], p)
	if open == rpShown then return end
	rpShown = open
	RpSetShown(open)
	StandardUISetVisible(not open)
	-- Миникарта на выборе расы: в правом верхнем углу, над подсказками и иконками,
	-- без рамки. После выбора UISetup возвращает её и рамку на место.
	local minimap = BlzGetFrameByName("MiniMapFrame", 0)
	if open and minimap ~= nil then
		FrameSetShown(BlzGetFrameByName("MinimapBorder", 0), false)
		BlzFrameSetVisible(minimap, true)
		BlzFrameClearAllPoints(minimap)
		BlzFrameSetAbsPoint(minimap, FRAMEPOINT_TOPRIGHT, 0.795, 0.595)
		BlzFrameSetAbsPoint(minimap, FRAMEPOINT_BOTTOMLEFT, 0.645, 0.445)
	end
	if not open and UISetup ~= nil then UISetup() end
end

local function RpTick()
	for pi = 0, bj_MAX_PLAYER_SLOTS - 1 do
		if rpCircle[pi] ~= nil and not RpValid(rpCircle[pi], Player(pi)) then
			rpCircle[pi] = nil
		end
	end
	RpApply()
end

-- Снять фокус с кнопки, иначе пробел/Enter продолжают нажимать её.
local function RpRelease(f, p)
	if GetLocalPlayer() == p then
		BlzFrameSetEnable(f, false)
		BlzFrameSetEnable(f, true)
	end
end

local function RpPick(entry)
	return function()
		local p = GetTriggerPlayer()
		local pi = GetPlayerId(p)
		RpRelease(BlzGetTriggerFrame(), p)
		local u = rpCircle[pi]
		if not RpValid(u, p) then return end
		rpCircle[pi] = nil
		RpApply()
		ProbeLogWrite("[RACEPICK] p=" .. pi .. " abil=" .. entry.id)
		-- Порядок как у способности: сначала обработчики SPELL_EFFECT, потом SPELL_FINISH.
		if entry.extra ~= nil and _G[entry.extra] ~= nil then _G[entry.extra](u) end
		local act = _G[entry.fn]
		if act ~= nil then act(u) end
		if CustomHudNoteRace ~= nil then CustomHudNoteRace(pi, entry.abil) end
	end
end

local function RpCamera()
	local p = GetTriggerPlayer()
	RpRelease(BlzGetTriggerFrame(), p)
	local u = rpCircle[GetPlayerId(p)]
	if GetLocalPlayer() == p and RpValid(u, p) then
		PanCameraToTimed(GetUnitX(u), GetUnitY(u), 0.4)
	end
end

local rpTipTop = 0

local function RpButton(texture, tip, x, y, id, onClick)
	local b = BlzCreateFrameByType("GLUEBUTTON", "RacePickButton", rpRoot, "ScoreScreenTabButtonTemplate", id)
	BlzFrameSetSize(b, RP_ICON, RP_ICON)
	RpPlace(b, FRAMEPOINT_BOTTOMLEFT, x, y)
	local icon = BlzCreateFrameByType("BACKDROP", "RacePickIcon", b, "", id)
	BlzFrameSetAllPoints(icon, b)
	BlzFrameSetTexture(icon, texture, 0, true)

	-- Подсказка растёт вверх от общей линии над панелью, по горизонтали — над иконкой.
	local box = BlzCreateFrame("BoxedTextBackgroundTemplate", b, 0, id)
	local text = BlzCreateFrame("HudBody", box, 0, id)
	BlzFrameSetTextAlignment(text, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
	BlzFrameSetSize(text, RP_TIP_W, 0)
	local tx = math.max(0.005, math.min(x + RP_ICON / 2 - RP_TIP_W / 2, 0.795 - RP_TIP_W))
	-- Подсказку показывает и прячет движок: её не уводим, она стоит на месте.
	BlzFrameSetAbsPoint(text, FRAMEPOINT_BOTTOMLEFT, tx, rpTipTop)
	BlzFrameSetText(text, tip)
	BlzFrameSetPoint(box, FRAMEPOINT_TOPLEFT, text, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
	BlzFrameSetPoint(box, FRAMEPOINT_BOTTOMRIGHT, text, FRAMEPOINT_BOTTOMRIGHT, 0.007, -0.007)
	BlzFrameSetTooltip(b, box)
	BlzFrameSetVisible(box, false)

	local t = CreateTrigger()
	BlzTriggerRegisterFrameEvent(t, b, FRAMEEVENT_CONTROL_CLICK)
	TriggerAddAction(t, onClick)
	return b
end

local function RpEntry(raw)
	local abil = FourCC(raw[1])
	return { id = raw[1], abil = abil, fn = raw[2], extra = raw[3] }
end

local function RpRaceTip(abil)
	return (GetObjectName(abil) or "") .. "|n" .. (BlzGetAbilityExtendedTooltip(abil, 0) or "")
end

function RacePicker_Create()
	if rpRoot ~= nil then return end
	if not BlzLoadTOCFile("war3mapimported\\HudText.toc") or not BlzLoadTOCFile("war3mapimported\\BoxedText.toc") then
		ProbeLogWrite("[RACEPICK] templates not loaded, keeping command card")
		return
	end
	local parent = BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0)
	-- Корень не растягивается на экран: все дочерние фреймы позиционируются сами.
	rpRoot = BlzCreateFrameByType("FRAME", "RacePickRoot", parent, "", 0)
	BlzFrameSetSize(rpRoot, 0.001, 0.001)
	BlzFrameSetAbsPoint(rpRoot, FRAMEPOINT_BOTTOMLEFT, 0.0, 0.0)

	-- Раскладка: группы по два ряда; нечётные — нижний ряд сдвинут на пол-иконки.
	local groups, total = {}, 0
	for g = 1, #RP_GROUPS do
		local list = {}
		for i = 1, #RP_GROUPS[g][2] do list[i] = RpEntry(RP_GROUPS[g][2][i]) end
		RacePickerSortGroup(list)
		local top = (#list + 1) // 2
		local w = top * RP_ICON + (top - 1) * RP_GAP
		groups[g] = { title = RP_GROUPS[g][1], list = list, top = top, w = w }
		total = total + w
	end
	total = total + (#groups - 1) * RP_GROUP_GAP

	local rowLow = RP_BOTTOM
	local rowHigh = RP_BOTTOM + RP_ICON + RP_GAP
	local labelY = rowHigh + RP_ICON + 0.004
	local headY = labelY + RP_LABEL_H + 0.006
	rpTipTop = headY + RP_ICON + 0.012

	local id, x = 1000, 0.4 - total / 2
	for g = 1, #groups do
		local grp = groups[g]
		local label = BlzCreateFrame("HudText", rpRoot, 0, id)
		BlzFrameSetSize(label, grp.w, RP_LABEL_H)
		RpPlace(label, FRAMEPOINT_BOTTOMLEFT, x, labelY)
		BlzFrameSetTextAlignment(label, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_CENTER)
		BlzFrameSetText(label, "|cffb99d66" .. grp.title .. "|r")
		BlzFrameSetEnable(label, false)
		local shift = (#grp.list % 2 == 1) and (RP_ICON + RP_GAP) / 2 or 0
		for i = 1, #grp.list do
			local e = grp.list[i]
			local bx, by
			if i <= grp.top then
				bx, by = x + (i - 1) * (RP_ICON + RP_GAP), rowHigh
			else
				bx, by = x + shift + (i - grp.top - 1) * (RP_ICON + RP_GAP), rowLow
			end
			id = id + 1
			RpButton(BlzGetAbilityIcon(e.abil), RpRaceTip(e.abil), bx, by, id, RpPick(e))
		end
		x = x + grp.w + RP_GROUP_GAP
		id = id + 1
	end

	-- Над группами по центру: случайная раса и камера к кольцу.
	local rnd = RpEntry(RP_RANDOM)
	RpButton(BlzGetAbilityIcon(rnd.abil), RpRaceTip(rnd.abil), 0.4 - RP_ICON - RP_GAP / 2, headY, id + 1, RpPick(rnd))
	RpButton(RP_CAM_ICON,
		"|cffebc56cК месту высадки|r|n|cffced4daПереносит камеру к вашему кольцу выбора расы.|r",
		0.4 + RP_GAP / 2, headY, id + 2, RpCamera)

	rpHint = BlzCreateFrame("HudBody", rpRoot, 0, id + 3)
	BlzFrameSetSize(rpHint, 0.5, 0.016)
	RpPlace(rpHint, FRAMEPOINT_TOP, 0.4, 0.585)
	BlzFrameSetTextAlignment(rpHint, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_CENTER)
	BlzFrameSetText(rpHint, "|cffffffffПКМ|cffced4da по карте — место высадки, затем раса|r")
	BlzFrameSetEnable(rpHint, false)

	RpSetShown(false)
	rpReady = true
	-- Кольца, созданные до готовности панели, теряют старое меню только сейчас.
	for pi = 0, bj_MAX_PLAYER_SLOTS - 1 do
		if rpCircle[pi] ~= nil then RpStripOldMenu(rpCircle[pi]) end
	end
	TimerStart(CreateTimer(), 0.25, true, RpTick)
	RpApply()
end

-- Регистрирует кольцо выбора расы; вызывается сразу после каждого создания h0HJ.
-- Регион на всю карту с событием входа здесь не годится: он ломает пути юнитов
-- (тот же баг, что с Allmap = CreateRegion() в InitGlobals).
function RacePickerAdopt(u)
	if u == nil or GetUnitTypeId(u) ~= RP_CIRCLE then return end
	rpCircle[GetPlayerId(GetOwningPlayer(u))] = u
	if not rpReady then return end
	RpStripOldMenu(u)
	RpApply()
end

function RacePicker_Init()
	-- Фреймы — после проходов UISetup (0.1 и 1.0 с), одинаково у всех клиентов.
	local delay = CreateTimer()
	TimerStart(delay, 1.5, false, function()
		DestroyTimer(delay)
		ProbeStep("RacePicker_Create", RacePicker_Create)
	end)
end
