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
---@return nothing
function ShuffleStartLoc()
	local j, tmp
	for i = StartLocCount - 1, 1, -1 do
		j = GetRandomInt(0, i)
		tmp = StartLoc[i]
		StartLoc[i] = StartLoc[j]
		StartLoc[j] = tmp
	end
end
---@param x real
---@param y real
---@return boolean
function IsSpawnFarEnough(x, y)
	for pi, pt in pairs(AiSpawnPoint) do
		if DistanceBetweenCoords(x, y, pt.x, pt.y) < MIN_SPAWN_DISTANCE then
			return false
		end
	end
	return true
end
---@return real
function SpawnMinDistToOthers(x, y)
	local best = 999999.0
	for pi, pt in pairs(AiSpawnPoint) do
		local d = DistanceBetweenCoords(x, y, pt.x, pt.y)
		if d < best then
			best = d
		end
	end
	return best
end
---@param pi integer
---@return location
function AiPickSpawnPoint(pi)
	if StartLocCount == 0 then
		return nil
	end
	local i = AiSpawnIndex
	while i < StartLocCount do
		local loc = StartLoc[i]
		local x, y = GetLocationX(loc), GetLocationY(loc)
		if IsSpawnFarEnough(x, y) then
			AiSpawnPoint[pi] = {x = x, y = y}
			AiSpawnIndex = i + 1
			return loc
		end
		i = i + 1
	end
	local bestLoc = StartLoc[AiSpawnIndex] or StartLoc[0]
	local bestDist = -1.0
	i = AiSpawnIndex
	while i < StartLocCount do
		local loc = StartLoc[i]
		local d = SpawnMinDistToOthers(GetLocationX(loc), GetLocationY(loc))
		if d > bestDist then
			bestDist = d
			bestLoc = loc
		end
		i = i + 1
	end
	AiSpawnPoint[pi] = {x = GetLocationX(bestLoc), y = GetLocationY(bestLoc)}
	AiSpawnIndex = AiSpawnIndex + 1
	return bestLoc
end
-- library RandomLocs ends
