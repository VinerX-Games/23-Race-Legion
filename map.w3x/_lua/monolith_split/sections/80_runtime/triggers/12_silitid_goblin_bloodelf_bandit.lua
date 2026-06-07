    gg_trg_StartHorde=CreateTrigger()
    TriggerAddAction(gg_trg_StartHorde, Trig_StartHorde_Actions)
end
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
    if ( not ( GetUnitTypeId(GetTrainedUnit()) == FourCC('h0MG') ) ) then
        return false
    end
    return true
end
function Trig_QTunServe_Func003A()
    SetUnitOwner(GetEnumUnit(), GetOwningPlayer(GetTriggerUnit()), true)
end
function Trig_QTunServe_Func004A()
    SetPlayerTechMaxAllowedSwap(FourCC('h0MG'), 0, GetEnumPlayer())
end
function Trig_QTunServe_Func005001002()
    return ( IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups) == true )
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
    BlzSetUnitStringFieldBJ(gg_unit_n03D_0666, UNIT_SF_NAME, ( "cffd45e19r" + GetUnitName(gg_unit_n03D_0666) ))
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
        PauseTimer(t)
        DestroyTimer(t)
        t=nil
        SaveBoolean(Hash, uid, 1, false)
        FlushChildHashtable(Hash, id)
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
        SetUnitLifePercentBJ(u, ( GetUnitLifePercent(u) + 12 * lvl ))
        SetUnitLifePercentBJ(u2, ( GetUnitLifePercent(u2) + 12 * lvl ))
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
    udg_Boolexpr = ItIsHive
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
        udg_Boolexpr = ItIsHive
        GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition[18], 300, udg_Boolexpr)
        
        IssueTargetDestructableOrder(GetLastCreatedUnit(), "harvest", GetUnitRallyDestructable(FirstOfGroup(udg_LocalOtrad2)))
        udg_LocalPosition[17]=GetUnitLoc(GetLastCreatedUnit())
        udg_Boolexpr = ItIsHive
        GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition[17], 300, udg_Boolexpr)
        if IsUnitSelected(gTriggerUnit, GetOwningPlayer(gTriggerUnit)) then
            SelectUnitAddForPlayer(GetLastCreatedUnit(), gPlayer)
        else
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
        else
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
        
        
        
        -- ????????????
        if GetPlayerTechCountSimple(FourCC('R089'), GetOwningPlayer(gTriggerUnit)) == 1 then
            SetUnitAbilityLevelSwapped(FourCC('A0VH'), GetLastCreatedUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0VH'), gTriggerUnit, 2)
            
            CreateNUnitsAtLoc(1, FourCC('e02W'), gPlayer, udg_LocalPosition[16], bj_UNIT_FACING)
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
        else
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
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01T') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08E') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08E') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08F') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08F') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08F') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08B') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08B') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R089') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R089') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08A') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08A') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08A') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08C') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08C') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08C') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08D') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08D') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R08D') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R085') ) ) then
        return false
    end
    return true
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
    if ( not ( GetResearched() == FourCC('R085') ) ) then
        return false
    end
    return true
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
--===========================================================================
-- Trigger: GoblinsOn
--===========================================================================
function Trig_GoblinsOn_Actions()
    EnableTrigger(gg_trg_CorrupTrain)
    EnableTrigger(gg_trg_CorrupPlus)
    EnableTrigger(gg_trg_CorrupMinus)
    EnableTrigger(gg_trg_Potreblenie)
    EnableTrigger(gg_trg_PotreblenieTrain)
    
    EnableTrigger(gg_trg_Brac)
    EnableTrigger(gg_trg_BracResearch)
    EnableTrigger(gg_trg_BracTrain)
    EnableTrigger(gg_trg_PodjogResearch)
    EnableTrigger(gg_trg_PodjogTrain)
    EnableTrigger(gg_trg_PodruvResearc)
    EnableTrigger(gg_trg_PodruvTrain)
    
    EnableTrigger(gg_trg_Samopodruv)
    EnableTrigger(gg_trg_Samopodjog)
    EnableTrigger(gg_trg_Adrenalin)
    
    
    
    
    EnableTrigger(gg_trg_Pulimetchik)
    EnableTrigger(gg_trg_Ognemetchik)
    EnableTrigger(gg_trg_Raketchik)
    EnableTrigger(gg_trg_Medic)
    EnableTrigger(gg_trg_Sniper)
    EnableTrigger(gg_trg_Saper)
    EnableTrigger(gg_trg_Car)
    EnableTrigger(gg_trg_Vezdehod)
    EnableTrigger(gg_trg_Tank)
    EnableTrigger(gg_trg_FireTank)
    EnableTrigger(gg_trg_Arta)
    EnableTrigger(gg_trg_Meha)
    EnableTrigger(gg_trg_OgneMeha)
    EnableTrigger(gg_trg_Eczo)
    EnableTrigger(gg_trg_Super)
    EnableTrigger(gg_trg_Submarina)
    EnableTrigger(gg_trg_Podlodka1)
    
    EnableTrigger(gg_trg_FarmLoseG)
    EnableTrigger(gg_trg_FarmBuildG)
   -- call EnableTrigger( gg_trg_SpellRecharge )
   -- call EnableTrigger( gg_trg_IconAutoRocket )
 
    
    
    
end
--===========================================================================
function InitTrig_GoblinsOn()
    gg_trg_GoblinsOn=CreateTrigger()
    TriggerAddAction(gg_trg_GoblinsOn, Trig_GoblinsOn_Actions)
end
--===========================================================================
-- Trigger: StartG
--===========================================================================
function goblinsStartLimits_act()
    SetPlayerTechResearchedSwap(FourCC('R04O'), 1, GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0BD'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N018'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N01A'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('N019'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Nalc'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Ntin'), 1, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('Gmex'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Galh'), 1, GetEnumPlayer())
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('h06L'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06N'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06Q'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06O'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h078'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06M'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06P'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06U'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06Y'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06S'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06T'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00W'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00Y'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o00X'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06R'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06V'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h06W'), 0, GetEnumPlayer())
end
function goblinsStartLimits()
    ForForce(bj_FORCE_ALL_PLAYERS, goblinsStartLimits_act)
    ForForce(udg_Bots, goblinsStartLimits_act)
end
function Trig_StartG_Actions()
    goblinsStartLimits()
end
--===========================================================================
function InitTrig_StartG()
    gg_trg_StartG=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartG, 5.00)
    TriggerAddAction(gg_trg_StartG, Trig_StartG_Actions)
end
--===========================================================================
-- Trigger: GoblinSold
--===========================================================================
function Trig_GoblinSold_Conditions()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h073') ) ) then
        return false
    end
    return true
end
function Trig_GoblinSold_Func002Func001C()
    if ( not ( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetSoldUnit()) ) ) then
        return false
    end
    if ( not ( GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL) == true ) ) then
        return false
    end
    return true
end
function Trig_GoblinSold_Func002Func002C()
    if ( ( GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetSoldUnit()) ) ) then
        return true
    end
    if ( ( GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetSoldUnit()), ALLIANCE_SHARED_ADVANCED_CONTROL) == true ) ) then
        return true
    end
    return false
end
function Trig_GoblinSold_Func002C()
    if ( not Trig_GoblinSold_Func002Func002C() ) then
        return false
    end
    return true
end
function Trig_GoblinSold_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if ( Trig_GoblinSold_Func002C() ) then
        if ( Trig_GoblinSold_Func002Func001C() ) then
            SetUnitOwner(GetSoldUnit(), GetOwningPlayer(GetTriggerUnit()), true)
            AddCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetTriggerUnit())))
            DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
            GoldDifference[pi]=GoldDifference[pi] - GetUnitGoldCost(GetUnitTypeId(GetSoldUnit()))
            LumberDifference[pi]=LumberDifference[pi] - GetUnitWoodCost(GetUnitTypeId(GetSoldUnit()))
        else
        end
        udg_LocalPosition2=GetUnitRallyPoint(GetTriggerUnit())
        IssuePointOrderLocBJ(GetSoldUnit(), "move", udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition2)
    else
        RemoveUnit(GetSoldUnit())
        DelCountDis(GetSoldUnit() , GetPlayerId(GetOwningPlayer(GetSoldUnit())))
    end
end
--===========================================================================
function InitTrig_GoblinSold()
    gg_trg_GoblinSold=CreateTrigger()
    DisableTrigger(gg_trg_GoblinSold)
    TriggerRegisterAnyUnitEventBJ(gg_trg_GoblinSold, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_GoblinSold, Condition(Trig_GoblinSold_Conditions))
    TriggerAddAction(gg_trg_GoblinSold, Trig_GoblinSold_Actions)
end
--===========================================================================
-- Trigger: IconAutoRocket
--===========================================================================
function Trig_IconAutoRocket_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1N1')
end
function Trig_IconAutoRocket_Actions()
    UnitAddAbility(GetLearningUnit(), FourCC('A1N2'))
end
--===========================================================================
function InitTrig_IconAutoRocket()
    gg_trg_IconAutoRocket=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_IconAutoRocket, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_IconAutoRocket, Condition(Trig_IconAutoRocket_Conditions))
    TriggerAddAction(gg_trg_IconAutoRocket, Trig_IconAutoRocket_Actions)
end
--===========================================================================
-- Trigger: SpellRecharge
--===========================================================================
function Trig_SpellRecharge_Actions()
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A0DU'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N0'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N3'))
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1N1'))
    
end
--===========================================================================
function InitTrig_SpellRecharge()
    gg_trg_SpellRecharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellRecharge, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_SpellRecharge, function()
        if GetSpellAbilityId() ~= FourCC('A1N4') then return end
        Trig_SpellRecharge_Actions()
    end)
end
--===========================================================================
-- Trigger: CorrupTrain
--===========================================================================
function Trig_CorrupTrain_Conditions()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_CorrupTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_CorrupTrain()
    gg_trg_CorrupTrain=CreateTrigger()
    DisableTrigger(gg_trg_CorrupTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_CorrupTrain, Condition(Trig_CorrupTrain_Conditions))
    TriggerAddAction(gg_trg_CorrupTrain, Trig_CorrupTrain_Actions)
end
--===========================================================================
-- Trigger: CorrupPlus
--===========================================================================
function Trig_CorrupPlus_Func008A()
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
end
function Trig_CorrupPlus_Actions()
    local t= CreateTimer()
    local tid= GetHandleId(t)
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), p)
    SetPlayerTechResearchedSwap(FourCC('R04O'), ( GetPlayerTechCountSimple(FourCC('R04O'), p) + 1 ), p)
    
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, p, nil)
    ForGroupBJ(udg_LocalOtrad2, Trig_CorrupPlus_Func008A)
    GroupClear(udg_LocalOtrad2)
    
	local p2 = p
	TimerStart(t, 60, false, function()
		if GetPlayerTechCountSimple(FourCC('R04O'), p2) == 6 then
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		else
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		end
		DestroyTimer(t)
	end)
    
    
    t=nil
end
--===========================================================================
function InitTrig_CorrupPlus()
    gg_trg_CorrupPlus=CreateTrigger()
    DisableTrigger(gg_trg_CorrupPlus)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupPlus, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CorrupPlus, function()
        if GetSpellAbilityId() ~= FourCC('A0AS') then return end
        Trig_CorrupPlus_Actions()
    end)
end
--===========================================================================
-- Trigger: CorrupMinus
--===========================================================================
function Trig_CorrupMinus_Func008A()
    SetUnitAbilityLevelSwapped(FourCC('A0AW'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
    SetUnitAbilityLevelSwapped(FourCC('A0AV'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04O'), GetOwningPlayer(GetEnumUnit())))
end
function Trig_CorrupMinus_Actions()
    local t= CreateTimer()
    local tid= GetHandleId(t)
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A0AT'), p)
    SetPlayerTechResearchedSwap(FourCC('R04O'), ( GetPlayerTechCountSimple(FourCC('R04O'), p) - 1 ), p)
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, p, nil)
    ForGroupBJ(udg_LocalOtrad2, Trig_CorrupMinus_Func008A)
    GroupClear(udg_LocalOtrad2)
    
    
	local p2 = p
	TimerStart(t, 60, false, function()
		if GetPlayerTechCountSimple(FourCC('R04O'), p2) == 1 then
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
		else
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AS'), p2)
			SetPlayerAbilityAvailableBJ(true, FourCC('A0AT'), p2)
		end
		DestroyTimer(t)
	end)
    
   
    
    t=nil
end
--===========================================================================
function InitTrig_CorrupMinus()
    gg_trg_CorrupMinus=CreateTrigger()
    DisableTrigger(gg_trg_CorrupMinus)
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorrupMinus, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CorrupMinus, function()
        if GetSpellAbilityId() ~= FourCC('A0AT') then return end
        Trig_CorrupMinus_Actions()
    end)
end
--===========================================================================
-- Trigger: Potreblenie
--===========================================================================
function Trig_Potreblenie_Conditions()
    if ( not ( GetResearched() == FourCC('R04N') ) ) then
        return false
    end
    return true
end
function Trig_Potreblenie_Func001C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) == 6 ) ) then
        return false
    end
    return true
