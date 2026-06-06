-- library common:
---@return boolean
function isEnemy()
	udg_LocalInteger2 = udg_LocalInteger2 + 1	--  Считаем колво
	return IsPlayerEnemy(GetOwningPlayer(GetFilterUnit()), udg_LocalPlayer)
	
end
-- library common ends
