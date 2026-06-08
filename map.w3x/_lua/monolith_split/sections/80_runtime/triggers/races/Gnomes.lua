
--===========================================================================
-- Trigger: GnomesOn
--===========================================================================
function Trig_GnomesOn_Actions()
    EnableTrigger(gg_trg_GelbinSpellAttacked)
    EnableTrigger(gg_trg_GelbinSpellClick)
    
    EnableTrigger(gg_trg_HeroSell)
    EnableTrigger(gg_trg_TankChangeAttack)
    EnableTrigger(gg_trg_TankVenecAttack)
   
    
end
--===========================================================================
function InitTrig_GnomesOn()
    gg_trg_GnomesOn=CreateTrigger()
    TriggerAddAction(gg_trg_GnomesOn, Trig_GnomesOn_Actions)
end
--===========================================================================
-- Trigger: GnomesStart
--===========================================================================
function Trig_GnomesStart_Func002A()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BB'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0B5'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BC'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BD'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BE'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BF'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BG'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BH'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BI'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BA'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0B9'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0B7'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0B8'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BJ'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BK'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BL'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BM'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BN'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BO'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BP'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CS'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CR'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CQ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CP'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C8'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C2'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BP'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BP'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0BO'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0G4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0G5'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0G1'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0G2'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FQ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FT'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FW'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FV'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FN'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FP'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FJ'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FG'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FF'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FH'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('h0FO'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0GE'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0GC'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0GG'), 1, GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0SH'), GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C4'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 0, GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0TL'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A16A'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0SO'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0SN'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0U8'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0U9'), GetEnumPlayer())
    SetPlayerAbilityAvailableBJ(false, FourCC('A0UA'), GetEnumPlayer())
end
function Trig_GnomesStart_Actions()
    ForForce(udg_AllPlayers, Trig_GnomesStart_Func002A)
end
--===========================================================================
function InitTrig_GnomesStart()
    gg_trg_GnomesStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_GnomesStart, 2.00)
    TriggerAddAction(gg_trg_GnomesStart, Trig_GnomesStart_Actions)
end
--===========================================================================
-- Trigger: GelbinSpellAttacked
--===========================================================================
function Trig_GelbinSpellAttacked_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0XC'), GetTriggerUnit()) == 1
end
function Trig_GelbinSpellAttacked_Func001Func001Func002Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) < 80.00
end
function Trig_GelbinSpellAttacked_Func001Func001Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) < 60.00
end
function Trig_GelbinSpellAttacked_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 40.00
end
function Trig_GelbinSpellAttacked_Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 20.00
end
function Trig_GelbinSpellAttacked_Actions()
    if Trig_GelbinSpellAttacked_Func001C() then
        SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 5)
    else
        if Trig_GelbinSpellAttacked_Func001Func001C() then
            SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 4)
        else
            if Trig_GelbinSpellAttacked_Func001Func001Func002C() then
                SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 3)
            else
                if Trig_GelbinSpellAttacked_Func001Func001Func002Func002C() then
                    SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 2)
                else
                    SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 1)
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_GelbinSpellAttacked()
    gg_trg_GelbinSpellAttacked=CreateTrigger()
    DisableTrigger(gg_trg_GelbinSpellAttacked)
    TriggerRegisterAnyUnitEventBJ(gg_trg_GelbinSpellAttacked, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_GelbinSpellAttacked, Condition(Trig_GelbinSpellAttacked_Conditions))
    TriggerAddAction(gg_trg_GelbinSpellAttacked, Trig_GelbinSpellAttacked_Actions)
end
--===========================================================================
-- Trigger: GelbinSpellClick
--===========================================================================
function Trig_GelbinSpellClick_Func002Func001Func002Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) < 80.00
end
function Trig_GelbinSpellClick_Func002Func001Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) < 60.00
end
function Trig_GelbinSpellClick_Func002Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 40.00
end
function Trig_GelbinSpellClick_Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) < 20.00
end
function Trig_GelbinSpellClick_Actions()
    SetUnitLifePercentBJ(GetTriggerUnit(), GetUnitLifePercent(GetTriggerUnit()) + 10.00)
    if Trig_GelbinSpellClick_Func002C() then
        SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 5)
    else
        if Trig_GelbinSpellClick_Func002Func001C() then
            SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 4)
        else
            if Trig_GelbinSpellClick_Func002Func001Func002C() then
                SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 3)
            else
                if Trig_GelbinSpellClick_Func002Func001Func002Func002C() then
                    SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 2)
                else
                    SetUnitAbilityLevelSwapped(FourCC('A0XD'), GetTriggerUnit(), 1)
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_GelbinSpellClick()
    gg_trg_GelbinSpellClick=CreateTrigger()
    DisableTrigger(gg_trg_GelbinSpellClick)
    TriggerRegisterAnyUnitEventBJ(gg_trg_GelbinSpellClick, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GelbinSpellClick, function()
        if GetSpellAbilityId() ~= FourCC('A0XC') then return end
        Trig_GelbinSpellClick_Actions()
    end)
