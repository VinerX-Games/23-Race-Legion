
-- ***************************************************************************
-- *  Settings
---@return nothing
function StartInc()
	
	local i = 0
	while true do
		if i >= 24 then break end
		income[i] = 0
		incomeW[i] = 0
		disincome[i] = 0
		logistic[i] = 0
		corruption[i] = 0
		balance[i] = 0
		additional[i] = 0
		AllyTax[i] = 0
		i = i + 1
	end
	RegionAddRect(Allmap, GetWorldBounds())
	
end