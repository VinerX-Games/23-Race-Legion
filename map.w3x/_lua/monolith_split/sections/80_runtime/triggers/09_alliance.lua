    gg_trg_TrainHakkar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainHakkar, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainHakkar, Condition(Trig_TrainHakkar_Conditions))
    TriggerAddAction(gg_trg_TrainHakkar, Trig_TrainHakkar_Actions)
end
--===========================================================================
-- Trigger: AllyOn
--===========================================================================
function Trig_AllyOn_Actions()
    
    EnableTrigger(gg_trg_AK1T1)
    
    
    EnableTrigger(gg_trg_Vozd)
    EnableTrigger(gg_trg_Heal)
    EnableTrigger(gg_trg_Defend)
    EnableTrigger(gg_trg_PaladinHpSpell)
    EnableTrigger(gg_trg_PaladinHpSpell2)
    EnableTrigger(gg_trg_MagicUsk)
    
    
    
    
    
    EnableTrigger(gg_trg_SandStrikeAlliance)
    EnableTrigger(gg_trg_Level2)
    EnableTrigger(gg_trg_VariarDamager)
    EnableTrigger(gg_trg_VariarTitan)
    EnableTrigger(gg_trg_VariarTaunt)
    EnableTrigger(gg_trg_MassMolot)
    EnableTrigger(gg_trg_Illusions)
    EnableTrigger(gg_trg_MagicUsk)
    EnableTrigger(gg_trg_WorgenSpell)
    EnableTrigger(gg_trg_HolyHelp)
    EnableTrigger(gg_trg_Kristall2)
    EnableTrigger(gg_trg_TankFire)
    
    EnableTrigger(gg_trg_VarianCharge)
    
    
    
    
    
    
    
    
    
    
--    call EnableTrigger( gg_trg_K1T2 )
--    call EnableTrigger( gg_trg_K1T2b )
--    call EnableTrigger( gg_trg_K1TCav )
--    call EnableTrigger( gg_trg_K1T4)
--    
--    call EnableTrigger( gg_trg_K2T1 )
--    call EnableTrigger( gg_trg_K2T2 )
--    call EnableTrigger( gg_trg_K2T2b )
--    call EnableTrigger( gg_trg_K2T3)
--
--
--    call EnableTrigger( gg_trg_KM1 )
--    call EnableTrigger( gg_trg_KM2 )
--    call EnableTrigger( gg_trg_KM3 )
--
--    call EnableTrigger( gg_trg_TechT1 )
--    call EnableTrigger( gg_trg_TechT2 )
--   
--    call EnableTrigger( gg_trg_NavyHeavy )
--    call EnableTrigger( gg_trg_NavyLight )
    
    
end
--===========================================================================
function InitTrig_AllyOn()
    gg_trg_AllyOn=CreateTrigger()
    TriggerAddAction(gg_trg_AllyOn, Trig_AllyOn_Actions)
end
--===========================================================================
-- Trigger: AK1T1
--===========================================================================
function Trig_AK1T1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hfoo')
end
function AT1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    -- ????????? ???????
    
    if GetPlayerTechCount(p, FourCC('R0H6'), true) < 1 then
        i=4
        --Stormwind common
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KD')
                b=b + 1
                if b >= i then break end
        end
    else
        --Stromwind blue
        i=4
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0LW')
                b=b + 1
                if b >= i then break end
        end
    
    end
    
    --??????????
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        i=1
        b=1
        
        -- ?????????? ???????????
        if GetPlayerTechCount(p, FourCC('R0HV'), true) > 1 then
            i=i + 2
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KR')
            
            b=b + 1
            if b >= i then break end
        end
    end
    --Stromgarge
    if GetPlayerTechCount(p, FourCC('R0HJ'), true) > 0 then
        i=3
        b=1
        
      
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M9')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["AT1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AT1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK1T1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AT1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AT1" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK1T1()
    gg_trg_AK1T1=CreateTrigger()
    --call DisableTrigger(gg_trg_AK1T1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK1T1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK1T1, Condition(Trig_AK1T1_Conditions))
    TriggerAddAction(gg_trg_AK1T1, Trig_AK1T1_Actions)
