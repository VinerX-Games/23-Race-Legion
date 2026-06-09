
--===========================================================================
-- Trigger: SilitidsOn
--===========================================================================
function Trig_SilitidsOn_Actions()
    EnableTrigger(gg_trg_ChoseLich)
    EnableTrigger(gg_trg_ChoseUnitsOld)
    
    --call EnableTrigger( gg_trg_TrutenStartUpgrade )
    EnableTrigger(gg_trg_LichStartUpgrade)
    
    EnableTrigger(gg_trg_LichinkaFinish)
    EnableTrigger(gg_trg_KokonDead2)
    
    EnableTrigger(gg_trg_MainSpawn2)
    EnableTrigger(gg_trg_LichDead)
    EnableTrigger(gg_trg_YleyDead)
    --call EnableTrigger( gg_trg_SpawnTimer )
    EnableTrigger(gg_trg_Antennu)
    EnableTrigger(gg_trg_AutoPolet)
    EnableTrigger(gg_trg_FastKokon)
    EnableTrigger(gg_trg_FireAutoCast)
    
    EnableTrigger(gg_trg_AcidMissleF)
    EnableTrigger(gg_trg_AcidMissleB)
    EnableTrigger(gg_trg_AcidMissleC)
    EnableTrigger(gg_trg_ParazitF)
    EnableTrigger(gg_trg_ParazitB)
    EnableTrigger(gg_trg_ParazitC)
    EnableTrigger(gg_trg_PlodovitostOsaB)
    EnableTrigger(gg_trg_PlodovitostOsaC)
    EnableTrigger(gg_trg_PlodovitostVoinaB)
    EnableTrigger(gg_trg_PlodovitostVoinaC)
    
    EnableTrigger(gg_trg_KriliaF)
    EnableTrigger(gg_trg_KriliaB)
    EnableTrigger(gg_trg_KriliaC)
    EnableTrigger(gg_trg_DelimostF)
    EnableTrigger(gg_trg_DelimostB)
    EnableTrigger(gg_trg_DelimostC)
    
    EnableTrigger(gg_trg_SlizeF)
    EnableTrigger(gg_trg_SlizeB)
    EnableTrigger(gg_trg_SlizeC)
    EnableTrigger(gg_trg_TankB)
    EnableTrigger(gg_trg_TankC)
    EnableTrigger(gg_trg_TankF)
    
    
    
    
    
    EnableTrigger(gg_trg_QTunServe)
    EnableTrigger(gg_trg_QTunAye)
    EnableTrigger(gg_trg_TweenBrothers)
    EnableTrigger(gg_trg_TweenBrothersDead)
    EnableTrigger(gg_trg_TweenBrothersRev)
    
    EnableTrigger(gg_trg_CanselBuildingSil)
    EnableTrigger(gg_trg_StartBuildingSil)
    EnableTrigger(gg_trg_ChoseUnits2)
    EnableTrigger(gg_trg_SpawnLich)
    
    
end
--===========================================================================
function InitTrig_SilitidsOn()
    gg_trg_SilitidsOn=CreateTrigger()
    TriggerAddAction(gg_trg_SilitidsOn, Trig_SilitidsOn_Actions)
end
--===========================================================================
-- Trigger: StartSilitids
--===========================================================================
function Trig_StartSilitids_Func001A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A0KM'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0KN'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0IZ'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A1KF'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0KL'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A1KD'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('U024'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('U025'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('U023'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('U02R'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0MG'), 1, GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A1B7'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R088'), 5, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('e01P'), 0, GetEnumPlayer()) --Tank
end
function Trig_StartSilitids_Actions()
    ForForce(udg_AllPlayers, Trig_StartSilitids_Func001A)
end
--===========================================================================
function InitTrig_StartSilitids()
    gg_trg_StartSilitids=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartSilitids, 5.00)
    TriggerAddAction(gg_trg_StartSilitids, Trig_StartSilitids_Actions)
end
--===========================================================================
-- Trigger: QTunServe
--===========================================================================
function Trig_QTunServe_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0MG')
end
function Trig_QTunServe_Func003A()
    SetUnitOwner(GetEnumUnit(), GetOwningPlayer(GetTriggerUnit()), true)
end
function Trig_QTunServe_Func004A()
    SetPlayerTechMaxAllowedSwap(FourCC('h0MG'), 0, GetEnumPlayer())
end
function Trig_QTunServe_Func005001002()
    return IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups)
end
function Trig_QTunServe_Func005A()
    GroupRemoveUnitSimple(GetEnumUnit(), udg_StolicaGroups)
    ReplaceUnitBJ(GetEnumUnit(), GetUnitTypeId(GetEnumUnit()), bj_UNIT_STATE_METHOD_RELATIVE)
end
function Trig_QTunServe_Func009A()
    UnitShareVisionBJ(true, gg_unit_n03D_0666, GetEnumPlayer())
end
function Trig_QTunServe_Actions()
    RemoveUnit(GetTrainedUnit())
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_38642")
    ForGroupBJ(GetUnitsInRectOfPlayer(gg_rct_Ankirag, Player(PLAYER_NEUTRAL_AGGRESSIVE)), Trig_QTunServe_Func003A)
    ForForce(GetPlayersAll(), Trig_QTunServe_Func004A)
    ForGroupBJ(GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(Trig_QTunServe_Func005001002)), Trig_QTunServe_Func005A)
    GroupAddUnitSimple(gg_unit_n03D_0666, udg_StolicaGroups)
    BlzSetUnitStringFieldBJ(gg_unit_n03D_0666, UNIT_SF_NAME, "cffd45e19r" .. GetUnitName(gg_unit_n03D_0666))
    TriggerRegisterUnitEvent(gg_trg_StolicaAttacked, gg_unit_n03D_0666, EVENT_UNIT_ATTACKED)
    ForForce(GetPlayersAll(), Trig_QTunServe_Func009A)
    SetUnitAbilityLevelSwapped(FourCC('A0W0'), gg_unit_n03D_0666, 2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_QTunServe()
    gg_trg_QTunServe=CreateTrigger()
    DisableTrigger(gg_trg_QTunServe)
    TriggerRegisterAnyUnitEventBJ(gg_trg_QTunServe, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_QTunServe, Condition(Trig_QTunServe_Conditions))
    TriggerAddAction(gg_trg_QTunServe, Trig_QTunServe_Actions)
end
--===========================================================================
-- Trigger: QTunAye
--===========================================================================
function Trig_QTunAye_Actions()
    local u= CreateUnit(GetOwningPlayer(GetTriggerUnit()), FourCC('oeye'), GetSpellTargetX(), GetSpellTargetY(), 0)
    UnitApplyTimedLife(u, FourCC('BTLF'), 1200)
    u=nil
end
--===========================================================================
function InitTrig_QTunAye()
    gg_trg_QTunAye=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QTunAye, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_QTunAye, function()
        if GetSpellAbilityId() ~= FourCC('A1B8') then return end
        Trig_QTunAye_Actions()
    end)
end
--===========================================================================
-- Trigger: ChoseLich
--===========================================================================
function Trig_ChoseLich_Conditions()
end
function HaveSpell()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0SW')) + GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0T1')) ~= 0
end
function Trig_ChoseLich_Func003002()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('e01I') and GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetFilterUnit())
end
function Trig_ChoseLich_Actions()
    local u1
    local u2
    local g= CreateGroup()
    local g2= CreateGroup()
    local i= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    ClearSelectionForPlayer(p)
    udg_Boolexpr = HaveSpell
    GroupEnumUnitsSelected(g, p, udg_Boolexpr)
    udg_Boolexpr = Trig_ChoseLich_Func003002
    
    while true do
        u1=FirstOfGroup(g)
        if u1 == nil or i >= 12 then break end
        
        GroupEnumUnitsInRangeCounted(g2, GetUnitX(u1), GetUnitY(u1), 1200, udg_Boolexpr, IMaxBJ(12 - i, 1))
        while true do
            u2=FirstOfGroup(g2)
            if u2 == nil or i >= 12 then break end
        
            SelectUnitAddForPlayer(u2, p)
    
            i=i + 1
            GroupRemoveUnit(g2, u2)
        end
         
    
        
        GroupRemoveUnit(g, u1)
    end
    
    
    
    
    
   
    DestroyGroup(g)
    DestroyGroup(g2)
    g=nil
    g2=nil
    u1=nil
    u2=nil
    
