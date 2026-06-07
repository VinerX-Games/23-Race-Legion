-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/init.lua — Unit indexer, start locations, initial setup
-- ============================================================

-- ============================================================
-- Unit Indexer (Bribe's UDex)
-- ============================================================

_G.udg_UnitIndexEvent = 0

function IndexUnit()
    local pdex = G.udg_UDex

    if G.udg_UnitIndexerEnabled then
        -- Generate a unique integer index for this unit
        if G.udg_UDexRecycle == 0 then
            G.udg_UDex = G.udg_UDexGen + 1
            G.udg_UDexGen = G.udg_UDex
        else
            G.udg_UDex = G.udg_UDexRecycle
            G.udg_UDexRecycle = G.udg_UDexNext[G.udg_UDex]
        end

        -- Link index to unit, unit to index
        G.udg_UDexUnits[G.udg_UDex] = GetFilterUnit()
        SetUnitUserData(G.udg_UDexUnits[G.udg_UDex], G.udg_UDex)

        -- Use a doubly-linked list to store all active indexes
        G.udg_UDexPrev[G.udg_UDexNext[0]] = G.udg_UDex
        G.udg_UDexNext[G.udg_UDex] = G.udg_UDexNext[0]
        G.udg_UDexNext[0] = G.udg_UDex

        -- Fire index event for UDex
        udg_UnitIndexEvent = 0.0
        udg_UnitIndexEvent = 1.0
        udg_UnitIndexEvent = 0.0
        G.udg_UDex = pdex
    end
    return false
end

function IndexNewUnit()
    local pdex = G.udg_UDex
    local ndex

    -- Recycle indices of units no longer in-play every 15 units created
    G.udg_UDexWasted = G.udg_UDexWasted + 1
    if G.udg_UDexWasted == 15 then
        G.udg_UDexWasted = 0
        G.udg_UDex = G.udg_UDexNext[0]
        while G.udg_UDex ~= 0 do
            if GetUnitUserData(G.udg_UDexUnits[G.udg_UDex]) == 0 then
                -- Remove index from linked list
                ndex = G.udg_UDexNext[G.udg_UDex]
                G.udg_UDexNext[G.udg_UDexPrev[G.udg_UDex]] = ndex
                G.udg_UDexPrev[ndex] = G.udg_UDexPrev[G.udg_UDex]
                G.udg_UDexPrev[G.udg_UDex] = 0

                -- Fire deindex event for UDex
                udg_UnitIndexEvent = 2.0
                udg_UnitIndexEvent = 0.0

                -- Recycle the index for later use
                G.udg_UDexUnits[G.udg_UDex] = nil
                G.udg_UDexNext[G.udg_UDex] = G.udg_UDexRecycle
                G.udg_UDexRecycle = G.udg_UDex
                G.udg_UDex = ndex
            else
                G.udg_UDex = G.udg_UDexNext[G.udg_UDex]
            end
        end
        G.udg_UDex = pdex
    end

    -- Handle the entering unit
    if GetUnitUserData(GetFilterUnit()) == 0 then
        IndexUnit()
    end
    return false
end

function InitializeUnitIndexer()
    G.udg_UnitIndexerEnabled = true

    local re = CreateRegion()
    local r = GetWorldBounds()
    RegionAddRect(re, r)

    local enterTrigger = CreateTrigger()
    TriggerRegisterEnterRegion(enterTrigger, re, Filter(IndexNewUnit))

    RemoveRect(r)

    for i = 0, 15 do
        GroupEnumUnitsOfPlayer(bj_lastCreatedGroup, Player(i), Filter(IndexUnit))
    end

    -- This is the "Unit Indexer Initialized" event
    udg_UnitIndexEvent = 3.0
    udg_UnitIndexEvent = 0.0
end

-- ============================================================
-- Start Locations (from LIBRARY_RandomLocs)
-- ============================================================

G.StartLoc = {}
G.StartLocCount = 0

function isStartPosition()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('h0O1')
end

function SetStartLocations()
    local StartLocations = CreateGroup()
    local b = Filter(isStartPosition)
    local u

    GroupEnumUnitsInRect(StartLocations, bj_mapInitialPlayableArea, b)

    repeat
        u = FirstOfGroup(StartLocations)
        if u == nil then break end

        G.StartLoc[G.StartLocCount] = GetUnitLoc(u)
        G.StartLocCount = G.StartLocCount + 1

        GroupRemoveUnit(StartLocations, u)
        RemoveUnit(u)
    until false

    DestroyGroup(StartLocations)
    DestroyFilter(b)
end

function RandomLoc()
    return G.StartLoc[GetRandomInt(0, G.StartLocCount - 1)]
end

-- ============================================================
-- Army Bonus Units (from LIBRARY_ArmyBonus)
-- ============================================================

G.ArmyExpBonus = {}
G.ArmyExp = {}

function CreateArmyBonusUnit(p)
    local pi = GetPlayerId(p)
    if G.ArmyExpBonus[pi] == nil then
        G.ArmyExpBonus[pi] = CreateUnit(p, FourCC('arbo'), 0, 0, 0.0)
        UnitAddAbility(G.ArmyExpBonus[pi], FourCC('arb1'))
        UnitAddAbility(G.ArmyExpBonus[pi], FourCC('arb0'))
    end
end

-- ============================================================
-- AI Turn Off (from LIBRARY_AI)
-- ============================================================

function turnOffAi(pi)
    if not G.udg_AiControl[pi] then return end
    G.udg_AiControl[pi] = false
    ForceRemovePlayer(G.udg_Bots, Player(pi))
end

-- ============================================================
-- InitGlobals - Sets initial values for all GUI globals
-- ============================================================

function InitGlobals()
    local i

    G.udg_UDex = 0
    G.udg_UDexRecycle = 0
    for i = 0, 8190 do G.udg_UDexNext[i] = 0 end
    G.udg_UDexGen = 0
    for i = 0, 8190 do G.udg_UDexPrev[i] = 0 end
    G.udg_UDexWasted = 0
    G.udg_UnitIndexerEnabled = false
    G.udg_UnitIndexEvent = 0

    G.udg_GameMode = 0
    G.udg_SET_TimerTime = 25
    G.udg_SET_VISIBLE_MODE = 0
    G.IncomeMod = 1.0
    G.Tax = 0.15
    G.DisOn = false
    G.PercentWin = 65
    G.DipMode = 2

    -- AI defaults
    G.AiMoney = 7
    G.AiMass = 5
    G.AiRepeat = 5
    G.AiRadius = 6
    G.AiLimit = 150

    -- Initialize groups
    G.udg_StolicaGroups = CreateGroup()
    G.udg_ZahvatBuildings = CreateGroup()
    G.udg_AllPlayers = CreateForce()
    G.udg_AllPlayers2 = CreateForce()
    G.udg_Bots = CreateForce()
    G.udg_BotsActive = CreateForce()
    G.udg_BotsActiveB = CreateForce()
    G.udg_CityNearWater = CreateGroup()
    G.udg_Flagmans = CreateGroup()

    -- Initialize timers
    G.udg_Timer = CreateTimer()
    G.udg_TimerSmall = CreateTimer()
    G.udg_TimerSmall2 = CreateTimer()
    G.udg_TimerSmall3 = CreateTimer()
    G.udg_TimerSmall4 = CreateTimer()
    G.udg_PlayerGet1 = CreateTimer()
    G.udg_PlayerGet2 = CreateTimer()
    G.udg_PlayerGet4 = CreateTimer()
    G.udg_AiTimerStrateg = CreateTimer()
    G.udg_TimerToChangeAi = CreateTimer()
    G.udg_SilitidTimer = CreateTimer()
    G.udg_IncomeTimerFirst = CreateTimer()
    G.udg_IncomeTimerSecond = CreateTimer()
    G.udg_LobbyTime = CreateTimer()
    G.udg_NewChargeTimer = CreateTimer()
    G.udg_ChargeTimer = CreateTimer()
    G.udg_Timer_Copy = CreateTimer()
    G.udg_Timer_R_Glaz = CreateTimer()
    G.udg_Timer_E_Glaz = CreateTimer()
    G.udg_Timer_W_Glaz = CreateTimer()
    G.udg_Timer_Q_Glaz = CreateTimer()

    -- Dynamic groups initialization (per player)
    for i = 0, 23 do
        G.udg_Ai_units[i] = CreateGroup()
        G.udg_Ai_builders[i] = CreateGroup()
        G.udg_Ai_buildings[i] = CreateGroup()
        G.udg_Ai_buildersT[i] = CreateGroup()
        G.udg_Ai_army[i] = CreateGroup()
        G.udg_Ai_harvest[i] = CreateGroup()
        G.udg_Ai_navy[i] = CreateGroup()
        G.udg_BuildedSctructure[i] = CreateGroup()
        G.AiCapitalGuard[i] = CreateGroup()
        G.AiCapitalBuildigs[i] = CreateGroup()
        G.AiUnitsToPort[i] = CreateGroup()
    end
end

-- ============================================================
-- JassHelper struct initializer (no-op in Lua)
-- ============================================================

function jasshelper__initstructs100223406()
    -- vJASS struct initialization - not needed in Lua
    -- StackTemplate and SanctifiedEnchantment structs are manually handled
end
