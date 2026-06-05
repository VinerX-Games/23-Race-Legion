-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/stolica.lua — Capital, Feodalism, Domination, Diplomacy
-- ============================================================
-- Sources: UpgradeStolica, MakeStolica, StolicaTime, StolicaDead,
--          StolicaAttacked, StolicaKill, FeodalDead, FeodalDead2,
--          DoNotAttackSenior, DoNotAttackSenior2, DominationButton,
--          Domination start, Diplomacy mode, CityCountCheck
-- ============================================================

local ALLIANCE_UNALLIED        = bj_ALLIANCE_UNALLIED
local ALLIANCE_ALLIED_VISION   = bj_ALLIANCE_ALLIED_VISION
local ALLIANCE_ALLIED_UNITS    = bj_ALLIANCE_ALLIED_UNITS
local ALLIANCE_ALLIED_ADVUNITS = bj_ALLIANCE_ALLIED_ADVUNITS

-- ============================================================
-- Helper: MathRound for Lua (JASS MathRound = R2I(x+0.5))
-- ============================================================

local function MathRound(x)
    return math.floor(x + 0.5)
end

-- ============================================================
-- Helper: SetUnitLifePercentBJ replacement (Lua)
-- ============================================================

local function SetUnitLifePercentBJ(u, percent)
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_MAX_LIFE) * percent / 100.0)
end

-- ============================================================
-- UpgradeStolica — When a capital finishes upgrading
-- ============================================================

function Trig_UpgradeStolica_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_StolicaGroups)
end

function Trig_UpgradeStolica_Actions()
    BlzSetUnitArmor(GetTriggerUnit(), 30.0)
    BlzSetUnitMaxHP(GetTriggerUnit(), 10000)
    UnitAddAbility(GetTriggerUnit(), FourCC('A0I6'))
    BlzSetUnitStringField(GetTriggerUnit(), UNIT_SF_NAME, "|cffd45e19Столица:|r " .. GetUnitName(GetTriggerUnit()))
    UnitAddAbility(GetTriggerUnit(), FourCC('A145'))
end

function InitTrig_UpgradeStolica()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(trig, Condition(Trig_UpgradeStolica_Conditions))
    TriggerAddAction(trig, Trig_UpgradeStolica_Actions)
    G.gg_trg_UpgradeStolica = trig
end

-- ============================================================
-- MakeStolica — Create a capital from a building
-- ============================================================

function HaveCapitalAbility()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0IQ')) ~= 0 and UnitAlive(GetFilterUnit())
end

function Capitals()
    return IsUnitInGroup(GetFilterUnit(), G.udg_StolicaGroups)
end

function unitShareVisionAll(u, flag)
    for i = 0, 23 do
        UnitShareVision(u, Player(i), flag)
    end
end

function checkMovingCity(u)
    local x = GetUnitX(u)
    local y = GetUnitY(u)

    if RectContainsCoords(gg_rct_Naxramas, x, y) then
        unitShareVisionAll(gg_unit_e00D_0080, true)
    elseif RectContainsCoords(gg_rct_KillDalaran, x, y) then
        unitShareVisionAll(gg_unit_e00C_0590, true)
    elseif RectContainsCoords(gg_rct_TurtleIsland, x, y) then
        unitShareVisionAll(gg_unit_e00E_0085, true)
    end
end

function MakeCapital(capital)
    UnitSetConstructionProgress(capital, 100)
    BlzSetUnitMaxHP(capital, 10000)
    SetUnitState(capital, UNIT_STATE_LIFE, 10000.0)
    BlzSetUnitRealField(capital, UNIT_RF_SIGHT_RADIUS, 750.0)
    BlzSetUnitArmor(capital, 30.0)
    UnitAddAbility(capital, FourCC('A0I6'))
    UnitAddAbility(capital, FourCC('A145'))
    BlzSetUnitStringField(capital, UNIT_SF_NAME, "|cffd45e19Столица:|r " .. GetUnitName(capital))
    GroupAddUnit(G.udg_StolicaGroups, capital)
    TriggerRegisterUnitEvent(G.gg_trg_StolicaAttacked, capital, EVENT_UNIT_ATTACKED)
    unitShareVisionAll(capital, true)
    checkMovingCity(capital)
    G.playerCapital[GetPlayerId(GetOwningPlayer(capital))] = capital
end

function MakeFakeCapital(p)
    local pi = GetPlayerId(p)
    GroupEnumUnitsOfPlayer(G.gGroup, p, Condition(HaveCapitalAbility))
    local u = BlzGroupUnitAt(G.gGroup, GetRandomInt(0, BlzGroupGetSize(G.gGroup) - 1))
    G.playerCapital[pi] = u
    aiCapitalEnter(u)
    GroupClear(G.gGroup)
end

function Trig_MakeStolica_Conditions()
    return GetSpellAbilityId() == FourCC('A0IQ')
end

function Trig_MakeStolica_Actions()
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A0IQ'), false)
    MakeCapital(GetTriggerUnit())
end

function InitTrig_MakeStolica()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_MakeStolica_Conditions))
    TriggerAddAction(trig, Trig_MakeStolica_Actions)
    G.gg_trg_MakeStolica = trig
end

-- ============================================================
-- StolicaTime — Auto-create capitals at IncomeTimerFirst
-- ============================================================

function CheckAndCreateCapital(p)
    local u
    local pi = GetPlayerId(p)
    local g = CreateGroup()

    GroupEnumUnitsOfPlayer(g, p, Condition(Capitals))
    if BlzGroupGetSize(g) == 0 then -- Столицы нет
        GroupClear(g)
        G.Counter = 0
        GroupEnumUnitsOfPlayer(g, p, Condition(HaveCapitalAbility))

        if BlzGroupGetSize(g) > 0 then
            u = BlzGroupUnitAt(g, GetRandomInt(0, BlzGroupGetSize(g) - 1))
            SetPlayerAbilityAvailable(p, FourCC('A0IQ'), false)
            MakeCapital(u)
            DisplayTimedTextToForce(G.udg_AllPlayers, 5, GetPlayerName(p) .. " - |cffffff00почти проиграл|r|r, его |cffd45e19столица|r не не была построена ко времени, а потому была установлена автоматически.")
        else
            if GetPlayerSlotState(p) == PLAYER_SLOT_STATE_PLAYING then
                DisplayTimedTextToForce(G.udg_AllPlayers, 5, GetPlayerName(p) .. " - |cffff0000проиграл|r, его |cffd45e19столица |r не построена ко времени. :(")
            end
            ClearPlayer(p)
        end
    end

    DestroyGroup(g)
