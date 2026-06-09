
-- ***************************************************************************
-- *  InitThings
---@return nothing
function InitThings()
	local i = 0
	while true do
		if i == 25 then break end
		cap_time[i] = true
		Vassals[i] = CreateForce()
		Senior[i] = nil
		Capital[i] = nil
		
		i = i + 1
		
	end
	
	
end

-- ===========================================================================
-- FeodalSetVassalMode — Chat command to switch vassal inheritance mode
-- ===========================================================================
---@return nothing
function FeodalSetVassalMode()
	local msg = GetEventPlayerChatString()
	local mode = tonumber(string.sub(msg, 11))
	if mode == 1 then
		FeodalVassalMode = 1
		DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "Vassal inheritance: TRANSFER to senior's senior")
	elseif mode == 2 then
		FeodalVassalMode = 2
		DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "Vassal inheritance: ALL VASSALS LOSE")
	end
end

---@return nothing
function InitTrig_FeodalVassalMode()
	local trig = CreateTrigger()
	for i = 0, 23 do
		TriggerRegisterPlayerChatEvent(trig, Player(i), "-feodmode ", false)
	end
	TriggerAddAction(trig, FeodalSetVassalMode)
end