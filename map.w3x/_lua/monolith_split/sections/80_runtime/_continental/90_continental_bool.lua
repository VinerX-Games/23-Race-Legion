
-- ***************************************************************************
-- *  TurnOffAi
-- ***************************************************************************
-- *  Globals And Start setttings
--  --------------    --------------   ??????? ????? --------------   --------------
-- ***************************************************************************
-- *  LibDifferentAiStuff
-- ***************************************************************************
-- *  LibRaces
-- ***************************************************************************
-- *  ContinentalBoolexrs
--  scope initContinentalBoolExprs begins
-- ????????? ???????????
--  ???? ???? ????????, ???? ?? ?? ???? ??????????
---@return boolean
function InKalim()
	return not (RectContainsUnit(gg_rct_Kalim, GetFilterUnit())) or RectContainsUnit(gg_rct_NordNotKalim, GetFilterUnit())
end
---@return boolean
function InNord()
	return not (RectContainsUnit(gg_rct_Nord, GetFilterUnit())) and not (RectContainsUnit(gg_rct_Azgel, GetFilterUnit()))
end
---@return boolean
function InVK()
	return (not (RectContainsUnit(gg_rct_EastenKingdoms, GetFilterUnit())) and not (RectContainsUnit(gg_rct_EasternDungeons, GetFilterUnit())) and not (RectContainsUnit(gg_rct_BlackMountain, GetFilterUnit()))) or RectContainsUnit(gg_rct_OutNoVk, GetFilterUnit())
end
---@return boolean
function InBisles()
	return not (RectContainsUnit(gg_rct_BrokenIsles, GetFilterUnit()))
end
---@return boolean
function InOutland()
	return not (RectContainsUnit(gg_rct_Outland, GetFilterUnit())) or RectContainsUnit(gg_rct_VknotOut, GetFilterUnit())
end
---@return boolean
function InArgus()
	return not (RectContainsUnit(gg_rct_Argus, GetFilterUnit()))
end
---@return boolean
function InPandaria()
	return not (RectContainsUnit(gg_rct_Pandaria, GetFilterUnit()))
end
--  ????????
---@return boolean
function InAnkirag()
	return not (RectContainsUnit(gg_rct_Ankirag, GetFilterUnit()))
end
---@return boolean
function InAzgel()
	return not (RectContainsUnit(gg_rct_Azgel, GetFilterUnit()))
end
---@return boolean
function InBlackRock()
	return not (RectContainsUnit(gg_rct_BlackMountain, GetFilterUnit()))
end
---@return boolean
function InOrgrimmar()
	return not (RectContainsUnit(gg_rct_Orgrimmar, GetFilterUnit()))
end
---@return boolean
function InDeadMines()
	return not (RectContainsUnit(gg_rct_DeadMines, GetFilterUnit()))
end
---@return boolean
function InStalgorn()
	return not (RectContainsUnit(gg_rct_Stalgorn, GetFilterUnit()))
end
---@return boolean
function InUldum()
	return not (RectContainsUnit(gg_rct_Uldum, GetFilterUnit()))
end
---@return boolean
function InMaradon()
	return not (RectContainsUnit(gg_rct_Maradon, GetFilterUnit()))
end
---@return boolean
function InUndercity()
	return not (RectContainsUnit(gg_rct_Undercity, GetFilterUnit()))
end
--  ???????? ??????
---@return boolean
function InDalaran()
	return not (RectContainsUnit(gg_rct_KillDalaran, GetFilterUnit()))
end
---@return boolean
function InNaxramas()
	return not (RectContainsUnit(gg_rct_Naxramas, GetFilterUnit()))
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