end
--===========================================================================
-- Trigger: HeroSell
--===========================================================================
function Trig_HeroSell_Actions()
    udg_LocalReal2=GetUnitStateSwap(UNIT_STATE_LIFE, GetSpellTargetUnit())
    udg_LocalReal2=udg_LocalReal2 * I2R(GetUnitAbilityLevelSwapped(FourCC('A0TF'), GetTriggerUnit()))
    udg_LocalReal2=udg_LocalReal2 * 0.25
    SetUnitLifeBJ(GetTriggerUnit(), GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) + udg_LocalReal2)
    KillUnit(GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_HeroSell()
    gg_trg_HeroSell=CreateTrigger()
    DisableTrigger(gg_trg_HeroSell)
    TriggerRegisterAnyUnitEventBJ(gg_trg_HeroSell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_HeroSell, function()
        if GetSpellAbilityId() ~= FourCC('A0TF') then return end
        Trig_HeroSell_Actions()
    end)
end
--===========================================================================
-- Trigger: TankChangeAttack
--===========================================================================
function Trig_TankChangeAttack_Func001C()
    return BlzGetUnitWeaponBooleanField(GetTriggerUnit(), UNIT_WEAPON_BF_ATTACKS_ENABLED, 0)
end
function Trig_TankChangeAttack_Actions()
    if Trig_TankChangeAttack_Func001C() then
        BlzSetUnitWeaponBooleanFieldBJ(GetTriggerUnit(), UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, false)
        BlzSetUnitWeaponBooleanFieldBJ(GetTriggerUnit(), UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, true)
    else
        BlzSetUnitWeaponBooleanFieldBJ(GetTriggerUnit(), UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, true)
        BlzSetUnitWeaponBooleanFieldBJ(GetTriggerUnit(), UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, false)
    end
end
--===========================================================================
function InitTrig_TankChangeAttack()
    gg_trg_TankChangeAttack=CreateTrigger()
    DisableTrigger(gg_trg_TankChangeAttack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankChangeAttack, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_TankChangeAttack, function()
        if GetSpellAbilityId() ~= FourCC('A0S6') then return end
        Trig_TankChangeAttack_Actions()
    end)
end
--===========================================================================
-- Trigger: TankVenecAttack
--===========================================================================
function Trig_TankVenecAttack_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0S2'), GetAttacker()) > 0
end
function Trig_TankVenecAttack_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0S3'), GetAttacker()) == 0
end
function Trig_TankVenecAttack_Actions()
    if Trig_TankVenecAttack_Func001C() then
        UnitAddAbilityBJ(FourCC('A0S3'), GetAttacker())
    else
        UnitRemoveAbilityBJ(FourCC('A0S3'), GetAttacker())
    end
end
--===========================================================================
function InitTrig_TankVenecAttack()
    gg_trg_TankVenecAttack=CreateTrigger()
    DisableTrigger(gg_trg_TankVenecAttack)
    TriggerRegisterAnyUnitEventBJ(gg_trg_TankVenecAttack, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_TankVenecAttack, Condition(Trig_TankVenecAttack_Conditions))
    TriggerAddAction(gg_trg_TankVenecAttack, Trig_TankVenecAttack_Actions)
end
--===========================================================================
-- Trigger: All Gnomes Cansel
--===========================================================================
function Trig_All_Gnomes_Cansel_Func001C()
    return (( ( GetResearched() == FourCC('R0B9') ) )) or (( ( GetResearched() == FourCC('R0BA') ) )) or (( ( GetResearched() == FourCC('R0BB') ) )) or (( ( GetResearched() == FourCC('R0B5') ) )) or (( ( GetResearched() == FourCC('R0BC') ) )) or (( ( GetResearched() == FourCC('R0BD') ) )) or (( ( GetResearched() == FourCC('R0BE') ) )) or (( ( GetResearched() == FourCC('R0BF') ) )) or (( ( GetResearched() == FourCC('R0BG') ) )) or (( ( GetResearched() == FourCC('R0BH') ) )) or (( ( GetResearched() == FourCC('R0CR') ) )) or (( ( GetResearched() == FourCC('R0BI') ) ))
end
function Trig_All_Gnomes_Cansel_Conditions()
    return Trig_All_Gnomes_Cansel_Func001C()
end
function Trig_All_Gnomes_Cansel_Func004Func002C()
    return GetPlayerTechCountSimple(FourCC('R0BC'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func004C()
    return GetPlayerTechCountSimple(FourCC('R0BA'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func005C()
    return GetPlayerTechCountSimple(FourCC('R0B5'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func006Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BD'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func006C()
    return GetPlayerTechCountSimple(FourCC('R0BI'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func007Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BF'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Func007C()
    return GetPlayerTechCountSimple(FourCC('R0BB'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Cansel_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    if Trig_All_Gnomes_Cansel_Func004C() then
        if Trig_All_Gnomes_Cansel_Func004Func002C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BH'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BC'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BA'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Cansel_Func005C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0BE'), 1, udg_LocalPlayer)
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0B5'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Cansel_Func006C() then
        if Trig_All_Gnomes_Cansel_Func006Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BD'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BI'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Cansel_Func007C() then
        if Trig_All_Gnomes_Cansel_Func007Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BG'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BF'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BB'), 1, udg_LocalPlayer)
    end
    SetPlayerTechMaxAllowedSwap(FourCC('R0B9'), 1, udg_LocalPlayer)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 1, udg_LocalPlayer)
end
--===========================================================================
function InitTrig_All_Gnomes_Cansel()
    gg_trg_All_Gnomes_Cansel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_All_Gnomes_Cansel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_All_Gnomes_Cansel, Condition(Trig_All_Gnomes_Cansel_Conditions))
    TriggerAddAction(gg_trg_All_Gnomes_Cansel, Trig_All_Gnomes_Cansel_Actions)
end
--===========================================================================
-- Trigger: All Gnomes Begin
--===========================================================================
function Trig_All_Gnomes_Begin_Func002C()
    return (( ( GetResearched() == FourCC('R0B9') ) )) or (( ( GetResearched() == FourCC('R0BA') ) )) or (( ( GetResearched() == FourCC('R0BB') ) )) or (( ( GetResearched() == FourCC('R0B5') ) )) or (( ( GetResearched() == FourCC('R0BC') ) )) or (( ( GetResearched() == FourCC('R0BD') ) )) or (( ( GetResearched() == FourCC('R0BE') ) )) or (( ( GetResearched() == FourCC('R0BF') ) )) or (( ( GetResearched() == FourCC('R0BG') ) )) or (( ( GetResearched() == FourCC('R0BH') ) )) or (( ( GetResearched() == FourCC('R0CR') ) )) or (( ( GetResearched() == FourCC('R0BI') ) )) or (( ( GetResearched() == FourCC('R0C0') ) ))
end
function Trig_All_Gnomes_Begin_Conditions()
    return Trig_All_Gnomes_Begin_Func002C()
end
function Trig_All_Gnomes_Begin_Func004Func002C()
    return GetPlayerTechCountSimple(FourCC('R0BC'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func004C()
    return GetPlayerTechCountSimple(FourCC('R0BA'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func005C()
    return GetPlayerTechCountSimple(FourCC('R0B5'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func006Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BD'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func006C()
    return GetPlayerTechCountSimple(FourCC('R0BI'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func007Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BF'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Func007C()
    return GetPlayerTechCountSimple(FourCC('R0BB'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Begin_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    if Trig_All_Gnomes_Begin_Func004C() then
        if Trig_All_Gnomes_Begin_Func004Func002C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BH'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BC'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BA'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Begin_Func005C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0BE'), 0, udg_LocalPlayer)
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0B5'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Begin_Func006C() then
        if Trig_All_Gnomes_Begin_Func006Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BD'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BI'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Begin_Func007C() then
        if Trig_All_Gnomes_Begin_Func007Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BG'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BF'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BB'), 0, udg_LocalPlayer)
    end
    SetPlayerTechMaxAllowedSwap(FourCC('R0B9'), 0, udg_LocalPlayer)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 0, udg_LocalPlayer)
end
--===========================================================================
function InitTrig_All_Gnomes_Begin()
    gg_trg_All_Gnomes_Begin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_All_Gnomes_Begin, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_All_Gnomes_Begin, Condition(Trig_All_Gnomes_Begin_Conditions))
    TriggerAddAction(gg_trg_All_Gnomes_Begin, Trig_All_Gnomes_Begin_Actions)
end
--===========================================================================
-- Trigger: All Gnomes
--===========================================================================
function Trig_All_Gnomes_Func001Func002C()
    return GetPlayerTechCountSimple(FourCC('R0BC'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BA'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0B5'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func003Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BD'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func003C()
    return GetPlayerTechCountSimple(FourCC('R0BI'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func004Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BF'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Func004C()
    return GetPlayerTechCountSimple(FourCC('R0BB'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Actions()
    if Trig_All_Gnomes_Func001C() then
        if Trig_All_Gnomes_Func001Func002C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BH'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BC'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BA'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0BE'), 1, udg_LocalPlayer)
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0B5'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Func003C() then
        if Trig_All_Gnomes_Func003Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BD'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BI'), 1, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Func004C() then
        if Trig_All_Gnomes_Func004Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BG'), 1, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BF'), 1, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BB'), 1, udg_LocalPlayer)
    end
    SetPlayerTechMaxAllowedSwap(FourCC('R0B9'), 1, udg_LocalPlayer)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 1, udg_LocalPlayer)
end
--===========================================================================
function InitTrig_All_Gnomes()
    gg_trg_All_Gnomes=CreateTrigger()
    TriggerAddAction(gg_trg_All_Gnomes, Trig_All_Gnomes_Actions)
end
--===========================================================================
-- Trigger: All Gnomes Off
--===========================================================================
function Trig_All_Gnomes_Off_Func001Func002C()
    return GetPlayerTechCountSimple(FourCC('R0BC'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BA'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0B5'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func003Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BD'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func003C()
    return GetPlayerTechCountSimple(FourCC('R0BI'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func004Func001C()
    return GetPlayerTechCountSimple(FourCC('R0BF'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Func004C()
    return GetPlayerTechCountSimple(FourCC('R0BB'), udg_LocalPlayer) == 1
end
function Trig_All_Gnomes_Off_Actions()
    if Trig_All_Gnomes_Off_Func001C() then
        if Trig_All_Gnomes_Off_Func001Func002C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BH'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BC'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BA'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Off_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0BE'), 0, udg_LocalPlayer)
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0B5'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Off_Func003C() then
        if Trig_All_Gnomes_Off_Func003Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0C0'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BD'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BI'), 0, udg_LocalPlayer)
    end
    if Trig_All_Gnomes_Off_Func004C() then
        if Trig_All_Gnomes_Off_Func004Func001C() then
            SetPlayerTechMaxAllowedSwap(FourCC('R0BG'), 0, udg_LocalPlayer)
        else
            SetPlayerTechMaxAllowedSwap(FourCC('R0BF'), 0, udg_LocalPlayer)
        end
    else
        SetPlayerTechMaxAllowedSwap(FourCC('R0BB'), 0, udg_LocalPlayer)
    end
    SetPlayerTechMaxAllowedSwap(FourCC('R0B9'), 0, udg_LocalPlayer)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C1'), 0, udg_LocalPlayer)
end
--===========================================================================
function InitTrig_All_Gnomes_Off()
    gg_trg_All_Gnomes_Off=CreateTrigger()
    TriggerAddAction(gg_trg_All_Gnomes_Off, Trig_All_Gnomes_Off_Actions)
end
--===========================================================================
-- Trigger: RegeNogi
--===========================================================================
function Trig_RegeNogi_Conditions()
    return GetResearched() == FourCC('R0B9')
end
function Trig_RegeNogi_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h0FP'), - 1, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_RegeNogi()
    gg_trg_RegeNogi=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RegeNogi, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_RegeNogi, Condition(Trig_RegeNogi_Conditions))
    TriggerAddAction(gg_trg_RegeNogi, Trig_RegeNogi_Actions)
end
--===========================================================================
-- Trigger: MehaWar start
--===========================================================================
function Trig_MehaWar_start_Conditions()
    return GetResearched() == FourCC('R0BA')
end
function Trig_MehaWar_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0G1'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaWar_start()
    gg_trg_MehaWar_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaWar_start, Condition(Trig_MehaWar_start_Conditions))
    TriggerAddAction(gg_trg_MehaWar_start, Trig_MehaWar_start_Actions)
end
--===========================================================================
-- Trigger: MehaWar Def
--===========================================================================
function Trig_MehaWar_Def_Conditions()
    return GetResearched() == FourCC('R0BQ')
end
function Trig_MehaWar_Def_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_MehaWar_Def()
    gg_trg_MehaWar_Def=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Def, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaWar_Def, Condition(Trig_MehaWar_Def_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Def, Trig_MehaWar_Def_Actions)
end
--===========================================================================
-- Trigger: MehaWar Def Beg
--===========================================================================
function Trig_MehaWar_Def_Beg_Conditions()
    return GetResearched() == FourCC('R0BQ')
end
function Trig_MehaWar_Def_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaWar_Def_Beg()
    gg_trg_MehaWar_Def_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Def_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MehaWar_Def_Beg, Condition(Trig_MehaWar_Def_Beg_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Def_Beg, Trig_MehaWar_Def_Beg_Actions)
end
--===========================================================================
-- Trigger: MehaWar Def Can
--===========================================================================
function Trig_MehaWar_Def_Can_Conditions()
    return GetResearched() == FourCC('R0BQ')
end
function Trig_MehaWar_Def_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BR'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaWar_Def_Can()
    gg_trg_MehaWar_Def_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Def_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MehaWar_Def_Can, Condition(Trig_MehaWar_Def_Can_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Def_Can, Trig_MehaWar_Def_Can_Actions)
end
--===========================================================================
-- Trigger: MehaWar Stan
--===========================================================================
function Trig_MehaWar_Stan_Conditions()
    return GetResearched() == FourCC('R0BR')
end
function Trig_MehaWar_Stan_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_MehaWar_Stan()
    gg_trg_MehaWar_Stan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Stan, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaWar_Stan, Condition(Trig_MehaWar_Stan_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Stan, Trig_MehaWar_Stan_Actions)
end
--===========================================================================
-- Trigger: MehaWar Stan Beg
--===========================================================================
function Trig_MehaWar_Stan_Beg_Conditions()
    return GetResearched() == FourCC('R0BR')
end
function Trig_MehaWar_Stan_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaWar_Stan_Beg()
    gg_trg_MehaWar_Stan_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Stan_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MehaWar_Stan_Beg, Condition(Trig_MehaWar_Stan_Beg_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Stan_Beg, Trig_MehaWar_Stan_Beg_Actions)
end
--===========================================================================
-- Trigger: MehaWar Stan Can
--===========================================================================
function Trig_MehaWar_Stan_Can_Conditions()
    return GetResearched() == FourCC('R0BR')
end
function Trig_MehaWar_Stan_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BQ'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaWar_Stan_Can()
    gg_trg_MehaWar_Stan_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaWar_Stan_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MehaWar_Stan_Can, Condition(Trig_MehaWar_Stan_Can_Conditions))
    TriggerAddAction(gg_trg_MehaWar_Stan_Can, Trig_MehaWar_Stan_Can_Actions)
end
--===========================================================================
-- Trigger: NanoGnom start
--===========================================================================
function Trig_NanoGnom_start_Conditions()
    return GetResearched() == FourCC('R0BC')
end
function Trig_NanoGnom_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C2'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C8'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0G2'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NanoGnom_start()
    gg_trg_NanoGnom_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnom_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NanoGnom_start, Condition(Trig_NanoGnom_start_Conditions))
    TriggerAddAction(gg_trg_NanoGnom_start, Trig_NanoGnom_start_Actions)
end
--===========================================================================
-- Trigger: NanoGnome1
--===========================================================================
function Trig_NanoGnome1_Conditions()
    return GetResearched() == FourCC('R0C2')
end
function Trig_NanoGnome1_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A16A'), GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_NanoGnome1()
    gg_trg_NanoGnome1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NanoGnome1, Condition(Trig_NanoGnome1_Conditions))
    TriggerAddAction(gg_trg_NanoGnome1, Trig_NanoGnome1_Actions)
end
--===========================================================================
-- Trigger: NanoGnome1 Beg
--===========================================================================
function Trig_NanoGnome1_Beg_Conditions()
    return GetResearched() == FourCC('R0C2')
end
function Trig_NanoGnome1_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C8'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NanoGnome1_Beg()
    gg_trg_NanoGnome1_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome1_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_NanoGnome1_Beg, Condition(Trig_NanoGnome1_Beg_Conditions))
    TriggerAddAction(gg_trg_NanoGnome1_Beg, Trig_NanoGnome1_Beg_Actions)
end
--===========================================================================
-- Trigger: NanoGnome1 Can
--===========================================================================
function Trig_NanoGnome1_Can_Conditions()
    return GetResearched() == FourCC('R0C2')
end
function Trig_NanoGnome1_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C8'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NanoGnome1_Can()
    gg_trg_NanoGnome1_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome1_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_NanoGnome1_Can, Condition(Trig_NanoGnome1_Can_Conditions))
    TriggerAddAction(gg_trg_NanoGnome1_Can, Trig_NanoGnome1_Can_Actions)
end
--===========================================================================
-- Trigger: NanoGnome 2
--===========================================================================
function Trig_NanoGnome_2_Conditions()
    return GetResearched() == FourCC('R0C8')
end
function Trig_NanoGnome_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_NanoGnome_2()
    gg_trg_NanoGnome_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_NanoGnome_2, Condition(Trig_NanoGnome_2_Conditions))
    TriggerAddAction(gg_trg_NanoGnome_2, Trig_NanoGnome_2_Actions)
end
--===========================================================================
-- Trigger: NanoGnome 2 can
--===========================================================================
function Trig_NanoGnome_2_can_Conditions()
    return GetResearched() == FourCC('R0C8')
end
function Trig_NanoGnome_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C2'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NanoGnome_2_can()
    gg_trg_NanoGnome_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_NanoGnome_2_can, Condition(Trig_NanoGnome_2_can_Conditions))
    TriggerAddAction(gg_trg_NanoGnome_2_can, Trig_NanoGnome_2_can_Actions)
end
--===========================================================================
-- Trigger: NanoGnome 2 beg
--===========================================================================
function Trig_NanoGnome_2_beg_Conditions()
    return GetResearched() == FourCC('R0C8')
end
function Trig_NanoGnome_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C2'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_NanoGnome_2_beg()
    gg_trg_NanoGnome_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NanoGnome_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_NanoGnome_2_beg, Condition(Trig_NanoGnome_2_beg_Conditions))
    TriggerAddAction(gg_trg_NanoGnome_2_beg, Trig_NanoGnome_2_beg_Actions)
end
--===========================================================================
-- Trigger: MehaGigant
--===========================================================================
function Trig_MehaGigant_Conditions()
    return GetResearched() == FourCC('R0BH')
end
function Trig_MehaGigant_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0CP'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CQ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FW'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaGigant()
    gg_trg_MehaGigant=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaGigant, Condition(Trig_MehaGigant_Conditions))
    TriggerAddAction(gg_trg_MehaGigant, Trig_MehaGigant_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 1
--===========================================================================
function Trig_MehaGigant_1_Conditions()
    return GetResearched() == FourCC('R0CP')
end
function Trig_MehaGigant_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_MehaGigant_1()
    gg_trg_MehaGigant_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaGigant_1, Condition(Trig_MehaGigant_1_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_1, Trig_MehaGigant_1_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 1 Can
--===========================================================================
function Trig_MehaGigant_1_Can_Conditions()
    return GetResearched() == FourCC('R0CP')
end
function Trig_MehaGigant_1_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CQ'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaGigant_1_Can()
    gg_trg_MehaGigant_1_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_1_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MehaGigant_1_Can, Condition(Trig_MehaGigant_1_Can_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_1_Can, Trig_MehaGigant_1_Can_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 1 Beg
--===========================================================================
function Trig_MehaGigant_1_Beg_Conditions()
    return GetResearched() == FourCC('R0CP')
end
function Trig_MehaGigant_1_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CQ'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaGigant_1_Beg()
    gg_trg_MehaGigant_1_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_1_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MehaGigant_1_Beg, Condition(Trig_MehaGigant_1_Beg_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_1_Beg, Trig_MehaGigant_1_Beg_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 2
--===========================================================================
function Trig_MehaGigant_2_Conditions()
    return GetResearched() == FourCC('R0CQ')
end
function Trig_MehaGigant_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CP'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailableBJ(true, FourCC('A0U8'), GetOwningPlayer(GetTriggerUnit()))
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_MehaGigant_2()
    gg_trg_MehaGigant_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MehaGigant_2, Condition(Trig_MehaGigant_2_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_2, Trig_MehaGigant_2_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 2 Can
--===========================================================================
function Trig_MehaGigant_2_Can_Conditions()
    return GetResearched() == FourCC('R0CQ')
end
function Trig_MehaGigant_2_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CP'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaGigant_2_Can()
    gg_trg_MehaGigant_2_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_2_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_MehaGigant_2_Can, Condition(Trig_MehaGigant_2_Can_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_2_Can, Trig_MehaGigant_2_Can_Actions)
end
--===========================================================================
-- Trigger: MehaGigant 2 Beg
--===========================================================================
function Trig_MehaGigant_2_Beg_Conditions()
    return GetResearched() == FourCC('R0CQ')
end
function Trig_MehaGigant_2_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CP'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MehaGigant_2_Beg()
    gg_trg_MehaGigant_2_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MehaGigant_2_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_MehaGigant_2_Beg, Condition(Trig_MehaGigant_2_Beg_Conditions))
    TriggerAddAction(gg_trg_MehaGigant_2_Beg, Trig_MehaGigant_2_Beg_Actions)
end
--===========================================================================
-- Trigger: Spider start
--===========================================================================
function Trig_Spider_start_Conditions()
    return GetResearched() == FourCC('R0B5')
end
function Trig_Spider_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0CR'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CS'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FV'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Spider_start()
    gg_trg_Spider_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Spider_start, Condition(Trig_Spider_start_Conditions))
    TriggerAddAction(gg_trg_Spider_start, Trig_Spider_start_Actions)
end
--===========================================================================
-- Trigger: Spider 1
--===========================================================================
function Trig_Spider_1_Conditions()
    return GetResearched() == FourCC('R0CR')
end
function Trig_Spider_1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CS'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Spider_1()
    gg_trg_Spider_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Spider_1, Condition(Trig_Spider_1_Conditions))
    TriggerAddAction(gg_trg_Spider_1, Trig_Spider_1_Actions)
end
--===========================================================================
-- Trigger: Spider 1 Beg
--===========================================================================
function Trig_Spider_1_Beg_Conditions()
    return GetResearched() == FourCC('R0CR')
end
function Trig_Spider_1_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CS'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Spider_1_Beg()
    gg_trg_Spider_1_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_1_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Spider_1_Beg, Condition(Trig_Spider_1_Beg_Conditions))
    TriggerAddAction(gg_trg_Spider_1_Beg, Trig_Spider_1_Beg_Actions)
end
--===========================================================================
-- Trigger: Spider 1 Can
--===========================================================================
function Trig_Spider_1_Can_Conditions()
    return GetResearched() == FourCC('R0CR')
end
function Trig_Spider_1_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CS'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Spider_1_Can()
    gg_trg_Spider_1_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_1_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Spider_1_Can, Condition(Trig_Spider_1_Can_Conditions))
    TriggerAddAction(gg_trg_Spider_1_Can, Trig_Spider_1_Can_Actions)
end
--===========================================================================
-- Trigger: Spider 2
--===========================================================================
function Trig_Spider_2_Conditions()
    return GetResearched() == FourCC('R0CS')
end
function Trig_Spider_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CR'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Spider_2()
    gg_trg_Spider_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Spider_2, Condition(Trig_Spider_2_Conditions))
    TriggerAddAction(gg_trg_Spider_2, Trig_Spider_2_Actions)
end
--===========================================================================
-- Trigger: Spider 2 Beg
--===========================================================================
function Trig_Spider_2_Beg_Conditions()
    return GetResearched() == FourCC('R0CS')
end
function Trig_Spider_2_Beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CR'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Spider_2_Beg()
    gg_trg_Spider_2_Beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_2_Beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Spider_2_Beg, Condition(Trig_Spider_2_Beg_Conditions))
    TriggerAddAction(gg_trg_Spider_2_Beg, Trig_Spider_2_Beg_Actions)
end
--===========================================================================
-- Trigger: Spider 2 Can
--===========================================================================
function Trig_Spider_2_Can_Conditions()
    return GetResearched() == FourCC('R0CS')
end
function Trig_Spider_2_Can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CR'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Spider_2_Can()
    gg_trg_Spider_2_Can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spider_2_Can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Spider_2_Can, Condition(Trig_Spider_2_Can_Conditions))
    TriggerAddAction(gg_trg_Spider_2_Can, Trig_Spider_2_Can_Actions)
end
--===========================================================================
-- Trigger: Chahohod Start
--===========================================================================
function Trig_Chahohod_Start_Conditions()
    return GetResearched() == FourCC('R0BE')
end
function Trig_Chahohod_Start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('h0FH'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_Start()
    gg_trg_Chahohod_Start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_Start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Chahohod_Start, Condition(Trig_Chahohod_Start_Conditions))
    TriggerAddAction(gg_trg_Chahohod_Start, Trig_Chahohod_Start_Actions)
end
--===========================================================================
-- Trigger: Chahohod 1
--===========================================================================
function Trig_Chahohod_1_Conditions()
    return GetResearched() == FourCC('R0CF')
end
function Trig_Chahohod_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
    SetPlayerAbilityAvailableBJ(true, FourCC('A0SO'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_1()
    gg_trg_Chahohod_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Chahohod_1, Condition(Trig_Chahohod_1_Conditions))
    TriggerAddAction(gg_trg_Chahohod_1, Trig_Chahohod_1_Actions)
end
--===========================================================================
-- Trigger: Chahohod 1 beg
--===========================================================================
function Trig_Chahohod_1_beg_Conditions()
    return GetResearched() == FourCC('R0CF')
end
function Trig_Chahohod_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_1_beg()
    gg_trg_Chahohod_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Chahohod_1_beg, Condition(Trig_Chahohod_1_beg_Conditions))
    TriggerAddAction(gg_trg_Chahohod_1_beg, Trig_Chahohod_1_beg_Actions)
end
--===========================================================================
-- Trigger: Chahohod 1 can
--===========================================================================
function Trig_Chahohod_1_can_Conditions()
    return GetResearched() == FourCC('R0CF')
end
function Trig_Chahohod_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_1_can()
    gg_trg_Chahohod_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Chahohod_1_can, Condition(Trig_Chahohod_1_can_Conditions))
    TriggerAddAction(gg_trg_Chahohod_1_can, Trig_Chahohod_1_can_Actions)
end
--===========================================================================
-- Trigger: Chahohod 2
--===========================================================================
function Trig_Chahohod_2_Conditions()
    return GetResearched() == FourCC('R0CG')
end
function Trig_Chahohod_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
    SetPlayerAbilityAvailableBJ(true, FourCC('A0SN'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_2()
    gg_trg_Chahohod_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Chahohod_2, Condition(Trig_Chahohod_2_Conditions))
    TriggerAddAction(gg_trg_Chahohod_2, Trig_Chahohod_2_Actions)
end
--===========================================================================
-- Trigger: Chahohod 2 beg
--===========================================================================
function Trig_Chahohod_2_beg_Conditions()
    return GetResearched() == FourCC('R0CG')
end
function Trig_Chahohod_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_2_beg()
    gg_trg_Chahohod_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Chahohod_2_beg, Condition(Trig_Chahohod_2_beg_Conditions))
    TriggerAddAction(gg_trg_Chahohod_2_beg, Trig_Chahohod_2_beg_Actions)
end
--===========================================================================
-- Trigger: Chahohod 2 can
--===========================================================================
function Trig_Chahohod_2_can_Conditions()
    return GetResearched() == FourCC('R0CG')
end
function Trig_Chahohod_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C7'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_2_can()
    gg_trg_Chahohod_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Chahohod_2_can, Condition(Trig_Chahohod_2_can_Conditions))
    TriggerAddAction(gg_trg_Chahohod_2_can, Trig_Chahohod_2_can_Actions)
end
--===========================================================================
-- Trigger: Chahohod 3
--===========================================================================
function Trig_Chahohod_3_Conditions()
    return GetResearched() == FourCC('R0C7')
end
function Trig_Chahohod_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Chahohod_3()
    gg_trg_Chahohod_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Chahohod_3, Condition(Trig_Chahohod_3_Conditions))
    TriggerAddAction(gg_trg_Chahohod_3, Trig_Chahohod_3_Actions)
end
--===========================================================================
-- Trigger: Chahohod 3 beg
--===========================================================================
function Trig_Chahohod_3_beg_Conditions()
    return GetResearched() == FourCC('R0C7')
end
function Trig_Chahohod_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_3_beg()
    gg_trg_Chahohod_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Chahohod_3_beg, Condition(Trig_Chahohod_3_beg_Conditions))
    TriggerAddAction(gg_trg_Chahohod_3_beg, Trig_Chahohod_3_beg_Actions)