end

function AllPlayersCapital()
    CheckAndCreateCapital(GetEnumPlayer())
end

function Trig_StolicaTime_Actions()
    ForForce(G.udg_AllPlayers, AllPlayersCapital)
    ForForce(G.udg_Bots, AllPlayersCapital)
end

function InitTrig_StolicaTime()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterTimerExpireEvent(trig, G.udg_IncomeTimerFirst)
    TriggerAddAction(trig, Trig_StolicaTime_Actions)
    G.gg_trg_StolicaTime = trig
end

-- ============================================================
-- StolicaDead — Capital death handling
-- ============================================================

function Trig_StolicaDead_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_StolicaGroups)
end

function Trig_StolicaDead_Actions()
    local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A0IQ'), true)
    DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. " - |cffff0000проиграл|r, его |cffd45e19столица |rуничтожена.")
    ClearPlayer(Player(pi))
    AiLimitsSet()
end

function InitTrig_StolicaDead()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(trig, Condition(Trig_StolicaDead_Conditions))
    TriggerAddAction(trig, Trig_StolicaDead_Actions)
    G.gg_trg_StolicaDead = trig
end

-- ============================================================
-- StolicaAttacked — Warning when capital is attacked (90s timer)
-- ============================================================

function CapTimeDel()
    local t = GetExpiredTimer()
    local pi = G.TimerData[t] -- stored player id via Lua table
    G.cap_time[pi] = true
    G.TimerData[t] = nil
    DestroyTimer(t)
end

function Trig_StolicaAttacked_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_StolicaGroups)
end

function Trig_StolicaAttacked_Actions()
    local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if G.cap_time[pi] then
        local t = CreateTimer()
        DisplayTextToPlayer(Player(pi), 0, 0, "TRIGSTR_27508")
        G.cap_time[pi] = false
        G.TimerData[t] = pi
        TimerStart(t, 90, false, CapTimeDel)
    end
end

function InitTrig_StolicaAttacked()
    local trig = CreateTrigger()
    -- Events registered per-unit via MakeCapital
    TriggerAddCondition(trig, Condition(Trig_StolicaAttacked_Conditions))
    TriggerAddAction(trig, Trig_StolicaAttacked_Actions)
    G.gg_trg_StolicaAttacked = trig
end

-- ============================================================
-- StolicaKill — Empty trigger, vassal comment
-- ============================================================

function Trig_StolicaKill_Actions()
    -- Обнуляю вассалов самоубийцы. Вы свободны!
end

function InitTrig_StolicaKill()
    local trig = CreateTrigger()
    TriggerAddAction(trig, Trig_StolicaKill_Actions)
    G.gg_trg_StolicaKill = trig
end

-- ============================================================
-- MOD stolica Start (GameMode == 1) — Classic stolica mode
-- ============================================================

function Trig_MOD_stolica_Start_Conditions()
    return G.udg_GameMode == 1
end

function Trig_MOD_stolica_Start_Func005A()
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A0IQ'), true)
end

function Trig_MOD_stolica_Start_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_19372")
    ForForce(G.udg_AllPlayers, Trig_MOD_stolica_Start_Func005A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaDead)
    EnableTrigger(G.gg_trg_StolicaTime)
    TriggerExecute(G.gg_trg_RebebmerToBuild)
end

function InitTrig_MOD_stolica_Start()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-mod st", true)
    TriggerRegisterTimerExpireEvent(trig, G.udg_LobbyTime)
    TriggerAddCondition(trig, Condition(Trig_MOD_stolica_Start_Conditions))
    TriggerAddAction(trig, Trig_MOD_stolica_Start_Actions)
    G.gg_trg_MOD_stolica_Start = trig
end

-- ============================================================
-- MOD stolica Start Copy (GameMode == 5) — Combo mode
-- ============================================================

function Trig_MOD_stolica_Start_Copy_Conditions()
    return G.udg_GameMode == 5
end

function Trig_MOD_stolica_Start_Copy_Func005A()
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A0IQ'), true)
end

function Trig_MOD_stolica_Start_Copy_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_5726")
    ForForce(G.udg_AllPlayers, Trig_MOD_stolica_Start_Copy_Func005A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaDead)
    EnableTrigger(G.gg_trg_StolicaTime)
    TriggerExecute(G.gg_trg_RebebmerToBuild)
end

function InitTrig_MOD_stolica_Start_Copy()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-mod st", true)
    TriggerRegisterTimerExpireEvent(trig, G.udg_LobbyTime)
    TriggerAddCondition(trig, Condition(Trig_MOD_stolica_Start_Copy_Conditions))
    TriggerAddAction(trig, Trig_MOD_stolica_Start_Copy_Actions)
    G.gg_trg_MOD_stolica_Start_Copy = trig
end

-- ============================================================
-- MOD feoda O Start (GameMode == 2) — Feodalism mode
-- ============================================================

function Trig_MOD_feoda_O_Start_Conditions()
    return G.udg_GameMode == 2
end

function Trig_MOD_feoda_O_Start_Func006A()
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A0IQ'), true)
end

function Trig_MOD_feoda_O_Start_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_19378")
    SetForceAllianceStateBJ(G.udg_AllPlayers, G.udg_AllPlayers, bj_ALLIANCE_UNALLIED)
    ForForce(G.udg_AllPlayers, Trig_MOD_feoda_O_Start_Func006A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaTime)
    EnableTrigger(G.gg_trg_FeodalDead2)
    EnableTrigger(G.gg_trg_DoNotAttackSenior2)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, true)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, true)
end

