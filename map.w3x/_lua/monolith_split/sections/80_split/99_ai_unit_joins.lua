-- *  AiUnitJoins
---@param u unit
---@param pi integer
---@return nothing
function aiUnitJoins(u, pi)
	local id = GetUnitTypeId(u)
	
	GroupAddUnit(udg_Ai_units[pi], u)
	-- call UnitApplyTimedLife( u,'BTLF',1200.00)
	NumberAdd(pi, id)
	
	AiDispatchJoin(id, pi, u)
	
end
-- ***************************************************************************
