-- library AI:
---@param pi integer
---@return nothing
function turnOffAi(pi)
	if  not udg_AiControl[gPi] then
		return 
	end
	
	udg_AiControl[pi] = false
	ForceRemovePlayer(udg_Bots, Player(pi))
	
	
	
end
-- library AI ends