function InitTrig_MOD_feoda_O_Start()
    local trig = CreateTrigger()
    TriggerRegisterTimerExpireEvent(trig, G.udg_LobbyTime)
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-mod feod", true)
    TriggerAddCondition(trig, Condition(Trig_MOD_feoda_O_Start_Conditions))
    TriggerAddAction(trig, Trig_MOD_feoda_O_Start_Actions)
    G.gg_trg_MOD_feoda_O_Start = trig
end

-- ============================================================
-- FeodalDead (old system) — Capital attacked below 15% HP
-- Uses scratch globals _iA/_iB for BJ loop indexer compatibility
-- ============================================================

function Trig_FeodalDead_Conditions()
    if not IsUnitInGroup(GetTriggerUnit(), G.udg_StolicaGroups) then
        return false
    end
    if GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) / GetUnitState(GetTriggerUnit(), UNIT_STATE_MAX_LIFE) * 100 > 15.0 then
        return false
    end
    return true
end

-- Func003C: checks if trigger unit's owner is NOT in the current bj_forLoopB vassal force
function Trig_FeodalDead_Func004Func002Func001Func010Func001Func003C()
    if IsPlayerInForce(GetOwningPlayer(GetTriggerUnit()), G.udg_Vassals[G._fd_iB]) then
        return false
    end
    return true
end

-- Func010A: transfer vassals of trigger unit owner to player(iA)
function Trig_FeodalDead_Func004Func002Func001Func010A()
    for G._fd_iB = 1, 24 do
        SetPlayerAllianceStateBJ(GetEnumPlayer(), Player(G._fd_iB - 1), bj_ALLIANCE_UNALLIED)
        SetPlayerAllianceStateBJ(Player(G._fd_iB - 1), GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
        if Trig_FeodalDead_Func004Func002Func001Func010Func001Func003C() then
            ForceRemovePlayerSimple(GetOwningPlayer(GetTriggerUnit()), G.udg_Vassals[G._fd_iB])
        end
    end
    ForceAddPlayerSimple(GetEnumPlayer(), G.udg_Vassals[G._fd_iA])
    SetPlayerAllianceStateBJ(GetEnumPlayer(), GetOwningPlayer(GetAttacker()), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(GetEnumPlayer(), Player(G._fd_iA - 1), bj_ALLIANCE_ALLIED_UNITS)
    SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(Player(G._fd_iA - 1), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
    DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. " - стал вассалом игрока " .. GetPlayerName(Player(G._fd_iA - 1)))
end

-- Func001C: checks if attacker is NOT in the current bj_forLoopA vassal force
function Trig_FeodalDead_Func004Func002Func001C()
    if IsPlayerInForce(GetOwningPlayer(GetAttacker()), G.udg_Vassals[G._fd_iA]) then
        return false
    end
    return true
end

-- Func011A: when senior captures - force vassalization on the defender's vassals
function Trig_FeodalDead_Func004Func011A()
    DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. " - стал вассалом игрока " .. GetPlayerName(GetOwningPlayer(GetAttacker())))
    ForceAddPlayerSimple(GetEnumPlayer(), G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetAttacker())) + 1])
    for G._fd_iB = 1, 24 do
        SetPlayerAllianceStateBJ(GetEnumPlayer(), Player(G._fd_iB - 1), bj_ALLIANCE_UNALLIED)
        SetPlayerAllianceStateBJ(Player(G._fd_iB - 1), GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
    end
end

-- Func017Func001C: check if enumeration unit is in ZahvatBuildings
function Trig_FeodalDead_Func004Func017Func001C()
    return IsUnitInGroup(GetEnumUnit(), G.udg_ZahvatBuildings)
end

-- Func017A: kill or transfer units of suicide player
function Trig_FeodalDead_Func004Func017A()
    if Trig_FeodalDead_Func004Func017Func001C() then
        SetUnitOwner(GetEnumUnit(), Player(PLAYER_NEUTRAL_AGGRESSIVE), true)
    else
        KillUnit(GetEnumUnit())
        RemoveUnit(GetEnumUnit())
    end
end

-- Func020A: free vassals from suicide player
function Trig_FeodalDead_Func004Func020A()
    DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. " освободился от игрока " .. GetPlayerName(GetOwningPlayer(GetTriggerUnit())))
    for G._fd_iA = 1, 24 do
        SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), Player(G._fd_iA - 1), bj_ALLIANCE_UNALLIED)
        SetPlayerAllianceStateBJ(GetEnumPlayer(), Player(G._fd_iA - 1), bj_ALLIANCE_UNALLIED)
        SetPlayerAllianceStateBJ(Player(G._fd_iA - 1), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_UNALLIED)
    end
end

-- Func004C: checks if it's a suicide (attacker == owner)
function Trig_FeodalDead_Func004C()
    return GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetAttacker())
end

