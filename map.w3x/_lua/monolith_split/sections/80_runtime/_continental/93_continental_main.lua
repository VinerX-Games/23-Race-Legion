-- *  ContinentalMain
---@param x group
---@return nothing
function RemKalim(x)
	GroupRemoveUnit(x, gg_unit_h0E2_0011)
	GroupRemoveUnit(x, gg_unit_h08O_0444)
	GroupRemoveUnit(x, gg_unit_h09B_0508)
	GroupRemoveUnit(x, gg_unit_h09C_0509)
	GroupRemoveUnit(x, gg_unit_h097_0502)
	
end
---@param x group
---@return nothing
function RemKalim_P(x)
	GroupRemoveUnit(x, gg_unit_n003_0123)
	GroupRemoveUnit(x, gg_unit_n003_0124)
end
---@param x group
---@return nothing
function RemKalim_P2(x)
	GroupRemoveUnit(x, gg_unit_n003_0118)
	GroupRemoveUnit(x, gg_unit_n003_0117)
end
---@param x group
---@return nothing
function RemNord(x)
	GroupRemoveUnit(x, gg_unit_h09A_0506)
	GroupRemoveUnit(x, gg_unit_h09N_0346)
end
---@param x group
---@return nothing
function RemPandaria(x)
	GroupRemoveUnit(x, gg_unit_h09V_0137)
	GroupRemoveUnit(x, gg_unit_h0BH_0601)
	
end
---@param x group
---@return nothing
function RemVK(x)
	
	GroupRemoveUnit(x, gg_unit_h0BJ_0602)
	GroupRemoveUnit(x, gg_unit_h0BG_0600)
	GroupRemoveUnit(x, gg_unit_h0BF_0012)
	GroupRemoveUnit(x, gg_unit_h09P_0009)
	
end
---@param x group
---@return nothing
function RemBisles(x)
	GroupRemoveUnit(x, gg_unit_h0BL_0603)
	GroupRemoveUnit(x, gg_unit_h0BM_0604)
	GroupRemoveUnit(x, gg_unit_h0OK_0337)
end
---@param x group
---@return nothing
function RemWaterPortals(x)
	GroupRemoveUnit(x, gg_unit_n01D_0904)
	GroupRemoveUnit(x, gg_unit_n01D_0903)
	-- call GroupRemoveUnit(x, gg_unit_n003_0901)
	-- call GroupRemoveUnit(x, gg_unit_n003_0902)
end
---@param x group
---@return nothing
function RemEmeraldPortals(x)
	GroupRemoveUnit(x, gg_unit_n01Y_0934)
	GroupRemoveUnit(x, gg_unit_n01Y_0896)
	GroupRemoveUnit(x, gg_unit_n01Y_0889)
	GroupRemoveUnit(x, gg_unit_n01Y_0897)
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleKalim(x, y, g)
	if RectContainsCoords(gg_rct_Kalim, x, y) and  not RectContainsCoords(gg_rct_NordNotKalim, x, y) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InKalim)
		GroupRemoveGroup2(gSubGroup, g)
		RemKalim(g)
		RemKalim_P(g)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleNord(x, y, g)
	if RectContainsCoords(gg_rct_Nord, x, y) or RectContainsCoords(gg_rct_Azgel, x, y) or RectContainsCoords(gg_rct_NordNotKalim, x, y) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InNord)
		GroupRemoveGroup2(gSubGroup, g)
		RemNord(g)
		AddOutsiders(g, gg_rct_Azgel)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleVK(x, y, g)
	if (RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_EasternDungeons, x, y) or RectContainsCoords(gg_rct_BlackMountain, x, y) or RectContainsCoords(gg_rct_VknotOut, x, y)) and  not (RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(gg_rct_KillDalaran, x, y)) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InVK)
		GroupRemoveGroup2(gSubGroup, g)
		RemVK(g)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleOutland(x, y, g)
	if (RectContainsCoords(gg_rct_Outland, x, y) or RectContainsCoords(gg_rct_OutNoVk, x, y)) and  not RectContainsCoords(gg_rct_VknotOut, x, y) then
		local dp1_before = IsUnitInGroup(gg_unit_n006_0023, g)
		local dp2_before = IsUnitInGroup(gg_unit_n006_0438, g)
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InOutland)
		GroupRemoveGroup2(gSubGroup, g)
		local dp1_after = IsUnitInGroup(gg_unit_n006_0023, g)
		local dp2_after = IsUnitInGroup(gg_unit_n006_0438, g)
		local logKey = StringHash("Log_Outland_n006")
		if not (AiData[-1][logKey] or false) then
			AiData[-1][logKey] = true
			ProbeLogWrite("[CONT] HandleOutland x=" .. tostring(x) .. " y=" .. tostring(y) .. " n006_0023 before=" .. tostring(dp1_before) .. " after=" .. tostring(dp1_after) .. " n006_0438 before=" .. tostring(dp2_before) .. " after=" .. tostring(dp2_after))
		end
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleBrokenIsles(x, y, g)
	if RectContainsCoords(gg_rct_BrokenIsles, x, y) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InBIsles)
		GroupRemoveGroup2(gSubGroup, g)
		RemBisles(g)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandleArgus(x, y, g)
	if RectContainsCoords(gg_rct_Argus, x, y) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InArgus)
		GroupRemoveGroup2(gSubGroup, g)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return boolean
function HandlePandaria(x, y, g)
	if RectContainsCoords(gg_rct_Pandaria, x, y) then
		GroupEnumUnitsInRect(gSubGroup, bj_mapInitialPlayableArea, udg_B_InPandaria)
		GroupRemoveGroup2(gSubGroup, g)
		RemPandaria(g)
		return true
	end
	return false
end
---@param x real
---@param y real
---@param g group
---@return nothing
function ProcessContinentalStuff(x, y, g)
	if HandleKalim(x, y, g) then
	elseif HandleVK(x, y, g) then
	elseif HandleNord(x, y, g) then
	elseif HandlePandaria(x, y, g) then
	elseif HandleOutland(x, y, g) then
	elseif HandleBrokenIsles(x, y, g) then
	elseif HandleArgus(x, y, g) then
	elseif HandleWestDungeons(x, y, g) then
	elseif HandleCentralDungeons(x, y, g) then
	end
	
	RemWaterPortals(g)
	RemEmeraldPortals(g)
end
--  ???? ?????? ????????????
---@param x real
---@param y real
---@param g group
---@return nothing
function ProcessContinentalStuffNaga(x, y, g)
	
	if HandleOutland(x, y, g) then
	elseif HandleArgus(x, y, g) then
	elseif HandleAnkirag(x, y, g) then
	elseif HandleWestDungeons(x, y, g) then
	elseif HandleCentralDungeons(x, y, g) then
	end
	
	
	RemWaterPortals(g)
	RemEmeraldPortals(g)
end
-- ***************************************************************************
