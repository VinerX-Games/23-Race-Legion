-- *  GoToWater
---@param pi integer
---@param u unit
---@param x real
---@param y real
---@return boolean
function GoToWaterPoint(pi, u, x, y)
	
	if Random(1, 10) and (AiData[pi][StringHash("NumberPorts")] or 0) < 8 then
		if RectContainsCoords(gg_rct_EastenKingdoms, x, y) then
			gInt = GetRandomInt(1, 4)
			if gInt == 1 then
				IssuePointOrder(u, "move", 30150, -3454)
			elseif gInt == 2 then
				IssuePointOrder(u, "move", 25504, -16284)
			elseif gInt == 3 then
				IssuePointOrder(u, "move", 19258, 5665)
			elseif gInt == 4 then
				IssuePointOrder(u, "move", 10979, 10501)
			end
		elseif RectContainsCoords(gg_rct_Kalim, x, y) then
			gInt = GetRandomInt(1, 4)
			if gInt == 1 then
				IssuePointOrder(u, "move", -28610, 16300)
			elseif gInt == 2 then
				IssuePointOrder(u, "move", -15796, -10105)
			elseif gInt == 3 then
				IssuePointOrder(u, "move", -12405, 96678)
			elseif gInt == 4 then
				IssuePointOrder(u, "move", -27443, 11058)
			end
		elseif RectContainsCoords(gg_rct_Nord, x, y) then
			gInt = GetRandomInt(1, 4)
			if gInt == 1 then
				IssuePointOrder(u, "move", -4711, 20912)
			elseif gInt == 2 then
				IssuePointOrder(u, "move", 8753, 22230)
			elseif gInt == 3 then
				IssuePointOrder(u, "move", 1273, 20088)
			elseif gInt == 4 then
				IssuePointOrder(u, "move", -15652, 21381)
			end
		elseif RectContainsCoords(gg_rct_BrokenIsles, x, y) then
			gInt = GetRandomInt(1, 2)
			if gInt == 1 then
				IssuePointOrder(u, "move", 2500, 12654)
			else
				IssuePointOrder(u, "move", 4121, 621)
			end
		elseif RectContainsCoords(gg_rct_Pandaria, x, y) then
			gInt = GetRandomInt(1, 2)
			if gInt == 1 then
				IssuePointOrder(u, "move", -9460, -12451)
			else
				IssuePointOrder(u, "move", -3941, -22869)
			end
		end
		
		return true
	end
	return false
end
-- ***************************************************************************