end
--===========================================================================
-- Trigger: AK1T2
--===========================================================================
function Trig_AK1T2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0K4')
end
function AT2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ????????? ???????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KC')
            b=b + 1
            if b >= i then break end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0HB'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Pandaren
        i=1
        b=1
        --
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 2
        
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o042')
            
            b=b + 1
            if b >= i then break end
        end
        
        
    end
    
    --Long Containment
    CommonHash[pi]["AT2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AT2" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK1T2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AT2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AT2" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK1T2()
    gg_trg_AK1T2=CreateTrigger()
    --call DisableTrigger(gg_trg_AK1T2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK1T2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK1T2, Condition(Trig_AK1T2_Conditions))
    TriggerAddAction(gg_trg_AK1T2, Trig_AK1T2_Actions)
end
--===========================================================================
-- Trigger: AK1T3
--===========================================================================
function Trig_AK1T3_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0K7')
end
function AT3Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ????????? ???????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KG')
            b=b + 1
            if b >= i then break end
    end
--    
    
    
    -- ??????? ??????
    if GetPlayerTechCount(p, FourCC('R0H7'), true) == 1 then
        i=2
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KF')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
        -- ??????? 2 ?????
    if GetPlayerTechCount(p, FourCC('R0HN'), true) == 1 then
        i=1
        b=2
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0OW')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HB'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Pandaren
        i=1
        b=1
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 1
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o043')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0H8'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Dranay
        i=1
        b=1
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 1
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KX')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    
    if GetPlayerTechCount(p, FourCC('R0H9'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Worgen
        i=1
        b=1
        --??????????
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 1
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M2')
            
            b=b + 1
            if b >= i then break end
        end
    end
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AT3_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AT3" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK1T3_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AT3_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AT3" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK1T3()
    gg_trg_AK1T3=CreateTrigger()
    --call DisableTrigger(gg_trg_AK1T3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK1T3, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK1T3, Condition(Trig_AK1T3_Conditions))
    TriggerAddAction(gg_trg_AK1T3, Trig_AK1T3_Actions)
end
--===========================================================================
-- Trigger: AK1Cav
--===========================================================================
function Trig_AK1Cav_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hkni')
end
function ACavCount(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ????????? ???????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KH')
            b=b + 1
            if b >= i then break end
    end
    
    if GetPlayerTechCount(p, FourCC('R0H6'), true) > 0 then
        -- ????????? ??????
        b=1
        i=3
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KE')
                b=b + 1
                if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --??????????
        i=1
        b=1
        
        if GetPlayerTechCount(p, FourCC('R0HV'), true) > 1 then
            i=i + 2
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KW')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0HJ'), true) > 0 then
        -- ????????? ??????
        b=1
        i=3
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0MA')
                b=b + 1
                if b >= i then break end
        end
    end
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["ACav_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["ACav" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK1Cav_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["ACav_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["ACav" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK1Cav()
    gg_trg_AK1Cav=CreateTrigger()
    --call DisableTrigger(gg_trg_AK1Cav)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK1Cav, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK1Cav, Condition(Trig_AK1Cav_Conditions))
    TriggerAddAction(gg_trg_AK1Cav, Trig_AK1Cav_Actions)
end
--===========================================================================
-- Trigger: AK2T1
--===========================================================================
function Trig_AK2T1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hrif')
end
function AK1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- Human
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KA')
            b=b + 1
            if b >= i then break end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --High elf
        i=1
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0L2')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0H5'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Night elf
        i=1
        b=1
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 2
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KN')
            
            b=b + 1
            if b >= i then break end
        end
    end
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AK1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AK1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK2T1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AK1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AK1" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK2T1()
    gg_trg_AK2T1=CreateTrigger()
    --call DisableTrigger(gg_trg_AK2T1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK2T1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK2T1, Condition(Trig_AK2T1_Conditions))
    TriggerAddAction(gg_trg_AK2T1, Trig_AK2T1_Actions)
end
--===========================================================================
-- Trigger: AK2T2
--===========================================================================
function Trig_AK2T2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0K5')
end
function AK2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        -- Dwarf
        
        i=4
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 2
        end
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KO')
                b=b + 1
                if b >= i then break end
        end
    end
    
    -- Human
    i=1
    b=1
    --?????????? ????????
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 2
        end
    while true do
        a[0]=a[0] + 1
        a[a[0]]=FourCC('h0KB')
        
        b=b + 1
        if b >= i then break end
    end
    
    --??????
    if GetPlayerTechCount(p, FourCC('R0H9'), true) == 1 and GetPlayerTechCount(p, FourCC('R0EH'), true) < 1 then
        i=3
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M3')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AK2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AK2" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK2T2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AK2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AK2" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK2T2()
    gg_trg_AK2T2=CreateTrigger()
    --call DisableTrigger(gg_trg_AK2T2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK2T2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK2T2, Condition(Trig_AK2T2_Conditions))
    TriggerAddAction(gg_trg_AK2T2, Trig_AK2T2_Actions)
end
--===========================================================================
-- Trigger: AK2T3
--===========================================================================
function Trig_AK2T3_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0K6')
end
function AK3Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ????????? ???????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0K9')
            b=b + 1
            if b >= i then break end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --??????????
        i=1
        b=1
        
        -- ?????????? ???????????
        if GetPlayerTechCount(p, FourCC('R0HV'), true) > 1 then
            i=i + 2
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KK')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0H5'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Night elf
        i=1
        b=1
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 3
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0LZ')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0H9'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Kultiras 
        i=1
        b=1
        --?????????? ????????
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 1
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M7')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AK3_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AK3" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AK2T3_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AK3_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AK3" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AK2T3()
    gg_trg_AK2T3=CreateTrigger()
    --call DisableTrigger(gg_trg_AK2T3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AK2T3, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AK2T3, Condition(Trig_AK2T3_Conditions))
    TriggerAddAction(gg_trg_AK2T3, Trig_AK2T3_Actions)
end
--===========================================================================
-- Trigger: AM1
--===========================================================================
function Trig_AM1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hmpr')
end
function AM1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        -- High elf
        
        i=2
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KU')
                b=b + 1
                if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --High eldf sorc
        b=0
        i=2
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KV')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --High eldf sorc
        b=0
        i=2
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KY')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    --Human
    i=1
    b=1
    --?????????? ????????
    if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
        i=i + 1
    end
    
    while true do
        a[0]=a[0] + 1
        a[a[0]]=FourCC('h0KL')
        
        b=b + 1
        if b >= i then break end
    end
    
    -- Light
    if GetPlayerTechCount(p, FourCC('R0HK'), true) > 0 then
        
        b=0
        i=3
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0MB')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AM1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AM1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AM1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AM1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AM1" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AM1()
    gg_trg_AM1=CreateTrigger()
    --call DisableTrigger(gg_trg_AM1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AM1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AM1, Condition(Trig_AM1_Conditions))
    TriggerAddAction(gg_trg_AM1, Trig_AM1_Actions)
end
--===========================================================================
-- Trigger: AM2
--===========================================================================
function Trig_AM2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hsor')
end
function AM2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- Human
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KM')
            b=b + 1
            if b >= i then break end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0H5'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Night elf
        i=1
        b=1
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 1
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KT')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0HD'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Kultiras
        i=1
        b=1
        --Arathor
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 1
        end
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M5')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    -- Void
    if GetPlayerTechCount(p, FourCC('R0HL'), true) > 0 then
        
        b=0
        i=3
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0MC')
            
            b=b + 1
            if b >= i then break end
        end
    end
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AM2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AM2" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AM2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AM2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AM2" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AM2()
    gg_trg_AM2=CreateTrigger()
    --call DisableTrigger(gg_trg_AM2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AM2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AM2, Condition(Trig_AM2_Conditions))
    TriggerAddAction(gg_trg_AM2, Trig_AM2_Actions)
end
--===========================================================================
-- Trigger: AM3
--===========================================================================
function Trig_AM3_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hspt')
end
function AM3Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    
    -- ???
    if GetPlayerTechCount(p, FourCC('R0HA'), true) >= 1 then
        
        i=4
        b=0
        
        
        --?????????? ????????
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 1
        end
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0LU')
                b=b + 1
                if b >= i then break end
        end
        
    end
    
    if GetPlayerTechCount(p, FourCC('R0H8'), true) == 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        --Dranay
        i=1
        b=1
        -- ????? ?????
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 2
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0KQ')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    if GetPlayerTechCount(p, FourCC('R0HI'), true) == 1 then
        --Dalaran
        i=3
        b=0
        --?????????? ????????
        if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
            i=i + 2
        end
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M8')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    --Long Containment
    CommonHash[pi]["AM3_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AM3" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AM3_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AM3_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AM3" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AM3()
    gg_trg_AM3=CreateTrigger()
    --call DisableTrigger(gg_trg_AM3)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AM3, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AM3, Condition(Trig_AM3_Conditions))
    TriggerAddAction(gg_trg_AM3, Trig_AM3_Actions)
end
--===========================================================================
-- Trigger: AE1
--===========================================================================
function Trig_AE1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hmtm')
end
function AE1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        -- Dwarf
        a[0]=0
        i=4
        if GetPlayerTechCount(p, FourCC('R0HE'), true) + GetPlayerTechCount(p, FourCC('R0HF'), true) > 0 then
            i=i + 1
        
        end
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KZ')
                b=b + 1
                if b >= i then break end
        end
    end
    --Cannon
    i=1
    b=1
    --?????????? ????????
    if GetPlayerTechCount(p, FourCC('R0HG'), true) > 0 then
        i=i + 3
    end
    while true do
        a[0]=a[0] + 1
        a[a[0]]=FourCC('h0KP')
        
        b=b + 1
        if b >= i then break end
    end
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AE1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AE1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AE1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AE1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AE1" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    UnitAddAbility(u, FourCC('A17P'))
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AE1()
    gg_trg_AE1=CreateTrigger()
    --call DisableTrigger(gg_trg_AE1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AE1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AE1, Condition(Trig_AE1_Conditions))
    TriggerAddAction(gg_trg_AE1, Trig_AE1_Actions)
end
--===========================================================================
-- Trigger: AE2
--===========================================================================
function Trig_AE2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('hmtt')
end
function AE2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    a[0]=0
    if GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        
        if GetPlayerTechCount(p, FourCC('R0HE'), true) > 0 then
            --New tank
            i=2
            while true do
                    a[0]=a[0] + 1
                    a[a[0]]=FourCC('h0KJ')
                    b=b + 1
                    if b >= i then break end
            end
        end
        
        -- Main Tank
        i=4
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0KS')
                b=b + 1
                if b >= i then break end
        end
    else
        -- Old Tank
        
        i=4
        while true do
                a[0]=a[0] + 1
                a[a[0]]=FourCC('h0LY')
                b=b + 1
                if b >= i then break end
        end
    
    end
    
    
    -- Black Iron
    if GetPlayerTechCount(p, FourCC('R0HM'), true) > 0 then
        
        b=0
        i=3
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('o044')
            
            b=b + 1
            if b >= i then break end
        end
    end
--    //??????????
--    set i = 1 
--    set b = 1
--    
--    loop
--        set a[0] = a[0] + 1
--        set a[ a[0] ] = 'h0KR'
--        
--        set b = b + 1
--        exitwhen b >= i
--    endloop
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AEE2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AEE2" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AE2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AEE2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AEE2" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    --call UnitAddAbility(u,'A17P')
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AE2()
    gg_trg_AE2=CreateTrigger()
    --call DisableTrigger(gg_trg_AE2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AE2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AE2, Condition(Trig_AE2_Conditions))
    TriggerAddAction(gg_trg_AE2, Trig_AE2_Actions)
end
--===========================================================================
-- Trigger: AN1
--===========================================================================
function Trig_AN1_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0L0')
end
function AN1Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ?????? ?????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h00Y')
            b=b + 1
            if b >= i then break end
    end
    
    
    -- ??????? ?????????
    if GetPlayerTechCount(p, FourCC('R0HD'), true) >= 1 and GetPlayerTechCount(p, FourCC('R0HH'), true) < 1 then
        i=3
        b=1
        
        while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h0M6')
            
            b=b + 1
            if b >= i then break end
        end
    end
    
    
    
    
--    
--    //??????????
--    set i = 1 
--    set b = 1
--    
--    loop
--        set a[0] = a[0] + 1
--        set a[ a[0] ] = 'h0KR'
--        
--        set b = b + 1
--        exitwhen b >= i
--    endloop
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AN1_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AN1" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AN1_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AN1_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AN1" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AN1()
    gg_trg_AN1=CreateTrigger()
    --call DisableTrigger(gg_trg_AN1)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AN1, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AN1, Condition(Trig_AN1_Conditions))
    TriggerAddAction(gg_trg_AN1, Trig_AN1_Actions)
end
--===========================================================================
-- Trigger: AN2
--===========================================================================
function Trig_AN2_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0L1')
end
function AN2Count(p)
    local a = {}
    local i= 0
    local b= 0
    local pi= GetPlayerId(p)
    
    -- ?????? ???????
    a[0]=0
    i=4
    while true do
            a[0]=a[0] + 1
            a[a[0]]=FourCC('h00Z')
            b=b + 1
            if b >= i then break end
    end
    
--    //??????????
--    set i = 1 
--    set b = 1
--    
--    loop
--        set a[0] = a[0] + 1
--        set a[ a[0] ] = 'h0KR'
--        
--        set b = b + 1
--        exitwhen b >= i
--    endloop
    
    
--    
--    //2 ???? ?????? ????
--    if GetPlayerTechCount(p,'R0D1',true) == 1  and GetPlayerTechCount(p,'R0EH',true)<1  then
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
--    //3 ???? - ?????
--    if GetPlayerTechCount(p,'R0D2',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 1 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01F'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--
--    endif
--    //4 ???? ??????
--    if GetPlayerTechCount(p,'R0D3',true) == 1 and GetPlayerTechCount(p,'R0E9',true) != 1 then
--        set i = 2 
--        set b = 1
--        
--        loop
--            set a[0] = a[0] + 1
--            set a[ a[0] ] = 'o01H'
--            
--            set b = b + 1
--            exitwhen b >= i
--        endloop
--    endif
    
    --Long Containment
    CommonHash[pi]["AN2_0"] = a[0]
    i=1
    while true do
        
        
        CommonHash[pi]["AN2" .. i] = a[i]
        i=i + 1
        
        if i > a[0] then break end
    end
    
    
    
    
end
function Trig_AN2_Actions()
    local a = {}
    local i= 0
    local b= 0
    local p= GetOwningPlayer(GetTriggerUnit())
    local l= GetUnitRallyPoint(GetTriggerUnit())
    local u
    local pi= GetPlayerId(p)
    
    
    i=(CommonHash[pi]["AN2_0"] or 0)
    i=GetRandomInt(1, i)
    b=(CommonHash[pi]["AN2" .. i] or 0)
    
    u=ReplaceUnit(GetTrainedUnit() , b , bj_UNIT_STATE_METHOD_RELATIVE)
    
   
    --call UnitAddAbility(u,'OR00')
    --call SetUnitAbilityLevel(u,'OR00',35+udg_HordeLandPrice[pi])
    
    
     
    
    IssuePointOrderLoc(u, "attack", l)
    RemoveLocation(l)
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_AN2()
    gg_trg_AN2=CreateTrigger()
    --call DisableTrigger(gg_trg_AN2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_AN2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_AN2, Condition(Trig_AN2_Conditions))
    TriggerAddAction(gg_trg_AN2, Trig_AN2_Actions)
end
--===========================================================================
-- Trigger: ACounters
--===========================================================================
function AcountAll(p)
    AT1Count(p)
    AT2Count(p)
    ACavCount(p)
    AT3Count(p)
    
    AK1Count(p)
    AK2Count(p)
    AK3Count(p)
    
    AM1Count(p)
    AM2Count(p)
    AM3Count(p)
    
    AE1Count(p)
    AE2Count(p)
    
    AN1Count(p)
    AN2Count(p)
end
--===========================================================================
-- Trigger: OldAllianceForever
--===========================================================================
function Trig_OldAllianceForever_Conditions()
    return GetResearched() == FourCC('R0DW')
end
function Trig_OldAllianceForever_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 15
    
    --???????? ?????
    SetPlayerTechMaxAllowed(p, FourCC('R0HS'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HR'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HQ'), 0)
end
--===========================================================================
function InitTrig_OldAllianceForever()
    gg_trg_OldAllianceForever=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OldAllianceForever, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_OldAllianceForever, Condition(Trig_OldAllianceForever_Conditions))
    TriggerAddAction(gg_trg_OldAllianceForever, Trig_OldAllianceForever_Actions)
end
--===========================================================================
-- Trigger: BegEvery
--===========================================================================
function Trig_BegEvery_Func001C()
    if ( ( GetResearched() == FourCC('R0HS') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R0HR') ) ) then
        return true
    end
    if ( ( GetResearched() == FourCC('R0HQ') ) ) then
        return true
    end
    return false
end
function Trig_BegEvery_Conditions()
    return Trig_BegEvery_Func001C()
end
function Trig_BegEvery_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GX'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegEvery()
    gg_trg_BegEvery=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegEvery, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegEvery, Condition(Trig_BegEvery_Conditions))
    TriggerAddAction(gg_trg_BegEvery, Trig_BegEvery_Actions)
end
--===========================================================================
-- Trigger: CanEvery
--===========================================================================
function Trig_CanEvery_Func001Func001C()
    return (( GetResearched() == FourCC('R0HS') )) and (( GetPlayerTechCountSimple(FourCC('R0HR'), GetOwningPlayer(GetTriggerUnit())) == 0 )) and (( GetPlayerTechCountSimple(FourCC('R0HQ'), GetOwningPlayer(GetTriggerUnit())) == 0 ))
end
function Trig_CanEvery_Func001Func002C()
    return (( GetResearched() == FourCC('R0HR') )) and (( GetPlayerTechCountSimple(FourCC('R0HS'), GetOwningPlayer(GetTriggerUnit())) == 0 )) and (( GetPlayerTechCountSimple(FourCC('R0HQ'), GetOwningPlayer(GetTriggerUnit())) == 0 ))
end
function Trig_CanEvery_Func001Func003C()
    return (( GetResearched() == FourCC('R0HQ') )) and (( GetPlayerTechCountSimple(FourCC('R0HS'), GetOwningPlayer(GetTriggerUnit())) == 0 )) and (( GetPlayerTechCountSimple(FourCC('R0HR'), GetOwningPlayer(GetTriggerUnit())) == 0 ))
end
function Trig_CanEvery_Func001C()
    if ( Trig_CanEvery_Func001Func001C() ) then
        return true
    end
    if ( Trig_CanEvery_Func001Func002C() ) then
        return true
    end
    if ( Trig_CanEvery_Func001Func003C() ) then
        return true
    end
    return false
end
function Trig_CanEvery_Conditions()
    return Trig_CanEvery_Func001C()
end
function Trig_CanEvery_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GX'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanEvery()
    gg_trg_CanEvery=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanEvery, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanEvery, Condition(Trig_CanEvery_Conditions))
    TriggerAddAction(gg_trg_CanEvery, Trig_CanEvery_Actions)
end
--===========================================================================
-- Trigger: BegForever
--===========================================================================
function Trig_BegForever_Conditions()
    return ( GetResearched() == FourCC('R0GX') )
end
function Trig_BegForever_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HR'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HS'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HQ'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegForever()
    gg_trg_BegForever=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegForever, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegForever, Condition(Trig_BegForever_Conditions))
    TriggerAddAction(gg_trg_BegForever, Trig_BegForever_Actions)
end
--===========================================================================
-- Trigger: CanForver
--===========================================================================
function Trig_CanForver_Conditions()
    return ( GetResearched() == FourCC('R0GX') )
end
function Trig_CanForver_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HR'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HS'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HQ'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanForver()
    gg_trg_CanForver=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanForver, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanForver, Condition(Trig_CanForver_Conditions))
    TriggerAddAction(gg_trg_CanForver, Trig_CanForver_Actions)
