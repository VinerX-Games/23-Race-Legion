
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
		DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, Loc("lua.auto_752c8e81dfae30e3"))
	elseif mode == 2 then
		FeodalVassalMode = 2
		DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, Loc("lua.auto_f6fa02c187fd0122"))
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