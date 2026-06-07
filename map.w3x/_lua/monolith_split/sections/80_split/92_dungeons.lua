-- *  Dungeons
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleAzgel(x, y, g)
	if RectContainsCoords(gg_rct_Azgel, x, y) then
		RemoveOutsiders(g, udg_B_Azgel)
		AddOutsiders(g, gg_rct_Nord)
		if RectContainsCoords(gg_rct_AzNerRocks, x, y) then
			EnumDestructablesInRect((gg_rct_AzNerRocks), nil, DestroyRocksAct)	--  INLINED!!
		end
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleAnkirag(x, y, g)
	if RectContainsCoords(gg_rct_Ankirag, x, y) then
		RemoveOutsiders(g, udg_B_Ankirag)
		AddOutsiders(g, gg_rct_KalimSouth)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleBlackRock(x, y, g)
	if RectContainsCoords(gg_rct_BlackMountain, x, y) then
		RemoveOutsiders(g, udg_B_BlackRock)
		AddOutsiders(g, gg_rct_EKsouth)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleOrgrimmar(x, y, g)
	if RectContainsCoords(gg_rct_Orgrimmar, x, y) then
		RemoveOutsiders(g, udg_B_Orgrimmar)
		AddOutsiders(g, gg_rct_KalimCentral)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleDeadMines(x, y, g)
	if RectContainsCoords(gg_rct_DeadMines, x, y) then
		RemoveOutsiders(g, udg_B_DeadMines)
		AddOutsiders(g, gg_rct_EKsouth)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleStalgorn(x, y, g)
	if RectContainsCoords(gg_rct_Stalgorn2, x, y) and  not RectContainsCoords(gg_rct_UldumNotStalgorn, x, y) then
		RemoveOutsiders(g, udg_B_Stalgorn)
		AddOutsiders(g, gg_rct_EKsouth)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleUldum(x, y, g)
	if RectContainsCoords(gg_rct_Uldum, x, y) then
		RemoveOutsiders(g, udg_B_Uldum)
		AddOutsiders(g, gg_rct_EKsouth)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleMaradon(x, y, g)
	if RectContainsCoords(gg_rct_Maradon, x, y) then
		RemoveOutsiders(g, udg_B_Maradon)
		AddOutsiders(g, gg_rct_KalimCentral)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleUndercity(x, y, g)
	if RectContainsCoords(gg_rct_Undercity, x, y) then
		RemoveOutsiders(g, udg_B_Undercity)
		AddOutsiders(g, gg_rct_EKWest)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleWestDungeons(x, y, g)
	if RectContainsCoords(gg_rct_NoWater1, x, y) then
		if HandleAzgel(x, y, g) then
		elseif HandleAnkirag(x, y, g) then
		elseif HandleBlackRock(x, y, g) then
		elseif HandleOrgrimmar(x, y, g) then
		elseif HandleDeadMines(x, y, g) then
		elseif HandleStalgorn(x, y, g) then
		elseif HandleUldum(x, y, g) then
		end
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleCentralDungeons(x, y, g)
	if RectContainsCoords(gg_rct_NoWater3, x, y) then
		if HandleMaradon(x, y, g) then
		elseif HandleUndercity(x, y, g) then
		end
	end
	return false
end
--  elseif HandleMaradon(x, y, g) then
--  elseif HandleUndercity(x, y, g) then
-- ***************************************************************************
