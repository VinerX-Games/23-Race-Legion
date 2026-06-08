
--===========================================================================
-- Trigger: TurnAi
--===========================================================================
function Trig_TurnAi_Actions()
    ProbeLogWrite("[AI] TurnAi: checking if triggers already enabled")
    if not IsTriggerEnabled(gg_trg_OchetStart) then
        ProbeLogWrite("[AI] TurnAi: enabling all AI triggers (first bot)")
        EnableTrigger(gg_trg_OchetStart)
        EnableTrigger(gg_trg_OchetEnd)
        EnableTrigger(gg_trg_PereborPlayersForBuilders)
        EnableTrigger(gg_trg_PereborBuilders_Uni)
        EnableTrigger(gg_trg_PereborPlayerForArmy)
        EnableTrigger(gg_trg_PerebobArmy_Uni)
        EnableTrigger(gg_trg_PereborPlayerForNavy)
        EnableTrigger(gg_trg_PereborBuildings)
        EnableTrigger(gg_trg_PerebobNavy)
        EnableTrigger(gg_trg_Strateg)
        EnableTrigger(gg_trg_AttackerAi)
        EnableTrigger(gg_trg_AttackedAI)
        EnableTrigger(gg_trg_GetLvl)
        EnableTrigger(gg_trg_Revive)
        EnableTrigger(gg_trg_PereborNavalBases)
        
        EnableTrigger(gg_trg_JoinAll)
        EnableTrigger(gg_trg_JoinBuildings)
        EnableTrigger(gg_trg_UpgradeBuildings)
        EnableTrigger(gg_trg_EndBuilding)
        EnableTrigger(gg_trg_CheckType)
        EnableTrigger(gg_trg_CheckOrderType)
        EnableTrigger(gg_trg_PortUnits)
        EnableTrigger(gg_trg_Leave_Army_U)
        EnableTrigger(gg_trg_Leave_Navy_U)
        EnableTrigger(gg_trg_Leave_Harvest_U)
        EnableTrigger(gg_trg_Leave_Builders_U)
        EnableTrigger(gg_trg_Leave_BuildersT_U)
        EnableTrigger(gg_trg_Leave_Buildings_U)
        EnableTrigger(gg_trg_CheckType)
        EnableTrigger(gg_trg_CheckOrderType)
        EnableTrigger(gg_trg_SellAl)
        
        --Scrited events
        EnableTrigger(gg_trg_SargerasTemple)
        
        
        ForForce(udg_Bots, Trig_sek5_Func001A)
    end
    
    
end
--===========================================================================
function InitTrig_TurnAi()
    gg_trg_TurnAi=CreateTrigger()
    TriggerAddAction(gg_trg_TurnAi, Trig_TurnAi_Actions)
end
--===========================================================================
-- Trigger: StartTimerToHard
--===========================================================================
function Trig_StartTimerToHard_Actions()
    AiMoney=AiMoney + 2
    --set AiRepeat = 6
    --set AiMass = 5
    --set AiLimit = 20
end
--===========================================================================
function InitTrig_StartTimerToHard()
    gg_trg_StartTimerToHard=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_StartTimerToHard, udg_TimerToChangeAi)
    TriggerAddAction(gg_trg_StartTimerToHard, Trig_StartTimerToHard_Actions)
end
--===========================================================================
-- Trigger: EveryAiEnemy
--===========================================================================
function Trig_EveryAiEnemy_Actions()
    local i= 0
    local f= CreateForce()
    while true do
        if i > 23 then break end
        if udg_AiControl[i] then
            ForceAddPlayer(f, Player(i))
        end
        
        i=i + 1
    end
    SetForceAllianceStateBJ(f, f, bj_ALLIANCE_ALLIED_VISION)
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, ". not ")
    DestroyForce(f)
    f=nil
end
--===========================================================================
function InitTrig_EveryAiEnemy()
    gg_trg_EveryAiEnemy=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_EveryAiEnemy, Player(0), " - AllIn", true)
    TriggerAddAction(gg_trg_EveryAiEnemy, Trig_EveryAiEnemy_Actions)
end
--===========================================================================
-- Trigger: CreateAi
--===========================================================================
function Trig_CreateAi_Conditions()
    return S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) >= 1 and S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) <= 24
end
function Trig_CreateAi_Actions()
    -- ??????: "-aiN" ??? "-aiN <????>" (???? ???????????, ?????????: jt, be, scarlet, goblins, naga, horde)
    local s = GetEventPlayerChatString()
    local numStr, raceStr = string.match(s, "^%-ai%s*(%d+)%s*(%S*)")
    gPi = (tonumber(numStr) or 1) - 1
    if raceStr == "" then raceStr = nil end
    ProbeLogWrite("[CHAT] -ai target=" .. tostring(gPi + 1) .. " race=" .. tostring(raceStr or "random"))
    createAiPlayer(gPi, raceStr)
end
--===========================================================================
function InitTrig_CreateAi()
    gg_trg_CreateAi=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_CreateAi, Player(0), "-ai", false)
    TriggerAddCondition(gg_trg_CreateAi, Condition(Trig_CreateAi_Conditions))
    TriggerAddAction(gg_trg_CreateAi, Trig_CreateAi_Actions)
end
function BridgeDispatchCommand(op, arg, sequence)
    if op == "ping" then
        ProbeLogWrite("[BRIDGE] ping seq=" .. tostring(sequence) .. " arg=" .. tostring(arg))
        return
    end
    -- arg ????? ???? "N" ??? "N:race" (???? ???????????, ?????????)
    local targetStr, raceTok = string.match(tostring(arg), "^(%d+):?(%S*)")
    local target = tonumber(targetStr)
    if target == nil then
        error("bridge command requires numeric arg: " .. tostring(op))
    end
    if target < 1 or target > 24 then
        error("bridge target out of range: " .. tostring(target))
    end
    if op == "create_ai" then
        if raceTok == "" then raceTok = nil end
        createAiPlayer(target - 1, raceTok)
        ProbeLogWrite("[BRIDGE] create_ai target=" .. tostring(target) .. " race=" .. tostring(raceTok or "random"))
        return
    end
    if op == "race_select" then
        BridgeRaceSelect(target)
        return
    end
    if op == "log" then
        local logOp, logTag = string.match(tostring(arg), "^(on|off|toggle|allon|alloff|list):?(.*)")
        if logOp == "allon" then
            LogFilterAll = true
            ProbeLogWrite("[LOG] filter all_on")
            return
        end
        if logOp == "alloff" then
            LogFilterAll = false
            ProbeLogWrite("[LOG] filter all_off")
            return
        end
        if logOp == "list" then
            LogList()
            return
        end
        if logTag == "" or logTag == nil then
            error("log requires tag, e.g. log:on:AI")
        end
        if logOp == "on" then
            LogEnable(logTag)
        elseif logOp == "off" then
            LogDisable(logTag)
        elseif logOp == "toggle" then
            LogToggle(logTag)
        else
            error("unknown log sub-command: " .. tostring(logOp))
        end
        ProbeLogWrite("[LOG] filter " .. logOp .. " tag=" .. logTag)
        return
    end
    error("unknown bridge command: " .. tostring(op))
end
--===========================================================================
-- Trigger: OchetStart
--===========================================================================
function Trig_OchetStart_Actions()
    udg_Octhet=true
end
--===========================================================================
function InitTrig_OchetStart()
    gg_trg_OchetStart=CreateTrigger()
    DisableTrigger(gg_trg_OchetStart)
    TriggerRegisterPlayerChatEvent(gg_trg_OchetStart, Player(0), " - Os", true)
    TriggerAddAction(gg_trg_OchetStart, Trig_OchetStart_Actions)
end
--===========================================================================
-- Trigger: OchetEnd
--===========================================================================
function Trig_OchetEnd_Actions()
    udg_Octhet=false
end
--===========================================================================
function InitTrig_OchetEnd()
    gg_trg_OchetEnd=CreateTrigger()
    DisableTrigger(gg_trg_OchetEnd)
    TriggerRegisterPlayerChatEvent(gg_trg_OchetEnd, Player(0), " - Oe", true)
    TriggerAddAction(gg_trg_OchetEnd, Trig_OchetEnd_Actions)
end
--===========================================================================
-- Trigger: CheckType
--===========================================================================
function Trig_CheckType_Actions()
    local g= CreateGroup()
    local u
    local i= 0
    local b= 0
    GroupEnumUnitsSelected(g, Player(0), nil)
    u=FirstOfGroup(g)
    --call DisplayTimedTextFromPlayer(Player(0),0,0, 4, ""+I2S(GetPlayerId(GetOwningPlayer(u)))+""+I2S(GetUnitTypeId(u)))
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    while true do
        if i == 23 then break end
        b=AiData[i][GetUnitTypeId(u)] or 0
        DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, GetPlayerName(Player(i)) .. " - " .. I2S(b))
        i=i + 1
    end
    
end
--===========================================================================
function InitTrig_CheckType()
    gg_trg_CheckType=CreateTrigger()
    DisableTrigger(gg_trg_CheckType)
    TriggerRegisterPlayerChatEvent(gg_trg_CheckType, Player(0), "1", true)
    TriggerAddAction(gg_trg_CheckType, Trig_CheckType_Actions)
end
--===========================================================================
-- Trigger: CheckOrderType
--===========================================================================
function Trig_CheckOrderType_Actions()
    local g= CreateGroup()
    local u
    local s
    GroupEnumUnitsSelected(g, Player(0), nil)
    u=FirstOfGroup(g)
    s="" .. OrderId2String(GetUnitCurrentOrder(u)) .. "" .. I2S(GetUnitCurrentOrder(u))
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, s)
end
--===========================================================================
function InitTrig_CheckOrderType()
    gg_trg_CheckOrderType=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_CheckOrderType, Player(0), " - getOrder", true)
    TriggerAddAction(gg_trg_CheckOrderType, Trig_CheckOrderType_Actions)
end
--===========================================================================
-- Trigger: CheckGroup
--===========================================================================
function ConditionPlayerNumber()
    return S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) >= 1 and S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) <= 24
end
function TestGroupForAll()
    local u= GetEnumUnit()
    BJDebugMsg(I2S(Counter) .. "" .. GetUnitName(u))
    Counter=Counter + 1
end
function Trig_CheckGroup_Actions()
    local pi= S2I(SubStringBJ(GetEventPlayerChatString(), 4, 5)) - 1
    local g= CreateGroup()
    
    LazyCount=0
    CheckPlayer=Player(pi)
    GroupEnumUnitsOfPlayer(g, Player(pi), B_LazyN)
    Counter=0
    BJDebugMsg("B_LazyN" .. GetPlayerName(Player(pi)) .. " - " .. I2S(LazyCount))
    ForGroup(g, TestGroupForAll)
    BJDebugMsg("" .. GetPlayerName(Player(pi)))
    
    BJDebugMsg("udg_Ai_navy" .. GetPlayerName(Player(pi)) .. " - " .. I2S(LazyCount))
    ForGroup(udg_Ai_navy[pi], TestGroupForAll)
    BJDebugMsg("" .. GetPlayerName(Player(pi)))
end
--===========================================================================
function InitTrig_CheckGroup()
    gg_trg_CheckGroup=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_CheckGroup, Player(0), " - gr", false)
    TriggerAddAction(gg_trg_CheckGroup, Trig_CheckGroup_Actions)
    TriggerAddCondition(gg_trg_CheckGroup, Condition(ConditionPlayerNumber))
end
--===========================================================================
-- Trigger: AiMoney
--===========================================================================
function Trig_AiMoney_Actions()
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 9, 10)
    AiMoney=S2I(udg_LocalText2)
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
end
--===========================================================================
function InitTrig_AiMoney()
    gg_trg_AiMoney=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiMoney, Player(0), " - aimoney", false)
    TriggerAddAction(gg_trg_AiMoney, Trig_AiMoney_Actions)
    
end
--===========================================================================
-- Trigger: AiRepeat
--===========================================================================
function Trig_AiRepeat_Actions()
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 10, 11)
    AiRepeat=IMinBJ(1, S2I(udg_LocalText2))
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
end
--===========================================================================
function InitTrig_AiRepeat()
    gg_trg_AiRepeat=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiRepeat, Player(0), " - airepeat", false)
    TriggerAddAction(gg_trg_AiRepeat, Trig_AiRepeat_Actions)
end
--===========================================================================
-- Trigger: AiRadius
--===========================================================================
function Trig_AiRadius_Actions()
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 10, 12)
    AiRadius=IMaxBJ(10, S2I(udg_LocalText2))
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
end
--===========================================================================
function InitTrig_AiRadius()
    gg_trg_AiRadius=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiRadius, Player(0), " - airadius", false)
    TriggerAddAction(gg_trg_AiRadius, Trig_AiRadius_Actions)
end
--===========================================================================
-- Trigger: AiMass
--===========================================================================
function Trig_AiMass_Actions()
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 8, 9)
    AiMass=S2I(udg_LocalText2)
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
end
--===========================================================================
function InitTrig_AiMass()
    gg_trg_AiMass=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiMass, Player(0), " - aimass", false)
    TriggerAddAction(gg_trg_AiMass, Trig_AiMass_Actions)
end
--===========================================================================
-- Trigger: Ailimit
--===========================================================================
function Trig_Ailimit_Actions()
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 9, 12)
    AiLimit=S2I(udg_LocalText2)
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "" .. I2S(AiLimit) .. "")
end
--===========================================================================
function InitTrig_Ailimit()
    gg_trg_Ailimit=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Ailimit, Player(0), " - ailimit", false)
    TriggerAddAction(gg_trg_Ailimit, Trig_Ailimit_Actions)
end
--===========================================================================
-- Trigger: CityNearWater2
--
-- ??? ??????, ??????? ????? ????????? ? ????
--===========================================================================
function Trig_CityNearWater2_Actions()
    -- ?????
    GroupAddUnitSimple(gg_unit_h08O_0444, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0E2_0011, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h08G_0419, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h00E_0106, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h00F_0105, udg_CityNearWater)
    -- ???????
    GroupAddUnitSimple(gg_unit_h0BM_0604, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BL_0603, udg_CityNearWater)
    -- ????????
    GroupAddUnitSimple(gg_unit_h0AH_0427, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AG_0010, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AF_0383, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AL_0496, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h09Z_0492, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AK_0488, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AM_0550, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0A0_0120, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h09V_0137, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h09W_0236, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0A3_0241, udg_CityNearWater)
    -- ??????? 2
    GroupAddUnitSimple(gg_unit_h0BH_0601, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0F8_0045, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BG_0600, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BF_0012, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0OT_0545, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0OJ_0336, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0OH_0333, udg_CityNearWater)
    -- ????????
    GroupAddUnitSimple(gg_unit_h00M_0113, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h04L_0458, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h07O_0251, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h07N_0238, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BI_0340, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BJ_0602, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h089_0405, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h08A_0406, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0II_0455, udg_CityNearWater)
    -- ??????????
    GroupAddUnitSimple(gg_unit_h0AW_0341, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0B9_0026, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BC_0342, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0BB_0343, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AU_0344, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h0AP_0552, udg_CityNearWater)
    -- ????
    GroupAddUnitSimple(gg_unit_h09O_0541, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h09M_0539, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h097_0502, udg_CityNearWater)
    GroupAddUnitSimple(gg_unit_h09A_0506, udg_CityNearWater)
end
--===========================================================================
function InitTrig_CityNearWater2()
    gg_trg_CityNearWater2=CreateTrigger()
    TriggerAddAction(gg_trg_CityNearWater2, Trig_CityNearWater2_Actions)
end
--===========================================================================
-- Trigger: Remove
--===========================================================================
function Trig_Remove_Actions()
    -- ?????
    GroupRemoveUnitSimple(gg_unit_h0E2_0011, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h08O_0444, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09B_0508, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09C_0509, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h097_0502, udg_TempGroup)
    -- ????????
    GroupRemoveUnitSimple(gg_unit_h0BJ_0602, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h0BG_0600, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h0BF_0012, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09P_0009, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09K_0537, udg_TempGroup)
    -- ????
    GroupRemoveUnitSimple(gg_unit_h09A_0506, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09N_0346, udg_TempGroup)
    -- ???????
    GroupRemoveUnitSimple(gg_unit_h0BL_0603, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h0BM_0604, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h0OK_0337, udg_TempGroup)
    -- ????????
    GroupRemoveUnitSimple(gg_unit_h0BH_0601, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_h09V_0137, udg_TempGroup)
    -- ????????
    GroupRemoveUnitSimple(gg_unit_n01D_0903, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_n01D_0904, udg_TempGroup)
end
--===========================================================================
function InitTrig_Remove()
    gg_trg_Remove=CreateTrigger()
    TriggerAddAction(gg_trg_Remove, Trig_Remove_Actions)
end
--===========================================================================
-- Trigger: RemPortalsFromAnotherSide
--===========================================================================
function Trig_RemPortalsFromAnotherSide_Actions()
    GroupRemoveUnitSimple(gg_unit_n003_0124, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_n003_0123, udg_TempGroup)
    -- ---
    GroupRemoveUnitSimple(gg_unit_n003_0118, udg_TempGroup)
    GroupRemoveUnitSimple(gg_unit_n003_0117, udg_TempGroup)
end
--===========================================================================
function InitTrig_RemPortalsFromAnotherSide()
    gg_trg_RemPortalsFromAnotherSide=CreateTrigger()
    TriggerAddAction(gg_trg_RemPortalsFromAnotherSide, Trig_RemPortalsFromAnotherSide_Actions)
