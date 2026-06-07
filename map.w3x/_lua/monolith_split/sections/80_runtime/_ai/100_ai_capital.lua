-- *  CapitalEnter
---@return nothing
function aiCapitalEnterAct()
	GroupAddUnit(AiCapitalBuildigs[gPi], GetEnumUnit())
end
--  ????????? ??? ?????? ????? ? ??????
---@param u unit
---@return nothing
function aiCapitalEnter(u)
	gPi = GetPlayerId(GetOwningPlayer(u))
	if udg_AiControl[gPi] then
		CheckPlayer = Player(gPi)
		GroupEnumUnitsInRange(gGroup, GetUnitX(u), GetUnitY(u), 3200, b_OwnBuldingsInRange)
		ForGroup(gGroup, aiCapitalEnterAct)
	end
end
-- ***************************************************************************
