
--===========================================================================
-- Trigger: StartForestTrolls
--===========================================================================
function ForestStart()
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('o05N'), 3, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o05M'), 3, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o05O'), 3, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('O056'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O057'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O058'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O059'), 1, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('o04Y'), 0, GetEnumPlayer())
    
end
function Trig_StartForestTrolls_Actions()
    ForForce(udg_AllPlayers, ForestStart)
end
--===========================================================================
function InitTrig_StartForestTrolls()
    gg_trg_StartForestTrolls=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartForestTrolls, 0.01)
    TriggerAddAction(gg_trg_StartForestTrolls, Trig_StartForestTrolls_Actions)
end
--===========================================================================
-- Trigger: Charge
--===========================================================================
--//================================================================================================================================================================================
--// ???? 3 - ??????? ??????
--//================
--function Trig_JumpSTR_move_units takes nothing returns nothing
--    local timer t = GetExpiredTimer()
--    local integer h = GetHandleId(t)
--    local unit un = LoadUnitHandle(Hash,h,1)
--    local real ugol = LoadReal(Hash,h,2)
--    local integer kol = LoadInteger(Hash,h,3)
--    local real x = GetUnitX(un)
--    local real y = GetUnitY(un)
--    // ---------
--    set x = x + 10 * Cos(ugol * bj_DEGTORAD) //????????? ????????? ?
--    set y = y + 10 * Sin(ugol * bj_DEGTORAD) //????????? ????????? ?
--    if kol >= 0 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
--        call SetUnitX(un,x)
--        call SetUnitY(un,y)
--        call SaveInteger(Hash, h, 3, kol-1)
--    else
--        call DestroyTimer(t)
--        call FlushChildHashtable(Hash,h)
--    endif
--    // ----------
--    set un = null
--    set t = null
--endfunction
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_Charge_move_hero()
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
                uron=JSTRKofDmg1 * lvl * GetHeroStr(GT, true) + lvl * JSTRKofDmg2
            else
                uron=lvl * JSTRKofDmg2 * 4
            end
            
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
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
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_Charge_Actions()
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
    TimerStart(t, 0.025, true, Trig_Charge_move_hero) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_Charge()
    gg_trg_Charge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Charge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Charge, function()
        if GetSpellAbilityId() ~= FourCC('A1H3') then return end
        Trig_Charge_Actions()
    end)
end
--===========================================================================
-- Trigger: SetLifeNormal
--===========================================================================
function Trig_SetLifeNormal_Conditions()
    return GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) - GetEventDamage() < 5 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1G6')) ~= 0
end
function Trig_SetLifeNormal_Actions()
   
    SetUnitLifeBJ(GetTriggerUnit(), 3.00 + GetEventDamage())
end
--===========================================================================
function InitTrig_SetLifeNormal()
    gg_trg_SetLifeNormal=CreateTrigger()
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_SetLifeNormal, EVENT_PLAYER_UNIT_DAMAGING )
    TriggerAddCondition(gg_trg_SetLifeNormal, Condition(Trig_SetLifeNormal_Conditions))
    TriggerAddAction(gg_trg_SetLifeNormal, Trig_SetLifeNormal_Actions)
end
function Trig_ZacliatieOfLive_Actions()
    local u= GetTriggerUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    UnitAddAbility(u, FourCC('A1G6'))
    TriggerRegisterUnitEvent(gg_trg_SetLifeNormal, u, EVENT_UNIT_DAMAGING)
	local t = CreateTimer()
	TimerStart(t, 15 * GetUnitAbilityLevel(u, FourCC('A1G6')), false, function()
		UnitRemoveAbility(u, FourCC('A1G6'))
		DestroyTimer(t)
	end)
    
    u=nil
    t=nil
end
--===========================================================================
function InitTrig_ZacliatieOfLive()
    gg_trg_ZacliatieOfLive=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZacliatieOfLive, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZacliatieOfLive, function()
        if GetSpellAbilityId() ~= FourCC('A1G5') then return end
        Trig_ZacliatieOfLive_Actions()
    end)