end
--===========================================================================
-- Trigger: PereborPlayersForBuilders
--===========================================================================
function AddPlayers2()
    ForceAddPlayer(udg_BotsActiveB, GetEnumPlayer())
end
function Trig_PereborPlayersForBuilders_Actions()
    PauseTimer(udg_TimerSmall)
    if not (AiData[-1][StringHash("TickLog_TimerSmall")] or false) then
        AiData[-1][StringHash("TickLog_TimerSmall")] = true
        ProbeLogWrite("[AI] PereborPlayersForBuilders FIRST TICK")
    end
    if udg_Octhet then
        DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    end
    ForForce(udg_Bots, AddPlayers2)
    TimerStart(udg_PlayerGet2, 1.2 * AiRepeat / 5, true, nil)
end
--===========================================================================
function InitTrig_PereborPlayersForBuilders()
    gg_trg_PereborPlayersForBuilders=CreateTrigger()
    DisableTrigger(gg_trg_PereborPlayersForBuilders)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborPlayersForBuilders, udg_TimerSmall)
    TriggerAddAction(gg_trg_PereborPlayersForBuilders, Trig_PereborPlayersForBuilders_Actions)
end
--===========================================================================
-- Trigger: PereborBuilders Uni
--===========================================================================
function PlayerBuilders()
    local pi
    local i
        
    if CountPlayersInForceBJ(udg_BotsActiveB) == 0 then
        PauseTimer(udg_PlayerGet2)
        ResumeTimer(udg_TimerSmall)
        TimerStart(udg_TimerSmall, 4 * AiRepeat / 5, false, nil)
        if udg_Octhet then
            DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
        end
    else
        gPlayer=ForcePickRandomPlayer(udg_BotsActiveB)
        pi=GetPlayerId(gPlayer)
        if not (AiData[pi][StringHash("Log_PlayerBuilders")] or false) then
            AiData[pi][StringHash("Log_PlayerBuilders")] = true
            ProbeLogWrite("[AI] PlayerBuilders processing pi=" .. tostring(pi) .. " race=" .. tostring(AiRace[pi]))
        end
        ForceRemovePlayer(udg_BotsActiveB, gPlayer)
            
    
        
        -- ??????? ?????? !!!
        --???????????????? ???????
        GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_LazyW)
        if FirstOfGroup(gGroup) ~= nil then
            bj_forLoopAIndex=1
            while true do
                gUnit=FirstOfGroup(gGroup)
                if bj_forLoopAIndex > AiMass + 4 or FirstOfGroup(gGroup) == nil then break end
                
                GroupRemoveUnit(gGroup, gUnit)
                
                -- ???????
                if (AiData[pi][StringHash("T")] or 0) >= 12 then
                    NumberAdd(pi , StringHash("HV"))
                    GroupAddUnit(udg_Ai_harvest[pi], gUnit)
                    GroupRemoveUnit(udg_Ai_builders[pi], gUnit)
                    IssueImmediateOrder(gUnit, "autoharvestlumber")
                else -- ?????????
                    NumberAdd(pi , StringHash("T"))
                    GroupAddUnit(udg_Ai_buildersT[pi], gUnit)
                    GroupRemoveUnit(udg_Ai_builders[pi], gUnit)
                    TryBuild_u=gUnit
                    TryBuild()
                end
                bj_forLoopAIndex=bj_forLoopAIndex + 1
            end
            GroupClear(gGroup)
        end
        
        -- ???????-?????????
        GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_LazyT)
        if FirstOfGroup(gGroup) ~= nil then
            bj_forLoopAIndex=1
            bj_forLoopAIndexEnd=3
            while true do
                if bj_forLoopAIndex > bj_forLoopAIndexEnd + AiMass or FirstOfGroup(gGroup) == nil then break end
                gUnit=FirstOfGroup(gGroup)
                GroupRemoveUnit(gGroup, gUnit)
                TryBuild_u=gUnit
                TryBuild()
                
                bj_forLoopAIndex=bj_forLoopAIndex + 1
            end
            GroupClear(gGroup)
        end
        
        -- ???????? - ?? ??? ???????? ???? ???????
        if (AiData[pi][StringHash("T")] or 0) < 12 then
            Counter=0
            GroupEnumUnitsOfPlayer(gGroup, gPlayer, Harwest)
            
            while true do
                if (AiData[pi][StringHash("T")] or 0) > 9 or (AiData[pi][StringHash("HV")] or 0) < 1 then break end
            
                
                gUnit=BlzGroupUnitAt(gGroup, GetRandomInt(0, Counter - 1))
                
                GroupAddUnit(udg_Ai_buildersT[pi], gUnit)
                GroupRemoveUnit(udg_Ai_harvest[pi], gUnit)
                Counter=Counter - 1
                
                NumberAdd(pi , StringHash("T"))
                NumberRem(pi , StringHash("HV"))
                TryBuild_u=gUnit
                TryBuild()
            end
            
        end
        GroupClear(gGroup)
        
    end
    gUnit=nil
end
--===========================================================================
function InitTrig_PereborBuilders_Uni()
    gg_trg_PereborBuilders_Uni=CreateTrigger()
    DisableTrigger(gg_trg_PereborBuilders_Uni)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborBuilders_Uni, udg_PlayerGet2)
    TriggerAddAction(gg_trg_PereborBuilders_Uni, PlayerBuilders)
end
--===========================================================================
-- Trigger: PereborPlayerForArmy
--===========================================================================
function AddPlayers()
    ForceAddPlayer(udg_BotsActive, GetEnumPlayer())
end
--??????? ???? ???????? ?????? ??????, ????? ????, ????????
function Trig_PereborPlayerForArmy_Actions()
    PauseTimer(udg_TimerSmall2)
    if not (AiData[-1][StringHash("TickLog_TimerSmall2")] or false) then
        AiData[-1][StringHash("TickLog_TimerSmall2")] = true
        ProbeLogWrite("[AI] PereborPlayerForArmy FIRST TICK")
    end
    if udg_Octhet then
        DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    end
    RemoveLocation(LastDestantion)
    ForForce(udg_Bots, AddPlayers)
    TimerStart(udg_PlayerGet1, 1.25 * AiRepeat / 5, true, nil)
end
--??????
--===========================================================================
function InitTrig_PereborPlayerForArmy()
    gg_trg_PereborPlayerForArmy=CreateTrigger()
    DisableTrigger(gg_trg_PereborPlayerForArmy)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborPlayerForArmy, udg_TimerSmall2)
    TriggerAddAction(gg_trg_PereborPlayerForArmy, Trig_PereborPlayerForArmy_Actions)
end
--===========================================================================
-- Trigger: PerebobArmy Uni
--===========================================================================
-- ??????? ???????
function PlayerArmy()
    gInt=CountPlayersInForceBJ(udg_BotsActive)
    if gInt == 0 then
        PauseTimer(udg_PlayerGet1)
        ResumeTimer(udg_TimerSmall2)
        TimerStart(udg_TimerSmall2, 3 * AiRepeat / 5, false, nil)
        if udg_Octhet then
            DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
        end
    else
            --?????? ????????? ????
        gPlayer=ForcePickRandomPlayer(udg_BotsActive)
        local pi_army = GetPlayerId(gPlayer)
        if not (AiData[pi_army][StringHash("Log_PlayerArmy")] or false) then
            AiData[pi_army][StringHash("Log_PlayerArmy")] = true
            ProbeLogWrite("[AI] PlayerArmy processing pi=" .. tostring(pi_army) .. " race=" .. tostring(AiRace[pi_army]))
        end
        ForceRemovePlayer(udg_BotsActive, gPlayer)
        -- Brain seam: bots with an active brain go through AiBrainArmyTick;
        -- everyone else (default) runs the unchanged swarm path. Body lives in
        -- AiArmyLegacyTick (83_ai_brain.lua). See AI_BRAIN_DESIGN.md.
        if AiBrainEnabled(pi_army) then
            AiBrainArmyTick(pi_army, gPlayer)
        else
            AiArmyLegacyTick(gPlayer)
        end
    end
    
    
end
--===========================================================================
function InitTrig_PerebobArmy_Uni()
    gg_trg_PerebobArmy_Uni=CreateTrigger()
    DisableTrigger(gg_trg_PerebobArmy_Uni)
    TriggerRegisterTimerExpireEvent(gg_trg_PerebobArmy_Uni, udg_PlayerGet1)
    TriggerAddAction(gg_trg_PerebobArmy_Uni, PlayerArmy)
end
--===========================================================================
-- Trigger: PereborPlayerForNavy
--===========================================================================
function AddPlayers3()
    ForceAddPlayer(udg_BotsActiveN, GetEnumPlayer())
end
--??????? ???? ???????? ?????? ??????, ????? ????, ????????
function Trig_PereborPlayerForNavy_Actions()
    PauseTimer(udg_TimerSmall4)
    if not (AiData[-1][StringHash("TickLog_TimerSmall4")] or false) then
        AiData[-1][StringHash("TickLog_TimerSmall4")] = true
        ProbeLogWrite("[AI] PereborPlayerForNavy FIRST TICK")
    end
    if udg_Octhet then
    DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    end
    
    
    
    
    ForForce(udg_Bots, AddPlayers3)
    TimerStart(udg_PlayerGet4, 3.5 * AiRepeat / 5, true, nil)
end
--??????
--===========================================================================
function InitTrig_PereborPlayerForNavy()
    gg_trg_PereborPlayerForNavy=CreateTrigger()
    DisableTrigger(gg_trg_PereborPlayerForNavy)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborPlayerForNavy, udg_TimerSmall4)
    TriggerAddAction(gg_trg_PereborPlayerForNavy, Trig_PereborPlayerForNavy_Actions)
end
--===========================================================================
-- Trigger: PerebobNavy
--===========================================================================
function PlayerNavy()
    local l__gGroup= CreateGroup()
    local p= nil
    local u
    local id
    local i
    local i2
    --???????
    
    --?????? ????????? ?????
    --????? ????? ??????
    
    if CountPlayersInForceBJ(udg_BotsActiveN) == 0 then
        PauseTimer(udg_PlayerGet4)
        ResumeTimer(udg_TimerSmall4)
        TimerStart(udg_TimerSmall4, 7 * AiRepeat / 5, false, nil)
        if udg_Octhet then
            DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
        end
    else
        
        p=ForcePickRandomPlayer(udg_BotsActiveN)
        local pi_navy = GetPlayerId(p)
        if not (AiData[pi_navy][StringHash("Log_PlayerNavy")] or false) then
            AiData[pi_navy][StringHash("Log_PlayerNavy")] = true
            ProbeLogWrite("[AI] PlayerNavy processing pi=" .. tostring(pi_navy) .. " race=" .. tostring(AiRace[pi_navy]))
        end
        --call BJDebugMsg(""+GetPlayerName(p))
        ForceRemovePlayer(udg_BotsActiveN, p)
        
        
        CheckPlayer=p
        LazyCount=0
        GroupEnumUnitsOfPlayer(l__gGroup, p, B_LazyN)
        --call BJDebugMsg(""+I2S(LazyCount))
        if FirstOfGroup(l__gGroup) ~= nil then
            --call BJDebugMsg(""+I2S(LazyCount))
            
            i=1
            while true do
        u=BlzGroupUnitAt(l__gGroup, GetRandomInt(0, LazyCount - 1))
                if i > AiMass or u == nil then break end
                
                id=GetUnitTypeId(u)
                GroupRemoveUnit(l__gGroup, u)
                LazyCount=LazyCount - 1
                i=i + 1
                --if id=='h00Y' or id=='h00Z' or id == 'h06W'  or id == 'h0DM'  or id == 'h06V' or id == 'h06X' or id == 'n079' then
                    udg_LocalUnit3=u
                    TryAttackN()
                --endif
            end
        end
        
    end
    u=nil
end
--===========================================================================
function InitTrig_PerebobNavy()
    gg_trg_PerebobNavy=CreateTrigger()
    DisableTrigger(gg_trg_PerebobNavy)
    TriggerRegisterTimerExpireEvent(gg_trg_PerebobNavy, udg_PlayerGet4)
    TriggerAddAction(gg_trg_PerebobNavy, PlayerNavy)
end
--===========================================================================
-- Trigger: PereborBuildings
--===========================================================================
function Trig_PereborBuildings_Code_Func002A()
    gPlayer=GetEnumPlayer()
    
    udg_LocalInteger2=GetPlayerId(gPlayer)
    gPi=GetPlayerId(gPlayer)
    Counter=0
    -- Reconcile g_AiCounts with actual Ai_units (drift guard for morph races like Ents)
    local syncTick = AiData[gPi][StringHash("SyncTick")] or 0
    if Counter == 0 and (syncTick % 3) == 0 then
        pcall(function() AiSyncCounts(gPi) end)
    end
    AiData[gPi][StringHash("SyncTick")] = syncTick + 1
    GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_OnlyNeaded)
    local numberCount = AiData[gPi][StringHash("Number")] or 0
    -- ??????? ???? 0 ??? ????? ??????
    if FirstOfGroup(gGroup) == nil then
        if not (AiData[gPi][StringHash("Log_PereborNoBld")] or false) then
            AiData[gPi][StringHash("Log_PereborNoBld")] = true
            -- Manual scan of Ai_buildings group
            local bldGrp = udg_Ai_buildings[gPi]
            local bldOk, bldErr = pcall(function()
                local manualCount = 0
                local manualU = FirstOfGroup(bldGrp)
                while manualU ~= nil do
                    manualCount = manualCount + 1
                    local uid = GetUnitTypeId(manualU)
                    local alive = UnitAlive(manualU)
                    GroupRemoveUnit(bldGrp, manualU)
                    manualU = FirstOfGroup(bldGrp)
                end
                if manualCount == 0 then
                end
            end)
            if not bldOk then
            end
        end
        if udg_Octhet then
            DisplayTimedTextFromPlayer(gPlayer, 0, 0, 4, GetPlayerName(gPlayer) .. " - ")
        end
        if gGroup == nil then
            gGroup=CreateGroup()
            DisplayTimedTextFromPlayer(gPlayer, 0, 0, 4, GetPlayerName(gPlayer) .. " - ")
        end
        return
    elseif numberCount > AiLimit then
        if not (AiData[gPi][StringHash("Log_PereborOverLimit")] or false) then
            AiData[gPi][StringHash("Log_PereborOverLimit")] = true
        end
        if udg_Octhet then
            DisplayTimedTextFromPlayer(gPlayer, 0, 0, 4, GetPlayerName(gPlayer) .. " - ")
        end
        return
    end
    
    if not (AiData[gPi][StringHash("Log_PereborWorking")] or false) then
        AiData[gPi][StringHash("Log_PereborWorking")] = true
    end
    --?????????? ?????? ??????, ??????? ???? ?????? 
       
    bj_forLoopAIndex=1
    bj_forLoopAIndexEnd=8
    while true do
        if bj_forLoopAIndex > bj_forLoopAIndexEnd or FirstOfGroup(gGroup) == nil then break end
        gUnit=BlzGroupUnitAt(gGroup, GetRandomInt(0, Counter - 1))
        GroupRemoveUnit(gGroup, gUnit)
        Counter=Counter - 1
        gId=GetUnitTypeId(gUnit)
        
        AiDispatchPerebor(gId, gPi, gUnit)
        bj_forLoopAIndex=bj_forLoopAIndex + 1
    end
    
end
function Trig_PereborBuildings_Actions()
    g_AiOrdered = {}
    PauseTimer(udg_TimerSmall3)
    if not (AiData[-1][StringHash("TickLog_TimerSmall3")] or false) then
        AiData[-1][StringHash("TickLog_TimerSmall3")] = true
        ProbeLogWrite("[AI] PereborBuildings FIRST TICK")
    end
    if udg_Octhet then
        DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    end
    ForForce(udg_Bots, Trig_PereborBuildings_Code_Func002A)
    if udg_Octhet then
        DisplayTimedTextFromPlayer(Player(0), 0, 0, 4, "")
    end
    TimerStart(udg_TimerSmall3, 8.50 * AiRepeat / 5, false, nil)
end
--===========================================================================
function InitTrig_PereborBuildings()
    gg_trg_PereborBuildings=CreateTrigger()
    DisableTrigger(gg_trg_PereborBuildings)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborBuildings, udg_TimerSmall3)
    TriggerAddAction(gg_trg_PereborBuildings, Trig_PereborBuildings_Actions)
end
--===========================================================================
-- Trigger: PereborNavalBases
--===========================================================================
function PereborNavalb()
    local p= GetEnumPlayer()
    local pi
    local id
    local i
    local u
    
    udg_LocalInteger2=GetPlayerId(GetEnumPlayer())
    pi=GetPlayerId(p)
    
    Counter=0
    GroupEnumUnitsOfPlayer(gGroup, p, B_NavalBases)
    i=AiData[pi][StringHash("NumberN")] or 0
    -- ??????? ???? 0 ??? ?????? ????? ?????
    if FirstOfGroup(gGroup) == nil then
        if udg_Octhet then
            DisplayTimedTextFromPlayer(p, 0, 0, 4, GetPlayerName(p) .. "0")
        end
        
        u=nil
        return
        
    elseif i > (AiData[pi][StringHash("Number")] or 0) / 3 then
        if udg_Octhet then
            DisplayTimedTextFromPlayer(p, 0, 0, 4, GetPlayerName(p) .. "")
        end
        
        u=nil
        return
    end
    
    bj_forLoopAIndex=1
    bj_forLoopAIndexEnd=6
    while true do
        
        if bj_forLoopAIndex > bj_forLoopAIndexEnd or FirstOfGroup(gGroup) == nil or GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) < 2000 then break end
        u=BlzGroupUnitAt(gGroup, GetRandomInt(0, Counter - 1))
        Counter=Counter - 1
       -- call DisplayTimedTextFromPlayer(p,0,0,4, GetUnitName(u))
        GroupRemoveUnit(gGroup, u)
        id=GetUnitTypeId(u)
          
        -- ?????
        AiDispatchNaval(u, pi)
        
        bj_forLoopAIndex=bj_forLoopAIndex + 1
    end
    
