
-- ***************************************************************************
-- *  BuildingTierSystem
---@param p player
---@return nothing
function Gstart(p)
	local pi = GetPlayerId(p)
	local phash = Gfarm
	PData[pi] = PData[pi] or {}
	PData[pi][phash] = (PData[pi][phash] or 0) + 1
end
---@param pi integer
---@param phash integer
---@param addition integer
---@return nothing
function ChangeObjectsCount(pi, phash, addition)
	PData[pi] = PData[pi] or {}
	PData[pi][phash] = (PData[pi][phash] or 0) + addition
	Ptiers(pi)
end