end
--===========================================================================
-- Trigger: EndBranch
--
-- ????????? ?????????? ????? ????????
--===========================================================================
function EndBranch()
    --New Allies
    SetPlayerTechMaxAllowed(p, FourCC('R0HS'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0H5'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0H8'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HB'), 0)
    
    --Old allies
    SetPlayerTechMaxAllowed(p, FourCC('R0HQ'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HV'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0H9'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HD'), 0)
    
    --Human
    SetPlayerTechMaxAllowed(p, FourCC('R0HR'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0H6'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0HA'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0H7'), 0)
  
end
--===========================================================================
-- Trigger: NewAllies
--===========================================================================
function Trig_NewAllies_Conditions()
    return GetResearched() == FourCC('R0HS')
end
function Trig_NewAllies_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0H5'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0GX'), 0)
    
    
end
--===========================================================================
function InitTrig_NewAllies()
    gg_trg_NewAllies=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NewAllies, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NewAllies, Condition(Trig_NewAllies_Conditions))
    TriggerAddAction(gg_trg_NewAllies, Trig_NewAllies_Actions)
end
--===========================================================================
-- Trigger: NightElf
--===========================================================================
function Trig_NightElf_Conditions()
    return GetResearched() == FourCC('R0H5')
end
function Trig_NightElf_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 4
    SetPlayerTechMaxAllowed(p, FourCC('R0H8'), 1)
    
    
    
end
--===========================================================================
function InitTrig_NightElf()
    gg_trg_NightElf=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NightElf, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NightElf, Condition(Trig_NightElf_Conditions))
    TriggerAddAction(gg_trg_NightElf, Trig_NightElf_Actions)
end
--===========================================================================
-- Trigger: Drayenay
--===========================================================================
function Trig_Drayenay_Conditions()
    return GetResearched() == FourCC('R0H8')
end
function Trig_Drayenay_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
    SetPlayerTechMaxAllowed(p, FourCC('R0HB'), 1)
    SetPlayerTechResearched(p, FourCC('R0H0'), 1)
    
    
    
end
--===========================================================================
function InitTrig_Drayenay()
    gg_trg_Drayenay=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Drayenay, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Drayenay, Condition(Trig_Drayenay_Conditions))
    TriggerAddAction(gg_trg_Drayenay, Trig_Drayenay_Actions)
end
--===========================================================================
-- Trigger: APandarens
--===========================================================================
function Trig_APandarens_Conditions()
    return GetResearched() == FourCC('R0HB')
end
function Trig_APandarens_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
    
    
    if GetPlayerTechCount(p, FourCC('R001'), true) < 1 then
        SetPlayerTechMaxAllowed(p, FourCC('R0HE'), 1)
        
        --???? ??????
        if GetPlayerTechCount(p, FourCC('R0HD'), true) > 0 then
            SetPlayerTechMaxAllowed(p, FourCC('R0HF'), 1)
        end
        
    end
    
    
    
end
--===========================================================================
function InitTrig_APandarens()
    gg_trg_APandarens=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_APandarens, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_APandarens, Condition(Trig_APandarens_Conditions))
    TriggerAddAction(gg_trg_APandarens, Trig_APandarens_Actions)