end
function Trig_PereborNavalBases_Actions()
    ForForce(udg_Bots, PereborNavalb)
end
--===========================================================================
function InitTrig_PereborNavalBases()
    gg_trg_PereborNavalBases=CreateTrigger()
    DisableTrigger(gg_trg_PereborNavalBases)
    TriggerRegisterTimerExpireEvent(gg_trg_PereborNavalBases, udg_TimerSmall3)
    TriggerAddAction(gg_trg_PereborNavalBases, Trig_PereborNavalBases_Actions)
end
--===========================================================================
-- Trigger: AndResearch
--===========================================================================
function Trig_AndResearch_Conditions()
    gPi=GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    return udg_AiControl[gPi]
end
function Trig_AndResearch_Actions()
    Grades[gPi]=Grades[gPi] + 1
end
--===========================================================================
function InitTrig_AndResearch()
    gg_trg_AndResearch=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AndResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AndResearch, Condition(Trig_AndResearch_Conditions))
    TriggerAddAction(gg_trg_AndResearch, Trig_AndResearch_Actions)
end
--===========================================================================
-- Trigger: Strateg
--
-- AiData
--===========================================================================
function ZahType()
    local u= GetEnumUnit()
    local pi= GetPlayerId(GetOwningPlayer(u))
    local id= GetUnitTypeId(u)
    --??? ?????
    if IsUnitInGroup(u, udg_ZahvatBuildings) then
        udg_LocalInteger3=udg_LocalInteger3 + 8
    else
    AiDispatchStrategEC(id, pi)
    end
end
function Strateg()
    local i= 0
    local r= 0
    local p= GetEnumPlayer()
    local pi= GetPlayerId(p)
    if not (AiData[pi][StringHash("Log_Strateg")] or false) then
        AiData[pi][StringHash("Log_Strateg")] = true
        ProbeLogWrite("[AI] Strateg processing pi=" .. tostring(pi) .. " race=" .. tostring(AiRace[pi]))
    end
    
    
    -- ?????? ????? ? ?????
    udg_LocalInteger3=0
    GroupEnumUnitsOfPlayer(gGroup, p, nil)
    ForGroup(gGroup, ZahType)
    GroupClear(gGroup)
    i=udg_LocalInteger3
    --????????
    
    
    --???? ?? ????????
    
    AdjustPlayerStateSimpleBJ(p, PLAYER_STATE_RESOURCE_GOLD, 500 + i * 9 * AiMoney) -- -(AiData[pi][StringHash("Number")] or 0)*10 )
    AdjustPlayerStateSimpleBJ(p, PLAYER_STATE_RESOURCE_LUMBER, 250 + i * 5 * AiMoney)
    
    --call DisplayTimedTextFromPlayer(Player(0),0,0,4,(GetPlayerName(p)+""+I2S(GetPlayerId(p))))
    --call DisplayTimedTextFromPlayer(Player(0),0,0,4,I2S(i))
    
    -- ??????????? ??????? ????????????? ????? ? ??????
    SetUnitAbilityLevel(BonusUnit[pi], FourCC('aib0'), IMinBJ(R2I(i / 50 + 1), 10))
    SetUnitAbilityLevel(BonusUnit[pi], FourCC('aib1'), IMinBJ(R2I(i / 50 + 1), 10))
    --call BJDebugMsg(""+GetUnitName(BonusUnit[pi])+""+I2S(i)+""+I2S(IMinBJ( R2I(i/10),4)))
    
    
    
    AiDispatchStrateg(i, pi, p)
   
    
    
    
    --????????? ??? - ??? ?????? ???????, ??? ?????? ???????
    r=0
    while true do
        if r > i / 55 then break end
        if FirstOfGroup(AiUnitsToPort[pi]) ~= nil then
            TryPort_pi=pi
            TryPort()
            
        end
        r=r + 1
    end
end
function Trig_Strateg_Actions()
    
    if not (AiData[-1][StringHash("TickLog_Strateg")] or false) then
        AiData[-1][StringHash("TickLog_Strateg")] = true
        ProbeLogWrite("[AI] Strateg FIRST TICK")
    end
    if udg_Octhet then
        DisplayTimedTextFromPlayer(GetEnumPlayer(), 0, 0, 4, "")
    end
    
    ForForce(udg_Bots, Strateg)
    if udg_Octhet then
        DisplayTimedTextFromPlayer(GetEnumPlayer(), 0, 0, 4, "")
    end
end
--===========================================================================
function InitTrig_Strateg()
    gg_trg_Strateg=CreateTrigger()
    DisableTrigger(gg_trg_Strateg)
    TriggerRegisterTimerExpireEvent(gg_trg_Strateg, udg_AiTimerStrateg)
    TriggerAddAction(gg_trg_Strateg, Trig_Strateg_Actions)
end
--===========================================================================
-- Trigger: SargerasTemple
--===========================================================================
function Trig_SargerasTemple_Conditions()
    return udg_AiControl[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
function Trig_SargerasTemple_Actions()
    SetUnitOwner(gg_unit_h0BA_0361, Player(PLAYER_NEUTRAL_AGGRESSIVE), true)
    DisableTrigger(gg_trg_SargerasTemple)
end
--===========================================================================
function InitTrig_SargerasTemple()
    gg_trg_SargerasTemple=CreateTrigger()
    DisableTrigger(gg_trg_SargerasTemple)
    TriggerRegisterUnitInRangeSimple(gg_trg_SargerasTemple, 1000.00, gg_unit_h0BA_0361)
    TriggerAddCondition(gg_trg_SargerasTemple, Condition(Trig_SargerasTemple_Conditions))
    TriggerAddAction(gg_trg_SargerasTemple, Trig_SargerasTemple_Actions)
end
--===========================================================================
-- Trigger: AttackerAi
--
-- IssuePointOrderLoc
-- IssueTargetOrder
--===========================================================================
function Trig_AttackerAi_Conditions()
    gAttacker=GetAttacker()
    gPlayer=GetOwningPlayer(gAttacker)
    gPi=GetPlayerId(gPlayer)
    return udg_AiControl[gPi]
end
function Trig_AttackerAi_Actions()
    local id= GetUnitTypeId(gAttacker)
    
    gTarget=GetTriggerUnit()
    AiDispatchAttacker(id, gAttacker, gTarget, gPlayer)
end
--===========================================================================
function InitTrig_AttackerAi()
    gg_trg_AttackerAi=CreateTrigger()
    DisableTrigger(gg_trg_AttackerAi)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AttackerAi, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_AttackerAi, Condition(Trig_AttackerAi_Conditions))
    TriggerAddAction(gg_trg_AttackerAi, Trig_AttackerAi_Actions)
end
--===========================================================================
-- Trigger: AttackedAI
--
-- IssuePointOrderLoc
-- IssueTargetOrder
--===========================================================================
function Trig_AttackedAI_Conditions()
    gAttacked=GetTriggerUnit()
    gPi=GetPlayerId(GetOwningPlayer(gAttacked))
    return udg_AiControl[gPi]
end
function Trig_AttackedAI_Actions()
    if IsUnitInGroup(gAttacked, udg_ZahvatBuildings) or IsUnitInGroup(gAttacked, AiUnitsToPort[gPi]) then
        if Random(1 , 30) then
            PortTo(gAttacked)
        end
    elseif IsUnitInGroup(gAttacked, udg_StolicaGroups) then
        if Random(1 , 10) and GetUnitState(gAttacked, UNIT_STATE_LIFE) > 7500 then
            PortToFast(gAttacked)
        elseif Random(1 , 5) then
            PortToFast(gAttacked)
        end
        
    elseif IsUnitType(gAttacked, UNIT_TYPE_STRUCTURE) then
        if Random(1 , 5) and IsUnitInGroup(gAttacked, AiCapitalBuildigs[gPi]) then
            PortToFast(gAttacked)
        elseif Random(1 , 30) then
            PortTo(gAttacked)
        end
    else
        -- --------------- ???? ?????
    AiDispatchAttacked(gAttacked, gPi)
    end
end
--===========================================================================
function InitTrig_AttackedAI()
    gg_trg_AttackedAI=CreateTrigger()
    DisableTrigger(gg_trg_AttackedAI)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AttackedAI, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_AttackedAI, Condition(Trig_AttackedAI_Conditions))
    TriggerAddAction(gg_trg_AttackedAI, Trig_AttackedAI_Actions)
end
--===========================================================================
-- Trigger: GetLvl
--===========================================================================
function Trig_GetLvl_Conditions()
    return udg_AiControl[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
function Trig_GetLvl_Actions()
    local u= GetTriggerUnit()
    local i
    local pi= GetPlayerId(GetOwningPlayer(u))
    
    
    
    AiDispatchGetLvl(u, pi)
    u=nil
end
--===========================================================================
function InitTrig_GetLvl()
    gg_trg_GetLvl=CreateTrigger()
    DisableTrigger(gg_trg_GetLvl)
    TriggerRegisterAnyUnitEventBJ(gg_trg_GetLvl, EVENT_PLAYER_HERO_LEVEL)
    TriggerAddCondition(gg_trg_GetLvl, Condition(Trig_GetLvl_Conditions))
    TriggerAddAction(gg_trg_GetLvl, Trig_GetLvl_Actions)
end
--===========================================================================
-- Trigger: Revive
--===========================================================================
function Trig_Revive_Conditions()
    gUnit=GetRevivableUnit()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return udg_AiControl[gPi]
end
function Trig_Revive_Actions()
    local u= gUnit
    --call ReviveHeroTimed(gUnit,GetUnitLevel(gUnit)*7)
    TriggerSleepAction(GetUnitLevel(gUnit) * 7)
    GroupEnumUnitsOfPlayer(gGroup, GetOwningPlayer(u), Altars)
    if FirstOfGroup(gGroup) ~= nil then
        gUnit2=GroupPickRandomUnit2(gGroup)
        ReviveHero(u, GetUnitX(gUnit2), GetUnitY(gUnit2), true)
    end
    
end
--===========================================================================
function InitTrig_Revive()
    gg_trg_Revive=CreateTrigger()
    DisableTrigger(gg_trg_Revive)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Revive, EVENT_PLAYER_HERO_REVIVABLE)
    TriggerAddCondition(gg_trg_Revive, Condition(Trig_Revive_Conditions))
    TriggerAddAction(gg_trg_Revive, Trig_Revive_Actions)
end
--===========================================================================
-- Trigger: JoinAll
--===========================================================================
function Trig_JoinAll_Conditions()
    gUnit=GetTrainedUnit()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return udg_AiControl[gPi]
end
function Trig_JoinAll_Actions()
    aiUnitJoins(gUnit , gPi)
end
--===========================================================================
function InitTrig_JoinAll()
    gg_trg_JoinAll=CreateTrigger()
    DisableTrigger(gg_trg_JoinAll)
    TriggerRegisterAnyUnitEventBJ(gg_trg_JoinAll, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_JoinAll, Condition(Trig_JoinAll_Conditions))
    TriggerAddAction(gg_trg_JoinAll, Trig_JoinAll_Actions)
end
--===========================================================================
-- Trigger: SellAl
--===========================================================================
function Trig_SellAl_Conditions()
    gPi=GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    return udg_AiControl[gPi]
end
function Trig_SellAl_Actions()
    aiUnitJoins(GetSoldUnit() , gPi)
end
--===========================================================================
function InitTrig_SellAl()
    gg_trg_SellAl=CreateTrigger()
    DisableTrigger(gg_trg_SellAl)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SellAl, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_SellAl, Condition(Trig_SellAl_Conditions))
    TriggerAddAction(gg_trg_SellAl, Trig_SellAl_Actions)
end
--===========================================================================
-- Trigger: JoinBuildings
--===========================================================================
function Trig_JoinBuildings_Conditions()
    gTriggerUnit=GetTriggerUnit()
    gPlayer=GetOwningPlayer(gTriggerUnit)
    gPi=GetPlayerId(gPlayer)
    return udg_AiControl[gPi]
end
---@param structure unit
---@param pi integer
function aiUnitBuildingJoins(structure, pi)
    local id= GetUnitTypeId(structure)
    GroupAddUnit(udg_Ai_buildings[pi], structure)
    GroupAddUnit(udg_Ai_units[pi], structure)
    NumberAdd(pi , id)
    if playerCapital[pi] ~= nil and DistanceBetweenUnits(playerCapital[pi] , structure) <= 3000 then
        GroupAddUnit(AiCapitalBuildigs[pi], structure)
    end
end
function Trig_JoinBuildings_Actions()
    gConstructingStructure=GetConstructingStructure()
    aiUnitBuildingJoins(gConstructingStructure , gPi)
end
--===========================================================================
function InitTrig_JoinBuildings()
    gg_trg_JoinBuildings=CreateTrigger()
    DisableTrigger(gg_trg_JoinBuildings)
    TriggerRegisterAnyUnitEventBJ(gg_trg_JoinBuildings, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_JoinBuildings, Condition(Trig_JoinBuildings_Conditions))
    TriggerAddAction(gg_trg_JoinBuildings, Trig_JoinBuildings_Actions)
end
--===========================================================================
-- Trigger: UpgradeBuildings
--===========================================================================
function Trig_UpgradeBuildings_Conditions()
    gUnit=GetTriggerUnit()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return udg_AiControl[gPi]
end
function Trig_UpgradeBuildings_Actions()
    gId=GetUnitTypeId(gUnit)
    NumberAdd(gPi , gId)
    AiDispatchUpgrade(gPi, gId)
    
end
--===========================================================================
function InitTrig_UpgradeBuildings()
    gg_trg_UpgradeBuildings=CreateTrigger()
    DisableTrigger(gg_trg_UpgradeBuildings)
    TriggerRegisterAnyUnitEventBJ(gg_trg_UpgradeBuildings, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_UpgradeBuildings, Condition(Trig_UpgradeBuildings_Conditions))
    TriggerAddAction(gg_trg_UpgradeBuildings, Trig_UpgradeBuildings_Actions)
end
--===========================================================================
-- Trigger: EndBuilding
--===========================================================================
function Trig_EndBuilding_Conditions()
    gUnit=GetTriggerUnit()
    gPlayer=GetOwningPlayer(gUnit)
    return udg_AiControl[GetPlayerId(gPlayer)]
end
function Trig_EndBuilding_Actions()
    local finishedBuilding = gUnit
    
    --set checkPlayer = gPlayer
    GroupEnumUnitsInRange(gGroup, GetUnitX(finishedBuilding), GetUnitY(finishedBuilding), 300.00, B_Worker)
    gUnit=FirstOfGroup(gGroup)
    if gUnit ~= nil then
        TryBuild_u=gUnit
        TryBuild()
    end
    
    -- Nerubs cocoon: upgrade to real building
    if GetUnitTypeId(finishedBuilding) == FourCC('u019') then
        local pi = GetPlayerId(gPlayer)
        local target = AiData[pi]["upgradeCocoon"]
        if target ~= nil and target ~= 0 then
            IssueImmediateOrderById(finishedBuilding, target)
            AiData[pi]["upgradeCocoon"] = nil
        end
    end
end
--===========================================================================
function InitTrig_EndBuilding()
    gg_trg_EndBuilding=CreateTrigger()
    DisableTrigger(gg_trg_EndBuilding)
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndBuilding, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_EndBuilding, Condition(Trig_EndBuilding_Conditions))
    TriggerAddAction(gg_trg_EndBuilding, Trig_EndBuilding_Actions)
end
--===========================================================================
-- Trigger: Leave Army U
--===========================================================================
function Trig_Leave_Army_U_Conditions()
    gUnit=GetTriggerUnit()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return IsUnitInGroup(gUnit, udg_Ai_army[gPi]) and not IsUnitType(gUnit, UNIT_TYPE_HERO)
end
function Trig_Leave_Army_U_Actions()
    GroupRemoveUnit(udg_Ai_army[gPi], gUnit)
    GroupRemoveUnit(udg_Ai_units[gPi], gUnit)
    NumberRem(gPi , GetUnitTypeId(gUnit))
    NumberRem(gPi , StringHash("Number"))
    
    
    SetUnitLifeBJ(gUnit, 0)
    if not IsUnitInGroup(gUnit, DeadGroupAi) then
        GroupAddUnit(DeadGroupAi, gUnit)
        TriggerRegisterUnitStateEvent(gg_trg_UnitReviveAi, gUnit, UNIT_STATE_LIFE, GREATER_THAN, 0.01)
    end
    
end
--===========================================================================
function InitTrig_Leave_Army_U()
    gg_trg_Leave_Army_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Army_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Army_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Army_U, Condition(Trig_Leave_Army_U_Conditions))
    TriggerAddAction(gg_trg_Leave_Army_U, Trig_Leave_Army_U_Actions)
