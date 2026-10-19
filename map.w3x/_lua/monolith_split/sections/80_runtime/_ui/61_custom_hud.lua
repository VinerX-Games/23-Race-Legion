-- ***************************************************************************
-- *  CustomHud
-- Own frames instead of the native multiboard and timer dialogs.
-- The hooks below only record what the game asks to show; the native
-- multiboard and timer dialogs stay hidden, and all existing code keeps
-- driving them unchanged. Pure presentation: never change game state here.
local HUD_COLS = 4
local HUD_MAX_ROWS = 25
local HUD_MAX_CHIPS = 4
local HUD_ROW_H = 0.013
local HUD_PAD = 0.0055
local HUD_BOARD_W = 0.245
local HUD_HEAD_H = 0.016
local HUD_SEP_GAP = 0.004
local HUD_ICON = 0.0135
local HUD_BTN = 0.0135
local HUD_CHIP_W = 0.125
local HUD_CHIP_H = 0.021
local HUD_TOP = 0.555
local HUD_LABEL = "|cffb99d66"
local HUD_VALUE = "|cffffffff"

local hudCell = {}       -- [row * HUD_COLS + col] = text of the main Multiboard
local hudItemCell = {}   -- multiboarditem -> row * HUD_COLS + col
local hudRows, hudCols = 0, 0
local hudBoardShown = false
local hudCollapsed = false
local hudDialogs = {}    -- array of { dialog, timer, title, shown }

local hudParent, hudBoard, hudToggle
local hudText = {}       -- [row * HUD_COLS + col] = text frame
local hudChip, hudChipText = {}, {}

local function HudPlain(s)
	return (string.gsub(string.gsub(s or "", "|[cC]%x%x%x%x%x%x%x%x", ""), "|[rR]", ""))
end

local function HudDialog(d)
	for i = 1, #hudDialogs do
		if hudDialogs[i].dialog == d then return hudDialogs[i], i end
	end
	return nil
end

-- Multiboard hooks: mirror the main board into hudCell, keep the native one hidden.
if MultiboardGetItem ~= nil then
	local nativeGetItem = MultiboardGetItem
	local nativeReleaseItem = MultiboardReleaseItem
	local nativeSetItemValue = MultiboardSetItemValue
	local nativeSetRowCount = MultiboardSetRowCount
	local nativeSetColumnCount = MultiboardSetColumnCount
	local nativeDisplay = MultiboardDisplay

	MultiboardGetItem = function(mb, row, col)
		local item = nativeGetItem(mb, row, col)
		if item ~= nil and mb ~= nil and mb == Multiboard and row < HUD_MAX_ROWS and col < HUD_COLS then
			hudItemCell[item] = row * HUD_COLS + col
		end
		return item
	end
	MultiboardReleaseItem = function(item)
		if item ~= nil then hudItemCell[item] = nil end
		nativeReleaseItem(item)
	end
	MultiboardSetItemValue = function(item, value)
		local cell = item ~= nil and hudItemCell[item]
		if cell then hudCell[cell] = value end
		nativeSetItemValue(item, value)
	end
	MultiboardSetRowCount = function(mb, count)
		if mb ~= nil and mb == Multiboard then hudRows = count end
		nativeSetRowCount(mb, count)
	end
	MultiboardSetColumnCount = function(mb, count)
		if mb ~= nil and mb == Multiboard then hudCols = count end
		nativeSetColumnCount(mb, count)
	end
	MultiboardDisplay = function(mb, show)
		if mb ~= nil and mb == Multiboard and hudBoard ~= nil then
			hudBoardShown = show
			nativeDisplay(mb, false)
			return
		end
		nativeDisplay(mb, show)
	end
end