end
--===========================================================================
-- Trigger: BegDec
--===========================================================================
function Trig_BegDec_Conditions()
    return ( GetResearched() == FourCC('R0HE') )
end
function Trig_BegDec_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HG'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HH'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HF'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegDec()
    gg_trg_BegDec=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegDec, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegDec, Condition(Trig_BegDec_Conditions))
    TriggerAddAction(gg_trg_BegDec, Trig_BegDec_Actions)
end
--===========================================================================
-- Trigger: Decentralization
--===========================================================================
function Trig_Decentralization_Conditions()
    return GetResearched() == FourCC('R0HE')
end
function Trig_Decentralization_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 6
    --call SetPlayerTechMaxAllowed(p, 'R0HE', 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HC'), 1)
    SetPlayerTechResearched(p, FourCC('R001'), 1)
    EndBranch(p)
    
end
--===========================================================================
function InitTrig_Decentralization()
    gg_trg_Decentralization=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Decentralization, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Decentralization, Condition(Trig_Decentralization_Conditions))
    TriggerAddAction(gg_trg_Decentralization, Trig_Decentralization_Actions)
end
--===========================================================================
-- Trigger: BegUnion
--===========================================================================
function Trig_BegUnion_Conditions()
    return ( GetResearched() == FourCC('R0HF') )
end
function Trig_BegUnion_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HG'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HH'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HE'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegUnion()
    gg_trg_BegUnion=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegUnion, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegUnion, Condition(Trig_BegUnion_Conditions))
    TriggerAddAction(gg_trg_BegUnion, Trig_BegUnion_Actions)
end
--===========================================================================
-- Trigger: Union
--===========================================================================
function Trig_Union_Conditions()
    return GetResearched() == FourCC('R0HF')
