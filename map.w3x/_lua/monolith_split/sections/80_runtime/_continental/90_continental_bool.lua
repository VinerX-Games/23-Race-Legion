-- *  ContinentalBoolexrs
--  scope initContinentalBoolExprs begins
-- ????????? ???????????
--  ???? ???? ????????, ???? ?? ?? ???? ??????????
---@return boolean
function InKalim()
	return RectContainsUnit(gg_rct_Kalim, GetFilterUnit()) ~= true or RectContainsUnit(gg_rct_NordNotKalim, GetFilterUnit())
end
---@return boolean
function InNord()
	return RectContainsUnit(gg_rct_Nord, GetFilterUnit()) ~= true and RectContainsUnit(gg_rct_Azgel, GetFilterUnit()) ~= true
end
---@return boolean
function InVK()
	return (RectContainsUnit(gg_rct_EastenKingdoms, GetFilterUnit()) ~= true and RectContainsUnit(gg_rct_EasternDungeons, GetFilterUnit()) ~= true and RectContainsUnit(gg_rct_BlackMountain, GetFilterUnit()) ~= true) or RectContainsUnit(gg_rct_OutNoVk, GetFilterUnit())
end
---@return boolean
function InBisles()
	return RectContainsUnit(gg_rct_BrokenIsles, GetFilterUnit()) ~= true
end
---@return boolean
function InOutland()
	return RectContainsUnit(gg_rct_Outland, GetFilterUnit()) ~= true or RectContainsUnit(gg_rct_VknotOut, GetFilterUnit())
end
---@return boolean
function InArgus()
	return RectContainsUnit(gg_rct_Argus, GetFilterUnit()) ~= true
end
---@return boolean
function InPandaria()
	return RectContainsUnit(gg_rct_Pandaria, GetFilterUnit()) ~= true
end
--  ????????
---@return boolean
function InAnkirag()
	return RectContainsUnit(gg_rct_Ankirag, GetFilterUnit()) ~= true
end
---@return boolean
function InAzgel()
	return RectContainsUnit(gg_rct_Azgel, GetFilterUnit()) ~= true
end
---@return boolean
function InBlackRock()
	return RectContainsUnit(gg_rct_BlackMountain, GetFilterUnit()) ~= true
end
---@return boolean
function InOrgrimmar()
	return RectContainsUnit(gg_rct_Orgrimmar, GetFilterUnit()) ~= true
end
---@return boolean
function InDeadMines()
	return RectContainsUnit(gg_rct_DeadMines, GetFilterUnit()) ~= true
end
---@return boolean
function InStalgorn()
	return RectContainsUnit(gg_rct_Stalgorn, GetFilterUnit()) ~= true
end
---@return boolean
function InUldum()
	return RectContainsUnit(gg_rct_Uldum, GetFilterUnit()) ~= true
end
---@return boolean
function InMaradon()
	return RectContainsUnit(gg_rct_Maradon, GetFilterUnit()) ~= true
end
---@return boolean
function InUndercity()
	return RectContainsUnit(gg_rct_Undercity, GetFilterUnit()) ~= true
end
--  ???????? ??????
---@return boolean
function InDalaran()
	return RectContainsUnit(gg_rct_KillDalaran, GetFilterUnit()) ~= true
end
---@return boolean
function InNaxramas()
	return RectContainsUnit(gg_rct_Naxramas, GetFilterUnit()) ~= true
end
---@return nothing
function SetContinetsBooleprs()
	
	udg_B_InKalim = Condition(InKalim)
	udg_B_InNord = Condition(InNord)
	udg_B_InVK = Condition(InVK)
	udg_B_InOutland = Condition(InOutland)
	udg_B_InBIsles = Condition(InBisles)
	udg_B_InArgus = Condition(InArgus)
	udg_B_InPandaria = Condition(InPandaria)
	
	--  ????????
	udg_B_Ankirag = Condition(InAnkirag)
	udg_B_Azgel = Condition(InAzgel)
	udg_B_BlackRock = Condition(InBlackRock)
	udg_B_Orgrimmar = Condition(InOrgrimmar)
	udg_B_DeadMines = Condition(InDeadMines)
	udg_B_Stalgorn = Condition(InStalgorn)
	udg_B_Uldum = Condition(InUldum)
	udg_B_Maradon = Condition(InMaradon)
	udg_B_Undercity = Condition(InUndercity)
	
	-- ???????? ??????
	udg_B_Dalaran = Condition(InDalaran)
	udg_B_Naxramas = Condition(InNaxramas)
	
end
--  ?????????????? ??? ??? ????
---@return nothing
function initContinentalBoolExprs___Init()
	SetContinetsBooleprs()
end
--  scope initContinentalBoolExprs ends
-- ***************************************************************************