end
--===========================================================================
function InitTrig_ChoseLich()
    gg_trg_ChoseLich=CreateTrigger()
    DisableTrigger(gg_trg_ChoseLich)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChoseLich, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ChoseLich, function()
        if GetSpellAbilityId() ~= FourCC('A0SW') then return end
        if not Trig_ChoseLich_Conditions() then return end
        Trig_ChoseLich_Actions()
    end)
end
--===========================================================================
-- Trigger: ChoseUnits2
--===========================================================================
function OnlyOrganic()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('e02W') and not IsUnitType(GetFilterUnit(), UNIT_TYPE_PEON)
end
function Trig_ChoseUnits2_Actions()
    local g= CreateGroup()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    udg_LocalPosition3=GetSpellTargetLoc()
    udg_Boolexpr = OnlyOrganic
    GroupEnumUnitsInRange(g, GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), 400, udg_Boolexpr)
    GroupPointOrder(g, "attack", GetSpellTargetX(), GetSpellTargetY())
    
    DestroyGroup(g)
    g=nil
end
--===========================================================================
function InitTrig_ChoseUnits2()
    gg_trg_ChoseUnits2=CreateTrigger()
    DisableTrigger(gg_trg_ChoseUnits2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChoseUnits2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ChoseUnits2, function()
        if GetSpellAbilityId() ~= FourCC('A0SX') then return end
        Trig_ChoseUnits2_Actions()
    end)
end
--===========================================================================
-- Trigger: MainSpawn2
--===========================================================================
function Trig_MainSpawn2_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('e01H')
end
function spawnlich()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 1)
    local typeid= GetUnitTypeId(u)
    local uid= GetHandleId(u)
    local currentCount= LoadInteger(Hash, uid, 1)
    local x= GetUnitX(u)
    local y= GetUnitY(u)
    local u2
    local p= GetOwningPlayer(u)
    --call DisplayTextToPlayer(Player(0),0,0,""+I2S(currentCount))
    if currentCount < 3 and UnitAlive(u) then
        u2=CreateUnit(p, FourCC('e01I'), x, y, bj_UNIT_FACING)
        SetUnitTimeScale(u2, 0.25)
        SaveUnitHandle(Hash, GetHandleId(u2), 1, u)
        SaveBoolean(Hash, GetHandleId(u2), 2, true)
        currentCount=currentCount + 1
        if udg_AiControl[GetPlayerId(p)] then
            GroupAddUnit(udg_Ai_buildings[GetPlayerId(p)], u2)
            NumberAdd(GetPlayerId(p), FourCC('e01I'))
        end
        if typeid == FourCC('e021') then
            u2=CreateUnit(p, FourCC('e01I'), x, y, bj_UNIT_FACING)
            SetUnitTimeScale(u2, 0.25)
            SaveUnitHandle(Hash, GetHandleId(u2), 1, u)
            SaveBoolean(Hash, GetHandleId(u2), 2, true)
            currentCount=currentCount + 1
            if udg_AiControl[GetPlayerId(p)] then
                GroupAddUnit(udg_Ai_buildings[GetPlayerId(p)], u2)
                NumberAdd(GetPlayerId(p), FourCC('e01I'))
            end
        elseif typeid == FourCC('e020') then
            u2=CreateUnit(p, FourCC('e01I'), x, y, bj_UNIT_FACING)
            SetUnitTimeScale(u2, 0.25)
            SaveBoolean(Hash, GetHandleId(u2), 2, true)
            SaveUnitHandle(Hash, GetHandleId(u2), 1, u)
            if udg_AiControl[GetPlayerId(p)] then
                GroupAddUnit(udg_Ai_buildings[GetPlayerId(p)], u2)
                NumberAdd(GetPlayerId(p), FourCC('e01I'))
            end
            u2=CreateUnit(p, FourCC('e01I'), x, y, bj_UNIT_FACING)
            SetUnitTimeScale(u2, 0.25)
            SaveBoolean(Hash, GetHandleId(u2), 2, true)
            SaveUnitHandle(Hash, GetHandleId(u2), 1, u)
            if udg_AiControl[GetPlayerId(p)] then
                GroupAddUnit(udg_Ai_buildings[GetPlayerId(p)], u2)
                NumberAdd(GetPlayerId(p), FourCC('e01I'))
            end
            currentCount=currentCount + 2
        end
        
    else
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        t=nil
        SaveBoolean(Hash, uid, 1, false)
        p=nil
    end
    SaveInteger(Hash, uid, 1, currentCount)
    t=nil
    u=nil
    u2=nil
    p=nil
end
function Trig_MainSpawn2_Actions()
    local t= CreateTimer()
    local id= GetHandleId(t)
    local uid= GetHandleId(GetConstructedStructure())
    TimerStart(t, 25, true, spawnlich)
    SaveUnitHandle(Hash, id, 1, GetConstructedStructure())
    SaveInteger(Hash, uid, 1, 0)
    SaveBoolean(Hash, uid, 2, true)
    
    t=nil
    
end
--===========================================================================
function InitTrig_MainSpawn2()
    gg_trg_MainSpawn2=CreateTrigger()
    DisableTrigger(gg_trg_MainSpawn2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MainSpawn2, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_MainSpawn2, Condition(Trig_MainSpawn2_Conditions))
    TriggerAddAction(gg_trg_MainSpawn2, Trig_MainSpawn2_Actions)
