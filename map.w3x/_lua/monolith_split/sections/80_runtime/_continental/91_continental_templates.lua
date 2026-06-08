
--  scope initContinentalBoolExprs ends
-- ***************************************************************************
-- *  ContinentalTemplates
---@param g group
---@param fromThisArea boolexpr
---@return nothing
function RemoveOutsiders(g, fromThisArea)
	GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, fromThisArea)
	GroupRemoveGroup2(gSubGroup, g)
end
---@param g group
---@param fromAreaRect rect
---@return nothing
function AddOutsiders(g, fromAreaRect)
	GroupEnumUnitsInRect(gSubGroup, fromAreaRect, udg_B_EnemyUnit)
	GroupAddGroup2(gSubGroup, g)
end
---@return nothing
function DestroyRocksAct()
	gDestructable = GetEnumDestructable()
	if GetDestructableTypeId(gDestructable) == FourCC('B01K') then
		SetDestructableLife(gDestructable, GetDestructableLife(gDestructable) - 350)
	end
	
end
---@param r rect
---@return nothing
function DestroyRocks(r)
	EnumDestructablesInRect(r, nil, DestroyRocksAct)
end