
-- ***************************************************************************
-- *  CityCountCheck
---@param p player
---@return nothing
function CheckCity(p)
	local winid = GetPlayerId(p)
	local WinLimit = MathRound(CityCount * PercentWin / 100)
	local DangerLimit = MathRound(WinLimit * 0.75)
	local i = 0
	
	
	
	
	-- Победа или предупреждение
	if CityPlayerCount[winid] >= WinLimit then
		while true do
			if i >= 23 then break end
			if i ~= winid then
				ClearPlayer(Player(i))
				DisplayTextToPlayer(Player(i), 0, 0, "|cffff4444Вы проиграли!|r Игрок |cffffcc00" .. GetPlayerName(p) .. "|r захватил требуемое число точек (|cffffffff" .. I2S(WinLimit) .. "|r) и одержал победу!")
			else
				DisplayTextToPlayer(Player(i), 0, 0, "|cff55ff55ПОБЕДА!|r Вы захватили требуемое число точек (|cffffffff" .. I2S(WinLimit) .. "|r) и одержали победу!")
			end
			i = i + 1
		end
	elseif CityPlayerCount[winid] >= DangerLimit then
		while true do
			if i >= 23 then break end
			if i ~= winid then
				DisplayTextToPlayer(Player(i), 0, 0, "|cffffaa00Осторожно!|r Игрок |cffffcc00" .. GetPlayerName(p) .. "|r близок к победе: захвачено |cffffffff" .. I2S(CityPlayerCount[winid]) .. "|r из |cffffffff" .. I2S(WinLimit) .. "|r точек!")
			else
				DisplayTextToPlayer(Player(i), 0, 0, "|cff55ff55Внимание!|r Вы близки к победе: захвачено |cffffffff" .. I2S(CityPlayerCount[winid]) .. "|r из |cffffffff" .. I2S(WinLimit) .. "|r точек!")
			end
			i = i + 1
		end
	end
	
end