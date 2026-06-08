
-- ***************************************************************************
-- *  Enter
---@param u unit
---@return nothing
function Enter(u)
	local id = GetUnitTypeId(u)
	local p = GetOwningPlayer(u)
	local pi = GetPlayerId(p)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	
	
	
	if ownerIndex == nil then
		return
	end
	MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 1], I2S(udg_UnitsCount[pi]))
	
	
end