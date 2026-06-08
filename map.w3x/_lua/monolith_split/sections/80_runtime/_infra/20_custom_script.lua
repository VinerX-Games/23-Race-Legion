
-- ***************************************************************************
-- 
-- *  Custom Script Code
-- 
-- ***************************************************************************
-- ***************************************************************************
-- *  Map
--  ??????? ??????
---@return nothing
function HandleCounter_Update()
	local i = 0
	local id = 0
	local P = {}
	local result = 0
	while true do
		if i >= 50 then break end
		i = i + 1
		P[i] = Location(0, 0)
		id = GetHandleId(P[i])
		result = result + (id - 0x100000)
	end
	result = result / i - i / 2
	while true do
		RemoveLocation(P[i])
		P[i] = nil
		if i <= 1 then break end
		i = i - 1
	end
	LeaderboardSetItemValue(udg_HandleBoard, 0, R2I(result))
end
---@return nothing
function HandleCounter_Actions()
	udg_HandleBoard = CreateLeaderboard()
	LeaderboardSetLabel(udg_HandleBoard, "Handle Counter")
	PlayerSetLeaderboard(GetLocalPlayer(), udg_HandleBoard)
	LeaderboardDisplay(udg_HandleBoard, true)
	LeaderboardAddItem(udg_HandleBoard, "Handles", 0, Player(0))
	LeaderboardSetSizeByItemCount(udg_HandleBoard, 1)
	HandleCounter_Update()
	TimerStart(GetExpiredTimer(), 0.05, true, HandleCounter_Update)
end
---@return nothing
function InitTrig_HandleCounter()
	TimerStart(CreateTimer(), 0, false, HandleCounter_Actions)
end
--  ????? ???????? ??????
---@return nothing
function ReturnFPS()
	framehandlefps = BlzGetFrameByName("ResourceBarFrame", 0)
	BlzFrameSetVisible(fps, true)
	BlzFrameClearAllPoints(fps)
	BlzFrameSetAbsPoint(fps, FRAMEPOINT_CENTER, 0.95, 0.62)
end
-- ***************************************************************************
-- *  Replace
--  ????? ???????????? ????????????, ??? ???? ????? "???????? ?????? ??????"
-- ??? ????????
---@param whichUnit unit
---@param newUnitId integer
---@param unitStateMethod integer
---@return unit
function ReplaceUnit(whichUnit, newUnitId, unitStateMethod)
	local oldUnit = whichUnit
	local newUnit
	local wasHidden
	local index
	local indexItem
	local oldRatio
	
	--  If we have bogus data, don't attempt the replace.
	if oldUnit == nil then
		bj_lastReplacedUnit = oldUnit
		return oldUnit
	end
	
	--  Hide the original unit.
	wasHidden = IsUnitHidden(oldUnit)
	ShowUnit(oldUnit, false)
	
	--  Create the replacement unit.
	if newUnitId == FourCC('ugol') then
		newUnit = CreateBlightedGoldmine(GetOwningPlayer(oldUnit), GetUnitX(oldUnit), GetUnitY(oldUnit), GetUnitFacing(oldUnit))
	else
		newUnit = CreateUnit(GetOwningPlayer(oldUnit), newUnitId, GetUnitX(oldUnit), GetUnitY(oldUnit), GetUnitFacing(oldUnit))
	end
	
	--  Set the unit's life and mana according to the requested method.
	if unitStateMethod == bj_UNIT_STATE_METHOD_RELATIVE then
		--  Set the replacement's current/max life ratio to that of the old unit.
		--  If both units have mana, do the same for mana.
		if GetUnitState(oldUnit, UNIT_STATE_MAX_LIFE) > 0 then
			oldRatio = GetUnitState(oldUnit, UNIT_STATE_LIFE) / GetUnitState(oldUnit, UNIT_STATE_MAX_LIFE)
			SetUnitState(newUnit, UNIT_STATE_LIFE, oldRatio * GetUnitState(newUnit, UNIT_STATE_MAX_LIFE))
		end
		
		if (GetUnitState(oldUnit, UNIT_STATE_MAX_MANA) > 0) and (GetUnitState(newUnit, UNIT_STATE_MAX_MANA) > 0) then
			oldRatio = GetUnitState(oldUnit, UNIT_STATE_MANA) / GetUnitState(oldUnit, UNIT_STATE_MAX_MANA)
			SetUnitState(newUnit, UNIT_STATE_MANA, oldRatio * GetUnitState(newUnit, UNIT_STATE_MAX_MANA))
		end
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_ABSOLUTE) then
		--  Set the replacement's current life to that of the old unit.
		--  If the new unit has mana, do the same for mana.
		SetUnitState(newUnit, UNIT_STATE_LIFE, GetUnitState(oldUnit, UNIT_STATE_LIFE))
		if GetUnitState(newUnit, UNIT_STATE_MAX_MANA) > 0 then
			SetUnitState(newUnit, UNIT_STATE_MANA, GetUnitState(oldUnit, UNIT_STATE_MANA))
		end
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_DEFAULTS) then
		--  The newly created unit should already have default life and mana.
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_MAXIMUM) then
		--  Use max life and mana.
		SetUnitState(newUnit, UNIT_STATE_LIFE, GetUnitState(newUnit, UNIT_STATE_MAX_LIFE))
		SetUnitState(newUnit, UNIT_STATE_MANA, GetUnitState(newUnit, UNIT_STATE_MAX_MANA))
	else
		--  Unrecognized unit state method - ignore the request.
	end
	
	--  Mirror properties of the old unit onto the new unit.
	-- call PauseUnit(newUnit, IsUnitPaused(oldUnit))
	SetResourceAmount(newUnit, GetResourceAmount(oldUnit))
	
	--  If both the old and new units are heroes, handle their hero info.
	if IsUnitType(oldUnit, UNIT_TYPE_HERO) and IsUnitType(newUnit, UNIT_TYPE_HERO) then
		SetHeroXP(newUnit, GetHeroXP(oldUnit), false)
		
		index = 0
		while true do
			indexItem = UnitItemInSlot(oldUnit, index)
			if indexItem ~= nil then
				UnitRemoveItem(oldUnit, indexItem)
				UnitAddItem(newUnit, indexItem)
			end
			
			index = index + 1
			if index >= bj_MAX_INVENTORY then break end
		end
	end
	
	--  Remove or kill the original unit.  It is sometimes unsafe to remove
	--  hidden units, so kill the original unit if it was previously hidden.
	
	
	RemoveUnit(oldUnit)
	
	
	bj_lastReplacedUnit = newUnit
	oldUnit = nil
	indexItem = nil
	newUnit = nil
	return bj_lastReplacedUnit
	