end
--===========================================================================
-- Trigger: LichDead
--===========================================================================
function Trig_LichDead_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e01I') and LoadBoolean(Hash, GetHandleId(GetTriggerUnit()), 2)
end
function Trig_LichDead_Actions()
    local oldid= GetHandleId(GetTriggerUnit())
    local u2= LoadUnitHandle(Hash, oldid, 1)
    local id= GetHandleId(u2)
    local currentCount= LoadInteger(Hash, id, 1) - 1
    local t
    FlushChildHashtable(Hash, oldid)
    
    SaveInteger(Hash, id, 1, currentCount)
    
    
    if UnitAlive(u2) and currentCount < 3 and not LoadBoolean(Hash, id, 2) then
        t=CreateTimer()
        TimerStart(t, 25, true, spawnlich)
        SaveBoolean(Hash, id, 2, true)
    end
    
    
    t=nil
    u2=nil
end
--===========================================================================
function InitTrig_LichDead()
    gg_trg_LichDead=CreateTrigger()
    DisableTrigger(gg_trg_LichDead)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LichDead, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_LichDead, Condition(Trig_LichDead_Conditions))
    TriggerAddAction(gg_trg_LichDead, Trig_LichDead_Actions)
end
--===========================================================================
-- Trigger: YleyDead
--===========================================================================
function Trig_YleyDead_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e01H')
end
function Trig_YleyDead_Actions()
    FlushChildHashtable(Hash, GetHandleId(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_YleyDead()
    gg_trg_YleyDead=CreateTrigger()
    DisableTrigger(gg_trg_YleyDead)
    TriggerRegisterAnyUnitEventBJ(gg_trg_YleyDead, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_YleyDead, Condition(Trig_YleyDead_Conditions))
    TriggerAddAction(gg_trg_YleyDead, Trig_YleyDead_Actions)
end
--===========================================================================
-- Trigger: TweenBrothers
--===========================================================================
function Trig_TweenBrothers_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('U02R')
end
function SetCommonHP()
    
end
function Trig_TweenBrothers_Actions()
    --local unit u = 
    CreateUnit(GetOwningPlayer(GetTrainedUnit()), FourCC('U02S'), GetUnitX(GetTrainedUnit()), GetUnitY(GetTrainedUnit()), bj_UNIT_FACING)
    --call UnitAddAbility(u,'A187')
    --call IssueTargetOrder( u, "spiritlink", GetTrainedUnit( ) )
    --set u = null
end
--===========================================================================
function InitTrig_TweenBrothers()
    gg_trg_TweenBrothers=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TweenBrothers, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TweenBrothers, Condition(Trig_TweenBrothers_Conditions))
    TriggerAddAction(gg_trg_TweenBrothers, Trig_TweenBrothers_Actions)
end
--===========================================================================
-- Trigger: TweenChange
--===========================================================================
function Brothers()
    local id= GetUnitTypeId(GetFilterUnit())
    return id == FourCC('U02R') or id == FourCC('U02S')
end
function Trig_TweenChange_Actions()
    local u=  GetTriggerUnit()
    local id= GetUnitTypeId(u)
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    local bex = Brothers
    local u2
    local x= GetUnitX(u)
    local y= GetUnitY(u)
    local lvl= GetUnitAbilityLevel(u, FourCC('A188'))
    GroupEnumUnitsOfPlayer(g, p, bex)
    GroupRemoveUnit(g, GetTriggerUnit())
    u2=FirstOfGroup(g)
    if u2 ~= nil then
        SetUnitPosition(u, GetUnitX(u2), GetUnitY(u2))
        SetUnitPosition(u2, x, y)
        SetUnitLifePercentBJ(u, GetUnitLifePercent(u) + 12 * lvl)
        SetUnitLifePercentBJ(u2, GetUnitLifePercent(u2) + 12 * lvl)
    end
    BlzStartUnitAbilityCooldown(u, FourCC('A188'), 30)
    
    
    DestroyGroup(g)
    g=nil
    p=nil
    bex=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_TweenChange()
    gg_trg_TweenChange=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TweenChange, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_TweenChange, function()
        if GetSpellAbilityId() ~= FourCC('A188') then return end
        Trig_TweenChange_Actions()
    end)
end
--===========================================================================
-- Trigger: TweenBrothersRev
--===========================================================================
function Trig_TweenBrothersRev_Conditions()
    return GetUnitTypeId(GetRevivingUnit()) == FourCC('U02R') or GetUnitTypeId(GetRevivingUnit()) == FourCC('U02S')
end
function Trig_TweenBrothersRev_Actions()
    local u=  GetTriggerUnit()
    local id= GetUnitTypeId(u)
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    local bex = Brothers
    local u2
    
    GroupEnumUnitsOfPlayer(g, p, bex)
    GroupRemoveUnit(g, u)
    u2=FirstOfGroup(g)
    
    if u2 ~= nil then
        ReviveHero(u2, GetUnitX(u), GetUnitY(u), false)
        UnitAddAbility(u, FourCC('A187'))
        IssueTargetOrder(u, "spiritlink", u2)
        UnitAddAbility(u2, FourCC('A187'))
        IssueTargetOrder(u2, "spiritlink", u)
    end
    DestroyGroup(g)
    g=nil
    p=nil
    bex=nil
    u=nil
    u2=nil
    
    
end
--===========================================================================
function InitTrig_TweenBrothersRev()
    gg_trg_TweenBrothersRev=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TweenBrothersRev, EVENT_PLAYER_HERO_REVIVE_FINISH)
    TriggerAddCondition(gg_trg_TweenBrothersRev, Condition(Trig_TweenBrothersRev_Conditions))
    TriggerAddAction(gg_trg_TweenBrothersRev, Trig_TweenBrothersRev_Actions)
end
--===========================================================================
-- Trigger: TweenBrothersDead
--===========================================================================
function Trig_TweenBrothersDead_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('U02R') or GetUnitTypeId(GetTriggerUnit()) == FourCC('U02S')
end
function Trig_TweenBrothersDead_Actions()
    local u=  GetTriggerUnit()
    local id= GetUnitTypeId(u)
    local p= GetOwningPlayer(u)
    local g= CreateGroup()
    local bex = Brothers
    local u2
    
    GroupEnumUnitsOfPlayer(g, p, bex)
    GroupRemoveUnit(g, u)
    u2=FirstOfGroup(g)
    
    if u2 ~= nil then
        KillUnit(u2)
    end
    DestroyGroup(g)
    g=nil
    p=nil
    bex=nil
    u=nil
    u2=nil
    
    
end
--===========================================================================
function InitTrig_TweenBrothersDead()
    gg_trg_TweenBrothersDead=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TweenBrothersDead, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_TweenBrothersDead, Condition(Trig_TweenBrothersDead_Conditions))
    TriggerAddAction(gg_trg_TweenBrothersDead, Trig_TweenBrothersDead_Actions)
