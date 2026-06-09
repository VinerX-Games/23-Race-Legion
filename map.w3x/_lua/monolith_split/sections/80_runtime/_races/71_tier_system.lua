
-- ***************************************************************************
-- *  CountForTier
---@param pi integer
---@return nothing
function Ptiers(pi)
	local phash = StringHash("Pfarm")
	local puhash = StringHash("Ptier")
	PData[pi] = PData[pi] or {}
	local count = PData[pi][phash] or 0
	local u = PData[pi][puhash]
	local id = GetUnitTypeId(u)
	
	if count < 20 then
		KillUnit(u)
	elseif count < 55 then
		KillUnit(u)
		u = CreateUnit(Player(pi), FourCC('pa24'), 0, 0, 0.0)
	else
		KillUnit(u)
		u = CreateUnit(Player(pi), FourCC('pa25'), 0, 0, 0.0)
	end
	
	PData[pi][puhash] = u
	u = nil
end