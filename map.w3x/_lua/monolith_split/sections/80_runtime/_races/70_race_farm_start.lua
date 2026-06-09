
-- ***************************************************************************
-- *  Pstart
---@param p player
---@return nothing
function Pstart(p)
	local pi = GetPlayerId(p)
	local phash = StringHash("Pfarm")
	PData[pi] = PData[pi] or {}
	PData[pi][phash] = (PData[pi][phash] or 0) + 1
end