end
--===========================================================================
-- Trigger: Leave Guard
--===========================================================================
function Trig_Leave_Guard_Conditions()
    gUnit=GetTriggerUnit()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return IsUnitInGroup(gUnit, AiCapitalGuard[gPi]) and not IsUnitType(gUnit, UNIT_TYPE_HERO)
end
function Trig_Leave_Guard_Actions()
    GroupRemoveUnit(AiCapitalGuard[gPi], gUnit)
    GroupRemoveUnit(udg_Ai_units[gPi], gUnit)
    NumberRem(gPi , GetUnitTypeId(gUnit))
    NumberRem(gPi , StringHash("NumberGuard"))
    
    
    SetUnitLifeBJ(gUnit, 0)
    if not IsUnitInGroup(gUnit, DeadGroupAi) then
        GroupAddUnit(DeadGroupAi, gUnit)
        TriggerRegisterUnitStateEvent(gg_trg_UnitReviveAi, gUnit, UNIT_STATE_LIFE, GREATER_THAN, 0.01)
    end
    
end
--===========================================================================
function InitTrig_Leave_Guard()
    gg_trg_Leave_Guard=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Guard)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Guard, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Guard, Condition(Trig_Leave_Guard_Conditions))
    TriggerAddAction(gg_trg_Leave_Guard, Trig_Leave_Guard_Actions)
end
--===========================================================================
-- Trigger: Leave Navy U
--===========================================================================
function Trig_Leave_Navy_U_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Ai_navy[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
function Trig_Leave_Navy_U_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    GroupRemoveUnit(udg_Ai_navy[pi], GetTriggerUnit())
    NumberRem(pi , GetUnitTypeId(GetTriggerUnit()))
    NumberRem(pi , StringHash("NumberN"))
end
--===========================================================================
function InitTrig_Leave_Navy_U()
    gg_trg_Leave_Navy_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Navy_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Navy_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Navy_U, Condition(Trig_Leave_Navy_U_Conditions))
    TriggerAddAction(gg_trg_Leave_Navy_U, Trig_Leave_Navy_U_Actions)
end
--===========================================================================
-- Trigger: Leave Harvest U
--===========================================================================
function Trig_Leave_Harvest_U_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Ai_harvest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
function Trig_Leave_Harvest_U_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_harvest[pi])
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_units[pi])
    NumberRem(pi , GetUnitTypeId(GetTriggerUnit()))
    NumberRem(pi , StringHash("Number"))
    AiData[pi][StringHash("HV")] = (AiData[pi][StringHash("HV")] or 0) - 1
end
--===========================================================================
function InitTrig_Leave_Harvest_U()
    gg_trg_Leave_Harvest_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Harvest_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Harvest_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Harvest_U, Condition(Trig_Leave_Harvest_U_Conditions))
    TriggerAddAction(gg_trg_Leave_Harvest_U, Trig_Leave_Harvest_U_Actions)
end
--===========================================================================
-- Trigger: Leave Builders U
--===========================================================================
function Trig_Leave_Builders_U_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Ai_builders[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
function Trig_Leave_Builders_U_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_builders[pi])
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_units[pi])
    NumberRem(pi , GetUnitTypeId(GetTriggerUnit()))
    NumberRem(pi , StringHash("Number"))
    --call AiData[pi][StringHash("HV")] = (AiData[pi][StringHash("HV")] or 0)-1
end
--===========================================================================
function InitTrig_Leave_Builders_U()
    gg_trg_Leave_Builders_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Builders_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Builders_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Builders_U, Condition(Trig_Leave_Builders_U_Conditions))
    TriggerAddAction(gg_trg_Leave_Builders_U, Trig_Leave_Builders_U_Actions)
end
--===========================================================================
-- Trigger: Leave BuildersT U
--===========================================================================
function Trig_Leave_BuildersT_U_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Ai_buildersT[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
function Trig_Leave_BuildersT_U_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_buildersT[pi])
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_units[pi])
    NumberRem(pi , GetUnitTypeId(GetTriggerUnit()))
    NumberRem(pi , StringHash("Number"))
    
    AiData[pi][StringHash("T")] = (AiData[pi][StringHash("T")] or 0) - 1
end
--===========================================================================
function InitTrig_Leave_BuildersT_U()
    gg_trg_Leave_BuildersT_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_BuildersT_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_BuildersT_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_BuildersT_U, Condition(Trig_Leave_BuildersT_U_Conditions))
    TriggerAddAction(gg_trg_Leave_BuildersT_U, Trig_Leave_BuildersT_U_Actions)
end
--===========================================================================
-- Trigger: Leave Buildings U
--===========================================================================
function Trig_Leave_Buildings_U_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), udg_Ai_buildings[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
function Trig_Leave_Buildings_U_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_buildings[pi])
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_Ai_units[pi])
    NumberRem(pi , GetUnitTypeId(GetTriggerUnit()))
    --call NumberRem(pi,StringHash("Number"))
end
--===========================================================================
function InitTrig_Leave_Buildings_U()
    gg_trg_Leave_Buildings_U=CreateTrigger()
    DisableTrigger(gg_trg_Leave_Buildings_U)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Leave_Buildings_U, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Leave_Buildings_U, Condition(Trig_Leave_Buildings_U_Conditions))
    TriggerAddAction(gg_trg_Leave_Buildings_U, Trig_Leave_Buildings_U_Actions)
end
--===========================================================================
-- Trigger: UnitReviveAi
--===========================================================================
function Trig_UnitReviveAi_Conditions()
    gUnit=GetTriggerUnit()
    return UnitAlive(gUnit) and not IsUnitType(gUnit, UNIT_TYPE_SUMMONED)
end
function Trig_UnitReviveAi_Actions()
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    
    GroupRemoveUnit(AiCapitalGuard[gPi], gUnit)
    aiUnitJoins(gUnit , gPi)
end
--===========================================================================
function InitTrig_UnitReviveAi()
    gg_trg_UnitReviveAi=CreateTrigger()
    TriggerAddCondition(gg_trg_UnitReviveAi, Condition(Trig_UnitReviveAi_Conditions))
    TriggerAddAction(gg_trg_UnitReviveAi, Trig_UnitReviveAi_Actions)
end
--===========================================================================
-- Trigger: MainFloatUnits
--===========================================================================
function isShip()
    return id == FourCC('h00X') or id == FourCC('h00Y') or id == FourCC('h00Z') or id == FourCC('h0CZ') or id == FourCC('h0D2') or id == FourCC('h0D0') or id == FourCC('h0D5') or id == FourCC('h0D4') or id == FourCC('h0D6') or id == FourCC('h0DB') or id == FourCC('h0D9') or id == FourCC('h0DA') or id == FourCC('h0E6') or id == FourCC('h0E5') or id == FourCC('h0E8') or id == FourCC('h03L') or id == FourCC('h03K') or id == FourCC('h06W') or id == FourCC('h0DM') or id == FourCC('h06V') or id == FourCC('h06X') --???????
    
end
function aiShipJoins()
    GroupAddUnit(Navy, u)
    GroupAddUnit(udg_Ai_navy[pi], u)
end
function Trig_MainFloatUnits_Conditions()
    gUnit=GetTrainedUnit()
    gId=GetUnitTypeId(gUnit)
    return isShip(gId)
end
function Trig_MainFloatUnits_Actions()
    aiShipJoins(gUnit , GetPlayerId(GetOwningPlayer(gUnit)))
end
--===========================================================================
function InitTrig_MainFloatUnits()
    gg_trg_MainFloatUnits=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MainFloatUnits, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_MainFloatUnits, Condition(Trig_MainFloatUnits_Conditions))
    TriggerAddAction(gg_trg_MainFloatUnits, Trig_MainFloatUnits_Actions)
end
--===========================================================================
-- Trigger: MainFloatUnitsLeave
--===========================================================================
function Trig_MainFloatUnitsLeave_Conditions()
    gUnit=GetTriggerUnit()
    return IsUnitInGroup(gUnit, Navy)
end
function Trig_MainFloatUnitsLeave_Actions()
    GroupRemoveUnit(Navy, gUnit)
end
--===========================================================================
function InitTrig_MainFloatUnitsLeave()
    gg_trg_MainFloatUnitsLeave=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MainFloatUnitsLeave, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_MainFloatUnitsLeave, Condition(Trig_MainFloatUnitsLeave_Conditions))
    TriggerAddAction(gg_trg_MainFloatUnitsLeave, Trig_MainFloatUnitsLeave_Actions)
end
--===========================================================================
-- Trigger: PortUnits
--===========================================================================
function isNavalBase()
    return id == FourCC('h0D1') or id == FourCC('h0D8') or id == FourCC('h03R') or id == FourCC('h0D3') or id == FourCC('h0E7') or id == FourCC('h011') or id == FourCC('h0D7') or id == FourCC('u01A') or gId == FourCC('n04L') or gId == FourCC('h0HO') -- ????????? ??? ???? ??????
end
function Trig_PortUnits_Conditions()
    gUnit=GetConstructingStructure()
    return isNavalBase(GetUnitTypeId(gUnit))
end
function aiNavalBaseJoin()
    NumberAdd(GetPlayerId(GetOwningPlayer(u)) , StringHash("NumberPorts"))
    GroupAddUnit(Port, u)
end
function Trig_PortUnits_Actions()
    aiNavalBaseJoin(gUnit)
end
--===========================================================================
function InitTrig_PortUnits()
    gg_trg_PortUnits=CreateTrigger()
    DisableTrigger(gg_trg_PortUnits)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PortUnits, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_PortUnits, Condition(Trig_PortUnits_Conditions))
    TriggerAddAction(gg_trg_PortUnits, Trig_PortUnits_Actions)
end
--===========================================================================
-- Trigger: PortUnitLeave
--===========================================================================
function Trig_PortUnitLeave_Conditions()
    gUnit=GetTriggerUnit()
    return IsUnitInGroup(gUnit, Port)
end
function Trig_PortUnitLeave_Actions()
    NumberRem(GetPlayerId(GetOwningPlayer(gUnit)) , StringHash("NumberPorts"))
    GroupRemoveUnit(Port, gUnit)
end
--===========================================================================
function InitTrig_PortUnitLeave()
    gg_trg_PortUnitLeave=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PortUnitLeave, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_PortUnitLeave, Condition(Trig_PortUnitLeave_Conditions))
    TriggerAddAction(gg_trg_PortUnitLeave, Trig_PortUnitLeave_Actions)
end
--===========================================================================
-- Trigger: AiRep
--===========================================================================
function aiRep()
    if not udg_AiControl[pi] then
        return
    end
    
    
    -- ???????
    g_AiCounts[pi] = nil; AiData[(pi)] = nil -- INLINED!!
    
    GroupClear(udg_Ai_units[pi])
    GroupClear(udg_Ai_navy[pi])
    GroupClear(udg_Ai_army[pi])
    GroupClear(udg_Ai_buildersT[pi])
    GroupClear(udg_Ai_builders[pi])
    GroupClear(udg_Ai_harvest[pi])
    GroupClear(AiUnitsToPort[pi])
    
    -- ???????
    if gGroup == nil then
        gGroup=CreateGroup()
    end
    
    gPlayer=Player(pi)
    BJDebugMsg("" .. GetPlayerName(gPlayer))
    GroupEnumUnitsOfPlayer(gGroup, gPlayer, nil)
    while true do
        gUnit=FirstOfGroup(gGroup)
        if gUnit == nil then
            if true then break end
        end
        BJDebugMsg("" .. GetUnitName(gUnit))
        if GetUnitAbilityLevel(gUnit, gDummySpell) == 0 and not IsUnitType(gUnit, UNIT_TYPE_SUMMONED) then
            
            -- ???????? ? ???????
            if BlzIsUnitInvulnerable(gUnit) then -- GetUnitAbilityLevel(gUnit, FourCC('Bvul')) > 0 then
                BJDebugMsg("")
                gUnit=ReplaceUnit2(gUnit , GetUnitTypeId(gUnit) , bj_UNIT_STATE_METHOD_MAXIMUM)
                
            end
           
            gId=GetUnitTypeId(gUnit)
            --call NumberReset(pi,id)
            
            if IsUnitType(gUnit, UNIT_TYPE_STRUCTURE) then
                UnitSetConstructionProgress(gUnit, 100)
                
                if isNavalBase(gId) then
                    aiNavalBaseJoin(gUnit)
                end
                
                aiUnitBuildingJoins(gUnit , pi)
                if IsUnitInGroup(gUnit, udg_ZahvatBuildings) then
                    GroupAddUnit(AiUnitsToPort[pi], gUnit)
                end
            else
                
                if isShip(gId) then
                    aiShipJoins(gUnit , pi)
                end
                
                aiUnitJoins(gUnit , pi)
                if gId == FourCC('h07A') then -- ???-??
                   GroupAddUnit(AiUnitsToPort[pi], gUnit)
                end
            end
        
        
        
        end
        
        GroupRemoveUnit(gGroup, gUnit)
    end
    
end
function aiRepUnvul_act()
    gUnit=GetEnumUnit()
    if not IsUnitType(gUnit, UNIT_TYPE_STRUCTURE) then
        gUnit=ReplaceUnit2(gUnit , GetUnitTypeId(gUnit) , bj_UNIT_STATE_METHOD_RELATIVE)
    end
    
end
-- ??????? ?????
function aiRepUnvul()
    if not udg_AiControl[pi] then
        return
    end
    
    gPlayer=Player(pi)
    GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_FixUnvul)
    ForGroup(gGroup, aiRepUnvul_act)
    
end
function aiFixAll()
    local i= 0
    while true do
        if i >= 23 then break end
        
                
        aiRepUnvul(i)
        aiRep(i)
        
        DisplayTextToPlayer(Player(i), 0, 0, "")
        i=i + 1
    end
    
end
 
--===========================================================================
-- Trigger: TestgGroup
--===========================================================================
function Trig_TestgGroup_Actions()
    
    BJDebugMsg("")
    if gGroup == nil then
        BJDebugMsg("gGroup")
    end
    if gSubGroup == nil then
        BJDebugMsg("gSubGroup")
    end
    if gAllyGroup == nil then
        BJDebugMsg("gAllyGroup")
    end
end
--===========================================================================
function InitTrig_TestgGroup()
    gg_trg_TestgGroup=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_TestgGroup, Player(0), " - gGr", true)
    TriggerAddAction(gg_trg_TestgGroup, Trig_TestgGroup_Actions)
end
--===========================================================================
-- Trigger: AiRepTrigger
--===========================================================================
function Trig_AiRepTrigger_Actions()
    aiFixAll()
end
--===========================================================================
function InitTrig_AiRepTrigger()
    gg_trg_AiRepTrigger=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_AiRepTrigger, aiFixer)
    TriggerAddAction(gg_trg_AiRepTrigger, Trig_AiRepTrigger_Actions)
end
--===========================================================================
-- Trigger: AiRepCommand
--===========================================================================
function Trig_AiRepCommand_Actions()
    aiFixAll()
end
--===========================================================================
function InitTrig_AiRepCommand()
    gg_trg_AiRepCommand=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiRepCommand, Player(0), " - airep", true)
    TriggerAddAction(gg_trg_AiRepCommand, Trig_AiRepCommand_Actions)
end
--===========================================================================
-- Trigger: AiLogAll
--===========================================================================
function Trig_AiLogAll_Conditions()
    return S2I(SubStringBJ(GetEventPlayerChatString(), 6, 8)) >= 1 and S2I(SubStringBJ(GetEventPlayerChatString(), 6, 8)) <= 24
end
function aiNameGroup()
    gString=gString .. "" .. I2S(Counter) .. "." .. GetUnitName(GetEnumUnit())
    Counter=Counter + 1
    if ModuloInteger(Counter, 28) == 0 then
        BJDebugMsg(I2S(Counter) .. "" .. gString)
        gString=""
    end
