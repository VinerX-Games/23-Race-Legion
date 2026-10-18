//===========================================================================
// Trigger: Draenei Building Inactive Periodic
//===========================================================================
function Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func001Func001C takes nothing returns boolean
    if ( not ( GetPlayerController(GetOwningPlayer(GetEnumUnit())) == MAP_CONTROL_USER ) ) then
        return false
    endif
    if ( not ( UnitHasBuffBJ(GetEnumUnit(), 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func001C takes nothing returns boolean
    if ( not Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func001Func001C() ) then
        return false
    endif
    return true
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func002Func002C takes nothing returns boolean
    if ( not ( GetPlayerController(GetOwningPlayer(GetEnumUnit())) == MAP_CONTROL_USER ) ) then
        return false
    endif
    if ( not ( UnitHasBuffBJ(GetEnumUnit(), 'B0CM') == false ) ) then
        return false
    endif
    return true
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func002C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(GetEnumUnit(), 'B0CG') == false ) ) then
        return false
    endif
    return true
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Func001Func002A takes nothing returns nothing
    if ( Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func001C() ) then
        call SetUnitVertexColorBJ(GetEnumUnit(), 100.00, 100.00, 100.00, 0)
        call UnitRemoveBuffBJ('B0CM', GetEnumUnit())
    else
    endif
    if ( Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func002C() ) then
        call SetUnitVertexColorBJ(GetEnumUnit(), 60.00, 60.00, 60.00, 35.00)
        if ( Trig_Draenei_Building_Inactive_Periodic_Func001Func002Func002Func002C() ) then
            // --------
            set udg_Int_AbilityLevel=1
            set udg_Player=GetOwningPlayer(GetEnumUnit())
            set udg_X=GetUnitX(GetEnumUnit())
            set udg_Y=GetUnitY(GetEnumUnit())
            set udg_Dummy=GetAttackDummy(udg_Player , 'A10S' , udg_Int_AbilityLevel , udg_X , udg_Y , 1)
            call UnitRemoveAbilityBJ('A10R', udg_Dummy)
            call IssueTargetOrderBJ(udg_Dummy, "attack", GetEnumUnit())
            // ---------
        else
        endif
    else
    endif
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Func001C takes nothing returns boolean
    if ( not ( CountUnitsInGroup(udg_ED_DraeneiBuildingsGroup) > 0 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Draenei_Building_Inactive_Periodic_Actions takes nothing returns nothing
    if ( Trig_Draenei_Building_Inactive_Periodic_Func001C() ) then
        call ForGroupBJ(udg_ED_DraeneiBuildingsGroup, function Trig_Draenei_Building_Inactive_Periodic_Func001Func002A)
    else
        call DisableTrigger(GetTriggeringTrigger())
    endif
endfunction

//===========================================================================
function InitTrig_Draenei_Building_Inactive_Periodic takes nothing returns nothing
    set gg_trg_Draenei_Building_Inactive_Periodic=CreateTrigger()
    call DisableTrigger(gg_trg_Draenei_Building_Inactive_Periodic)
    call TriggerRegisterTimerEventPeriodic(gg_trg_Draenei_Building_Inactive_Periodic, 1.00)
    call TriggerAddAction(gg_trg_Draenei_Building_Inactive_Periodic, function Trig_Draenei_Building_Inactive_Periodic_Actions)
endfunction


//===========================================================================
// Trigger: Gift of Naaru
//===========================================================================
function Trig_Gift_of_Naaru_Func002Func001C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(udg_heal_target, 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Gift_of_Naaru_Func002C takes nothing returns boolean
    if ( not ( GetUnitAbilityLevelSwapped('A10Z', udg_heal_target) > 0 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Gift_of_Naaru_Actions takes nothing returns nothing
    call DisableTrigger(GetTriggeringTrigger())
    if ( Trig_Gift_of_Naaru_Func002C() ) then
        if ( Trig_Gift_of_Naaru_Func002Func001C() ) then
            set udg_NextHealTarget=udg_heal_target
            set udg_NextHealAmount=( udg_heal_amount * 0.20 )
            call TriggerExecute(gg_trg_Heal_Unit)
        else
            set udg_NextHealTarget=udg_heal_target
            set udg_NextHealAmount=( udg_heal_amount * 0.10 )
            call TriggerExecute(gg_trg_Heal_Unit)
        endif
    else
    endif
    call EnableTrigger(GetTriggeringTrigger())
endfunction

//===========================================================================
function InitTrig_Gift_of_Naaru takes nothing returns nothing
    set gg_trg_Gift_of_Naaru=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Gift_of_Naaru, "udg_HealEvent", EQUAL, 1.00)
    call TriggerAddAction(gg_trg_Gift_of_Naaru, function Trig_Gift_of_Naaru_Actions)
endfunction


//===========================================================================
// Trigger: Charged Gems Periodic
//===========================================================================
function Trig_Charged_Gems_Periodic_Func001Func001C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(GetEnumUnit(), 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Charged_Gems_Periodic_Func001A takes nothing returns nothing
    if ( Trig_Charged_Gems_Periodic_Func001Func001C() ) then
        call UnitRemoveAbilityBJ('Abun', GetEnumUnit())
        call UnitAddAbilityBJ('A10X', GetEnumUnit())
    else
        call UnitAddAbilityBJ('Abun', GetEnumUnit())
        call UnitRemoveAbilityBJ('A10X', GetEnumUnit())
    endif
endfunction

function Trig_Charged_Gems_Periodic_Actions takes nothing returns nothing
    call ForGroupBJ(udg_ED_GemcraftersGroup, function Trig_Charged_Gems_Periodic_Func001A)
endfunction

//===========================================================================
function InitTrig_Charged_Gems_Periodic takes nothing returns nothing
    set gg_trg_Charged_Gems_Periodic=CreateTrigger()
    call DisableTrigger(gg_trg_Charged_Gems_Periodic)
    call TriggerRegisterTimerEventPeriodic(gg_trg_Charged_Gems_Periodic, 0.50)
    call TriggerAddAction(gg_trg_Charged_Gems_Periodic, function Trig_Charged_Gems_Periodic_Actions)
endfunction


//===========================================================================
// Trigger: Shield of Argus Reduce Damage
//===========================================================================
function Trig_Shield_of_Argus_Reduce_Damage_Conditions takes nothing returns boolean
    if ( not ( GetUnitTypeId(udg_DamageEventTarget) == 'h04X' ) ) then
        return false
    endif
    if ( not ( udg_DamageEventAmount >= 1.00 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Shield_of_Argus_Reduce_Damage_Func001C takes nothing returns boolean
    if ( not ( udg_IsDamageAttack == true ) ) then
        return false
    endif
    if ( not ( GetUnitAbilityLevelSwapped('A11J', udg_DamageEventTarget) > 1 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Shield_of_Argus_Reduce_Damage_Actions takes nothing returns nothing
    if ( Trig_Shield_of_Argus_Reduce_Damage_Func001C() ) then
        set udg_DamageEventAmount=( udg_DamageEventAmount * 0.50 )
        call DecUnitAbilityLevelSwapped('A11J', udg_DamageEventTarget)
        call AddSpecialEffectTargetUnitBJ("hand, left", udg_DamageEventTarget, "Abilities\\Spells\\Human\\Defend\\DefendCaster.mdl")
        call DestroyEffectBJ(GetLastCreatedEffectBJ())
    else
    endif
endfunction

//===========================================================================
function InitTrig_Shield_of_Argus_Reduce_Damage takes nothing returns nothing
    set gg_trg_Shield_of_Argus_Reduce_Damage=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Shield_of_Argus_Reduce_Damage, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Shield_of_Argus_Reduce_Damage, Condition(function Trig_Shield_of_Argus_Reduce_Damage_Conditions))
    call TriggerAddAction(gg_trg_Shield_of_Argus_Reduce_Damage, function Trig_Shield_of_Argus_Reduce_Damage_Actions)
endfunction


//===========================================================================
// Trigger: Shield of Argus Restock
//===========================================================================
function Trig_Shield_of_Argus_Restock_Func001Func001C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(GetSpellAbilityUnit(), 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Shield_of_Argus_Restock_Func001C takes nothing returns boolean
    if ( not ( GetUnitAbilityLevelSwapped('A11J', GetSpellAbilityUnit()) < 4 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Shield_of_Argus_Restock_Actions takes nothing returns nothing
    if ( Trig_Shield_of_Argus_Restock_Func001C() ) then
        if ( Trig_Shield_of_Argus_Restock_Func001Func001C() ) then
            call IncUnitAbilityLevelSwapped('A11J', GetSpellAbilityUnit())
            call SetUnitAbilityLevelSwapped('A11I', GetSpellAbilityUnit(), 2)
        else
            call IncUnitAbilityLevelSwapped('A11J', GetSpellAbilityUnit())
            call SetUnitAbilityLevelSwapped('A11I', GetSpellAbilityUnit(), 1)
        endif
    else
    endif
endfunction

//===========================================================================
function InitTrig_Shield_of_Argus_Restock takes nothing returns nothing
        call RegisterSpellEffectEvent('A11I' , function Trig_Shield_of_Argus_Restock_Actions)
endfunction

//===========================================================================
// Trigger: Exiled Arrow Effect
//===========================================================================
function Trig_Exiled_Arrow_Effect_Conditions takes nothing returns boolean
    if ( not ( udg_DamageEventAmount >= 1.00 ) ) then
        return false
    endif
    if ( not ( GetUnitAbilityLevelSwapped('A10U', udg_DamageEventSource) > 1 ) ) then
        return false
    endif
    if ( not ( IsPlayerEnemy(GetOwningPlayer(udg_DamageEventSource), GetOwningPlayer(udg_DamageEventTarget)) == true ) ) then
        return false
    endif
    if ( not ( udg_IsDamageAttack == true ) ) then
        return false
    endif
    if ( not ( IsUnitType(udg_DamageEventTarget, UNIT_TYPE_STRUCTURE) == false ) ) then
        return false
    endif
    if ( not ( IsUnitIllusionBJ(udg_DamageEventSource) == false ) ) then
        return false
    endif
    return true
endfunction

function Trig_Exiled_Arrow_Effect_Actions takes nothing returns nothing
    set udg_ExiledArrowCaster=udg_DamageEventSource
    set udg_ExiledArrowTarget=udg_DamageEventTarget
    set udg_ExiledArrowCount=( GetUnitAbilityLevelSwapped('A10U', udg_ExiledArrowCaster) - 1 )
    call SetUnitAbilityLevelSwapped('A10U', udg_ExiledArrowCaster, udg_ExiledArrowCount)
    call RemoveUnitFromStockBJ('n02S', udg_ExiledArrowCaster)
    call AddUnitToStockBJ('n02S', udg_ExiledArrowCaster, ( udg_ExiledArrowCount - 1 ), ( udg_ExiledArrowCount - 1 ))
    // Create Dummy
    // --------
    set udg_Int_AbilityLevel=1
    set udg_Player=GetOwningPlayer(udg_DamageEventSource)
    set udg_X=GetUnitX(udg_DamageEventTarget)
    set udg_Y=GetUnitY(udg_DamageEventTarget)
    set udg_Dummy=GetDummy(udg_Player , 'A10T' , udg_Int_AbilityLevel , udg_X , udg_Y , 1)
    call IssueImmediateOrderBJ(udg_Dummy, "fanofknives")
    // ---------
endfunction

//===========================================================================
function InitTrig_Exiled_Arrow_Effect takes nothing returns nothing
    set gg_trg_Exiled_Arrow_Effect=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Exiled_Arrow_Effect, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Exiled_Arrow_Effect, Condition(function Trig_Exiled_Arrow_Effect_Conditions))
    call TriggerAddAction(gg_trg_Exiled_Arrow_Effect, function Trig_Exiled_Arrow_Effect_Actions)
endfunction


//===========================================================================
// Trigger: Exiled Arrow Charge Gained
//===========================================================================
function Trig_Exiled_Arrow_Charge_Gained_Func002Func005C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(GetSpellAbilityUnit(), 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Exiled_Arrow_Charge_Gained_Func002C takes nothing returns boolean
    if ( not ( GetUnitAbilityLevelSwapped('A10U', udg_ExiledArrowCaster) < 4 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Exiled_Arrow_Charge_Gained_Actions takes nothing returns nothing
    set udg_ExiledArrowCaster=GetTriggerUnit()
    if ( Trig_Exiled_Arrow_Charge_Gained_Func002C() ) then
        set udg_ExiledArrowCount=( GetUnitAbilityLevelSwapped('A10U', udg_ExiledArrowCaster) + 1 )
        call SetUnitAbilityLevelSwapped('A10U', udg_ExiledArrowCaster, udg_ExiledArrowCount)
        call RemoveUnitFromStockBJ('n02S', udg_ExiledArrowCaster)
        call AddUnitToStockBJ('n02S', udg_ExiledArrowCaster, ( udg_ExiledArrowCount - 1 ), ( udg_ExiledArrowCount - 1 ))
        if ( Trig_Exiled_Arrow_Charge_Gained_Func002Func005C() ) then
            call SetUnitAbilityLevelSwapped('A10E', GetSpellAbilityUnit(), 2)
        else
            call SetUnitAbilityLevelSwapped('A10E', GetSpellAbilityUnit(), 1)
        endif
    else
    endif
endfunction

//===========================================================================
function InitTrig_Exiled_Arrow_Charge_Gained takes nothing returns nothing
        call RegisterSpellEffectEvent('A10E' , function Trig_Exiled_Arrow_Charge_Gained_Actions)
endfunction

//===========================================================================
// Trigger: Tempest Tusk Effect
//===========================================================================
function Trig_Tempest_Tusk_Effect_Conditions takes nothing returns boolean
    if ( not ( GetUnitAbilityLevelSwapped('A11X', udg_DamageEventSource) > 1 ) ) then
        return false
    endif
    if ( not ( IsPlayerEnemy(GetOwningPlayer(udg_DamageEventSource), GetOwningPlayer(udg_DamageEventTarget)) == true ) ) then
        return false
    endif
    if ( not ( udg_IsDamageAttack == true ) ) then
        return false
    endif
    if ( not ( IsUnitType(udg_DamageEventTarget, UNIT_TYPE_STRUCTURE) == false ) ) then
        return false
    endif
    if ( not ( IsUnitIllusionBJ(udg_DamageEventSource) == false ) ) then
        return false
    endif
    if ( not ( udg_DamageEventAmount >= 1.00 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Tempest_Tusk_Effect_Actions takes nothing returns nothing
    set udg_TempestTuskCaster=udg_DamageEventSource
    set udg_TempestTuskTarget=udg_DamageEventTarget
    set udg_TempestTuskCount=( GetUnitAbilityLevelSwapped('A11X', udg_TempestTuskCaster) - 1 )
    call SetUnitAbilityLevelSwapped('A11X', udg_TempestTuskCaster, udg_TempestTuskCount)
    call RemoveUnitFromStockBJ('n02U', udg_TempestTuskCaster)
    call AddUnitToStockBJ('n02U', udg_TempestTuskCaster, ( udg_TempestTuskCount - 1 ), ( udg_TempestTuskCount - 1 ))
    call AddSpecialEffectLocBJ(GetUnitLoc(udg_DamageEventSource), "Abilities\\Spells\\Human\\ThunderClap\\ThunderClapCaster.mdl")
    call BlzSetSpecialEffectAlpha(GetLastCreatedEffectBJ(), 100)
    call BlzSetSpecialEffectScale(GetLastCreatedEffectBJ(), 0.70)
    call DestroyEffectBJ(GetLastCreatedEffectBJ())
endfunction

//===========================================================================
function InitTrig_Tempest_Tusk_Effect takes nothing returns nothing
    set gg_trg_Tempest_Tusk_Effect=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Tempest_Tusk_Effect, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Tempest_Tusk_Effect, Condition(function Trig_Tempest_Tusk_Effect_Conditions))
    call TriggerAddAction(gg_trg_Tempest_Tusk_Effect, function Trig_Tempest_Tusk_Effect_Actions)
endfunction


//===========================================================================
// Trigger: Tempest Tusk Charge Gained
//===========================================================================
function Trig_Tempest_Tusk_Charge_Gained_Func002Func005C takes nothing returns boolean
    if ( not ( UnitHasBuffBJ(GetSpellAbilityUnit(), 'B0CG') == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Tempest_Tusk_Charge_Gained_Func002C takes nothing returns boolean
    if ( not ( GetUnitAbilityLevelSwapped('A11X', udg_TempestTuskCaster) < 4 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Tempest_Tusk_Charge_Gained_Actions takes nothing returns nothing
    set udg_TempestTuskCaster=GetTriggerUnit()
    if ( Trig_Tempest_Tusk_Charge_Gained_Func002C() ) then
        set udg_TempestTuskCount=( GetUnitAbilityLevelSwapped('A11X', udg_TempestTuskCaster) + 1 )
        call SetUnitAbilityLevelSwapped('A11X', udg_TempestTuskCaster, udg_TempestTuskCount)
        call RemoveUnitFromStockBJ('n02U', udg_TempestTuskCaster)
        call AddUnitToStockBJ('n02U', udg_TempestTuskCaster, ( udg_TempestTuskCount - 1 ), ( udg_TempestTuskCount - 1 ))
        if ( Trig_Tempest_Tusk_Charge_Gained_Func002Func005C() ) then
            call SetUnitAbilityLevelSwapped('A11Z', GetSpellAbilityUnit(), 2)
        else
            call SetUnitAbilityLevelSwapped('A11Z', GetSpellAbilityUnit(), 1)
        endif
    else
    endif
endfunction

//===========================================================================
function InitTrig_Tempest_Tusk_Charge_Gained takes nothing returns nothing
        call RegisterSpellEffectEvent('A11Z' , function Trig_Tempest_Tusk_Charge_Gained_Actions)
endfunction

//===========================================================================
// Trigger: Reconstitute
//
// //Reconstitue Ability
//===========================================================================
function Trig_Reconstitute_Actions takes nothing returns nothing
    local unit caster= GetSpellAbilityUnit()
    local unit targetUnit= GetSpellTargetUnit()
    local player p= GetOwningPlayer(caster)
    local real tX= GetUnitX(targetUnit)
    local real tY= GetUnitY(targetUnit)
    local group g= CreateGroup()
    local unit u
    local effect eff
    local boolean hasTech= ( GetPlayerTechCountSimple('R07A', p) > 0 )

    // 1. Gather all units in a 150 radius around the TARGET without leaking
    call GroupEnumUnitsInRange(g, tX, tY, 150.00, null)

    loop
        set u=FirstOfGroup(g)
        exitwhen u == null
        call GroupRemoveUnit(g, u)

        // Filters: Alive, Ally, Wounded, Not Structure, Not Primary Target, and Not Caster
        if UnitAlive(u) and IsUnitAlly(u, p) and GetUnitLifePercent(u) < 100.00 then
            if u != targetUnit and u != caster and not IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                
                // 2. Check Tech: If tech is NOT researched, ignore mechanical units!
                if hasTech or not IsUnitType(u, UNIT_TYPE_MECHANICAL) then
                    
                    // Apply Healing
                    call SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + 5.00)
                    
                    // Apply Visuals
                    set eff=AddSpecialEffectTarget("Exodar Draenei - Reconstitute.mdx", u, "origin")
                    call BlzSetSpecialEffectScale(eff, 0.50)
                    call DestroyEffect(eff)
                    set eff=null
                    
                endif
                
            endif
        endif
    endloop

    // CLEANUP
    call DestroyGroup(g)
    set caster=null
    set targetUnit=null
    set p=null
    set u=null
    set g=null
endfunction

//===========================================================================
function InitTrig_Reconstitute takes nothing returns nothing
    local trigger t= CreateTrigger()
    call RegisterSpellEffectEvent('A11C' , function Trig_Reconstitute_Actions)
    set t=null
endfunction

//===========================================================================
// Trigger: Incandescence
//===========================================================================
function Trig_Incandescence_Func002Func002C takes nothing returns boolean
    if ( not ( udg_WDS_TmpInteger[0] > 0 ) ) then
        return false
    endif
    if ( not ( IsUnitAliveBJ(GetEnumUnit()) == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Incandescence_Func002A takes nothing returns nothing
    set udg_WDS_TmpInteger[0]=GetUnitAbilityLevelSwapped(udg_WDS_DockAbilityLevel, GetEnumUnit())
    if ( Trig_Incandescence_Func002Func002C() ) then
        set udg_WDS_TmpReal[0]=( 1.50 * I2R(udg_WDS_TmpInteger[0]) )
        call SetUnitLifeBJ(GetEnumUnit(), ( GetUnitStateSwap(UNIT_STATE_LIFE, GetEnumUnit()) + udg_WDS_TmpReal[0] ))
        call CreateTextTagUnitBJ(( "+" + I2S(R2I(udg_WDS_TmpReal[0])) ), GetEnumUnit(), 0, 10, 0.00, 100, 0.00, 0)
        call SetTextTagVelocityBJ(GetLastCreatedTextTag(), 64, 90)
        call SetTextTagPermanentBJ(GetLastCreatedTextTag(), false)
        call SetTextTagLifespanBJ(GetLastCreatedTextTag(), 1.00)
        call SetTextTagFadepointBJ(GetLastCreatedTextTag(), 0.50)
        // -----------------
        call UnitAddAbilityBJ('A0YI', GetEnumUnit())
        call SetUnitAbilityLevelSwapped('A0YI', GetEnumUnit(), udg_WDS_TmpInteger[0])
    else
        call UnitRemoveAbilityBJ('A0YI', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YJ', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YK', GetEnumUnit())
    endif
endfunction

function Trig_Incandescence_Func004Func002C takes nothing returns boolean
    if ( not ( udg_WDS_TmpInteger[0] > 0 ) ) then
        return false
    endif
    if ( not ( IsUnitAliveBJ(GetEnumUnit()) == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Incandescence_Func004A takes nothing returns nothing
    set udg_WDS_TmpInteger[0]=GetUnitAbilityLevelSwapped(udg_WDS_DockAbilityLevel, GetEnumUnit())
    if ( Trig_Incandescence_Func004Func002C() ) then
        set udg_WDS_TmpReal[0]=( 1.50 * I2R(udg_WDS_TmpInteger[0]) )
        call SetUnitLifeBJ(GetEnumUnit(), ( GetUnitStateSwap(UNIT_STATE_LIFE, GetEnumUnit()) + udg_WDS_TmpReal[0] ))
        call CreateTextTagUnitBJ(( "+" + I2S(R2I(udg_WDS_TmpReal[0])) ), GetEnumUnit(), 0, 10, 0.00, 100, 0.00, 0)
        call SetTextTagVelocityBJ(GetLastCreatedTextTag(), 64, 90)
        call SetTextTagPermanentBJ(GetLastCreatedTextTag(), false)
        call SetTextTagLifespanBJ(GetLastCreatedTextTag(), 1.00)
        call SetTextTagFadepointBJ(GetLastCreatedTextTag(), 0.50)
        // -----------------
        call UnitAddAbilityBJ('A0YJ', GetEnumUnit())
        call SetUnitAbilityLevelSwapped('A0YJ', GetEnumUnit(), udg_WDS_TmpInteger[0])
    else
        call UnitRemoveAbilityBJ('A0YI', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YJ', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YK', GetEnumUnit())
    endif
endfunction

function Trig_Incandescence_Func006Func002C takes nothing returns boolean
    if ( not ( udg_WDS_TmpInteger[0] > 0 ) ) then
        return false
    endif
    if ( not ( IsUnitAliveBJ(GetEnumUnit()) == true ) ) then
        return false
    endif
    return true
endfunction

function Trig_Incandescence_Func006A takes nothing returns nothing
    set udg_WDS_TmpInteger[0]=GetUnitAbilityLevelSwapped(udg_WDS_DockAbilityLevel, GetEnumUnit())
    if ( Trig_Incandescence_Func006Func002C() ) then
        set udg_WDS_TmpReal[0]=( 1.50 * I2R(udg_WDS_TmpInteger[0]) )
        call SetUnitLifeBJ(GetEnumUnit(), ( GetUnitStateSwap(UNIT_STATE_LIFE, GetEnumUnit()) + udg_WDS_TmpReal[0] ))
        call CreateTextTagUnitBJ(( "+" + I2S(R2I(udg_WDS_TmpReal[0])) ), GetEnumUnit(), 0, 10, 0.00, 100, 0.00, 0)
        call SetTextTagVelocityBJ(GetLastCreatedTextTag(), 64, 90)
        call SetTextTagPermanentBJ(GetLastCreatedTextTag(), false)
        call SetTextTagLifespanBJ(GetLastCreatedTextTag(), 1.00)
        call SetTextTagFadepointBJ(GetLastCreatedTextTag(), 0.50)
        // -----------------
        call UnitAddAbilityBJ('A0YK', GetEnumUnit())
        call SetUnitAbilityLevelSwapped('A0YK', GetEnumUnit(), udg_WDS_TmpInteger[0])
    else
        call UnitRemoveAbilityBJ('A0YI', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YJ', GetEnumUnit())
        call UnitRemoveAbilityBJ('A0YK', GetEnumUnit())
    endif
endfunction

function Trig_Incandescence_Actions takes nothing returns nothing
    set bj_wantDestroyGroup=true
    call ForGroupBJ(GetUnitsOfTypeIdAll('h061'), function Trig_Incandescence_Func002A)
    set bj_wantDestroyGroup=true
    call ForGroupBJ(GetUnitsOfTypeIdAll('h05Z'), function Trig_Incandescence_Func004A)
    set bj_wantDestroyGroup=true
    call ForGroupBJ(GetUnitsOfTypeIdAll('h060'), function Trig_Incandescence_Func006A)
endfunction

//===========================================================================
function InitTrig_Incandescence takes nothing returns nothing
    set gg_trg_Incandescence=CreateTrigger()
    call DisableTrigger(gg_trg_Incandescence)
    call TriggerRegisterTimerEventPeriodic(gg_trg_Incandescence, 1.00)
    call TriggerAddAction(gg_trg_Incandescence, function Trig_Incandescence_Actions)
endfunction


//===========================================================================
// Trigger: Inviolable Arrows
//===========================================================================
function Trig_Inviolable_Arrows_Conditions takes nothing returns boolean
    return GetUnitTypeId(udg_DamageEventSource) == 'h05U' and udg_IsDamageAttack == true and GetPlayerTechCountSimple('R07T', GetOwningPlayer(udg_DamageEventSource)) > 0 and udg_DamageEventAmount >= 1.00
endfunction

function Trig_Inviolable_Arrows_Actions takes nothing returns nothing
    local unit source= udg_DamageEventSource
    local real bonusDamage

    // Calculate 3% of the attacker's current life.
    set bonusDamage=GetUnitState(source, UNIT_STATE_LIFE) * 0.03

    // Add the calculated bonus damage to the total damage of this attack.
    // This modifies the damage event before it is finalized by the damage system.
    set udg_DamageEventAmount=udg_DamageEventAmount + bonusDamage

    set source=null
endfunction

//===========================================================================
function InitTrig_Inviolable_Arrows takes nothing returns nothing
    set gg_trg_Inviolable_Arrows=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Inviolable_Arrows, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Inviolable_Arrows, Condition(function Trig_Inviolable_Arrows_Conditions))
    call TriggerAddAction(gg_trg_Inviolable_Arrows, function Trig_Inviolable_Arrows_Actions)
endfunction

//===========================================================================
// Trigger: Living Precision Periodic
//===========================================================================
function Trig_Living_Precision_Periodic_Func001Func001C takes nothing returns boolean
    if ( not ( GetUnitLifePercent(GetEnumUnit()) >= 80.00 ) ) then
        return false
    endif
    return true
endfunction

function Trig_Living_Precision_Periodic_Func001A takes nothing returns nothing
    if ( Trig_Living_Precision_Periodic_Func001Func001C() ) then
        call UnitAddAbilityBJ('A0YD', GetEnumUnit())
    else
        call UnitRemoveAbilityBJ('A0YD', GetEnumUnit())
    endif
endfunction

function Trig_Living_Precision_Periodic_Actions takes nothing returns nothing
    call ForGroupBJ(udg_LF_SagittaryGroup, function Trig_Living_Precision_Periodic_Func001A)
endfunction

//===========================================================================
function InitTrig_Living_Precision_Periodic takes nothing returns nothing
    set gg_trg_Living_Precision_Periodic=CreateTrigger()
    call DisableTrigger(gg_trg_Living_Precision_Periodic)
    call TriggerRegisterTimerEventPeriodic(gg_trg_Living_Precision_Periodic, 1.00)
    call TriggerAddAction(gg_trg_Living_Precision_Periodic, function Trig_Living_Precision_Periodic_Actions)
endfunction


//===========================================================================
// Trigger: Flare Shard
//===========================================================================
function Trig_Flare_Shard_Conditions takes nothing returns boolean
    return GetUnitTypeId(udg_DamageEventSource) == 'e023' and udg_IsDamageAttack == true and GetPlayerTechCountSimple('R07S', GetOwningPlayer(udg_DamageEventSource)) > 0 and udg_DamageEventAmount >= 1.00
endfunction

function Trig_Flare_Shard_Actions takes nothing returns nothing
    local unit source= udg_DamageEventSource
    local real healAmount= udg_DamageEventAmount * 0.10

    call SetUnitState(source, UNIT_STATE_LIFE, GetUnitState(source, UNIT_STATE_LIFE) + healAmount)

    set source=null
endfunction

//===========================================================================
function InitTrig_Flare_Shard takes nothing returns nothing
    set gg_trg_Flare_Shard=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Flare_Shard, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Flare_Shard, Condition(function Trig_Flare_Shard_Conditions))
    call TriggerAddAction(gg_trg_Flare_Shard, function Trig_Flare_Shard_Actions)
endfunction

//===========================================================================
// Trigger: Retributive Core
//===========================================================================
function Trig_Retributive_Core_Conditions takes nothing returns boolean
    return GetUnitTypeId(udg_DamageEventTarget) == 'h05W' and GetUnitAbilityLevel(udg_DamageEventTarget, 'A0YQ') == 2 and udg_DamageEventAmount >= 1.00
endfunction

function Trig_Retributive_Core_Actions takes nothing returns nothing
    local unit target= udg_DamageEventTarget
    local player owner= GetOwningPlayer(target)
    local real tX= GetUnitX(target)
    local real tY= GetUnitY(target)
    local real healAmount
    local group g= CreateGroup()
    local group validTargets= CreateGroup()
    local integer groupSize
    local unit u

    // 1. Set the ability level and start the cooldown.
    call SetUnitAbilityLevel(target, 'A0YQ', 1)
    call BlzStartUnitAbilityCooldown(target, 'A0YQ', 0.50)

    // 2. Gather all units in range without generating a condition handle!
    call GroupEnumUnitsInRange(g, tX, tY, 450.00, null)
    
    loop
        set u=FirstOfGroup(g)
        exitwhen u == null
        call GroupRemoveUnit(g, u)
        
        // Manual Filtering: Alive, Ally, Wounded, Not Structure, and Not the Caster!
        if UnitAlive(u) and IsUnitAlly(u, owner) and u != target then
            if GetUnitLifePercent(u) < 100.00 and not IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                
                call GroupAddUnit(validTargets, u)
                
            endif
        endif
    endloop

    // 3. Calculate the heal amount.
    set groupSize=BlzGroupGetSize(validTargets)
    
    if groupSize > 0 then
        set healAmount=udg_DamageEventPrevAmt / groupSize
    else
        // Cleanup and exit if no allies need healing to prevent division by zero!
        call DestroyGroup(g)
        call DestroyGroup(validTargets)
        set target=null
        set g=null
        set validTargets=null
        return
    endif

    // 4. Loop through the valid group and apply the healing and visual effect.
    loop
        set u=FirstOfGroup(validTargets)
        exitwhen u == null
        call GroupRemoveUnit(validTargets, u)

        call SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + healAmount)
        call DestroyEffect(AddSpecialEffectTarget("Abilities\\Weapons\\ProcMissile\\ProcMissile.mdl", u, "head"))
        
    endloop

    // 5. Clean up all handles.
    call DestroyGroup(g)
    call DestroyGroup(validTargets)
    set target=null
    set g=null
    set validTargets=null
    set u=null
endfunction

//===========================================================================
function InitTrig_Retributive_Core takes nothing returns nothing
    set gg_trg_Retributive_Core=CreateTrigger()
    call h__TriggerRegisterVariableEvent(gg_trg_Retributive_Core, "udg_DamageEvent", EQUAL, 1.00)
    call TriggerAddCondition(gg_trg_Retributive_Core, Condition(function Trig_Retributive_Core_Conditions))
    call TriggerAddAction(gg_trg_Retributive_Core, function Trig_Retributive_Core_Actions)
endfunction
