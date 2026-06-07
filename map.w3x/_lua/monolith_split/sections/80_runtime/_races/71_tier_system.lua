-- *  CountForTier
---@param pi integer
---@return nothing
function Ptiers(pi)
	local phash = StringHash("Pfarm")
	local puhash = StringHash("Ptier")
	local count = LoadInteger(Hash, pi, phash)
	local u = LoadUnitHandle(Hash, pi, puhash)
	local id = GetUnitTypeId(u)
	
	
	
	-- call DisplayTextToPlayer(Player(0),0,0,GetUnitName(u))
	-- call DisplayTextToPlayer(Player(0),0,0,I2S(id))
	
	if count < 20 then
		KillUnit(u)
		
		
		
	elseif count < 55 then
		
		KillUnit(u)
		u = CreateUnit(Player(pi), FourCC('pa24'), 0, 0, 0.0)
		
	else
		KillUnit(u)
		u = CreateUnit(Player(pi), FourCC('pa25'), 0, 0, 0.0)
		
		
	end
	
	SaveUnitHandle(Hash, pi, puhash, u)
	u = nil
end
-- ***************************************************************************
