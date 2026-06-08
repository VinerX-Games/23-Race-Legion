
-- ***************************************************************************
-- *  ChangeSpellLimit
-- 
-- 
-- function OnlyFaselessFarms takes nothing returns boolean
--     return GetUnitTypeId(GetFilterUnit())=='u02E'
-- 
-- endfunction
-- 
-- 
-- 
---@param p player
---@return nothing
function FaselessFarmLimit(p)
	local i
	local NowLimit = GetPlayerTechMaxAllowed(p, FourCC('u02E'))
	local g = CreateGroup()
	-- local boolexpr b = Condition(function OnlyFaselessFarms)
	i = GetPlayerUnitTypeCount(p, FourCC('u02E'))
	
	if i <= NowLimit then
		SetPlayerAbilityAvailable(p, FourCC('A11G'), true)
	else
		SetPlayerAbilityAvailable(p, FourCC('A11G'), false)
	end
	
	
	DestroyGroup(g)
	g = nil
end