end
--===========================================================================
-- Trigger: Chahohod 3 beg Copy
--===========================================================================
function Trig_Chahohod_3_beg_Copy_Conditions()
    return GetResearched() == FourCC('R0C7')
end
function Trig_Chahohod_3_beg_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CF'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CG'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Chahohod_3_beg_Copy()
    gg_trg_Chahohod_3_beg_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Chahohod_3_beg_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Chahohod_3_beg_Copy, Condition(Trig_Chahohod_3_beg_Copy_Conditions))
    TriggerAddAction(gg_trg_Chahohod_3_beg_Copy, Trig_Chahohod_3_beg_Copy_Actions)
end
--===========================================================================
-- Trigger: Minitank Start
--===========================================================================
function Trig_Minitank_Start_Conditions()
    return GetResearched() == FourCC('R0BB')
end
function Trig_Minitank_Start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FN'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_Start()
    gg_trg_Minitank_Start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_Start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Minitank_Start, Condition(Trig_Minitank_Start_Conditions))
    TriggerAddAction(gg_trg_Minitank_Start, Trig_Minitank_Start_Actions)
end
--===========================================================================
-- Trigger: Minitank 1
--===========================================================================
function Trig_Minitank_1_Conditions()
    return GetResearched() == FourCC('R0C5')
