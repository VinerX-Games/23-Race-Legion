
-- ***************************************************************************
-- *  BuildingTierSystem
---@param p player
---@return nothing
function Gstart(p)
	local pi = GetPlayerId(p)
	local phash = Gfarm
	local count = LoadInteger(Hash, pi, phash)
	SaveInteger(Hash, pi, phash, count + 1)
end
---@param pi integer
---@param phash integer
---@param addition integer
---@return nothing
function ChangeObjectsCount(pi, phash, addition)
	local count = LoadInteger(Hash, pi, phash)
	SaveInteger(Hash, pi, phash, count + addition)
	Ptiers(pi)
end