end
--===========================================================================
-- Trigger: ReturnDamage
--===========================================================================
function Trig_ReturnDamage_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1GQ')) > 0
end
function Trig_ReturnDamage_Actions()
    local u= GetTriggerUnit()
    local u2= nil
    local g= CreateGroup()
    local b
    local l
    local damage= GetEventDamage() * 1.30
    DisableTrigger(GetTriggeringTrigger())
    udg_LocalPlayer=GetOwningPlayer(u)
    udg_LocalInteger2=0
    GroupEnumUnitsInRange(g, GetUnitX(u), GetUnitY(u), 550, b)
   -- set u2 = FirstOfGroup(g) 
    if udg_LocalInteger2 > 0 then
        u2=BlzGroupUnitAt(g, GetRandomInt(0, udg_LocalInteger2 - 1))
        if u2 ~= nil and UnitAlive(u2) and u ~= u2 then
            SetUnitLifeBJ(u, GetUnitState(u, UNIT_STATE_LIFE) + damage)
            UnitDamageTargetBJ(u, u2, damage, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
            l=AddLightning("MFPB", true, GetUnitX(u), GetUnitY(u), GetUnitX(u2), GetUnitY(u2))
            RemoveLigtingTimed(l , 0.9)
            
        end
    end
    DestroyGroup(g)
    DestroyBoolExpr(b)
    g=nil
    b=nil
    l=nil
    u=nil
    u2=nil
    
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_ReturnDamage()
    gg_trg_ReturnDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ReturnDamage, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_ReturnDamage, Condition(Trig_ReturnDamage_Conditions))
    TriggerAddAction(gg_trg_ReturnDamage, Trig_ReturnDamage_Actions)
end
--===========================================================================
-- Trigger: ZacliatieOfDamage
--===========================================================================
function Trig_ZacliatieOfDamage_Actions()
    local u= GetTriggerUnit()
    
    UnitAddAbility(u, FourCC('A1GQ'))
    RemoveAbilityTimed(u , FourCC('A1GQ') , GetUnitAbilityLevel(u, FourCC('A1GP')) * 20)
    u=nil
end
--===========================================================================
function InitTrig_ZacliatieOfDamage()
    gg_trg_ZacliatieOfDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZacliatieOfDamage, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_ZacliatieOfDamage, function()
        if GetSpellAbilityId() ~= FourCC('A1GP') then return end
        Trig_ZacliatieOfDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: YarostBeg
--===========================================================================
function Trig_YarostBeg_Actions()
    local u= GetTriggerUnit()
    
    SetUnitLifePercentBJ(u, GetUnitLifePercent(u) * 0.75)
    
    UnitAddAbility(u, FourCC('A1GS')) -- ?????? ?? ????
    RemoveAbilityTimed(u , FourCC('A1GS') , 24.5)
    --call UnitAddAbility(u,'A1G2')
    --call BlzStartUnitAbilityCooldown(u,'A1G2',1)
    --call BlzUnitHideAbility(u,'A1F9',true)
    RemoveAbilityTimed(u , FourCC('A1GS') , 25)
    
    u=nil
end
--===========================================================================
function InitTrig_YarostBeg()
    gg_trg_YarostBeg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_YarostBeg, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_YarostBeg, function()
        if GetSpellAbilityId() ~= FourCC('A1F9') then return end
        Trig_YarostBeg_Actions()
    end)
end
--===========================================================================
-- Trigger: RitualPoglocenia
--===========================================================================
function Trig_RitualPoglocenia_Actions()
   --local unit u = GetTriggerUnit()
    local u2= GetSpellTargetUnit()
    local id= GetUnitTypeId(u2)
    
    
    --????
    if id == FourCC('o052') or id == FourCC('o051') then
        u2=ReplaceUnit2(u2 , FourCC('o05O') , bj_UNIT_STATE_METHOD_RELATIVE)
        
    --?????
    elseif id == FourCC('o04Z') or id == FourCC('o04X') or id == FourCC('o04V') or id == FourCC('o050') then
        u2=ReplaceUnit2(u2 , FourCC('o05M') , bj_UNIT_STATE_METHOD_RELATIVE)
    --??
    elseif id == FourCC('o04W') or id == FourCC('o04Y') or id == FourCC('o053') then
        u2=ReplaceUnit2(u2 , FourCC('o05N') , bj_UNIT_STATE_METHOD_RELATIVE)
    else
        KillUnit(u2)
    end
    
    UnitAddAbility(u2, FourCC('A0Z5'))
    
    u2=nil
end
--===========================================================================
function InitTrig_RitualPoglocenia()
    gg_trg_RitualPoglocenia=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RitualPoglocenia, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_RitualPoglocenia, function()
        if GetSpellAbilityId() ~= FourCC('A1GA') then return end
        if not (GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1F9')) > 0 and not IsUnitType(GetSpellTargetUnit(), UNIT_TYPE_HERO)) then return end
        Trig_RitualPoglocenia_Actions()
    end)
