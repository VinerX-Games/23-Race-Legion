-- *  PointAi
---@return nothing
function AiPoitsSet()
	PointForAi[0] = Location(-18782, 469)
	PointForAi[1] = Location(-27743, 548)
	PointForAi[2] = Location(-26040, -6528)
	PointForAi[3] = Location(-16827, -5185)
	PointForAi[4] = Location(-16827, -5185)
	-- set PointForAi[5]=Location(-18782,469)
end
---@return nothing
function RandomAiPlace()
	local i = 0
	local c = 0
	local b = {}
	
	i = 0
	while true do
		if i >= 15 then break end
		
		if PointForAi[i] ~= nil then
			b[c] = PointForAi[i]
			PointForAi[i] = nil
			c = c + 1
		end
		i = i + 1
	end
	--  ??????? ?????? ??????? ?
	
	i = GetRandomInt(0, c - 1)
	udg_LocalPoint = b[i]
	i = 0
	while true do
		if i >= 15 then break end
		b[i] = nil
		
		i = i + 1
	end
	
	
end
-- ***************************************************************************