end
function Trig_Potreblenie_Func002002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0A5'), GetFilterUnit()) ~= 0 )
end
function Trig_Potreblenie_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A5'), GetEnumUnit(), ( GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) + 1 ))
end
function Trig_Potreblenie_Actions()
    if ( Trig_Potreblenie_Func001C() ) then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A5'), GetOwningPlayer(GetTriggerUnit()))
        return
    else
    end
    udg_Boolexpr = Trig_Potreblenie_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Potreblenie_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_Potreblenie()
    gg_trg_Potreblenie=CreateTrigger()
    DisableTrigger(gg_trg_Potreblenie)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Potreblenie, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Potreblenie, Condition(Trig_Potreblenie_Conditions))
    TriggerAddAction(gg_trg_Potreblenie, Trig_Potreblenie_Actions)
end
--===========================================================================
-- Trigger: PotreblenieTrain
--===========================================================================
function Trig_PotreblenieTrain_Conditions()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A0A5'), GetTriggerUnit()) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_PotreblenieTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A5'), GetEnumUnit(), ( GetPlayerTechCountSimple(FourCC('R04N'), GetOwningPlayer(GetTriggerUnit())) + 1 ))
end
--===========================================================================
function InitTrig_PotreblenieTrain()
    gg_trg_PotreblenieTrain=CreateTrigger()
    DisableTrigger(gg_trg_PotreblenieTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PotreblenieTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PotreblenieTrain, Condition(Trig_PotreblenieTrain_Conditions))
    TriggerAddAction(gg_trg_PotreblenieTrain, Trig_PotreblenieTrain_Actions)
end
--===========================================================================
-- Trigger: BracResearch
--===========================================================================
function Trig_BracResearch_Conditions()
    if ( not ( GetResearched() == FourCC('R05W') ) ) then
        return false
    end
    return true
end
function Trig_BracResearch_Func001C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())) == 6 ) ) then
        return false
    end
    return true
end
function Trig_BracResearch_Func002002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0A6'), GetFilterUnit()) ~= 0 )
end
function Trig_BracResearch_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A6'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())))
end
function Trig_BracResearch_Actions()
    if ( Trig_BracResearch_Func001C() ) then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A6'), GetOwningPlayer(GetTriggerUnit()))
        return
    else
    end
    udg_Boolexpr = Trig_BracResearch_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_BracResearch_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_BracResearch()
    gg_trg_BracResearch=CreateTrigger()
    DisableTrigger(gg_trg_BracResearch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BracResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BracResearch, Condition(Trig_BracResearch_Conditions))
    TriggerAddAction(gg_trg_BracResearch, Trig_BracResearch_Actions)
end
--===========================================================================
-- Trigger: BracTrain
--===========================================================================
function Trig_BracTrain_Conditions()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A0A6'), GetTriggerUnit()) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_BracTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A6'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R05W'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_BracTrain()
    gg_trg_BracTrain=CreateTrigger()
    DisableTrigger(gg_trg_BracTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BracTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_BracTrain, Condition(Trig_BracTrain_Conditions))
    TriggerAddAction(gg_trg_BracTrain, Trig_BracTrain_Actions)
end
--===========================================================================
-- Trigger: PodjogResearch
--===========================================================================
function Trig_PodjogResearch_Conditions()
    if ( not ( GetResearched() == FourCC('R04R') ) ) then
        return false
    end
    return true
end
function Trig_PodjogResearch_Func001C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())) == 6 ) ) then
        return false
    end
    return true
end
function Trig_PodjogResearch_Func002002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0AR'), GetFilterUnit()) ~= 0 )
end
function Trig_PodjogResearch_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0AR'), GetEnumUnit(), GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())))
end
function Trig_PodjogResearch_Actions()
    if ( Trig_PodjogResearch_Func001C() ) then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0AR'), GetOwningPlayer(GetTriggerUnit()))
        return
    else
    end
    udg_Boolexpr = Trig_PodjogResearch_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PodjogResearch_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_PodjogResearch()
    gg_trg_PodjogResearch=CreateTrigger()
    DisableTrigger(gg_trg_PodjogResearch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodjogResearch, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PodjogResearch, Condition(Trig_PodjogResearch_Conditions))
    TriggerAddAction(gg_trg_PodjogResearch, Trig_PodjogResearch_Actions)
end
--===========================================================================
-- Trigger: PodjogTrain
--===========================================================================
function Trig_PodjogTrain_Conditions()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A0AR'), GetTrainedUnit()) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_PodjogTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0AR'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04R'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_PodjogTrain()
    gg_trg_PodjogTrain=CreateTrigger()
    DisableTrigger(gg_trg_PodjogTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodjogTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PodjogTrain, Condition(Trig_PodjogTrain_Conditions))
    TriggerAddAction(gg_trg_PodjogTrain, Trig_PodjogTrain_Actions)
end
--===========================================================================
-- Trigger: PodruvResearc
--===========================================================================
function Trig_PodruvResearc_Conditions()
    if ( not ( GetResearched() == FourCC('R04Q') ) ) then
        return false
    end
    return true
end
function Trig_PodruvResearc_Func001C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())) == 6 ) ) then
        return false
    end
    return true
end
function Trig_PodruvResearc_Func002002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0A9'), GetFilterUnit()) ~= 0 )
end
function Trig_PodruvResearc_Func005A()
    SetUnitAbilityLevelSwapped(FourCC('A0A9'), GetEnumUnit(), ( GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())) + 1 ))
end
function Trig_PodruvResearc_Actions()
    if ( Trig_PodruvResearc_Func001C() ) then
        SetPlayerAbilityAvailableBJ(false, FourCC('A0A9'), GetOwningPlayer(GetTriggerUnit()))
        return
    else
    end
    udg_Boolexpr = Trig_PodruvResearc_Func002002
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PodruvResearc_Func005A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_PodruvResearc()
    gg_trg_PodruvResearc=CreateTrigger()
    DisableTrigger(gg_trg_PodruvResearc)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodruvResearc, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PodruvResearc, Condition(Trig_PodruvResearc_Conditions))
    TriggerAddAction(gg_trg_PodruvResearc, Trig_PodruvResearc_Actions)
end
--===========================================================================
-- Trigger: PodruvTrain
--===========================================================================
function Trig_PodruvTrain_Conditions()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A0A9'), GetTrainedUnit()) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_PodruvTrain_Actions()
    SetUnitAbilityLevelSwapped(FourCC('A0A9'), GetTrainedUnit(), GetPlayerTechCountSimple(FourCC('R04Q'), GetOwningPlayer(GetTriggerUnit())))
end
--===========================================================================
function InitTrig_PodruvTrain()
    gg_trg_PodruvTrain=CreateTrigger()
    DisableTrigger(gg_trg_PodruvTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PodruvTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PodruvTrain, Condition(Trig_PodruvTrain_Conditions))
    TriggerAddAction(gg_trg_PodruvTrain, Trig_PodruvTrain_Actions)
end
--===========================================================================
-- Trigger: Brac
--===========================================================================
function Trig_Brac_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B028')) > 0 and GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A0A6')) > 0
end
function Trig_Brac_Actions()
    local t
    CreateTextTagUnitBJ("TRIGSTR_7336", GetEventDamageSource(), - 20.00, 5.00, 100, 100, 100, 0.00)
    t=GetLastCreatedTextTag()
    SetTextTagPermanentBJ(t, false)
    SetTextTagLifespanBJ(t, 2.00)
    SetTextTagFadepointBJ(t, 2.00)
    SetTextTagVelocityBJ(t, 75.00, 90)
    RemoveTextTagTimed(t , 2.1)
    t=nil
end
--===========================================================================
function InitTrig_Brac()
    gg_trg_Brac=CreateTrigger()
    DisableTrigger(gg_trg_Brac)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Brac, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Brac, Condition(Trig_Brac_Conditions))
    TriggerAddAction(gg_trg_Brac, Trig_Brac_Actions)
end
--===========================================================================
-- Trigger: Samopodruv
--===========================================================================
function Trig_Samopodruv_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0A9')) > 0
end
function Trig_Samopodruv_Actions()
    local t
    if GetRandomInt(1, 100) < 35 + ( - 5 * GetUnitAbilityLevel(GetAttacker(), FourCC('A0A9')) ) then
        SetUnitLifeBJ(GetAttacker(), ( GetUnitStateSwap(UNIT_STATE_LIFE, GetAttacker()) - 15.00 ))
        CreateTextTagUnitBJ("TRIGSTR_433", GetAttacker(), - 20.00, 5.00, 100, 100, 100, 0.00)
        t=GetLastCreatedTextTag()
        SetTextTagPermanentBJ(t, false)
        SetTextTagLifespanBJ(t, 2.00)
        SetTextTagFadepointBJ(t, 2.00)
        SetTextTagVelocityBJ(t, 75.00, 90)
        RemoveTextTagTimed(t , 2.1)
    end
    t=nil
end
--===========================================================================
function InitTrig_Samopodruv()
    gg_trg_Samopodruv=CreateTrigger()
    DisableTrigger(gg_trg_Samopodruv)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Samopodruv, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Samopodruv, Condition(Trig_Samopodruv_Conditions))
    TriggerAddAction(gg_trg_Samopodruv, Trig_Samopodruv_Actions)
end
--===========================================================================
-- Trigger: Samopodjog
--===========================================================================
function Trig_Samopodjog_Conditions()
     return GetUnitAbilityLevel(GetAttacker(), FourCC('A0AR')) > 0
end
function Trig_Samopodjog_Actions()
    local t
    if GetRandomInt(1, 100) < 35 + ( - 5 * GetUnitAbilityLevel(GetAttacker(), FourCC('A0AR')) ) then
        SetUnitLifeBJ(GetAttacker(), ( GetUnitStateSwap(UNIT_STATE_LIFE, GetAttacker()) - 15.00 ))
        CreateTextTagUnitBJ("TRIGSTR_433", GetAttacker(), - 20.00, 5.00, 100, 100, 100, 0.00)
        t=GetLastCreatedTextTag()
        SetTextTagPermanentBJ(t, false)
        SetTextTagLifespanBJ(t, 2.00)
        SetTextTagFadepointBJ(t, 2.00)
        SetTextTagVelocityBJ(t, 75.00, 90)
        RemoveTextTagTimed(t , 2.1)
    end
    t=nil
end
--===========================================================================
function InitTrig_Samopodjog()
    gg_trg_Samopodjog=CreateTrigger()
    DisableTrigger(gg_trg_Samopodjog)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Samopodjog, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Samopodjog, Condition(Trig_Samopodjog_Conditions))
    TriggerAddAction(gg_trg_Samopodjog, Trig_Samopodjog_Actions)
end
--===========================================================================
-- Trigger: Adrenalin
--===========================================================================
function Trig_Adrenalin_Actions()
    SetUnitLifePercentBJ(GetTriggerUnit(), ( GetUnitLifePercent(GetTriggerUnit()) - 15.00 ))
end
--===========================================================================
function InitTrig_Adrenalin()
    gg_trg_Adrenalin=CreateTrigger()
    DisableTrigger(gg_trg_Adrenalin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Adrenalin, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Adrenalin, function()
        if GetSpellAbilityId() ~= FourCC('A0D2') then return end
        Trig_Adrenalin_Actions()
    end)
end
--===========================================================================
-- Trigger: GazloySpellheals
--===========================================================================
function Trig_GazloySpellheals_Conditions()
    
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1KK')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
    
    
    
end
function Trig_GazloySpellheals_Actions()
    local u= GetEventDamageSource()
    local level= GetUnitAbilityLevel(u, FourCC('A1KK'))
    local damage= GetEventDamage()
    local e= AddSpecialEffectTargetUnitBJ("Chest", u, "AbilitiesSpellsItemsVampiricPotionVampPotionCaster.mdl")
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + damage * ( 0.01 * level ))
  
    
    u=nil
    DestroyEffect(e)
    e=nil
end
--===========================================================================
function InitTrig_GazloySpellheals()
    gg_trg_GazloySpellheals=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GazloySpellheals, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_GazloySpellheals, Condition(Trig_GazloySpellheals_Conditions))
    TriggerAddAction(gg_trg_GazloySpellheals, Trig_GazloySpellheals_Actions)
end
--===========================================================================
-- Trigger: FarmBuildG
--===========================================================================
function Gtiers()
    local phash= Gfarm
    local puhash= Gtier
    local count= LoadInteger(Hash, pi, phash)
    local u= LoadUnitHandle(Hash, pi, puhash)
    local id= GetUnitTypeId(u)
   
    if count < 6 then
        KillUnit(u)
    elseif count < 12 then
        KillUnit(u)
        u=CreateUnit(Player(pi), FourCC('h001'), 0, 0, 0.0)
    else
        KillUnit(u)
        u=CreateUnit(Player(pi), FourCC('h0P6'), 0, 0, 0.0)
    end
    SaveUnitHandle(Hash, pi, puhash, u)
    u=nil
end
function Trig_FarmBuildG_Conditions()
    gUnit=GetTriggerUnit()
    gInt=GetUnitTypeId(gUnit)
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return gInt == FourCC('h076') -- Lab
end
function Trig_FarmBuildG_Actions()
    ChangeObjectsCount(gPi , Gfarm , 1)
    Gtiers(gPi)
end
--===========================================================================
function InitTrig_FarmBuildG()
    gg_trg_FarmBuildG=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmBuildG, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FarmBuildG, Condition(Trig_FarmBuildG_Conditions))
    TriggerAddAction(gg_trg_FarmBuildG, Trig_FarmBuildG_Actions)
end
--===========================================================================
-- Trigger: FarmLoseG
--===========================================================================
function Trig_FarmLoseG_Conditions()
    gUnit=GetTriggerUnit()
    gInt=GetUnitTypeId(gUnit)
    gPi=GetPlayerId(GetOwningPlayer(gUnit))
    return gInt == FourCC('h076') -- Lab
