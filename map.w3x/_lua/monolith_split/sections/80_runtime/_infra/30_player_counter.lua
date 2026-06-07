-- *  Counter
---@return boolean
function PlayerCounter()
	Counter = Counter + 1
	return true
end
---@return code
function startPlayerCounter()
	Counter = 0
	return PlayerCounter
	
end
-- ***************************************************************************
