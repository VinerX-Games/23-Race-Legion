    gg_trg_Klap_Klap_War_big=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War_big, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War_big, Condition(Trig_Klap_Klap_War_big_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War_big, Trig_Klap_Klap_War_big_Actions)
end
--===========================================================================
-- Trigger: HordeOn
--===========================================================================
function Trig_HordeOn_Actions()
    
    EnableTrigger(gg_trg_K1T1)
    EnableTrigger(gg_trg_K1T2)
    EnableTrigger(gg_trg_K1T2b)
    EnableTrigger(gg_trg_K1TCav)
    EnableTrigger(gg_trg_K1T4)
    
    EnableTrigger(gg_trg_K2T1)
    EnableTrigger(gg_trg_K2T2)
    EnableTrigger(gg_trg_K2T2b)
    EnableTrigger(gg_trg_K2T3)
    EnableTrigger(gg_trg_KM1)
    EnableTrigger(gg_trg_KM2)
    EnableTrigger(gg_trg_KM3)
 
    EnableTrigger(gg_trg_TechT1)
    EnableTrigger(gg_trg_TechT2)
    
    EnableTrigger(gg_trg_NavyHeavy)
    EnableTrigger(gg_trg_NavyLight)
--    call EnableTrigger( gg_trg_ParazitB )
--    call EnableTrigger( gg_trg_ParazitC )
--    call EnableTrigger( gg_trg_PlodovitostOsaB )
--    call EnableTrigger( gg_trg_PlodovitostOsaC )
--    call EnableTrigger( gg_trg_PlodovitostVoinaB )
--    call EnableTrigger( gg_trg_PlodovitostVoinaC )
--    
--    call EnableTrigger( gg_trg_KriliaF )
--    call EnableTrigger( gg_trg_KriliaB )
--    call EnableTrigger( gg_trg_KriliaC )
--    call EnableTrigger( gg_trg_DelimostF )
--    call EnableTrigger( gg_trg_DelimostB )
--    call EnableTrigger( gg_trg_DelimostC )
--    
--    call EnableTrigger( gg_trg_SlizeF )
--    call EnableTrigger( gg_trg_SlizeB )
--    call EnableTrigger( gg_trg_SlizeC )
--
--    call EnableTrigger( gg_trg_TankB )
--    call EnableTrigger( gg_trg_TankC )
    
        
    EnableTrigger(gg_trg_ThrallMolnya)
    EnableTrigger(gg_trg_Okovi)
    EnableTrigger(gg_trg_GarraoshMassBloodlast)
    --call EnableTrigger( gg_trg_K2T3)
    EnableTrigger(gg_trg_BerserkOrc)
    EnableTrigger(gg_trg_BerserkTrol)
    EnableTrigger(gg_trg_AutoSetkaH)
    EnableTrigger(gg_trg_IronStar)
    EnableTrigger(gg_trg_AutoShield2)
    EnableTrigger(gg_trg_PandaSecondAttack)
    EnableTrigger(gg_trg_DragonFire)
    
    EnableTrigger(gg_trg_ShaSpell)
    
end
--===========================================================================
function InitTrig_HordeOn()
    gg_trg_HordeOn=CreateTrigger()
    TriggerAddAction(gg_trg_HordeOn, Trig_HordeOn_Actions)
end
--===========================================================================
-- Trigger: AiFixTrain
--===========================================================================
function aiFixTrainBefore(oldUnit, pi)
    
    if udg_AiControl[pi] then
        --call GroupRemoveUnit( udg_Ai_army[pi],oldUnit )
        --call GroupRemoveUnit( udg_Ai_units[pi],oldUnit )
        NumberRem(pi , GetUnitTypeId(oldUnit))
        NumberRem(pi , StringHash("Number"))
        return true
    end
    
    return false
end
function aiFixTrainAfter(NewUnit, pi)
    if udg_AiControl[pi] then
        aiUnitJoins(NewUnit , pi)
    end
    
