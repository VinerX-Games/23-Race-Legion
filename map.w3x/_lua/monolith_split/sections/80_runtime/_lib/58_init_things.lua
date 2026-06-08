
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