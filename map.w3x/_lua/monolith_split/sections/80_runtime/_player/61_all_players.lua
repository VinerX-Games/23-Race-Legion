
--  scope init2 ends
-- ***************************************************************************
-- *  AllPlayersStart
---@return nothing
function AllPlayersStart()
	for pi = 0, 23 do
		if GetPlayerSlotState(Player(pi)) == PLAYER_SLOT_STATE_PLAYING then
			ForceAddPlayer(udg_AllPlayers, Player(pi))
			ForceAddPlayer(udg_AllPlayers2, Player(pi))
		end
	end
end
---@return nothing
function aiStart()
	for pi = 0, 23 do
		if GetPlayerController(Player(pi)) == MAP_CONTROL_COMPUTER then
			createAiPlayer(pi)
		end
	end
end