end
function Trig_Minitank_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Minitank_1()
    gg_trg_Minitank_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Minitank_1, Condition(Trig_Minitank_1_Conditions))
    TriggerAddAction(gg_trg_Minitank_1, Trig_Minitank_1_Actions)
end
--===========================================================================
-- Trigger: Minitank 1 can
--===========================================================================
function Trig_Minitank_1_can_Conditions()
    return GetResearched() == FourCC('R0C5')
end
function Trig_Minitank_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_1_can()
    gg_trg_Minitank_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Minitank_1_can, Condition(Trig_Minitank_1_can_Conditions))
    TriggerAddAction(gg_trg_Minitank_1_can, Trig_Minitank_1_can_Actions)
end
--===========================================================================
-- Trigger: Minitank 1 beg
--===========================================================================
function Trig_Minitank_1_beg_Conditions()
    return GetResearched() == FourCC('R0C5')
end
function Trig_Minitank_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_1_beg()
    gg_trg_Minitank_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Minitank_1_beg, Condition(Trig_Minitank_1_beg_Conditions))
    TriggerAddAction(gg_trg_Minitank_1_beg, Trig_Minitank_1_beg_Actions)
end
--===========================================================================
-- Trigger: Minitank 2
--===========================================================================
function Trig_Minitank_2_Conditions()
    return GetResearched() == FourCC('R0C6')