end
--===========================================================================
-- Trigger: StartBuildingSil
--===========================================================================
function Trig_StartBuildingSil_Conditions()
    local id= GetUnitTypeId(GetConstructingStructure())
    return id == FourCC('e01J') or id == FourCC('e01J') or id == FourCC('e01L') or id == FourCC('eo1M') or id == FourCC('e01H') or id == FourCC('eo1K')
end
function Trig_StartBuildingSil_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    disincome[pi]=disincome[pi] - GetUnitGoldCost(FourCC('e01G')) * 0.15 * 0.5
    
    UpdateGraf(pi)
    
end
--===========================================================================
function InitTrig_StartBuildingSil()
    gg_trg_StartBuildingSil=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartBuildingSil, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_StartBuildingSil, Condition(Trig_StartBuildingSil_Conditions))
    TriggerAddAction(gg_trg_StartBuildingSil, Trig_StartBuildingSil_Actions)
end
--===========================================================================
-- Trigger: SlowAnimation
--===========================================================================
function Trig_SlowAnimation_Conditions()
    gTarget=GetConstructedStructure()
    gInt=GetUnitTypeId(gTarget)
    return gInt == FourCC('e01J') or gInt == FourCC('e01J') or gInt == FourCC('e01L') or gInt == FourCC('eo1M') or gInt == FourCC('e01H') or gInt == FourCC('eo1K')
end
function Trig_SlowAnimation_Actions()
    SetUnitTimeScale(gTarget, 0.15)
    --if gInt=='eo1K' then
    --    call SetUnitAnimation( null, "stand" )
   -- endif
end
--===========================================================================
function InitTrig_SlowAnimation()
    gg_trg_SlowAnimation=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SlowAnimation, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_SlowAnimation, Condition(Trig_SlowAnimation_Conditions))
    TriggerAddAction(gg_trg_SlowAnimation, Trig_SlowAnimation_Actions)
end
--===========================================================================
-- Trigger: CanselBuildingSil
--===========================================================================
function Trig_CanselBuildingSil_Conditions()
    local id= GetUnitTypeId(GetTriggerUnit())
    
    return id == FourCC('e01J') or id == FourCC('e01J') or id == FourCC('e01L') or id == FourCC('eo1M') or id == FourCC('e01H') or id == FourCC('eo1K') --FourCC('e01G')
end
function Trig_CanselBuildingSil_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    
    --set disincome[pi]=disincome[pi]+6.25
    disincome[pi]=disincome[pi] + GetUnitGoldCost(FourCC('e01G')) * 0.15 * 0.5
    UpdateGraf(pi)
    
end
--===========================================================================
function InitTrig_CanselBuildingSil()
    gg_trg_CanselBuildingSil=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselBuildingSil, EVENT_PLAYER_UNIT_CONSTRUCT_CANCEL)
    TriggerAddCondition(gg_trg_CanselBuildingSil, Condition(Trig_CanselBuildingSil_Conditions))
    TriggerAddAction(gg_trg_CanselBuildingSil, Trig_CanselBuildingSil_Actions)
end
--===========================================================================
-- Trigger: LichStartUpgrade
--===========================================================================
function Trig_LichStartUpgrade_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1JE')) > 0
end
function Trig_LichStartUpgrade_Actions()
    --local integer i = GetPlayerId( GetOwningPlayer( GetTriggerUnit( ) ) )
    local uid= GetHandleId(GetTriggerUnit()) * 10
    local e= AddSpecialEffectTarget("DoodadsDungeonTerrainEggSackEggSack1.mdl", GetTriggerUnit(), "origin")
    BlzSetSpecialEffectColor(e, 255, 102, 0)
    SaveEffectHandle(Hash, uid, StringHash("Cocon"), e)
    e=nil
    
    local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if udg_AiControl[pi] then
        GroupRemoveUnit(udg_Ai_buildings[pi], GetTriggerUnit())
        NumberRem(pi, FourCC('e01I'))
    end
     
     
--    set udg_LocalPosition[15] = GetUnitLoc(GetTriggerUnit())
--    call CreateNUnitsAtLoc( 1, 'h0DE', GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[15], bj_UNIT_FACING )
--    call UnitApplyTimedLifeBJ( 75.00, 'BTLF', GetLastCreatedUnit() )
--    call SetUnitAnimation( GetLastCreatedUnit(), "stand" )
--    call GroupAddUnitSimple( GetLastCreatedUnit(), udg_Kokon )
--    set i = 0
--    call RemoveLocation(udg_LocalPosition[15])
end
--===========================================================================
function InitTrig_LichStartUpgrade()
    gg_trg_LichStartUpgrade=CreateTrigger()
    DisableTrigger(gg_trg_LichStartUpgrade)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LichStartUpgrade, EVENT_PLAYER_UNIT_UPGRADE_START)
    TriggerAddCondition(gg_trg_LichStartUpgrade, Condition(Trig_LichStartUpgrade_Conditions))
    TriggerAddAction(gg_trg_LichStartUpgrade, Trig_LichStartUpgrade_Actions)
end
--===========================================================================
-- Trigger: LichinkaFinish
--
-- ??????? ???????????, ????? ??????? ??????????? ???? ??????????? ? ?????. ????????? ? ???, ?????? ?????????, ?? ?????? ?????????
--===========================================================================
function Trig_LichinkaFinish_Conditions()
    gTriggerUnit=GetTriggerUnit()
    gPlayer=GetOwningPlayer(gTriggerUnit)
    return GetUnitAbilityLevel(gTriggerUnit, FourCC('A1JE')) > 0
end
function OrderAfterUleyFinish()
    local l= GetUnitRallyPoint(GetEnumUnit())
    udg_LocalPosition[17]=l
    if GetUnitTypeId(gTriggerUnit) == FourCC('e01G') then
        IssueTargetOrder(gTriggerUnit, "harvest", GetUnitRallyDestructable(GetEnumUnit()))
    else
        IssuePointOrderLoc(gTriggerUnit, "attack", l)
    end
    l=nil
end
function ItIsHive()
    local id= GetUnitTypeId(GetFilterUnit())
    return id == FourCC('e01H') or id == FourCC('e020') or id == FourCC('e021')
