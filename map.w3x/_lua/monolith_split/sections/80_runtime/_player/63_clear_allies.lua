
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
-- Reentrancy guard: each SetPlayerAllianceStateBJ above fires gg_trg_StartAlly
-- SYNCHRONOUSLY, which (when a player is over DipMode) calls ClearAllies again —
-- re-entering this ForForce and clobbering the global gPlayer mid-iteration. With
-- the AI diplomat churning alliances on 20+ bots this nested cascade overflows and
-- hard-crashes the engine (uncatchable in Lua). gAllianceClearing makes the nested
-- StartAlly a no-op (see Trig_StartAlly_Actions) so the cascade can't recurse.
gAllianceClearing = gAllianceClearing or false
---@param p player
---@return nothing
function ClearAllies(p)
	if gAllianceClearing then return end
	gAllianceClearing = true
	gPlayer = p
	ForForce(GetPlayersAllies(gPlayer), BrokeOneAlliance)
	gAllianceClearing = false
end