end
function Trig_Minitank_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Minitank_2()
    gg_trg_Minitank_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Minitank_2, Condition(Trig_Minitank_2_Conditions))
    TriggerAddAction(gg_trg_Minitank_2, Trig_Minitank_2_Actions)
end
--===========================================================================
-- Trigger: Minitank 2 can
--===========================================================================
function Trig_Minitank_2_can_Conditions()
    return GetResearched() == FourCC('R0C6')
end
function Trig_Minitank_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_2_can()
    gg_trg_Minitank_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Minitank_2_can, Condition(Trig_Minitank_2_can_Conditions))
    TriggerAddAction(gg_trg_Minitank_2_can, Trig_Minitank_2_can_Actions)
end
--===========================================================================
-- Trigger: Minitank 2 beg
--===========================================================================
function Trig_Minitank_2_beg_Conditions()
    return GetResearched() == FourCC('R0C6')
end
function Trig_Minitank_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BT'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_2_beg()
    gg_trg_Minitank_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Minitank_2_beg, Condition(Trig_Minitank_2_beg_Conditions))
    TriggerAddAction(gg_trg_Minitank_2_beg, Trig_Minitank_2_beg_Actions)
end
--===========================================================================
-- Trigger: Minitank 3
--===========================================================================
function Trig_Minitank_3_Conditions()
    return GetResearched() == FourCC('R0BT')
end
function Trig_Minitank_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Minitank_3()
    gg_trg_Minitank_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Minitank_3, Condition(Trig_Minitank_3_Conditions))
    TriggerAddAction(gg_trg_Minitank_3, Trig_Minitank_3_Actions)
end
--===========================================================================
-- Trigger: Minitank 3 can
--===========================================================================
function Trig_Minitank_3_can_Conditions()
    return GetResearched() == FourCC('R0BT')
end
function Trig_Minitank_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_3_can()
    gg_trg_Minitank_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Minitank_3_can, Condition(Trig_Minitank_3_can_Conditions))
    TriggerAddAction(gg_trg_Minitank_3_can, Trig_Minitank_3_can_Actions)
end
--===========================================================================
-- Trigger: Minitank 3 beg
--===========================================================================
function Trig_Minitank_3_beg_Conditions()
    return GetResearched() == FourCC('R0BT')
end
function Trig_Minitank_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C5'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C6'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Minitank_3_beg()
    gg_trg_Minitank_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Minitank_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Minitank_3_beg, Condition(Trig_Minitank_3_beg_Conditions))
    TriggerAddAction(gg_trg_Minitank_3_beg, Trig_Minitank_3_beg_Actions)
end
--===========================================================================
-- Trigger: UniTank start
--===========================================================================
function Trig_UniTank_start_Conditions()
    return GetResearched() == FourCC('R0BF')
end
function Trig_UniTank_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FF'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_start()
    gg_trg_UniTank_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_UniTank_start, Condition(Trig_UniTank_start_Conditions))
    TriggerAddAction(gg_trg_UniTank_start, Trig_UniTank_start_Actions)
end
--===========================================================================
-- Trigger: UniTank 1
--===========================================================================
function Trig_UniTank_1_Conditions()
    return GetResearched() == FourCC('R0CC')
end
function Trig_UniTank_1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_UniTank_1()
    gg_trg_UniTank_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_UniTank_1, Condition(Trig_UniTank_1_Conditions))
    TriggerAddAction(gg_trg_UniTank_1, Trig_UniTank_1_Actions)
end
--===========================================================================
-- Trigger: UniTank 1 can
--===========================================================================
function Trig_UniTank_1_can_Conditions()
    return GetResearched() == FourCC('R0CC')
end
function Trig_UniTank_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_1_can()
    gg_trg_UniTank_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_UniTank_1_can, Condition(Trig_UniTank_1_can_Conditions))
    TriggerAddAction(gg_trg_UniTank_1_can, Trig_UniTank_1_can_Actions)
end
--===========================================================================
-- Trigger: UniTank 1 beg
--===========================================================================
function Trig_UniTank_1_beg_Conditions()
    return GetResearched() == FourCC('R0CC')
end
function Trig_UniTank_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_1_beg()
    gg_trg_UniTank_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_UniTank_1_beg, Condition(Trig_UniTank_1_beg_Conditions))
    TriggerAddAction(gg_trg_UniTank_1_beg, Trig_UniTank_1_beg_Actions)
end
--===========================================================================
-- Trigger: UniTank 2
--===========================================================================
function Trig_UniTank_2_Conditions()
    return GetResearched() == FourCC('R0CD')
end
function Trig_UniTank_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_UniTank_2()
    gg_trg_UniTank_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_UniTank_2, Condition(Trig_UniTank_2_Conditions))
    TriggerAddAction(gg_trg_UniTank_2, Trig_UniTank_2_Actions)
