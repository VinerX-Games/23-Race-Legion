-- *  Global Variables
-- 
-- ***************************************************************************
---@return nothing
function InitGlobals()
	local i = 0
	i = 0
	while true do
		if (i > 25) then break end
		udg_Income[i] = 0
		i = i + 1
	end
	
	udg_IncomeTimerFirst = CreateTimer()
	udg_IncomeTimerSecond = CreateTimer()
	udg_LocalOtrad = CreateGroup()
	i = 0
	while true do
		if (i > 1) then break end
		udg_LocalReal[i] = 0
		i = i + 1
	end
	
	udg_Flagmans = CreateGroup()
	i = 0
	while true do
		if (i > 1) then break end
		udg_FlagmanEst[i] = false
		i = i + 1
	end
	
	udg_BuildEffectGroup = CreateGroup()
	i = 0
	while true do
		if (i > 1) then break end
		udg_T2[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_T3[i] = CreateGroup()
		i = i + 1
	end
	
	udg_NaimEffectGroup = CreateGroup()
	udg_Nalog = 0
	udg_Stoimost = 0
	udg_LocalInteger = 0
	udg_Price = 0
	udg_GoldCost = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_GlobalGroups[i] = CreateGroup()
		i = i + 1
	end
	
	udg_ZahvatBuildings = CreateGroup()
	udg_SilitidsLichinki = CreateGroup()
	i = 0
	while true do
		if (i > 25) then break end
		udg_PlayerScoreArmy[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_BuildedSctructure[i] = CreateGroup()
		i = i + 1
	end
	
	udg_wawt = 0
	udg_Kokon = CreateGroup()
	i = 0
	while true do
		if (i > 3) then break end
		udg_SpawnLichinok[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Kol_voUnitod = 0
	udg_StolicaGroups = CreateGroup()
	i = 0
	while true do
		if (i > 25) then break end
		udg_Vassals[i] = CreateForce()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 15) then break end
		udg_TunnelGroup[i] = CreateGroup()
		i = i + 1
	end
	
	udg_playersingame = 0
	i = 0
	while true do
		if (i > 24) then break end
		udg_numberofforces[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 24) then break end
		udg_forces[i] = CreateForce()
		i = i + 1
	end
	
	udg_Timer = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_peasants[i] = 0
		i = i + 1
	end
	
	udg_AllPlayers = CreateForce()
	udg_Skin = "e01J"
	i = 0
	while true do
		if (i > 1) then break end
		udg_Dm[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Drain_Interval[i] = 0
		i = i + 1
	end
	
	udg_z = 0
	udg_Drain_Life_Max = 0
	udg_i2 = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Drain_Value[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Drain_Range[i] = 0
		i = i + 1
	end
	
	udg_y2 = 0
	udg_x2 = 0
	udg_y = 0
	udg_x = 0
	udg_i = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Drain_Targets[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Drain_Max = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_SSfacing[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_SS[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_SSdamage[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_SSeffect[i] = ""
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_SSgroup[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_SSinteger[i] = 0
		i = i + 1
	end
	
	udg_TempGroup = CreateGroup()
	udg_LocalOtrad2 = CreateGroup()
	udg_AllPlayers2 = CreateForce()
	udg_LocalForce = CreateForce()
	udg_LocalText2 = ""
	udg_SilitidTimer = CreateTimer()
	udg_LocalReal2 = 0
	udg_ChargeTimer = CreateTimer()
	udg_Inc = 0
	udg_l = 0
	i = 0
	while true do
		if (i > 24) then break end
		udg_PlayerTableNumber[i] = 0
		i = i + 1
	end
	
	udg_LocalOtrad3 = CreateGroup()
	udg_PlayersCount = 0
	i = 0
	while true do
		if (i > 25) then break end
		udg_UnitsCount[i] = 0
		i = i + 1
	end
	
	udg_Portal_INDEX_CASTER = 0
	udg_Portal_INDEX_TARGET = 0
	udg_Portal_INDEX_TRAVELLER = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_ConfigIndex[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_range[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_delay[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_missileSpeed[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_missileHeight[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_active[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_activeFX[i] = ""
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_departureFX[i] = ""
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_arrivalFX[i] = ""
		i = i + 1
	end
	
	udg_Portal_group = CreateGroup()
	udg_Portal_teleMissiles = CreateGroup()
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_preventAllies[i] = false
		i = i + 1
	end
	
	udg_UDex = 0
	udg_UDexRecycle = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_UDexNext[i] = 0
		i = i + 1
	end
	
	udg_UDexGen = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_UDexPrev[i] = 0
		i = i + 1
	end
	
	udg_UnitIndexEvent = 0
	udg_UnitIndexerEnabled = false
	udg_UDexWasted = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_isTeleporting[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_missileTargetable[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Portal_missileUseOwnMovement[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 20) then break end
		udg_Continents[i] = 0
		i = i + 1
	end
	
	udg_LobbyTime = CreateTimer()
	udg_GameMode = 1
	udg_Total_hero = 0
	udg_Random_Hero = 0
	udg_Players_hero = CreateForce()
	udg_SET_TimerTime = 25
	udg_SET_VISIBLE_MODE = 0
	i = 0
	while true do
		if (i > 28) then break end
		udg_F_Group[i] = CreateGroup()
		i = i + 1
	end
	
	udg_LocalInteger2 = 0
	udg_LocalInteger3 = 0
	i = 0
	while true do
		if (i > 24) then break end
		udg_Tier[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 5) then break end
		udg_ElemCount[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 24) then break end
		udg_TierLevel[i] = 1
		i = i + 1
	end
	
	udg_NewChargeTimer = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_TechResearched[i] = 0
		i = i + 1
	end
	
	udg_MAX_TECH_RESEARCHES = 2
	i = 0
	while true do
		if (i > 25) then break end
		udg_AiControl[i] = false
		i = i + 1
	end
	
	udg_Bots = CreateForce()
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_units[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_builders[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_buildings[i] = CreateGroup()
		i = i + 1
	end
	ProbeLogWrite("[AI] Ai_buildings groups created for 0..25")
	
	udg_TimerSmall = CreateTimer()
	udg_TimerSmall2 = CreateTimer()
	udg_TimerSmall3 = CreateTimer()
	udg_AiTimerStrateg = CreateTimer()
	udg_Octhet = false
	udg_CityNearWater = CreateGroup()
	udg_LocalInteger4 = 0
	udg_LocalInteger5 = 0
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_buildersT[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_army[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_harvest[i] = CreateGroup()
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_Ai_navy[i] = CreateGroup()
		i = i + 1
	end
	
	udg_TimerToChangeAi = CreateTimer()
	i = 0
	while true do
		if (i > 25) then break end
		udg_HeroFirstYes[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_HordeLandPrice[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_MainPrice[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_HordeElitePrice[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_HordeNavyPrice[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_HordeMagicPrice[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 25) then break end
		udg_HordeTechPrice[i] = 0
		i = i + 1
	end
	
	udg_FacelessLumberBuildings = CreateGroup()
	udg_LoadedGroup = CreateGroup()
	udg_TransportingGroup = CreateGroup()
	udg_TransportingIncrement = 0
	udg_TransportingMin = 0
	i = 0
	while true do
		if (i > 8000) then break end
		udg_LoadedGroupArray[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Logika = false
	i = 0
	while true do
		if (i > 1) then break end
		udg_HisloA[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Ygol[i] = 0
		i = i + 1
	end
	
	udg_Timer_Copy = CreateTimer()
	udg_LogikaCast = false
	udg_Group = CreateGroup()
	i = 0
	while true do
		if (i > 1) then break end
		udg_Dalnost_R_Glaz[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Group_R_Glaz[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Timer_R_Glaz = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_S4et_R_Glaz[i] = 0
		i = i + 1
	end
	
	udg_Cikl_R_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Antibag_R_Glaz[i] = 0
		i = i + 1
	end
	
	udg_MUI_R_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Logika_R_Glaz[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Dalnost_E_Glaz[i] = 0
		i = i + 1
	end
	
	udg_Timer_E_Glaz = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_Group_E_Glaz[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Cikl_E_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Antibag_E_Glaz[i] = 0
		i = i + 1
	end
	
	udg_MUI_E_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Logika_E_Glaz[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_S4et_W2_Glaz[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Logika_W2_Glaz[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Group_W_Glaz[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Timer_W_Glaz = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_S4et_W_Glaz[i] = 0
		i = i + 1
	end
	
	udg_Cikl_W_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Antibag_W_Glaz[i] = 0
		i = i + 1
	end
	
	udg_MUI_W_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Logika_W_Glaz[i] = false
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Wait_Q_Glaz[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Range_Q_Glaz[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_S4et_Timer_Q_Glaz[i] = 0
		i = i + 1
	end
	
	i = 0
	while true do
		if (i > 1) then break end
		udg_Group_Q_Glaz[i] = CreateGroup()
		i = i + 1
	end
	
	udg_Timer_Q_Glaz = CreateTimer()
	i = 0
	while true do
		if (i > 1) then break end
		udg_Antibag_Q_Glaz[i] = 0
		i = i + 1
	end
	
	udg_Cikl_Q_Glaz = 0
	udg_MUI_Q_Glaz = 0
	i = 0
	while true do
		if (i > 1) then break end
		udg_Logika_Q_Glaz[i] = false
		i = i + 1
	end
	
	udg_FastTest = false
	udg_DalaranKills = CreateGroup()
	udg_NaxramasKills = CreateGroup()
	udg_AllLords = CreateGroup()
	udg_MellLord = CreateGroup()
	udg_TimerToCont = CreateTimer()
end
---@param hash hashtable
---@param parent integer
---@param child integer
---@param value integer|nil
---@return nothing
function SaveIntegerIfPresent(hash, parent, child, value)
    if value ~= nil then
        SaveInteger(hash, parent, child, value)
    end
end
-- ***************************************************************************
-- 
