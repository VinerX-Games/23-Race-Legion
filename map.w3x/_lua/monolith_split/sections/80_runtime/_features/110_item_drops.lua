
-- ***************************************************************************
-- 
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
	if trigWidget == nil then
		trigUnit = GetTriggerUnit()
	end
	
	if trigUnit ~= nil then
		canDrop =  not IsUnitHidden(trigUnit)
		if canDrop and GetChangingUnit() ~= nil then
			canDrop = GetChangingUnitPrevOwner() == Player(PLAYER_NEUTRAL_AGGRESSIVE)
		end
	end
	
	if canDrop then
		--  Item set 0
		RandomDistReset()
		RandomDistAddItem(-1, 100)
		itemID = RandomDistChoose()
		if trigUnit ~= nil then
			UnitDropItem(trigUnit, itemID)
		else
			WidgetDropItem(trigWidget, itemID)
		end
		
	end
	
	bj_lastDyingWidget = nil
	DestroyTrigger(GetTriggeringTrigger())
end

-- ***************************************************************************
-- *  Spell-spawned item litter cleanup
-- *
-- *  Several hero spells spawn an item on the ground (Forsaken ult, Old Gods
-- *  spells). The caster is meant to walk over and pick it up, but AI heroes
-- *  never do, so the items pile up by the hundreds over a long game. Each
-- *  spawned item is registered here and removed if it is still lying on the
-- *  ground (not in anyone's inventory) after a grace window — long enough for
-- *  a human to grab it, short enough that AI litter does not accumulate.
-- ***************************************************************************
g_SpawnedItems = g_SpawnedItems or {}
ItemLitterGraceSec = ItemLitterGraceSec or 45.0
ItemLitterTickSec  = ItemLitterTickSec  or 10.0

---@param itemId integer
---@param x real
---@param y real
---@return item
function SpawnGroundItem(itemId, x, y)
	local it = CreateItem(itemId, x, y)
	g_SpawnedItems[#g_SpawnedItems + 1] = { item = it, age = 0.0 }
	return it
end

function ItemLitterCleanup()
	local kept = {}
	for _, e in ipairs(g_SpawnedItems) do
		local it = e.item
		if it ~= nil and GetItemTypeId(it) ~= 0 and GetWidgetLife(it) > 0.0 then
			if IsItemOwned(it) then
				-- picked up into an inventory — stop tracking, leave it alone
			else
				e.age = e.age + ItemLitterTickSec
				if e.age >= ItemLitterGraceSec then
					RemoveItem(it)
				else
					kept[#kept + 1] = e
				end
			end
		end
	end
	g_SpawnedItems = kept
end

function InitTrig_ItemLitterCleanup()
	TimerStart(CreateTimer(), ItemLitterTickSec, true, ItemLitterCleanup)
end