end
--===========================================================================
-- Trigger: K1T1
--===========================================================================
function Trig_K1T1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('ogru')
end
function T1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01I')
            b=b + 1
            if b >= i then break end
    end
    --2 ???? ?????? ????
    if GetPlayerTechCount(p, FourCC('R0D1'), true) == 1 and GetPlayerTechCount(p, FourCC('R0EH'), true) < 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01E')
            
            b=b + 1
            if b >= i then break end
        end
    end
    --3 ???? - ?????
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01F')
            
            b=b + 1
            if b >= i then break end
        end
    end
    --4 ???? ??????
    if GetPlayerTechCount(p, FourCC('R0D3'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01H')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["T1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["T1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K1T1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["T1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["T1" .. i] or 0)
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--   
--    call UnitAddAbility(u,'OR00')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
--    
--    call UnitAddAbility(u,'A1J0')
--    if udg_HordeLandPrice[pi] > 0 then
--        call BlzSetAbilityExtendedTooltip( 'A1J0', ""+I2S((udg_HordeLandPrice[pi])+".", 0 )
--    elseif udg_HordeLandPrice[pi] < 0 then
--        call BlzSetAbilityExtendedTooltip( 'A1J0', ""+I2S((udg_HordeLandPrice[pi])+".", 0 )
--    endif
    
    UnitAddAbility(u, FourCC('A0YU'))
    
    -- Ai moment    
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    u=nil
end
--===========================================================================
function InitTrig_K1T1()
    gg_trg_K1T1=CreateTrigger()
    DisableTrigger(gg_trg_K1T1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K1T1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K1T1, Condition(Trig_K1T1_Conditions))
    TriggerAddAction(gg_trg_K1T1, Trig_K1T1_Actions)
end
--===========================================================================
-- Trigger: K1T2
--===========================================================================
function Trig_K1T2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o01N')
end
function T2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    
    b=0
    i=2
    while true do --???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01Q')
            b=b + 1
            if b >= i then break end
    end
    
    b=0
    i=1
    while true do --???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01O')
            b=b + 1
            if b >= i then break end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0EE'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        b=0
        i=1
        while true do --Pandaren
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o02S')
                b=b + 1
                if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["T2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["T2" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K1T2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    -- 
    i=(CommonHash[pi]["T2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["T2" .. i] or 0)
    --
    
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
    IssuePointOrderLoc(u, "attack", l)
--
--    call UnitAddAbility(u,'OR00')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
--    
    
     
    UnitAddAbility(u, FourCC('A0YU'))
    
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K1T2()
    gg_trg_K1T2=CreateTrigger()
    DisableTrigger(gg_trg_K1T2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K1T2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K1T2, Condition(Trig_K1T2_Conditions))
    TriggerAddAction(gg_trg_K1T2, Trig_K1T2_Actions)
end
--===========================================================================
-- Trigger: K1T2b
--===========================================================================
function Trig_K1T2b_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o029')
end
function T2bCount(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    
    b=0
    i=5
    while true do --???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02A')
            b=b + 1
            if b >= i then break end
    end
    
    b=0
    i=2
    while true do --???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o00A')
            b=b + 1
            if b >= i then break end
    end
    
    --Long Containment
    CommonHash[pi]["T2b_0"] = a[0]
    i=1
    while true do
       
        
        CommonHash[pi]["T2b" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K1T2b_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    
    
    -- 
    i=(CommonHash[pi]["T2b_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["T2b" .. i] or 0)
    --
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    //Elite
--    call UnitAddAbility(u,'A0UX')
--    call SetUnitAbilityLevel(u,'A0UX',35+udg_HordeElitePrice[pi])
--    
    
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K1T2b()
    gg_trg_K1T2b=CreateTrigger()
    DisableTrigger(gg_trg_K1T2b)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K1T2b, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K1T2b, Condition(Trig_K1T2b_Conditions))
    TriggerAddAction(gg_trg_K1T2b, Trig_K1T2b_Actions)
end
--===========================================================================
-- Trigger: K1TCav
--===========================================================================
function Trig_K1TCav_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('orai')
end
function TCavCount(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    
    b=0
    i=3
    while true do --???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o027')
            b=b + 1
            if b >= i then break end
    end
    
    --3 ???? - ?????
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02H')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --???????? ?????
    if GetPlayerTechCount(p, FourCC('R0E1'), true) == 1 and GetPlayerTechCount(p, FourCC('R0EH'), true) < 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01Z')
            
            b=b + 1
            if b >= i then break end
        end
    end
    --?????????
    if GetPlayerTechCount(p, FourCC('R0E5'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02E')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    --Long Containment
    CommonHash[pi]["TCav_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["TCav" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K1TCav_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    
    -- 
    i=(CommonHash[pi]["TCav_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["TCav" .. i] or 0)
    --
    
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--
--    call UnitAddAbility(u,'OR00')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
--    
    
     
    UnitAddAbility(u, FourCC('A0YU'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K1TCav()
    gg_trg_K1TCav=CreateTrigger()
    DisableTrigger(gg_trg_K1TCav)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K1TCav, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K1TCav, Condition(Trig_K1TCav_Conditions))
    TriggerAddAction(gg_trg_K1TCav, Trig_K1TCav_Actions)
end
--===========================================================================
-- Trigger: K1T4
--===========================================================================
function Trig_K1T4_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('otau')
end
function T3Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        b=0
        i=5
        while true do -- ??????
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o01L')
                
                
                b=b + 1
                if b >= i then break end
        end
    end
    b=0
    i=2
    while true do -- ???-???????
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01M')
            b=b + 1
            if b >= i then break end
    end
    
    --Cor Cron
    if GetPlayerTechCount(p, FourCC('R0E0'), false) == 1 and GetPlayerTechCount(p, FourCC('R0EH'), true) < 1 then
        i=4
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01U')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Death knight
    if GetPlayerTechCount(p, FourCC('R0E3'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o021')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0EE'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        b=0
        i=2
        while true do --Pandaren
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o02W')
                b=b + 1
                if b >= i then break end
        end
    end
    
    
    --Long Containment
    CommonHash[pi]["T3_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["T3" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K1T4_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    
    
    
    -- 
    i=(CommonHash[pi]["T3_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["T3" .. i] or 0)
    --
    
    --??? ?????
    if b == FourCC('o01L') and Random(1 , 25) then
        b=FourCC('o032')
    end
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
    
--    
--    // Elite Price
--    call UnitAddAbility(u,'A0UX')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeElitePrice[pi])
--    
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K1T4()
    gg_trg_K1T4=CreateTrigger()
    DisableTrigger(gg_trg_K1T4)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K1T4, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K1T4, Condition(Trig_K1T4_Conditions))
    TriggerAddAction(gg_trg_K1T4, Trig_K1T4_Actions)
end
--===========================================================================
-- Trigger: K2T1
--===========================================================================
function Trig_K2T1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('ohun')
end
function K1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    --1 ????
    a[0]=0
    
    -- Troll
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        i=5
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o01G')
                b=b + 1
                if b >= i then break end
        end
    end
    
    --???
    b=0
    i=2
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01X')
            b=b + 1
            if b >= i then break end
    end
    
    
    
--    if GetPlayerTechCount(p,'R0D1',true) >= 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01E'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
    
    
    --Long Containment
    CommonHash[pi]["K1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["K1" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K2T1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    
    -- 
    i=(CommonHash[pi]["K1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["K1" .. i] or 0)
    --
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
    
--    
--    call UnitAddAbility(u,'OR00')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
--    
    
     
    UnitAddAbility(u, FourCC('A0YU'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K2T1()
    gg_trg_K2T1=CreateTrigger()
    DisableTrigger(gg_trg_K2T1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K2T1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K2T1, Condition(Trig_K2T1_Conditions))
    TriggerAddAction(gg_trg_K2T1, Trig_K2T1_Actions)
end
--===========================================================================
-- Trigger: K2T2
--===========================================================================
function Trig_K2T2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o01P')
end
function K2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
   a[0]=0
    
    
    
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        i=4
        -- Troll
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('otbk')
                b=b + 1
                if b >= i then break end
        end
    
    end
    
    -- black mountain orc
    if GetPlayerTechCount(p, FourCC('R0D1'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01Y')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Goblin sniper
    if GetPlayerTechCount(p, FourCC('R0E4'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02F')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["K2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["K2" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K2T2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    -- 
    i=(CommonHash[pi]["K2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["K2" .. i] or 0)
    --
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
    
--    call UnitAddAbility(u,'OR00')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
--    
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K2T2()
    gg_trg_K2T2=CreateTrigger()
    DisableTrigger(gg_trg_K2T2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K2T2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K2T2, Condition(Trig_K2T2_Conditions))
    TriggerAddAction(gg_trg_K2T2, Trig_K2T2_Actions)
end
--===========================================================================
-- Trigger: K2T2b
--===========================================================================
function Trig_K2T2b_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o02B')
end
function K2bCount(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    
    
    
    
    -- ironhorde orc
    
    i=1
    b=3
    
    while true do
        a[0]=a[0] + 1
        a[a[0]]=FourCC('o02D')
        
        b=b + 1
        if b >= i then break end
    end
    
    -- black mountain orc
    
    i=1
    b=1
    
    while true do
        a[0]=a[0] + 1
        a[a[0]]=FourCC('o02C')
        
        b=b + 1
        if b >= i then break end
    end
    --??????? 2
    if GetPlayerTechCount(p, FourCC('R0E4'), true) >= 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02J')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["K2b_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["K2b" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K2T2b_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    -- 
    i=(CommonHash[pi]["K2b_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["K2b" .. i] or 0)
    --
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    //Elite
--    call UnitAddAbility(u,'A0UX')
--    call SetUnitAbilityLevel(u,'A0UX',35+udg_HordeElitePrice[pi])
--    
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K2T2b()
    gg_trg_K2T2b=CreateTrigger()
    DisableTrigger(gg_trg_K2T2b)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K2T2b, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K2T2b, Condition(Trig_K2T2b_Conditions))
    TriggerAddAction(gg_trg_K2T2b, Trig_K2T2b_Actions)
end
--===========================================================================
-- Trigger: K2T3
--===========================================================================
function Trig_K2T3_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('okod')
end
function K3Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    
    
    -- Kodo-orc
    b=0
    i=2
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01R')
            b=b + 1
            if b >= i then break end
    end
    
    --Dragon    
    if GetPlayerTechCount(p, FourCC('R0E1'), true) >= 1 and GetPlayerTechCount(p, FourCC('R0EH'), true) < 1 then
        b=0
        i=2
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o01S')
                b=b + 1
                if b >= i then break end
        end
    end
    --Dark ranger    
    if GetPlayerTechCount(p, FourCC('R0D3'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        b=0
        i=2
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o02M')
                b=b + 1
                if b >= i then break end
        end
    end
    
    
    --Long Containment
    CommonHash[pi]["K3_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["K3" .. i] = a[i]
        i=i + 1
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_K2T3_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    
    -- 
    i=(CommonHash[pi]["K3_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["K3" .. i] or 0)
    --
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    // Elite Price
--    call UnitAddAbility(u,'A0UX')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeElitePrice[pi])
--
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_K2T3()
    gg_trg_K2T3=CreateTrigger()
    DisableTrigger(gg_trg_K2T3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_K2T3, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_K2T3, Condition(Trig_K2T3_Conditions))
    TriggerAddAction(gg_trg_K2T3, Trig_K2T3_Actions)
end
--===========================================================================
-- Trigger: KM1
--===========================================================================
function Trig_KM1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('oshm')
end
function Trig_KM1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    a[0]=0
    --1 ????
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        
        i=5
        while true do --?????
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o01J')
                b=b + 1
                if b >= i then break end
        end
    else
        
        i=4
        while true do --??????
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o02G')
                b=b + 1
                if b >= i then break end
        end
    
    end
    
    -- ????????????
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        b=1
        i=3
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('ospw')
                b=b + 1
                if b >= i then break end
        end
    end
    
    
    b=1
    i=2
    while true do --???-???
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01K')
            b=b + 1
            if b >= i then break end
    end
    
    
--    //???????? ????? - ??????
--    if GetPlayerTechCount(p,'R0E1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o02G'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
    
    -- ????????????
    if GetPlayerTechCount(p, FourCC('R0F4'), true) >= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02U')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    i=GetRandomInt(1, a[0])
    b=a[i]
   
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    call UnitAddAbility(u,'A0UY')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeMagicPrice[pi])
--    
    
     
    
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_KM1()
    gg_trg_KM1=CreateTrigger()
    DisableTrigger(gg_trg_KM1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KM1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_KM1, Condition(Trig_KM1_Conditions))
    TriggerAddAction(gg_trg_KM1, Trig_KM1_Actions)
end
--===========================================================================
-- Trigger: KM2
--===========================================================================
function Trig_KM2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o01W')
end
function Trig_KM2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    --1 ????
    a[0]=0
  
  
    -- ???????
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o023')
            
            b=b + 1
            if b >= i then break end
        end
    end
    -- ?????? ?????
    if GetPlayerTechCount(p, FourCC('R0E9'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o01V')
            
            b=b + 1
            if b >= i then break end
        end
    
    
    end
    i=GetRandomInt(1, a[0])
    b=a[i]
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
    
--    
--    call UnitAddAbility(u,'A0UY')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeMagicPrice[pi])
--    
    
     
    
    UnitAddAbility(u, FourCC('A0YU'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_KM2()
    gg_trg_KM2=CreateTrigger()
    DisableTrigger(gg_trg_KM2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KM2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_KM2, Condition(Trig_KM2_Conditions))
    TriggerAddAction(gg_trg_KM2, Trig_KM2_Actions)
end
--===========================================================================
-- Trigger: KM3
--===========================================================================
function Trig_KM3_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('odoc')
end
function Trig_KM3_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    a[0]=0
    
    --1 ????
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        
        i=4
        while true do --???????
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o024')
                b=b + 1
                if b >= i then break end
        end
    else
        
        i=3
        while true do --?????? ???
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o02L')
                b=b + 1
                if b >= i then break end
        end
    
    
    
    
    end
    
    -- ???????
    if GetPlayerTechCount(p, FourCC('R0D2'), true) >= 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=2
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o025')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    -- ?????
    if GetPlayerTechCount(p, FourCC('R0E4'), true) >= 1 then
        i=1
        b=2
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02I')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    -- Killer
    if GetPlayerTechCount(p, FourCC('R0D3'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=2
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0IH')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    i=GetRandomInt(1, a[0])
    b=a[i]
    
   aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    
--    call UnitAddAbility(u,'A0UY')
--    call SetUnitAbilityLevel(u,'OR00',35+udg_HordeMagicPrice[pi])
--    
    
     
    
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_KM3()
    gg_trg_KM3=CreateTrigger()
    DisableTrigger(gg_trg_KM3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_KM3, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_KM3, Condition(Trig_KM3_Conditions))
    TriggerAddAction(gg_trg_KM3, Trig_KM3_Actions)
end
--===========================================================================
-- Trigger: TechT1
--===========================================================================
function Trig_TechT1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('ocat')
end
function Trig_TechT1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    a[0]=0
    
    --1 ????
    if GetPlayerTechCount(p, FourCC('R0EA'), true) < 1 then
        
        b=0
        i=2
        while true do -- Destroyer
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o01T')
                b=b + 1
                if b >= i then break end
        end
        
    else
        
        b=0
        i=2
        while true do -- Better Destroyer
                a[0]=a[0] + 1
                a[a[0]]=FourCC('o020')
                b=b + 1
                if b >= i then break end
        end
    
    end
    --3 ???? - ????? ballista
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o02K')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    
    
    i=GetRandomInt(1, a[0])
    b=a[i]
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--
--    call UnitAddAbility(u,'A0UZ')
--    call SetUnitAbilityLevel(u,'A0UZ',35+udg_HordeTechPrice[pi])
--
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_TechT1()
    gg_trg_TechT1=CreateTrigger()
    DisableTrigger(gg_trg_TechT1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TechT1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TechT1, Condition(Trig_TechT1_Conditions))
    TriggerAddAction(gg_trg_TechT1, Trig_TechT1_Actions)
end
--===========================================================================
-- Trigger: TechT2
--===========================================================================
function Trig_TechT2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('o022')
end
function Trig_TechT2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    --1 ????
    a[0]=0
    
    --blood elves arcane guard
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o026')
            
            b=b + 1
            if b >= i then break end
        end
    end
    --Goblins golem
    if GetPlayerTechCount(p, FourCC('R0E4'), true) == 1 then
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o028')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    i=GetRandomInt(1, a[0])
    b=a[i]
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--
--    call UnitAddAbility(u,'A0UZ')
--    call SetUnitAbilityLevel(u,'A0UZ',35+udg_HordeTechPrice[pi])
--
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_TechT2()
    gg_trg_TechT2=CreateTrigger()
    DisableTrigger(gg_trg_TechT2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TechT2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TechT2, Condition(Trig_TechT2_Conditions))
    TriggerAddAction(gg_trg_TechT2, Trig_TechT2_Actions)
end
--===========================================================================
-- Trigger: NavyHeavy
--===========================================================================
function Trig_NavyHeavy_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0HK')
end
function Trig_NavyHeavy_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    a[0]=0
    
    --1 ????
    if GetPlayerTechCount(p, FourCC('R0E9'), true) < 1 then
        
        b=0
        i=2
        while true do -- Drednout
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0D5')
                b=b + 1
                if b >= i then break end
        end
        
    else
        
        b=0
        i=2
        while true do -- ArmoredShip
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0HM')
                b=b + 1
                if b >= i then break end
        end
    
    end
    --??????
    if GetPlayerTechCount(p, FourCC('R0D3'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0I5')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    
    
    i=GetRandomInt(1, a[0])
    b=a[i]
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--
--    call UnitAddAbility(u,'A0UZ')
--    call SetUnitAbilityLevel(u,'A0V0',35+udg_HordeNavyPrice[pi])
--
     
    UnitAddAbility(u, FourCC('A0YU'))
    
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_NavyHeavy()
    gg_trg_NavyHeavy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NavyHeavy, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_NavyHeavy, Condition(Trig_NavyHeavy_Conditions))
    TriggerAddAction(gg_trg_NavyHeavy, Trig_NavyHeavy_Actions)
end
--===========================================================================
-- Trigger: NavyLight
--===========================================================================
function Trig_NavyLight_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0HN')
end
function Trig_NavyLight_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    a[0]=0
    
    --1 ????
    b=0
    i=4
    while true do -- Fregat
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0D6')
            b=b + 1
            if b >= i then break end
    end
    --4 ???? ??????
    if GetPlayerTechCount(p, FourCC('R0D3'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0J3')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --4 ???? ??????
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 and GetPlayerTechCount(p, FourCC('R0E9'), true) ~= 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0HT')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    --?????????
    if GetPlayerTechCount(p, FourCC('R0F3'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0J4')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --?????????
    if GetPlayerTechCount(p, FourCC('R0E4'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0JB')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    i=GetRandomInt(1, a[0])
    b=a[i]
    
    aiFixTrainBefore(GetTrainedUnit() , pi)
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    aiFixTrainAfter(u , pi)
--    call UnitAddAbility(u,'A0UZ')
--    call SetUnitAbilityLevel(u,'A0V0',35+udg_HordeNavyPrice[pi])
--
     
    UnitAddAbility(u, FourCC('A0YU'))
        IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_NavyLight()
    gg_trg_NavyLight=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NavyLight, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_NavyLight, Condition(Trig_NavyLight_Conditions))
    TriggerAddAction(gg_trg_NavyLight, Trig_NavyLight_Actions)
end
--===========================================================================
-- Trigger: TrallHordeForever
--===========================================================================
function Trig_TrallHordeForever_Conditions()
    return GetResearched() == FourCC('R0DW')
end
function Trig_TrallHordeForever_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    local g= CreateGroup()
    udg_MainPrice[pi]=udg_MainPrice[pi] - 15
    
    --???????? ?????
    SetPlayerTechMaxAllowed(p, FourCC('R0DY'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0DX'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0DZ'), 0)
end
--===========================================================================
function InitTrig_TrallHordeForever()
    gg_trg_TrallHordeForever=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrallHordeForever, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_TrallHordeForever, Condition(Trig_TrallHordeForever_Conditions))
    TriggerAddAction(gg_trg_TrallHordeForever, Trig_TrallHordeForever_Actions)
end
--===========================================================================
-- Trigger: NoLeft
--===========================================================================
function Trig_NoLeft_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0DY'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EI'), 0, GetOwningPlayer(GetTriggerUnit()))
    -- -
    SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0D2'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EH'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NoLeft()
    gg_trg_NoLeft=CreateTrigger()
    TriggerAddAction(gg_trg_NoLeft, Trig_NoLeft_Actions)
end
--===========================================================================
-- Trigger: YesLeft
--===========================================================================
function Trig_YesLeft_Func001C()
    return GetPlayerTechMaxAllowedSwap(FourCC('R0D3'), GetOwningPlayer(GetTriggerUnit())) == 0
end
function Trig_YesLeft_Func002C()
    return true
end
function Trig_YesLeft_Func003C()
    return GetPlayerTechCountSimple(FourCC('R0D3'), GetOwningPlayer(GetTriggerUnit())) == 0
end
function Trig_YesLeft_Func004C()
    return GetPlayerTechMaxAllowedSwap(FourCC('R0D2'), GetOwningPlayer(GetTriggerUnit())) == 0
end
function Trig_YesLeft_Actions()
    if Trig_YesLeft_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0DY'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if true then -- INLINED!!
        SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_YesLeft_Func003C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_YesLeft_Func004C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    SetPlayerTechMaxAllowedSwap(FourCC('R0EI'), 0, GetOwningPlayer(GetTriggerUnit()))
    -- -
    SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0D2'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EH'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_YesLeft()
    gg_trg_YesLeft=CreateTrigger()
    TriggerAddAction(gg_trg_YesLeft, Trig_YesLeft_Actions)
end
--===========================================================================
-- Trigger: NoRight
--===========================================================================
function Trig_NoRight_Actions()
end
--===========================================================================
function InitTrig_NoRight()
    gg_trg_NoRight=CreateTrigger()
    TriggerAddAction(gg_trg_NoRight, Trig_NoRight_Actions)
end
--===========================================================================
-- Trigger: YesRight
--===========================================================================
function Trig_YesRight_Actions()
end
--===========================================================================
function InitTrig_YesRight()
    gg_trg_YesRight=CreateTrigger()
    TriggerAddAction(gg_trg_YesRight, Trig_YesRight_Actions)
end
--===========================================================================
-- Trigger: Counters
--===========================================================================
function countAll(p)
    T1Count(p)
    T2Count(p)
    T2bCount(p)
    TCavCount(p)
    T3Count(p)
    
    K1Count(p)
    K2Count(p)
    K2bCount(p)
    K3Count(p)
end
--===========================================================================
-- Trigger: StartCommonHome
--===========================================================================
function Trig_StartCommonHome_Conditions()
    return GetResearched() == FourCC('R0DY')
end
function Trig_StartCommonHome_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 1, GetOwningPlayer(GetTriggerUnit()))
    -- -
    SetPlayerTechMaxAllowedSwap(FourCC('R0DW'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StartCommonHome()
    gg_trg_StartCommonHome=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartCommonHome, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StartCommonHome, Condition(Trig_StartCommonHome_Conditions))
    TriggerAddAction(gg_trg_StartCommonHome, Trig_StartCommonHome_Actions)
end
--===========================================================================
-- Trigger: Forsaken
--===========================================================================
function Trig_Forsaken_Conditions()
    return GetResearched() == FourCC('R0D3')
end
function Trig_Forsaken_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 4
--    set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] - 4
--    set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 2
--    set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] - 2
    
--    
--    call ChangeLandUnitsNow(p,pi)
--    call ChangeEliteUnitsNow(p,pi)
--    
--    call ChangeNavyUnitsNow(p,pi)
--    
--    
    
    
    SetPlayerTechMaxAllowed(p, FourCC('R0D2'), 1)
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_Forsaken()
    gg_trg_Forsaken=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Forsaken, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Forsaken, Condition(Trig_Forsaken_Conditions))
    TriggerAddAction(gg_trg_Forsaken, Trig_Forsaken_Actions)
end
--===========================================================================
-- Trigger: BloodElf
--===========================================================================
function Trig_BloodElf_Conditions()
    return GetResearched() == FourCC('R0D2')
end
function Trig_BloodElf_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 4
--    set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] - 3
--    set udg_HordeMagicPrice[pi] = udg_HordeMagicPrice[pi] - 6
--    set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] - 2
--    set udg_HordeTechPrice[pi] = udg_HordeTechPrice[pi] - 2
--    call ChangeTechUnitsNow(p,pi)
--    call ChangeLandUnitsNow(p,pi)
--    call ChangeMagicUnitsNow(p,pi)
--    call ChangeNavyUnitsNow(p,pi)
    
    
    
    
    
    
    
    SetPlayerTechResearched(p, FourCC('R0E8'), 1) -- ????????? ?????? ???????
    SetPlayerTechResearched(p, FourCC('R0E7'), 1) --????????? ??
    SetPlayerTechMaxAllowed(p, FourCC('R0EE'), 1)
    
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_BloodElf()
    gg_trg_BloodElf=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BloodElf, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BloodElf, Condition(Trig_BloodElf_Conditions))
    TriggerAddAction(gg_trg_BloodElf, Trig_BloodElf_Actions)
end
--===========================================================================
-- Trigger: Pandarens
--===========================================================================
function Trig_Pandarens_Conditions()
    return GetResearched() == FourCC('R0EE')
end
function Trig_Pandarens_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
--    set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] - 3
--    set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 2
--    call ChangeLandUnitsNow(p,pi)
--    call ChangeEliteUnitsNow(p,pi)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0EH'), 1)
    --Compromise
    if GetPlayerTechCount(p, FourCC('R0EE'), true) == 1 then
        SetPlayerTechMaxAllowed(p, FourCC('R0EI'), 1)
    end
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Pandarens()
    gg_trg_Pandarens=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pandarens, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Pandarens, Condition(Trig_Pandarens_Conditions))
    TriggerAddAction(gg_trg_Pandarens, Trig_Pandarens_Actions)
end
--===========================================================================
-- Trigger: BeginCommonHome
--===========================================================================
function Trig_BeginCommonHome_Conditions()
    return GetResearched() == FourCC('R0EH')
end
function Trig_BeginCommonHome_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0DX'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BeginCommonHome()
    gg_trg_BeginCommonHome=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeginCommonHome, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BeginCommonHome, Condition(Trig_BeginCommonHome_Conditions))
    TriggerAddAction(gg_trg_BeginCommonHome, Trig_BeginCommonHome_Actions)
end
--===========================================================================
-- Trigger: CanselCommonHome
--===========================================================================
function Trig_CanselCommonHome_Conditions()
    return GetResearched() == FourCC('R0E9')
end
function Trig_CanselCommonHome_Func001C()
    return GetPlayerTechMaxAllowedSwap(FourCC('R0D1'), GetOwningPlayer(GetTriggerUnit())) == 0
end
function Trig_CanselCommonHome_Actions()
    if Trig_CanselCommonHome_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0DX'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanselCommonHome()
    gg_trg_CanselCommonHome=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselCommonHome, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanselCommonHome, Condition(Trig_CanselCommonHome_Conditions))
    TriggerAddAction(gg_trg_CanselCommonHome, Trig_CanselCommonHome_Actions)
end
--===========================================================================
-- Trigger: CommonHome
--===========================================================================
function Trig_CommonHome_Conditions()
    return GetResearched() == FourCC('R0EH')
end
function NoneRadicals()
    local id= GetUnitTypeId(GetFilterUnit())
    return id == FourCC('o01U') or id == FourCC('o01Z') or id == FourCC('o02G') or id == FourCC('o01Y') or id == FourCC('o01S') or id == FourCC('o01E') or id == FourCC('o02L')
end
function Trig_CommonHome_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    local g= CreateGroup()
    udg_MainPrice[pi]=udg_MainPrice[pi] - 10
    countAll(p)
    
    
    
    --End other races
    g=CreateGroup()
    udg_Boolexpr = NoneRadicals
    GroupEnumUnitsOfPlayer(g, p, udg_Boolexpr)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        SetUnitOwner(u, Player(24), true)
        
        GroupRemoveUnit(g, u)
        u=nil
    end
    
    
    
    -- ?????? ?? -
    if GetPlayerTechCount(p, FourCC('R0D1'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] + 3
        --set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] + 5
        
    end
    SetPlayerTechResearched(p, FourCC('R0D1'), 2)
     
    
    -- ?????? ????????? ?????  -
    if GetPlayerTechCount(p, FourCC('R0E1'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] + 3
        --set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] + 5
        --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] + 3
        
    end
    SetPlayerTechResearched(p, FourCC('R0E1'), 2)
     
    -- ?????? ??? ????  -
    if GetPlayerTechCount(p, FourCC('R0E0'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
        --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] + 5
        
    end
    SetPlayerTechResearched(p, FourCC('R0E0'), 2)
    
    
    
    
    
    
    --call SetPlayerTechMaxAllowed(p,'R0EA',1)
    --call SetPlayerTechResearched(p,'R0E7',1) //????????? ??
    DestroyGroup(g)
    
    
    
    --call ChangeLandUnitsNow(p,pi)
    --call ChangeMagicUnitsNow(p,pi)
    --call ChangeTechUnitsNow(p,pi)
    --call ChangeEliteUnitsNow(p,pi)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0F3'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0F4'), 1)
    
    
    SetPlayerTechMaxAllowed(p, FourCC('R0EI'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0E9'), 0)
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_CommonHome()
    gg_trg_CommonHome=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CommonHome, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_CommonHome, Condition(Trig_CommonHome_Conditions))
    TriggerAddAction(gg_trg_CommonHome, Trig_CommonHome_Actions)
end
--===========================================================================
-- Trigger: Zandalars
--===========================================================================
function Trig_Zandalars_Conditions()
    return GetResearched() == FourCC('R0F3')
end
function Trig_Zandalars_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    --set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi]
    
    --call ChangeNavyUnitsNow(p,pi)
    
    
 
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_Zandalars()
    gg_trg_Zandalars=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Zandalars, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Zandalars, Condition(Trig_Zandalars_Conditions))
    TriggerAddAction(gg_trg_Zandalars, Trig_Zandalars_Actions)
end
--===========================================================================
-- Trigger: NightBorn
--===========================================================================
function Trig_NightBorn_Conditions()
    return GetResearched() == FourCC('R0F3')
end
function Trig_NightBorn_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
    --set udg_HordeMagicPrice[pi] = udg_HordeMagicPrice[pi] - 7
    
    --call ChangeMagicUnitsNow(p,pi)
    
    
 
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_NightBorn()
    gg_trg_NightBorn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NightBorn, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NightBorn, Condition(Trig_NightBorn_Conditions))
    TriggerAddAction(gg_trg_NightBorn, Trig_NightBorn_Actions)
end
--===========================================================================
-- Trigger: StartUnitedOrcs
--===========================================================================
function Trig_StartUnitedOrcs_Conditions()
    return GetResearched() == FourCC('R0DX')
end
function Trig_StartUnitedOrcs_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D1'), 1, GetOwningPlayer(GetTriggerUnit()))
    -- -
    SetPlayerTechMaxAllowedSwap(FourCC('R0DW'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StartUnitedOrcs()
    gg_trg_StartUnitedOrcs=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartUnitedOrcs, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StartUnitedOrcs, Condition(Trig_StartUnitedOrcs_Conditions))
    TriggerAddAction(gg_trg_StartUnitedOrcs, Trig_StartUnitedOrcs_Actions)
end
--===========================================================================
-- Trigger: BlackMountainHorde
--===========================================================================
function Trig_BlackMountainHorde_Conditions()
    return GetResearched() == FourCC('R0D1')
end
function Trig_BlackMountainHorde_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    --set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] - 5
    --call ChangeLandUnitsNow(p,pi)
    
    
    
    SetPlayerTechMaxAllowed(p, FourCC('R0E1'), 1)
    
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_BlackMountainHorde()
    gg_trg_BlackMountainHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlackMountainHorde, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BlackMountainHorde, Condition(Trig_BlackMountainHorde_Conditions))
    TriggerAddAction(gg_trg_BlackMountainHorde, Trig_BlackMountainHorde_Actions)
end
--===========================================================================
-- Trigger: DragonHorde
--===========================================================================
function Trig_DragonHorde_Conditions()
    return GetResearched() == FourCC('R0E1')
end
function Trig_DragonHorde_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    --set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] - 5
    --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 3
    --call ChangeLandUnitsNow(p,pi)
    --call ChangeEliteUnitsNow(p,pi)
    
    
    
    SetPlayerTechMaxAllowed(p, FourCC('R0E0'), 1)
    
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_DragonHorde()
    gg_trg_DragonHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonHorde, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_DragonHorde, Condition(Trig_DragonHorde_Conditions))
    TriggerAddAction(gg_trg_DragonHorde, Trig_DragonHorde_Actions)
end
--===========================================================================
-- Trigger: CorCron
--===========================================================================
function Trig_CorCron_Conditions()
    return GetResearched() == FourCC('R0E0')
end
function Trig_CorCron_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 5
    --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 5
    countAll(p)
    --call ChangeEliteUnitsNow(p,pi)
    
    
    
    SetPlayerTechMaxAllowed(p, FourCC('R0E9'), 1)
    
    --Compromise
    if GetPlayerTechCount(p, FourCC('R0E0'), true) == 1 then
        SetPlayerTechMaxAllowed(p, FourCC('R0EI'), 1)
    end
    p=nil
    u=nil
    
    
end
--===========================================================================
function InitTrig_CorCron()
    gg_trg_CorCron=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CorCron, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_CorCron, Condition(Trig_CorCron_Conditions))
    TriggerAddAction(gg_trg_CorCron, Trig_CorCron_Actions)
end
--===========================================================================
-- Trigger: StartTrueHorde
--===========================================================================
function Trig_StartTrueHorde_Conditions()
    return GetResearched() == FourCC('R0E9')
end
function Trig_StartTrueHorde_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0DY'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EI'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0EH'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StartTrueHorde()
    gg_trg_StartTrueHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartTrueHorde, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_StartTrueHorde, Condition(Trig_StartTrueHorde_Conditions))
    TriggerAddAction(gg_trg_StartTrueHorde, Trig_StartTrueHorde_Actions)
end
--===========================================================================
-- Trigger: CanselTrueHorde
--===========================================================================
function Trig_CanselTrueHorde_Conditions()
    return GetResearched() == FourCC('R0E9')
end
function Trig_CanselTrueHorde_Func001C()
    return GetPlayerTechMaxAllowedSwap(FourCC('R0D3'), GetOwningPlayer(GetTriggerUnit())) == 0
end
function Trig_CanselTrueHorde_Actions()
    if Trig_CanselTrueHorde_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0DY'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanselTrueHorde()
    gg_trg_CanselTrueHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselTrueHorde, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanselTrueHorde, Condition(Trig_CanselTrueHorde_Conditions))
    TriggerAddAction(gg_trg_CanselTrueHorde, Trig_CanselTrueHorde_Actions)
end
--===========================================================================
-- Trigger: Reptaur
--===========================================================================
function Trig_Replace_Func001A()
    ReplaceUnit2(GetEnumUnit() , FourCC('O02Z') , bj_UNIT_STATE_METHOD_RELATIVE)
end
function Reptaur()
    ForGroupBJ(GetUnitsOfPlayerAndTypeId(udg_LocalPlayer, FourCC('Otch')), Trig_Replace_Func001A)
end
--===========================================================================
-- Trigger: TrueHorde
--===========================================================================
function Trig_TrueHorde_Conditions()
    return GetResearched() == FourCC('R0E9')
end
function NoNeORc()
    local id= GetUnitTypeId(GetFilterUnit())
    return id == FourCC('ospw') or id == FourCC('o026') or id == FourCC('o025') or id == FourCC('o024') or id == FourCC('o023') or id == FourCC('o01G') or id == FourCC('o01L') or id == FourCC('o01F') or id == FourCC('o01H') or id == FourCC('otbk') or id == FourCC('o02M') or id == FourCC('o02S') or id == FourCC('o02W')
end
function Trig_TrueHorde_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    local g= CreateGroup()
    udg_MainPrice[pi]=udg_MainPrice[pi] + 15
    --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 5
    countAll(p)
    --call ChangeEliteUnitsNow(p,pi)
    
    
    --End other races
    g=CreateGroup()
    udg_Boolexpr = NoNeORc
    GroupEnumUnitsOfPlayer(g, p, udg_Boolexpr)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        KillUnit(u)
        
        GroupRemoveUnit(g, u)
        u=nil
    end
    
    
    -- ?????? ???????  -
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] + 4
--    set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] + 4
--    set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] + 2
--    set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] + 2
        
    end
    SetPlayerTechResearched(p, FourCC('R0D3'), 2)
    
    -- ?????? ?????? -
    if GetPlayerTechCount(p, FourCC('R0D2'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] + 4
--        set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] + 3
--        set udg_HordeMagicPrice[pi] = udg_HordeMagicPrice[pi] + 6
--        set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] + 2
--        set udg_HordeTechPrice[pi] = udg_HordeTechPrice[pi] + 2
        
    end
    SetPlayerTechResearched(p, FourCC('R0D2'), 2)
    
    -- ?????? ??????????  -
    if GetPlayerTechCount(p, FourCC('R0E0'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] + 2
--        set udg_HordeLandPrice[pi] = udg_HordeLandPrice[pi] + 3
--        set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] + 2
        
    end
    SetPlayerTechResearched(p, FourCC('R0E0'), 2)
     
    
    SetPlayerTechMaxAllowed(p, FourCC('R0EA'), 1)
    SetPlayerTechResearched(p, FourCC('R0E7'), 1) --????????? ??
    DestroyGroup(g)
    
    SetPlayerTechMaxAllowed(p, FourCC('Otch'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('O02Z'), 1)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0KO'), 1) -- Sha
   -- call ChangeLandUnitsNow(p,pi)
    --call ChangeMagicUnitsNow(p,pi)
    --call ChangeTechUnitsNow(p,pi)
    --call ChangeEliteUnitsNow(p,pi)
    
    udg_LocalPlayer=p
    ForGroupBJ(GetUnitsOfPlayerAndTypeId(udg_LocalPlayer, FourCC('Otch')), Trig_Replace_Func001A) -- INLINED!!
    
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_TrueHorde()
    gg_trg_TrueHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrueHorde, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_TrueHorde, Condition(Trig_TrueHorde_Conditions))
    TriggerAddAction(gg_trg_TrueHorde, Trig_TrueHorde_Actions)
end
--===========================================================================
-- Trigger: IronHorde
--===========================================================================
function Trig_IronHorde_Conditions()
    return GetResearched() == FourCC('R0EA')
end
function Trig_IronHorde_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 6
--    set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 8
--    set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] - 3
 --   call ChangeEliteUnitsNow(p,pi)
   -- call ChangeNavyUnitsNow(p,pi)
    
    --Old units
    SetPlayerTechMaxAllowed(p, FourCC('ogru'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('ohun'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('o01N'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('o01P'), 0)
    --New units
    SetPlayerTechMaxAllowed(p, FourCC('o029'), - 1)
    SetPlayerTechMaxAllowed(p, FourCC('o02B'), - 1)
    SetPlayerTechMaxAllowed(p, FourCC('h0CY'), - 1)
    
    
   
    
    
    --call SetPlayerTechMaxAllowed(p,'R0E9',1)
    
    
    
    
    
    
    p=nil
    u=nil
    
end
--===========================================================================
function InitTrig_IronHorde()
    gg_trg_IronHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_IronHorde, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_IronHorde, Condition(Trig_IronHorde_Conditions))
    TriggerAddAction(gg_trg_IronHorde, Trig_IronHorde_Actions)
end
--===========================================================================
-- Trigger: IronHordeBegin
--===========================================================================
function Trig_IronHordeBegin_Conditions()
    return GetResearched() == FourCC('R0EA')
end
function Trig_IronHordeBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0KO'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_IronHordeBegin()
    gg_trg_IronHordeBegin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_IronHordeBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_IronHordeBegin, Condition(Trig_IronHordeBegin_Conditions))
    TriggerAddAction(gg_trg_IronHordeBegin, Trig_IronHordeBegin_Actions)
end
--===========================================================================
-- Trigger: ShaHorde
--===========================================================================
function Trig_ShaHorde_Conditions()
    return GetResearched() == FourCC('R0KO')
end
function Trig_ShaHorde_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    SetPlayerAbilityAvailable(p, FourCC('A1OJ'), true) -- ?? ??????
    SetPlayerAbilityAvailable(p, FourCC('A1OK'), true) -- ?? ??????
    
    
end
--===========================================================================
function InitTrig_ShaHorde()
    gg_trg_ShaHorde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShaHorde, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_ShaHorde, Condition(Trig_ShaHorde_Conditions))
    TriggerAddAction(gg_trg_ShaHorde, Trig_ShaHorde_Actions)
end
--===========================================================================
-- Trigger: ShaSpell
--===========================================================================
function Trig_ShaSpell_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A1OJ')) > 0 and GetPlayerTechCount(GetOwningPlayer(GetAttacker()), FourCC('R0KO'), true) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker()))
end
function Trig_ShaSpell_Actions()
    if Random(1 , 100) then
        CreateUnit(GetOwningPlayer(GetAttacker()), FourCC('n04J'), GetUnitX(GetAttacker()), GetUnitY(GetAttacker()), 0.0)
    end
    
end
--===========================================================================
function InitTrig_ShaSpell()
    gg_trg_ShaSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShaSpell, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_ShaSpell, Condition(Trig_ShaSpell_Conditions))
    TriggerAddAction(gg_trg_ShaSpell, Trig_ShaSpell_Actions)
end
--===========================================================================
-- Trigger: ShaHordeBegin
--===========================================================================
function Trig_ShaHordeBegin_Conditions()
    return GetResearched() == FourCC('R0KO')
end
function Trig_ShaHordeBegin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0EA'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_ShaHordeBegin()
    gg_trg_ShaHordeBegin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShaHordeBegin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_ShaHordeBegin, Condition(Trig_ShaHordeBegin_Conditions))
    TriggerAddAction(gg_trg_ShaHordeBegin, Trig_ShaHordeBegin_Actions)
end
--===========================================================================
-- Trigger: StartNeutrals
--===========================================================================
function Trig_StartNeutrals_Conditions()
    return GetResearched() == FourCC('R0DZ')
end
function Trig_StartNeutrals_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0E4'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0E5'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0E3'), 1, GetOwningPlayer(GetTriggerUnit()))
    -- -
    SetPlayerTechMaxAllowedSwap(FourCC('R0DW'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_StartNeutrals()
    gg_trg_StartNeutrals=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartNeutrals, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StartNeutrals, Condition(Trig_StartNeutrals_Conditions))
    TriggerAddAction(gg_trg_StartNeutrals, Trig_StartNeutrals_Actions)
end
--===========================================================================
-- Trigger: BuyGoblins
--===========================================================================
function Trig_BuyGoblins_Conditions()
    return GetResearched() == FourCC('R0E4')
end
function Trig_BuyGoblins_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 2
    --set udg_HordeTechPrice[pi] = udg_HordeTechPrice[pi] - 7
    --set udg_HordeNavyPrice[pi] = udg_HordeNavyPrice[pi] - 3
    
    --call ChangeTechUnitsNow(p,pi)
    --call ChangeNavyUnitsNow(p,pi)
    
    SetPlayerTechResearched(p, FourCC('R0E8'), 1) -- ????????? ?????? ???????
   
end
--===========================================================================
function InitTrig_BuyGoblins()
    gg_trg_BuyGoblins=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuyGoblins, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BuyGoblins, Condition(Trig_BuyGoblins_Conditions))
    TriggerAddAction(gg_trg_BuyGoblins, Trig_BuyGoblins_Actions)
end
--===========================================================================
-- Trigger: Magnatavrs
--===========================================================================
function Trig_Magnatavrs_Conditions()
    return GetResearched() == FourCC('R0E4')
end
function Trig_Magnatavrs_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_HordeLandPrice[pi]=udg_HordeLandPrice[pi] + 1
    --call ChangeLandUnitsNow(p,pi)
    
    u=nil
end
--===========================================================================
function InitTrig_Magnatavrs()
    gg_trg_Magnatavrs=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Magnatavrs, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Magnatavrs, Condition(Trig_Magnatavrs_Conditions))
    TriggerAddAction(gg_trg_Magnatavrs, Trig_Magnatavrs_Actions)
end
--===========================================================================
-- Trigger: DeathKnights
--===========================================================================
function Trig_DeathKnights_Conditions()
    return GetResearched() == FourCC('R0E3')
end
function Trig_DeathKnights_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    countAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 2
    --set udg_HordeElitePrice[pi] = udg_HordeElitePrice[pi] - 4
    --call ChangeEliteUnitsNow(p,pi)
    
    u=nil
end
--===========================================================================
function InitTrig_DeathKnights()
    gg_trg_DeathKnights=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeathKnights, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_DeathKnights, Condition(Trig_DeathKnights_Conditions))
    TriggerAddAction(gg_trg_DeathKnights, Trig_DeathKnights_Actions)
end
--===========================================================================
-- Trigger: Compromise
--===========================================================================
function Trig_Compromise_Conditions()
    return GetResearched() == FourCC('R0EI')
end
function Trig_Compromise_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    local g= CreateGroup()
    udg_MainPrice[pi]=udg_MainPrice[pi] - 9
    
    
    --???????? ?????? ?????
    SetPlayerTechMaxAllowed(p, FourCC('R0EH'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0E9'), 0)
    
end
--===========================================================================
function InitTrig_Compromise()
    gg_trg_Compromise=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Compromise, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Compromise, Condition(Trig_Compromise_Conditions))
    TriggerAddAction(gg_trg_Compromise, Trig_Compromise_Actions)
end
--===========================================================================
-- Trigger: BerserkOrc
--===========================================================================
function Trig_BerserkOrc_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0ZA')) >= 1 and Random(1 , 25)
end
function Trig_BerserkOrc_Actions()
    DummyCastTarget(FourCC('A1MG') , "bloodlust" , GetAttacker() , GetAttacker())
end
--===========================================================================
function InitTrig_BerserkOrc()
    gg_trg_BerserkOrc=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BerserkOrc, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_BerserkOrc, Condition(Trig_BerserkOrc_Conditions))
    TriggerAddAction(gg_trg_BerserkOrc, Trig_BerserkOrc_Actions)
end
--===========================================================================
-- Trigger: BerserkTrol
--===========================================================================
function Trig_BerserkTrol_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0ZC')) == 1 and Random(1 , 10)
end
function Trig_BerserkTrol_Actions()
    local u
    local s
    u=GetAttacker()
    s=gg_snd_BerserkerCaster
    UnitAddAbility(u, FourCC('A13H'))
    UnitAddAbility(u, FourCC('A13I'))
    UnitAddAbility(u, FourCC('Bbsk'))
    
    AttachSoundToUnit(s, u)
    SetSoundVolume(s, 127)
    StartSound(s)
    RemoveAbilityTimed(u , FourCC('A13H') , 9)
    RemoveAbilityTimed(u , FourCC('A13I') , 9)
    RemoveAbilityTimed(u , FourCC('Bbsk') , 9)
        
    u=nil
    s=nil
end
--===========================================================================
function InitTrig_BerserkTrol()
    gg_trg_BerserkTrol=CreateTrigger()
    --call DisableTrigger( gg_trg_BerserkTrol )
    TriggerRegisterAnyUnitEventBJ(gg_trg_BerserkTrol, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_BerserkTrol, Condition(Trig_BerserkTrol_Conditions))
    TriggerAddAction(gg_trg_BerserkTrol, Trig_BerserkTrol_Actions)
end
--===========================================================================
-- Trigger: AutoSetkaH
--===========================================================================
function Trig_AutoSetkaH_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoSetkaH()
    gg_trg_AutoSetkaH=CreateTrigger()
    DisableTrigger(gg_trg_AutoSetkaH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoSetkaH, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoSetkaH, function()
        if GetSpellAbilityId() ~= FourCC('A0ZB') then return end
        Trig_AutoSetkaH_Actions()
    end)
end
--===========================================================================
-- Trigger: IronStar
--===========================================================================
function Trig_IronStar_Actions()
    UnitApplyTimedLifeBJ(10.00, FourCC('BTLF'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_IronStar()
    gg_trg_IronStar=CreateTrigger()
    DisableTrigger(gg_trg_IronStar)
    TriggerRegisterAnyUnitEventBJ(gg_trg_IronStar, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_IronStar, function()
        if GetSpellAbilityId() ~= FourCC('A103') then return end
        Trig_IronStar_Actions()
    end)
end
--===========================================================================
-- Trigger: AutoShield2
--===========================================================================
function Trig_AutoShield2_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "antimagicshell", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_AutoShield2()
    gg_trg_AutoShield2=CreateTrigger()
    DisableTrigger(gg_trg_AutoShield2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutoShield2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AutoShield2, function()
        if GetSpellAbilityId() ~= FourCC('A124') then return end
        Trig_AutoShield2_Actions()
    end)
end
--===========================================================================
-- Trigger: PandaSecondAttack
--===========================================================================
function Trig_PandaSecondAttack_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A129'), GetAttacker()) > 0
end
function Trig_PandaSecondAttack_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A12A'), GetAttacker()) == 0
end
function Trig_PandaSecondAttack_Actions()
    if Trig_PandaSecondAttack_Func001C() then
        UnitAddAbilityBJ(FourCC('A12A'), GetAttacker())
    else
        UnitRemoveAbilityBJ(FourCC('A12A'), GetAttacker())
    end
end
--===========================================================================
function InitTrig_PandaSecondAttack()
    gg_trg_PandaSecondAttack=CreateTrigger()
    DisableTrigger(gg_trg_PandaSecondAttack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PandaSecondAttack, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_PandaSecondAttack, Condition(Trig_PandaSecondAttack_Conditions))
    TriggerAddAction(gg_trg_PandaSecondAttack, Trig_PandaSecondAttack_Actions)
end
--===========================================================================
-- Trigger: DragonFire
--===========================================================================
function Trig_DragonFire_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A0ZX')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker())) and Random(8 , 100)
end
function Trig_DragonFire_Actions()
    IssueTargetOrder(GetAttacker(), "breathoffire", GetTriggerUnit())
end
--===========================================================================
function InitTrig_DragonFire()
    gg_trg_DragonFire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonFire, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_DragonFire, Condition(Trig_DragonFire_Conditions))
    TriggerAddAction(gg_trg_DragonFire, Trig_DragonFire_Actions)
end
--===========================================================================
-- Trigger: ThrallMolnya
--===========================================================================
function Thrallenum()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('A14V'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('A14V'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A12X'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "chainlightning", GetEnumUnit())
end
function Trig_ThrallMolnya_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    udg_Boolexpr = EnemEl
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 400, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Thrallenum)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_ThrallMolnya()
    gg_trg_ThrallMolnya=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ThrallMolnya, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ThrallMolnya, function()
        if GetSpellAbilityId() ~= FourCC('A12X') then return end
        Trig_ThrallMolnya_Actions()
    end)
end
--===========================================================================
-- Trigger: Okovi
--===========================================================================
function Trig_Okovi_Func002002()
    return 0 == 0
end
function Trig_Okovi_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('A12Y'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('A12Y'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A12Z'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "firebolt", GetEnumUnit())
end
function Trig_Okovi_Actions()
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_Boolexpr = Trig_Okovi_Func002002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 225, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_Okovi_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_Okovi()
    gg_trg_Okovi=CreateTrigger()
    DisableTrigger(gg_trg_Okovi)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Okovi, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Okovi, function()
        if GetSpellAbilityId() ~= FourCC('A12Z') then return end
        Trig_Okovi_Actions()
    end)
end
--===========================================================================
-- Trigger: GarraoshMassBloodlast
--===========================================================================
function Trig_GarraoshMassBloodlast_Func002002()
    return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer
end
function Trig_GarraoshMassBloodlast_Func007A()
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    udg_LocalUnit2=GetLastCreatedUnit()
    TriggerExecute(gg_trg_ToKill2)
    UnitAddAbilityBJ(FourCC('A12L'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('A12L'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A12M'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "bloodlust", GetEnumUnit())
end
function Trig_GarraoshMassBloodlast_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    udg_Boolexpr = Trig_GarraoshMassBloodlast_Func002002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 500, udg_Boolexpr)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    ForGroupBJ(udg_LocalOtrad2, Trig_GarraoshMassBloodlast_Func007A)
    RemoveLocation(udg_LocalPosition2)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_GarraoshMassBloodlast()
    gg_trg_GarraoshMassBloodlast=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GarraoshMassBloodlast, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GarraoshMassBloodlast, function()
        if GetSpellAbilityId() ~= FourCC('A12M') then return end
        Trig_GarraoshMassBloodlast_Actions()
    end)
end
--===========================================================================
-- Trigger: StartHorde
--===========================================================================
function HordeStartLimits()
    SetPlayerTechMaxAllowedSwap(FourCC('Oshd'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Otch'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Ofar'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Obla'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O02P'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Othr'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o029'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o02B'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0CY'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0D1'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0D2'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0D3'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E0'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E1'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E3'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E5'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0E9'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0EA'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0EE'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0EI'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0EH'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0F4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0F3'), 0, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('R0F3'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0KO'), 0, GetEnumPlayer()) -- Sha
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A1LO'), false)
    
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A1OJ'), false) -- ?? ??????
    SetPlayerAbilityAvailable(GetEnumPlayer(), FourCC('A1OK'), false) -- ?? ?????? ????
    countAll(GetEnumPlayer())
end
function Trig_StartHorde_Actions()
    ForForce(udg_AllPlayers, HordeStartLimits)
    ForForce(udg_Bots, HordeStartLimits)
end
--===========================================================================
function InitTrig_StartHorde()