end
function Trig_AiLogAll_Actions()
    gPi=S2I(SubStringBJ(GetEventPlayerChatString(), 6, 8)) - 1
    gPlayer=Player(gPi)
    --call ForGroup(gGroup,function )
    BJDebugMsg("" .. GetPlayerName(gPlayer))
    BJDebugMsg("")
    BJDebugMsg("Number" .. I2S(AiData[(gPi )][( StringHash("Number"))] or 0)) -- INLINED!!
    BJDebugMsg("NumberN" .. I2S(AiData[(gPi )][( StringHash("NumberN"))] or 0)) -- INLINED!!
    BJDebugMsg("NumberPorts" .. I2S(AiData[(gPi )][( StringHash("NumberPorts"))] or 0)) -- INLINED!!
    BJDebugMsg("NumberGuard" .. I2S(AiData[(gPi )][( StringHash("NumberGuard"))] or 0)) -- INLINED!!
    BJDebugMsg("T" .. I2S(AiData[(gPi )][( StringHash("T"))] or 0)) -- INLINED!!
    BJDebugMsg("HV" .. I2S(AiData[(gPi )][( StringHash("HV"))] or 0)) -- INLINED!!
    BJDebugMsg("")
    
    gString="Groupudg_Ai_army[pi]"
    Counter=0
    ForGroup(udg_Ai_army[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="Groupudg_Ai_navy[pi]"
    Counter=0
    ForGroup(udg_Ai_navy[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="GroupAiCapitalGuard[pi]"
    Counter=0
    ForGroup(AiCapitalGuard[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="Groupudg_Ai_builders[pi]"
        Counter=0
    ForGroup(udg_Ai_builders[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="Groupudg_Ai_buildersT[pi]"
    Counter=0
    ForGroup(udg_Ai_buildersT[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="Groupudg_Ai_harvest[pi]"
    Counter=0
    ForGroup(udg_Ai_harvest[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    
    gString="Groupudg_Ai_buildings[pi]"
    Counter=0
    ForGroup(udg_Ai_buildings[gPi], aiNameGroup)
    BJDebugMsg(I2S(Counter) .. "" .. gString)
    if gGroup == nil then
        BJDebugMsg("gGroup")
    end
    if gSubGroup == nil then
        BJDebugMsg("gSubGroup")
    end
    if gAllyGroup == nil then
        BJDebugMsg("gAllyGroup")
    end
    
    --call BJDebugMsg("1"+I2S(getAiCount(gPi,'ogre')))
    --call BJDebugMsg("2"+I2S(getAiCount(gPi,'ostr')))
    --call BJDebugMsg("T3"+I2S(getAiCount(gPi,'ofrt')))
    
end
--===========================================================================
function InitTrig_AiLogAll()
    gg_trg_AiLogAll=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AiLogAll, Player(0), " - chai", false)
    TriggerAddCondition(gg_trg_AiLogAll, Condition(Trig_AiLogAll_Conditions))
    TriggerAddAction(gg_trg_AiLogAll, Trig_AiLogAll_Actions)
end
--===========================================================================
-- Trigger: Spawn12Ai
--===========================================================================
function Trig_Spawn12Ai_Actions()
    BJDebugMsg("12")
    gInt=1
    while true do
        createAiPlayer(gInt)
        if gInt > 12 then break end
        gInt=gInt + 1
    end
    
end
--===========================================================================
function InitTrig_Spawn12Ai()
    gg_trg_Spawn12Ai=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Spawn12Ai, Player(0), "12ai", true)
    TriggerAddAction(gg_trg_Spawn12Ai, Trig_Spawn12Ai_Actions)
end
--===========================================================================
-- Trigger: PortalSell
--===========================================================================
function Trig_PortalSell_Conditions()
    return GetUnitTypeId(GetSoldUnit()) == FourCC('h0P0')
end
function Trig_PortalSell_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "web")
    RemoveUnit(GetSoldUnit())
end
--===========================================================================
function InitTrig_PortalSell()
    gg_trg_PortalSell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PortalSell, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_PortalSell, Condition(Trig_PortalSell_Conditions))
    TriggerAddAction(gg_trg_PortalSell, Trig_PortalSell_Actions)
end
--===========================================================================
-- Trigger: PortalFix
--===========================================================================
function Trig_PortalFix_Actions()
    WaygateSetDestinationLocBJ(gg_unit_n003_0020, GetRectCenter(gg_rct_UldamanOut))
    WaygateSetDestinationLocBJ(gg_unit_n003_0588, GetRectCenter(gg_rct_DalaranOut))
    WaygateSetDestinationLocBJ(gg_unit_n003_0126, GetRectCenter(gg_rct_NaxOut))
end
--===========================================================================
function InitTrig_PortalFix()
    gg_trg_PortalFix=CreateTrigger()
    TriggerAddAction(gg_trg_PortalFix, Trig_PortalFix_Actions)
end
--===========================================================================
-- Trigger: CheckNearCapitals
--===========================================================================
function CheckNearCapitals()
    local g= CreateGroup()
    local u= GetTriggerUnit()
    
    udg_LocalPlayer=GetOwningPlayer(city)
    GroupEnumUnitsInRange(g, GetUnitX(city), GetUnitY(city), 3050, CapitalOfEnemy)
    if FirstOfGroup(g) ~= nil then
        DisplayTextToPlayer(udg_LocalPlayer, 0, 0, "(3)")
        g=nil
        return false
    end
    
    
    
    
    DestroyGroup(g)
    g=nil
    return true
end
--===========================================================================
-- Trigger: PortalCommonFunction
--===========================================================================
function PortalConditions()
    return not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Sch5')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A001')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1M3')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A00A')) == 0
end
function TeleportUnitsEach()
    SetUnitPosition(GetEnumUnit(), GetRandomReal(GetRectMinX(gRect), GetRectMaxX(gRect)), GetRandomReal(GetRectMinY(gRect), GetRectMaxY(gRect)))
    RemoveLocation(gLoc)
    EnterGreen(GetEnumUnit())
end
---@param portal unit
---@param rect rect
---@param radius real
function TeleportUnits(portal, rect, radius)
    gLoc=GetUnitLoc(portal)
    gRect=rect
    GroupEnumUnitsInRangeOfLocCounted(gGroup, gLoc, radius, PortalConditions, 150)
    ForGroup(gGroup, TeleportUnitsEach)
    GroupClear(gGroup)
    RemoveLocation(gLoc)
end
-- ?? ??? ??? ????
function PortalConditionsED()
    return not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Sch5')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A001')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1M3')) == 0 and GetUnitTypeId(GetFilterUnit()) ~= FourCC('n01W') and GetUnitTypeId(GetFilterUnit()) ~= FourCC('n01X') and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1LR')) >= 1
end
---@param portal unit
---@param rect rect
---@param radius real
function TeleportUnitsED(portal, rect, radius)
    gLoc=GetUnitLoc(portal)
    gRect=rect
    GroupEnumUnitsInRangeOfLocCounted(gGroup, gLoc, radius, PortalConditionsED, 150)
    ForGroup(gGroup, TeleportUnitsEach)
    GroupClear(gGroup)
    RemoveLocation(gLoc)
end
--===========================================================================
-- Trigger: UndercityFromRin
--===========================================================================
function Trig_UndercityFromRin_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0044
end
function Trig_UndercityFromRin_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UndecityOutTop , 800)
end
--===========================================================================
function InitTrig_UndercityFromRin()
    gg_trg_UndercityFromRin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UndercityFromRin, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UndercityFromRin, Condition(Trig_UndercityFromRin_Conditions))
    TriggerAddAction(gg_trg_UndercityFromRin, Trig_UndercityFromRin_Actions)
end
--===========================================================================
-- Trigger: UndercityFromTopin
--===========================================================================
function Trig_UndercityFromTopin_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0046
end
function Trig_UndercityFromTopin_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UndecityOutBot , 800)
end
--===========================================================================
function InitTrig_UndercityFromTopin()
    gg_trg_UndercityFromTopin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UndercityFromTopin, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UndercityFromTopin, Condition(Trig_UndercityFromTopin_Conditions))
    TriggerAddAction(gg_trg_UndercityFromTopin, Trig_UndercityFromTopin_Actions)
end
--===========================================================================
-- Trigger: UndercityFromTopOut
--===========================================================================
function Trig_UndercityFromTopOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0050
end
function Trig_UndercityFromTopOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UndercityInR , 800)
end
--===========================================================================
function InitTrig_UndercityFromTopOut()
    gg_trg_UndercityFromTopOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UndercityFromTopOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UndercityFromTopOut, Condition(Trig_UndercityFromTopOut_Conditions))
    TriggerAddAction(gg_trg_UndercityFromTopOut, Trig_UndercityFromTopOut_Actions)
end
--===========================================================================
-- Trigger: UndercityFromBotOut
--===========================================================================
function Trig_UndercityFromBotOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0051
end
function Trig_UndercityFromBotOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UndercityInTop , 800)
end
--===========================================================================
function InitTrig_UndercityFromBotOut()
    gg_trg_UndercityFromBotOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UndercityFromBotOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UndercityFromBotOut, Condition(Trig_UndercityFromBotOut_Conditions))
    TriggerAddAction(gg_trg_UndercityFromBotOut, Trig_UndercityFromBotOut_Actions)
end
--===========================================================================
-- Trigger: OrgrimmarFromTopOut
--===========================================================================
function Trig_OrgrimmarFromTopOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0516
end
function Trig_OrgrimmarFromTopOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_OrgrimmarTopIn , 800)
end
--===========================================================================
function InitTrig_OrgrimmarFromTopOut()
    gg_trg_OrgrimmarFromTopOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgrimmarFromTopOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_OrgrimmarFromTopOut, Condition(Trig_OrgrimmarFromTopOut_Conditions))
    TriggerAddAction(gg_trg_OrgrimmarFromTopOut, Trig_OrgrimmarFromTopOut_Actions)
end
--===========================================================================
-- Trigger: OrgrimmarFromBotOut
--===========================================================================
function Trig_OrgrimmarFromBotOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0514
end
function Trig_OrgrimmarFromBotOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_OrgrimmarBotIn , 800)
end
--===========================================================================
function InitTrig_OrgrimmarFromBotOut()
    gg_trg_OrgrimmarFromBotOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgrimmarFromBotOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_OrgrimmarFromBotOut, Condition(Trig_OrgrimmarFromBotOut_Conditions))
    TriggerAddAction(gg_trg_OrgrimmarFromBotOut, Trig_OrgrimmarFromBotOut_Actions)
end
--===========================================================================
-- Trigger: OrgrimmarFromTopIn
--===========================================================================
function Trig_OrgrimmarFromTopIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0517
end
function Trig_OrgrimmarFromTopIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_OrgrimmarTopOut , 800)
end
--===========================================================================
function InitTrig_OrgrimmarFromTopIn()
    gg_trg_OrgrimmarFromTopIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgrimmarFromTopIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_OrgrimmarFromTopIn, Condition(Trig_OrgrimmarFromTopIn_Conditions))
    TriggerAddAction(gg_trg_OrgrimmarFromTopIn, Trig_OrgrimmarFromTopIn_Actions)
end
--===========================================================================
-- Trigger: OrgrimmarFromBotIn
--===========================================================================
function Trig_OrgrimmarFromBotIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0518
end
function Trig_OrgrimmarFromBotIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_OrgrimmarBotOut , 800)
end
--===========================================================================
function InitTrig_OrgrimmarFromBotIn()
    gg_trg_OrgrimmarFromBotIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgrimmarFromBotIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_OrgrimmarFromBotIn, Condition(Trig_OrgrimmarFromBotIn_Conditions))
    TriggerAddAction(gg_trg_OrgrimmarFromBotIn, Trig_OrgrimmarFromBotIn_Actions)
end
--===========================================================================
-- Trigger: DeadmonesFromin
--===========================================================================
function Trig_DeadmonesFromin_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0521
end
function Trig_DeadmonesFromin_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DeadminersOut , 800)
end
--===========================================================================
function InitTrig_DeadmonesFromin()
    gg_trg_DeadmonesFromin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadmonesFromin, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DeadmonesFromin, Condition(Trig_DeadmonesFromin_Conditions))
    TriggerAddAction(gg_trg_DeadmonesFromin, Trig_DeadmonesFromin_Actions)
end
--===========================================================================
-- Trigger: DeadmonesFromout
--===========================================================================
function Trig_DeadmonesFromout_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0420
end
function Trig_DeadmonesFromout_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DeadminerIn , 800)
end
--===========================================================================
function InitTrig_DeadmonesFromout()
    gg_trg_DeadmonesFromout=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadmonesFromout, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DeadmonesFromout, Condition(Trig_DeadmonesFromout_Conditions))
    TriggerAddAction(gg_trg_DeadmonesFromout, Trig_DeadmonesFromout_Actions)
end
--===========================================================================
-- Trigger: DM 1 O
--===========================================================================
function Trig_DM_1_O_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0943
end
function Trig_DM_1_O_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkM_4 , 1200)
end
--===========================================================================
function InitTrig_DM_1_O()
    gg_trg_DM_1_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DM_1_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DM_1_O, Condition(Trig_DM_1_O_Conditions))
    TriggerAddAction(gg_trg_DM_1_O, Trig_DM_1_O_Actions)
end
--===========================================================================
-- Trigger: DM 2
--===========================================================================
function Trig_DM_2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0942
end
function Trig_DM_2_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkM_3 , 1200)
end
--===========================================================================
function InitTrig_DM_2()
    gg_trg_DM_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DM_2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DM_2, Condition(Trig_DM_2_Conditions))
    TriggerAddAction(gg_trg_DM_2, Trig_DM_2_Actions)
end
--===========================================================================
-- Trigger: DM 3
--===========================================================================
function Trig_DM_3_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0940
end
function Trig_DM_3_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkM_1 , 1200)
end
--===========================================================================
function InitTrig_DM_3()
    gg_trg_DM_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DM_3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DM_3, Condition(Trig_DM_3_Conditions))
    TriggerAddAction(gg_trg_DM_3, Trig_DM_3_Actions)
end
--===========================================================================
-- Trigger: DM 4
--===========================================================================
function Trig_DM_4_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0941
end
function Trig_DM_4_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkM_2 , 1200)
end
--===========================================================================
function InitTrig_DM_4()
    gg_trg_DM_4=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DM_4, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DM_4, Condition(Trig_DM_4_Conditions))
    TriggerAddAction(gg_trg_DM_4, Trig_DM_4_Actions)
end
--===========================================================================
-- Trigger: Emerald Dream TP O Copy
--===========================================================================
function Trig_Emerald_Dream_TP_O_Copy_Func001C()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('H049')
end
function Trig_Emerald_Dream_TP_O_Copy_Actions()
    if Trig_Emerald_Dream_TP_O_Copy_Func001C() then
        udg_LocalPosition[21]=GetRectCenter(GetPlayableMapRect())
        SetUnitPositionLoc(GetTriggerUnit(), udg_LocalPosition[21])
        DisplayTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), "TRIGSTR_10588")
        udg_LocalText2=".."
        DisplayTextToPlayer(GetEnumPlayer(), 0, 0, udg_LocalText2)
        RemoveLocation(udg_LocalPosition[21])
    else
        if IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE) then --and GetUnitAbilityLevel(GetTriggerUnit(),FourCC('A1LR'))==0 then
            KillUnit(GetTriggerUnit())
        else
            UnitAddAbilityBJ(FourCC('A0LT'), GetTriggerUnit())
        end
    end
end
--===========================================================================
function InitTrig_Emerald_Dream_TP_O_Copy()
    gg_trg_Emerald_Dream_TP_O_Copy=CreateTrigger()
    TriggerRegisterEnterRectSimple(gg_trg_Emerald_Dream_TP_O_Copy, gg_rct_EmeraldDream)
    TriggerAddAction(gg_trg_Emerald_Dream_TP_O_Copy, Trig_Emerald_Dream_TP_O_Copy_Actions)
end
--===========================================================================
-- Trigger: Emerald Dream TP OFF O
--===========================================================================
function Trig_Emerald_Dream_TP_OFF_O_Actions()
    UnitRemoveAbilityBJ(FourCC('A0LT'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Emerald_Dream_TP_OFF_O()
    gg_trg_Emerald_Dream_TP_OFF_O=CreateTrigger()
    TriggerRegisterLeaveRectSimple(gg_trg_Emerald_Dream_TP_OFF_O, gg_rct_EmeraldDream)
    TriggerAddAction(gg_trg_Emerald_Dream_TP_OFF_O, Trig_Emerald_Dream_TP_OFF_O_Actions)
end
--===========================================================================
-- Trigger: NoAttackGreen
--===========================================================================
function Trig_NoAttackGreen_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0LR')) > 0 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1LR')) > 0 -- or GetUnitAbilityLevel( GetTriggerUnit(),FourCC('A0LR'))>0 and GetUnitAbilityLevel( GetAttacker(),FourCC('A1LR'))>0
end
function Trig_NoAttackGreen_Actions()
    IssueImmediateOrder(GetAttacker(), "stop")
end
--===========================================================================
function InitTrig_NoAttackGreen()
    local t= CreateTimer()
    gg_trg_NoAttackGreen=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoAttackGreen, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_NoAttackGreen, Condition(Trig_NoAttackGreen_Conditions))
    TriggerAddAction(gg_trg_NoAttackGreen, Trig_NoAttackGreen_Actions)
    TimerStart(t, 150, true, checkGreenArea)
end
--===========================================================================
-- Trigger: NoAttackGreen2
--===========================================================================
function Trig_NoAttackGreen2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0LR')) > 0 and GetUnitAbilityLevel(GetAttacker(), FourCC('A1LR')) > 0 -- or GetUnitAbilityLevel( GetTriggerUnit(),FourCC('A0LR'))>0 and GetUnitAbilityLevel( GetAttacker(),FourCC('A1LR'))>0
end
function Trig_NoAttackGreen2_Actions()
    IssueImmediateOrder(GetAttacker(), "stop")
end
--===========================================================================
function InitTrig_NoAttackGreen2()
    local t= CreateTimer()
    gg_trg_NoAttackGreen2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoAttackGreen2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_NoAttackGreen2, Condition(Trig_NoAttackGreen2_Conditions))
    TriggerAddAction(gg_trg_NoAttackGreen2, Trig_NoAttackGreen2_Actions)
end
--===========================================================================
-- Trigger: ED 1
--===========================================================================
function Trig_ED_1_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0889
end
function Trig_ED_1_Actions()
   TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_1 , 750)
end
--===========================================================================
function InitTrig_ED_1()
    gg_trg_ED_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_1, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_1, Condition(Trig_ED_1_Conditions))
    TriggerAddAction(gg_trg_ED_1, Trig_ED_1_Actions)
