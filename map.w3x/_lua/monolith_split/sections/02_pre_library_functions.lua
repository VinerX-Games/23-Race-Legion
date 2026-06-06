-- NOTE: vJASS->Lua emitted an EMPTY stub here (`function UnitAlive(u) end`) which
-- shadowed the engine native and returned nil for every call -> broke ALL AI combat
-- (IsAiCombatRetaskable / enemy filters / navy filter never matched). Real life-based
-- body (the map's own convention, same as f_LazyW) fixes every UnitAlive() call at once.
---@param u unit
---@return boolean
function UnitAlive(u)
	return u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end
---@param unitid integer
---@return integer
function GetUnitGoldCost(unitid) end	-- (native)
---@param unitid integer
---@return integer
function GetUnitWoodCost(unitid) end	-- (native)
---@param p player
---@param unitid integer
---@return integer
function GetPlayerUnitTypeCount(p, unitid) end	-- (native)
-- Generated allocator of StackTemplate
---@return integer
function s__StackTemplate__allocate()
	local this = si__StackTemplate_F
	if (this ~= 0) then
		si__StackTemplate_F = si__StackTemplate_V[this]
	else
		si__StackTemplate_I = si__StackTemplate_I + 1
		this = si__StackTemplate_I
	end
	if (this > 8190) then
		return 0
	end
	
	si__StackTemplate_V[this] = -1
	return this
end
-- Generated destructor of StackTemplate
---@param this integer
---@return nothing
function s__StackTemplate_deallocate(this)
	if this == nil then
		return 
	elseif (si__StackTemplate_V[this] ~= -1) then
		return 
	end
	si__StackTemplate_V[this] = si__StackTemplate_F
	si__StackTemplate_F = this
end
-- Generated allocator of SanctifiedEnchantment
---@return integer
function s__SanctifiedEnchantment__allocate()
	local this = si__SanctifiedEnchantment_F
	if (this ~= 0) then
		si__SanctifiedEnchantment_F = si__SanctifiedEnchantment_V[this]
	else
		si__SanctifiedEnchantment_I = si__SanctifiedEnchantment_I + 1
		this = si__SanctifiedEnchantment_I
	end
	if (this > 8190) then
		return 0
	end
	
	s__SanctifiedEnchantment_Time[this] = 0
	si__SanctifiedEnchantment_V[this] = -1
	return this
end
-- Generated destructor of SanctifiedEnchantment
---@param this integer
---@return nothing
function s__SanctifiedEnchantment_deallocate(this)
	if this == nil then
		return 
	elseif (si__SanctifiedEnchantment_V[this] ~= -1) then
		return 
	end
	si__SanctifiedEnchantment_V[this] = si__SanctifiedEnchantment_F
	si__SanctifiedEnchantment_F = this
end