end
function Trig_FarmLoseG_Actions()
    ChangeObjectsCount(gPi , Gfarm , - 1)
    Gtiers(gPi)
end
--===========================================================================
function InitTrig_FarmLoseG()
    gg_trg_FarmLoseG=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmLoseG, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_FarmLoseG, Condition(Trig_FarmLoseG_Conditions))
    TriggerAddAction(gg_trg_FarmLoseG, Trig_FarmLoseG_Actions)
end
--===========================================================================
-- Trigger: Pulimetchik
--===========================================================================
function Trig_Pulimetchik_Func002C()
    if ( ( GetResearched() == FourCC('R04E') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Pulimetchik_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Pulimetchik_Conditions()
    if ( not Trig_Pulimetchik_Func002C() ) then
        return false
    end
    if ( not Trig_Pulimetchik_Func003C() ) then
        return false
    end
    return true
end
function Trig_Pulimetchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06L'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Pulimetchik()
    gg_trg_Pulimetchik=CreateTrigger()
    DisableTrigger(gg_trg_Pulimetchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pulimetchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Pulimetchik, Condition(Trig_Pulimetchik_Conditions))
    TriggerAddAction(gg_trg_Pulimetchik, Trig_Pulimetchik_Actions)
end
--===========================================================================
-- Trigger: Ognemetchik
--===========================================================================
function Trig_Ognemetchik_Func002C()
    if ( ( GetResearched() == FourCC('R04G') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Ognemetchik_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Ognemetchik_Conditions()
    if ( not Trig_Ognemetchik_Func002C() ) then
        return false
    end
    if ( not Trig_Ognemetchik_Func003C() ) then
        return false
    end
    return true
end
function Trig_Ognemetchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Ognemetchik()
    gg_trg_Ognemetchik=CreateTrigger()
    DisableTrigger(gg_trg_Ognemetchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ognemetchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Ognemetchik, Condition(Trig_Ognemetchik_Conditions))
    TriggerAddAction(gg_trg_Ognemetchik, Trig_Ognemetchik_Actions)
end
--===========================================================================
-- Trigger: Raketchik
--===========================================================================
function Trig_Raketchik_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Raketchik_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Raketchik_Conditions()
    if ( not Trig_Raketchik_Func002C() ) then
        return false
    end
    if ( not Trig_Raketchik_Func003C() ) then
        return false
    end
    return true
end
function Trig_Raketchik_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06N'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Raketchik()
    gg_trg_Raketchik=CreateTrigger()
    DisableTrigger(gg_trg_Raketchik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Raketchik, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Raketchik, Condition(Trig_Raketchik_Conditions))
    TriggerAddAction(gg_trg_Raketchik, Trig_Raketchik_Actions)
end
--===========================================================================
-- Trigger: Medic
--===========================================================================
function Trig_Medic_Func002C()
    if ( ( GetResearched() == FourCC('R04P') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Medic_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04P'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Medic_Conditions()
    if ( not Trig_Medic_Func002C() ) then
        return false
    end
    if ( not Trig_Medic_Func003C() ) then
        return false
    end
    return true
end
function Trig_Medic_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06O'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Medic()
    gg_trg_Medic=CreateTrigger()
    DisableTrigger(gg_trg_Medic)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Medic, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Medic, Condition(Trig_Medic_Conditions))
    TriggerAddAction(gg_trg_Medic, Trig_Medic_Actions)
end
--===========================================================================
-- Trigger: Sniper
--===========================================================================
function Trig_Sniper_Func002C()
    if ( ( GetResearched() == FourCC('R04M') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04E') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Sniper_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 3 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04M'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Sniper_Conditions()
    if ( not Trig_Sniper_Func002C() ) then
        return false
    end
    if ( not Trig_Sniper_Func003C() ) then
        return false
    end
    return true
end
function Trig_Sniper_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06M'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sniper()
    gg_trg_Sniper=CreateTrigger()
    DisableTrigger(gg_trg_Sniper)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sniper, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Sniper, Condition(Trig_Sniper_Conditions))
    TriggerAddAction(gg_trg_Sniper, Trig_Sniper_Actions)
end
--===========================================================================
-- Trigger: Saper
--===========================================================================
function Trig_Saper_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04K') ) ) then
        return true
    end
    return false
end
function Trig_Saper_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 3 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04K'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Saper_Conditions()
    if ( not Trig_Saper_Func002C() ) then
        return false
    end
    if ( not Trig_Saper_Func003C() ) then
        return false
    end
    return true
end
function Trig_Saper_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h078'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Saper()
    gg_trg_Saper=CreateTrigger()
    DisableTrigger(gg_trg_Saper)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Saper, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Saper, Condition(Trig_Saper_Conditions))
    TriggerAddAction(gg_trg_Saper, Trig_Saper_Actions)
end
--===========================================================================
-- Trigger: Car
--===========================================================================
function Trig_Car_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04I') ) ) then
        return true
    end
    return false
end
function Trig_Car_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Car_Conditions()
    if ( not Trig_Car_Func002C() ) then
        return false
    end
    if ( not Trig_Car_Func003C() ) then
        return false
    end
    return true
end
function Trig_Car_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06R'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car()
    gg_trg_Car=CreateTrigger()
    DisableTrigger(gg_trg_Car)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car, Condition(Trig_Car_Conditions))
    TriggerAddAction(gg_trg_Car, Trig_Car_Actions)
end
--===========================================================================
-- Trigger: Vezdehod
--===========================================================================
function Trig_Vezdehod_Func002C()
    if ( ( GetResearched() == FourCC('R04E') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04I') ) ) then
        return true
    end
    return false
end
function Trig_Vezdehod_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Vezdehod_Conditions()
    if ( not Trig_Vezdehod_Func002C() ) then
        return false
    end
    if ( not Trig_Vezdehod_Func003C() ) then
        return false
    end
    return true
end
function Trig_Vezdehod_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06U'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Vezdehod()
    gg_trg_Vezdehod=CreateTrigger()
    DisableTrigger(gg_trg_Vezdehod)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Vezdehod, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Vezdehod, Condition(Trig_Vezdehod_Conditions))
    TriggerAddAction(gg_trg_Vezdehod, Trig_Vezdehod_Actions)
end
--===========================================================================
-- Trigger: Tank
--===========================================================================
function Trig_Tank_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04I') ) ) then
        return true
    end
    return false
end
function Trig_Tank_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Tank_Conditions()
    if ( not Trig_Tank_Func002C() ) then
        return false
    end
    if ( not Trig_Tank_Func003C() ) then
        return false
    end
    return true
end
function Trig_Tank_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06T'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Tank()
    gg_trg_Tank=CreateTrigger()
    DisableTrigger(gg_trg_Tank)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Tank, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Tank, Condition(Trig_Tank_Conditions))
    TriggerAddAction(gg_trg_Tank, Trig_Tank_Actions)
end
--===========================================================================
-- Trigger: FireTank
--===========================================================================
function Trig_FireTank_Func002C()
    if ( ( GetResearched() == FourCC('R04G') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    return false
end
function Trig_FireTank_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_FireTank_Conditions()
    if ( not Trig_FireTank_Func002C() ) then
        return false
    end
    if ( not Trig_FireTank_Func003C() ) then
        return false
    end
    return true
end
function Trig_FireTank_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06S'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FireTank()
    gg_trg_FireTank=CreateTrigger()
    DisableTrigger(gg_trg_FireTank)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireTank, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FireTank, Condition(Trig_FireTank_Conditions))
    TriggerAddAction(gg_trg_FireTank, Trig_FireTank_Actions)
end
--===========================================================================
-- Trigger: Arta
--===========================================================================
function Trig_Arta_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04M') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    return false
end
function Trig_Arta_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04M'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Arta_Conditions()
    if ( not Trig_Arta_Func002C() ) then
        return false
    end
    if ( not Trig_Arta_Func003C() ) then
        return false
    end
    return true
end
function Trig_Arta_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06Y'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Arta()
    gg_trg_Arta=CreateTrigger()
    DisableTrigger(gg_trg_Arta)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Arta, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Arta, Condition(Trig_Arta_Conditions))
    TriggerAddAction(gg_trg_Arta, Trig_Arta_Actions)
end
--===========================================================================
-- Trigger: Meha
--===========================================================================
function Trig_Meha_Func002C()
    if ( ( GetResearched() == FourCC('R04H') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04J') ) ) then
        return true
    end
    return false
end
function Trig_Meha_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04H'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Meha_Conditions()
    if ( not Trig_Meha_Func002C() ) then
        return false
    end
    if ( not Trig_Meha_Func003C() ) then
        return false
    end
    return true
end
function Trig_Meha_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00W'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Meha()
    gg_trg_Meha=CreateTrigger()
    DisableTrigger(gg_trg_Meha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Meha, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Meha, Condition(Trig_Meha_Conditions))
    TriggerAddAction(gg_trg_Meha, Trig_Meha_Actions)
end
--===========================================================================
-- Trigger: OgneMeha
--===========================================================================
function Trig_OgneMeha_Func002C()
    if ( ( GetResearched() == FourCC('R04G') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04J') ) ) then
        return true
    end
    return false
end
function Trig_OgneMeha_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04G'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_OgneMeha_Conditions()
    if ( not Trig_OgneMeha_Func002C() ) then
        return false
    end
    if ( not Trig_OgneMeha_Func003C() ) then
        return false
    end
    return true
end
function Trig_OgneMeha_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00X'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_OgneMeha()
    gg_trg_OgneMeha=CreateTrigger()
    DisableTrigger(gg_trg_OgneMeha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgneMeha, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_OgneMeha, Condition(Trig_OgneMeha_Conditions))
    TriggerAddAction(gg_trg_OgneMeha, Trig_OgneMeha_Actions)
end
--===========================================================================
-- Trigger: Eczo
--===========================================================================
function Trig_Eczo_Func002C()
    if ( ( GetResearched() == FourCC('R04H') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04J') ) ) then
        return true
    end
    return false
end
function Trig_Eczo_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04H'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Eczo_Conditions()
    if ( not Trig_Eczo_Func002C() ) then
        return false
    end
    if ( not Trig_Eczo_Func003C() ) then
        return false
    end
    return true
end
function Trig_Eczo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o00Y'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Eczo()
    gg_trg_Eczo=CreateTrigger()
    DisableTrigger(gg_trg_Eczo)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Eczo, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Eczo, Condition(Trig_Eczo_Conditions))
    TriggerAddAction(gg_trg_Eczo, Trig_Eczo_Actions)
end
--===========================================================================
-- Trigger: Super
--===========================================================================
function Trig_Super_Func002C()
    if ( ( GetResearched() == FourCC('R04E') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04J') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04P') ) ) then
        return true
    end
    return false
end
function Trig_Super_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04P'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04J'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04E'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Super_Conditions()
    if ( not Trig_Super_Func002C() ) then
        return false
    end
    if ( not Trig_Super_Func003C() ) then
        return false
    end
    return true
end
function Trig_Super_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06P'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Super()
    gg_trg_Super=CreateTrigger()
    DisableTrigger(gg_trg_Super)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Super, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Super, Condition(Trig_Super_Conditions))
    TriggerAddAction(gg_trg_Super, Trig_Super_Actions)
end
--===========================================================================
-- Trigger: Submarina
--===========================================================================
function Trig_Submarina_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04I') ) ) then
        return true
    end
    return false
end
function Trig_Submarina_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 1 ) ) then
        return false
    end
    return true
end
function Trig_Submarina_Conditions()
    if ( not Trig_Submarina_Func002C() ) then
        return false
    end
    if ( not Trig_Submarina_Func003C() ) then
        return false
    end
    return true
end
function Trig_Submarina_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06V'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Submarina()
    gg_trg_Submarina=CreateTrigger()
    DisableTrigger(gg_trg_Submarina)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Submarina, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Submarina, Condition(Trig_Submarina_Conditions))
    TriggerAddAction(gg_trg_Submarina, Trig_Submarina_Actions)
end
--===========================================================================
-- Trigger: Podlodka1
--===========================================================================
function Trig_Podlodka1_Func002C()
    if ( ( GetResearched() == FourCC('R04F') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04L') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R04I') ) ) then
        return true
    end
    return false
end
function Trig_Podlodka1_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R04L'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04I'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R04F'), GetOwningPlayer(GetTriggerUnit())) >= 2 ) ) then
        return false
    end
    return true
end
function Trig_Podlodka1_Conditions()
    if ( not Trig_Podlodka1_Func002C() ) then
        return false
    end
    if ( not Trig_Podlodka1_Func003C() ) then
        return false
    end
    return true
end
function Trig_Podlodka1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h06W'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Podlodka1()
    gg_trg_Podlodka1=CreateTrigger()
    DisableTrigger(gg_trg_Podlodka1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Podlodka1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Podlodka1, Condition(Trig_Podlodka1_Conditions))
    TriggerAddAction(gg_trg_Podlodka1, Trig_Podlodka1_Actions)
end
--===========================================================================
-- Trigger: BloodElvesOn
--===========================================================================
function Trig_BloodElvesOn_Actions()
    EnableTrigger(gg_trg_KaelMassAstral)
    --call EnableTrigger( gg_trg_LortemarAddArmor )
    EnableTrigger(gg_trg_LortemarArmorActive)
    EnableTrigger(gg_trg_Arcana)
    EnableTrigger(gg_trg_ArcanaBegin)
    EnableTrigger(gg_trg_ArcanaCansel)
    EnableTrigger(gg_trg_Fel)
    EnableTrigger(gg_trg_FelBegin)
    EnableTrigger(gg_trg_FelCansel)
    EnableTrigger(gg_trg_Void)
    EnableTrigger(gg_trg_VoidBegin)
    EnableTrigger(gg_trg_VoidCansel)
    EnableTrigger(gg_trg_Light)
    EnableTrigger(gg_trg_LightBegin)
    EnableTrigger(gg_trg_LightCansel)
    EnableTrigger(gg_trg_felspell2)
    EnableTrigger(gg_trg_voidspell111)
    EnableTrigger(gg_trg_lightspel)
    EnableTrigger(gg_trg_ArcanaBuild)
    EnableTrigger(gg_trg_FelBuild)
    EnableTrigger(gg_trg_VoidBuild)
    EnableTrigger(gg_trg_LigthBuild)
    
    
    EnableTrigger(gg_trg_FireShielDamageUniversal)
    
    EnableTrigger(gg_trg_Porcha)
    EnableTrigger(gg_trg_FirePodgogStrela)
    EnableTrigger(gg_trg_Souz)
    
    EnableTrigger(gg_trg_ArcanaIscachenie)
    EnableTrigger(gg_trg_ArcanaStrela)
    
    EnableTrigger(gg_trg_AutoMana)
    EnableTrigger(gg_trg_AutoStrelaFire)
    EnableTrigger(gg_trg_AutoStrelaArcana)
    EnableTrigger(gg_trg_AutoStrelaFel)
    EnableTrigger(gg_trg_AutoSummonGonch)
    
    EnableTrigger(gg_trg_FirePodgog)
    EnableTrigger(gg_trg_FirePodgogStrela2)
    EnableTrigger(gg_trg_VedmakF)
    EnableTrigger(gg_trg_VedmakB)
    EnableTrigger(gg_trg_VedmakC)
    
    EnableTrigger(gg_trg_MagsF)
    EnableTrigger(gg_trg_MagsB)
    EnableTrigger(gg_trg_MagsC)
    
    EnableTrigger(gg_trg_StrannikF)
    EnableTrigger(gg_trg_StrannikB)
    EnableTrigger(gg_trg_StrannikC)
    
    EnableTrigger(gg_trg_PaladinF)
    EnableTrigger(gg_trg_PaladinB)
    EnableTrigger(gg_trg_PaladinC)
    
    EnableTrigger(gg_trg_Manasbor)
    EnableTrigger(gg_trg_SpellMassSunAttack)
    EnableTrigger(gg_trg_LiadrinUlta)
    
end
--===========================================================================
function InitTrig_BloodElvesOn()
    gg_trg_BloodElvesOn=CreateTrigger()
    TriggerAddAction(gg_trg_BloodElvesOn, Trig_BloodElvesOn_Actions)
end
--===========================================================================
-- Trigger: Start Elves O
--===========================================================================
function Trig_Start_Elves_O_Func001A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetEnumPlayer())
    -- -----------------------
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetEnumPlayer())
    -- -----------------------
    SetPlayerTechMaxAllowedSwap(FourCC('H043'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H044'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H05H'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H05I'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H045'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hjnd'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hkal'), 1, GetEnumPlayer())
    --????????? ???????
    SetPlayerTechMaxAllowedSwap(FourCC('h0O6'), 0, GetEnumPlayer())
end
function Trig_Start_Elves_O_Actions()
    ForForce(udg_AllPlayers, Trig_Start_Elves_O_Func001A)
end
--===========================================================================
function InitTrig_Start_Elves_O()
    gg_trg_Start_Elves_O=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Start_Elves_O, 5.00)
    TriggerAddAction(gg_trg_Start_Elves_O, Trig_Start_Elves_O_Actions)
