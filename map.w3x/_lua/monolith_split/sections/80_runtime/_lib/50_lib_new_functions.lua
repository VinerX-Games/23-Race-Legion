
--  scope initBoolExprs ends
-- ***************************************************************************
-- *  LibNewFunctions
-- ***************************************************************************
-- *  AddExp
---@param u unit
---@param pi integer
---@return nothing
function addArmyExp(u, pi)
	--    call BJDebugMsg("Start")
	gPlayer = GetOwningPlayer(u)
	gId = GetUnitTypeId(u)
	gPi = GetPlayerId(gPlayer)
	if IsPlayerAlly(gPlayer, Player(pi)) then
		return 
	end
	
	if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
		if IsUnitInGroup(gAttacked, udg_ZahvatBuildings) then
			gReal = 1
		else
			gReal = I2R(GetUnitGoldCost(gId) or 0) * 0.01
		end
	else
		if IsUnitType(u, UNIT_TYPE_HERO) then
			gReal = GetHeroLevel(u) * 1
		else
			gReal = I2R(GetUnitGoldCost(gId) or 0) * 0.02
		end
	end
	ArmyExp[pi] = (ArmyExp[pi] or 0) + gReal
	ArmyExp[gPi] = RMaxBJ(0, (ArmyExp[gPi] or 0) - gReal * 0.9)
	--  call BJDebugMsg( GetUnitName(u)+" "+R2S(ArmyExp[pi]))
end
-- ????????????? ????? ?? ????
---@param pi integer
---@return nothing
function ArmyExpSetBonus(pi)
	if ArmyExpBonus[pi] == nil then
		return
	end
	SetUnitAbilityLevel(ArmyExpBonus[pi], FourCC('arb1'), IMinBJ(R2I((ArmyExp[pi] / 500) + 1), 11))
	SetUnitAbilityLevel(ArmyExpBonus[pi], FourCC('arb0'), IMinBJ(R2I((ArmyExp[pi] / 500) + 1), 11))
end
--  ????????? ??????? ?????
---@return nothing
function ExpandTableArmyExpr()
	local i = 0
	MultiboardSetColumnCount(Multiboard, 4)
	
	
	local header = MultiboardGetItem(Multiboard, 0, 3)
	ArmyPowerColumnHeader = header
	MultiboardSetItemValue(header, "Опыт")
	MultiboardSetItemWidth(header, 0.06)
	MultiboardReleaseItem(header)
	
	while true do
		if i > 23 then break end
		ArmyExp[i] = 0.001
		local ownerIndex = MultiboardItemOwnerIndex[i]
		if ownerIndex ~= nil then
			ArmyPowerColumn[i] = MultiboardGetItem(Multiboard, ownerIndex, 3)
			MultiboardSetItemValue(ArmyPowerColumn[i], "0")
			MultiboardSetItemWidth(ArmyPowerColumn[i], 0.06)
		end
		i = i + 1
		
	end
	
	
	
	MultiboardDisplay(Multiboard, false)
	MultiboardDisplay(Multiboard, true)
	
	
end