function Trig_FeodalDead_Actions()
    SetUnitLifePercentBJ(GetTriggerUnit(), 100)
    SetUnitInvulnerable(GetTriggerUnit(), true)
    SetUnitInvulnerable(GetTriggerUnit(), false)
    if Trig_FeodalDead_Func004C() then
        -- Триггер для самоубийцы
        DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. "|cffff0000 - самоубился! |rЗачем?)")
        ForGroupBJ(GetUnitsOfPlayerAll(GetOwningPlayer(GetTriggerUnit())), Trig_FeodalDead_Func004Func017A)
        SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A0IQ'), true)
        -- Обнуляю вассалов самоубийцы. Вы свободны!
        ForForce(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1], Trig_FeodalDead_Func004Func020A)
        ForceClear(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1])
    else
        -- --------------------------------------------------------------------   Васссал кого-то захватил
        for G._fd_iA = 1, 24 do
            if Trig_FeodalDead_Func004Func002Func001C() then
                for G._fd_iB = 1, 24 do
                    SetPlayerAllianceStateBJ(GetTriggerPlayer(), Player(G._fd_iB - 1), bj_ALLIANCE_UNALLIED)
                    SetPlayerAllianceStateBJ(Player(G._fd_iB - 1), GetTriggerPlayer(), bj_ALLIANCE_UNALLIED)
                end
                -- Есть сеньор
                -- Вассализация хозяина столицы
                DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. " - стал вассалом игрока " .. GetPlayerName(Player(G._fd_iA - 1)))
                ForceAddPlayerSimple(GetOwningPlayer(GetTriggerUnit()), G.udg_Vassals[G._fd_iA])
                SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), Player(G._fd_iA - 1), bj_ALLIANCE_ALLIED_UNITS)
                SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
                SetPlayerAllianceStateBJ(Player(G._fd_iA - 1), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
                -- Вассализация вассалов хозяина столицы
                ForForce(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1], Trig_FeodalDead_Func004Func002Func001Func010A)
                ForceClear(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1])
                SetForceAllianceStateBJ(G.udg_Vassals[G._fd_iA], G.udg_Vassals[G._fd_iA], bj_ALLIANCE_ALLIED_VISION)
                SetForceAllianceStateBJ(G.udg_Vassals[G._fd_iA], GetForceOfPlayer(GetOwningPlayer(GetAttacker())), bj_ALLIANCE_ALLIED_UNITS)
                return
            end
        end
        -- --------------------------------------------------------------------   Сеньор кого-то захватил
        -- Вассализация хозяина столицы
        for G._fd_iB = 1, 24 do
            SetPlayerAllianceStateBJ(GetTriggerPlayer(), Player(G._fd_iB - 1), bj_ALLIANCE_UNALLIED)
            SetPlayerAllianceStateBJ(Player(G._fd_iB - 1), GetTriggerPlayer(), bj_ALLIANCE_UNALLIED)
        end
        DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. " - стал вассалом игрока " .. GetPlayerName(GetOwningPlayer(GetAttacker())))
        ForceAddPlayerSimple(GetOwningPlayer(GetTriggerUnit()), G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetAttacker())) + 1])
        SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker()), bj_ALLIANCE_ALLIED_UNITS)
        SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
        -- Вассализация вассалов хозяина столицы
        ForForce(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1], Trig_FeodalDead_Func004Func011A)
        SetForceAllianceStateBJ(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetAttacker())) + 1], G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetAttacker())) + 1], bj_ALLIANCE_ALLIED_VISION)
        SetForceAllianceStateBJ(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetAttacker())) + 1], GetForceOfPlayer(GetOwningPlayer(GetAttacker())), bj_ALLIANCE_ALLIED_UNITS)
        ForceClear(G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1])
    end
end

function InitTrig_FeodalDead()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(trig, Condition(Trig_FeodalDead_Conditions))
    TriggerAddAction(trig, Trig_FeodalDead_Actions)
    G.gg_trg_FeodalDead = trig
end

-- ============================================================
-- FeodalDead2 (new system) — Capital attacked, vassalage with Senior/Vassals
-- ============================================================

-- 3 сек неуяза (3 sec invulnerability)
function CapTime()
    local u = G.udg_LocalUnit3
    SetUnitLifePercentBJ(u, 100)
    UnitAddAbility(u, FourCC('Avul'))
    RemoveAbilityTimed(u, FourCC('Avul'), 3)
end

function ClearOldAllies(p)
    local p0 = G.Senior[GetPlayerId(p)]
    ForceRemovePlayer(G.Vassals[GetPlayerId(p0)], p)
    SetPlayerAllianceStateBJ(p, p0, bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(p0, p, bj_ALLIANCE_UNALLIED)
    SetForceAllianceStateBJ(GetForceOfPlayer(p), G.Vassals[GetPlayerId(p0)], bj_ALLIANCE_UNALLIED)
    SetForceAllianceStateBJ(G.Vassals[GetPlayerId(p0)], GetForceOfPlayer(p), bj_ALLIANCE_UNALLIED)
end

function NewAlly(p)
    local p3 = G.Senior[GetPlayerId(p)]
    SetPlayerAllianceStateBJ(p, p3, bj_ALLIANCE_ALLIED_UNITS)
    SetPlayerAllianceStateBJ(p3, p, bj_ALLIANCE_ALLIED_VISION)
    SetForceAllianceStateBJ(GetForceOfPlayer(p), G.Vassals[GetPlayerId(p3)], bj_ALLIANCE_ALLIED_VISION)
    SetForceAllianceStateBJ(G.Vassals[GetPlayerId(p3)], GetForceOfPlayer(p), bj_ALLIANCE_ALLIED_VISION)
end

function Freedom()
    local p = GetEnumPlayer()
    DisplayTextToForce(G.udg_AllPlayers, GetPlayerName(p) .. " - стал свободен")
    ClearOldAllies(p)
end

function ChangeAlly()
    local p0 = GetEnumPlayer()
    local p = G.udg_LocalPlayer

    DisplayTextToForce(G.udg_AllPlayers, GetPlayerName(p0) .. " - игроком захвачен игроком " .. GetPlayerName(p))
    ClearOldAllies(p0)
    G.Senior[GetPlayerId(p0)] = p
    ForceAddPlayer(G.Vassals[GetPlayerId(p)], p0)
    NewAlly(p0)
end

function Trig_FeodalDead2_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_StolicaGroups) and GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) / GetUnitState(GetTriggerUnit(), UNIT_STATE_MAX_LIFE) * 100 <= 15.0
end