end
function Trig_Union_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 10
    SetPlayerTechMaxAllowed(p, FourCC('R0HK'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HL'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HM'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HC'), 1)
    SetPlayerTechResearched(p, FourCC('R001'), 1)
    EndBranch(p)
    
    
    
end
--===========================================================================
function InitTrig_Union()
    gg_trg_Union=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Union, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Union, Condition(Trig_Union_Conditions))
    TriggerAddAction(gg_trg_Union, Trig_Union_Actions)
end
--===========================================================================
-- Trigger: VoidElfes
--===========================================================================
function Trig_VoidElfes_Conditions()
    return GetResearched() == FourCC('R0HL')
end
function Trig_VoidElfes_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    
    
    
    
end
--===========================================================================
function InitTrig_VoidElfes()
    gg_trg_VoidElfes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VoidElfes, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_VoidElfes, Condition(Trig_VoidElfes_Conditions))
    TriggerAddAction(gg_trg_VoidElfes, Trig_VoidElfes_Actions)
end
--===========================================================================
-- Trigger: LightArmy
--===========================================================================
function Trig_LightArmy_Conditions()
    return GetResearched() == FourCC('R0HK')
end
function Trig_LightArmy_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    
    
    
    
end
--===========================================================================
function InitTrig_LightArmy()
    gg_trg_LightArmy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LightArmy, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_LightArmy, Condition(Trig_LightArmy_Conditions))
    TriggerAddAction(gg_trg_LightArmy, Trig_LightArmy_Actions)
end
--===========================================================================
-- Trigger: BlackIron
--===========================================================================
function Trig_BlackIron_Conditions()
    return GetResearched() == FourCC('R0HM')
end
function Trig_BlackIron_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
    
    
    
    
end
--===========================================================================
function InitTrig_BlackIron()
    gg_trg_BlackIron=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlackIron, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BlackIron, Condition(Trig_BlackIron_Conditions))
    TriggerAddAction(gg_trg_BlackIron, Trig_BlackIron_Actions)
end
--===========================================================================
-- Trigger: OldAllies
--===========================================================================
function Trig_OldAllies_Conditions()
    return GetResearched() == FourCC('R0HQ')
end
function Trig_OldAllies_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0HV'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0GX'), 0)
    
    
end
--===========================================================================
function InitTrig_OldAllies()
    gg_trg_OldAllies=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OldAllies, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_OldAllies, Condition(Trig_OldAllies_Conditions))
    TriggerAddAction(gg_trg_OldAllies, Trig_OldAllies_Actions)
end
--===========================================================================
-- Trigger: LordaeronAndTeramor
--===========================================================================
function Trig_LordaeronAndTeramor_Conditions()
    return GetResearched() == FourCC('R0HV')
end
function Trig_LordaeronAndTeramor_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 3
    SetPlayerTechMaxAllowed(p, FourCC('R0H9'), 1)
    
    
    
end
--===========================================================================
function InitTrig_LordaeronAndTeramor()
    gg_trg_LordaeronAndTeramor=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordaeronAndTeramor, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_LordaeronAndTeramor, Condition(Trig_LordaeronAndTeramor_Conditions))
    TriggerAddAction(gg_trg_LordaeronAndTeramor, Trig_LordaeronAndTeramor_Actions)
end
--===========================================================================
-- Trigger: Gilneas
--===========================================================================
function Trig_Gilneas_Conditions()
    return GetResearched() == FourCC('R0H9')
end
function Trig_Gilneas_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 2
    SetPlayerTechMaxAllowed(p, FourCC('R0HD'), 1)
    
    
    
end
--===========================================================================
function InitTrig_Gilneas()
    gg_trg_Gilneas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Gilneas, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Gilneas, Condition(Trig_Gilneas_Conditions))
    TriggerAddAction(gg_trg_Gilneas, Trig_Gilneas_Actions)
end
--===========================================================================
-- Trigger: Kultiras
--===========================================================================
function Trig_Kultiras_Conditions()
    return GetResearched() == FourCC('R0HD')
end
function Trig_Kultiras_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 3
    
    if GetPlayerTechCount(p, FourCC('R001'), true) < 1 then
        --???? ??????
        if GetPlayerTechCount(p, FourCC('R0HB'), true) > 0 then
            SetPlayerTechMaxAllowed(p, FourCC('R0HF'), 1)
        end
        
        --???? ???????
        if GetPlayerTechCount(p, FourCC('R0H7'), true) > 0 then
            SetPlayerTechMaxAllowed(p, FourCC('R0HG'), 1)
        end
    end
    
    
    
end
--===========================================================================
function InitTrig_Kultiras()
    gg_trg_Kultiras=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Kultiras, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Kultiras, Condition(Trig_Kultiras_Conditions))
    TriggerAddAction(gg_trg_Kultiras, Trig_Kultiras_Actions)
end
--===========================================================================
-- Trigger: BegArat
--===========================================================================
function Trig_BegArat_Conditions()
    return ( GetResearched() == FourCC('R0HG') )
end
function Trig_BegArat_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HH'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HF'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegArat()
    gg_trg_BegArat=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegArat, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegArat, Condition(Trig_BegArat_Conditions))
    TriggerAddAction(gg_trg_BegArat, Trig_BegArat_Actions)
end
--===========================================================================
-- Trigger: Arathor
--===========================================================================
function Trig_Arathor_Conditions()
    return GetResearched() == FourCC('R0HG')
end
function Trig_Arathor_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 10
    SetPlayerTechMaxAllowed(p, FourCC('R0HJ'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HI'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HC'), 1)
    SetPlayerTechResearched(p, FourCC('R001'), 1)
    EndBranch(p)
    
    
    
end
--===========================================================================
function InitTrig_Arathor()
    gg_trg_Arathor=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Arathor, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Arathor, Condition(Trig_Arathor_Conditions))
    TriggerAddAction(gg_trg_Arathor, Trig_Arathor_Actions)
end
--===========================================================================
-- Trigger: Stromgarge
--===========================================================================
function Trig_Stromgarge_Conditions()
    return GetResearched() == FourCC('R0HJ')
end
function Trig_Stromgarge_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 2
    
    
    
    
end
--===========================================================================
function InitTrig_Stromgarge()
    gg_trg_Stromgarge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Stromgarge, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Stromgarge, Condition(Trig_Stromgarge_Conditions))
    TriggerAddAction(gg_trg_Stromgarge, Trig_Stromgarge_Actions)
end
--===========================================================================
-- Trigger: Dalaran
--===========================================================================
function Trig_Dalaran_Conditions()
    return GetResearched() == FourCC('R0HI')
end
function Trig_Dalaran_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 3
    
    SetPlayerTechResearched(p, FourCC('R0H0'), 1)
    
    
    
end
--===========================================================================
function InitTrig_Dalaran()
    gg_trg_Dalaran=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dalaran, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Dalaran, Condition(Trig_Dalaran_Conditions))
    TriggerAddAction(gg_trg_Dalaran, Trig_Dalaran_Actions)
end
--===========================================================================
-- Trigger: FinStormwind
--===========================================================================
function Trig_FinStormwind_Conditions()
    return GetResearched() == FourCC('R0HR')