end
--===========================================================================
-- Trigger: ED 1 b
--===========================================================================
function Trig_ED_1_b_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_1012
end
function Trig_ED_1_b_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_1_B , 750)
end
--===========================================================================
function InitTrig_ED_1_b()
    gg_trg_ED_1_b=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_1_b, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_1_b, Condition(Trig_ED_1_b_Conditions))
    TriggerAddAction(gg_trg_ED_1_b, Trig_ED_1_b_Actions)
end
--===========================================================================
-- Trigger: ED 2
--===========================================================================
function Trig_ED_2_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0934
end
function Trig_ED_2_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_2 , 750)
end
--===========================================================================
function InitTrig_ED_2()
    gg_trg_ED_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_2, Condition(Trig_ED_2_Conditions))
    TriggerAddAction(gg_trg_ED_2, Trig_ED_2_Actions)
end
--===========================================================================
-- Trigger: ED 2 b
--===========================================================================
function Trig_ED_2_b_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_1013
end
function Trig_ED_2_b_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_2_b , 750)
end
--===========================================================================
function InitTrig_ED_2_b()
    gg_trg_ED_2_b=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_2_b, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_2_b, Condition(Trig_ED_2_b_Conditions))
    TriggerAddAction(gg_trg_ED_2_b, Trig_ED_2_b_Actions)
end
--===========================================================================
-- Trigger: ED 3
--===========================================================================
function Trig_ED_3_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0896
end
function Trig_ED_3_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_3 , 750)
end
--===========================================================================
function InitTrig_ED_3()
    gg_trg_ED_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_3, Condition(Trig_ED_3_Conditions))
    TriggerAddAction(gg_trg_ED_3, Trig_ED_3_Actions)
end
--===========================================================================
-- Trigger: ED 3 b
--===========================================================================
function Trig_ED_3_b_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_1014
end
function Trig_ED_3_b_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_3_b , 750)
end
--===========================================================================
function InitTrig_ED_3_b()
    gg_trg_ED_3_b=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_3_b, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_3_b, Condition(Trig_ED_3_b_Conditions))
    TriggerAddAction(gg_trg_ED_3_b, Trig_ED_3_b_Actions)
end
--===========================================================================
-- Trigger: ED 4
--===========================================================================
function Trig_ED_4_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_1015
end
function Trig_ED_4_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_4_b , 750)
end
--===========================================================================
function InitTrig_ED_4()
    gg_trg_ED_4=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_4, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_4, Condition(Trig_ED_4_Conditions))
    TriggerAddAction(gg_trg_ED_4, Trig_ED_4_Actions)
end
--===========================================================================
-- Trigger: ED 4 b
--===========================================================================
function Trig_ED_4_b_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0897
end
function Trig_ED_4_b_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_4 , 750)
end
--===========================================================================
function InitTrig_ED_4_b()
    gg_trg_ED_4_b=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_4_b, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_4_b, Condition(Trig_ED_4_b_Conditions))
    TriggerAddAction(gg_trg_ED_4_b, Trig_ED_4_b_Actions)
end
--===========================================================================
-- Trigger: ED 5
--===========================================================================
function Trig_ED_5_Conditions()
    return GetTriggerUnit() == gg_unit_n01Z_1016
end
function Trig_ED_5_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_5 , 750)
end
--===========================================================================
function InitTrig_ED_5()
    gg_trg_ED_5=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_5, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_5, Condition(Trig_ED_5_Conditions))
    TriggerAddAction(gg_trg_ED_5, Trig_ED_5_Actions)
end
--===========================================================================
-- Trigger: ED 5 B
--===========================================================================
function Trig_ED_5_B_Conditions()
    return GetTriggerUnit() == gg_unit_n01Z_1017
end
function Trig_ED_5_B_Actions()
    TeleportUnitsED(GetTriggerUnit() , gg_rct_ED_5_B , 750)
end
--===========================================================================
function InitTrig_ED_5_B()
    gg_trg_ED_5_B=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ED_5_B, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_ED_5_B, Condition(Trig_ED_5_B_Conditions))
    TriggerAddAction(gg_trg_ED_5_B, Trig_ED_5_B_Actions)
end
--===========================================================================
-- Trigger: Portal1
--===========================================================================
function Trig_Portal1_Conditions()
    return GetTriggerUnit() == gg_unit_n006_0023
end
function Trig_Portal1_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkPortal1 , 1200)
end
--===========================================================================
function InitTrig_Portal1()
    gg_trg_Portal1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal1, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal1, Condition(Trig_Portal1_Conditions))
    TriggerAddAction(gg_trg_Portal1, Trig_Portal1_Actions)
end
--===========================================================================
-- Trigger: Portal2
--===========================================================================
function Trig_Portal2_Conditions()
    return GetTriggerUnit() == gg_unit_n006_0438
end
function Trig_Portal2_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DarkPortal2 , 1200)
end
--===========================================================================
function InitTrig_Portal2()
    gg_trg_Portal2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal2, Condition(Trig_Portal2_Conditions))
    TriggerAddAction(gg_trg_Portal2, Trig_Portal2_Actions)
end
--===========================================================================
-- Trigger: Portal3
--===========================================================================
function Trig_Portal3_Conditions()
    return GetTriggerUnit() == gg_unit_n001_0845
end
function Trig_Portal3_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_009 , 1200)
end
--===========================================================================
function InitTrig_Portal3()
    gg_trg_Portal3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal3, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal3, Condition(Trig_Portal3_Conditions))
    TriggerAddAction(gg_trg_Portal3, Trig_Portal3_Actions)
end
--===========================================================================
-- Trigger: Portal4
--===========================================================================
function Trig_Portal4_Conditions()
    return GetTriggerUnit() == gg_unit_n04O_0136
end
function Trig_Portal4_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_010 , 1200)
end
--===========================================================================
function InitTrig_Portal4()
    gg_trg_Portal4=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal4, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal4, Condition(Trig_Portal4_Conditions))
    TriggerAddAction(gg_trg_Portal4, Trig_Portal4_Actions)
end
--===========================================================================
-- Trigger: Portal5
--===========================================================================
function Trig_Portal5_Conditions()
    return GetTriggerUnit() == gg_unit_n00W_0442
end
function Trig_Portal5_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_EKportalAlterac , 1200)
end
--===========================================================================
function InitTrig_Portal5()
    gg_trg_Portal5=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal5, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal5, Condition(Trig_Portal5_Conditions))
    TriggerAddAction(gg_trg_Portal5, Trig_Portal5_Actions)
end
--===========================================================================
-- Trigger: Portal6
--===========================================================================
function Trig_Portal6_Conditions()
    return GetTriggerUnit() == gg_unit_n00W_0589
end
function Trig_Portal6_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_OutlandNagrand , 1200)
end
--===========================================================================
function InitTrig_Portal6()
    gg_trg_Portal6=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal6, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal6, Condition(Trig_Portal6_Conditions))
    TriggerAddAction(gg_trg_Portal6, Trig_Portal6_Actions)
end
--===========================================================================
-- Trigger: Portal7
--===========================================================================
function Trig_Portal7_Conditions()
    return GetTriggerUnit() == gg_unit_n00W_0446
end
function Trig_Portal7_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_013 , 1200)
end
--===========================================================================
function InitTrig_Portal7()
    gg_trg_Portal7=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal7, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal7, Condition(Trig_Portal7_Conditions))
    TriggerAddAction(gg_trg_Portal7, Trig_Portal7_Actions)
end
--===========================================================================
-- Trigger: Portal8
--===========================================================================
function Trig_Portal8_Conditions()
    return GetTriggerUnit() == gg_unit_n001_0847
end
function Trig_Portal8_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_014 , 1200)
end
--===========================================================================
function InitTrig_Portal8()
    gg_trg_Portal8=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal8, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal8, Condition(Trig_Portal8_Conditions))
    TriggerAddAction(gg_trg_Portal8, Trig_Portal8_Actions)
end
--===========================================================================
-- Trigger: Portal9Tomb
--===========================================================================
function Trig_Portal9Tomb_Conditions()
    return GetTriggerUnit() == gg_unit_n065_0125
end
function Trig_Portal9Tomb_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_ArgusShip , 1200)
end
--===========================================================================
function InitTrig_Portal9Tomb()
    gg_trg_Portal9Tomb=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal9Tomb, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal9Tomb, Condition(Trig_Portal9Tomb_Conditions))
    TriggerAddAction(gg_trg_Portal9Tomb, Trig_Portal9Tomb_Actions)
end
--===========================================================================
-- Trigger: Portal10
--===========================================================================
function Trig_Portal10_Conditions()
    return GetTriggerUnit() == gg_unit_n00W_0848
end
function Trig_Portal10_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_Broken_Island , 1200)
end
--===========================================================================
function InitTrig_Portal10()
    gg_trg_Portal10=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal10, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal10, Condition(Trig_Portal10_Conditions))
    TriggerAddAction(gg_trg_Portal10, Trig_Portal10_Actions)
end
--===========================================================================
-- Trigger: Portal11
--===========================================================================
function Trig_Portal11_Conditions()
    return GetTriggerUnit() == gg_unit_n01B_0849
end
function Trig_Portal11_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_017 , 1200)
end
--===========================================================================
function InitTrig_Portal11()
    gg_trg_Portal11=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal11, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal11, Condition(Trig_Portal11_Conditions))
    TriggerAddAction(gg_trg_Portal11, Trig_Portal11_Actions)
end
--===========================================================================
-- Trigger: Portal12
--===========================================================================
function Trig_Portal12_Conditions()
    return GetTriggerUnit() == gg_unit_n01B_0850
end
function Trig_Portal12_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Region_018 , 1200)
end
--===========================================================================
function InitTrig_Portal12()
    gg_trg_Portal12=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal12, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Portal12, Condition(Trig_Portal12_Conditions))
    TriggerAddAction(gg_trg_Portal12, Trig_Portal12_Actions)
end
--===========================================================================
-- Trigger: Azner 2
--===========================================================================
function Trig_Azner_2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0098
end
function Trig_Azner_2_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Nord_5 , 1200)
end
--===========================================================================
function InitTrig_Azner_2()
    gg_trg_Azner_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Azner_2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Azner_2, Condition(Trig_Azner_2_Conditions))
    TriggerAddAction(gg_trg_Azner_2, Trig_Azner_2_Actions)
end
--===========================================================================
-- Trigger: Azner 5
--===========================================================================
function Trig_Azner_5_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0060
end
function Trig_Azner_5_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_AzNer_5 , 650)
end
--===========================================================================
function InitTrig_Azner_5()
    gg_trg_Azner_5=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Azner_5, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Azner_5, Condition(Trig_Azner_5_Conditions))
    TriggerAddAction(gg_trg_Azner_5, Trig_Azner_5_Actions)
end
--===========================================================================
-- Trigger: Nord 2
--===========================================================================
function Trig_Nord_2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0097
end
function Trig_Nord_2_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_AzNer_2 , 1200)
end
--===========================================================================
function InitTrig_Nord_2()
    gg_trg_Nord_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Nord_2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Nord_2, Condition(Trig_Nord_2_Conditions))
    TriggerAddAction(gg_trg_Nord_2, Trig_Nord_2_Actions)
end
--===========================================================================
-- Trigger: Nord 4
--===========================================================================
function Trig_Nord_4_Conditions()
    return GetTriggerUnit() == gg_unit_n003_1004
end
function Trig_Nord_4_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Nord4 , 1200)
end
--===========================================================================
function InitTrig_Nord_4()
    gg_trg_Nord_4=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Nord_4, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Nord_4, Condition(Trig_Nord_4_Conditions))
    TriggerAddAction(gg_trg_Nord_4, Trig_Nord_4_Actions)
end
--===========================================================================
-- Trigger: Nord 5
--===========================================================================
function Trig_Nord_5_Conditions()
    return GetTriggerUnit() == gg_unit_n003_1002
end
function Trig_Nord_5_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Nord_1 , 1200)
end
--===========================================================================
function InitTrig_Nord_5()
    gg_trg_Nord_5=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Nord_5, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_Nord_5, Condition(Trig_Nord_5_Conditions))
    TriggerAddAction(gg_trg_Nord_5, Trig_Nord_5_Actions)
end
--===========================================================================
-- Trigger: HrenPoimiHareUdaliatPortalu
--===========================================================================
function Trig_HrenPoimiHareUdaliatPortalu_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0995
end
function Trig_HrenPoimiHareUdaliatPortalu_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_AzNer1 , 1200)
end
--===========================================================================
function InitTrig_HrenPoimiHareUdaliatPortalu()
    gg_trg_HrenPoimiHareUdaliatPortalu=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HrenPoimiHareUdaliatPortalu, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_HrenPoimiHareUdaliatPortalu, Condition(Trig_HrenPoimiHareUdaliatPortalu_Conditions))
    TriggerAddAction(gg_trg_HrenPoimiHareUdaliatPortalu, Trig_HrenPoimiHareUdaliatPortalu_Actions)
end
--===========================================================================
-- Trigger: FromDarnas
--===========================================================================
function Trig_FromDarnas_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0578
end
function Trig_FromDarnas_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_Teldrasil , 1200)
end
--===========================================================================
function InitTrig_FromDarnas()
    gg_trg_FromDarnas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FromDarnas, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_FromDarnas, Condition(Trig_FromDarnas_Conditions))
    TriggerAddAction(gg_trg_FromDarnas, Trig_FromDarnas_Actions)
end
--===========================================================================
-- Trigger: FromTeldrasil
--===========================================================================
function Trig_FromTeldrasil_Conditions()
    return GetTriggerUnit() == gg_unit_n01Y_0580
end
function Trig_FromTeldrasil_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Darnas , 1200)
end
--===========================================================================
function InitTrig_FromTeldrasil()
    gg_trg_FromTeldrasil=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FromTeldrasil, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_FromTeldrasil, Condition(Trig_FromTeldrasil_Conditions))
    TriggerAddAction(gg_trg_FromTeldrasil, Trig_FromTeldrasil_Actions)
end
--===========================================================================
-- Trigger: QtunOut
--===========================================================================
function Trig_QtunOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0118
end
function Trig_QtunOut_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_QtunIn , 1200)
end
--===========================================================================
function InitTrig_QtunOut()
    gg_trg_QtunOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QtunOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_QtunOut, Condition(Trig_QtunOut_Conditions))
    TriggerAddAction(gg_trg_QtunOut, Trig_QtunOut_Actions)
end
--===========================================================================
-- Trigger: QtunOut2
--===========================================================================
function Trig_QtunOut2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0117
end
function Trig_QtunOut2_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_QtunIn2 , 1200)
end
--===========================================================================
function InitTrig_QtunOut2()
    gg_trg_QtunOut2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QtunOut2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_QtunOut2, Condition(Trig_QtunOut2_Conditions))
    TriggerAddAction(gg_trg_QtunOut2, Trig_QtunOut2_Actions)
end
--===========================================================================
-- Trigger: QtunIn
--===========================================================================
function Trig_QtunIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0124
end
function Trig_QtunIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_QtunOut , 1200)
end
--===========================================================================
function InitTrig_QtunIn()
    gg_trg_QtunIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QtunIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_QtunIn, Condition(Trig_QtunIn_Conditions))
    TriggerAddAction(gg_trg_QtunIn, Trig_QtunIn_Actions)
end
--===========================================================================
-- Trigger: QtunIn2
--===========================================================================
function Trig_QtunIn2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0123
end
function Trig_QtunIn2_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_QtunOu2 , 1200)
end
--===========================================================================
function InitTrig_QtunIn2()
    gg_trg_QtunIn2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QtunIn2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_QtunIn2, Condition(Trig_QtunIn2_Conditions))
    TriggerAddAction(gg_trg_QtunIn2, Trig_QtunIn2_Actions)
end
--===========================================================================
-- Trigger: MaradonIn
--===========================================================================
function Trig_MaradonIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0308
end
function Trig_MaradonIn_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_MarodonOut , 900)
end
--===========================================================================
function InitTrig_MaradonIn()
    gg_trg_MaradonIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MaradonIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_MaradonIn, Condition(Trig_MaradonIn_Conditions))
    TriggerAddAction(gg_trg_MaradonIn, Trig_MaradonIn_Actions)
end
--===========================================================================
-- Trigger: MaradonIn2
--===========================================================================
function Trig_MaradonIn2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0311
end
function Trig_MaradonIn2_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_MarodonOut2 , 900)
end
--===========================================================================
function InitTrig_MaradonIn2()
    gg_trg_MaradonIn2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MaradonIn2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_MaradonIn2, Condition(Trig_MaradonIn2_Conditions))
    TriggerAddAction(gg_trg_MaradonIn2, Trig_MaradonIn2_Actions)
end
--===========================================================================
-- Trigger: MaradonOut
--===========================================================================
function Trig_MaradonOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0305
end
function Trig_MaradonOut_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_MarodonIn , 900)
end
--===========================================================================
function InitTrig_MaradonOut()
    gg_trg_MaradonOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MaradonOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_MaradonOut, Condition(Trig_MaradonOut_Conditions))
    TriggerAddAction(gg_trg_MaradonOut, Trig_MaradonOut_Actions)
end
--===========================================================================
-- Trigger: MaradonOut2
--===========================================================================
function Trig_MaradonOut2_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0314
end
function Trig_MaradonOut2_Actions()
   TeleportUnits(GetTriggerUnit() , gg_rct_MarodonIn2 , 900)
