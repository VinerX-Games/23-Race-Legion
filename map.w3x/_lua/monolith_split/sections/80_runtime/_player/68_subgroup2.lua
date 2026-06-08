-- *  SubGroup2
---@param count integer
---@param sourceGroup group
---@return group
function GetRandomSubGroup2(count, sourceGroup)
	GroupClear(SubGroup2)
	
	bj_randomSubGroupGroup = SubGroup2
	bj_randomSubGroupWant = count
	bj_randomSubGroupTotal = CountUnitsInGroup(sourceGroup)
	
	if bj_randomSubGroupWant <= 0 or bj_randomSubGroupTotal <= 0 then
		return SubGroup2
	end
	
	bj_randomSubGroupChance = I2R(bj_randomSubGroupWant) / I2R(bj_randomSubGroupTotal)
	ForGroup(sourceGroup, GetRandomSubGroupEnum)
	return SubGroup2
	
end
-- ***************************************************************************
