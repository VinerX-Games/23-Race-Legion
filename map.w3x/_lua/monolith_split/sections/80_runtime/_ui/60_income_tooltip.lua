
--  scope init ends
-- ***************************************************************************
-- *  IncomeTooltip
local stateHover
-- Общий контейнер показателя дохода: прячется целиком на экране выбора расы.
local incomeRoot
local stateTooltip
local stateBody

-- Give the text a fixed wrapping width and automatic height. A bottom anchor
-- would stretch it to the background and make measuring its content circular.
local function FitResourceTooltip(background, body, width)
	BlzFrameClearAllPoints(body)
	BlzFrameSetPoint(body, FRAMEPOINT_TOPLEFT, background, FRAMEPOINT_TOPLEFT, 0.005, -0.02)
	BlzFrameSetSize(body, width - 0.01, 0)
	BlzFrameSetSize(background, width, BlzFrameGetHeight(body) + 0.025)
end

local function ResourceAmount(value)
	local color = value < 0 and "|cffef8173" or "|cffc8e087"
	return color .. string.format("%+.0f", value) .. "|cffced4da"
end

local function ResourceValue(value)
	return "|cffffffff" .. tostring(value) .. "|cffced4da"
end

-- Only local presentation: never mutate economy, units or player state here.
function UpdateResourceTooltips(p, pi)
	local base = income[pi] or 0
	local modifier = IncomeMod or 1
	local tax = AllyTax[pi] or 0
	local upkeep = DisOn and (disincome[pi] or 0) or 0
	local transport = DisOn and (logistic[pi] or 0) or 0
	local refund = DisOn and (corruption[pi] or 0) or 0
	local bonus = DisOn and (additional[pi] or 0) or 0
	local net = balance[pi] or 0
	local rows = {
		"Базовый доход: " .. ResourceAmount(base),
		"Модификатор дохода: " .. ResourceValue(string.format("%.2f", modifier)),
		"Налог союзникам: " .. ResourceValue(string.format("%.0f%%", tax * 100))
			.. " (" .. ResourceAmount(-base * modifier * tax) .. ")",
		"Доход после модификатора и налога: " .. ResourceAmount(base * modifier * (1 - tax)),
		"|nСодержание армии: " .. ResourceAmount(-upkeep),
		"Логистика: " .. ResourceAmount(-transport),
		"Доход от коррупции: " .. ResourceAmount(refund),
		"Дополнительный доход: " .. ResourceAmount(bonus),
		"|nЧистый доход: " .. ResourceAmount(net),
		"Древесина за выплату: " .. ResourceAmount(incomeW[pi] or 0),
	}
	if not DisOn then rows[#rows + 1] = "|cffb99d66Расходы отключены в этом режиме.|cffced4da" end
	local remaining = udg_IncomeTimerSecond and TimerGetRemaining(udg_IncomeTimerSecond) or 0
	rows[#rows + 1] = remaining > 0
		and ("|nСледующая выплата через " .. ResourceValue(math.ceil(remaining)) .. " сек.")
		or "|nВыплаты начнутся после выбора режима."
	rows[#rows + 1] = "|cffb99d66Итог обновляется при выплате дохода.|cffced4da"
	BlzFrameSetText(tooltipBody, "|cffb99d66ИНТЕРФЕЙС:|cffced4da Доходы и расходы за выплату.|n|n" .. table.concat(rows, "|n") .. "|r")
	if net > 0 then
		BlzFrameSetText(tooltipTitle, "|cffebc56cЧистый доход|r")
	elseif net < 0 then
		BlzFrameSetText(tooltipTitle, "|cffebc56cЧистый убыток|r")
	else
		BlzFrameSetText(tooltipTitle, "|cffebc56cДоходы равны расходам|r")
	end
	FitResourceTooltip(tooltip, tooltipBody, 0.32)
	-- The actual payout uses R2I (truncate), rather than rounding the amount.
	BlzFrameSetText(IncomeTextFr, ResourceAmount(R2I(net)) .. "|r")

	if stateBody == nil then return end
	local cities = CityPlayerCount[pi] or 0
	local total = CityCount or 0
	local capital = playerCapital[pi]
	local capitalName = "Не назначена"
	if capital ~= nil and GetUnitState(capital, UNIT_STATE_LIFE) > 0.405
		and GetOwningPlayer(capital) == p then
		capitalName = GetUnitName(capital)
	end
	local state = {
		"Города: " .. ResourceValue(cities) .. " / " .. ResourceValue(total),
		"Доля территории: " .. ResourceValue(string.format("%.1f%%", total > 0 and cities * 100 / total or 0)),
		"Столица: " .. capitalName .. "|cffced4da",
	}
	if udg_GameMode == 3 or udg_GameMode == 5 then
		local target = math.floor(total * PercentWin / 100 + 0.5)
		state[#state + 1] = "|nДля победы: " .. ResourceValue(PercentWin) .. "% городов (" .. ResourceValue(target) .. ")"
		state[#state + 1] = "Осталось захватить: " .. ResourceValue(math.max(0, target - cities))
	else
		state[#state + 1] = "|nПобеда: по правилам выбранного режима."
	end
	state[#state + 1] = "|nАрмия: " .. ResourceValue(udg_UnitsCount[pi] or 0) .. " юнитов"
	BlzFrameSetText(stateBody, "|cffb99d66ИНТЕРФЕЙС:|cffced4da Состояние государства.|n|n" .. table.concat(state, "|n") .. "|r")
	FitResourceTooltip(stateTooltip, stateBody, 0.30)
end

---@return nothing
function Face2()
	
	
	BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
	incomeRoot = BlzCreateFrameByType("FRAME", "IncomeRoot", BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0), "", 0)
	-- Корень — точка, а не весь экран: дочерние фреймы стоят по своим точкам.
	BlzFrameSetSize(incomeRoot, 0.001, 0.001)
	FrameSetAbsPoint(incomeRoot, FRAMEPOINT_BOTTOMLEFT, 0.0, 0.0)
	face = BlzCreateFrameByType("BACKDROP", "Face", incomeRoot, "", 0)
	faceHover = BlzCreateFrameByType("FRAME", "FaceFrame", face, "", 0)
	IncomeTextFr = BlzCreateFrameByType("TEXT", "MyTextFrame", incomeRoot, "", 0)
	tooltip = BlzCreateFrame("BoxedText", face, 0, 0)
	tooltipBody = BlzGetFrameByName("BoxedTextValue", 0)
	tooltipTitle = BlzGetFrameByName("BoxedTextTitle", 0)
	BlzFrameSetText(IncomeTextFr, "|cffffffff0|r")
	FrameSetAbsPoint(IncomeTextFr, FRAMEPOINT_TOPRIGHT, 0.2337, 0.5937)
	BlzFrameSetEnable(IncomeTextFr, false)
	BlzFrameSetScale(IncomeTextFr, 1.075)
	BlzFrameSetTextAlignment(IncomeTextFr, TEXT_JUSTIFY_CENTER, TEXT_JUSTIFY_LEFT)
	BlzFrameSetAllPoints(faceHover, face)
	BlzFrameSetTooltip(faceHover, tooltip)
	
	BlzFrameSetSize(face, 0.085, 0.015)
	FrameSetAbsPoint(face, FRAMEPOINT_TOPRIGHT, 0.239, 0.5965)
	BlzFrameClearAllPoints(tooltip)
	BlzFrameSetAbsPoint(tooltip, FRAMEPOINT_TOPLEFT, 0.15, 0.575)
	BlzFrameSetTextAlignment(tooltipBody, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
	BlzFrameSetVisible(tooltip, false)
	
	BlzFrameSetText(tooltipBody, "|cffb99d66ИНТЕРФЕЙС:|cffced4da Доход с учётом модификаторов и расходов.|r")
	BlzFrameSetText(tooltipTitle, "|cffebc56cЧистый доход|r")
	FitResourceTooltip(tooltip, tooltipBody, 0.32)
	
	BlzFrameSetTexture(face, "ResourceBar222.tga", 0, true)

	-- The native supply listener is child 3 of ResourceBarFrame (Reforged).
	-- Replace its hover area, leaving the engine-owned food counter untouched.
	local supply = BlzGetFrameByName("ResourceBarSupplyText", 0)
	local resourceBar = BlzGetFrameByName("ResourceBarFrame", 0)
	if supply ~= nil and resourceBar ~= nil then
		stateHover = BlzCreateFrameByType("FRAME", "StateResourceHover", incomeRoot, "", 0)
		FrameSetPoint(stateHover, FRAMEPOINT_TOPRIGHT, supply, FRAMEPOINT_TOPRIGHT, 0.005, 0.003)
		BlzFrameSetSize(stateHover, 0.095, 0.022)
		BlzFrameSetLevel(stateHover, 5)
		stateTooltip = BlzCreateFrame("BoxedText", stateHover, 0, 1)
		stateBody = BlzGetFrameByName("BoxedTextValue", 1)
		BlzFrameSetText(BlzGetFrameByName("BoxedTextTitle", 1), "|cffebc56cГосударство|r")
		BlzFrameSetTextAlignment(stateBody, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
		BlzFrameClearAllPoints(stateTooltip)
		BlzFrameSetAbsPoint(stateTooltip, FRAMEPOINT_TOPRIGHT, 0.65, 0.575)
		FitResourceTooltip(stateTooltip, stateBody, 0.30)
		BlzFrameSetVisible(stateTooltip, false)
		BlzFrameSetTooltip(stateHover, stateTooltip)
		local listener = BlzFrameGetChild(resourceBar, 3)
		-- Нативная зона наведения на лимит больше не нужна: скрыта и уведена за экран навсегда.
		FrameSetShown(listener, false)
	end
	if CustomHud_Create ~= nil then CustomHud_Create() end

end

-- Показатель дохода и зона подсказки «Государство» — прячутся вместе с консолью.
-- Дочерние фреймы стоят по своим точкам, а не по корню: уводятся каждый сам.
function IncomeUISetVisible(show)
	if incomeRoot == nil then return end
	FrameSetShown(incomeRoot, show)
	FramePark(face, not show)
	FramePark(IncomeTextFr, not show)
	FramePark(stateHover, not show)
	ProbeLogWrite("[UI] income visible=" .. tostring(show))
end
--  scope init2 begins
---@return nothing
function init2___Init()
	Face2()
end
