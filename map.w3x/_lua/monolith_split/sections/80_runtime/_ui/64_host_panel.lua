-- ***************************************************************************
-- *  HostPanel
-- Панель настроек лобби для хоста (Player(0)) вместо листаемого здания-меню
-- (n04G → n04D → … → n074). Все настройки на одном экране; пока лобби идёт,
-- у хоста локально скрыт стандартный интерфейс (кроме «Меню» и «Чата»).
-- Клик — синхронное событие фрейма; обработчик меняет те же глобалы, что и
-- способности старого меню. Если панель не создалась, StartLobby создаёт
-- здание-меню как раньше.
-- Раскладка подстраивается под тексты: ширина колонки — по самой длинной
-- кнопке в ней, ширина подписей — по самой длинной подписи, фон — по сетке.
-- Позиции фреймов — только внешний вид, на синхронную логику не влияют.
local HP_HOST = 0
local HP_COLS = 4
local HP_PAD = 0.015
local HP_BTN_H = 0.026
local HP_BTN_MIN = 0.07
local HP_ICON = 0.018
local HP_INSET = 0.004      -- отступ иконки от края кнопки
local HP_TEXT_PAD = 0.006   -- зазор между иконкой и текстом и после текста
local HP_GAP = 0.004
local HP_ROW_GAP = 0.01
local HP_LABEL_GAP = 0.012
local HP_TIP_W = 0.26
local HP_CHAR_W = 0.0072    -- оценка ширины символа HudBody, если движок не измерил
local HP_SELECTED = "ui\\widgets\\escmenu\\human\\quest-button-highlight"
local HP_BTN = "ReplaceableTextures\\CommandButtons\\"

-- Строки настроек. Радио-строка: get() возвращает текущее значение, set(v) его
-- задаёт; у опции { значение, название, описание, иконка }.
local HP_ROWS = {
	{ "lua.auto_3f53fb873461737d",
		get = function() return udg_GameMode end,
		set = function(v) udg_GameMode = v end,
		{ 0, "lua.auto_a39ad47c922226a5", "lua.auto_ac4d96817fdf1af9", HP_BTN .. "BTNSorceressAdept.blp" },
		{ 1, "lua.auto_7552614d66b8a7a1", "lua.auto_61a0bbfb1890c9be", HP_BTN .. "BTNCastle.blp" },
		{ 2, "lua.auto_61379f15167d5f16", "lua.auto_ec0079fe99f86065", HP_BTN .. "BTNHelmutPurple.blp" },
		{ 5, "lua.auto_26dd9e3aae5c8d4c", "lua.auto_50f00368e762f6ed", HP_BTN .. "BTNAltarOfKings.blp" },
		{ 3, "lua.auto_1287b176ee3a0776", "lua.auto_012084117924e404", HP_BTN .. "BTNHumanBarracks.blp" },
		{ 4, "lua.auto_55cbf0812cc59fa5", "lua.auto_7ceabbc5fbaf6343", HP_BTN .. "BTNScrollOfHaste.blp" },
	},
	{ "lua.auto_fac7927ccc7ca958",
		get = function() return udg_SET_VISIBLE_MODE end,
		set = function(v) udg_SET_VISIBLE_MODE = v end,
		{ 0, "lua.auto_509c0a93349416ca", "lua.auto_3e90a8f5c00c5ff7", HP_BTN .. "BTNUndeadShrine.blp" },
		{ 1, "lua.auto_4a978bae23429c8f", "lua.auto_d4c33d954fc31e3b", HP_BTN .. "BTNSentinel.blp" },
		{ 2, "lua.auto_1df09de4504fc344", "lua.auto_ddfc93285a52d9d9", HP_BTN .. "BTNFarSight.blp" },
	},
	{ "lua.auto_78d132d664cd635b",
		get = function() return DipMode end,
		set = function(v) DipMode = v end,
		{ 0, "lua.auto_65b08c1f055c0a1a", "lua.auto_78185876b7938ca9", HP_BTN .. "BTNHumanCaptureFlag.blp" },
		{ 1, "lua.auto_722b5b8c030fcea9", "lua.auto_c7a2d35d77aa2938", HP_BTN .. "BTNAttack.blp" },
		{ 2, "lua.auto_ac8a4d534efd4fc8", "lua.auto_d1cca99d19051b82", HP_BTN .. "BTNOrcCaptureFlag.blp" },
		{ 3, "lua.auto_9693fa514a0642f5", "lua.auto_d8d87791362fbe1a", HP_BTN .. "BTNNightElfCaptureFlag.blp" },
	},
	{ "lua.auto_384d916bbcef012f",
		get = function() return IncomeMod end,
		set = function(v) IncomeMod = v end,
		{ 0.75, "×0.75", "lua.auto_39613b8bfff3e719", HP_BTN .. "BTNPillage.blp" },
		{ 1, "×1.00", "lua.auto_10f79199643a1472", HP_BTN .. "BTNChestOfGold.blp" },
	},
	{ "lua.auto_bb45d8092581d222",
		get = function() return TotalProduction end,
		set = function(v)
			if v then
				Trig_StartTotalProductionCommon_Actions()
			else
				TotalProduction = false
				for i = 0, 22 do SetPlayerAbilityAvailable(Player(i), FourCC('A1KH'), false) end
			end
		end,
		{ false, "lua.auto_5a577d90566052be", "lua.auto_db448c0d871437a0", HP_BTN .. "BTNCancel.blp" },
		{ true, "lua.auto_0b8162990567631a", "lua.auto_c48a1b9379356fa5", HP_BTN .. "BTNRallyPoint.blp" },
	},
}