end
--===========================================================================
-- Trigger: WantAxe
--===========================================================================
function Trig_WantAxe_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0,"2")
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1G3')) > 0 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1G4')) == 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_WantAxe_Actions()
    local u= GetEventDamageSource()
    local u2= GetTriggerUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    --call DisplayTextToPlayer(Player(0),0,0,"2"+GetUnitName(u2))
     
    UnitAddAbility(u2, FourCC('A1G4'))
    
	local t = CreateTimer()
	TimerStart(t, 7, false, function()
		UnitRemoveAbility(u2, FourCC('A1G4'))
		DestroyTimer(t)
	end)
    
    u=nil
    u2=nil
    t=nil
end
--===========================================================================
function InitTrig_WantAxe()
    gg_trg_WantAxe=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_WantAxe, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_WantAxe, Condition(Trig_WantAxe_Conditions))
    TriggerAddAction(gg_trg_WantAxe, Trig_WantAxe_Actions)
end
--===========================================================================
-- Trigger: BeFaster
--===========================================================================
function Trig_BeFaster_Conditions()
    
    return GetUnitAbilityLevel(BlzGetEventDamageTarget(), FourCC('A1F9')) > 0 or GetUnitAbilityLevel(BlzGetEventDamageTarget(), FourCC('A1G2')) > 0 -- ??? ?????? ??????
    
    
end
function Trig_BeFaster_Actions()
    local u= BlzGetEventDamageTarget()
    local spellid= FourCC('A1F8')
    local timerspellid= FourCC('A1CX')
    local lifep= GetUnitLifePercent(u)
    local time= 10
    
    
    --call DisplayTextToPlayer(Player(0),0,0,"")
    if lifep <= 30 then
        UnitAddAbility(u, spellid)
        SetUnitAbilityLevel(u, spellid, 4)
        BlzStartUnitAbilityCooldown(u, timerspellid, 20)
       -- call DisplayTextToPlayer(Player(0),0,0,"25"+R2S(lifep))
    elseif lifep <= 50 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 3)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))   
    elseif lifep <= 70 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 2)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
    elseif lifep <= 90 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 1)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
                
    else
            UnitRemoveAbility(u, spellid)
       --     call DisplayTextToPlayer(Player(0),0,0,""+R2S(lifep))
    end
    UnitAddAbility(u, timerspellid)
    BlzStartUnitAbilityCooldown(u, timerspellid, time)
    TriggerSleepAction(time)
    
    if BlzGetUnitAbilityCooldownRemaining(u, timerspellid) == 0 then
        UnitRemoveAbility(u, spellid)
    end
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_BeFaster()
    gg_trg_BeFaster=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeFaster, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_BeFaster, Condition(Trig_BeFaster_Conditions))
    TriggerAddAction(gg_trg_BeFaster, Trig_BeFaster_Actions)
end
--===========================================================================
-- Trigger: MassSetca
--===========================================================================
function Trig_MassSetca_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local bex
    local dammyAbility= FourCC('A1FD')
    local level= GetUnitAbilityLevel(GetTriggerUnit(), GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 100 + 45 * level, bex)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('H0BN'), l, bj_UNIT_FACING)
        udg_LocalUnit2=u2
        TriggerExecute(gg_trg_ToKill2)
        UnitAddAbility(u2, dammyAbility)
        SetUnitManaBJ(u2, 1111111.00)
        SetUnitAbilityLevel(u2, dammyAbility, level)
        IssueTargetOrder(u2, "ensnare", u)
        
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
function InitTrig_MassSetca()
    gg_trg_MassSetca=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassSetca, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassSetca, function()
        if GetSpellAbilityId() ~= FourCC('A1FC') then return end
        Trig_MassSetca_Actions()
    end)
end
--===========================================================================
-- Trigger: MassFrenzy
--===========================================================================
function FFrenzy()
    return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and GetUnitAbilityLevel(GetFilterUnit(), FourCC('BUhf')) == 0 and not IsUnitType(GetFilterUnit(), UNIT_TYPE_MECHANICAL) and not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
    
end
function Trig_MassFrenzy_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local p= GetOwningPlayer(GetTriggerUnit())
    
    local bex
    
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = FFrenzy
    GroupEnumUnitsInRangeOfLocCounted(g, l, 400, bex, 4)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if i > 4 or u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('h05P'), l, bj_UNIT_FACING)
        
        
        UnitAddAbility(u2, FourCC('A1FA'))
        SetUnitManaBJ(u2, 1111111.00)
        
        IssueTargetOrder(u2, "unholyfrenzy", u)
        
        i=i + 1
        RemoveUnitTimed(u2 , 2)
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
function InitTrig_MassFrenzy()
    gg_trg_MassFrenzy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassFrenzy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassFrenzy, function()
        if GetSpellAbilityId() ~= FourCC('A1ID') then return end
        Trig_MassFrenzy_Actions()
    end)
end