function Trig_FeodalDead2_Actions()
    local p = GetOwningPlayer(GetTriggerUnit())
    local pi = GetPlayerId(p)
    local p2 = GetOwningPlayer(GetAttacker())
    local pi2 = GetPlayerId(p2)
    local pi3
    local p3

    -- Случай самоубийцы
    if p == p2 then
        ClearPlayer(p)
        DisplayTextToForce(G.udg_AllPlayers, GetPlayerName(p) .. " - решил уничтожить свою столицу - зачем?")
        ForForce(G.Vassals[pi], Freedom)
        return
    end

    G.udg_LocalUnit3 = GetTriggerUnit()
    CapTime()

    -- Захватил свободный
    if G.Senior[pi2] == nil then
        -- свободного
        DisplayTextToForce(G.udg_AllPlayers, GetPlayerName(p) .. " - игроком захвачен игроком " .. GetPlayerName(p2))
        if G.Senior[pi] == nil then
            G.Senior[pi] = p2
            ForceAddPlayer(G.Vassals[pi2], p)
            NewAlly(p)

            if CountPlayersInForceBJ(G.Vassals[pi]) ~= 0 then
                G.udg_LocalPlayer = p2
                ForForce(G.Vassals[pi], ChangeAlly)
            end
        -- Чужого вассала
        else
            ClearOldAllies(p)
            G.Senior[pi] = p2
            ForceAddPlayer(G.Vassals[pi2], p)
            NewAlly(p)
        end
    -- Захватил чей-то вассал
    else
        p3 = G.Senior[pi2]
        pi3 = GetPlayerId(p3)
        DisplayTextToForce(G.udg_AllPlayers, GetPlayerName(p) .. " - игроком захвачен игроком " .. GetPlayerName(p3))
        -- свободного
        if G.Senior[pi] == nil then
            G.Senior[pi] = p3
            ForceAddPlayer(G.Vassals[pi3], p)
            NewAlly(p)

            if CountPlayersInForceBJ(G.Vassals[pi]) ~= 0 then
                G.udg_LocalPlayer = p3
                ForForce(G.Vassals[pi], ChangeAlly)
            end
        -- Чужого вассала
        else
            ClearOldAllies(p)
            G.Senior[pi] = p3
            ForceAddPlayer(G.Vassals[pi3], p)
            NewAlly(p)
        end
    end
end

function InitTrig_FeodalDead2()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(trig, Condition(Trig_FeodalDead2_Conditions))
    TriggerAddAction(trig, Trig_FeodalDead2_Actions)
    G.gg_trg_FeodalDead2 = trig
end

-- ============================================================
-- DoNotAttackSenior (old) — Stop vassals from attacking senior
-- ============================================================

function Trig_DoNotAttackSenior_Conditions()
    return IsPlayerInForce(GetOwningPlayer(GetAttacker()), G.udg_Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1])
end

function Trig_DoNotAttackSenior_Actions()
    IssueImmediateOrderBJ(GetAttacker(), "stop")
end

function InitTrig_DoNotAttackSenior()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(trig, Condition(Trig_DoNotAttackSenior_Conditions))
    TriggerAddAction(trig, Trig_DoNotAttackSenior_Actions)
    G.gg_trg_DoNotAttackSenior = trig
end

-- ============================================================
-- DoNotAttackSenior2 (new) — Stop vassals from attacking senior
-- ============================================================

function Trig_DoNotAttackSenior2_Conditions()
    return IsPlayerInForce(GetOwningPlayer(GetAttacker()), G.Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end

function Trig_DoNotAttackSenior2_Actions()
    IssueImmediateOrder(GetAttacker(), "stop")
end

function InitTrig_DoNotAttackSenior2()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(trig, Condition(Trig_DoNotAttackSenior2_Conditions))
    TriggerAddAction(trig, Trig_DoNotAttackSenior2_Actions)
    G.gg_trg_DoNotAttackSenior2 = trig
end

-- ============================================================
-- AllPlayers and vassals — Debug command
-- ============================================================

function Trig_AllPlayers_and_vassals_Actions()
    for iA = 1, 24 do
        DisplayTextToForce(GetPlayersAll(), GetPlayerName(Player(iA - 1)))
        DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19436")
        DisplayTextToForce(GetPlayersAll(), tostring(CountPlayersInForceBJ(G.udg_Vassals[iA])))
    end
end

function InitTrig_AllPlayers_and_vassals()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-feodifo", true)
    TriggerAddAction(trig, Trig_AllPlayers_and_vassals_Actions)
    G.gg_trg_AllPlayers_and_vassals = trig
end

-- ============================================================
-- DominationButton — Sets game mode to Domination (3)
-- ============================================================

function Trig_DominationButton_Conditions()
    return GetSpellAbilityId() == FourCC('A1KJ')
end

function Trig_DominationButton_Actions()
    G.udg_GameMode = 3
    DisplayTextToForce(GetPlayersAll(), "Режим выбран: Доминация")
end

function InitTrig_DominationButton()
    local trig = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_DominationButton_Conditions))
    TriggerAddAction(trig, Trig_DominationButton_Actions)
    G.gg_trg_DominationButton = trig
end

-- ============================================================
-- Domination start — Domination mode initialization
-- ============================================================

function Trig_Domination_start_Conditions()
    return G.udg_GameMode == 3 or G.udg_GameMode == 5
end

function ExpandTable()
    local i = 0
    local max = 1

    MultiboardSetColumnCount(G.Multiboard, 3)

    G.ThirdColumn[24] = MultiboardGetItem(G.Multiboard, 0, 2)
    MultiboardSetItemValue(G.ThirdColumn[24], "Точек,%")
    MultiboardSetItemWidth(G.ThirdColumn[24], 0.06)
    MultiboardReleaseItem(G.ThirdColumn[24])

    while i <= 23 do
        G.CityPlayerCount[i] = 0
        if GetPlayerSlotState(Player(i)) == PLAYER_SLOT_STATE_PLAYING or IsPlayerInForce(Player(i), G.udg_Bots) then
            G.ThirdColumn[i] = MultiboardGetItem(G.Multiboard, max, 2)
            MultiboardSetItemValue(G.ThirdColumn[i], "0.000%")
            MultiboardSetItemWidth(G.ThirdColumn[i], 0.06)
            max = max + 1
        end
        i = i + 1
    end

    MultiboardDisplay(G.Multiboard, false)
    MultiboardDisplay(G.Multiboard, true)
end

function Trig_Domination_start_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "Включен режим доминация. Захватите " .. tostring(G.PercentWin) .. "% городов, чтобы победить!")
end

function InitTrig_Domination_start()
    local trig = CreateTrigger()
    TriggerRegisterTimerExpireEvent(trig, G.udg_LobbyTime)
    TriggerAddCondition(trig, Condition(Trig_Domination_start_Conditions))
    TriggerAddAction(trig, Trig_Domination_start_Actions)
    G.gg_trg_Domination_start = trig
end

-- ============================================================
-- DomCheckCommand — Check domination progress
-- ============================================================

