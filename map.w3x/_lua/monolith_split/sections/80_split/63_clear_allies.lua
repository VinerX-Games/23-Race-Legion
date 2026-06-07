-- *  ClearAllies
---@return nothing
function BrokeOneAlliance()
	SetPlayerAllianceStateBJ(gPlayer, GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
	SetPlayerAllianceStateBJ(GetEnumPlayer(), gPlayer, bj_ALLIANCE_UNALLIED)
end
---@param p player
---@return nothing
function ClearAllies(p)
	gPlayer = p
	ForForce(GetPlayersAllies(gPlayer), BrokeOneAlliance)
end
-- ***************************************************************************