end
--===========================================================================
-- Trigger: UniTank 2 can
--===========================================================================
function Trig_UniTank_2_can_Conditions()
    return GetResearched() == FourCC('R0CD')
end
function Trig_UniTank_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_2_can()
    gg_trg_UniTank_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_UniTank_2_can, Condition(Trig_UniTank_2_can_Conditions))
    TriggerAddAction(gg_trg_UniTank_2_can, Trig_UniTank_2_can_Actions)
end
--===========================================================================
-- Trigger: UniTank 2 beg
--===========================================================================
function Trig_UniTank_2_beg_Conditions()
    return GetResearched() == FourCC('R0CD')
end
function Trig_UniTank_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CE'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_2_beg()
    gg_trg_UniTank_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_UniTank_2_beg, Condition(Trig_UniTank_2_beg_Conditions))
    TriggerAddAction(gg_trg_UniTank_2_beg, Trig_UniTank_2_beg_Actions)
end
--===========================================================================
-- Trigger: UniTank 3
--===========================================================================
function Trig_UniTank_3_Conditions()
    return GetResearched() == FourCC('R0CE')
end
function Trig_UniTank_3_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_UniTank_3()
    gg_trg_UniTank_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_UniTank_3, Condition(Trig_UniTank_3_Conditions))
    TriggerAddAction(gg_trg_UniTank_3, Trig_UniTank_3_Actions)
end
--===========================================================================
-- Trigger: UniTank 3 can
--===========================================================================
function Trig_UniTank_3_can_Conditions()
    return GetResearched() == FourCC('R0CE')
end
function Trig_UniTank_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_3_can()
    gg_trg_UniTank_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_UniTank_3_can, Condition(Trig_UniTank_3_can_Conditions))
    TriggerAddAction(gg_trg_UniTank_3_can, Trig_UniTank_3_can_Actions)
end
--===========================================================================
-- Trigger: UniTank 3 beg
--===========================================================================
function Trig_UniTank_3_beg_Conditions()
    return GetResearched() == FourCC('R0CE')
end
function Trig_UniTank_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CD'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CC'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_UniTank_3_beg()
    gg_trg_UniTank_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UniTank_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_UniTank_3_beg, Condition(Trig_UniTank_3_beg_Conditions))
    TriggerAddAction(gg_trg_UniTank_3_beg, Trig_UniTank_3_beg_Actions)
end
--===========================================================================
-- Trigger: Venec Tank start
--===========================================================================
function Trig_Venec_Tank_start_Conditions()
    return GetResearched() == FourCC('R0BG')
end
function Trig_Venec_Tank_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FG'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_start()
    gg_trg_Venec_Tank_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Venec_Tank_start, Condition(Trig_Venec_Tank_start_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_start, Trig_Venec_Tank_start_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 1
--===========================================================================
function Trig_Venec_Tank_1_Conditions()
    return GetResearched() == FourCC('R0C9')
end
function Trig_Venec_Tank_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Venec_Tank_1()
    gg_trg_Venec_Tank_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Venec_Tank_1, Condition(Trig_Venec_Tank_1_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_1, Trig_Venec_Tank_1_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 1 can
--===========================================================================
function Trig_Venec_Tank_1_can_Conditions()
    return GetResearched() == FourCC('R0C9')
end
function Trig_Venec_Tank_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_1_can()
    gg_trg_Venec_Tank_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Venec_Tank_1_can, Condition(Trig_Venec_Tank_1_can_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_1_can, Trig_Venec_Tank_1_can_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 1 beg
--===========================================================================
function Trig_Venec_Tank_1_beg_Conditions()
    return GetResearched() == FourCC('R0C9')
end
function Trig_Venec_Tank_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_1_beg()
    gg_trg_Venec_Tank_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Venec_Tank_1_beg, Condition(Trig_Venec_Tank_1_beg_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_1_beg, Trig_Venec_Tank_1_beg_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 2
--===========================================================================
function Trig_Venec_Tank_2_Conditions()
    return GetResearched() == FourCC('R0CA')
end
function Trig_Venec_Tank_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Venec_Tank_2()
    gg_trg_Venec_Tank_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Venec_Tank_2, Condition(Trig_Venec_Tank_2_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_2, Trig_Venec_Tank_2_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 2 can
--===========================================================================
function Trig_Venec_Tank_2_can_Conditions()
    return GetResearched() == FourCC('R0CA')
end
function Trig_Venec_Tank_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_2_can()
    gg_trg_Venec_Tank_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Venec_Tank_2_can, Condition(Trig_Venec_Tank_2_can_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_2_can, Trig_Venec_Tank_2_can_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 2 beg
--===========================================================================
function Trig_Venec_Tank_2_beg_Conditions()
    return GetResearched() == FourCC('R0CA')
end
function Trig_Venec_Tank_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CB'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_2_beg()
    gg_trg_Venec_Tank_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Venec_Tank_2_beg, Condition(Trig_Venec_Tank_2_beg_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_2_beg, Trig_Venec_Tank_2_beg_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 3
--===========================================================================
function Trig_Venec_Tank_3_Conditions()
    return GetResearched() == FourCC('R0CB')
end
function Trig_Venec_Tank_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Venec_Tank_3()
    gg_trg_Venec_Tank_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Venec_Tank_3, Condition(Trig_Venec_Tank_3_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_3, Trig_Venec_Tank_3_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 3 can
--===========================================================================
function Trig_Venec_Tank_3_can_Conditions()
    return GetResearched() == FourCC('R0CB')
end
function Trig_Venec_Tank_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_3_can()
    gg_trg_Venec_Tank_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Venec_Tank_3_can, Condition(Trig_Venec_Tank_3_can_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_3_can, Trig_Venec_Tank_3_can_Actions)
end
--===========================================================================
-- Trigger: Venec Tank 3 beg
--===========================================================================
function Trig_Venec_Tank_3_beg_Conditions()
    return GetResearched() == FourCC('R0CB')
end
function Trig_Venec_Tank_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CA'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C9'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Venec_Tank_3_beg()
    gg_trg_Venec_Tank_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Venec_Tank_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Venec_Tank_3_beg, Condition(Trig_Venec_Tank_3_beg_Conditions))
    TriggerAddAction(gg_trg_Venec_Tank_3_beg, Trig_Venec_Tank_3_beg_Actions)
end
--===========================================================================
-- Trigger: Car start
--===========================================================================
function Trig_Car_start_Conditions()
    return GetResearched() == FourCC('R0BI')
end
function Trig_Car_start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FQ'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_start()
    gg_trg_Car_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car_start, Condition(Trig_Car_start_Conditions))
    TriggerAddAction(gg_trg_Car_start, Trig_Car_start_Actions)
end
--===========================================================================
-- Trigger: Car 1
--===========================================================================
function Trig_Car_1_Conditions()
    return GetResearched() == FourCC('R0CJ')
end
function Trig_Car_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Car_1()
    gg_trg_Car_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car_1, Condition(Trig_Car_1_Conditions))
    TriggerAddAction(gg_trg_Car_1, Trig_Car_1_Actions)
end
--===========================================================================
-- Trigger: Car 1 can
--===========================================================================
function Trig_Car_1_can_Conditions()
    return GetResearched() == FourCC('R0CJ')
end
function Trig_Car_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_1_can()
    gg_trg_Car_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Car_1_can, Condition(Trig_Car_1_can_Conditions))
    TriggerAddAction(gg_trg_Car_1_can, Trig_Car_1_can_Actions)
end
--===========================================================================
-- Trigger: Car 1 beg
--===========================================================================
function Trig_Car_1_beg_Conditions()
    return GetResearched() == FourCC('R0CJ')
end
function Trig_Car_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_1_beg()
    gg_trg_Car_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Car_1_beg, Condition(Trig_Car_1_beg_Conditions))
    TriggerAddAction(gg_trg_Car_1_beg, Trig_Car_1_beg_Actions)
end
--===========================================================================
-- Trigger: Car 2
--===========================================================================
function Trig_Car_2_Conditions()
    return GetResearched() == FourCC('R0CK')
end
function Trig_Car_2_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0TL'), GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Car_2()
    gg_trg_Car_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car_2, Condition(Trig_Car_2_Conditions))
    TriggerAddAction(gg_trg_Car_2, Trig_Car_2_Actions)
end
--===========================================================================
-- Trigger: Car 2 can
--===========================================================================
function Trig_Car_2_can_Conditions()
    return GetResearched() == FourCC('R0CK')
end
function Trig_Car_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_2_can()
    gg_trg_Car_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Car_2_can, Condition(Trig_Car_2_can_Conditions))
    TriggerAddAction(gg_trg_Car_2_can, Trig_Car_2_can_Actions)
end
--===========================================================================
-- Trigger: Car 2 beg
--===========================================================================
function Trig_Car_2_beg_Conditions()
    return GetResearched() == FourCC('R0CK')
end
function Trig_Car_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CL'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_2_beg()
    gg_trg_Car_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Car_2_beg, Condition(Trig_Car_2_beg_Conditions))
    TriggerAddAction(gg_trg_Car_2_beg, Trig_Car_2_beg_Actions)