end
--===========================================================================
function InitTrig_MaradonOut2()
    gg_trg_MaradonOut2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MaradonOut2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_MaradonOut2, Condition(Trig_MaradonOut2_Conditions))
    TriggerAddAction(gg_trg_MaradonOut2, Trig_MaradonOut2_Actions)
end
--===========================================================================
-- Trigger: Untitled Trigger 011
--===========================================================================
function Trig_Untitled_Trigger_011_Conditions()
    return (( GetTriggerUnit() == gg_unit_n003_0314 )) and (( GetTriggerUnit() == gg_unit_n003_0311 ))
end
function Trig_Untitled_Trigger_011_Actions()
end
--===========================================================================
function InitTrig_Untitled_Trigger_011()
    gg_trg_Untitled_Trigger_011=CreateTrigger()
    TriggerAddCondition(gg_trg_Untitled_Trigger_011, Condition(Trig_Untitled_Trigger_011_Conditions))
    TriggerAddAction(gg_trg_Untitled_Trigger_011, Trig_Untitled_Trigger_011_Actions)
end
--===========================================================================
-- Trigger: GnomeOut
--===========================================================================
function Trig_GnomeOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0025
end
function Trig_GnomeOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_GnomreganIn , 1200)
end
--===========================================================================
function InitTrig_GnomeOut()
    gg_trg_GnomeOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GnomeOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_GnomeOut, Condition(Trig_GnomeOut_Conditions))
    TriggerAddAction(gg_trg_GnomeOut, Trig_GnomeOut_Actions)
end
--===========================================================================
-- Trigger: GnomeIn
--===========================================================================
function Trig_GnomeIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0018
end
function Trig_GnomeIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_GnomreganOut , 1200)
end
--===========================================================================
function InitTrig_GnomeIn()
    gg_trg_GnomeIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GnomeIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_GnomeIn, Condition(Trig_GnomeIn_Conditions))
    TriggerAddAction(gg_trg_GnomeIn, Trig_GnomeIn_Actions)
end
--===========================================================================
-- Trigger: StalgornOut
--===========================================================================
function Trig_StalgornOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0024
end
function Trig_StalgornOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Stalgorn , 1200)
end
--===========================================================================
function InitTrig_StalgornOut()
    gg_trg_StalgornOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StalgornOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_StalgornOut, Condition(Trig_StalgornOut_Conditions))
    TriggerAddAction(gg_trg_StalgornOut, Trig_StalgornOut_Actions)
end
--===========================================================================
-- Trigger: StalgornIn
--===========================================================================
function Trig_StalgornIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0019
end
function Trig_StalgornIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_StalgornOut , 1200)
end
--===========================================================================
function InitTrig_StalgornIn()
    gg_trg_StalgornIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StalgornIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_StalgornIn, Condition(Trig_StalgornIn_Conditions))
    TriggerAddAction(gg_trg_StalgornIn, Trig_StalgornIn_Actions)
end
--===========================================================================
-- Trigger: TrainOut
--===========================================================================
function Trig_TrainOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0028
end
function Trig_TrainOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_TrainIn , 1200)
end
--===========================================================================
function InitTrig_TrainOut()
    gg_trg_TrainOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_TrainOut, Condition(Trig_TrainOut_Conditions))
    TriggerAddAction(gg_trg_TrainOut, Trig_TrainOut_Actions)
end
--===========================================================================
-- Trigger: TrainIn
--===========================================================================
function Trig_TrainIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0149
end
function Trig_TrainIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_TrainOut , 1200)
end
--===========================================================================
function InitTrig_TrainIn()
    gg_trg_TrainIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_TrainIn, Condition(Trig_TrainIn_Conditions))
    TriggerAddAction(gg_trg_TrainIn, Trig_TrainIn_Actions)
end
--===========================================================================
-- Trigger: GrimBatonIn
--===========================================================================
function Trig_GrimBatonIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0021
end
function Trig_GrimBatonIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_GrimBatolOut , 1200)
end
--===========================================================================
function InitTrig_GrimBatonIn()
    gg_trg_GrimBatonIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GrimBatonIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_GrimBatonIn, Condition(Trig_GrimBatonIn_Conditions))
    TriggerAddAction(gg_trg_GrimBatonIn, Trig_GrimBatonIn_Actions)
end
--===========================================================================
-- Trigger: GrimBatolOut
--===========================================================================
function Trig_GrimBatolOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0022
end
function Trig_GrimBatolOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_GrimBatolIn , 1200)
end
--===========================================================================
function InitTrig_GrimBatolOut()
    gg_trg_GrimBatolOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GrimBatolOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_GrimBatolOut, Condition(Trig_GrimBatolOut_Conditions))
    TriggerAddAction(gg_trg_GrimBatolOut, Trig_GrimBatolOut_Actions)
end
--===========================================================================
-- Trigger: UldamanOut
--===========================================================================
function Trig_UldamanOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0027
end
function Trig_UldamanOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UldamanIn , 1200)
end
--===========================================================================
function InitTrig_UldamanOut()
    gg_trg_UldamanOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UldamanOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UldamanOut, Condition(Trig_UldamanOut_Conditions))
    TriggerAddAction(gg_trg_UldamanOut, Trig_UldamanOut_Actions)
end
--===========================================================================
-- Trigger: UldamanIn
--===========================================================================
function Trig_UldamanIn_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0020
end
function Trig_UldamanIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_UldamanOut , 1200)
end
--===========================================================================
function InitTrig_UldamanIn()
    gg_trg_UldamanIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UldamanIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_UldamanIn, Condition(Trig_UldamanIn_Conditions))
    TriggerAddAction(gg_trg_UldamanIn, Trig_UldamanIn_Actions)
end
--===========================================================================
-- Trigger: NaxOut
--===========================================================================
function Trig_NaxOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0126
end
function Trig_NaxOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_NaxOut , 1200)
end
--===========================================================================
function InitTrig_NaxOut()
    gg_trg_NaxOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_NaxOut, Condition(Trig_NaxOut_Conditions))
    TriggerAddAction(gg_trg_NaxOut, Trig_NaxOut_Actions)
end
--===========================================================================
-- Trigger: NaxIn
--===========================================================================
function Trig_NaxIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_NaxPortalIn , 1200)
end
--===========================================================================
function InitTrig_NaxIn()
    gg_trg_NaxIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_NaxIn, function()
        if GetSpellAbilityId() ~= FourCC('A0HY') then return end
        if not (GetUnitTypeId(GetTriggerUnit()) == FourCC('n066')) then return end
        Trig_NaxIn_Actions()
    end)
end
--===========================================================================
-- Trigger: DalOut
--===========================================================================
function Trig_DalOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0588
end
function Trig_DalOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DalaranOut , 1200)
end
--===========================================================================
function InitTrig_DalOut()
    gg_trg_DalOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_DalOut, Condition(Trig_DalOut_Conditions))
    TriggerAddAction(gg_trg_DalOut, Trig_DalOut_Actions)
end
--===========================================================================
-- Trigger: DalIn
--===========================================================================
function Trig_DalIn_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_DalaranIn , 1200)
end
--===========================================================================
function InitTrig_DalIn()
    gg_trg_DalIn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalIn, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DalIn, function()
        if GetSpellAbilityId() ~= FourCC('A0HY') then return end
        if not (GetUnitTypeId(GetTriggerUnit()) == FourCC('n063')) then return end
        Trig_DalIn_Actions()
    end)
end
--===========================================================================
-- Trigger: FromIsland
--===========================================================================
function Trig_FromIsland_Conditions()
    return GetTriggerUnit() == gg_unit_n060_0350
end
function Trig_FromIsland_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_Silvermoon , 1200)
end
--===========================================================================
function InitTrig_FromIsland()
    gg_trg_FromIsland=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FromIsland, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_FromIsland, Condition(Trig_FromIsland_Conditions))
    TriggerAddAction(gg_trg_FromIsland, Trig_FromIsland_Actions)
end
--===========================================================================
-- Trigger: Untitled Trigger 014
--===========================================================================
function Trig_Untitled_Trigger_014_Actions()
end
--===========================================================================
function InitTrig_Untitled_Trigger_014()
    gg_trg_Untitled_Trigger_014=CreateTrigger()
    TriggerRegisterUnitManaEvent(gg_trg_Untitled_Trigger_014, gg_unit_n060_0350, LESS_THAN, 50)
    TriggerRegisterUnitManaEvent(gg_trg_Untitled_Trigger_014, gg_unit_n060_0287, LESS_THAN, 50)
    TriggerAddAction(gg_trg_Untitled_Trigger_014, Trig_Untitled_Trigger_014_Actions)
end
--===========================================================================
-- Trigger: FromCity
--===========================================================================
function Trig_FromCity_Conditions()
    return GetTriggerUnit() == gg_unit_n060_0287
end
function Trig_FromCity_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_QuelIsland , 1200)
end
--===========================================================================
function InitTrig_FromCity()
    gg_trg_FromCity=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FromCity, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_FromCity, Condition(Trig_FromCity_Conditions))
    TriggerAddAction(gg_trg_FromCity, Trig_FromCity_Actions)
end
--===========================================================================
-- Trigger: Test
--===========================================================================
function Trig_Test_Actions()
    WaygateActivateBJ(false, gg_unit_n01Y_0578)
    WaygateSetDestinationLocBJ(gg_unit_n01Y_0578, GetRectCenter(gg_rct_Teldrasil))
    WaygateActivateBJ(true, gg_unit_n01Y_0578)
    WaygateSetDestinationLocBJ(gg_unit_n01Y_0578, GetRectCenter(gg_rct_Teldrasil))
    -- ---
end
--===========================================================================
function InitTrig_Test()
    gg_trg_Test=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Test, 26.00)
    TriggerAddAction(gg_trg_Test, Trig_Test_Actions)
end
--===========================================================================
-- Trigger: PrepareToBurnCity
--===========================================================================
function Trig_PrepareToBurnCity_Actions()
    UnitRemoveAbility(GetTriggerUnit(), FourCC('A1LD'))
    UnitAddAbility(GetTriggerUnit(), FourCC('A1LC'))
end
--===========================================================================
function InitTrig_PrepareToBurnCity()
    gg_trg_PrepareToBurnCity=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PrepareToBurnCity, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_PrepareToBurnCity, function()
        if GetSpellAbilityId() ~= FourCC('A1LD') then return end
        Trig_PrepareToBurnCity_Actions()
    end)
end
--===========================================================================
-- Trigger: BurnCity
--===========================================================================
function Trig_BurnCity_Actions()
   -- call UnitDamageTarget(GetTriggerUnit(),GetTriggerUnit(),99999,true,false,ATTACK_TYPE_NORMAL,DAMAGE_TYPE_UNIVERSAL,WEAPON_TYPE_WHOKNOWS)
   -- if not UnitAlive(GetTriggerUnit()) then
        KillUnit(GetTriggerUnit())
   -- endif
    
end
--===========================================================================
function InitTrig_BurnCity()
    gg_trg_BurnCity=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BurnCity, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BurnCity, function()
        if GetSpellAbilityId() ~= FourCC('A1LC') then return end
        Trig_BurnCity_Actions()
    end)
end
--===========================================================================
-- Trigger: NoTpNearCapitalDalNax
--===========================================================================
function CheckPosition()
    return not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY)
  
  -- if not (IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY)) then
    --    return true
   -- endif
    
end
function CheckPositionT()
    --local real add = 25
    if IsTerrainPathable(x + add, y - add, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x + add, y, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x + add, y + add, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x, y - add, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x, y + add, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x - add, y - add, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x - add, y, PATHING_TYPE_FLOATABILITY) and IsTerrainPathable(x - add, y + add, PATHING_TYPE_FLOATABILITY) then
        return true
    end
    DisplayTextToPlayer(udg_LocalPlayer, 0, 0, ".")
    return false
end
--===========================================================================
-- Trigger: Owner
--===========================================================================
function Trig_Owner_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == DalaranOutType
end
function Trig_Owner_Actions()
    SetUnitOwner(gg_unit_e00C_0590, GetOwningPlayer(GetKillingUnit()), true)
    SetPlayerAbilityAvailableBJ(true, AbilityDown, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, AbilityDown, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, AbilityAp, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, AbilityAp, GetOwningPlayer(GetTriggerUnit()))
    
    
end
--===========================================================================
function InitTrig_Owner()
    gg_trg_Owner=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Owner, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Owner, Condition(Trig_Owner_Conditions))
    TriggerAddAction(gg_trg_Owner, Trig_Owner_Actions)
end
--===========================================================================
-- Trigger: StartDal
--===========================================================================
function Trig_StartDal_Func002A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A1F7'), GetEnumPlayer())
end
function Trig_StartDal_Actions()
    IssuePointOrderLocBJ(gg_unit_e00C_0590, "flamestrike", GetUnitLoc(gg_unit_e00C_0590))
    ForForce(udg_AllPlayers, Trig_StartDal_Func002A)
    WaygateSetDestinationLocBJ(gg_unit_n003_0588, GetUnitLoc(gg_unit_e00C_0590))
    WaygateActivateBJ(true, gg_unit_n003_0588)
    WaygateSetDestinationLocBJ(gg_unit_n003_0588, GetUnitLoc(gg_unit_e00C_0590))
end
--===========================================================================
function InitTrig_StartDal()
    gg_trg_StartDal=CreateTrigger()
    TriggerAddAction(gg_trg_StartDal, Trig_StartDal_Actions)
end
--===========================================================================
-- Trigger: PosadkaDal2
--===========================================================================
function Trig_PosadkaDal_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0,"")
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    return GetSpellAbilityId() == AbilityDown and CheckPosition(GetSpellTargetX() , GetSpellTargetY() , 25) and CheckNearCapitals(GetTriggerUnit())
    
    --return ( GetIssuedOrderId()==OrderId("root") or GetIssuedOrderId()==OrderId("unroot") ) and GetUnitTypeId(GetTriggerUnit())=='e00C'
end
function Trig_PosadkaDal_Actions()
    local u= GetTriggerUnit()
    local u2= CreateUnit(Player(PLAYER_NEUTRAL_PASSIVE), FourCC('n063'), GetUnitX(u), GetUnitY(u) - 65, 0.00)
    SetUnitMoveSpeed(u, 0.0)
    SaveUnitHandle(Hash, StringHash("Dalaran"), 1, u2)
    
    
    --???? ??????
    --call DisplayTextToPlayer(Player(0),0,0," - "+R2S(GetUnitMoveSpeed(u)))
    BlzSetUnitRealFieldBJ(u, UNIT_RF_FLY_HEIGHT, - 200.00)
    SetUnitFlyHeightBJ(u, - 200, 55.00)
    UnitAddAbility(u, FourCC('A1M6'))
    UnitAddAbility(u, FourCC('A1GE'))
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.00)
   
    UnitAddAbility(u, AbilityAp)
    BlzStartUnitAbilityCooldown(u, AbilityAp, 15)
    UnitRemoveAbility(u, AbilityDown)
    
    
    
    ShowUnit(gg_unit_n003_0588, true)
    
    --call UnitRemoveAbilityBJ( 'A1F3', u )
    --call UnitAddAbility(u,'A0HY')
    
    WaygateActivate(gg_unit_n003_0588, true)
    WaygateActivate(u2, true)
    MoveRectTo(gg_rct_DalaranOut, GetUnitX(u), GetUnitY(u))
    WaygateSetDestination(gg_unit_n003_0588, GetRectCenterX(gg_rct_DalaranOut), GetRectCenterY(gg_rct_DalaranOut))
    WaygateSetDestination(u2, GetRectCenterX(gg_rct_DalaranIn), GetRectCenterY(gg_rct_DalaranIn))
    WaygateActivate(u2, true)
    WaygateActivate(gg_unit_n003_0588, true)
    u2=nil
    u=nil
end
--===========================================================================
function InitTrig_PosadkaDal2()
    gg_trg_PosadkaDal2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PosadkaDal2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_PosadkaDal2, Condition(Trig_PosadkaDal_Conditions))
    TriggerAddAction(gg_trg_PosadkaDal2, Trig_PosadkaDal_Actions)
end
--===========================================================================
-- Trigger: VzletDal
--===========================================================================
function Trig_VzletDal_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0,"")
    return GetSpellAbilityId() == AbilityAp
    
    --return ( GetIssuedOrderId()==OrderId("root") or GetIssuedOrderId()==OrderId("unroot") ) and GetUnitTypeId(GetTriggerUnit())=='e00C'
end
function Trig_VzletDal_Actions()
    local u= GetTriggerUnit()
    RemoveUnit(LoadUnitHandle(Hash, StringHash("Dalaran"), 1))
    FlushChildHashtable(Hash, StringHash("Dalaran"))
    SetUnitMoveSpeed(u, GetUnitDefaultMoveSpeed(u))
    --???? ????????
    BlzSetUnitRealFieldBJ(u, UNIT_RF_FLY_HEIGHT, 400.00)
    SetUnitFlyHeightBJ(u, 400.00, 55.00)
    
    ShowUnit(gg_unit_n003_0588, false)
    UnitRemoveAbility(u, FourCC('A1M6'))
    UnitRemoveAbility(u, FourCC('A1GE'))
    UnitAddAbility(u, AbilityDown)
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.15)
    BlzStartUnitAbilityCooldown(u, AbilityDown, 15)
    UnitRemoveAbility(u, AbilityAp)
    
    WaygateActivateBJ(false, gg_unit_n003_0588)
    
    --call UnitAddAbility( u, 'A1F3')
    --call UnitRemoveAbility(u,'A0HY')
    
    --call DisplayTextToPlayer(Player(0),0,0," - "+R2S(GetUnitMoveSpeed(u)))
    WaygateActivate(gg_unit_n003_0588, false)
    
    
    u=nil
