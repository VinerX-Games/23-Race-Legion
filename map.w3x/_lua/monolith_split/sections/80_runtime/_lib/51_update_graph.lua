
-- ***************************************************************************
-- *  UpdateGraph
---@param pi integer
---@return nothing
function PercentGraph(pi)
	if ThirdColumn[pi] == nil and EnsureMultiboardPlayerRow(pi) == nil then
		return
	end
	MultiboardSetItemValue(ThirdColumn[pi], (R2SW_Polyfill(I2R(CityPlayerCount[pi]) * 100.0 / I2R(CityCount)) .. "%"))
end
---@param pi integer
---@return nothing
function ArmyExpGraph(pi)
	if ArmyPowerColumn[pi] == nil and EnsureMultiboardPlayerRow(pi) == nil then
		return
	end
	MultiboardSetItemValue(ArmyPowerColumn[pi], R2SW_Polyfill(ArmyExp[pi]))
end
---@param pi integer
---@return nothing
function UpdateGraf(pi)
	local p = Player(pi)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	local r = R2I(udg_UnitsCount[pi] / 25.00)
	logistic[pi] = ((500 + 100 * (r - 1)) / 2 * r)	--  ??????????
	
	-- ????? ??????????? ????????
	if GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) >= 1 then
		additional[pi] = disincome[pi] * (udg_MainPrice[pi] / (-100.0))
	end
	
	
	if DisOn then
		balance[pi] = income[pi] - disincome[pi] + corruption[pi] - logistic[pi] + additional[pi]
	else
		balance[pi] = income[pi]
	end
	
	--  ????????
	if ownerIndex == nil then
		return
	end
	MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 1], I2S(udg_UnitsCount[pi]))
	PercentGraph(pi)
	ArmyExpGraph(pi)
	
end