end
--===========================================================================
-- Trigger: Car 3
--===========================================================================
function Trig_Car_3_Conditions()
    return GetResearched() == FourCC('R0CL')
end
function Trig_Car_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Car_3()
    gg_trg_Car_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Car_3, Condition(Trig_Car_3_Conditions))
    TriggerAddAction(gg_trg_Car_3, Trig_Car_3_Actions)
end
--===========================================================================
-- Trigger: Car 3 can
--===========================================================================
function Trig_Car_3_can_Conditions()
    return GetResearched() == FourCC('R0CL')
end
function Trig_Car_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_3_can()
    gg_trg_Car_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Car_3_can, Condition(Trig_Car_3_can_Conditions))
    TriggerAddAction(gg_trg_Car_3_can, Trig_Car_3_can_Actions)
end
--===========================================================================
-- Trigger: Car 3 beg
--===========================================================================
function Trig_Car_3_beg_Conditions()
    return GetResearched() == FourCC('R0CL')
end
function Trig_Car_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CK'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Car_3_beg()
    gg_trg_Car_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Car_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Car_3_beg, Condition(Trig_Car_3_beg_Conditions))
    TriggerAddAction(gg_trg_Car_3_beg, Trig_Car_3_beg_Actions)
end
--===========================================================================
-- Trigger: SGT Start
--===========================================================================
function Trig_SGT_Start_Conditions()
    return GetResearched() == FourCC('R0BD')
end
function Trig_SGT_Start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('h0FO'), - 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_Start()
    gg_trg_SGT_Start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_Start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SGT_Start, Condition(Trig_SGT_Start_Conditions))
    TriggerAddAction(gg_trg_SGT_Start, Trig_SGT_Start_Actions)
end
--===========================================================================
-- Trigger: SGT 1
--===========================================================================
function Trig_SGT_1_Conditions()
    return GetResearched() == FourCC('R0CH')
end
function Trig_SGT_1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_SGT_1()
    gg_trg_SGT_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SGT_1, Condition(Trig_SGT_1_Conditions))
    TriggerAddAction(gg_trg_SGT_1, Trig_SGT_1_Actions)
end
--===========================================================================
-- Trigger: SGT 1 can
--===========================================================================
function Trig_SGT_1_can_Conditions()
    return GetResearched() == FourCC('R0CH')
end
function Trig_SGT_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_1_can()
    gg_trg_SGT_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SGT_1_can, Condition(Trig_SGT_1_can_Conditions))
    TriggerAddAction(gg_trg_SGT_1_can, Trig_SGT_1_can_Actions)
end
--===========================================================================
-- Trigger: SGT 1 beg
--===========================================================================
function Trig_SGT_1_beg_Conditions()
    return GetResearched() == FourCC('R0CH')
end
function Trig_SGT_1_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_1_beg()
    gg_trg_SGT_1_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_1_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SGT_1_beg, Condition(Trig_SGT_1_beg_Conditions))
    TriggerAddAction(gg_trg_SGT_1_beg, Trig_SGT_1_beg_Actions)
end
--===========================================================================
-- Trigger: SGT 2
--===========================================================================
function Trig_SGT_2_Conditions()
    return GetResearched() == FourCC('R0CI')
end
function Trig_SGT_2_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0U9'), GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_SGT_2()
    gg_trg_SGT_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SGT_2, Condition(Trig_SGT_2_Conditions))
    TriggerAddAction(gg_trg_SGT_2, Trig_SGT_2_Actions)
end
--===========================================================================
-- Trigger: SGT 2can
--===========================================================================
function Trig_SGT_2can_Conditions()
    return GetResearched() == FourCC('R0CI')
end
function Trig_SGT_2can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_2can()
    gg_trg_SGT_2can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_2can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SGT_2can, Condition(Trig_SGT_2can_Conditions))
    TriggerAddAction(gg_trg_SGT_2can, Trig_SGT_2can_Actions)
end
--===========================================================================
-- Trigger: SGT 2 beg
--===========================================================================
function Trig_SGT_2_beg_Conditions()
    return GetResearched() == FourCC('R0CI')
end
function Trig_SGT_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CM'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_2_beg()
    gg_trg_SGT_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SGT_2_beg, Condition(Trig_SGT_2_beg_Conditions))
    TriggerAddAction(gg_trg_SGT_2_beg, Trig_SGT_2_beg_Actions)
end
--===========================================================================
-- Trigger: SGT 3
--===========================================================================
function Trig_SGT_3_Conditions()
    return GetResearched() == FourCC('R0CM')
end
function Trig_SGT_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
    SetPlayerAbilityAvailableBJ(true, FourCC('A0UA'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_3()
    gg_trg_SGT_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SGT_3, Condition(Trig_SGT_3_Conditions))
    TriggerAddAction(gg_trg_SGT_3, Trig_SGT_3_Actions)
end
--===========================================================================
-- Trigger: SGT 3 can
--===========================================================================
function Trig_SGT_3_can_Conditions()
    return GetResearched() == FourCC('R0CM')
end
function Trig_SGT_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_3_can()
    gg_trg_SGT_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SGT_3_can, Condition(Trig_SGT_3_can_Conditions))
    TriggerAddAction(gg_trg_SGT_3_can, Trig_SGT_3_can_Actions)
end
--===========================================================================
-- Trigger: SGT 3 beg
--===========================================================================
function Trig_SGT_3_beg_Conditions()
    return GetResearched() == FourCC('R0CM')
end
function Trig_SGT_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CI'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CH'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SGT_3_beg()
    gg_trg_SGT_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SGT_3_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SGT_3_beg, Condition(Trig_SGT_3_beg_Conditions))
    TriggerAddAction(gg_trg_SGT_3_beg, Trig_SGT_3_beg_Actions)
end
--===========================================================================
-- Trigger: SAU Start
--===========================================================================
function Trig_SAU_Start_Conditions()
    return GetResearched() == FourCC('R0C0')
end
function Trig_SAU_Start_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes_Off)
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FJ'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_Start()
    gg_trg_SAU_Start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_Start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SAU_Start, Condition(Trig_SAU_Start_Conditions))
    TriggerAddAction(gg_trg_SAU_Start, Trig_SAU_Start_Actions)
end
--===========================================================================
-- Trigger: SAU 1
--===========================================================================
function Trig_SAU_1_Conditions()
    return GetResearched() == FourCC('R0CN')
end
function Trig_SAU_1_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_SAU_1()
    gg_trg_SAU_1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SAU_1, Condition(Trig_SAU_1_Conditions))
    TriggerAddAction(gg_trg_SAU_1, Trig_SAU_1_Actions)
end
--===========================================================================
-- Trigger: SAU 1 can
--===========================================================================
function Trig_SAU_1_can_Conditions()
    return GetResearched() == FourCC('R0CN')
end
function Trig_SAU_1_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_1_can()
    gg_trg_SAU_1_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_1_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SAU_1_can, Condition(Trig_SAU_1_can_Conditions))
    TriggerAddAction(gg_trg_SAU_1_can, Trig_SAU_1_can_Actions)
end
--===========================================================================
-- Trigger: SAU 1  beg
--===========================================================================
function Trig_SAU_1__beg_Conditions()
    return GetResearched() == FourCC('R0CN')
end
function Trig_SAU_1__beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_1__beg()
    gg_trg_SAU_1__beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_1__beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SAU_1__beg, Condition(Trig_SAU_1__beg_Conditions))
    TriggerAddAction(gg_trg_SAU_1__beg, Trig_SAU_1__beg_Actions)
end
--===========================================================================
-- Trigger: SAU 2
--===========================================================================
function Trig_SAU_2_Conditions()
    return GetResearched() == FourCC('R0CO')