-- Континенты: индекс в udg_Continents, название, полное название, иконка.
-- udg_Continents[0] = 0 — вся карта.
local HP_CONTINENTS = {
	{ 1, "lua.auto_88897d593739ee25", "lua.auto_88897d593739ee25", "CommonIcons\\PASBTN_CONT_EK.blp" },
	{ 2, "lua.auto_f98207a144b1480b", "lua.auto_f98207a144b1480b", "CommonIcons\\PASBTN_CONT_Kalim.blp" },
	{ 3, "lua.auto_ad45a7d12d975f7d", "lua.auto_ad45a7d12d975f7d", "CommonIcons\\PASBTN_CONT_Outland.blp" },
	{ 4, "lua.auto_1d9ba41af9bd8982", "lua.auto_1d9ba41af9bd8982", "CommonIcons\\PASBTN_CONT_Nord.blp" },
	{ 5, "lua.auto_91cf723beb3c0f96", "lua.auto_91cf723beb3c0f96", "CommonIcons\\PASBTN_CONT_Pandaria.blp" },
	{ 7, "lua.auto_83104b113adcbc77", "lua.auto_a7e7c6599d14a0cb", "CommonIcons\\PASBTN_CONT_Okeania.blp" },
	{ 6, "lua.auto_9a0f6ad9710e2500", "lua.auto_9a0f6ad9710e2500", "CommonIcons\\PASBTN_CONT_Argus.blp" },
}
local HP_ALL_MAP_ICON = HP_BTN .. "BTN_CONT_All.blp"

local hpRoot, hpTime, hpMinute, hpTick, hpMeasure
local hpButtons = {}   -- { text, mark, name, selected = function() }
local hpPlaced = {}    -- фреймы с абсолютной позицией: при скрытии уводятся за экран
local hpShown = false

local function HpIsHost(p)
	return GetPlayerId(p) == HP_HOST
end

local function HpAnnounce(what, value)
	DisplayTimedTextToForce(GetPlayersAll(), 6, Loc("lua.auto_108968b5be7d38b0") .. what
		.. " — |cffebc56c" .. value .. "|r")
end

-- Ширина текста шрифтом HudBody: автоподгоняемый скрытый фрейм, а если движок
-- ещё ничего не посчитал — оценка по числу символов (берётся большее).
local function HpTextWidth(text)
	local w = 0
	if hpMeasure ~= nil then
		BlzFrameSetText(hpMeasure, text)
		w = BlzFrameGetWidth(hpMeasure) or 0
	end
	return math.max(w, (utf8.len(text) or string.len(text)) * HP_CHAR_W)