end
function Trig_FinStormwind_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    
    SetPlayerTechMaxAllowed(p, FourCC('R0H6'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0GX'), 0)
    
    
end
--===========================================================================
function InitTrig_FinStormwind()
    gg_trg_FinStormwind=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinStormwind, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinStormwind, Condition(Trig_FinStormwind_Conditions))
    TriggerAddAction(gg_trg_FinStormwind, Trig_FinStormwind_Actions)
end
--===========================================================================
-- Trigger: Fin7Legion
--===========================================================================
function Trig_Fin7Legion_Conditions()
    
    return GetResearched() == FourCC('R0H6')
end
function Trig_Fin7Legion_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    
    udg_MainPrice[pi]=udg_MainPrice[pi] + 4
    SetPlayerTechMaxAllowed(p, FourCC('R0HA'), 2)
end
--===========================================================================
function InitTrig_Fin7Legion()
    gg_trg_Fin7Legion=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Fin7Legion, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Fin7Legion, Condition(Trig_Fin7Legion_Conditions))
    TriggerAddAction(gg_trg_Fin7Legion, Trig_Fin7Legion_Actions)
end
--===========================================================================
-- Trigger: FinSRU
--===========================================================================
function Trig_FinSRU_Conditions()
    return GetResearched() == FourCC('R0HA')
end
function Trig_FinSRU_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 3
    SetPlayerTechMaxAllowed(p, FourCC('R0H7'), 1)
    SetPlayerTechResearched(p, FourCC('R0H0'), 1)
end
--===========================================================================
function InitTrig_FinSRU()
    gg_trg_FinSRU=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinSRU, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinSRU, Condition(Trig_FinSRU_Conditions))
    TriggerAddAction(gg_trg_FinSRU, Trig_FinSRU_Actions)
end
--===========================================================================
-- Trigger: FinHoly
--===========================================================================
function Trig_FinHoly_Conditions()
    return GetResearched() == FourCC('R0H7')
end
function Trig_FinHoly_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    AcountAll(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 3
    
    if GetPlayerTechCount(p, FourCC('R001'), true) < 1 then
        SetPlayerTechMaxAllowed(p, FourCC('R0HH'), 1)
    
        --???? ???????
        if GetPlayerTechCount(p, FourCC('R0HD'), true) > 0 then
            SetPlayerTechMaxAllowed(p, FourCC('R0HG'), 1)
        end
    end
 
end
--===========================================================================
function InitTrig_FinHoly()
    gg_trg_FinHoly=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinHoly, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinHoly, Condition(Trig_FinHoly_Conditions))
    TriggerAddAction(gg_trg_FinHoly, Trig_FinHoly_Actions)
end
--===========================================================================
-- Trigger: BegStorm
--===========================================================================
function Trig_BegStorm_Conditions()
    return ( GetResearched() == FourCC('R0HH') )
end
function Trig_BegStorm_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0HE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HG'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0HF'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegStorm()
    gg_trg_BegStorm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegStorm, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegStorm, Condition(Trig_BegStorm_Conditions))
    TriggerAddAction(gg_trg_BegStorm, Trig_BegStorm_Actions)
end
--===========================================================================
-- Trigger: StormwindFirst
--===========================================================================
function Trig_StormwindFirst_Conditions()
    return GetResearched() == FourCC('R0HH')
end
function Trig_StormwindFirst_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    
    
    
    -- ?????? ????? 
    if GetPlayerTechCount(p, FourCC('R0HS'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    if GetPlayerTechCount(p, FourCC('R0H8'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    if GetPlayerTechCount(p, FourCC('R0HB'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    
    --?????
    if GetPlayerTechCount(p, FourCC('R0H9'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    if GetPlayerTechCount(p, FourCC('R0H9'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    if GetPlayerTechCount(p, FourCC('R0HD'), true) == 1 then
        udg_MainPrice[pi]=udg_MainPrice[pi] - 5
    end
    
    AcountAll(p)
    SetPlayerTechMaxAllowed(p, FourCC('R0HN'), 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0HC'), 1)
    SetPlayerTechResearched(p, FourCC('R001'), 1)
    EndBranch(p)
end
--===========================================================================
function InitTrig_StormwindFirst()
    gg_trg_StormwindFirst=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StormwindFirst, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_StormwindFirst, Condition(Trig_StormwindFirst_Conditions))
    TriggerAddAction(gg_trg_StormwindFirst, Trig_StormwindFirst_Actions)
end
--===========================================================================
-- Trigger: RememberLothar
--===========================================================================
function Trig_RememberLothar_Conditions()
    return GetResearched() == FourCC('R0HN')
end
function Trig_RememberLothar_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local pi= GetPlayerId(p)
    udg_MainPrice[pi]=udg_MainPrice[pi] + 15
    AcountAll(p)
    SetPlayerAbilityAvailable(p, FourCC('A19A'), true)
end
--===========================================================================
function InitTrig_RememberLothar()
    gg_trg_RememberLothar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RememberLothar, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_RememberLothar, Condition(Trig_RememberLothar_Conditions))
    TriggerAddAction(gg_trg_RememberLothar, Trig_RememberLothar_Actions)
end
--===========================================================================
-- Trigger: TankFire
--===========================================================================
function Trig_TankFire_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A19N')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker())) and Random(7 , 100)
end
function Trig_TankFire_Actions()
    IssueTargetOrder(GetAttacker(), "breathoffire", GetTriggerUnit())
 
end
--===========================================================================
function InitTrig_TankFire()
    gg_trg_TankFire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankFire, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_TankFire, Condition(Trig_TankFire_Conditions))
    TriggerAddAction(gg_trg_TankFire, Trig_TankFire_Actions)
end
--===========================================================================
-- Trigger: Kristall2
--===========================================================================
function Trig_Kristall2_Actions()
    local u=  CreateUnit(GetOwningPlayer(GetTriggerUnit()), FourCC('o040'), GetSpellTargetX(), GetSpellTargetY(), bj_UNIT_FACING)
    IssueImmediateOrder(u, "manaflareon")
    UnitApplyTimedLife(u, FourCC('BTLF'), 30.00)
    u=nil
end
--===========================================================================
function InitTrig_Kristall2()
    gg_trg_Kristall2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Kristall2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Kristall2, function()
        if GetSpellAbilityId() ~= FourCC('A19S') then return end
        Trig_Kristall2_Actions()
    end)
end
--===========================================================================
-- Trigger: HolyHelp
--===========================================================================
function Trig_HolyHelp_Conditions()
    return ( GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A18X')) > 0 or GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A19F')) > 0 ) and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_HolyHelp_Actions()
    local u= GetEventDamageSource()
    local i=  GetUnitStateSwap(UNIT_STATE_MANA, u) + 10
    SetUnitManaBJ(u, i)
    if i >= 100 then
        IssueImmediateOrder(u, "roar")
    end
    
    u=nil
end
--===========================================================================
function InitTrig_HolyHelp()
    gg_trg_HolyHelp=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HolyHelp, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_HolyHelp, Condition(Trig_HolyHelp_Conditions))
    TriggerAddAction(gg_trg_HolyHelp, Trig_HolyHelp_Actions)
end
--===========================================================================
-- Trigger: WorgenSpell
--===========================================================================
function Trig_WorgenSpell_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A19X')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_WorgenSpell_Actions()
    local u= GetEventDamageSource()
    local i=  GetUnitStateSwap(UNIT_STATE_MANA, u) + 10
    SetUnitManaBJ(u, i)
    if i >= 100 then
        IssueImmediateOrder(u, "frenzyon")
    end
    
    u=nil
end
--===========================================================================
function InitTrig_WorgenSpell()
    gg_trg_WorgenSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_WorgenSpell, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_WorgenSpell, Condition(Trig_WorgenSpell_Conditions))
    TriggerAddAction(gg_trg_WorgenSpell, Trig_WorgenSpell_Actions)
end
--===========================================================================
-- Trigger: MagicUsk
--===========================================================================
function Trig_MagicUsk_Actions()
    local u= GetSpellTargetUnit()
    UnitAddAbility(u, FourCC('A182'))
    RemoveAbilityTimed(u , FourCC('A182') , 15)
    u=nil
end
--===========================================================================
function InitTrig_MagicUsk()
    gg_trg_MagicUsk=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MagicUsk, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MagicUsk, function()
        if GetSpellAbilityId() ~= FourCC('A180') then return end
        Trig_MagicUsk_Actions()
    end)
end
--===========================================================================
-- Trigger: Illusions
--===========================================================================
function Trig_Illusions_Actions()
    local u= GetSpellTargetUnit()
    
    if not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_HERO) then
        UnitAddAbility(u, FourCC('AInv'))
        UnitAddItemByIdSwapped(FourCC('I020'), u)
        RemoveAbilityTimed(u , FourCC('AInv') , 1)
        
    end
    
    
    u=nil
end
--===========================================================================
function InitTrig_Illusions()
    gg_trg_Illusions=CreateTrigger()
    --call DisableTrigger( gg_trg_Illusions )
    TriggerRegisterAnyUnitEventBJ(gg_trg_Illusions, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Illusions, function()
        if GetSpellAbilityId() ~= FourCC('A1A5') then return end
        Trig_Illusions_Actions()
    end)
end
--===========================================================================
-- Trigger: MassMolot
--===========================================================================
function Trig_MassMolot_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local p= GetOwningPlayer(GetTriggerUnit())
    
    local bex = EnemEl
    local level= GetUnitAbilityLevelSwapped(FourCC('AHtb'), GetTriggerUnit())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    GroupEnumUnitsInRangeOfLoc(g, l, 400, bex)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if i >= ( 4 * level ) or u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('H0BN'), l, bj_UNIT_FACING)
        RemoveUnitTimed(u2 , 2)
        UnitAddAbility(u2, FourCC('A17Z'))
        SetUnitManaBJ(u2, 1111111.00)
        SetUnitAbilityLevel(u2, FourCC('A17Z'), level)
        IssueTargetOrder(u2, "thunderbolt", u)
        
        i=i + 1
        GroupRemoveUnit(g, u)
    end
    
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    u2=nil
    bex=nil