end
function Trig_LichinkaFinish_Actions()
    local i= GetPlayerId(gPlayer)
    --local unit u = gTriggerUnit 
    local id= GetUnitTypeId(gTriggerUnit)
    local e
    
    
    --???? ?????? ??????
    local oldid= GetHandleId(gTriggerUnit)
    local u2= LoadUnitHandle(Hash, oldid, 1)
    local id2= GetHandleId(u2)
    local currentCount= LoadInteger(Hash, id2, 1) - 1
    local t
    FlushChildHashtable(Hash, oldid)
    
    SaveInteger(Hash, id2, 1, currentCount)
    
    
    if UnitAlive(u2) and currentCount < 3 and not LoadBoolean(Hash, oldid, 1) then
        t=CreateTimer()
        TimerStart(t, 25, true, spawnlich)
        SaveUnitHandle(Hash, GetHandleId(t), 1, u2)
        SaveBoolean(Hash, id2, 1, true)
    end
    t=nil
    u2=nil
    
    
    
    --local real x = GetUnitX(gPlayer)
    --local real y = GetUnitY(u)
    -- ?? ?????? 2, ??? ??? ?????))) ? ??? ???????? ??? ?????????.
    
    
    --???? ???? ??????
--    if GetUnitTypeId(u) == 'e01I' then
--
--    endif
    
    --?? ???? ???????, ??? ??????????, ? ?? ????? ?? ?????, ?????? ???? ??? ??? ??? ?????????
    AddCountDis(gTriggerUnit , i)
    
    udg_LocalPosition[16]=GetUnitLoc(gTriggerUnit)
    udg_Boolexpr = Condition(ItIsHive)
    udg_LocalOtrad2=CreateGroup()
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition[16], 300, udg_Boolexpr)
    -- ???? ???? ???? ????? ???? ????
    ForGroup(udg_LocalOtrad2, OrderAfterUleyFinish)
    GroupClear(udg_LocalOtrad2)
    SetUnitLifePercentBJ(gTriggerUnit, 100)
    
    
    e=LoadEffectHandle(Hash, oldid * 10, StringHash("Cocon"))
    BlzPlaySpecialEffect(e, ANIM_TYPE_DEATH)
    RemoveEffectTimed(e , 1.5)
    FlushChildHashtable(Hash, oldid * 10)
    
    
    
    
    
    -- ???????
    -- ----
    if id == FourCC('e01G') then
        
        CreateNUnitsAtLoc(1, FourCC('e01G'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
        if udg_AiControl[i] then
            aiUnitJoins(GetLastCreatedUnit(), i)
        end
        udg_LocalPosition[18]=GetUnitLoc(GetLastCreatedUnit())
        udg_Boolexpr = Condition(ItIsHive)
        GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition[18], 300, udg_Boolexpr)
        
        IssueTargetDestructableOrder(GetLastCreatedUnit(), "harvest", GetUnitRallyDestructable(FirstOfGroup(udg_LocalOtrad2)))
        udg_LocalPosition[17]=GetUnitLoc(GetLastCreatedUnit())
        udg_Boolexpr = Condition(ItIsHive)
        GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition[17], 300, udg_Boolexpr)
        if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
            SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
        end
    
    
    
    
    
    -- ???????
    -- ----
    elseif id == FourCC('e01Z') then
        UnitAddAbilityBJ(FourCC('A0VH'), gTriggerUnit)
        
        
        CreateNUnitsAtLoc(1, FourCC('e01Z'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
        UnitAddAbilityBJ(FourCC('A0VH'), GetLastCreatedUnit())
        if udg_AiControl[i] then
            aiUnitJoins(GetLastCreatedUnit(), i)
        end
        
        IssuePointOrderLocBJ(GetLastCreatedUnit(), "attack", udg_LocalPosition[17])
        if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
            SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
        end
    
    
    
    
    -- ?????? ?1
    -- ----
    elseif id == FourCC('e02W') then
        CreateNUnitsAtLoc(1, FourCC('e02W'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
        if udg_AiControl[i] then
            aiUnitJoins(GetLastCreatedUnit(), i)
        end
        IssuePointOrderLocBJ(GetLastCreatedUnit(), "attack", udg_LocalPosition[17])
        
        
        -- ?????
        if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
            SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
        end
        
        
        
        -- ????????????
        if GetPlayerTechCountSimple(FourCC('R089'), GetOwningPlayer(gTriggerUnit)) == 1 then
            SetUnitAbilityLevelSwapped(FourCC('A0VH'), GetLastCreatedUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0VH'), gTriggerUnit, 2)
            
            CreateNUnitsAtLoc(1, FourCC('e02W'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
            if udg_AiControl[i] then
                aiUnitJoins(GetLastCreatedUnit(), i)
            end
            SetUnitAbilityLevelSwapped(FourCC('A0VH'), GetLastCreatedUnit(), 2)
            IssuePointOrderLocBJ(GetLastCreatedUnit(), "attack", udg_LocalPosition[17])
            if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
                SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
            
            end
        
            
        end
        
        
       
        
    
     
     
    -- ----
    -- ???
    elseif id == FourCC('e01Q') and GetPlayerTechCountSimple(FourCC('R08B'), GetOwningPlayer(gTriggerUnit)) == 1 then
        CreateNUnitsAtLoc(1, FourCC('e01Q'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
        if udg_AiControl[i] then
            aiUnitJoins(GetLastCreatedUnit(), i)
        end
        UnitAddAbilityBJ(FourCC('A0VH'), gTriggerUnit)
        UnitAddAbilityBJ(FourCC('A0VH'), GetLastCreatedUnit())
        
        IssuePointOrderLocBJ(GetLastCreatedUnit(), "attack", udg_LocalPosition[17])
        if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
            SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
        end
    
    
    --???? ????? ? ??? ??????? 
    elseif id == FourCC('e01U') then
        
        IssueImmediateOrder(gTriggerUnit, "parasiteon")
    --???? ???????
    elseif id == FourCC('e01T') then
        
        SetUnitManaBJ(gTriggerUnit, 125)
        BlzStartUnitAbilityCooldown(gTriggerUnit, FourCC('A1KG'), 50)
    
    end
    
    
    if udg_AiControl[i] then
        aiUnitJoins(gTriggerUnit, i)
    end
    
    -- ----
    -- ----
    GroupClear(udg_LocalOtrad2)
    RemoveLocation(udg_LocalPosition[16])
    RemoveLocation(udg_LocalPosition[17])
    RemoveLocation(udg_LocalPosition[18])
    e=nil
end
--===========================================================================
function InitTrig_LichinkaFinish()
    gg_trg_LichinkaFinish=CreateTrigger()
    DisableTrigger(gg_trg_LichinkaFinish)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LichinkaFinish, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LichinkaFinish, EVENT_PLAYER_UNIT_UPGRADE_CANCEL)
    TriggerAddCondition(gg_trg_LichinkaFinish, Condition(Trig_LichinkaFinish_Conditions))
    TriggerAddAction(gg_trg_LichinkaFinish, Trig_LichinkaFinish_Actions)
end
--===========================================================================
-- Trigger: KokonDead2
--===========================================================================
function Trig_KokonDead2_Conditions()
     return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1JE')) > 0
end
--
--function Trig_KokonDead2_Func002Func002C takes nothing returns boolean
--    if ( not ( R2I(DistanceBetweenPoints(udg_LocalPosition[17], udg_LocalPosition[16])) <= 25 ) ) then
--        return false
--    endif
--    return true
--endfunction
--
--function Trig_KokonDead2_Func002A takes nothing returns nothing
--    set udg_LocalPosition[17] = GetUnitLoc(GetEnumUnit())
--    if ( Trig_KokonDead2_Func002Func002C() ) then
--        call RemoveUnit( GetEnumUnit() )
--    else
--    endif
--    call RemoveLocation(udg_LocalPosition[17])
--endfunction
--
function Trig_KokonDead2_Actions()
    local u= GetTriggerUnit()
    DestroyEffect(LoadEffectHandle(Hash, GetHandleId(u) * 10, StringHash("Cocon")))
    FlushChildHashtable(Hash, GetHandleId(u) * 10)
    u=nil
--    set udg_LocalPosition[16] = GetUnitLoc(GetTriggerUnit())
--    call ForGroupBJ( udg_Kokon, function Trig_KokonDead2_Func002A )
--    call RemoveLocation(udg_LocalPosition[16])
end
--===========================================================================
function InitTrig_KokonDead2()
    gg_trg_KokonDead2=CreateTrigger()
    DisableTrigger(gg_trg_KokonDead2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KokonDead2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_KokonDead2, Condition(Trig_KokonDead2_Conditions))
    TriggerAddAction(gg_trg_KokonDead2, Trig_KokonDead2_Actions)
end
--===========================================================================
-- Trigger: SpellBook
--===========================================================================
function Trig_SpellBook_Actions()
    local u1
    local g= CreateGroup()
    local i= 0
    
    udg_Boolexpr = HaveSpell
    GroupEnumUnitsSelected(g, GetOwningPlayer(GetTriggerUnit()), udg_Boolexpr)
    while true do
            u1=FirstOfGroup(g)
            if u1 == nil then break end
            IssueImmediateOrder(u1, "spellbook")
            GroupRemoveUnit(g, u1)
    end
    
    
    
    
    DestroyGroup(g)
    u1=nil
    g=nil
end
--===========================================================================
function InitTrig_SpellBook()
    gg_trg_SpellBook=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellBook, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_SpellBook, function()
        if GetSpellAbilityId() ~= FourCC('A1AV') then return end
        Trig_SpellBook_Actions()
    end)
end
--===========================================================================
-- Trigger: SpawnLich
--===========================================================================
function Trig_SpawnLich_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local i
    local u2= CreateUnit(p, FourCC('e01I'), GetUnitX(u), GetUnitY(u), bj_UNIT_FACING)
   --call UnitAddAbility(u2,'A1JF') //?????????
    BlzSetUnitRealFieldBJ(u2, UNIT_RF_HIT_POINTS_REGENERATION_RATE, - 4.00)
    SetUnitTimeScale(u2, 0.25)
    u2=CreateUnit(p, FourCC('e01I'), GetUnitX(u), GetUnitY(u), bj_UNIT_FACING)
    BlzSetUnitRealFieldBJ(u2, UNIT_RF_HIT_POINTS_REGENERATION_RATE, - 4.00)
   -- call UnitAddAbility(u2,'A1JF') //?????????
    SetUnitTimeScale(u2, 0.25)
    i=GetUnitAbilityLevel(u, FourCC('A1AV'))
    
    if i >= 1 then
        --call DisplayTextToPlayer(Player(0),0,0,I2S(i))
        if i == 1 then
            IssueImmediateOrderById(u2, FourCC('e02W'))
        elseif i == 2 then
            IssueImmediateOrderById(u2, FourCC('e01Q'))
        elseif i == 3 then
            IssueImmediateOrderById(u2, FourCC('e01U'))
        elseif i == 4 then
            IssueImmediateOrderById(u2, FourCC('e01V'))
        elseif i == 5 then
            IssueImmediateOrderById(u2, FourCC('e01T'))
        elseif i == 6 then
            IssueImmediateOrderById(u2, FourCC('e01O'))
        elseif i == 7 then
            IssueImmediateOrderById(u2, FourCC('e01S'))
        elseif i == 8 then
            IssueImmediateOrderById(u2, FourCC('e01Z'))
        elseif i == 9 then
          
        elseif i == 10 then
            IssueImmediateOrderById(u2, FourCC('e01G'))
        end
    
    end
    
    
    
    p=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_SpawnLich()
    gg_trg_SpawnLich=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpawnLich, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_SpawnLich, function()
        if GetSpellAbilityId() ~= FourCC('A0ZU') then return end
        Trig_SpawnLich_Actions()
    end)
end
--===========================================================================
-- Trigger: SpawnTimer
--===========================================================================
function Trig_SpawnTimer_Func001A()
    local id= GetUnitTypeId(GetEnumUnit())
    udg_LocalPosition[16]=GetUnitLoc(GetEnumUnit())
    CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
    if id == FourCC('e021') then
        CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
        CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
    elseif id == FourCC('e020') then
        CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
        CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
        CreateUnitAtLoc(GetOwningPlayer(GetEnumUnit()), FourCC('e01I'), udg_LocalPosition[16], bj_UNIT_FACING)
        
    end
    RemoveLocation(udg_LocalPosition[16])
end
function Trig_SpawnTimer_Actions()
    ForGroup(udg_SpawnLichinok[1], Trig_SpawnTimer_Func001A)
end
--===========================================================================
function InitTrig_SpawnTimer()
    gg_trg_SpawnTimer=CreateTrigger()
    DisableTrigger(gg_trg_SpawnTimer)
    TriggerRegisterTimerExpireEventBJ(gg_trg_SpawnTimer, udg_SilitidTimer)
    TriggerAddAction(gg_trg_SpawnTimer, Trig_SpawnTimer_Actions)
end
--===========================================================================
-- Trigger: Antennu
--
-- ???????
--===========================================================================
function Trig_Antennu_Conditions()
    gTriggerUnit=GetConstructedStructure()
    return GetUnitTypeId(gTriggerUnit) == FourCC('e01X')
end
function Trig_Antennu_Actions()
    UnitAddAbility(gTriggerUnit, FourCC('A0J0'))
    SetUnitTimeScale(gTriggerUnit, 0.1)
end
--===========================================================================
function InitTrig_Antennu()
    gg_trg_Antennu=CreateTrigger()
    DisableTrigger(gg_trg_Antennu)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Antennu, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_Antennu, Condition(Trig_Antennu_Conditions))
    TriggerAddAction(gg_trg_Antennu, Trig_Antennu_Actions)
end
--===========================================================================
-- Trigger: AutoPolet
--===========================================================================
function Trig_AutoPolet_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "deathcoil", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoPolet()
    gg_trg_AutoPolet=CreateTrigger()
    DisableTrigger(gg_trg_AutoPolet)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoPolet, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoPolet, function()
        if GetSpellAbilityId() ~= FourCC('A0KL') then return end
        Trig_AutoPolet_Actions()
    end)
end
--===========================================================================
-- Trigger: FastKokon
--===========================================================================
function Trig_FastKokon_Actions()
    gUnit=GetTriggerUnit()
    SetUnitTimeScale(gUnit, 1)
    KillUnit(gUnit)
    CreateUnit(GetOwningPlayer(gUnit), FourCC('e02W'), GetUnitX(gUnit), GetUnitY(gUnit), 0.0)
    CreateUnit(GetOwningPlayer(gUnit), FourCC('e02W'), GetUnitX(gUnit), GetUnitY(gUnit), 0.0)
    CreateUnit(GetOwningPlayer(gUnit), FourCC('e02W'), GetUnitX(gUnit), GetUnitY(gUnit), 0.0)
end
--===========================================================================
function InitTrig_FastKokon()
    gg_trg_FastKokon=CreateTrigger()
    DisableTrigger(gg_trg_FastKokon)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FastKokon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FastKokon, function()
        if GetSpellAbilityId() ~= FourCC('A0ML') then return end
        Trig_FastKokon_Actions()
    end)
end
--===========================================================================
-- Trigger: FireAutoCast
--===========================================================================
function Trig_FireAutoCast_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e01T')
end
function Trig_FireAutoCast_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "faeriefireon")
end
--===========================================================================
function InitTrig_FireAutoCast()
    gg_trg_FireAutoCast=CreateTrigger()
    DisableTrigger(gg_trg_FireAutoCast)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireAutoCast, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_FireAutoCast, Condition(Trig_FireAutoCast_Conditions))
    TriggerAddAction(gg_trg_FireAutoCast, Trig_FireAutoCast_Actions)
end
--===========================================================================
-- Trigger: AcidMissleF
--===========================================================================
function Trig_AcidMissleF_Conditions()
    return GetResearched() == FourCC('R08E')
end
function Trig_AcidMissleF_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A1KF'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_AcidMissleF()
    gg_trg_AcidMissleF=CreateTrigger()
    DisableTrigger(gg_trg_AcidMissleF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AcidMissleF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AcidMissleF, Condition(Trig_AcidMissleF_Conditions))
    TriggerAddAction(gg_trg_AcidMissleF, Trig_AcidMissleF_Actions)
end
--===========================================================================
-- Trigger: AcidMissleB
--===========================================================================
function Trig_AcidMissleB_Conditions()
    return GetResearched() == FourCC('R08E')
end
function Trig_AcidMissleB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08F'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_AcidMissleB()
    gg_trg_AcidMissleB=CreateTrigger()
    DisableTrigger(gg_trg_AcidMissleB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AcidMissleB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_AcidMissleB, Condition(Trig_AcidMissleB_Conditions))
    TriggerAddAction(gg_trg_AcidMissleB, Trig_AcidMissleB_Actions)
end
--===========================================================================
-- Trigger: AcidMissleC
--===========================================================================
function Trig_AcidMissleC_Conditions()
    return GetResearched() == FourCC('R08E')
end
function Trig_AcidMissleC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08F'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_AcidMissleC()
    gg_trg_AcidMissleC=CreateTrigger()
    DisableTrigger(gg_trg_AcidMissleC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AcidMissleC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_AcidMissleC, Condition(Trig_AcidMissleC_Conditions))
    TriggerAddAction(gg_trg_AcidMissleC, Trig_AcidMissleC_Actions)
end
--===========================================================================
-- Trigger: ParazitF
--===========================================================================
function Trig_ParazitF_Conditions()
    return GetResearched() == FourCC('R08F')
end
function Trig_ParazitF_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0IZ'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ParazitF()
    gg_trg_ParazitF=CreateTrigger()
    DisableTrigger(gg_trg_ParazitF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ParazitF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_ParazitF, Condition(Trig_ParazitF_Conditions))
    TriggerAddAction(gg_trg_ParazitF, Trig_ParazitF_Actions)
end
--===========================================================================
-- Trigger: ParazitB
--===========================================================================
function Trig_ParazitB_Conditions()
    return GetResearched() == FourCC('R08F')
end
function Trig_ParazitB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08E'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ParazitB()
    gg_trg_ParazitB=CreateTrigger()
    DisableTrigger(gg_trg_ParazitB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ParazitB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_ParazitB, Condition(Trig_ParazitB_Conditions))
    TriggerAddAction(gg_trg_ParazitB, Trig_ParazitB_Actions)
end
--===========================================================================
-- Trigger: ParazitC
--===========================================================================
function Trig_ParazitC_Conditions()
    return GetResearched() == FourCC('R08F')
end
function Trig_ParazitC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08E'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ParazitC()
    gg_trg_ParazitC=CreateTrigger()
    DisableTrigger(gg_trg_ParazitC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ParazitC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_ParazitC, Condition(Trig_ParazitC_Conditions))
    TriggerAddAction(gg_trg_ParazitC, Trig_ParazitC_Actions)
end
--===========================================================================
-- Trigger: PlodovitostOsaB
--===========================================================================
function Trig_PlodovitostOsaB_Conditions()
    return GetResearched() == FourCC('R08B')
end
function Trig_PlodovitostOsaB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08A'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PlodovitostOsaB()
    gg_trg_PlodovitostOsaB=CreateTrigger()
    DisableTrigger(gg_trg_PlodovitostOsaB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PlodovitostOsaB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_PlodovitostOsaB, Condition(Trig_PlodovitostOsaB_Conditions))
    TriggerAddAction(gg_trg_PlodovitostOsaB, Trig_PlodovitostOsaB_Actions)
end
--===========================================================================
-- Trigger: PlodovitostOsaC
--===========================================================================
function Trig_PlodovitostOsaC_Conditions()
    return GetResearched() == FourCC('R08B')
end
function Trig_PlodovitostOsaC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08A'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PlodovitostOsaC()
    gg_trg_PlodovitostOsaC=CreateTrigger()
    DisableTrigger(gg_trg_PlodovitostOsaC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PlodovitostOsaC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_PlodovitostOsaC, Condition(Trig_PlodovitostOsaC_Conditions))
    TriggerAddAction(gg_trg_PlodovitostOsaC, Trig_PlodovitostOsaC_Actions)
end
--===========================================================================
-- Trigger: PlodovitostVoinaB
--===========================================================================
function Trig_PlodovitostVoinaB_Conditions()
    return GetResearched() == FourCC('R089')
end
function Trig_PlodovitostVoinaB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R085'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PlodovitostVoinaB()
    gg_trg_PlodovitostVoinaB=CreateTrigger()
    DisableTrigger(gg_trg_PlodovitostVoinaB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PlodovitostVoinaB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_PlodovitostVoinaB, Condition(Trig_PlodovitostVoinaB_Conditions))
    TriggerAddAction(gg_trg_PlodovitostVoinaB, Trig_PlodovitostVoinaB_Actions)
end
--===========================================================================
-- Trigger: PlodovitostVoinaC
--===========================================================================
function Trig_PlodovitostVoinaC_Conditions()
    return GetResearched() == FourCC('R089')
end
function Trig_PlodovitostVoinaC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R085'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PlodovitostVoinaC()
    gg_trg_PlodovitostVoinaC=CreateTrigger()
    DisableTrigger(gg_trg_PlodovitostVoinaC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PlodovitostVoinaC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_PlodovitostVoinaC, Condition(Trig_PlodovitostVoinaC_Conditions))
    TriggerAddAction(gg_trg_PlodovitostVoinaC, Trig_PlodovitostVoinaC_Actions)
end
--===========================================================================
-- Trigger: KriliaF
--===========================================================================
function Trig_KriliaF_Conditions()
    return GetResearched() == FourCC('R08A')
end
function Trig_KriliaF_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A1KD'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KriliaF()
    gg_trg_KriliaF=CreateTrigger()
    DisableTrigger(gg_trg_KriliaF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KriliaF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_KriliaF, Condition(Trig_KriliaF_Conditions))
    TriggerAddAction(gg_trg_KriliaF, Trig_KriliaF_Actions)
end
--===========================================================================
-- Trigger: KriliaB
--===========================================================================
function Trig_KriliaB_Conditions()
    return GetResearched() == FourCC('R08A')
end
function Trig_KriliaB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KriliaB()
    gg_trg_KriliaB=CreateTrigger()
    DisableTrigger(gg_trg_KriliaB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KriliaB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_KriliaB, Condition(Trig_KriliaB_Conditions))
    TriggerAddAction(gg_trg_KriliaB, Trig_KriliaB_Actions)
end
--===========================================================================
-- Trigger: KriliaC
--===========================================================================
function Trig_KriliaC_Conditions()
    return GetResearched() == FourCC('R08A')
end
function Trig_KriliaC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08B'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_KriliaC()
    gg_trg_KriliaC=CreateTrigger()
    DisableTrigger(gg_trg_KriliaC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KriliaC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_KriliaC, Condition(Trig_KriliaC_Conditions))
    TriggerAddAction(gg_trg_KriliaC, Trig_KriliaC_Actions)
end
--===========================================================================
-- Trigger: DelimostF
--===========================================================================
function Trig_DelimostF_Conditions()
    return GetResearched() == FourCC('R08C')
end
function Trig_DelimostF_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0KM'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DelimostF()
    gg_trg_DelimostF=CreateTrigger()
    DisableTrigger(gg_trg_DelimostF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_DelimostF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_DelimostF, Condition(Trig_DelimostF_Conditions))
    TriggerAddAction(gg_trg_DelimostF, Trig_DelimostF_Actions)
end
--===========================================================================
-- Trigger: DelimostB
--===========================================================================
function Trig_DelimostB_Conditions()
    return GetResearched() == FourCC('R08C')
end
function Trig_DelimostB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08D'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DelimostB()
    gg_trg_DelimostB=CreateTrigger()
    DisableTrigger(gg_trg_DelimostB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_DelimostB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_DelimostB, Condition(Trig_DelimostB_Conditions))
    TriggerAddAction(gg_trg_DelimostB, Trig_DelimostB_Actions)
end
--===========================================================================
-- Trigger: DelimostC
--===========================================================================
function Trig_DelimostC_Conditions()
    return GetResearched() == FourCC('R08C')
end
function Trig_DelimostC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08D'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DelimostC()
    gg_trg_DelimostC=CreateTrigger()
    DisableTrigger(gg_trg_DelimostC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_DelimostC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_DelimostC, Condition(Trig_DelimostC_Conditions))
    TriggerAddAction(gg_trg_DelimostC, Trig_DelimostC_Actions)
end
--===========================================================================
-- Trigger: SlizeF
--===========================================================================
function Trig_SlizeF_Conditions()
    return GetResearched() == FourCC('R08D')
end
function Trig_SlizeF_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0KN'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SlizeF()
    gg_trg_SlizeF=CreateTrigger()
    DisableTrigger(gg_trg_SlizeF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SlizeF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SlizeF, Condition(Trig_SlizeF_Conditions))
    TriggerAddAction(gg_trg_SlizeF, Trig_SlizeF_Actions)
end
--===========================================================================
-- Trigger: SlizeB
--===========================================================================
function Trig_SlizeB_Conditions()
    return GetResearched() == FourCC('R08D')
end
function Trig_SlizeB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08C'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SlizeB()
    gg_trg_SlizeB=CreateTrigger()
    DisableTrigger(gg_trg_SlizeB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SlizeB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SlizeB, Condition(Trig_SlizeB_Conditions))
    TriggerAddAction(gg_trg_SlizeB, Trig_SlizeB_Actions)
end
--===========================================================================
-- Trigger: SlizeC
--===========================================================================
function Trig_SlizeC_Conditions()
    return GetResearched() == FourCC('R08D')
end
function Trig_SlizeC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R08C'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SlizeC()
    gg_trg_SlizeC=CreateTrigger()
    DisableTrigger(gg_trg_SlizeC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SlizeC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SlizeC, Condition(Trig_SlizeC_Conditions))
    TriggerAddAction(gg_trg_SlizeC, Trig_SlizeC_Actions)
end
--===========================================================================
-- Trigger: TankB
--===========================================================================
function Trig_TankB_Conditions()
    return GetResearched() == FourCC('R085')
end
function Trig_TankB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R089'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_TankB()
    gg_trg_TankB=CreateTrigger()
    DisableTrigger(gg_trg_TankB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_TankB, Condition(Trig_TankB_Conditions))
    TriggerAddAction(gg_trg_TankB, Trig_TankB_Actions)
end
--===========================================================================
-- Trigger: TankC
--===========================================================================
function Trig_TankC_Conditions()
    return GetResearched() == FourCC('R085')
end
function Trig_TankC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R089'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_TankC()
    gg_trg_TankC=CreateTrigger()
    DisableTrigger(gg_trg_TankC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_TankC, Condition(Trig_TankC_Conditions))
    TriggerAddAction(gg_trg_TankC, Trig_TankC_Actions)
end
--===========================================================================
-- Trigger: TankF
--===========================================================================
function Trig_TankF_Conditions()
    return GetResearched() == FourCC('R085')
end
function Trig_TankF_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('e01P'), - 1, GetOwningPlayer(GetTriggerUnit())) --Tank
    SetPlayerTechMaxAllowedSwap(FourCC('e02W'), 0, GetOwningPlayer(GetTriggerUnit())) --Silit
end
--===========================================================================
function InitTrig_TankF()
    gg_trg_TankF=CreateTrigger()
    DisableTrigger(gg_trg_TankF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_TankF, Condition(Trig_TankF_Conditions))
    TriggerAddAction(gg_trg_TankF, Trig_TankF_Actions)
end