
-- ***************************************************************************
-- *  Pstart
---@param p player
---@return nothing
function Pstart(p)
	local pi = GetPlayerId(p)
	local phash = StringHash("Pfarm")
	local count = LoadInteger(Hash, pi, phash)
	SaveInteger(Hash, pi, phash, count + 1)
	
end