end
function Trig_SAU_2_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_SAU_2()
    gg_trg_SAU_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SAU_2, Condition(Trig_SAU_2_Conditions))
    TriggerAddAction(gg_trg_SAU_2, Trig_SAU_2_Actions)
end
--===========================================================================
-- Trigger: SAU 2 can
--===========================================================================
function Trig_SAU_2_can_Conditions()
    return GetResearched() == FourCC('R0CO')
end
function Trig_SAU_2_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_2_can()
    gg_trg_SAU_2_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_2_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SAU_2_can, Condition(Trig_SAU_2_can_Conditions))
    TriggerAddAction(gg_trg_SAU_2_can, Trig_SAU_2_can_Actions)
end
--===========================================================================
-- Trigger: SAU 2 beg
--===========================================================================
function Trig_SAU_2_beg_Conditions()
    return GetResearched() == FourCC('R0CO')
end
function Trig_SAU_2_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C3'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_2_beg()
    gg_trg_SAU_2_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_2_beg, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_SAU_2_beg, Condition(Trig_SAU_2_beg_Conditions))
    TriggerAddAction(gg_trg_SAU_2_beg, Trig_SAU_2_beg_Actions)
end
--===========================================================================
-- Trigger: SAU 3
--===========================================================================
function Trig_SAU_3_Conditions()
    return GetResearched() == FourCC('R0C3')
end
function Trig_SAU_3_Actions()
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_SAU_3()
    gg_trg_SAU_3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_3, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SAU_3, Condition(Trig_SAU_3_Conditions))
    TriggerAddAction(gg_trg_SAU_3, Trig_SAU_3_Actions)
end
--===========================================================================
-- Trigger: SAU 3 beg
--===========================================================================
function Trig_SAU_3_beg_Conditions()
    return GetResearched() == FourCC('R0C3')
end
function Trig_SAU_3_beg_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_3_beg()
    gg_trg_SAU_3_beg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_3_beg, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_SAU_3_beg, Condition(Trig_SAU_3_beg_Conditions))
    TriggerAddAction(gg_trg_SAU_3_beg, Trig_SAU_3_beg_Actions)
end
--===========================================================================
-- Trigger: SAU 3 can
--===========================================================================
function Trig_SAU_3_can_Conditions()
    return GetResearched() == FourCC('R0C3')
end
function Trig_SAU_3_can_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0CN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0CO'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_SAU_3_can()
    gg_trg_SAU_3_can=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SAU_3_can, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_SAU_3_can, Condition(Trig_SAU_3_can_Conditions))
    TriggerAddAction(gg_trg_SAU_3_can, Trig_SAU_3_can_Actions)
end
--===========================================================================
-- Trigger: MEGA SAU
--===========================================================================
function Trig_MEGA_SAU_Conditions()
    return GetResearched() == FourCC('R0C1')
end
function Trig_MEGA_SAU_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('h0FT'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0C4'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_MEGA_SAU()
    gg_trg_MEGA_SAU=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MEGA_SAU, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_MEGA_SAU, Condition(Trig_MEGA_SAU_Conditions))
    TriggerAddAction(gg_trg_MEGA_SAU, Trig_MEGA_SAU_Actions)
end
--===========================================================================
-- Trigger: URAN
--===========================================================================
function Trig_URAN_Conditions()
    return GetResearched() == FourCC('R0C4')
end
function Trig_URAN_Actions()
    SetPlayerAbilityAvailableBJ(true, FourCC('A0SH'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_URAN()
    gg_trg_URAN=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_URAN, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_URAN, Condition(Trig_URAN_Conditions))
    TriggerAddAction(gg_trg_URAN, Trig_URAN_Actions)
end
--===========================================================================
-- Trigger: Klap Klap End
--===========================================================================
function Trig_Klap_Klap_End_Conditions()
    return GetResearched() == FourCC('R0B7')
end
function Trig_Klap_Klap_End_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0B8'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Klap_Klap_End()
    gg_trg_Klap_Klap_End=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_End, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_End, Condition(Trig_Klap_Klap_End_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_End, Trig_Klap_Klap_End_Actions)
end
--===========================================================================
-- Trigger: Klap Klap start
--===========================================================================
function Trig_Klap_Klap_start_Conditions()
    return GetResearched() == FourCC('R0BJ')
end
function Trig_Klap_Klap_start_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BM'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0B8'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Klap_Klap_start()
    gg_trg_Klap_Klap_start=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_start, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_start, Condition(Trig_Klap_Klap_start_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_start, Trig_Klap_Klap_start_Actions)
end
--===========================================================================
-- Trigger: Klap Klap LUM
--===========================================================================
function Trig_Klap_Klap_LUM_Conditions()
    return GetResearched() == FourCC('R0BM')
end
function Trig_Klap_Klap_LUM_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BP'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Klap_Klap_LUM()
    gg_trg_Klap_Klap_LUM=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_LUM, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_LUM, Condition(Trig_Klap_Klap_LUM_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_LUM, Trig_Klap_Klap_LUM_Actions)
end
--===========================================================================
-- Trigger: Klap Klap LUM 2
--===========================================================================
function Trig_Klap_Klap_LUM_2_Conditions()
    return GetResearched() == FourCC('R0BP')
end
function Trig_Klap_Klap_LUM_2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0B7'), 0, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Klap_Klap_LUM_2()
    gg_trg_Klap_Klap_LUM_2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_LUM_2, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_LUM_2, Condition(Trig_Klap_Klap_LUM_2_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_LUM_2, Trig_Klap_Klap_LUM_2_Actions)
end
--===========================================================================
-- Trigger: Klap Klap War
--===========================================================================
function Trig_Klap_Klap_War_Conditions()
    return GetResearched() == FourCC('R0B8')
end
function Trig_Klap_Klap_War_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BK'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BL'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Klap_Klap_War()
    gg_trg_Klap_Klap_War=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War, Condition(Trig_Klap_Klap_War_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War, Trig_Klap_Klap_War_Actions)
end
--===========================================================================
-- Trigger: Klap Klap War Bomb
--===========================================================================
function Trig_Klap_Klap_War_Bomb_Conditions()
    return GetResearched() == FourCC('R0BK')
end
function Trig_Klap_Klap_War_Bomb_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BL'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BO'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Klap_Klap_War_Bomb()
    gg_trg_Klap_Klap_War_Bomb=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War_Bomb, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War_Bomb, Condition(Trig_Klap_Klap_War_Bomb_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War_Bomb, Trig_Klap_Klap_War_Bomb_Actions)
end
--===========================================================================
-- Trigger: Klap Klap War Shield
--===========================================================================
function Trig_Klap_Klap_War_Shield_Conditions()
    return GetResearched() == FourCC('R0BL')
end
function Trig_Klap_Klap_War_Shield_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BN'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0BO'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Klap_Klap_War_Shield()
    gg_trg_Klap_Klap_War_Shield=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War_Shield, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War_Shield, Condition(Trig_Klap_Klap_War_Shield_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War_Shield, Trig_Klap_Klap_War_Shield_Actions)
end
--===========================================================================
-- Trigger: Klap Klap War small
--===========================================================================
function Trig_Klap_Klap_War_small_Conditions()
    return GetResearched() == FourCC('R0BN')
end
function Trig_Klap_Klap_War_small_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BO'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0B7'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FX'), 0, Player(0))
    SetPlayerTechMaxAllowedSwap(FourCC('h0G4'), - 1, Player(0))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Klap_Klap_War_small()
    gg_trg_Klap_Klap_War_small=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War_small, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War_small, Condition(Trig_Klap_Klap_War_small_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War_small, Trig_Klap_Klap_War_small_Actions)
end
--===========================================================================
-- Trigger: Klap Klap War big
--===========================================================================
function Trig_Klap_Klap_War_big_Conditions()
    return GetResearched() == FourCC('R0BO')
end
function Trig_Klap_Klap_War_big_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0BN'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0B7'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0FX'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('h0G5'), - 1, GetOwningPlayer(GetTriggerUnit()))
    udg_LocalPlayer=GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(gg_trg_All_Gnomes)
end
--===========================================================================
function InitTrig_Klap_Klap_War_big()
    gg_trg_Klap_Klap_War_big=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Klap_Klap_War_big, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Klap_Klap_War_big, Condition(Trig_Klap_Klap_War_big_Conditions))
    TriggerAddAction(gg_trg_Klap_Klap_War_big, Trig_Klap_Klap_War_big_Actions)
end