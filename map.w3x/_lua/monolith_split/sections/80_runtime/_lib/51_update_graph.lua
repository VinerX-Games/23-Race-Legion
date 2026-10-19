
-- ***************************************************************************
-- *  UpdateGraph
-- Запись в ячейку главной таблицы через свежий хендл. Закэшированные хендлы
-- ячеек перестают работать после MultiboardSetColumnCount/RowCount
-- (ExpandTable, ExpandTableArmyExpr, EnsureMultiboardPlayerRow), и значение
-- до таблицы не доходит.
---@param row integer
---@param col integer
---@param value string
function MultiboardSetCell(row, col, value)
	if Multiboard == nil then return end
	local item = MultiboardGetItem(Multiboard, row, col)
	MultiboardSetItemValue(item, value)
	MultiboardReleaseItem(item)
end
---@param pi integer
---@return nothing
function PercentGraph(pi)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	if ownerIndex == nil or ThirdColumnHeader == nil then return end
	local count = CityCount or 0
	local pct = count > 0 and I2R(CityPlayerCount[pi] or 0) * 100.0 / I2R(count) or 0.0
	MultiboardSetCell(ownerIndex, 2, I2S(R2I(pct + 0.5)) .. "%")
end
---@param pi integer
---@return nothing
function ArmyExpGraph(pi)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	if ownerIndex == nil or ArmyPowerColumnHeader == nil then return end
	MultiboardSetCell(ownerIndex, 3, R2SW_Polyfill(ArmyExp[pi] or 0.001))
end
---@param unitCount integer
---@return number
function CalculateLogistics(unitCount)
	local count = math.max(0, unitCount or 0)
	local bracket = math.floor(count / 25)
	local base = (500 + 100 * (bracket - 1)) / 2 * bracket
	-- Preserve the old 25-unit anchors and interpolate the next bracket.
	return base + (count - bracket * 25) * (250 + 100 * bracket) / 25
end

---@param pi integer
---@return nothing
function UpdateGraf(pi)
	local p = Player(pi)
	local ownerIndex = EnsureMultiboardPlayerRow(pi)
	logistic[pi] = CalculateLogistics(udg_UnitsCount[pi])
	
	-- ????? ??????????? ????????
	if (udg_MainPrice[pi] or 0) ~= 0 and GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) >= 1 then
		additional[pi] = disincome[pi] * (udg_MainPrice[pi] / (-100.0))
	end
	
	
	if DisOn then
		balance[pi] = income[pi] * IncomeMod * (1 - AllyTax[pi]) - disincome[pi] + corruption[pi] - logistic[pi] + additional[pi]
	else
		balance[pi] = income[pi] * IncomeMod * (1 - AllyTax[pi])
	end
	
	--  ????????
	if ownerIndex == nil then
		return
	end
	MultiboardSetCell(ownerIndex, 1, I2S(udg_UnitsCount[pi] or 0))
	PercentGraph(pi)
	ArmyExpGraph(pi)
	
end