function Trig_DomCheckCommand_Actions()
    local pi = GetPlayerId(GetTriggerPlayer())
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "Вы контролируете " .. tostring(G.CityPlayerCount[pi]) .. " Точек из " .. tostring(G.CityCount) .. " на карте и из " .. tostring(MathRound(G.CityCount * 0.01 * G.PercentWin)) .. " необходимых для победы")
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "Таким образом ваш процент " .. R2SW_Polyfill(G.CityPlayerCount[pi] * 100.0 / G.CityCount) .. "% из необходимых " .. tostring(G.PercentWin) .. "%")
end

function InitTrig_DomCheckCommand()
    local trig = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(trig, Player(i), "-domck", true)
    end
    TriggerAddAction(trig, Trig_DomCheckCommand_Actions)
    G.gg_trg_DomCheckCommand = trig
end

-- ============================================================
-- PercentGraph — Update domination percentage on multiboard
-- ============================================================

function PercentGraph(pi)
    MultiboardSetItemValue(G.ThirdColumn[pi], R2SW_Polyfill(G.CityPlayerCount[pi] * 100.0 / G.CityCount) .. "%")
end

-- ============================================================
-- CheckCity — Win/loss check for domination mode
-- ============================================================

function CheckCity(p)
    local winid = GetPlayerId(p)
    local WinLimit = MathRound(G.CityCount * G.PercentWin / 100)
    local DangerLimit = MathRound(WinLimit * 0.75)
    local i = 0

    -- Победа
    if G.CityPlayerCount[winid] >= WinLimit then
        while i <= 23 do
            if i ~= winid then
                ClearPlayer(Player(i))
                DisplayTextToPlayer(Player(i), 0, 0, "Вы проиграли, игрок " .. GetPlayerName(p) .. " - достиг " .. R2S(WinLimit / G.CityCount) .. "% кол-ва точек и победил")
            else
                DisplayTextToPlayer(Player(i), 0, 0, "Вы победили!")
            end
            i = i + 1
        end
    elseif G.CityPlayerCount[winid] >= DangerLimit then
        while i <= 23 do
            if i ~= winid then
                DisplayTextToPlayer(Player(i), 0, 0, "Острожно, игрок " .. GetPlayerName(p) .. " - достиг " .. R2S(DangerLimit / G.CityCount) .. "% кол-ва точек (" .. tostring(DangerLimit) .. ")")
            else
                DisplayTextToPlayer(Player(i), 0, 0, "Вы достигли " .. R2S(DangerLimit / G.CityCount) .. "%!")
            end
            i = i + 1
        end
    end
end

-- ============================================================
-- City capture (AHad) — economic fix and city counting
-- ============================================================

function FixEcEnum()
    local u = GetEnumUnit()
    local pi = GetPlayerId(GetOwningPlayer(u))

    if GetUnitAbilityLevel(u, FourCC('AHad')) > 0 then
        G.CityPlayerCount[pi] = G.CityPlayerCount[pi] + 1
    end

    AddCountDis(u, pi)
end

-- ============================================================
-- Cities Start 2 — Initialize neutral cities
-- ============================================================

function ItIsCity()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('AHad')) == 1 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0
end

function Trig_Cities_Start_2_Func003A()
    local u = GetEnumUnit()
    local id = GetUnitTypeId(u)
    G.CityCount = G.CityCount + 1
    BlzSetUnitArmor(u, 3)
    SetUnitState(u, UNIT_STATE_LIFE, 5000)
    GroupAddUnit(G.udg_ZahvatBuildings, u)
    GroupAddUnit(G.udg_BuildedSctructure[1], u)
    if id == FourCC('h08A') or id == FourCC('h004') or id == FourCC('h0B3') or id == FourCC('h081') or id == FourCC('h0AP')
    or id == FourCC('h00G') or id == FourCC('h08G') or id == FourCC('h05O') or id == FourCC('h089') or id == FourCC('h0AG')
    or id == FourCC('h097') or id == FourCC('h09Z') or id == FourCC('h088') or id == FourCC('h094') or id == FourCC('h00F')
    or id == FourCC('h09P') or id == FourCC('h0BB') or id == FourCC('h0E3') or id == FourCC('h06I') then
        GroupAddUnit(G.PortalBuildingAi, u)
    end
end

function Trig_Cities_Start_2_Actions()
    G.udg_Boolexpr = Condition(ItIsCity)
    GroupEnumUnitsInRect(G.udg_LocalOtrad2, bj_mapInitialPlayableArea, G.udg_Boolexpr)
    ForGroup(G.udg_LocalOtrad2, Trig_Cities_Start_2_Func003A)
    GroupClear(G.udg_LocalOtrad2)
end

function InitTrig_Cities_Start_2()
    local trig = CreateTrigger()
    TriggerRegisterTimerEvent(trig, 0.01, false)
    TriggerAddAction(trig, Trig_Cities_Start_2_Actions)
    G.gg_trg_Cities_Start_2 = trig

    for i = 0, 23 do
        G.CityPlayerCount[i] = 0
    end
end

-- ============================================================
-- DeadSituastion — City death capture for domination/feodal
-- ============================================================
-- (This handler is for city capture. The city death that
-- creates a new unit with new owner is in the main map code.)

-- ============================================================
-- Diplomacy: NoDipFFA (DipMode 1)
-- ============================================================

function Trig_NoDipFFA_Conditions()
    return GetSpellAbilityId() == FourCC('A1KR')
end

function Trig_NoDipFFA_Actions()
    G.DipMode = 1
    DisplayTextToForce(GetPlayersAll(), "Союзы отключены. Да начнутся голодные игры.")
end

function InitTrig_NoDipFFA()
    local trig = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_NoDipFFA_Conditions))
    TriggerAddAction(trig, Trig_NoDipFFA_Actions)
    G.gg_trg_NoDipFFA = trig
end

-- ============================================================
-- Diplomacy: Dip2 (DipMode 2)
-- ============================================================

function Trig_Dip2_Conditions()
    return GetSpellAbilityId() == FourCC('A1KS')
end

function Trig_Dip2_Actions()
    G.DipMode = 2
    DisplayTextToForce(GetPlayersAll(), "Включены союзы по 2")
end