end
--===========================================================================
-- Trigger: KaelMassAstral
--===========================================================================
function Trig_KaelMassAstral_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    RemoveUnitTimed(GetLastCreatedUnit() , 3)
end
function Trig_KaelMassAstral_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 150, nil)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_KaelMassAstral_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KaelMassAstral()
    gg_trg_KaelMassAstral=CreateTrigger()
    DisableTrigger(gg_trg_KaelMassAstral)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KaelMassAstral, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KaelMassAstral, function()
        if GetSpellAbilityId() ~= FourCC('A08R') then return end
        Trig_KaelMassAstral_Actions()
    end)
end
--===========================================================================
-- Trigger: LortemarArmorActive
--===========================================================================
function Trig_LortemarArmorActive_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A0DD'))
    UnitAddAbility(u, FourCC('ACmi'))
    
    RemoveAbilityTimed(u , FourCC('A0DD') , 20)
    RemoveAbilityTimed(u , FourCC('ACmi') , 20)
    u=nil
end
--===========================================================================
function InitTrig_LortemarArmorActive()
    gg_trg_LortemarArmorActive=CreateTrigger()
    DisableTrigger(gg_trg_LortemarArmorActive)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LortemarArmorActive, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LortemarArmorActive, function()
        if GetSpellAbilityId() ~= FourCC('A16M') then return end
        Trig_LortemarArmorActive_Actions()
    end)
end
--===========================================================================
-- Trigger: LiadrinUlta
--===========================================================================
function Trig_LiadrinUlta_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A1KV'))
    RemoveAbilityTimed(u , FourCC('A1KV') , 15)
    u=nil
end
--===========================================================================
function InitTrig_LiadrinUlta()
    gg_trg_LiadrinUlta=CreateTrigger()
    
    TriggerRegisterAnyUnitEventBJ(gg_trg_LiadrinUlta, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LiadrinUlta, function()
        if GetSpellAbilityId() ~= FourCC('A1KU') then return end
        Trig_LiadrinUlta_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellMassSunAttack
--===========================================================================
function Trig_SpellMassSunAttack_Actions()
    local l= GetSpellTargetLoc()
    local caster= GetTriggerUnit()
    local p= GetOwningPlayer(caster)
    --local boolexpr bex
    local dammyAbility= FourCC('A1KY')
    local level= GetUnitAbilityLevel(caster, GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    --set bex = Condition(function EnemEl) 
    GroupEnumUnitsInRangeOfLoc(g, l, 150, nil)
    
    if FirstOfGroup(g) == nil then
        --???? ??????
        BlzStartUnitAbilityCooldown(caster, dammyAbility, 15)
        SetUnitState(caster, UNIT_STATE_MANA, GetUnitState(caster, UNIT_STATE_MANA) + 100 + 35 * level)
        
    
    else
        RemoveLocation(l)
        l=GetUnitLoc(caster)
        while true do
            u=FirstOfGroup(g)
            if u == nil then break end
            
            u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
            
            if IsPlayerEnemy(GetOwningPlayer(u), p) then
                dammyAbility=FourCC('A1KZ')
            else
                dammyAbility=FourCC('A1KY')
            end
            
            UnitAddAbility(u2, dammyAbility)
            SetUnitAbilityLevel(u2, dammyAbility, level)
            
            if IsPlayerEnemy(GetOwningPlayer(u), p) then
                IssueTargetOrder(u2, "firebolt", u)
            else
                IssueTargetOrder(u2, "holybolt", u)
            end
            RemoveUnitTimed(u2 , 2)
            i=i + 1
            GroupRemoveUnit(g, u)
            u=nil
        end
    end
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    --call
    u2=nil
    --set bex = null
end
--===========================================================================
function InitTrig_SpellMassSunAttack()
    gg_trg_SpellMassSunAttack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellMassSunAttack, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellMassSunAttack, function()
        if GetSpellAbilityId() ~= FourCC('A1KX') then return end
        Trig_SpellMassSunAttack_Actions()
    end)
end
--===========================================================================
-- Trigger: Manasbor
--===========================================================================
function Trig_Manasbor_Conditions()
    gCaster=GetEventDamageSource()
    gTarget=GetEventTargetUnit()
    return GetUnitAbilityLevel(gCaster, FourCC('A1GR')) > 0
end
function Trig_Manasbor_Actions()
    local enemyMana= GetUnitState(GetTriggerUnit(), UNIT_STATE_MANA)
    local k= 0
    if IsUnitType(gTarget, UNIT_TYPE_HERO) then
        if enemyMana > 1 then
            k=1
        else
            return
        end
    else
        if enemyMana > 5 then
            k=5
        else
            return
        end
    end
    if gCaster ~= nil and UnitAlive(gCaster) then
        SetUnitState(gCaster, UNIT_STATE_MANA, RMaxBJ(0, GetUnitState(gCaster, UNIT_STATE_MANA) + k))
    end
end
--===========================================================================
function InitTrig_Manasbor()
    gg_trg_Manasbor=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Manasbor, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_Manasbor, Condition(Trig_Manasbor_Conditions))
    TriggerAddAction(gg_trg_Manasbor, Trig_Manasbor_Actions)
end
--===========================================================================
-- Trigger: ManaAura
--===========================================================================
function Trig_ManaAura_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F')
end
function Trig_ManaAura_Actions()
    UnitAddAbility(GetConstructedStructure(), FourCC('A1GT'))
end
--===========================================================================
function InitTrig_ManaAura()
    gg_trg_ManaAura=CreateTrigger()
    DisableTrigger(gg_trg_ManaAura)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ManaAura, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_ManaAura, Condition(Trig_ManaAura_Conditions))
    TriggerAddAction(gg_trg_ManaAura, Trig_ManaAura_Actions)