end

local function HpButtonWidth(name)
	return math.max(HP_BTN_MIN, HP_INSET + HP_ICON + HP_TEXT_PAD + HpTextWidth(name) + HP_TEXT_PAD)
end

-- Перекрасить кнопки по текущим значениям. Только внешний вид фреймов.
local function HpRefresh()
	for i = 1, #hpButtons do
		local b = hpButtons[i]
		local on = b.selected()
		FrameSetShown(b.mark, on)
		BlzFrameSetText(b.text, (on and "|cffebc56c" or "|cffced4da") .. b.name .. "|r")
	end
end

-- Абсолютная позиция с учётом для HpSetShown.
local function HpPlace(f, point, x, y)
	FrameSetAbsPoint(f, point, x, y)
	hpPlaced[#hpPlaced + 1] = f
end

-- Скрытый фрейм может продолжать ловить мышь: при скрытии вся панель уводится
-- вниз за экран, при показе возвращается. Только локально.
local function HpSetShown(show)
	FrameSetShown(hpRoot, show)
	for i = 1, #hpPlaced do FramePark(hpPlaced[i], not show) end
	-- «+1 минута» уже использована: кнопка остаётся скрытой.
	if not IsTriggerEnabled(gg_trg_AddMinute) then FrameSetShown(hpMinute, false) end
end

-- Снять фокус с кнопки, иначе пробел/Enter продолжают нажимать её.
local function HpRelease(f, p)
	if GetLocalPlayer() == p then
		BlzFrameSetEnable(f, false)
		BlzFrameSetEnable(f, true)
	end
end

local function HpTip(parent, x, y, w, id, tip)
	local box = BlzCreateFrame("BoxedTextBackgroundTemplate", parent, 0, id)
	local text = BlzCreateFrame("HudBody", box, 0, id)
	BlzFrameSetTextAlignment(text, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
	BlzFrameSetSize(text, HP_TIP_W, 0)
	local tx = math.max(0.005, math.min(x + w / 2 - HP_TIP_W / 2, 0.795 - HP_TIP_W))
	-- Подсказку показывает и прячет движок: её не уводим, она стоит на месте.
	BlzFrameSetAbsPoint(text, FRAMEPOINT_BOTTOMLEFT, tx, y + HP_BTN_H + 0.012)
	BlzFrameSetText(text, tip)
	BlzFrameSetPoint(box, FRAMEPOINT_TOPLEFT, text, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
	BlzFrameSetPoint(box, FRAMEPOINT_BOTTOMRIGHT, text, FRAMEPOINT_BOTTOMRIGHT, 0.007, -0.007)
	BlzFrameSetTooltip(parent, box)
	BlzFrameSetVisible(box, false)
end

-- Кнопка: иконка слева, текст по центру оставшейся части.
-- opt = { name, icon, tip, selected = function | nil, click = function }.
local function HpButton(x, y, w, id, opt)
	local b = BlzCreateFrame("TasButtonTemplate", hpRoot, 0, id)
	BlzFrameSetSize(b, w, HP_BTN_H)
	HpPlace(b, FRAMEPOINT_BOTTOMLEFT, x, y)
	local mark = BlzCreateFrameByType("BACKDROP", "HostPanelMark", b, "", id)
	FrameSetPoint(mark, FRAMEPOINT_TOPLEFT, b, FRAMEPOINT_TOPLEFT, 0, 0)
	FrameSetPoint(mark, FRAMEPOINT_BOTTOMRIGHT, b, FRAMEPOINT_BOTTOMRIGHT, 0, 0)
	BlzFrameSetTexture(mark, HP_SELECTED, 0, true)
	BlzFrameSetEnable(mark, false)
	FrameSetShown(mark, false)
	local icon = BlzCreateFrameByType("BACKDROP", "HostPanelIcon", b, "", id)
	BlzFrameSetSize(icon, HP_ICON, HP_ICON)
	BlzFrameSetPoint(icon, FRAMEPOINT_LEFT, b, FRAMEPOINT_LEFT, HP_INSET, 0)
	BlzFrameSetTexture(icon, opt.icon, 0, true)
	BlzFrameSetEnable(icon, false)
	local text = BlzCreateFrame("HudBody", b, 0, id)
	BlzFrameSetPoint(text, FRAMEPOINT_TOPLEFT, icon, FRAMEPOINT_TOPRIGHT, HP_TEXT_PAD, 0.004)
	BlzFrameSetPoint(text, FRAMEPOINT_BOTTOMRIGHT, b, FRAMEPOINT_BOTTOMRIGHT, -HP_TEXT_PAD, 0.0)
	BlzFrameSetTextAlignment(text, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_CENTER)
	BlzFrameSetText(text, "|cffced4da" .. opt.name .. "|r")
	BlzFrameSetEnable(text, false)
	HpTip(b, x, y, w, id, "|cffebc56c" .. (opt.title or opt.name) .. "|r|n|cffced4da" .. opt.tip .. "|r")

	local t = CreateTrigger()
	BlzTriggerRegisterFrameEvent(t, b, FRAMEEVENT_CONTROL_CLICK)
	TriggerAddAction(t, function()
		local p = GetTriggerPlayer()
		HpRelease(BlzGetTriggerFrame(), p)
		if not HpIsHost(p) or hpRoot == nil then return end
		opt.click()
		HpRefresh()
	end)
	if opt.selected ~= nil then
		hpButtons[#hpButtons + 1] = { text = text, mark = mark, name = opt.name, selected = opt.selected }
	end
	return b
end

local function HpLabel(x, y, w, id, title)
	local label = BlzCreateFrame("HudBody", hpRoot, 0, id)
	BlzFrameSetSize(label, w, HP_BTN_H)
	HpPlace(label, FRAMEPOINT_BOTTOMLEFT, x, y)
	BlzFrameSetTextAlignment(label, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_LEFT)
	BlzFrameSetText(label, "|cffb99d66" .. title .. "|r")
	BlzFrameSetEnable(label, false)
end

local function HpContinentsAny()
	for i = 1, #HP_CONTINENTS do
		if udg_Continents[HP_CONTINENTS[i][1]] == 1 then return true end
	end
	return false
end

local function HpContinentsAll()
	udg_Continents[0] = 0
	for i = 1, 15 do udg_Continents[i] = 0 end
	HpAnnounce(Loc("lua.auto_4befbe5b117f5dc0"), Loc("lua.auto_b9cc9f71c3cb1e73"))
end

local function HpContinentToggle(c)
	local on = udg_Continents[c[1]] ~= 1
	udg_Continents[c[1]] = on and 1 or 0
	udg_Continents[0] = HpContinentsAny() and 1 or 0
	HpAnnounce(Loc(c[3]), on and Loc("lua.auto_a5de79ca324d2f35") or Loc("lua.auto_6f4f17fc7201101f"))
end

-- Все строки панели в порядке показа: { title, options = { opt, ... } }.
local function HpLayoutRows()
	local rows = {}
	for r = 1, #HP_ROWS do
		local row = HP_ROWS[r]
		local opts = {}
		for i = 2, #row do
			local o = row[i]
				opts[#opts + 1] = { name = Loc(o[2]), tip = Loc(o[3]), icon = o[4],
				selected = function() return row.get() == o[1] end,
				click = function()
					if row.get() == o[1] then return end
					row.set(o[1])
					HpAnnounce(Loc(row[1]), Loc(o[2]))
				end }
		end
		rows[#rows + 1] = { title = Loc(row[1]), options = opts }
		-- Континенты — сразу после режима.
		if r == 1 then
			local cont = { { name = Loc("lua.auto_245f55d3c204ee69"), icon = HP_ALL_MAP_ICON,
				tip = Loc("lua.auto_b6ddb9708bc19b8b"),
				selected = function() return udg_Continents[0] ~= 1 end,
				click = function() if udg_Continents[0] == 1 then HpContinentsAll() end end } }
			for i = 1, #HP_CONTINENTS do
				local c = HP_CONTINENTS[i]
				cont[#cont + 1] = { name = Loc(c[2]), title = Loc(c[3]), icon = c[4],
					tip = Loc("lua.auto_ee27e733524ef7b2")
						.. Loc("lua.auto_bf312df3ad8c8ee7"),
					selected = function() return udg_Continents[0] == 1 and udg_Continents[c[1]] == 1 end,
					click = function() HpContinentToggle(c) end }
			end
			rows[#rows + 1] = { title = Loc("lua.auto_4befbe5b117f5dc0"), options = cont }
		end
	end
	return rows
end

local function HpLobbyButtons()
	return {
		{ name = Loc("lua.auto_28f26716a4cca51d"), icon = "CommonIcons\\BTNTimeStop.blp",
			tip = Loc("lua.auto_5c617b8361f535c3"),
			click = function()
				if TimerGetRemaining(udg_LobbyTime) > 5.0 then
					TimerStart(udg_LobbyTime, 5.00, false, nil)
					DisplayTimedTextToForce(GetPlayersAll(), 6, Loc("lua.auto_49f42b76e1fe7b33"))
				end
			end },
		{ name = Loc("lua.auto_9df8266469c2c1aa"), icon = "CommonIcons\\BTNTimeSpell.blp",
			tip = Loc("lua.auto_9f56ccd4169ff595"),
			click = function()
				if not IsTriggerEnabled(gg_trg_AddMinute) then return end
				TimerStart(udg_LobbyTime, TimerGetRemaining(udg_LobbyTime) + 60.00, false, nil)
				DisableTrigger(gg_trg_AddMinute)
				FrameSetShown(hpMinute, false)
				DisplayTimedTextToForce(GetPlayersAll(), 6, Loc("lua.auto_514bbe15504ed8e0"))
			end },
	}
end

local function HpTimeText()
	local s = R2I(TimerGetRemaining(udg_LobbyTime) + 0.99)
	return Loc("lua.auto_7192876cf690ad66") .. (s // 60) .. ":" .. string.format("%02d", s % 60) .. "|r"
end

local function HpTickFn()
	if hpTime ~= nil then BlzFrameSetText(hpTime, HpTimeText()) end
end

-- Показать или спрятать панель хосту. Остальным игрокам она не видна никогда.
local function HpShow(show)
	if hpRoot == nil or hpShown == show then return end
	hpShown = show
	if GetLocalPlayer() == Player(HP_HOST) then
		HpSetShown(show)
		if StandardUISetVisible ~= nil then StandardUISetVisible(not show) end
		if not show and UISetup ~= nil then UISetup() end
	end
end

-- Создаёт панель (у всех клиентов одинаково) и показывает её хосту.
-- Возвращает false, если шаблоны не загрузились: тогда нужно старое меню.
function HostPanel_Open()
	if hpRoot ~= nil then return true end
	if StandardUIAcquireCommandButtons ~= nil then StandardUIAcquireCommandButtons() end
	if not BlzLoadTOCFile("war3mapimported\\HudText.toc") or not BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
		or not BlzLoadTOCFile("war3mapimported\\TasItemShop.toc") then
		ProbeLogWrite("[HOSTPANEL] templates not loaded, keeping mode building")
		return false
	end
	local parent = BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0)
	hpRoot = BlzCreateFrame("BoxedTextBackgroundTemplate", parent, 0, 2000)
	BlzFrameSetLevel(hpRoot, 5)
	hpMeasure = BlzCreateFrame("HudBody", hpRoot, 0, 2001)
	BlzFrameSetAbsPoint(hpMeasure, FRAMEPOINT_TOPLEFT, 0.0, FRAME_PARK_Y)
	BlzFrameSetAlpha(hpMeasure, 0)
	BlzFrameSetEnable(hpMeasure, false)

	-- Размеры: подписи, колонки сетки, кнопки лобби, заголовок.
	local rows = HpLayoutRows()
	local lobby = HpLobbyButtons()
	local labelW, colW = 0, {}
	for c = 1, HP_COLS do colW[c] = HP_BTN_MIN end
	for r = 1, #rows do
		labelW = math.max(labelW, HpTextWidth(rows[r].title))
		for i = 1, #rows[r].options do
			local c = (i - 1) % HP_COLS + 1
			colW[c] = math.max(colW[c], HpButtonWidth(rows[r].options[i].name))
		end
	end
	labelW = labelW + HP_LABEL_GAP
	local gridW = (HP_COLS - 1) * HP_GAP
	for c = 1, HP_COLS do gridW = gridW + colW[c] end
	local lobbyW = 0
	for i = 1, #lobby do lobbyW = math.max(lobbyW, HpButtonWidth(lobby[i].name)) end
	lobbyW = lobbyW + 0.03
	local headW = HpTextWidth(Loc("lua.auto_14bcc1b1cb897657")) * 1.4 + HpTextWidth(Loc("lua.auto_7a0bc2f02438e548")) + 0.03
	local innerW = math.max(labelW + gridW, lobbyW * 2 + HP_GAP, headW)
	local width = innerW + HP_PAD * 2
	local left = 0.4 - width / 2
	local bx0 = left + HP_PAD + (innerW - gridW)
	local colX = {}
	local cx = bx0
	for c = 1, HP_COLS do
		colX[c] = cx
		cx = cx + colW[c] + HP_GAP
	end

	local top = 0.56
	local y = top - HP_PAD
	local id = 2002

	local title = BlzCreateFrame("HudTitle", hpRoot, 0, id)
	BlzFrameSetSize(title, innerW / 2, 0.02)
	HpPlace(title, FRAMEPOINT_TOPLEFT, left + HP_PAD, y)
	BlzFrameSetText(title, Loc("lua.auto_b4dea7c8121d6c2d"))
	BlzFrameSetEnable(title, false)
	hpTime = BlzCreateFrame("HudBody", hpRoot, 0, id)
	BlzFrameSetSize(hpTime, innerW / 2, 0.02)
	HpPlace(hpTime, FRAMEPOINT_TOPRIGHT, left + width - HP_PAD, y)
	BlzFrameSetTextAlignment(hpTime, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_RIGHT)
	BlzFrameSetEnable(hpTime, false)
	y = y - 0.02 - HP_ROW_GAP

	-- Строки: подпись слева, кнопки сеткой по HP_COLS в ряд.
	for r = 1, #rows do
		local row = rows[r]
		id = id + 1
		HpLabel(left + HP_PAD, y - HP_BTN_H, labelW, id, row.title)
		local n = #row.options
		for i = 1, n do
			local c, line = (i - 1) % HP_COLS + 1, (i - 1) // HP_COLS
			id = id + 1
			HpButton(colX[c], y - HP_BTN_H - line * (HP_BTN_H + HP_GAP), colW[c], id, row.options[i])
		end
		local lines = (n + HP_COLS - 1) // HP_COLS
		y = y - lines * HP_BTN_H - (lines - 1) * HP_GAP - HP_ROW_GAP
	end

	-- Управление лобби: кнопки одной ширины по центру панели.
	y = y - 0.004
	id = id + 1
	HpButton(0.4 - lobbyW - HP_GAP / 2, y - HP_BTN_H, lobbyW, id, lobby[1])
	id = id + 1
	hpMinute = HpButton(0.4 + HP_GAP / 2, y - HP_BTN_H, lobbyW, id, lobby[2])
	y = y - HP_BTN_H - HP_PAD

	FrameSetAbsPoint(hpRoot, FRAMEPOINT_TOPLEFT, left, top)
	FrameSetAbsPoint(hpRoot, FRAMEPOINT_BOTTOMRIGHT, left + width, y)
	FrameSetShown(hpMeasure, false)
	HpSetShown(false)
	HpRefresh()
	HpTickFn()
	hpTick = CreateTimer()
	TimerStart(hpTick, 0.25, true, HpTickFn)
	HpShow(true)
	return true
end

-- Закрывает панель в конце лобби, до создания колец выбора расы.
function HostPanel_Close()
	if hpRoot == nil then return end
	HpShow(false)
	if hpTick ~= nil then
		PauseTimer(hpTick)
		DestroyTimer(hpTick)
		hpTick = nil
	end
end
