-- *  AllPlayersStart
---@return nothing
function AllPlayersStart()
	gInt = 0
	
	
	while true do
		if gInt >= 23 then break end
		
		if GetPlayerSlotState(Player(gInt)) == PLAYER_SLOT_STATE_PLAYING then
			ForceAddPlayer(udg_AllPlayers, Player(gInt))
			ForceAddPlayer(udg_AllPlayers2, Player(gInt))
		end
		
		
		gInt = gInt + 1
	end
	
	
end
---@return nothing
function aiStart()
	gInt = 0
	while true do
		if gInt >= 23 then break end
		if GetPlayerController(Player(gInt)) == MAP_CONTROL_COMPUTER then
			createAiPlayer(gInt)
		end
		gInt = gInt + 1
	end
end
-- ***************************************************************************