end
--===========================================================================
-- Trigger: Arcana
--===========================================================================
function Trig_Arcana_Func009C()
    if ( not ( GetResearched() == FourCC('R01D') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_Arcana_Conditions()
    if ( not Trig_Arcana_Func009C() ) then
        return false
    end
    return true
end
function Trig_Arcana_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cff8080ffr")
end
function Trig_Arcana_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Arcana_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechResearchedSwap(FourCC('R01E'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R01F'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Arcana()
    gg_trg_Arcana=CreateTrigger()
    DisableTrigger(gg_trg_Arcana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Arcana, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Arcana, Condition(Trig_Arcana_Conditions))
    TriggerAddAction(gg_trg_Arcana, Trig_Arcana_Actions)
end
--===========================================================================
-- Trigger: ArcanaBegin
--===========================================================================
function Trig_ArcanaBegin_Func004C()
    if ( not ( GetResearched() == FourCC('R01D') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_ArcanaBegin_Conditions()
    if ( not Trig_ArcanaBegin_Func004C() ) then
        return false
    end
    return true
end
function Trig_ArcanaBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ArcanaBegin()
    gg_trg_ArcanaBegin=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_ArcanaBegin, Condition(Trig_ArcanaBegin_Conditions))
    TriggerAddAction(gg_trg_ArcanaBegin, Trig_ArcanaBegin_Actions)
end
--===========================================================================
-- Trigger: ArcanaCansel
--===========================================================================
function Trig_ArcanaCansel_Func004C()
    if ( not ( GetResearched() == FourCC('R01D') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_ArcanaCansel_Conditions()
    if ( not Trig_ArcanaCansel_Func004C() ) then
        return false
    end
    return true
end
function Trig_ArcanaCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ArcanaCansel()
    gg_trg_ArcanaCansel=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_ArcanaCansel, Condition(Trig_ArcanaCansel_Conditions))
    TriggerAddAction(gg_trg_ArcanaCansel, Trig_ArcanaCansel_Actions)
end
--===========================================================================
-- Trigger: Fel
--===========================================================================
function Trig_Fel_Func007C()
    if ( not ( GetResearched() == FourCC('R01G') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_Fel_Conditions()
    if ( not Trig_Fel_Func007C() ) then
        return false
    end
    return true
end
function Trig_Fel_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cff80ff80r")
end
function Trig_Fel_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Fel_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0O6'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h03Z'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Fel()
    gg_trg_Fel=CreateTrigger()
    DisableTrigger(gg_trg_Fel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fel, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Fel, Condition(Trig_Fel_Conditions))
    TriggerAddAction(gg_trg_Fel, Trig_Fel_Actions)
end
--===========================================================================
-- Trigger: FelBegin
--===========================================================================
function Trig_FelBegin_Func004C()
    if ( not ( GetResearched() == FourCC('R01G') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_FelBegin_Conditions()
    if ( not Trig_FelBegin_Func004C() ) then
        return false
    end
    return true
end
function Trig_FelBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FelBegin()
    gg_trg_FelBegin=CreateTrigger()
    DisableTrigger(gg_trg_FelBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_FelBegin, Condition(Trig_FelBegin_Conditions))
    TriggerAddAction(gg_trg_FelBegin, Trig_FelBegin_Actions)
end
--===========================================================================
-- Trigger: FelCansel
--===========================================================================
function Trig_FelCansel_Func004C()
    if ( not ( GetResearched() == FourCC('R01G') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_FelCansel_Conditions()
    if ( not Trig_FelCansel_Func004C() ) then
        return false
    end
    return true
end
function Trig_FelCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FelCansel()
    gg_trg_FelCansel=CreateTrigger()
    DisableTrigger(gg_trg_FelCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_FelCansel, Condition(Trig_FelCansel_Conditions))
    TriggerAddAction(gg_trg_FelCansel, Trig_FelCansel_Actions)
end
--===========================================================================
-- Trigger: FelGolemStrike
--===========================================================================
function Trig_FelGolemStrike_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A1LW')) == 1 and Random(1 , 20)
end
function Trig_FelGolemStrike_Actions()
    IssueTargetOrder(GetAttacker(), "forkedlightning", GetTriggerUnit())
end
--===========================================================================
function InitTrig_FelGolemStrike()
    gg_trg_FelGolemStrike=CreateTrigger()
    --call DisableTrigger( gg_trg_FelGolemStrike )
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelGolemStrike, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_FelGolemStrike, Condition(Trig_FelGolemStrike_Conditions))
    TriggerAddAction(gg_trg_FelGolemStrike, Trig_FelGolemStrike_Actions)
end
--===========================================================================
-- Trigger: Void
--===========================================================================
function Trig_Void_Func008C()
    if ( not ( GetResearched() == FourCC('R01H') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_Void_Conditions()
    if ( not Trig_Void_Func008C() ) then
        return false
    end
    return true
end
function Trig_Void_Func002A()
    BlzSetUnitName(GetEnumUnit(), "cffff00ffr")
end
function Trig_Void_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Void_Func002A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R020'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Void()
    gg_trg_Void=CreateTrigger()
    DisableTrigger(gg_trg_Void)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Void, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Void, Condition(Trig_Void_Conditions))
    TriggerAddAction(gg_trg_Void, Trig_Void_Actions)
end
--===========================================================================
-- Trigger: VoidBegin
--===========================================================================
function Trig_VoidBegin_Func004C()
    if ( not ( GetResearched() == FourCC('R01H') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_VoidBegin_Conditions()
    if ( not Trig_VoidBegin_Func004C() ) then
        return false
    end
    return true
end
function Trig_VoidBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VoidBegin()
    gg_trg_VoidBegin=CreateTrigger()
    DisableTrigger(gg_trg_VoidBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_VoidBegin, Condition(Trig_VoidBegin_Conditions))
    TriggerAddAction(gg_trg_VoidBegin, Trig_VoidBegin_Actions)
end
--===========================================================================
-- Trigger: VoidCansel
--===========================================================================
function Trig_VoidCansel_Func004C()
    if ( not ( GetResearched() == FourCC('R01H') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_VoidCansel_Conditions()
    if ( not Trig_VoidCansel_Func004C() ) then
        return false
    end
    return true
end
function Trig_VoidCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01I'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VoidCansel()
    gg_trg_VoidCansel=CreateTrigger()
    DisableTrigger(gg_trg_VoidCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_VoidCansel, Condition(Trig_VoidCansel_Conditions))
    TriggerAddAction(gg_trg_VoidCansel, Trig_VoidCansel_Actions)
end
--===========================================================================
-- Trigger: LightBegin
--===========================================================================
function Trig_LightBegin_Func004C()
    if ( not ( GetResearched() == FourCC('R01I') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_LightBegin_Conditions()
    if ( not Trig_LightBegin_Func004C() ) then
        return false
    end
    return true
end
function Trig_LightBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_LightBegin()
    gg_trg_LightBegin=CreateTrigger()
    DisableTrigger(gg_trg_LightBegin)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LightBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_LightBegin, Condition(Trig_LightBegin_Conditions))
    TriggerAddAction(gg_trg_LightBegin, Trig_LightBegin_Actions)
end
--===========================================================================
-- Trigger: LightCansel
--===========================================================================
function Trig_LightCansel_Func004C()
    if ( not ( GetResearched() == FourCC('R01I') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_LightCansel_Conditions()
    if ( not Trig_LightCansel_Func004C() ) then
        return false
    end
    return true
end
function Trig_LightCansel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 3, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 3, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_LightCansel()
    gg_trg_LightCansel=CreateTrigger()
    DisableTrigger(gg_trg_LightCansel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LightCansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_LightCansel, Condition(Trig_LightCansel_Conditions))
    TriggerAddAction(gg_trg_LightCansel, Trig_LightCansel_Actions)
end
--===========================================================================
-- Trigger: Light
--===========================================================================
function Trig_Light_Func008C()
    if ( not ( GetResearched() == FourCC('R01I') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_Light_Conditions()
    if ( not Trig_Light_Func008C() ) then
        return false
    end
    return true
end
function Trig_Light_Func003A()
    BlzSetUnitName(GetEnumUnit(), "cffffff00r")
end
function Trig_Light_Actions()
    udg_LocalOtrad=GetUnitsOfPlayerAndTypeId(GetOwningPlayer(GetTriggerUnit()), FourCC('h04F'))
    ForGroupBJ(udg_LocalOtrad, Trig_Light_Func003A)
    DestroyGroup(udg_LocalOtrad)
    SetPlayerTechMaxAllowedSwap(FourCC('R01D'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01G'), 2, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R01H'), 2, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Light()
    gg_trg_Light=CreateTrigger()
    DisableTrigger(gg_trg_Light)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Light, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Light, Condition(Trig_Light_Conditions))
    TriggerAddAction(gg_trg_Light, Trig_Light_Actions)
end
--===========================================================================
-- Trigger: ArcanaBuild
--===========================================================================
function Trig_ArcanaBuild_Func001C()
    if ( not ( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01D'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_ArcanaBuild_Conditions()
    if ( not Trig_ArcanaBuild_Func001C() ) then
        return false
    end
    return true
end
function Trig_ArcanaBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cff8080ffr")
end
--===========================================================================
function InitTrig_ArcanaBuild()
    gg_trg_ArcanaBuild=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_ArcanaBuild, Condition(Trig_ArcanaBuild_Conditions))
    TriggerAddAction(gg_trg_ArcanaBuild, Trig_ArcanaBuild_Actions)
end
--===========================================================================
-- Trigger: FelBuild
--===========================================================================
function Trig_FelBuild_Func001C()
    if ( not ( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01G'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_FelBuild_Conditions()
    if ( not Trig_FelBuild_Func001C() ) then
        return false
    end
    return true
end
function Trig_FelBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cff80ff80r")
end
--===========================================================================
function InitTrig_FelBuild()
    gg_trg_FelBuild=CreateTrigger()
    DisableTrigger(gg_trg_FelBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FelBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FelBuild, Condition(Trig_FelBuild_Conditions))
    TriggerAddAction(gg_trg_FelBuild, Trig_FelBuild_Actions)
end
--===========================================================================
-- Trigger: VoidBuild
--===========================================================================
function Trig_VoidBuild_Func001C()
    if ( not ( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01H'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_VoidBuild_Conditions()
    if ( not Trig_VoidBuild_Func001C() ) then
        return false
    end
    return true
end
function Trig_VoidBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cffff00ffrr")
end
--===========================================================================
function InitTrig_VoidBuild()
    gg_trg_VoidBuild=CreateTrigger()
    DisableTrigger(gg_trg_VoidBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_VoidBuild, Condition(Trig_VoidBuild_Conditions))
    TriggerAddAction(gg_trg_VoidBuild, Trig_VoidBuild_Actions)
end
--===========================================================================
-- Trigger: LigthBuild
--===========================================================================
function Trig_LigthBuild_Func001C()
    if ( not ( GetUnitTypeId(GetConstructedStructure()) == FourCC('h04F') ) ) then
        return false
    end
    if ( not ( GetPlayerTechCountSimple(FourCC('R01I'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_LigthBuild_Conditions()
    if ( not Trig_LigthBuild_Func001C() ) then
        return false
    end
    return true
end
function Trig_LigthBuild_Actions()
    BlzSetUnitName(GetTriggerUnit(), "cffffff00r")
end
--===========================================================================
function InitTrig_LigthBuild()
    gg_trg_LigthBuild=CreateTrigger()
    DisableTrigger(gg_trg_LigthBuild)
    TriggerRegisterAnyUnitEventBJ(gg_trg_LigthBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_LigthBuild, Condition(Trig_LigthBuild_Conditions))
    TriggerAddAction(gg_trg_LigthBuild, Trig_LigthBuild_Actions)
end
--===========================================================================
-- Trigger: felspell
--===========================================================================
function Trig_felspell_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1QZ'))
    end
end
--===========================================================================
function InitTrig_felspell()
    gg_trg_felspell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_felspell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_felspell, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01G'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1QZ')) < 1) then return end
        Trig_felspell_Actions()
    end)
end
--===========================================================================
-- Trigger: voidspell
--===========================================================================
function Trig_voidspell_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1R0'))
    end
end
--===========================================================================
function InitTrig_voidspell()
    gg_trg_voidspell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_voidspell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_voidspell, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01H'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1R0')) < 1) then return end
        Trig_voidspell_Actions()
    end)
end
--===========================================================================
-- Trigger: lightspel
--===========================================================================
function Trig_lightspel_Actions()
    if UnitAlive(GetSpellTargetUnit()) then
        UnitAddAbility(GetSpellTargetUnit(), FourCC('A1R1'))
    end
end
--===========================================================================
function InitTrig_lightspel()
    gg_trg_lightspel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_lightspel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_lightspel, function()
        if GetSpellAbilityId() ~= FourCC('A02D') then return end
        if not (GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R01I'), true) == 3 and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1R1')) < 1) then return end
        Trig_lightspel_Actions()
    end)
end
--===========================================================================
-- Trigger: Porcha
--===========================================================================
function Trig_Porcha_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02X')) > 0
end
function Trig_Porcha_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetAttacker(), FourCC('A08I'))
        RemoveAbilityTimed(GetAttacker() , FourCC('A08I') , 9)
    end
end
--===========================================================================
function InitTrig_Porcha()
    gg_trg_Porcha=CreateTrigger()
    DisableTrigger(gg_trg_Porcha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Porcha, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Porcha, Condition(Trig_Porcha_Conditions))
    TriggerAddAction(gg_trg_Porcha, Trig_Porcha_Actions)
end
--===========================================================================
-- Trigger: FirePodgogStrela
--===========================================================================
function Trig_FirePodgogStrela_Conditions()
end
function Trig_FirePodgogStrela_Actions()
   
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A08I'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A08I') , 9)
end
--===========================================================================
function InitTrig_FirePodgogStrela()
    gg_trg_FirePodgogStrela=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgogStrela)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgogStrela, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FirePodgogStrela, function()
        if GetSpellAbilityId() ~= FourCC('A030') then return end
        if not Trig_FirePodgogStrela_Conditions() then return end
        Trig_FirePodgogStrela_Actions()
    end)
end
--===========================================================================
-- Trigger: Souz
--===========================================================================
function Trig_Souz_Actions()
    local u= GetSpellTargetUnit()
    UnitAddAbility(u, FourCC('A16H'))
    RemoveAbilityTimed(u , FourCC('A16H') , 60)
    u=nil
end
--===========================================================================
function InitTrig_Souz()
    gg_trg_Souz=CreateTrigger()
    DisableTrigger(gg_trg_Souz)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Souz, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Souz, function()
        if GetSpellAbilityId() ~= FourCC('A02Y') then return end
        if not (GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A16H')) ~= 1) then return end
        Trig_Souz_Actions()
    end)
end
--===========================================================================
-- Trigger: ArcanaIscachenie
--===========================================================================
function Trig_ArcanaIscachenie_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02S')) > 0
end
function Trig_ArcanaIscachenie_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetTriggerUnit(), FourCC('A02T'))
        RemoveAbilityTimed(GetTriggerUnit() , FourCC('A02T') , 9)
    end
    
end
--===========================================================================
function InitTrig_ArcanaIscachenie()
    gg_trg_ArcanaIscachenie=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaIscachenie)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaIscachenie, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_ArcanaIscachenie, Condition(Trig_ArcanaIscachenie_Conditions))
    TriggerAddAction(gg_trg_ArcanaIscachenie, Trig_ArcanaIscachenie_Actions)
end
--===========================================================================
-- Trigger: ArcanaStrela
--===========================================================================
function Trig_ArcanaStrela_Actions()
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02T'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02T') , 9)
end
--===========================================================================
function InitTrig_ArcanaStrela()
    gg_trg_ArcanaStrela=CreateTrigger()
    DisableTrigger(gg_trg_ArcanaStrela)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ArcanaStrela, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ArcanaStrela, function()
        if GetSpellAbilityId() ~= FourCC('A02R') then return end
        if not (GetSpellAbilityId() == FourCC('A02G')) then return end
        Trig_ArcanaStrela_Actions()
    end)
end
--===========================================================================
-- Trigger: FirePodgog
--===========================================================================
function Trig_FirePodgog_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A02N')) > 1
end
function Trig_FirePodgog_Actions()
    if Random(1 , 10) then
        UnitAddAbility(GetTriggerUnit(), FourCC('A02O'))
        RemoveAbilityTimed(GetTriggerUnit() , FourCC('A02O') , 10)
        UnitAddAbility(GetAttacker(), FourCC('A02Q'))
        RemoveAbilityTimed(GetAttacker() , FourCC('A02Q') , 10)
    end
end
--===========================================================================
function InitTrig_FirePodgog()
    gg_trg_FirePodgog=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgog)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgog, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_FirePodgog, Condition(Trig_FirePodgog_Conditions))
    TriggerAddAction(gg_trg_FirePodgog, Trig_FirePodgog_Actions)
end
--===========================================================================
-- Trigger: FirePodgogStrela2
--===========================================================================
function Trig_FirePodgogStrela2_Conditions()
end
function Trig_FirePodgogStrela2_Actions()
    local u= GetSpellTargetUnit()
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02O'))
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A02Q'))
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02O') , 2)
    RemoveAbilityTimed(GetSpellTargetUnit() , FourCC('A02Q') , 2)
    u=nil
end
--===========================================================================
function InitTrig_FirePodgogStrela2()
    gg_trg_FirePodgogStrela2=CreateTrigger()
    DisableTrigger(gg_trg_FirePodgogStrela2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_FirePodgogStrela2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FirePodgogStrela2, function()
        if GetSpellAbilityId() ~= FourCC('A07P') then return end
        if not Trig_FirePodgogStrela2_Conditions() then return end
        Trig_FirePodgogStrela2_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoMana
--===========================================================================
function Trig_AutoMana_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "drain", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoMana()
    gg_trg_AutoMana=CreateTrigger()
    DisableTrigger(gg_trg_AutoMana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoMana, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoMana, function()
        if GetSpellAbilityId() ~= FourCC('A02E') then return end
        Trig_AutoMana_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStrelaFire
--===========================================================================
function Trig_AutoStrelaFire_Func001C()
    if ( ( GetSpellAbilityId() == FourCC('A00W') ) ) then
        return true
    end
    if ( ( GetSpellAbilityId() == FourCC('A07Q') ) ) then
        return true
    end
    return false
end
function Trig_AutoStrelaFire_Conditions()
    if ( not Trig_AutoStrelaFire_Func001C() ) then
        return false
    end
    return true
end
function Trig_AutoStrelaFire_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFire()
    gg_trg_AutoStrelaFire=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaFire)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFire, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaFire, Condition(Trig_AutoStrelaFire_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaFire, Trig_AutoStrelaFire_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaArcana
--===========================================================================
function Trig_AutoStrelaArcana_Func001C()
    if ( ( GetSpellAbilityId() == FourCC('A07D') ) ) then
        return true
    end
    if ( ( GetSpellAbilityId() == FourCC('A02U') ) ) then
        return true
    end
    return false
end
function Trig_AutoStrelaArcana_Conditions()
    if ( not Trig_AutoStrelaArcana_Func001C() ) then
        return false
    end
    return true
end
function Trig_AutoStrelaArcana_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaArcana()
    gg_trg_AutoStrelaArcana=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaArcana)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaArcana, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaArcana, Condition(Trig_AutoStrelaArcana_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaArcana, Trig_AutoStrelaArcana_Actions)
end
--===========================================================================
-- Trigger: AutoStrelaFel
--===========================================================================
function Trig_AutoStrelaFel_Func001C()
    if ( ( GetSpellAbilityId() == FourCC('A02Z') ) ) then
        return true
    end
    if ( ( GetSpellAbilityId() == FourCC('A07O') ) ) then
        return true
    end
    return false
end
function Trig_AutoStrelaFel_Conditions()
    if ( not Trig_AutoStrelaFel_Func001C() ) then
        return false
    end
    return true
end
function Trig_AutoStrelaFel_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoStrelaFel()
    gg_trg_AutoStrelaFel=CreateTrigger()
    DisableTrigger(gg_trg_AutoStrelaFel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStrelaFel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_AutoStrelaFel, Condition(Trig_AutoStrelaFel_Conditions))
    TriggerAddAction(gg_trg_AutoStrelaFel, Trig_AutoStrelaFel_Actions)
end
--===========================================================================
-- Trigger: AutoSummonGonch
--===========================================================================
function Trig_AutoSummonGonch_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "waterelemental")
end
--===========================================================================
function InitTrig_AutoSummonGonch()
    gg_trg_AutoSummonGonch=CreateTrigger()
    DisableTrigger(gg_trg_AutoSummonGonch)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSummonGonch, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSummonGonch, function()
        if GetSpellAbilityId() ~= FourCC('A032') then return end
        Trig_AutoSummonGonch_Actions()
    end)
end
--===========================================================================
-- Trigger: VedmakF
--===========================================================================
function Trig_VedmakF_Conditions()
    if ( not ( GetResearched() == FourCC('R025') ) ) then
        return false
    end
    return true
end
function Trig_VedmakF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakF()
    gg_trg_VedmakF=CreateTrigger()
    DisableTrigger(gg_trg_VedmakF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_VedmakF, Condition(Trig_VedmakF_Conditions))
    TriggerAddAction(gg_trg_VedmakF, Trig_VedmakF_Actions)
end
--===========================================================================
-- Trigger: VedmakB
--===========================================================================
function Trig_VedmakB_Conditions()
    if ( not ( GetResearched() == FourCC('R025') ) ) then
        return false
    end
    return true
end
function Trig_VedmakB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakB()
    gg_trg_VedmakB=CreateTrigger()
    DisableTrigger(gg_trg_VedmakB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_VedmakB, Condition(Trig_VedmakB_Conditions))
    TriggerAddAction(gg_trg_VedmakB, Trig_VedmakB_Actions)
end
--===========================================================================
-- Trigger: VedmakC
--===========================================================================
function Trig_VedmakC_Conditions()
    if ( not ( GetResearched() == FourCC('R025') ) ) then
        return false
    end
    return true
end
function Trig_VedmakC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_VedmakC()
    gg_trg_VedmakC=CreateTrigger()
    DisableTrigger(gg_trg_VedmakC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VedmakC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_VedmakC, Condition(Trig_VedmakC_Conditions))
    TriggerAddAction(gg_trg_VedmakC, Trig_VedmakC_Actions)
end
--===========================================================================
-- Trigger: MagsF
--===========================================================================
function Trig_MagsF_Conditions()
    if ( not ( GetResearched() == FourCC('R03D') ) ) then
        return false
    end
    return true
end
function Trig_MagsF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02U'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsF()
    gg_trg_MagsF=CreateTrigger()
    DisableTrigger(gg_trg_MagsF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MagsF, Condition(Trig_MagsF_Conditions))
    TriggerAddAction(gg_trg_MagsF, Trig_MagsF_Actions)
end
--===========================================================================
-- Trigger: MagsB
--===========================================================================
function Trig_MagsB_Conditions()
    if ( not ( GetResearched() == FourCC('R03D') ) ) then
        return false
    end
    return true
end
function Trig_MagsB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsB()
    gg_trg_MagsB=CreateTrigger()
    DisableTrigger(gg_trg_MagsB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MagsB, Condition(Trig_MagsB_Conditions))
    TriggerAddAction(gg_trg_MagsB, Trig_MagsB_Actions)
end
--===========================================================================
-- Trigger: MagsC
--===========================================================================
function Trig_MagsC_Conditions()
    if ( not ( GetResearched() == FourCC('R03D') ) ) then
        return false
    end
    return true
end
function Trig_MagsC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MagsC()
    gg_trg_MagsC=CreateTrigger()
    DisableTrigger(gg_trg_MagsC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagsC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MagsC, Condition(Trig_MagsC_Conditions))
    TriggerAddAction(gg_trg_MagsC, Trig_MagsC_Actions)
end
--===========================================================================
-- Trigger: StrannikF
--===========================================================================
function Trig_StrannikF_Conditions()
    if ( not ( GetResearched() == FourCC('R03C') ) ) then
        return false
    end
    return true
end
function Trig_StrannikF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02U'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikF()
    gg_trg_StrannikF=CreateTrigger()
    DisableTrigger(gg_trg_StrannikF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StrannikF, Condition(Trig_StrannikF_Conditions))
    TriggerAddAction(gg_trg_StrannikF, Trig_StrannikF_Actions)
end
--===========================================================================
-- Trigger: StrannikB
--===========================================================================
function Trig_StrannikB_Conditions()
    if ( not ( GetResearched() == FourCC('R03C') ) ) then
        return false
    end
    return true
end
function Trig_StrannikB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikB()
    gg_trg_StrannikB=CreateTrigger()
    DisableTrigger(gg_trg_StrannikB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_StrannikB, Condition(Trig_StrannikB_Conditions))
    TriggerAddAction(gg_trg_StrannikB, Trig_StrannikB_Actions)
end
--===========================================================================
-- Trigger: StrannikC
--===========================================================================
function Trig_StrannikC_Conditions()
    if ( not ( GetResearched() == FourCC('R03C') ) ) then
        return false
    end
    return true
end
function Trig_StrannikC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R026'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StrannikC()
    gg_trg_StrannikC=CreateTrigger()
    DisableTrigger(gg_trg_StrannikC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_StrannikC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_StrannikC, Condition(Trig_StrannikC_Conditions))
    TriggerAddAction(gg_trg_StrannikC, Trig_StrannikC_Actions)
end
--===========================================================================
-- Trigger: PaladinF
--===========================================================================
function Trig_PaladinF_Conditions()
    if ( not ( GetResearched() == FourCC('R026') ) ) then
        return false
    end
    return true
end
function Trig_PaladinF_Actions()
    SetPlayerTechResearchedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A05J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A05K'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A049'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('Asps'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A07L'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A037'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07K'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07P'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07Q'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07N'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07O'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07D'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(false, FourCC('A07M'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07S'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A07R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A07T'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerAbilityAvailableBJ(true, FourCC('A02J'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A00W'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A030'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02Z'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02R'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A02G'), GetOwningPlayer(GetTriggerUnit()))
    --                           
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinF()
    gg_trg_PaladinF=CreateTrigger()
    DisableTrigger(gg_trg_PaladinF)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinF, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_PaladinF, Condition(Trig_PaladinF_Conditions))
    TriggerAddAction(gg_trg_PaladinF, Trig_PaladinF_Actions)
end
--===========================================================================
-- Trigger: PaladinB
--===========================================================================
function Trig_PaladinB_Conditions()
    if ( not ( GetResearched() == FourCC('R026') ) ) then
        return false
    end
    return true
end
function Trig_PaladinB_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinB()
    gg_trg_PaladinB=CreateTrigger()
    DisableTrigger(gg_trg_PaladinB)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinB, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_PaladinB, Condition(Trig_PaladinB_Conditions))
    TriggerAddAction(gg_trg_PaladinB, Trig_PaladinB_Actions)
end
--===========================================================================
-- Trigger: PaladinC
--===========================================================================
function Trig_PaladinC_Conditions()
    if ( not ( GetResearched() == FourCC('R026') ) ) then
        return false
    end
    return true
end
function Trig_PaladinC_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R03D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R03C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R025'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_PaladinC()
    gg_trg_PaladinC=CreateTrigger()
    DisableTrigger(gg_trg_PaladinC)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinC, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_PaladinC, Condition(Trig_PaladinC_Conditions))
    TriggerAddAction(gg_trg_PaladinC, Trig_PaladinC_Actions)
end
--===========================================================================
-- Trigger: FireShielDamageUniversal
--===========================================================================
function Trig_FireShielDamageUniversal_Conditions()
    local dx
    local dy
    gCaster=GetEventDamageSource() --?? ??? ???
    gTarget=BlzGetEventDamageTarget()
    dx=GetUnitX(gCaster) - GetUnitX(gTarget)
    dy=GetUnitY(gCaster) - GetUnitY(gTarget)
    return GetUnitAbilityLevel(gCaster, FourCC('B00F')) > 0 and SquareRoot(dx * dx + dy * dy) < 200 and gCaster ~= nil and UnitAlive(gCaster) and gTarget ~= nil and UnitAlive(gTarget)
end
function Trig_FireShielDamageUniversal_Actions()
    UnitDamageTargetBJ(GetTriggerUnit(), gCaster, 45, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_FIRE)
end
--===========================================================================
function InitTrig_FireShielDamageUniversal()
    gg_trg_FireShielDamageUniversal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FireShielDamageUniversal, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_FireShielDamageUniversal, Condition(Trig_FireShielDamageUniversal_Conditions))
    TriggerAddAction(gg_trg_FireShielDamageUniversal, Trig_FireShielDamageUniversal_Actions)
end
--===========================================================================
-- Trigger: BanditsOn
--===========================================================================
function Trig_BanditsOn_Actions()
    --call EnableTrigger( gg_trg_VoevodaSpell )
    EnableTrigger(gg_trg_BlinkToUnit_attack)
    EnableTrigger(gg_trg_DelAttackSpel)
    EnableTrigger(gg_trg_BlinkToUnit_Spell)
    EnableTrigger(gg_trg_Edvin_Ult)
    EnableTrigger(gg_trg_AutoChance)
    EnableTrigger(gg_trg_AutoChance_2)
    EnableTrigger(gg_trg_AutoChance_3)
    EnableTrigger(gg_trg_Dovorougenie_Code_O)
    EnableTrigger(gg_trg_Dovorougenie_2t_Code_O)
    EnableTrigger(gg_trg_Dovorougenie_3t_O)
    
    
    EnableTrigger(gg_trg_Voron)
    EnableTrigger(gg_trg_Sindicat)
    EnableTrigger(gg_trg_Bratstwo)
    EnableTrigger(gg_trg_Pirats)
    EnableTrigger(gg_trg_Shesterenka)
    EnableTrigger(gg_trg_Trumnue_vodu)
    
    
    EnableTrigger(gg_trg_AutoSetka)
    EnableTrigger(gg_trg_AutoSetkaHero)
    EnableTrigger(gg_trg_AutoSvita)
    EnableTrigger(gg_trg_AutoStaya)
    EnableTrigger(gg_trg_AutoManaSteal)
    EnableTrigger(gg_trg_AutoShield)
    EnableTrigger(gg_trg_ResearhRobbery)
    EnableTrigger(gg_trg_RobberyTrain)
    
    EnableTrigger(gg_trg_Edvin_Ult)
    EnableTrigger(gg_trg_BlinkToUnit_Spell)
    EnableTrigger(gg_trg_BlinkToUnit_attack)
    
    
    
    
end
--===========================================================================
function InitTrig_BanditsOn()
    gg_trg_BanditsOn=CreateTrigger()
    TriggerAddAction(gg_trg_BanditsOn, Trig_BanditsOn_Actions)
end
--===========================================================================
-- Trigger: StartBandits
--===========================================================================
function Trig_StartBandits_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('h03L'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h03K'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02Q'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H048'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H03S'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H047'), 1, GetEnumPlayer())
    SetPlayerTechResearchedSwap(FourCC('R00H'), 1, GetEnumPlayer())
end
function Trig_StartBandits_Actions()
    ForForce(udg_AllPlayers, Trig_StartBandits_Func001A)
end
--===========================================================================
function InitTrig_StartBandits()
    gg_trg_StartBandits=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartBandits, 0.01)
    TriggerAddAction(gg_trg_StartBandits, Trig_StartBandits_Actions)
end
--===========================================================================
-- Trigger: BlinkToUnit attack
--===========================================================================
function Trig_BlinkToUnit_attack_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0MZ')) >= 1 and BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('A0MZ')) == 0
end
function MoveTimedEnd()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    SetUnitPositionLoc(LoadUnitHandle(Hash, id, 1), LoadLocationHandle(Hash, id, 2))
       
    RemoveLocation(LoadLocationHandle(Hash, id, 2))
    DestroyTimer(t)
    t=nil
    
    
end
function MoveTimed()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    SaveUnitHandle(Hash, id, 1, u)
    SaveLocationHandle(Hash, id, 2, l)
    TimerStart(t, time, false, MoveTimedEnd)
    
    t=nil
end
function MoveWithOrderTimedEnd()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    SetUnitPositionLoc(LoadUnitHandle(Hash, id, 1), LoadLocationHandle(Hash, id, 2))
    IssueTargetOrder(LoadUnitHandle(Hash, id, 1), LoadStr(Hash, id, 4), LoadUnitHandle(Hash, id, 3))
    
    RemoveLocation(LoadLocationHandle(Hash, id, 2))
    DestroyTimer(t)
    t=nil
    
    
end
function MoveWithOrderTimed()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    SaveUnitHandle(Hash, id, 1, u)
    SaveLocationHandle(Hash, id, 2, l)
    SaveUnitHandle(Hash, id, 3, target)
    SaveStr(Hash, id, 4, order)
    TimerStart(t, time, false, MoveWithOrderTimedEnd)
 
    t=nil
end
function Trig_BlinkToUnit_attack_Actions()
    gUnit=GetAttacker()
--
--    call IssueTargetOrderBJ( gUnit, "attack", GetAttackedUnitBJ() )
--    call UnitAddAbility( 'A0N0', gUnit )
--    call SetUnitAbilityLevelSwapped( 'A0N0', gUnit, GetUnitAbilityLevelSwapped('A0MZ', gUnit) )
--    call UnitAddAbility( 'A0N2', gUnit )
--    call SetUnitAbilityLevelSwapped( 'A0N2', gUnit, GetUnitAbilityLevelSwapped('A0MZ', gUnit) )
--    call UnitRemoveAbility( 'A0MZ', gUnit )
--    
    MoveWithOrderTimed(gUnit , GetTriggerUnit() , GetUnitLoc(GetTriggerUnit()) , "attack" , 0.1)
    DummyCastTargetLevel(FourCC('A1MY') , "shadowstrike" , gUnit , GetTriggerUnit() , GetUnitAbilityLevel(gUnit, FourCC('A0MZ')))
    
    BlzStartUnitAbilityCooldown(gUnit, FourCC('A0MZ'), 3)
--    call UnitAddAbilityBJ( 'A0MZ', gUnit )
--    call SetUnitAbilityLevelSwapped( 'A0MZ', gUnit, GetUnitAbilityLevelSwapped('A0N0', gUnit) )
--    call UnitRemoveAbilityBJ( 'A0N0', gUnit )
--    call UnitRemoveAbilityBJ( 'A0N2', gUnit )
end
--===========================================================================
function InitTrig_BlinkToUnit_attack()
    gg_trg_BlinkToUnit_attack=CreateTrigger()
    DisableTrigger(gg_trg_BlinkToUnit_attack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlinkToUnit_attack, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_BlinkToUnit_attack, Condition(Trig_BlinkToUnit_attack_Conditions))
    TriggerAddAction(gg_trg_BlinkToUnit_attack, Trig_BlinkToUnit_attack_Actions)
end
--===========================================================================
-- Trigger: BlinkToUnit Spell
--===========================================================================
function Trig_BlinkToUnit_Spell_Actions()
    local l1= GetUnitLoc(GetSpellTargetUnit())
    local l2= GetUnitLoc(GetTriggerUnit())
    
    MoveWithOrderTimed(GetTriggerUnit() , GetSpellTargetUnit() , l1 , "attack" , DistanceBetweenPoints(l1, l2) / 1200 + 0.4)
    RemoveLocation(l2)
    l1=nil
    l2=nil
end
--===========================================================================
function InitTrig_BlinkToUnit_Spell()
    gg_trg_BlinkToUnit_Spell=CreateTrigger()
    DisableTrigger(gg_trg_BlinkToUnit_Spell)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlinkToUnit_Spell, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_BlinkToUnit_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0N3') then return end
        Trig_BlinkToUnit_Spell_Actions()
    end)
end
--===========================================================================
-- Trigger: Edvin Ult
--
-- ????? ? ????
--===========================================================================
function Trig_Edvin_Ult_Actions()
    local u= GetTriggerUnit()
    local u2
    local g= CreateGroup()
    GroupEnumUnitsInRange(g, GetSpellTargetX(), GetSpellTargetY(), 235.00, nil)
    
    
    
    while true do
        u2=FirstOfGroup(g)
        if u2 == nil then break end
        
        if GetOwningPlayer(u2) ~= GetOwningPlayer(u) then
            
            SetUnitX(u, GetUnitX(u2))
            SetUnitY(u, GetUnitY(u2))
            RemoveEffectTimed(AddSpecialEffect("ObjectsSpawnmodelsHumanHumanBloodHumanBloodLarge1.mdl", GetUnitX(u2), GetUnitY(u2)) , 1)
            UnitDamageTargetBJ(u, u2, ( 300 * GetUnitAbilityLevel(u, FourCC('A0N4')) + 2 * GetHeroAgi(u, true) ), ATTACK_TYPE_HERO, DAMAGE_TYPE_FORCE)
                 
            
            
        end
        
        GroupRemoveUnit(g, u2)
    end
    
    
    
    
    UnitAddAbility(u, FourCC('A0N5'))
    BlzUnitDisableAbility(u, FourCC('A0N1'), true, true)
    IssueImmediateOrder(u, "windwalk")
    BlzUnitDisableAbility(u, FourCC('A0N1'), false, false)
    BlzStartUnitAbilityCooldown(u, FourCC('A0N4'), 35)
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_Edvin_Ult()
    gg_trg_Edvin_Ult=CreateTrigger()
    DisableTrigger(gg_trg_Edvin_Ult)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Edvin_Ult, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_Edvin_Ult, function()
        if GetSpellAbilityId() ~= FourCC('A0N4') then return end
        Trig_Edvin_Ult_Actions()
    end)
end
--===========================================================================
-- Trigger: Del1FromTable C
--===========================================================================
function Trig_Del1FromTable_C_Actions()
    local i= GetPlayerId(udg_LocalPlayer)
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i + 1]))
    i=0
end
--===========================================================================
-- Trigger: OnlySelected
--===========================================================================
function Trig_Dovorougenie_3t_O_Copy_Func001C()
    if ( not ( IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true ) ) then
        return false
    end
    return true
end
--===========================================================================
-- Trigger: AutoChance
--===========================================================================
function Trig_AutoChance_Func003C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A000'), GetEventDamageSource()) >= 1 ) ) then
        return false
    end
    if ( not ( IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource())) == true ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_Conditions()
    if ( not Trig_AutoChance_Func003C() ) then
        return false
    end
    return true
end
function Trig_AutoChance_Func002C()
    if ( not ( udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 ) ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_Actions()
    udg_LocalInteger=GetRandomInt(1, 100)
    if ( Trig_AutoChance_Func002C() ) then
        AdjustPlayerStateBJ(150, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
        AdjustPlayerStateBJ(50, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    else
    end
end
--===========================================================================
function InitTrig_AutoChance()
    gg_trg_AutoChance=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance, Condition(Trig_AutoChance_Conditions))
    TriggerAddAction(gg_trg_AutoChance, Trig_AutoChance_Actions)
end
--===========================================================================
-- Trigger: AutoChance 2
--===========================================================================
function Trig_AutoChance_2_Func001C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A01A'), GetEventDamageSource()) >= 1 ) ) then
        return false
    end
    if ( not ( IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource())) == true ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_2_Conditions()
    if ( not Trig_AutoChance_2_Func001C() ) then
        return false
    end
    return true
end
function Trig_AutoChance_2_Func003C()
    if ( not ( udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 ) ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_2_Actions()
    udg_LocalInteger=GetRandomInt(1, 125)
    if ( Trig_AutoChance_2_Func003C() ) then
        AdjustPlayerStateBJ(400, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
        AdjustPlayerStateBJ(75, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    else
    end
end
--===========================================================================
function InitTrig_AutoChance_2()
    gg_trg_AutoChance_2=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance_2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance_2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance_2, Condition(Trig_AutoChance_2_Conditions))
    TriggerAddAction(gg_trg_AutoChance_2, Trig_AutoChance_2_Actions)
end
--===========================================================================
-- Trigger: AutoChance 3
--===========================================================================
function Trig_AutoChance_3_Func003C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) >= 1 ) ) then
        return false
    end
    if ( not ( IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource())) == true ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Conditions()
    if ( not Trig_AutoChance_3_Func003C() ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Func002Func001C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 1 ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Func002Func002C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 2 ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Func002Func003C()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A01B'), GetEventDamageSource()) == 3 ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Func002C()
    if ( not ( udg_LocalInteger <= ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetEventDamageSource()) * 1 ) ) ) then
        return false
    end
    return true
end
function Trig_AutoChance_3_Actions()
    udg_LocalInteger=GetRandomInt(1, 175)
    if ( Trig_AutoChance_3_Func002C() ) then
        if ( Trig_AutoChance_3_Func002Func001C() ) then
            AdjustPlayerStateBJ(2500, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(1000, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        else
        end
        if ( Trig_AutoChance_3_Func002Func002C() ) then
            AdjustPlayerStateBJ(1000, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(500, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        else
        end
        if ( Trig_AutoChance_3_Func002Func003C() ) then
            AdjustPlayerStateBJ(250, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
            AdjustPlayerStateBJ(100, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_LUMBER)
        else
        end
        IssueImmediateOrderBJ(GetEventDamageSource(), "berserk")
    else
    end
end
--===========================================================================
function InitTrig_AutoChance_3()
    gg_trg_AutoChance_3=CreateTrigger()
    DisableTrigger(gg_trg_AutoChance_3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoChance_3, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_AutoChance_3, Condition(Trig_AutoChance_3_Conditions))
    TriggerAddAction(gg_trg_AutoChance_3, Trig_AutoChance_3_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie Code O
--===========================================================================
function Trig_Dovorougenie_Code_Func001C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h003') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_Code_Func002C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h00P') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_Code_Func003C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h029') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_Code_Func004C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('n000') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_Code_O_Actions()
    if ( Trig_Dovorougenie_Code_Func001C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h005') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_Code_Func002C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h00S') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_Code_Func003C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h02A') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_Code_Func004C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('n002') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
end
--===========================================================================
function InitTrig_Dovorougenie_Code_O()
    gg_trg_Dovorougenie_Code_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_Code_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_Code_O, function()
        if GetSpellAbilityId() ~= FourCC('A000') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Dovorougenie_Code_O_Actions()
    end)
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerAddAction(gg_trg_Dovorougenie_Code_O, Trig_Del1FromTable_C_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie 2t Code O
--===========================================================================
function Trig_Dovorougenie_2t_Code_Func001C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h005') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_2t_Code_Func002C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h00S') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_2t_Code_Func003C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h02A') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_2t_Code_Func004C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('n002') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_2t_Code_O_Actions()
    if ( Trig_Dovorougenie_2t_Code_Func001C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h006') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_2t_Code_Func002C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h00U') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_2t_Code_Func003C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('h02B') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
    if ( Trig_Dovorougenie_2t_Code_Func004C() ) then
        ReplaceUnit2(GetTriggerUnit() , FourCC('n004') , bj_UNIT_STATE_METHOD_RELATIVE)
        if ( Trig_Dovorougenie_3t_O_Copy_Func001C() ) then
            SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
        else
        end
    else
    end
end
--===========================================================================
function InitTrig_Dovorougenie_2t_Code_O()
    gg_trg_Dovorougenie_2t_Code_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_2t_Code_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_2t_Code_O, function()
        if GetSpellAbilityId() ~= FourCC('A01A') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Dovorougenie_2t_Code_O_Actions()
    end)
    TriggerAddAction(gg_trg_Dovorougenie_2t_Code_O, Trig_Del1FromTable_C_Actions)
end
--===========================================================================
-- Trigger: Dovorougenie 3t O
--===========================================================================
function Trig_Dovorougenie_3t_O_Conditions()
    if ( not ( IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_3t_O_Func002Func002C()
    if ( not ( IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_3t_O_Func002C()
    if ( not ( GetUnitTypeId(GetTriggerUnit()) == FourCC('h006') ) ) then
        return false
    end
    return true
end
function Trig_Dovorougenie_3t_O_Actions()
    local i= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    if ( Trig_Dovorougenie_3t_O_Func002C() ) then
    ReplaceUnit2(GetTriggerUnit() , FourCC('h00Q') , bj_UNIT_STATE_METHOD_RELATIVE)
    if ( Trig_Dovorougenie_3t_O_Func002Func002C() ) then
        SelectUnitAddForPlayer(GetLastReplacedUnitBJ(), GetOwningPlayer(GetTriggerUnit()))
    else
    end
else
end
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i]))
    i=0
end
--===========================================================================
function InitTrig_Dovorougenie_3t_O()
    gg_trg_Dovorougenie_3t_O=CreateTrigger()
    DisableTrigger(gg_trg_Dovorougenie_3t_O)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dovorougenie_3t_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dovorougenie_3t_O, function()
        if GetSpellAbilityId() ~= FourCC('A01B') then return end
        if not Trig_Dovorougenie_3t_O_Conditions() then return end
        Trig_Dovorougenie_3t_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Voron
--===========================================================================
function Trig_Voron_Conditions()
    if ( not ( GetResearched() == FourCC('R00A') ) ) then
        return false
    end
    return true
end
function Trig_Voron_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00B'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Voron()
    gg_trg_Voron=CreateTrigger()
    DisableTrigger(gg_trg_Voron)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Voron, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Voron, Condition(Trig_Voron_Conditions))
    TriggerAddAction(gg_trg_Voron, Trig_Voron_Actions)
end
--===========================================================================
-- Trigger: Sindicat
--===========================================================================
function Trig_Sindicat_Conditions()
    if ( not ( GetResearched() == FourCC('R00B') ) ) then
        return false
    end
    return true
end
function Trig_Sindicat_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02U'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02S'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00A'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sindicat()
    gg_trg_Sindicat=CreateTrigger()
    DisableTrigger(gg_trg_Sindicat)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sindicat, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Sindicat, Condition(Trig_Sindicat_Conditions))
    TriggerAddAction(gg_trg_Sindicat, Trig_Sindicat_Actions)
end
--===========================================================================
-- Trigger: Bratstwo
--===========================================================================
function Trig_Bratstwo_Conditions()
    if ( not ( GetResearched() == FourCC('R00F') ) ) then
        return false
    end
    return true
end
function Trig_Bratstwo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Bratstwo()
    gg_trg_Bratstwo=CreateTrigger()
    DisableTrigger(gg_trg_Bratstwo)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Bratstwo, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Bratstwo, Condition(Trig_Bratstwo_Conditions))
    TriggerAddAction(gg_trg_Bratstwo, Trig_Bratstwo_Actions)
end
--===========================================================================
-- Trigger: Pirats
--===========================================================================
function Trig_Pirats_Conditions()
    if ( not ( GetResearched() == FourCC('R00E') ) ) then
        return false
    end
    return true
end
function Trig_Pirats_O_Copy_Func005002()
    return ( GetUnitTypeId(GetFilterUnit()) == FourCC('h00Y') )
end
function Trig_Pirats_O_Copy_Func008A()
    ReplaceUnit(GetEnumUnit() , FourCC('h03L') , bj_UNIT_STATE_METHOD_RELATIVE)
end
function Trig_Pirats_O_Copy_Func010002()
    return ( GetUnitTypeId(GetFilterUnit()) == FourCC('h00Z') )
end
function Trig_Pirats_O_Copy_Func013A()
    ReplaceUnit(GetEnumUnit() , FourCC('h03K') , bj_UNIT_STATE_METHOD_RELATIVE)
end
function Trig_Pirats_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h03L'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h03K'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h00Y'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h00Z'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_Boolexpr = Trig_Pirats_O_Copy_Func005002
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Pirats_O_Copy_Func008A)
    GroupClear(udg_LocalOtrad2)
    udg_Boolexpr = Trig_Pirats_O_Copy_Func010002
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_Pirats_O_Copy_Func013A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_Pirats()
    gg_trg_Pirats=CreateTrigger()
    DisableTrigger(gg_trg_Pirats)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pirats, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Pirats, Condition(Trig_Pirats_Conditions))
    TriggerAddAction(gg_trg_Pirats, Trig_Pirats_Actions)
