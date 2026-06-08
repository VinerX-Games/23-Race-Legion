
-- ***************************************************************************
-- *  CommonHash
-- 
-- 
-- // ??? ?????? ???? ????? ??????, ?? ?????
-- function NumberAdd takes integer Playerid, integer Unitid returns nothing
--     local integer Cunit = LoadInteger(CommonHash,Playerid, Unitid) + 1
--     call SaveInteger(CommonHash,Playerid,Unitid,Cunit)
-- endfunction
-- 
-- function NumberRem takes integer Playerid, integer Unitid returns nothing
--     local integer Cunit = LoadInteger(CommonHash,Playerid, Unitid) - 1
--     call SaveInteger(CommonHash,Playerid,Unitid,Cunit)
-- endfunction
-- 
-- 
-- 
-- ***************************************************************************
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