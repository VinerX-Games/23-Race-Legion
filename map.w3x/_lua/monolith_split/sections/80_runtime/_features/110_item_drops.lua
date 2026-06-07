-- *  Unit Item Tables
-- 
-- ***************************************************************************
---@return nothing
function Unit000387_DropItems()
	local trigWidget = nil
	local trigUnit = nil
	local itemID = 0
	local canDrop = true
	
	trigWidget = bj_lastDyingWidget
	if (trigWidget == nil) then
		trigUnit = GetTriggerUnit()
	end
	
	if (trigUnit ~= nil) then
		canDrop =  not IsUnitHidden(trigUnit)
		if (canDrop and GetChangingUnit() ~= nil) then
			canDrop = (GetChangingUnitPrevOwner() == Player(PLAYER_NEUTRAL_AGGRESSIVE))
		end
	end
	
	if (canDrop) then
		--  Item set 0
		RandomDistReset()
		RandomDistAddItem(-1, 100)
		itemID = RandomDistChoose()
		if (trigUnit ~= nil) then
			UnitDropItem(trigUnit, itemID)
		else
			WidgetDropItem(trigWidget, itemID)
		end
		
	end
	
	bj_lastDyingWidget = nil
	DestroyTrigger(GetTriggeringTrigger())
end
-- ***************************************************************************
-- 