end
--===========================================================================
-- Trigger: Shesterenka
--===========================================================================
function Trig_Shesterenka_Conditions()
    if ( not ( GetResearched() == FourCC('R00D') ) ) then
        return false
    end
    return true
end
function Trig_Shesterenka_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00C'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Shesterenka()
    gg_trg_Shesterenka=CreateTrigger()
    DisableTrigger(gg_trg_Shesterenka)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Shesterenka, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Shesterenka, Condition(Trig_Shesterenka_Conditions))
    TriggerAddAction(gg_trg_Shesterenka, Trig_Shesterenka_Actions)
end
--===========================================================================
-- Trigger: Trumnue vodu
--===========================================================================
function Trig_Trumnue_vodu_Conditions()
    if ( not ( GetResearched() == FourCC('R00C') ) ) then
        return false
    end
    return true
end
function Trig_Trumnue_vodu_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h02T'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h02R'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R00D'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Trumnue_vodu()
    gg_trg_Trumnue_vodu=CreateTrigger()
    DisableTrigger(gg_trg_Trumnue_vodu)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Trumnue_vodu, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Trumnue_vodu, Condition(Trig_Trumnue_vodu_Conditions))
    TriggerAddAction(gg_trg_Trumnue_vodu, Trig_Trumnue_vodu_Actions)
