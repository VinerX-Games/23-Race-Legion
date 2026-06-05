-- library RandomLocs:
---@return boolean
function isStartPosition()
	return GetUnitTypeId(GetFilterUnit()) == FourCC('h0O1')
end
---@return nothing
function SetStartLocations()
	local StartLocations = CreateGroup()
	local b = Condition(isStartPosition)
	local u
	GroupEnumUnitsInRect(StartLocations, bj_mapInitialPlayableArea, b)
	while true do
		u = FirstOfGroup(StartLocations)
		if u == nil then break end
		
		StartLoc[StartLocCount] = GetUnitLoc(u)
		StartLocCount = StartLocCount + 1
		
		
		GroupRemoveUnit(StartLocations, u)
		RemoveUnit(u)
		u = nil
	end
	
	DestroyGroup(StartLocations)
	StartLocations = nil
	DestroyBoolExpr(b)
	b = nil
	u = nil
end
---@return location
function RandomLoc()
	
	return StartLoc[GetRandomInt(0, StartLocCount - 1)]
	
end
-- library RandomLocs ends
