
-- ***************************************************************************
-- *  RandomLocationFromUnits
-- ***************************************************************************
-- *  CreateRaceCircles
---@param p player
---@return nothing
function CreateRaceCircles(p)
	
	local l = (StartLoc[GetRandomInt(0, StartLocCount - 1)])	--  INLINED!!
	CreateUnitAtLoc(p, FourCC('h0HJ'), l, 0)
	PanCameraToTimedLocForPlayer(p, l, 0)
	l = nil
end