end
--===========================================================================
-- Trigger: AutoSetka
--===========================================================================
function Trig_AutoSetka_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoSetka()
    gg_trg_AutoSetka=CreateTrigger()
    DisableTrigger(gg_trg_AutoSetka)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSetka, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSetka, function()
        if GetSpellAbilityId() ~= FourCC('A011') then return end
        Trig_AutoSetka_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoSetkaHero
--===========================================================================
function Trig_AutoSetkaHero_Actions()
    UnitAddAbilityBJ(FourCC('A011'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_AutoSetkaHero()
    gg_trg_AutoSetkaHero=CreateTrigger()
    DisableTrigger(gg_trg_AutoSetkaHero)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSetkaHero, EVENT_PLAYER_HERO_SKILL)
    TriggerAddAction(gg_trg_AutoSetkaHero, function()
        if GetSpellAbilityId() ~= FourCC('A01I') then return end
        Trig_AutoSetkaHero_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoSvita
--===========================================================================
function Trig_AutoSvita_Actions()
    IssueImmediateOrderBJ(GetTriggerUnit(), "waterelemental")
end
--===========================================================================
function InitTrig_AutoSvita()
    gg_trg_AutoSvita=CreateTrigger()
    DisableTrigger(gg_trg_AutoSvita)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSvita, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSvita, function()
        if GetSpellAbilityId() ~= FourCC('A012') then return end
        Trig_AutoSvita_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoStaya
--===========================================================================
function Trig_AutoStaya_Actions()
    IssuePointOrderLocBJ(GetTriggerUnit(), "carrionswarm", GetUnitLoc(GetSpellTargetUnit()))
end
--===========================================================================
function InitTrig_AutoStaya()
    gg_trg_AutoStaya=CreateTrigger()
    DisableTrigger(gg_trg_AutoStaya)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoStaya, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoStaya, function()
        if GetSpellAbilityId() ~= FourCC('A00W') then return end
        Trig_AutoStaya_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoManaSteal
--===========================================================================
function Trig_AutoManaSteal_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "drain", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoManaSteal()
    gg_trg_AutoManaSteal=CreateTrigger()
    DisableTrigger(gg_trg_AutoManaSteal)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoManaSteal, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoManaSteal, function()
        if GetSpellAbilityId() ~= FourCC('A015') then return end
        Trig_AutoManaSteal_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoShield
--===========================================================================
function Trig_AutoShield_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "antimagicshell", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoShield()
    gg_trg_AutoShield=CreateTrigger()
    DisableTrigger(gg_trg_AutoShield)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoShield, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoShield, function()
        if GetSpellAbilityId() ~= FourCC('A016') then return end
        Trig_AutoShield_Actions()
    end)
end
--===========================================================================
-- Trigger: ResearhRobbery
--===========================================================================
function Trig_ResearhRobbery_Conditions()
    if ( not ( GetResearched() == FourCC('R00I') ) ) then
        return false
    end
    return true
end
function Trig_ResearhRobbery_Func001Func001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1 )
end
function Trig_ResearhRobbery_Func001Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 2)
end
function Trig_ResearhRobbery_Func001C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_ResearhRobbery_Func002Func001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1 )
end
function Trig_ResearhRobbery_Func002Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 3)
end
function Trig_ResearhRobbery_Func002C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_ResearhRobbery_Func003Func001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) >= 1 )
end
function Trig_ResearhRobbery_Func003Func004A()
    SetUnitAbilityLevelSwapped(FourCC('A00M'), GetEnumUnit(), 4)
