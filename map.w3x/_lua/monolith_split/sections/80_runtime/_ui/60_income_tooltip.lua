
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
		Loc("lua.auto_6ce872ab72265ae8") .. ResourceAmount(base),
		Loc("lua.auto_541666499cc23df8") .. ResourceValue(string.format("%.2f", modifier)),
		Loc("lua.auto_4e529aac8d8f3a28") .. ResourceValue(string.format("%.0f%%", tax * 100))
			.. " (" .. ResourceAmount(-base * modifier * tax) .. ")",
		Loc("lua.auto_5fbd8d0d8fda64c7") .. ResourceAmount(base * modifier * (1 - tax)),
		Loc("lua.auto_253c8bbcef699586") .. ResourceAmount(-upkeep),
		Loc("lua.auto_a46b2882d7a7cbf4") .. ResourceAmount(-transport),
		Loc("lua.auto_c1e9f3793437db82") .. ResourceAmount(refund),
		Loc("lua.auto_a2953833fe9e429a") .. ResourceAmount(bonus),
		Loc("lua.auto_81a7fd487c659924") .. ResourceAmount(net),
		Loc("lua.auto_4458c12f02185407") .. ResourceAmount(incomeW[pi] or 0),
	}
	if not DisOn then rows[#rows + 1] = Loc("lua.auto_b49fb6e4d6777d0f") end
	local remaining = udg_IncomeTimerSecond and TimerGetRemaining(udg_IncomeTimerSecond) or 0
	rows[#rows + 1] = remaining > 0
		and (Loc("lua.auto_2bbcac0f2a85b859") .. ResourceValue(math.ceil(remaining)) .. Loc("lua.auto_dab1f0e47a5117f2"))
		or Loc("lua.auto_d9b4c023c248c216")
	rows[#rows + 1] = Loc("lua.auto_5245d442f69fa873")
	BlzFrameSetText(tooltipBody, Loc("lua.auto_a86e547890c577f5") .. table.concat(rows, "|n") .. "|r")
	if net > 0 then
		BlzFrameSetText(tooltipTitle, Loc("lua.auto_9b473bbb7f16794d"))
	elseif net < 0 then
		BlzFrameSetText(tooltipTitle, Loc("lua.auto_c68851d2b26a6198"))
	else
		BlzFrameSetText(tooltipTitle, Loc("lua.auto_89c561e16ea27fd9"))
	end
	FitResourceTooltip(tooltip, tooltipBody, 0.32)
	-- The actual payout uses R2I (truncate), rather than rounding the amount.
	BlzFrameSetText(IncomeTextFr, ResourceAmount(R2I(net)) .. "|r")

	if stateBody == nil then return end
	local cities = CityPlayerCount[pi] or 0
	local total = CityCount or 0
	local capital = playerCapital[pi]
	local capitalName = Loc("lua.auto_ae6bef78e3c5ad94")
	if capital ~= nil and GetUnitState(capital, UNIT_STATE_LIFE) > 0.405
		and GetOwningPlayer(capital) == p then
		capitalName = GetUnitName(capital)
	end
	local state = {
		Loc("lua.auto_2de1bebf53a4930d") .. ResourceValue(cities) .. " / " .. ResourceValue(total),
		Loc("lua.auto_3b3b88d7791db525") .. ResourceValue(string.format("%.1f%%", total > 0 and cities * 100 / total or 0)),
		Loc("lua.auto_bb28d0c98efc8ffd") .. capitalName .. "|cffced4da",
	}
	if udg_GameMode == 3 or udg_GameMode == 5 then
		local target = math.floor(total * PercentWin / 100 + 0.5)
		state[#state + 1] = Loc("lua.auto_56c66422c020837f") .. ResourceValue(PercentWin) .. Loc("lua.auto_1b07bb787a6a599e") .. ResourceValue(target) .. ")"
		state[#state + 1] = Loc("lua.auto_ada93d34276f5052") .. ResourceValue(math.max(0, target - cities))
	else
		state[#state + 1] = Loc("lua.auto_5c5acfd77dfabdcc")
	end
	state[#state + 1] = Loc("lua.auto_7c64961450656198") .. ResourceValue(udg_UnitsCount[pi] or 0) .. Loc("lua.auto_9d95f9afed5e3343")
	BlzFrameSetText(stateBody, Loc("lua.auto_8bd88f056ebfbee3") .. table.concat(state, "|n") .. "|r")
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
	
	BlzFrameSetText(tooltipBody, Loc("lua.auto_ed58ee792770cf01"))
	BlzFrameSetText(tooltipTitle, Loc("lua.auto_9b473bbb7f16794d"))
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
		BlzFrameSetText(BlzGetFrameByName("BoxedTextTitle", 1), Loc("lua.auto_82adbf29b8139f1b"))
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
