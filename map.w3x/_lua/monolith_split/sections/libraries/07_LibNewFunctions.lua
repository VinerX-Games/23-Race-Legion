-- library LibNewFunctions:
-- ***************************************************************************
-- *  R2SW_Polyfill
---@param value real
---@return string
function R2SW_Polyfill(value)
	local output = ""
	local two_off = ModuloInteger(R2I(value / 0.01), 10)
	local on_off = ModuloInteger(R2I(value / 0.1), 10)
	return I2S(R2I(value)) .. "." .. I2S(on_off) .. I2S(two_off)
end
-- ***************************************************************************
-- *  GroupPickRandomUnit2
---@return nothing
function GroupPickRandomUnitEnum2()
	bj_groupRandomConsidered = bj_groupRandomConsidered + 1
	if GetRandomInt(1, bj_groupRandomConsidered) == 1 then
		bj_groupRandomCurrentPick = GetEnumUnit()
	end
end
---@param whichGroup group
---@return unit
function GroupPickRandomUnit2(whichGroup)
	
	bj_groupRandomConsidered = 0
	bj_groupRandomCurrentPick = nil
	ForGroup(whichGroup, GroupPickRandomUnitEnum2)
	
	
	return bj_groupRandomCurrentPick
end
-- ***************************************************************************
-- *  Distance
---@param u unit
---@param target unit
---@return real
function DistanceBetweenUnits(u, target)
	gX2 = GetUnitX(u) - GetUnitX(target)
	gY2 = GetUnitY(u) - GetUnitY(target)
	return SquareRoot(gX2 * gX2 + gY2 * gY2)
end
---@param x real
---@param y real
---@param x2 real
---@param y2 real
---@return real
function DistanceBetweenCoords2(x, y, x2, y2)
	gX2 = x - x2
	gY2 = y - y2
	return SquareRoot(gX2 * gX2 + gY2 * gY2)
end
---@param x real
---@param y real
---@param target unit
---@return real
function DistanceBetweenUnitsXY(x, y, target)
	gX2 = x - GetUnitX(target)
	gY2 = y - GetUnitY(target)
	return SquareRoot(gX2 * gX2 + gY2 * gY2)
end
-- ***************************************************************************
-- *  GroupRemoveGroup2
---@return nothing
function GroupRemoveGroupEnum2()
	GroupRemoveUnit(bj_groupRemoveGroupDest, GetEnumUnit())
end
---@param sourceGroup group
---@param destGroup group
---@return nothing
function GroupRemoveGroup2(sourceGroup, destGroup)
	bj_groupRemoveGroupDest = destGroup
	ForGroup(sourceGroup, GroupRemoveGroupEnum2)
end
-- ***************************************************************************
-- *  GroupAddGroup2
---@return nothing
function GroupAddGroupEnum2()
	GroupAddUnit(bj_groupRemoveGroupDest, GetEnumUnit())
end
---@param sourceGroup group
---@param destGroup group
---@return nothing
function GroupAddGroup2(sourceGroup, destGroup)
	bj_groupRemoveGroupDest = destGroup
	ForGroup(sourceGroup, GroupAddGroupEnum2)
end
-- ***************************************************************************
-- *  RandomFunction
---@param Chance integer
---@param FromAll integer
---@return boolean
function Random(Chance, FromAll)
	local i = GetRandomInt(1, FromAll)
	return i <= Chance
end
-- ***************************************************************************
-- *  RemoveAbilityTimed
---@param u unit
---@param abilid integer
---@param time real
---@return nothing
function RemoveAbilityTimed(u, abilid, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		UnitRemoveAbility(u, abilid)
		DestroyTimer(t)
	end)
end
---@param u unit
---@param abilid integer
---@param time real
---@return nothing
function AddAbilityTimed(u, abilid, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		UnitAddAbility(u, abilid)
		DestroyTimer(t)
	end)
end
---@param u unit
---@param abilid integer
---@param time real
---@return nothing
function RemoveAbilityTimedCD(u, abilid, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		if BlzGetUnitAbilityCooldownRemaining(u, abilid) == 0 then
			UnitRemoveAbility(u, abilid)
		end
		DestroyTimer(t)
	end)
end
-- ***************************************************************************
-- *  RemoveEffectTimed
---@param e effect
---@param time real
---@return nothing
function RemoveEffectTimed(e, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		DestroyEffect(e)
		DestroyTimer(t)
	end)
end
-- ***************************************************************************
-- *  CapitalFunctions
---@param pi integer
---@param x real
---@param y real
---@param radius real
---@return unit
function OwnCapitalInRange(pi, x, y, radius)
	CheckPlayer = Player(pi)
	GroupEnumUnitsInRange(gGroup, x, y, radius, b_OwnCapitalInRange)
	
	return FirstOfGroup(gGroup)
end
---@param u unit
---@return boolean
function isCapital(u)
	return IsUnitInGroup(u, udg_StolicaGroups)
end
-- ***************************************************************************
-- *  LibNewFunctionsEnd
-- library LibNewFunctions ends
