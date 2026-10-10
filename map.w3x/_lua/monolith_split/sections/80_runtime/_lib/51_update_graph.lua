
-- ***************************************************************************
-- *  UpdateGraph
---@param pi integer
---@return nothing
function PercentGraph(pi)
	local ownerIndex = MultiboardItemOwnerIndex[pi]
	if ownerIndex == nil and EnsureMultiboardPlayerRow(pi) == nil then return end
	local item = ThirdColumn[pi]
	if item == nil and ownerIndex ~= nil then
		item = MultiboardGetItem(Multiboard, ownerIndex, 2)
		ThirdColumn[pi] = item
	end
	if item ~= nil then
		local count = CityCount or 0
		local pct = count > 0 and I2R(CityPlayerCount[pi] or 0) * 100.0 / I2R(count) or 0.0
		MultiboardSetItemValue(item, R2SW_Polyfill(pct) .. "%")
	end
end
---@param pi integer
---@return nothing
function ArmyExpGraph(pi)
	local ownerIndex = MultiboardItemOwnerIndex[pi]
	if ownerIndex == nil and EnsureMultiboardPlayerRow(pi) == nil then return end
	local item = ArmyPowerColumn[pi]
	if item == nil and ownerIndex ~= nil then
		item = MultiboardGetItem(Multiboard, ownerIndex, 3)
		ArmyPowerColumn[pi] = item
	end
	if item ~= nil then MultiboardSetItemValue(item, R2SW_Polyfill(ArmyExp[pi] or 0.001)) end
end
---@param pi integer
---@return nothing
function UpdateGraf(pi)
	local p = Player(pi)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	local r = R2I((udg_UnitsCount[pi] or 0) / 25.00)
	logistic[pi] = (500 + 100 * (r - 1)) / 2 * r	--  ??????????
	
	-- ????? ??????????? ????????
	if (udg_MainPrice[pi] or 0) ~= 0 and GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) >= 1 then
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
	MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 1], I2S(udg_UnitsCount[pi] or 0))
	PercentGraph(pi)
	ArmyExpGraph(pi)
	
end