-- Timer dialog hooks. TimerDialogDisplayForPlayerBJ calls TimerDialogDisplay inside
-- GetLocalPlayer(), so `shown` is per-client; it only feeds the local chips.
if CreateTimerDialog ~= nil then
	local nativeCreate = CreateTimerDialog
	local nativeDestroy = DestroyTimerDialog
	local nativeSetTitle = TimerDialogSetTitle
	local nativeDisplay = TimerDialogDisplay

	CreateTimerDialog = function(t)
		local d = nativeCreate(t)
		hudDialogs[#hudDialogs + 1] = { dialog = d, timer = t, title = "", shown = false }
		return d
	end
	DestroyTimerDialog = function(d)
		local _, i = HudDialog(d)
		if i then table.remove(hudDialogs, i) end
		nativeDestroy(d)
	end
	TimerDialogSetTitle = function(d, title)
		local rec = HudDialog(d)
		if rec then rec.title = HudPlain(title) end
		nativeSetTitle(d, title)
	end
	TimerDialogDisplay = function(d, show)
		local rec = HudDialog(d)
		if rec and hudBoard ~= nil then
			rec.shown = show
			nativeDisplay(d, false)
			return
		end
		nativeDisplay(d, show)
	end
end

local function HudTime(seconds)
	local s = math.ceil(seconds)
	if s < 0 then s = 0 end
	if s >= 3600 then
		return string.format("%d:%02d:%02d", s // 3600, (s % 3600) // 60, s % 60)
	end
	return string.format("%02d:%02d", s // 60, s % 60)
end

-- Right screen edge in the 0.8 x 0.6 frame space (widescreen extends past 0.8).
local function HudRightEdge()
	local w, h = BlzGetLocalClientWidth(), BlzGetLocalClientHeight()
	if w == nil or h == nil or w <= 0 or h <= 0 then return 0.8 end
	return 0.4 + 0.3 * w / h
end

local function HudNewText(parent, id, justify)
	local f = BlzCreateFrame("HudText", parent, 0, id)
	BlzFrameSetTextAlignment(f, TEXT_JUSTIFY_MIDDLE, justify)
	BlzFrameSetEnable(f, false)
	return f
end

local function HudNewStripe(parent, alpha)
	local f = BlzCreateFrameByType("BACKDROP", "HudStripe", parent, "", 0)
	BlzFrameSetTexture(f, "Textures\\white.blp", 0, true)
	BlzFrameSetAlpha(f, alpha)
	BlzFrameSetEnable(f, false)
	return f
end

-- Value columns: equal width, centred text, header icon with hover text.
local HUD_COL_W = 0.038
local function HudColX(col)
	return HUD_BOARD_W - 0.008 - HUD_COL_W * (HUD_COLS - col) + HUD_COL_W / 2
end
local HUD_COL_ICON = {
	[1] = "ReplaceableTextures\\CommandButtons\\BTNFootman.blp",
	[2] = "ReplaceableTextures\\CommandButtons\\BTNTownHall.blp",
	[3] = "ReplaceableTextures\\CommandButtons\\BTNMedalionOfCourage.blp",
}
local HUD_COL_TIP = {
	[1] = { "Юниты", "Число юнитов игрока." },
	[2] = { "Города", "Доля захваченных городов карты." },
	[3] = { "Опыт", "Опыт армии игрока." },
}
local hudIcon, hudStripe, hudSep = {}, {}, nil
local hudMeasure
local HUD_NAME_X = 0.024
local HUD_NAME_BASE_W = HUD_BOARD_W - HUD_COL_W * (HUD_COLS - 1) - 0.008 - HUD_NAME_X - 0.004

-- Width of a text in frame units: measured by an auto-sized hidden frame,
-- estimated from the character count if the engine reports nothing.
local function HudTextWidth(text)
	local w = 0
	if hudMeasure ~= nil then
		BlzFrameSetText(hudMeasure, text)
		w = BlzFrameGetWidth(hudMeasure)
	end
	if w == nil or w <= 0 then
		w = (utf8.len(HudPlain(text)) or string.len(text)) * 0.0056
	end
	return w
end

-- Race of a player: selection ability (icon and name for the row) and the marker
-- tech its pick researches. The marker also covers Random race and AI bots;
-- Dragon Union researches none and is caught only by the cast itself.
local HUD_RACES = {
	{ 'A0HW', 'R0F9' },
	{ 'A1EG', 'R0L1' },
	{ 'A0Y0', 'R0H3' },
	{ 'A0RQ', 'R0BY' },
	{ 'A1MZ', nil },
	{ 'A0QQ', 'R0BZ' },
	{ 'A0QN', 'R0A2' },
	{ 'A0AC', 'R07E' },
	{ 'A0MY', 'R0AO' },
	{ 'A0OK', 'R07H' },
	{ 'A0HR', 'R00G' },
	{ 'A0HM', 'R07B' },
	{ 'A0HV', 'R07I' },
	{ 'A0YV', 'R0DV' },
	{ 'A0HQ', 'R07C' },
	{ 'A0HN', 'R0BW' },
	{ 'A0HO', 'R07D' },
	{ 'A0HU', 'R07J' },
	{ 'A0HS', 'R07G' },
	{ 'A0HP', 'R07F' },
	{ 'A0HX', 'R07K' },
	{ 'A0HT', 'R07N' },
	{ 'A0J7', 'R0BV' },
	{ 'A0SD', 'R0BX' },
	{ 'A121', 'R0FX' },
	{ 'A14O', 'R0FS' },
	{ 'A0HL', 'R07L' },
	{ 'A155', 'R0G3' },
	{ 'A17N', 'R0HT' },
	{ 'A02A', 'R0GZ' },
	{ 'A1DZ', 'R0IH' },
	{ 'A1JL', 'R0KA' },
	{ 'A1FN', 'R0J1' },
	{ 'A1HA', 'R0J4' },
	{ 'A1I6', 'R0L3' },
	{ 'A1JN', 'R0KB' },
}
local hudRaceByAbil = {}
local hudRaceAbil = {}   -- [pi] = selection ability id
local hudRaceIcon, hudRaceHover, hudRaceTipText = {}, {}, {}

local function HudRaceOf(pi)
	local id = hudRaceAbil[pi]
	if id ~= nil then return id end
	local p = Player(pi)
	for i = 1, #HUD_RACES do
		local r = HUD_RACES[i]
		if r.tech ~= nil and GetPlayerTechCount(p, r.tech, true) > 0 then
			hudRaceAbil[pi] = r.abil
			return r.abil
		end
	end
	return nil
end

-- Race picked from the RacePicker panel: there is no spell event to catch.
function CustomHudNoteRace(pi, abil)
	if hudRaceByAbil[abil] then hudRaceAbil[pi] = abil end
end
local hudToggleText

local function HudValue(col, raw)
	local v = HudPlain(raw)
	if col == 2 then
		local n = tonumber(string.match(v, "[%d%.]+"))
		if n then v = string.format("%d%%", math.floor(n + 0.5)) end
	end
	return HUD_VALUE .. v .. "|r"
end

-- Пока стандартный интерфейс скрыт (панели выбора расы и хоста), HUD уведён за экран.
-- Глобал, а не local: главный чанк war3map.lua упирается в лимит регистров Lua.
CustomHudHidden = false

function CustomHudRender()
	if hudBoard == nil then return end
	if CustomHudHidden then
		for i = 1, HUD_MAX_CHIPS do FrameSetShown(hudChip[i], false) end
		FrameSetShown(hudBoard, false)
		return
	end
	local right = HudRightEdge() - 0.006
	local top = HUD_TOP

	-- The name column grows to the longest visible name; the board widens leftwards.
	local nameW = HUD_NAME_BASE_W
	if hudBoardShown and not hudCollapsed then
		for row = 1, math.min(hudRows - 1, HUD_MAX_ROWS - 1) do
			local need = HudTextWidth(hudCell[row * HUD_COLS] or "") + 0.002
			if need > nameW then nameW = need end
		end
	end
	local boardW = HUD_BOARD_W + (nameW - HUD_NAME_BASE_W)

	-- Timer chips, right to left in creation order.
	local total = 0
	for i = 1, #hudDialogs do
		if hudDialogs[i].shown then total = total + 1 end
	end
	total = math.min(total, HUD_MAX_CHIPS)
	local chipW = total > 0 and (boardW - 0.004 * (total - 1)) / total or boardW
	local x, n = right, 0
	for i = 1, #hudDialogs do
		local rec = hudDialogs[i]
		if rec.shown and n < HUD_MAX_CHIPS then
			n = n + 1
			BlzFrameSetSize(hudChip[n], chipW, HUD_CHIP_H)
			FrameClearAllPoints(hudChip[n])
			FrameSetAbsPoint(hudChip[n], FRAMEPOINT_TOPRIGHT, x, top)
			BlzFrameSetText(hudChipText[n], HUD_LABEL .. rec.title .. "  " .. HUD_VALUE
				.. HudTime(TimerGetRemaining(rec.timer)) .. "|r")
			FrameSetShown(hudChip[n], true)
			x = x - chipW - 0.004
		end
	end
	for i = n + 1, HUD_MAX_CHIPS do FrameSetShown(hudChip[i], false) end
	if n > 0 then top = top - HUD_CHIP_H - 0.004 end

	-- Board.
	if not hudBoardShown or Multiboard == nil or hudRows < 1 then
		FrameSetShown(hudBoard, false)
		return
	end
	local cols = math.min(hudCols, HUD_COLS)
	local players = math.min(hudRows - 1, HUD_MAX_ROWS - 1)
	local shownPlayers = hudCollapsed and 0 or players
	FrameClearAllPoints(hudBoard)
	FrameSetAbsPoint(hudBoard, FRAMEPOINT_TOPRIGHT, right, top)
	BlzFrameSetSize(hudBoard, boardW, HUD_PAD * 2 + HUD_HEAD_H
		+ (shownPlayers > 0 and (HUD_SEP_GAP + HUD_ROW_H * shownPlayers) or 0))
	FrameSetShown(hudBoard, true)

	BlzFrameSetText(hudToggleText, HUD_VALUE .. (hudCollapsed and "+" or "-") .. "|r")
	BlzFrameSetText(hudText[0], HUD_LABEL .. "Игроки " .. HUD_VALUE .. players .. "|r")
	FrameSetShown(hudText[0], true)
	for col = 1, HUD_COLS - 1 do
		FrameSetShown(hudIcon[col], col < cols)
	end
	FrameSetShown(hudSep, shownPlayers > 0)
	BlzFrameSetSize(hudSep, boardW - 0.012, 0.0008)
	local rowPi = {}
	for pi = 0, 23 do
		local r = MultiboardItemOwnerIndex[pi]
		if r ~= nil then rowPi[r] = pi end
	end
	for row = 1, HUD_MAX_ROWS - 1 do
		local visibleRow = row <= shownPlayers
		local abil = visibleRow and rowPi[row] ~= nil and HudRaceOf(rowPi[row]) or nil
		if abil ~= nil then
			BlzFrameSetTexture(hudRaceIcon[row], BlzGetAbilityIcon(abil), 0, true)
			BlzFrameSetText(hudRaceTipText[row], "|cffebc56c" .. HudPlain(GetAbilityName(abil)) .. "|r")
		end
		FrameSetShown(hudRaceIcon[row], abil ~= nil)
		FrameSetShown(hudStripe[row], visibleRow and row % 2 == 0)
		BlzFrameSetSize(hudStripe[row], boardW - 0.008, HUD_ROW_H)
		BlzFrameSetSize(hudText[row * HUD_COLS], nameW, HUD_ROW_H)
		for col = 0, HUD_COLS - 1 do
			local f = hudText[row * HUD_COLS + col]
			local visible = visibleRow and col < cols
			if visible then
				local raw = hudCell[row * HUD_COLS + col] or ""
				BlzFrameSetText(f, col == 0 and raw or HudValue(col, raw))
			end
			FrameSetShown(f, visible)
		end
	end
end

-- Только локально: вызывается из StandardUISetVisible.
function CustomHudSetVisible(show)
	CustomHudHidden = not show
	CustomHudRender()
end

local function HudToggleClick()
	if GetTriggerPlayer() == GetLocalPlayer() then
		hudCollapsed = not hudCollapsed
		BlzFrameSetEnable(hudToggle, false)
		BlzFrameSetEnable(hudToggle, true)
		CustomHudRender()
	end
end

local function HudRowY(row)
	return -HUD_PAD - HUD_HEAD_H - HUD_SEP_GAP - (row - 1) * HUD_ROW_H
end

function CustomHud_Create()
	if hudBoard ~= nil then return end
	if not BlzLoadTOCFile("war3mapimported\\HudText.toc") then
		ProbeLogWrite("[HUD] HudText.toc not loaded, keeping native multiboard")
		return
	end
	BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
	hudParent = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	if hudParent == nil then hudParent = BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0) end

	for i = 1, HUD_MAX_CHIPS do
		hudChip[i] = BlzCreateFrame("BoxedTextBackgroundTemplate", hudParent, 0, 100 + i)
		BlzFrameSetSize(hudChip[i], HUD_CHIP_W, HUD_CHIP_H)
		hudChipText[i] = HudNewText(hudChip[i], 100 + i, TEXT_JUSTIFY_CENTER)
		BlzFrameSetAllPoints(hudChipText[i], hudChip[i])
		FrameSetShown(hudChip[i], false)
	end

	hudBoard = BlzCreateFrame("BoxedTextBackgroundTemplate", hudParent, 0, 200)
	hudMeasure = BlzCreateFrame("HudText", hudParent, 0, 900)
	BlzFrameSetAbsPoint(hudMeasure, FRAMEPOINT_TOPLEFT, 0.0, FRAME_PARK_Y)
	BlzFrameSetAlpha(hudMeasure, 0)
	BlzFrameSetEnable(hudMeasure, false)

	-- Header: collapse button, player count, column icons with hover text.
	local headMid = -HUD_PAD - HUD_HEAD_H / 2
	local btn = BlzCreateFrameByType("BACKDROP", "HudToggleFace", hudBoard, "", 0)
	BlzFrameSetTexture(btn, "UI\\ButtonBorder.dds", 0, true)
	BlzFrameSetSize(btn, HUD_BTN, HUD_BTN)
	BlzFrameSetPoint(btn, FRAMEPOINT_LEFT, hudBoard, FRAMEPOINT_TOPLEFT, 0.007, headMid)
	hudToggleText = HudNewText(btn, 201, TEXT_JUSTIFY_CENTER)
	BlzFrameSetAllPoints(hudToggleText, btn)
	hudToggle = BlzCreateFrameByType("BUTTON", "HudBoardToggle", btn, "", 0)
	BlzFrameSetAllPoints(hudToggle, btn)
	local trig = CreateTrigger()
	BlzTriggerRegisterFrameEvent(trig, hudToggle, FRAMEEVENT_CONTROL_CLICK)
	TriggerAddAction(trig, HudToggleClick)

	hudText[0] = HudNewText(hudBoard, 300, TEXT_JUSTIFY_LEFT)
	BlzFrameSetSize(hudText[0], 0.08, HUD_HEAD_H)
	FrameSetPoint(hudText[0], FRAMEPOINT_LEFT, btn, FRAMEPOINT_RIGHT, 0.004, 0)

	for col = 1, HUD_COLS - 1 do
		local icon = BlzCreateFrameByType("BACKDROP", "HudColIcon", hudBoard, "", col)
		BlzFrameSetTexture(icon, HUD_COL_ICON[col], 0, true)
		BlzFrameSetSize(icon, HUD_ICON, HUD_ICON)
		FrameSetPoint(icon, FRAMEPOINT_CENTER, hudBoard, FRAMEPOINT_TOPRIGHT, HudColX(col) - HUD_BOARD_W, headMid)
		local hover = BlzCreateFrameByType("FRAME", "HudColHover", icon, "", col)
		BlzFrameSetAllPoints(hover, icon)
		local tip = BlzCreateFrame("BoxedText", hover, 0, 400 + col)
		BlzFrameSetText(BlzGetFrameByName("BoxedTextTitle", 400 + col), "|cffebc56c" .. HUD_COL_TIP[col][1] .. "|r")
		BlzFrameSetText(BlzGetFrameByName("BoxedTextValue", 400 + col), "|cffced4da" .. HUD_COL_TIP[col][2] .. "|r")
		BlzFrameSetSize(tip, 0.13, 0.04)
		BlzFrameClearAllPoints(tip)
		BlzFrameSetPoint(tip, FRAMEPOINT_TOPRIGHT, icon, FRAMEPOINT_BOTTOMRIGHT, 0, -0.004)
		BlzFrameSetTooltip(hover, tip)
		BlzFrameSetVisible(tip, false)
		hudIcon[col] = icon
	end

	hudSep = HudNewStripe(hudBoard, 70)
	BlzFrameSetSize(hudSep, HUD_BOARD_W - 0.012, 0.0008)
	FrameSetPoint(hudSep, FRAMEPOINT_TOPLEFT, hudBoard, FRAMEPOINT_TOPLEFT, 0.006,
		-HUD_PAD - HUD_HEAD_H - HUD_SEP_GAP / 2)

	for row = 1, HUD_MAX_ROWS - 1 do
		local y = HudRowY(row)
		hudStripe[row] = HudNewStripe(hudBoard, 14)
		BlzFrameSetSize(hudStripe[row], HUD_BOARD_W - 0.008, HUD_ROW_H)
		FrameSetPoint(hudStripe[row], FRAMEPOINT_TOPLEFT, hudBoard, FRAMEPOINT_TOPLEFT, 0.004, y)
		FrameSetShown(hudStripe[row], false)
		local icon = BlzCreateFrameByType("BACKDROP", "HudRaceIcon", hudBoard, "", row)
		BlzFrameSetSize(icon, HUD_ROW_H - 0.001, HUD_ROW_H - 0.001)
		FrameSetPoint(icon, FRAMEPOINT_TOPLEFT, hudBoard, FRAMEPOINT_TOPLEFT, 0.008, y - 0.0005)
		local hover = BlzCreateFrameByType("FRAME", "HudRaceHover", icon, "", row)
		BlzFrameSetAllPoints(hover, icon)
		local tip = BlzCreateFrame("BoxedText", hover, 0, 500 + row)
		hudRaceTipText[row] = BlzGetFrameByName("BoxedTextTitle", 500 + row)
		BlzFrameSetText(BlzGetFrameByName("BoxedTextValue", 500 + row), "")
		BlzFrameSetSize(tip, 0.13, 0.021)
		BlzFrameClearAllPoints(tip)
		BlzFrameSetPoint(tip, FRAMEPOINT_TOPRIGHT, icon, FRAMEPOINT_TOPLEFT, -0.004, 0.004)
		BlzFrameSetTooltip(hover, tip)
		BlzFrameSetVisible(tip, false)
		FrameSetShown(icon, false)
		hudRaceIcon[row] = icon
		for col = 0, HUD_COLS - 1 do
			local f = HudNewText(hudBoard, 300 + row * HUD_COLS + col,
				col == 0 and TEXT_JUSTIFY_LEFT or TEXT_JUSTIFY_CENTER)
			if col == 0 then
				BlzFrameSetSize(f, HUD_NAME_BASE_W, HUD_ROW_H)
				FrameSetPoint(f, FRAMEPOINT_TOPLEFT, hudBoard, FRAMEPOINT_TOPLEFT, HUD_NAME_X, y)
			else
				BlzFrameSetSize(f, HUD_COL_W, HUD_ROW_H)
				FrameSetPoint(f, FRAMEPOINT_TOP, hudBoard, FRAMEPOINT_TOPRIGHT, HudColX(col) - HUD_BOARD_W, y)
			end
			FrameSetShown(f, false)
			hudText[row * HUD_COLS + col] = f
		end
	end
	FrameSetShown(hudBoard, false)

	for i = 1, #HUD_RACES do
		local r = HUD_RACES[i]
		r.abil = FourCC(r[1])
		r.tech = r[2] and FourCC(r[2]) or nil
		hudRaceByAbil[r.abil] = true
	end
	local pick = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(pick, EVENT_PLAYER_UNIT_SPELL_FINISH)
	TriggerAddAction(pick, function()
		local id = GetSpellAbilityId()
		if hudRaceByAbil[id] then hudRaceAbil[GetPlayerId(GetTriggerPlayer())] = id end
	end)

	TimerStart(CreateTimer(), 0.25, true, CustomHudRender)
	CustomHudRender()
end