function InitTrig_Dip2()
    local trig = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_Dip2_Conditions))
    TriggerAddAction(trig, Trig_Dip2_Actions)
    G.gg_trg_Dip2 = trig
end

-- ============================================================
-- Diplomacy: Dip3 (DipMode 3)
-- ============================================================

function Trig_Dip3_Conditions()
    return GetSpellAbilityId() == FourCC('A1KT')
end

function Trig_Dip3_Actions()
    G.DipMode = 3
    DisplayTextToForce(GetPlayersAll(), "Включены союзы по 3")
end

function InitTrig_Dip3()
    local trig = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_Dip3_Conditions))
    TriggerAddAction(trig, Trig_Dip3_Actions)
    G.gg_trg_Dip3 = trig
end

-- ============================================================
-- Diplomacy: FreeDip (DipMode 0) — Free diplomacy
-- ============================================================

function Trig_FreeDip_Conditions()
    return GetSpellAbilityId() == FourCC('A1KQ')
end

function Trig_FreeDip_Actions()
    G.DipMode = 0
    DisplayTextToForce(GetPlayersAll(), "Включена свободная дипломатия")
end

function InitTrig_FreeDip()
    local trig = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trig, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trig, Condition(Trig_FreeDip_Conditions))
    TriggerAddAction(trig, Trig_FreeDip_Actions)
    G.gg_trg_FreeDip = trig
end

-- ============================================================
-- Diplomacy: DipStart — Apply diplomacy settings at lobby time
-- ============================================================

function ClearPlayerEach()
    ClearOldAllies(GetEnumPlayer())
end

function Trig_DipStart_Actions()
    -- FFA
    if G.DipMode == 1 then
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, true)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, true)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, true)
        ForForce(G.udg_AllPlayers2, ClearPlayerEach)
    -- FREE
    else
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    end
end

function InitTrig_DipStart()
    local trig = CreateTrigger()
    TriggerRegisterTimerExpireEvent(trig, G.udg_LobbyTime)
    TriggerAddAction(trig, Trig_DipStart_Actions)
    G.gg_trg_DipStart = trig
end

-- ============================================================
-- Diplomacy: StartAlly — Alliance change enforcement
-- ============================================================

function WritePlayerName()
    DisplayTextToForce(G.udg_AllPlayers, "Игроком: " .. GetPlayerName(GetEnumPlayer()))
end

function Trig_StartAlly_Actions()
    local p = GetTriggerPlayer()
    local AllyCount = 0
    ForceEnumAllies(G.gForce, p, nil)
    AllyCount = CountPlayersInForceBJ(G.gForce)
    if G.DipMode == 0 then
        -- Оповещение о превышении
        if AllyCount > 1 then
            DisplayTextToForce(G.udg_AllPlayers, "Игрок " .. GetPlayerName(p) .. " заключил союз с более чем одним!")
            ForForce(G.gForce, WritePlayerName)
        end
    else
        if AllyCount > G.DipMode then
            ClearAllies(p)
            DisplayTextToForce(G.udg_AllPlayers, "Игрок " .. GetPlayerName(p) .. " заключил слишком много союзов, его альянсы сброшены")
        end
    end
    G.AllyTax[GetPlayerId(p)] = 0.1 * AllyCount
    ForceClear(G.gForce)
end

function InitTrig_StartAlly()
    local trig = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerEvent(trig, Player(i), EVENT_PLAYER_ALLIANCE_CHANGED)
    end
    TriggerAddAction(trig, Trig_StartAlly_Actions)
    G.gg_trg_StartAlly = trig
end

-- ============================================================
-- InitThings — Initialize capital, vassal, senior arrays
-- ============================================================

function InitThings()
    for i = 0, 24 do
        G.cap_time[i] = true
        G.Vassals[i] = CreateForce()
        G.Senior[i] = nil
        G.Capital[i] = nil
    end
end

-- ============================================================
-- CorrectNumber — helper for ArchontMode (DipMode check)
-- ============================================================

function CorrectNumber(pi2)
    return pi2 >= 0 and pi2 <= 24
end

-- ============================================================
-- Debug test commands: Player2VassalTo1, Player3VassalTo1
-- ============================================================

-- Player2VassalTo1 Back Copy (-dv <id>)
function Trig_Player2VassalTo1_Back_Copy_Conditions()
    local val = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    return val and val >= 1 and val <= 24
end

function Trig_Player2VassalTo1_Back_Copy_Actions()
    G.udg_LocalInteger = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    SetPlayerAllianceStateBJ(Player(G.udg_LocalInteger - 1), Player(0), bj_ALLIANCE_UNALLIED)
end

function InitTrig_Player2VassalTo1_Back_Copy()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-dv", false)
    TriggerAddCondition(trig, Condition(Trig_Player2VassalTo1_Back_Copy_Conditions))
    TriggerAddAction(trig, Trig_Player2VassalTo1_Back_Copy_Actions)
    G.gg_trg_Player2VassalTo1_Back_Copy = trig
end

-- Player2VassalTo1 Copy (-vs <id>)
function Trig_Player2VassalTo1_Copy_Conditions()
    local val = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    return val and val >= 1 and val <= 24
end

function Trig_Player2VassalTo1_Copy_Actions()
    G.udg_LocalInteger = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    SetPlayerAllianceStateBJ(Player(G.udg_LocalInteger - 1), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end

function InitTrig_Player2VassalTo1_Copy()
    local trig = CreateTrigger()
    DisableTrigger(trig)
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-vs", false)
    TriggerAddCondition(trig, Condition(Trig_Player2VassalTo1_Copy_Conditions))
    TriggerAddAction(trig, Trig_Player2VassalTo1_Copy_Actions)
    G.gg_trg_Player2VassalTo1_Copy = trig
end

-- Player2VassalTo1 (b1)
function Trig_Player2VassalTo1_Actions()
    SetPlayerAllianceStateBJ(Player(1), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end

function InitTrig_Player2VassalTo1()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "b1", true)
    TriggerAddAction(trig, Trig_Player2VassalTo1_Actions)
    G.gg_trg_Player2VassalTo1 = trig
end

-- Player2VassalTo1 Back (b2)
function Trig_Player2VassalTo1_Back_Actions()
    SetPlayerAllianceStateBJ(Player(1), Player(0), bj_ALLIANCE_UNALLIED)
end

function InitTrig_Player2VassalTo1_Back()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "b2", true)
    TriggerAddAction(trig, Trig_Player2VassalTo1_Back_Actions)
    G.gg_trg_Player2VassalTo1_Back = trig
