
-- ***************************************************************************
-- *  CityCountCheck
---@param p player
---@return nothing
function CheckCity(p)
	local winid = GetPlayerId(p)
	local WinLimit = MathRound(CityCount * PercentWin / 100)
	local DangerLimit = MathRound(WinLimit * 0.75)
	local i = 0
	
	
	
	
	-- ??????
	if CityPlayerCount[winid] >= WinLimit then
		
		while true do
			if i >= 23 then break end
			if i ~= winid then
				ClearPlayer(Player(i))
				DisplayTextToPlayer(Player(i), 0, 0, "?? ?????????, ????? " .. GetPlayerName(p) .. " - ?????? " .. R2S(I2R(WinLimit) / I2R(CityCount)) .. "% ???-?? ????? ? ???????")
			else
				DisplayTextToPlayer(Player(i), 0, 0, "?? ????????!")
			end
			
			i = i + 1
		end
	elseif CityPlayerCount[winid] >= DangerLimit then
		while true do
			if i >= 23 then break end
			if i ~= winid then
				DisplayTextToPlayer(Player(i), 0, 0, "????????, ????? " .. GetPlayerName(p) .. " - ?????? " .. R2S(I2R(DangerLimit) / I2R(CityCount)) .. "% ???-?? ????? (" .. I2S(DangerLimit) .. ")")
			else
				DisplayTextToPlayer(Player(i), 0, 0, "?? ???????? " .. R2S(I2R(DangerLimit) / I2R(CityCount)) .. "%!")
			end
			
			i = i + 1
		end
		
		
	end
	
end