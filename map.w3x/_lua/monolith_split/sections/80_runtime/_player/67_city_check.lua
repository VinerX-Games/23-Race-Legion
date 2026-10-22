
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
				DisplayTextToPlayer(Player(i), 0, 0, Loc("lua.auto_ad2516552a0f128e") .. GetPlayerName(p) .. Loc("lua.auto_ce73238ceb73013d") .. I2S(WinLimit) .. Loc("lua.auto_e9d0bbbfdc575574"))
			else
				DisplayTextToPlayer(Player(i), 0, 0, Loc("lua.auto_9396b0f099dd5132") .. I2S(WinLimit) .. Loc("lua.auto_8df17ea2bcbcc4a3"))
			end
			i = i + 1
		end
	elseif CityPlayerCount[winid] >= DangerLimit then
		while true do
			if i >= 23 then break end
			if i ~= winid then
				DisplayTextToPlayer(Player(i), 0, 0, Loc("lua.auto_8053af7449391a19") .. GetPlayerName(p) .. Loc("lua.auto_30c03b2cc47d4534") .. I2S(CityPlayerCount[winid]) .. Loc("lua.auto_5deb09bfbea204d3") .. I2S(WinLimit) .. Loc("lua.auto_726570465f08c41f"))
			else
				DisplayTextToPlayer(Player(i), 0, 0, Loc("lua.auto_a6e92d645867d601") .. I2S(CityPlayerCount[winid]) .. Loc("lua.auto_5deb09bfbea204d3") .. I2S(WinLimit) .. Loc("lua.auto_726570465f08c41f"))
			end
			i = i + 1
		end
	end
	
end