end

-- Player3VassalTo1 (c1)
function Trig_Player3VassalTo1_Actions()
    SetPlayerAllianceStateBJ(Player(2), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end

function InitTrig_Player3VassalTo1()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "c1", true)
    TriggerAddAction(trig, Trig_Player3VassalTo1_Actions)
    G.gg_trg_Player3VassalTo1 = trig
end

-- Player3VassalTo1 Back (c2)
function Trig_Player3VassalTo1_Back_Actions()
    SetPlayerAllianceStateBJ(Player(2), Player(0), bj_ALLIANCE_UNALLIED)
end

function InitTrig_Player3VassalTo1_Back()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "c2", true)
    TriggerAddAction(trig, Trig_Player3VassalTo1_Back_Actions)
    G.gg_trg_Player3VassalTo1_Back = trig
end

-- ============================================================
-- AnyPlayerVassalToFirst (-vs <id>)
-- ============================================================

function Trig_AnyPlayerVassalToFirst_Conditions()
    local val = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5))
    return val and val >= 1 and val <= 24
end

function Trig_AnyPlayerVassalToFirst_Actions()
    local pi = tonumber(SubStringBJ(GetEventPlayerChatString(), 4, 5)) - 1
    SetPlayerAllianceStateBJ(Player(pi), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
end

function InitTrig_AnyPlayerVassalToFirst()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-vs", false)
    TriggerAddAction(trig, Trig_AnyPlayerVassalToFirst_Actions)
    TriggerAddCondition(trig, Condition(Trig_AnyPlayerVassalToFirst_Conditions))
    G.gg_trg_AnyPlayerVassalToFirst = trig
end

-- ============================================================
-- AnyPlayerVassalToFirstOff (-vsoff <id>)
-- ============================================================

function Trig_AnyPlayerVassalToFirstOff_Conditions()
    local val = tonumber(SubStringBJ(GetEventPlayerChatString(), 7, 8))
    return val and val >= 1 and val <= 24
end

function Trig_AnyPlayerVassalToFirstOff_Actions()
    local pi = tonumber(SubStringBJ(GetEventPlayerChatString(), 7, 8)) - 1
    SetPlayerAllianceStateBJ(Player(pi), Player(0), bj_ALLIANCE_UNALLIED)
end

function InitTrig_AnyPlayerVassalToFirstOff()
    local trig = CreateTrigger()
    TriggerRegisterPlayerChatEvent(trig, Player(0), "-vsoff", false)
    TriggerAddAction(trig, Trig_AnyPlayerVassalToFirstOff_Actions)
    TriggerAddCondition(trig, Condition(Trig_AnyPlayerVassalToFirstOff_Conditions))
    G.gg_trg_AnyPlayerVassalToFirstOff = trig
end

-- ============================================================
-- ArchontMode — Command to give full control
-- ============================================================

function Trig_ArchontMode_Actions()
    local s = SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2 = tonumber(s) - 1
    local pi1 = GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) and G.DipMode ~= 1 then
        DisplayTextToPlayer(Player(pi1), 0, 0, "Вы попытались дать полный контроль игроку " .. GetPlayerName(Player(pi2)) .. " номер " .. tostring(pi2))
        DisplayTextToPlayer(Player(pi2), 0, 0, "Вам попытался дать полный контроль игрок " .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceStateBJ(Player(pi1), Player(pi2), bj_ALLIANCE_ALLIED_ADVUNITS)
    end
    MultiboardAllowDisplayBJ(true)
end

function InitTrig_ArchontMode()
    local trig = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(trig, Player(i), "-arhont", false)
    end
    TriggerAddAction(trig, Trig_ArchontMode_Actions)
    G.gg_trg_ArchontMode = trig
end

-- ============================================================
-- Initialization entry point
-- ============================================================

function InitStolica()
    -- Create groups and forces
    G.udg_StolicaGroups = CreateGroup()
    for i = 0, 25 do
        G.udg_Vassals[i] = CreateForce()
    end

    -- Initialize non-udg globals
    InitThings()

    -- TimerData table for StolicaAttacked closure-based storage
    G.TimerData = {}

    -- FeodalDead scratch globals (BJ loop indexer replacement)
    G._fd_iA = 1
    G._fd_iB = 1

    -- Multiboard ThirdColumn array
    G.ThirdColumn = {}

    -- Initialize all triggers
    InitTrig_UpgradeStolica()
    InitTrig_MakeStolica()
    InitTrig_StolicaTime()
    InitTrig_StolicaDead()
    InitTrig_StolicaAttacked()
    InitTrig_StolicaKill()
    InitTrig_MOD_stolica_Start()
    InitTrig_MOD_stolica_Start_Copy()
    InitTrig_MOD_feoda_O_Start()
    InitTrig_FeodalDead()
    InitTrig_FeodalDead2()
    InitTrig_DoNotAttackSenior()
    InitTrig_DoNotAttackSenior2()
    InitTrig_AllPlayers_and_vassals()
    InitTrig_DominationButton()
    InitTrig_Domination_start()
    InitTrig_DomCheckCommand()
    InitTrig_Cities_Start_2()
    InitTrig_NoDipFFA()
    InitTrig_Dip2()
    InitTrig_Dip3()
    InitTrig_FreeDip()
    InitTrig_DipStart()
    InitTrig_StartAlly()
    InitTrig_Player2VassalTo1_Back_Copy()
    InitTrig_Player2VassalTo1_Copy()
    InitTrig_Player2VassalTo1()
    InitTrig_Player2VassalTo1_Back()
    InitTrig_Player3VassalTo1()
    InitTrig_Player3VassalTo1_Back()
    InitTrig_AnyPlayerVassalToFirst()
    InitTrig_AnyPlayerVassalToFirstOff()
    InitTrig_ArchontMode()
end