end
function Trig_ResearhRobbery_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 4 ) ) then
        return false
    end
    return true
end
function Trig_ResearhRobbery_Actions()
    if ( Trig_ResearhRobbery_Func001C() ) then
        udg_Boolexpr = Trig_ResearhRobbery_Func001Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func001Func004A)
        GroupClear(udg_LocalOtrad2)
    else
    end
    if ( Trig_ResearhRobbery_Func002C() ) then
        udg_Boolexpr = Trig_ResearhRobbery_Func002Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func002Func004A)
        GroupClear(udg_LocalOtrad2)
    else
    end
    if ( Trig_ResearhRobbery_Func003C() ) then
        udg_Boolexpr = Trig_ResearhRobbery_Func003Func001002
        GroupEnumUnitsOfPlayer(udg_LocalOtrad2, udg_LocalPlayer, udg_Boolexpr)
        ForGroupBJ(udg_LocalOtrad2, Trig_ResearhRobbery_Func003Func004A)
        GroupClear(udg_LocalOtrad2)
    else
    end
end
--===========================================================================
function InitTrig_ResearhRobbery()
    gg_trg_ResearhRobbery=CreateTrigger()
    DisableTrigger(gg_trg_ResearhRobbery)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ResearhRobbery, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_ResearhRobbery, Condition(Trig_ResearhRobbery_Conditions))
    TriggerAddAction(gg_trg_ResearhRobbery, Trig_ResearhRobbery_Actions)
end
--===========================================================================
-- Trigger: RobberyTrain
--===========================================================================
function Trig_RobberyTrain_Conditions()
    if ( not ( GetUnitAbilityLevelSwapped(FourCC('A00M'), GetTriggerUnit()) == 1 ) ) then
        return false
    end
    return true
end
function Trig_RobberyTrain_Func002C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 2 ) ) then
        return false
    end
    return true
end
function Trig_RobberyTrain_Func003C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 3 ) ) then
        return false
    end
    return true
end
function Trig_RobberyTrain_Func004C()
    if ( not ( GetPlayerTechCountSimple(FourCC('R00I'), GetOwningPlayer(GetTriggerUnit())) == 4 ) ) then
        return false
    end
    return true
end
function Trig_RobberyTrain_Actions()
    if ( Trig_RobberyTrain_Func002C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 2)
    else
    end
    if ( Trig_RobberyTrain_Func003C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 3)
    else
    end
    if ( Trig_RobberyTrain_Func004C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A00M'), GetTrainedUnit(), 4)
    else
    end
end
--===========================================================================
function InitTrig_RobberyTrain()
    gg_trg_RobberyTrain=CreateTrigger()
    DisableTrigger(gg_trg_RobberyTrain)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RobberyTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_RobberyTrain, Condition(Trig_RobberyTrain_Conditions))
    TriggerAddAction(gg_trg_RobberyTrain, Trig_RobberyTrain_Actions)
end
--===========================================================================
-- Trigger: RobberyOfPlayer
--===========================================================================
function Trig_RobberyOfPlayer_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A00M')) >= 1
end
function Trig_RobberyOfPlayer_Actions()
    local i= GetUnitGoldCost(GetUnitTypeId(GetTriggerUnit()))
    local lvl= GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A00M'))
    
    i=R2I(i * 0.25 * lvl)
    AdjustPlayerStateBJ(- i, GetOwningPlayer(GetEventDamageSource()), PLAYER_STATE_RESOURCE_GOLD)
end
--===========================================================================
function InitTrig_RobberyOfPlayer()
    gg_trg_RobberyOfPlayer=CreateTrigger()
    DisableTrigger(gg_trg_RobberyOfPlayer)
    TriggerRegisterAnyUnitEventBJ(gg_trg_RobberyOfPlayer, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_RobberyOfPlayer, Condition(Trig_RobberyOfPlayer_Conditions))
    TriggerAddAction(gg_trg_RobberyOfPlayer, Trig_RobberyOfPlayer_Actions)
end
--===========================================================================
-- Trigger: AreaOfDeath2
--===========================================================================
function Trig_AreaOfDeath2_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local level= GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1K1'))
    
    local u
    local u2
    local i= 0
   
    
    u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
    UnitAddAbility(u2, FourCC('ANrf'))
    SetUnitManaBJ(u2, 1111111.00)
    SetUnitAbilityLevel(u2, FourCC('ANrf'), level)
    IssuePointOrderLoc(u2, "rainoffire", l)
    RemoveLocation(l)
    
    RemoveUnitTimed(u2 , 25)
    
    u=nil
    
    p=nil
    u2=nil
end
--===========================================================================
function InitTrig_AreaOfDeath2()