end
-- ? ?????????
---@param whichUnit unit
---@param newUnitId integer
---@param unitStateMethod integer
---@return unit
function ReplaceUnit2(whichUnit, newUnitId, unitStateMethod)
	local oldUnit = whichUnit
	local newUnit
	local wasHidden
	local index
	local indexItem
	local oldRatio
	
	--  If we have bogus data, don't attempt the replace.
	if oldUnit == nil then
		bj_lastReplacedUnit = oldUnit
		return oldUnit
	end
	
	--  Hide the original unit.
	wasHidden = IsUnitHidden(oldUnit)
	ShowUnit(oldUnit, false)
	
	--  Create the replacement unit.
	if newUnitId == FourCC('ugol') then
		newUnit = CreateBlightedGoldmine(GetOwningPlayer(oldUnit), GetUnitX(oldUnit), GetUnitY(oldUnit), GetUnitFacing(oldUnit))
	else
		newUnit = CreateUnit(GetOwningPlayer(oldUnit), newUnitId, GetUnitX(oldUnit), GetUnitY(oldUnit), GetUnitFacing(oldUnit))
	end
	
	--  Set the unit's life and mana according to the requested method.
	if unitStateMethod == bj_UNIT_STATE_METHOD_RELATIVE then
		--  Set the replacement's current/max life ratio to that of the old unit.
		--  If both units have mana, do the same for mana.
		if GetUnitState(oldUnit, UNIT_STATE_MAX_LIFE) > 0 then
			oldRatio = GetUnitState(oldUnit, UNIT_STATE_LIFE) / GetUnitState(oldUnit, UNIT_STATE_MAX_LIFE)
			SetUnitState(newUnit, UNIT_STATE_LIFE, oldRatio * GetUnitState(newUnit, UNIT_STATE_MAX_LIFE))
		end
		
		if (GetUnitState(oldUnit, UNIT_STATE_MAX_MANA) > 0) and (GetUnitState(newUnit, UNIT_STATE_MAX_MANA) > 0) then
			oldRatio = GetUnitState(oldUnit, UNIT_STATE_MANA) / GetUnitState(oldUnit, UNIT_STATE_MAX_MANA)
			SetUnitState(newUnit, UNIT_STATE_MANA, oldRatio * GetUnitState(newUnit, UNIT_STATE_MAX_MANA))
		end
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_ABSOLUTE) then
		--  Set the replacement's current life to that of the old unit.
		--  If the new unit has mana, do the same for mana.
		SetUnitState(newUnit, UNIT_STATE_LIFE, GetUnitState(oldUnit, UNIT_STATE_LIFE))
		if GetUnitState(newUnit, UNIT_STATE_MAX_MANA) > 0 then
			SetUnitState(newUnit, UNIT_STATE_MANA, GetUnitState(oldUnit, UNIT_STATE_MANA))
		end
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_DEFAULTS) then
		--  The newly created unit should already have default life and mana.
	elseif (unitStateMethod == bj_UNIT_STATE_METHOD_MAXIMUM) then
		--  Use max life and mana.
		SetUnitState(newUnit, UNIT_STATE_LIFE, GetUnitState(newUnit, UNIT_STATE_MAX_LIFE))
		SetUnitState(newUnit, UNIT_STATE_MANA, GetUnitState(newUnit, UNIT_STATE_MAX_MANA))
	else
		--  Unrecognized unit state method - ignore the request.
	end
	
	--  Mirror properties of the old unit onto the new unit.
	-- call PauseUnit(newUnit, IsUnitPaused(oldUnit))
	SetResourceAmount(newUnit, GetResourceAmount(oldUnit))
	
	--  If both the old and new units are heroes, handle their hero info.
	if IsUnitType(oldUnit, UNIT_TYPE_HERO) and IsUnitType(newUnit, UNIT_TYPE_HERO) then
		SetHeroXP(newUnit, GetHeroXP(oldUnit), false)
		
		index = 0
		while true do
			indexItem = UnitItemInSlot(oldUnit, index)
			if indexItem ~= nil then
				UnitRemoveItem(oldUnit, indexItem)
				UnitAddItem(newUnit, indexItem)
			end
			
			index = index + 1
			if index >= bj_MAX_INVENTORY then break end
		end
	end
	
	--  Remove or kill the original unit.  It is sometimes unsafe to remove
	--  hidden units, so kill the original unit if it was previously hidden.
	
	
	
	KillUnit(oldUnit)
	RemoveUnit(oldUnit)
	
	bj_lastReplacedUnit = newUnit
	oldUnit = nil
	indexItem = nil
	newUnit = nil
	return bj_lastReplacedUnit
	
end