end
--===========================================================================
function InitTrig_MassMolot()
    gg_trg_MassMolot=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassMolot, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassMolot, function()
        if GetSpellAbilityId() ~= FourCC('AHtb') then return end
        Trig_MassMolot_Actions()
    end)
end
--===========================================================================
-- Trigger: VarianCharge
--===========================================================================
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_Charge_move_heroV()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
    local dx= GetUnitX(GT)
    local dy= GetUnitY(GT)
    local un
    local x
    local y
    local uron
    local lvl
    local w
    local ugol= JSTRUgolMT(dx , x1 , dy , y1)
    local t1
    local h1
    local MaxW
    if l <= 500 then
        MaxW=l
    else
        MaxW=500
    end
    ---------
    x=dx + 25 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 25 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    w=JSTRParabolaZ(MaxW , l , JSTRRastMT(x , x1 , y , y1)) --????????? ??????
    
    -- ???? ????? ????
    if JSTRRastMT(x1 , dx , y1 , dy) > 25 then --and not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        --call SetUnitFlyHeight(GT, w, 0)
    else
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "attack")
        --call SetUnitFlyHeight(GT, 0, 0)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, JSTRSkill)
            
            -- ????? - ???????? ?? ?????
            if IsUnitType(GT, UNIT_TYPE_HERO) then
                uron=JSTRKofDmg1 * lvl * 0.75 * GetHeroStr(GT, true) + lvl * JSTRKofDmg2
            else
                uron=lvl * JSTRKofDmg2 * 4
            end
            
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
                ----------
                -- ??????? ????? ? ?????? ??????? ?? ???????
                if JSTRBoolMove then
                    ugol=JSTRUgolMT(dx , GetUnitX(un) , dy , GetUnitY(un))
                    t1=CreateTimer()
                    h1=GetHandleId(t1)
                    SaveUnitHandle(Hash, h1, 1, un)
                    SaveReal(Hash, h1, 2, ugol)
                    SaveInteger(Hash, h1, 3, 17)
                    TimerStart(t1, 0.015, true, Trig_JumpSTR_move_units)
                end
                ---------- 
            end
            GroupRemoveUnit(g, un)
        end
        DestroyGroup(g)
    end
    ---------
    GT=nil
    un=nil
    g=nil
    t=nil
    t1=nil
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_VarianCharge_Actions()
    local GT= GetTriggerUnit()
    --local group g = CreateGroup()
    local t= CreateTimer()
    local h= GetHandleId(t)
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= JSTRRastMT(x , x1 , y , y1)
    
    JSTRSkill=GetSpellAbilityId()
    UnitAddAbility(GT, FourCC('Amrf'))
    UnitRemoveAbility(GT, FourCC('Amrf'))
    ---------
    SaveUnitHandle(Hash, h, 1, GT)
    if l ~= 0 then
        SaveReal(Hash, h, 2, l)
    else
        SaveReal(Hash, h, 2, 1)
    end
    SaveReal(Hash, h, 4, x1)
    SaveReal(Hash, h, 5, y1)
    --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.025, true, Trig_Charge_move_heroV) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_VarianCharge()
    gg_trg_VarianCharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VarianCharge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VarianCharge, function()
        if GetSpellAbilityId() ~= FourCC('A1AG') then return end
        Trig_VarianCharge_Actions()
    end)
end
--===========================================================================
-- Trigger: VariarTaunt
--===========================================================================
function Trig_VariarTaunt_Func004C()
    return ( GetUnitAbilityLevelSwapped(FourCC('A1AL'), GetTriggerUnit()) > 1 )