end
--===========================================================================
function InitTrig_VzletDal()
    gg_trg_VzletDal=CreateTrigger()
    
    
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_VzletDal, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER )
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_VzletDal, EVENT_PLAYER_UNIT_ISSUED_ORDER )
    
    
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_VzletDal, EVENT_PLAYER_UNIT_SPELL_FINISH )
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_VzletDal, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_VzletDal, EVENT_PLAYER_UNIT_SPELL_EFFECT )
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_VzletDal, EVENT_PLAYER_UNIT_SPELL_ENDCAST )
    TriggerAddCondition(gg_trg_VzletDal, Condition(Trig_VzletDal_Conditions))
    TriggerAddAction(gg_trg_VzletDal, Trig_VzletDal_Actions)
end
--===========================================================================
-- Trigger: DalDiy
--===========================================================================
function Trig_DalDiy_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00C')
end
function Trig_DalDiy_Func002A()
    KillUnit(GetEnumUnit())
end
function Trig_DalDiy_Func003A()
    RemoveUnit(GetEnumUnit())
end
function Trig_DalDiy_Actions()
    ForGroupBJ(GetUnitsInRectAll(gg_rct_RenameDeath), Trig_DalDiy_Func002A)
    ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('n063')), Trig_DalDiy_Func003A)
    TriggerExecute(gg_trg_DallKill)
    DisableTrigger(GetTriggeringTrigger())
    
end
--===========================================================================
function InitTrig_DalDiy()
    gg_trg_DalDiy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalDiy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DalDiy, Condition(Trig_DalDiy_Conditions))
    TriggerAddAction(gg_trg_DalDiy, Trig_DalDiy_Actions)
end
--===========================================================================
-- Trigger: DallKill
--===========================================================================
function Trig_DallKill_Actions()
    UnitDamagePointLoc(nil, 0, 3000.00, GetRectCenter(gg_rct_KillDalaran), 999999.00, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_NORMAL)
end
--===========================================================================
function InitTrig_DallKill()
    gg_trg_DallKill=CreateTrigger()
    TriggerAddAction(gg_trg_DallKill, Trig_DallKill_Actions)
end
--===========================================================================
-- Trigger: OwnerNax
--===========================================================================
function Trig_OwnerNax_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0F3')
end
function Trig_OwnerNax_Actions()
    SetUnitOwner(gg_unit_e00D_0080, GetOwningPlayer(GetKillingUnit()), true)
    SetPlayerAbilityAvailableBJ(true, NaxAbilityDown, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, NaxAbilityDown, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, NaxAbilityAp, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, NaxAbilityAp, GetOwningPlayer(GetTriggerUnit()))
    
    
end
--===========================================================================
function InitTrig_OwnerNax()
    gg_trg_OwnerNax=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OwnerNax, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_OwnerNax, Condition(Trig_OwnerNax_Conditions))
    TriggerAddAction(gg_trg_OwnerNax, Trig_OwnerNax_Actions)
end
--===========================================================================
-- Trigger: NaxStart
--===========================================================================
function Trig_NaxStart_Func002A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A1GV'), GetEnumPlayer())
end
function Trig_NaxStart_Actions()
    IssuePointOrderLocBJ(gg_unit_e00D_0080, "flamestrike", GetUnitLoc(gg_unit_e00D_0080))
    ForForce(udg_AllPlayers, Trig_NaxStart_Func002A)
    WaygateSetDestinationLocBJ(gg_unit_n003_0126, GetUnitLoc(gg_unit_e00D_0080))
    WaygateActivateBJ(true, gg_unit_n003_0126)
    WaygateSetDestinationLocBJ(gg_unit_n003_0126, GetUnitLoc(gg_unit_e00D_0080))
end
--===========================================================================
function InitTrig_NaxStart()
    gg_trg_NaxStart=CreateTrigger()
    TriggerAddAction(gg_trg_NaxStart, Trig_NaxStart_Actions)
end
--===========================================================================
-- Trigger: NaxPosadka
--===========================================================================
function Trig_PosadkaNax_Conditions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    return GetSpellAbilityId() == NaxAbilityDown and CheckPosition(GetSpellTargetX() , GetSpellTargetY() , 25) and CheckNearCapitals(GetTriggerUnit())
end
function Trig_PosadkaNax_Actions()
    local u= GetTriggerUnit()
    local u2= CreateUnit(Player(PLAYER_NEUTRAL_PASSIVE), FourCC('n066'), GetUnitX(u), GetUnitY(u) - 65, 0.00)
    SetUnitMoveSpeed(u, 0.0)
    SaveUnitHandle(Hash, StringHash("Nax"), 1, u2)
    
    
    --???? ??????
    --call DisplayTextToPlayer(Player(0),0,0," - "+R2S(GetUnitMoveSpeed(u)))
    BlzSetUnitRealFieldBJ(u, UNIT_RF_FLY_HEIGHT, - 200.00)
    SetUnitFlyHeightBJ(u, - 200, 55.00)
    UnitAddAbility(u, FourCC('A1M6'))
    UnitAddAbility(u, FourCC('A1GE'))
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.00)
   
    UnitAddAbility(u, NaxAbilityAp)
    BlzStartUnitAbilityCooldown(u, NaxAbilityAp, 15)
    UnitRemoveAbility(u, NaxAbilityDown)
    
    
    
    ShowUnit(gg_unit_n003_0126, true)
    
    --call UnitRemoveAbilityBJ( 'A1F3', u )
    --call UnitAddAbility(u,'A0HY')
    
    WaygateActivate(gg_unit_n003_0126, true)
    WaygateActivate(u2, true)
    MoveRectTo(gg_rct_NaxOut, GetUnitX(u), GetUnitY(u))
    WaygateSetDestination(gg_unit_n003_0126, GetRectCenterX(gg_rct_NaxOut), GetRectCenterY(gg_rct_NaxOut))
    WaygateSetDestination(u2, GetRectCenterX(gg_rct_NaxPortalIn), GetRectCenterY(gg_rct_NaxPortalIn))
    WaygateActivate(u2, true)
    WaygateActivate(gg_unit_n003_0126, true)
    u2=nil
    u=nil
end
--===========================================================================
function InitTrig_NaxPosadka()
    gg_trg_NaxPosadka=CreateTrigger()
    
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxPosadka, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_NaxPosadka, Condition(Trig_PosadkaNax_Conditions))
    TriggerAddAction(gg_trg_NaxPosadka, Trig_PosadkaNax_Actions)
end
--===========================================================================
-- Trigger: NaxFly
--===========================================================================
function Trig_NaxFly_Conditions()
    return GetSpellAbilityId() == NaxAbilityAp
    
end
function Trig_NaxFly_Actions()
    local u= GetTriggerUnit()
    RemoveUnit(LoadUnitHandle(Hash, StringHash("Nax"), 1))
    FlushChildHashtable(Hash, StringHash("Nax"))
    SetUnitMoveSpeed(u, GetUnitDefaultMoveSpeed(u))
    --???? ????????
    BlzSetUnitRealFieldBJ(u, UNIT_RF_FLY_HEIGHT, 400.00)
    SetUnitFlyHeightBJ(u, 400.00, 55.00)
    
    ShowUnit(gg_unit_n003_0126, false)
    UnitRemoveAbility(u, FourCC('A1M6'))
    UnitRemoveAbility(u, FourCC('A1GE'))
    UnitAddAbility(u, NaxAbilityDown)
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.15)
    BlzStartUnitAbilityCooldown(u, NaxAbilityDown, 15)
    UnitRemoveAbility(u, NaxAbilityAp)
    
    WaygateActivateBJ(false, gg_unit_n003_0126)
    
    --call UnitAddAbility( u, 'A1F3')
    --call UnitRemoveAbility(u,'A0HY')
    
    --call DisplayTextToPlayer(Player(0),0,0," - "+R2S(GetUnitMoveSpeed(u)))
    WaygateActivate(gg_unit_n003_0126, false)
    
    
    u=nil
end
--===========================================================================
function InitTrig_NaxFly()
    gg_trg_NaxFly=CreateTrigger()
    
    
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_NaxFly, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER )
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_NaxFly, EVENT_PLAYER_UNIT_ISSUED_ORDER )
    
    
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_NaxFly, EVENT_PLAYER_UNIT_SPELL_FINISH )
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxFly, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_NaxFly, EVENT_PLAYER_UNIT_SPELL_EFFECT )
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_NaxFly, EVENT_PLAYER_UNIT_SPELL_ENDCAST )
    TriggerAddCondition(gg_trg_NaxFly, Condition(Trig_NaxFly_Conditions))
    TriggerAddAction(gg_trg_NaxFly, Trig_NaxFly_Actions)
end
--===========================================================================
-- Trigger: NaxDiy
--===========================================================================
function Trig_NaxDiy_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00D')
end
function Trig_NaxDiy_Func002A()
    KillUnit(GetEnumUnit())
end
function Trig_NaxDiy_Func003A()
    RemoveUnit(GetEnumUnit())
end
function Trig_NaxDiy_Actions()
    ForGroupBJ(GetUnitsInRectAll(gg_rct_Naxramas), Trig_NaxDiy_Func002A)
    ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('n066')), Trig_NaxDiy_Func003A)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_NaxDiy()
    gg_trg_NaxDiy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxDiy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_NaxDiy, Condition(Trig_NaxDiy_Conditions))
    TriggerAddAction(gg_trg_NaxDiy, Trig_NaxDiy_Actions)
end
--===========================================================================
-- Trigger: OwnerTurtle
--===========================================================================
function Trig_OwnerTurtle_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0O5')
end
function Trig_OwnerTurtle_Actions()
    SetUnitOwner(gg_unit_e00E_0085, GetOwningPlayer(GetKillingUnit()), true)
    SetPlayerAbilityAvailableBJ(true, TurtleAbilityDown, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, TurtleAbilityDown, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, TurtleAbilityAp, GetOwningPlayer(GetKillingUnit()))
    SetPlayerAbilityAvailableBJ(false, TurtleAbilityAp, GetOwningPlayer(GetTriggerUnit()))
    
    
end
--===========================================================================
function InitTrig_OwnerTurtle()
    gg_trg_OwnerTurtle=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OwnerTurtle, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_OwnerTurtle, Condition(Trig_OwnerTurtle_Conditions))
    TriggerAddAction(gg_trg_OwnerTurtle, Trig_OwnerTurtle_Actions)
end
--===========================================================================
-- Trigger: TurtleStart
--===========================================================================
function Trig_TurtleStart_Copy_Func002A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A1M1'), GetEnumPlayer())
end
function Trig_TurtleStart_Actions()
    IssuePointOrderLocBJ(gg_unit_e00E_0085, "flamestrike", GetUnitLoc(gg_unit_e00E_0085))
    ForForce(udg_AllPlayers, Trig_TurtleStart_Copy_Func002A)
    WaygateSetDestinationLocBJ(gg_unit_n003_0090, GetUnitLoc(gg_unit_e00E_0085))
    WaygateActivateBJ(true, gg_unit_n003_0090)
    WaygateSetDestinationLocBJ(gg_unit_n003_0090, GetUnitLoc(gg_unit_e00E_0085))
end
--===========================================================================
function InitTrig_TurtleStart()
    gg_trg_TurtleStart=CreateTrigger()
    TriggerAddAction(gg_trg_TurtleStart, Trig_TurtleStart_Actions)
end
--===========================================================================
-- Trigger: TurtlePosadka
--===========================================================================
function Trig_PosadkaTurtle_Conditions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    return GetSpellAbilityId() == TurtleAbilityDown and CheckPosition(GetSpellTargetX() , GetSpellTargetY() , 15) and CheckNearCapitals(GetTriggerUnit())
end
function Trig_PosadkaTurtle_Actions()
    local u= GetTriggerUnit()
    local u2= CreateUnit(Player(PLAYER_NEUTRAL_PASSIVE), FourCC('n075'), GetUnitX(u), GetUnitY(u) + 65, 0.00)
    SetUnitMoveSpeed(u, 0.0)
    SaveUnitHandle(Hash, StringHash("Turtle"), 1, u2)
    
    --call DisplayTextToPlayer(Player(0),0,0," - ")
    AddUnitAnimationProperties(u, "Swim", false)
    UnitAddAbility(u, FourCC('A1M6'))
    UnitAddAbility(u, FourCC('A1GE'))
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.00)
   
    UnitAddAbility(u, TurtleAbilityAp)
    BlzStartUnitAbilityCooldown(u, TurtleAbilityAp, 15)
    UnitRemoveAbility(u, TurtleAbilityDown)
    
    
    
    ShowUnit(gg_unit_n003_0090, true)
    
    --call UnitRemoveAbilityBJ( 'A1F3', u )
    --call UnitAddAbility(u,'A0HY')
    
    WaygateActivate(gg_unit_n003_0090, true)
    WaygateActivate(u2, true)
    MoveRectTo(gg_rct_TurtleOut, GetUnitX(u), GetUnitY(u))
    WaygateSetDestination(gg_unit_n003_0090, GetRectCenterX(gg_rct_TurtleOut), GetRectCenterY(gg_rct_TurtleOut))
    WaygateSetDestination(u2, GetRectCenterX(gg_rct_TurtleIn), GetRectCenterY(gg_rct_TurtleIn))
    WaygateActivate(u2, true)
    WaygateActivate(gg_unit_n003_0090, true)
    u2=nil
    u=nil
end
--===========================================================================
function InitTrig_TurtlePosadka()
    gg_trg_TurtlePosadka=CreateTrigger()
    
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_TurtlePosadka, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_TurtlePosadka, Condition(Trig_PosadkaTurtle_Conditions))
    TriggerAddAction(gg_trg_TurtlePosadka, Trig_PosadkaTurtle_Actions)
end
--===========================================================================
-- Trigger: TurtleSwim
--===========================================================================
function Trig_TurtleSwim_Conditions()
    return GetSpellAbilityId() == TurtleAbilityAp
    
end
function Trig_TurtleSwim_Actions()
    local u= GetTriggerUnit()
    RemoveUnit(LoadUnitHandle(Hash, StringHash("Turtle"), 1))
    FlushChildHashtable(Hash, StringHash("Turtle"))
    SetUnitMoveSpeed(u, GetUnitDefaultMoveSpeed(u))
    
    AddUnitAnimationProperties(u, "Swim", true)
    ShowUnit(gg_unit_n003_0090, false)
    UnitRemoveAbility(u, FourCC('A1M6'))
    UnitRemoveAbility(u, FourCC('A1GE'))
    UnitAddAbility(u, TurtleAbilityDown)
    BlzSetUnitRealFieldBJ(u, UNIT_RF_TURN_RATE, 0.15)
    BlzStartUnitAbilityCooldown(u, TurtleAbilityDown, 15)
    UnitRemoveAbility(u, TurtleAbilityAp)
    
    WaygateActivateBJ(false, gg_unit_n003_0090)
    
    --call UnitAddAbility( u, 'A1F3')
    --call UnitRemoveAbility(u,'A0HY')
    
    --call DisplayTextToPlayer(Player(0),0,0," - "+R2S(GetUnitMoveSpeed(u)))
    WaygateActivate(gg_unit_n003_0090, false)
    
    
    u=nil
end
--===========================================================================
function InitTrig_TurtleSwim()
    gg_trg_TurtleSwim=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TurtleSwim, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_TurtleSwim, Condition(Trig_TurtleSwim_Conditions))
    TriggerAddAction(gg_trg_TurtleSwim, Trig_TurtleSwim_Actions)
end
--===========================================================================
-- Trigger: TurtleDiy
--===========================================================================
function Trig_TurtleDiy_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00E')
end
function Trig_TurtleDiy_Actions()
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TurtleIsland), Trig_NaxDiy_Func002A)
    ForGroupBJ(GetUnitsOfTypeIdAll(FourCC('n075')), Trig_NaxDiy_Func003A)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_TurtleDiy()
    gg_trg_TurtleDiy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TurtleDiy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_TurtleDiy, Condition(Trig_TurtleDiy_Conditions))
    TriggerAddAction(gg_trg_TurtleDiy, Trig_TurtleDiy_Actions)
end
--===========================================================================
-- Trigger: TurtleOut
--===========================================================================
function Trig_TurtleOut_Conditions()
    return GetTriggerUnit() == gg_unit_n003_0090
end
function Trig_TurtleOut_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_TurtleOut , 800)
end
--===========================================================================
function InitTrig_TurtleOut()
    gg_trg_TurtleOut=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TurtleOut, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_TurtleOut, Condition(Trig_TurtleOut_Conditions))
    TriggerAddAction(gg_trg_TurtleOut, Trig_TurtleOut_Actions)
end
--===========================================================================
-- Trigger: DalIn Copy
--===========================================================================
function Trig_DalIn_Copy_Actions()
    TeleportUnits(GetTriggerUnit() , gg_rct_TurtleIn , 800)
end
--===========================================================================
function InitTrig_DalIn_Copy()
    gg_trg_DalIn_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalIn_Copy, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DalIn_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0HY') then return end
        if not (GetUnitTypeId(GetTriggerUnit()) == FourCC('n075')) then return end
        Trig_DalIn_Copy_Actions()
    end)
end
--===========================================================================