end
function Trig_VariarTaunt_Actions()
    BlzUnitHideAbility(GetTriggerUnit(), FourCC('A1AL'), true)
    UnitAddAbilityBJ(FourCC('A1AK'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A1AJ'), GetTriggerUnit())
    if ( Trig_VariarTaunt_Func004C() ) then
        SetUnitAbilityLevelSwapped(FourCC('A1AJ'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AK'), GetTriggerUnit(), 2)
    else
    end
end
--===========================================================================
function InitTrig_VariarTaunt()
    gg_trg_VariarTaunt=CreateTrigger()
    DisableTrigger(gg_trg_VariarTaunt)
    TriggerRegisterAnyUnitEventBJ(gg_trg_VariarTaunt, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VariarTaunt, function()
        if GetSpellAbilityId() ~= FourCC('A1AM') then return end
        Trig_VariarTaunt_Actions()
    end)
end
--===========================================================================
-- Trigger: VariarTitan
--===========================================================================
function Trig_VariarTitan_Actions()
    BlzUnitHideAbility(GetTriggerUnit(), FourCC('A1AL'), true)
    UnitAddAbilityBJ(FourCC('A1AP'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A1AQ'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A1AR'), GetTriggerUnit())
    if GetUnitAbilityLevelSwapped(FourCC('A1AL'), GetTriggerUnit()) > 1 then
        SetUnitAbilityLevelSwapped(FourCC('A1AQ'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AR'), GetTriggerUnit(), 2)
    end
    
    
end
--===========================================================================
function InitTrig_VariarTitan()
    gg_trg_VariarTitan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VariarTitan, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VariarTitan, function()
        if GetSpellAbilityId() ~= FourCC('A1AO') then return end
        Trig_VariarTitan_Actions()
    end)
end
--===========================================================================
-- Trigger: VariarDamager
--===========================================================================
function Trig_VariarDamager_Actions()
    BlzUnitHideAbility(GetTriggerUnit(), FourCC('A1AL'), true)
    UnitAddAbilityBJ(FourCC('A1AU'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A1AT'), GetTriggerUnit())
    
    if GetUnitAbilityLevelSwapped(FourCC('A1AL'), GetTriggerUnit()) > 1 then
        SetUnitAbilityLevelSwapped(FourCC('A1AU'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AT'), GetTriggerUnit(), 2)
    end
    
    
end
--===========================================================================
function InitTrig_VariarDamager()
    gg_trg_VariarDamager=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VariarDamager, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VariarDamager, function()
        if GetSpellAbilityId() ~= FourCC('A1AS') then return end
        Trig_VariarDamager_Actions()
    end)
end
--===========================================================================
-- Trigger: Level2
--===========================================================================
function Trig_Level2_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1AL') and GetLearnedSkillLevel() == 2
end
function Trig_Level2_Actions()
    --Tank
    if GetUnitAbilityLevelSwapped(FourCC('A1AJ'), GetTriggerUnit()) ~= 0 then
        SetUnitAbilityLevelSwapped(FourCC('A1AK'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AJ'), GetTriggerUnit(), 2)
    end
    --Titan
    if GetUnitAbilityLevelSwapped(FourCC('A1AR'), GetTriggerUnit()) ~= 0 then
        SetUnitAbilityLevelSwapped(FourCC('A1AR'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AQ'), GetTriggerUnit(), 2)
    end
    --Damager
    if GetUnitAbilityLevelSwapped(FourCC('A1AU'), GetTriggerUnit()) ~= 0 then
        SetUnitAbilityLevelSwapped(FourCC('A1AU'), GetTriggerUnit(), 2)
        SetUnitAbilityLevelSwapped(FourCC('A1AT'), GetTriggerUnit(), 2)
    end
    
    
end
--===========================================================================
function InitTrig_Level2()
    gg_trg_Level2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Level2, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Level2, Condition(Trig_Level2_Conditions))
    TriggerAddAction(gg_trg_Level2, Trig_Level2_Actions)
end
--===========================================================================
-- Trigger: PaladinHpSpell
--===========================================================================
function Trig_PaladinHpSpell_Conditions()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0WZ'), GetTriggerUnit()) == 1 )
end
function Trig_PaladinHpSpell_Func001Func001Func007C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 75.00 )
end
function Trig_PaladinHpSpell_Func001Func001C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 50.00 )
end
function Trig_PaladinHpSpell_Func001C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 25.00 )
end
function Trig_PaladinHpSpell_Actions()
    if ( Trig_PaladinHpSpell_Func001C() ) then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if ( Trig_PaladinHpSpell_Func001Func001C() ) then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if ( Trig_PaladinHpSpell_Func001Func001Func007C() ) then
                UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 1)
            else
                UnitRemoveAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            end
        end
    end
end
--===========================================================================
function InitTrig_PaladinHpSpell()
    gg_trg_PaladinHpSpell=CreateTrigger()
    DisableTrigger(gg_trg_PaladinHpSpell)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinHpSpell, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_PaladinHpSpell, Condition(Trig_PaladinHpSpell_Conditions))
    TriggerAddAction(gg_trg_PaladinHpSpell, Trig_PaladinHpSpell_Actions)
end
--===========================================================================
-- Trigger: PaladinHpSpell2
--===========================================================================
function Trig_PaladinHpSpell2_Conditions()
    return ( GetUnitAbilityLevelSwapped(FourCC('A0WZ'), GetTriggerUnit()) == 2 )
end
function Trig_PaladinHpSpell2_Func001Func001Func007C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 95.00 )
end
function Trig_PaladinHpSpell2_Func001Func001C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 70.00 )
end
function Trig_PaladinHpSpell2_Func001C()
    return ( GetUnitLifePercent(GetTriggerUnit()) < 45.00 )
end
function Trig_PaladinHpSpell2_Actions()
    if ( Trig_PaladinHpSpell2_Func001C() ) then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if ( Trig_PaladinHpSpell2_Func001Func001C() ) then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if ( Trig_PaladinHpSpell2_Func001Func001Func007C() ) then
                UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 1)
            else
                UnitRemoveAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            end
        end
    end
end
--===========================================================================
function InitTrig_PaladinHpSpell2()
    gg_trg_PaladinHpSpell2=CreateTrigger()
    DisableTrigger(gg_trg_PaladinHpSpell2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PaladinHpSpell2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_PaladinHpSpell2, Condition(Trig_PaladinHpSpell2_Conditions))
    TriggerAddAction(gg_trg_PaladinHpSpell2, Trig_PaladinHpSpell2_Actions)
end
--===========================================================================
-- Trigger: Vozd
--===========================================================================
function Trig_Vozd_Actions()
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XI'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('H0H7'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XH'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XJ'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Vozd()
    gg_trg_Vozd=CreateTrigger()
    DisableTrigger(gg_trg_Vozd)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Vozd, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Vozd, function()
        if GetSpellAbilityId() ~= FourCC('A0XI') then return end
        Trig_Vozd_Actions()
    end)
end
--===========================================================================
-- Trigger: Defend
--===========================================================================
function Trig_Defend_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('H0H9'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XH'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XI'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XJ'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Defend()
    gg_trg_Defend=CreateTrigger()
    DisableTrigger(gg_trg_Defend)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Defend, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Defend, function()
        if GetSpellAbilityId() ~= FourCC('A0XH') then return end
        Trig_Defend_Actions()
    end)
end
--===========================================================================
-- Trigger: Heal
--===========================================================================
function Trig_Heal_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('H0H8'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XH'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XI'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A0XJ'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Heal()
    gg_trg_Heal=CreateTrigger()
    DisableTrigger(gg_trg_Heal)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Heal, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Heal, function()
        if GetSpellAbilityId() ~= FourCC('A0XJ') then return end
        Trig_Heal_Actions()
    end)
end
--===========================================================================
-- Trigger: StartAlliance
--===========================================================================
function Trig_StartAlliance_Func001A()
    AcountAll(GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A19A'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h02Z'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0HX'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0I3'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hamg'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0ME'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hmkg'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0MF'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0MD'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HM'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HL'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HK'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HJ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HI'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HH'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HG'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HF'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HE'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HD'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HB'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HA'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0H9'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0H8'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0H7'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0H6'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0H5'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HN'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HC'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0HV'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('Hlgr'), 1, GetEnumPlayer())
    -- ---
end
function Trig_StartAlliance_Actions()
    ForForce(udg_AllPlayers, Trig_StartAlliance_Func001A)
end
--===========================================================================
function InitTrig_StartAlliance()
