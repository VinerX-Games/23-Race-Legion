    gg_trg_MageTpSell=CreateTrigger()
    DisableTrigger(gg_trg_MageTpSell)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MageTpSell, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_MageTpSell, Condition(Trig_MageTpSell_Conditions))
    TriggerAddAction(gg_trg_MageTpSell, Trig_MageTpSell_Actions)
end
--===========================================================================
-- Trigger: Deathwing
--===========================================================================
function Trig_Deathwing_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('A0YW')) > 0
end
function Trig_Deathwing_Actions()
    BlzStartUnitAbilityCooldown(GetTrainedUnit(), FourCC('A0YW'), 150)
end
--===========================================================================
function InitTrig_Deathwing()
    gg_trg_Deathwing=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Deathwing, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Deathwing, Condition(Trig_Deathwing_Conditions))
    TriggerAddAction(gg_trg_Deathwing, Trig_Deathwing_Actions)
end
--===========================================================================
-- Trigger: TrainHeroGiveItem
--===========================================================================
function Trig_TrainHeroGiveItem_Conditions()
    return IsUnitType(GetTrainedUnit(), UNIT_TYPE_HERO) and not udg_HeroFirstYes[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
function Trig_TrainHeroGiveItem_Actions()
    UnitAddItemByIdSwapped(FourCC('stwp'), GetTrainedUnit())
    UnitAddItemByIdSwapped(FourCC('I015'), GetTrainedUnit())
    udg_HeroFirstYes[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=true
end
--===========================================================================
function InitTrig_TrainHeroGiveItem()
    gg_trg_TrainHeroGiveItem=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainHeroGiveItem, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainHeroGiveItem, Condition(Trig_TrainHeroGiveItem_Conditions))
    TriggerAddAction(gg_trg_TrainHeroGiveItem, Trig_TrainHeroGiveItem_Actions)
end
--===========================================================================
-- Trigger: LimitHero Exep
--===========================================================================
function Trig_LimitHero_Exep_Conditions()
    return IsUnitType(GetTrainedUnit(), UNIT_TYPE_HERO)
end
function Trig_LimitHero_Exep_Actions()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), GetTrainedUnitType(), 1)
end
--===========================================================================
function InitTrig_LimitHero_Exep()
    gg_trg_LimitHero_Exep=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LimitHero_Exep, EVENT_PLAYER_UNIT_TRAIN_START)
    TriggerAddCondition(gg_trg_LimitHero_Exep, Condition(Trig_LimitHero_Exep_Conditions))
    TriggerAddAction(gg_trg_LimitHero_Exep, Trig_LimitHero_Exep_Actions)
end
--===========================================================================
-- Trigger: fire
--===========================================================================
function Trig_fire_Conditions()
    return GetResearched() == FourCC('pa16')
end
function Trig_fire_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa47'), 0, Player(0))
end
--===========================================================================
function InitTrig_fire()
    gg_trg_fire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_fire, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_fire, Condition(Trig_fire_Conditions))
    TriggerAddAction(gg_trg_fire, Trig_fire_Actions)
end
--===========================================================================
-- Trigger: fire1
--===========================================================================
function Trig_fire1_Conditions()
    return GetResearched() == FourCC('pa16')
end
function Trig_fire1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa47'), 1, Player(0))
end
--===========================================================================
function InitTrig_fire1()
    gg_trg_fire1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_fire1, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_fire1, Condition(Trig_fire1_Conditions))
    TriggerAddAction(gg_trg_fire1, Trig_fire1_Actions)
end
--===========================================================================
-- Trigger: earth
--===========================================================================
function Trig_earth_Conditions()
    return GetResearched() == FourCC('pa47')
end
function Trig_earth_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa16'), 0, Player(0))
end
--===========================================================================
function InitTrig_earth()
    gg_trg_earth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_earth, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_earth, Condition(Trig_earth_Conditions))
    TriggerAddAction(gg_trg_earth, Trig_earth_Actions)
end
--===========================================================================
-- Trigger: earth1
--===========================================================================
function Trig_earth1_Conditions()
    return GetResearched() == FourCC('pa47')
end
function Trig_earth1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa16'), 1, Player(0))
end
--===========================================================================
function InitTrig_earth1()
    gg_trg_earth1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_earth1, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_earth1, Condition(Trig_earth1_Conditions))
    TriggerAddAction(gg_trg_earth1, Trig_earth1_Actions)
end
--===========================================================================
-- Trigger: Beer
--===========================================================================
function Trig_Beer_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_Beer_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA83'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Beer()
    gg_trg_Beer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Beer, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Beer, Condition(Trig_Beer_Conditions))
    TriggerAddAction(gg_trg_Beer, Trig_Beer_Actions)
end
--===========================================================================
-- Trigger: BeerFin
--===========================================================================
function Trig_BeerFin_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_BeerFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa22'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BeerFin()
    gg_trg_BeerFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeerFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BeerFin, Condition(Trig_BeerFin_Conditions))
    TriggerAddAction(gg_trg_BeerFin, Trig_BeerFin_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy O Copy
--===========================================================================
function Trig_flot2_Copy_O_Copy_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_flot2_Copy_O_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA83'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_O_Copy()
    gg_trg_flot2_Copy_O_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_O_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_O_Copy, Condition(Trig_flot2_Copy_O_Copy_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_O_Copy, Trig_flot2_Copy_O_Copy_Actions)
end
--===========================================================================
-- Trigger: Geo
--===========================================================================
function Trig_Geo_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_Geo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA82'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Geo()
    gg_trg_Geo=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Geo, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Geo, Condition(Trig_Geo_Conditions))
    TriggerAddAction(gg_trg_Geo, Trig_Geo_Actions)
end
--===========================================================================
-- Trigger: GeoFin
--===========================================================================
function Trig_GeoFin_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_GeoFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa06'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_GeoFin()
    gg_trg_GeoFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GeoFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_GeoFin, Condition(Trig_GeoFin_Conditions))
    TriggerAddAction(gg_trg_GeoFin, Trig_GeoFin_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy O Copy
--===========================================================================
function Trig_arm2_Copy_O_Copy_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_arm2_Copy_O_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA82'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_O_Copy()
    gg_trg_arm2_Copy_O_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_O_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_O_Copy, Condition(Trig_arm2_Copy_O_Copy_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_O_Copy, Trig_arm2_Copy_O_Copy_Actions)
end
--===========================================================================
-- Trigger: FarmBuild
--===========================================================================
function Trig_FarmBuild_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('pa26') or GetUnitTypeId(GetTriggerUnit()) == FourCC('h0NZ')
end
function Trig_FarmBuild_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    local count= LoadInteger(Hash, pi, phash)
    SaveInteger(Hash, pi, phash, count + 1)
    Ptiers(pi)
end
--===========================================================================
function InitTrig_FarmBuild()
    gg_trg_FarmBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FarmBuild, Condition(Trig_FarmBuild_Conditions))
    TriggerAddAction(gg_trg_FarmBuild, Trig_FarmBuild_Actions)
end
--===========================================================================
-- Trigger: FarmLose
--===========================================================================
function Trig_FarmLose_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('pa26') or GetUnitTypeId(GetTriggerUnit()) == FourCC('h0NZ')
end
function Trig_FarmLose_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    local count= LoadInteger(Hash, pi, phash)
    SaveInteger(Hash, pi, phash, count - 1)
    --call DisplayTextToPlayer(Player(0),0,0,I2S(count-1))
    Ptiers(pi)
end
--===========================================================================
function InitTrig_FarmLose()
    gg_trg_FarmLose=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmLose, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_FarmLose, Condition(Trig_FarmLose_Conditions))
    TriggerAddAction(gg_trg_FarmLose, Trig_FarmLose_Actions)
end
--===========================================================================
-- Trigger: Provocation
--===========================================================================
function Trig_Provocation_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A1OH'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A1OH') , 7)
end
--===========================================================================
function InitTrig_Provocation()
    gg_trg_Provocation=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Provocation, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Provocation, function()
        if GetSpellAbilityId() ~= FourCC('PA78') then return end
        Trig_Provocation_Actions()
    end)
end
--===========================================================================
-- Trigger: PUnitTrained
--===========================================================================
function Trig_PUnitTrained_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1I7')) > 0
end
function Trig_PUnitTrained_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    local count= LoadInteger(Hash, pi, phash)
    local u= GetTrainedUnit()
    if Random(count , 200) then
        BlzSetUnitMaxHP(u, R2I(BlzGetUnitMaxHP(u) * 1.2))
        SetUnitLifePercentBJ(u, 100)
        UnitAddAbility(u, FourCC('A1I8'))
    end
    u=nil
end
--===========================================================================
function InitTrig_PUnitTrained()
    gg_trg_PUnitTrained=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PUnitTrained, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PUnitTrained, Condition(Trig_PUnitTrained_Conditions))
    TriggerAddAction(gg_trg_PUnitTrained, Trig_PUnitTrained_Actions)
end
--===========================================================================
-- Trigger: Anub Vozvratka
--===========================================================================
function Trig_Anub_Vozvratka_Conditions()
    return (( GetUnitAbilityLevelSwapped(FourCC('A1LJ'), BlzGetEventDamageTarget()) > 0 )) and (( GetEventDamage() >= 2.00 )) and (( GetUnitAbilityLevelSwapped(FourCC('A1LJ'), GetEventDamageSource()) == 0 ))
end
function Trig_Anub_Vozvratka_Actions()
    UnitDamageTargetBJ(BlzGetEventDamageTarget(), GetEventDamageSource(), ( 0.50 * I2R(GetHeroStatBJ(bj_HEROSTAT_STR, BlzGetEventDamageTarget(), false)) ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
end
--===========================================================================
function InitTrig_Anub_Vozvratka()
    gg_trg_Anub_Vozvratka=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Anub_Vozvratka, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Anub_Vozvratka, Condition(Trig_Anub_Vozvratka_Conditions))
    TriggerAddAction(gg_trg_Anub_Vozvratka, Trig_Anub_Vozvratka_Actions)
end
--===========================================================================
-- Trigger: Undermining
--
-- Abilities\Spells\Undead\Impale\ImpaleMissTarget.mdl
--===========================================================================
-- ?????????? ?????????? ?????? ?????? ???
--===================================================================================================================================
-- ???????? ???????, ??? ?????? ?????? ?? ?????
--===================================================================================================================================
--================================================================================================================================================================================
-- ???? 0 - ??? ???????
--================
function UnUgolMT()
    return bj_RADTODEG * Atan2(y2 - y1, x2 - x1)
end
function UnRastMT()
    local dx= x2 - x1
    local dy= y2 - y1
    return SquareRoot(dx * dx + dy * dy)
end
--function UnParabolaZ takes real h, real d, real x returns real
 -- return (4 * h / d) * (d - x) * (x / d)
--endfunction
--h - ???????????? ?????? ? ?????? ?? ???????? ?????????? (x = d / 2),
--d - ????? ?????????? ?? ????
--x - ?????????? ?? ???????? ???? ?? ?????, ??? ??????? ????? ?????? ?? ????????.
--================================================================================================================================================================================
-- ???? 1 - ???????? ?????
--================
function Trig_Undermining_Conditions()
    return GetSpellAbilityId() == UnSkill
end
--================================================================================================================================================================================
-- ???? 3 - ???????????? ??????
--================
function Trig_Undermining_move_units()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local un= LoadUnitHandle(Hash, h, 2)
    local kol= LoadInteger(Hash, h, 3)
    local lvl
    local uron
    ---------
    SetUnitFlyHeight(un, kol * 20, 0)
    if LoadBoolean(Hash, h, 4) then
        kol=kol + 1
        SaveInteger(Hash, h, 3, kol)
        if kol >= 25 then
            SaveBoolean(Hash, h, 4, false)
        end
    else
        kol=kol - 1
        SaveInteger(Hash, h, 3, kol)
        if kol <= 1 then
            SetUnitFlyHeight(un, 0, 0)
            DestroyTimer(t)
            FlushChildHashtable(Hash, h)
            lvl=GetUnitAbilityLevel(GT, UnSkill)
            uron=UnKofDmg1 * lvl * GetHeroStr(GT, true) + lvl * UnKofDmg2
            UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
            DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsDemonDemonBoltImpactDemonBoltImpact.mdl", un, "orign"))
        end
    end
    ---------
    GT=nil
    un=nil
end
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_Undermining_move_hero()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g= LoadGroupHandle(Hash, h, 3)
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
    local dx= GetUnitX(GT)
    local dy= GetUnitY(GT)
    local gg= CreateGroup()
    local un
    local x
    local y
    local ugol= UnUgolMT(dx , x1 , dy , y1)
    local t1
    local h1
    ---------
    x=dx + 70 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 70 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    --set w = UnParabolaZ(500, l, UnRastMT(x, x1, y, y1)) //????????? ??????
    -- ???? ????? ????
    if UnRastMT(x1 , dx , y1 , dy) > 70 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsUndeadImpaleImpaleMissTarget.mdl", x, y))
        --------------------------------------
        -- ?????????? ?????? ? ?????? ? ???????????? ??
        GroupEnumUnitsInRange(gg, x, y, 150, nil)
        while true do
            un=FirstOfGroup(gg)
            if un == nil then break end
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) and not IsUnitInGroup(un, g) then
                --call BJDebugMsg("")
                UnitAddAbility(un, FourCC('Amrf'))
                UnitRemoveAbility(un, FourCC('Amrf'))
                t1=CreateTimer()
                h1=GetHandleId(t1)
                SaveUnitHandle(Hash, h1, 1, GT)
                SaveUnitHandle(Hash, h1, 2, un)
                SaveInteger(Hash, h1, 3, 1)
                SaveBoolean(Hash, h1, 4, true)
                GroupAddUnit(g, un)
                TimerStart(t1, 0.01, true, Trig_Undermining_move_units)
            end
            GroupRemoveUnit(gg, un)
        end
        -----------------------------------------
    else
        --call BJDebugMsg("")
        DestroyGroup(g)
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitFlyHeight(GT, 0, 0)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", dx, dy))
        PauseUnit(GT, false)
        ShowUnit(GT, true)
        SelectUnitAddForPlayer(GT, GetOwningPlayer(GT))
    end
    ---------
    GT=nil
    un=nil
    g=nil
    t=nil
    DestroyGroup(gg)
    gg=nil
    t1=nil
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_Undermining_Actions()
    local GT= GetTriggerUnit()
    local t= CreateTimer()
    local h= GetHandleId(t)
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= UnRastMT(x , x1 , y , y1)
    ---------
    --call BJDebugMsg("")
    SaveUnitHandle(Hash, h, 1, GT)
    SaveReal(Hash, h, 2, l)
    -- ??????????? ????
    SetSoundPosition(gg_snd_ImpaleHit, x, y, 0)
    SetSoundVolume(gg_snd_ImpaleHit, PercentToInt(100, 127))
    PlaySoundBJ(gg_snd_ImpaleHit)
    ------
    SaveGroupHandle(Hash, h, 3, CreateGroup())
    SaveReal(Hash, h, 4, x1)
    SaveReal(Hash, h, 5, y1)
    PauseUnit(GT, true)
    ShowUnit(GT, false)
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.055, true, Trig_Undermining_move_hero) --???????? ???????? ?????
    ---------
    GT=nil
    t=nil
end
--===========================================================================
function InitTrig_Undermining()
    gg_trg_Undermining=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Undermining, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Undermining, Condition(Trig_Undermining_Conditions))
    TriggerAddAction(gg_trg_Undermining, Trig_Undermining_Actions)
end
--===========================================================================
-- Trigger: PassiveAdal
--===========================================================================
function Trig_PassiveAdal_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B084')) > 0 and not IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO) and GetEventDamage() >= GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) --?? ????
end
function Adal()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1L6')) > 0 --??????
end
function Trig_PassiveAdal_Actions()
    local g= CreateGroup()
    local u= GetTriggerUnit()
    local u2
    GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 500, Adal, 1)
    u2=FirstOfGroup(g)
    if GetRandomInt(1, 4) + 0.25 * GetUnitAbilityLevel(u2, FourCC('A1L6')) > 3 and GetUnitState(u2, UNIT_STATE_MANA) > 50 then --??????
        SetUnitManaBJ(u2, GetUnitState(u2, UNIT_STATE_MANA) - 50)
        SetUnitLifePercentBJ(u, 50)
        RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanResurrectResurrectTarget.mdl", GetUnitX(u), GetUnitY(u)) , 3)
    end
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_PassiveAdal()
    gg_trg_PassiveAdal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PassiveAdal, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_PassiveAdal, Condition(Trig_PassiveAdal_Conditions))
    TriggerAddAction(gg_trg_PassiveAdal, Trig_PassiveAdal_Actions)
end
--===========================================================================
-- Trigger: ADall
--
-- Default melee game initialization for all players
--===========================================================================
function Trig_ADall_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "healingwave", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_ADall()
    gg_trg_ADall=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ADall, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_ADall, function()
        if GetSpellAbilityId() ~= FourCC('A1L1') then return end
        Trig_ADall_Actions()
    end)
end
--===========================================================================
-- Trigger: Rexan
--===========================================================================
function Trig_Rexan_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1NW')
end
function Trig_Rexan_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()) == 1
end
function Trig_Rexan_Actions()
    if Trig_Rexan_Func001C() then
        UnitAddAbilityBJ(FourCC('A1NY'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A1NY'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()))
    else
        SetUnitAbilityLevelSwapped(FourCC('A1NY'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_Rexan()
    gg_trg_Rexan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Rexan, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Rexan, Condition(Trig_Rexan_Conditions))
    TriggerAddAction(gg_trg_Rexan, Trig_Rexan_Actions)
end
--===========================================================================
-- Trigger: OgresHpSpell2
--===========================================================================
function Trig_OgresHpSpell2_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A173'), GetTriggerUnit()) == 2
end
function Trig_OgresHpSpell2_Func001Func001Func007C()
    return GetUnitLifePercent(GetTriggerUnit()) < 95.00
end
function Trig_OgresHpSpell2_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 70.00
end
function Trig_OgresHpSpell2_Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 45.00
end
function Trig_OgresHpSpell2_Actions()
    if Trig_OgresHpSpell2_Func001C() then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if Trig_OgresHpSpell2_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if Trig_OgresHpSpell2_Func001Func001Func007C() then
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
function InitTrig_OgresHpSpell2()
    gg_trg_OgresHpSpell2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgresHpSpell2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_OgresHpSpell2, Condition(Trig_OgresHpSpell2_Conditions))
    TriggerAddAction(gg_trg_OgresHpSpell2, Trig_OgresHpSpell2_Actions)
end
--===========================================================================
-- Trigger: OrgesHpSpell
--===========================================================================
function Trig_OrgesHpSpell_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A173'), GetTriggerUnit()) == 1
end
function Trig_OrgesHpSpell_Func001Func001Func007C()
    return GetUnitLifePercent(GetTriggerUnit()) < 75.00
end
function Trig_OrgesHpSpell_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 50.00
end
function Trig_OrgesHpSpell_Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 25.00
end
function Trig_OrgesHpSpell_Actions()
    if Trig_OrgesHpSpell_Func001C() then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if Trig_OrgesHpSpell_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if Trig_OrgesHpSpell_Func001Func001Func007C() then
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
function InitTrig_OrgesHpSpell()
    gg_trg_OrgesHpSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgesHpSpell, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_OrgesHpSpell, Condition(Trig_OrgesHpSpell_Conditions))
    TriggerAddAction(gg_trg_OrgesHpSpell, Trig_OrgesHpSpell_Actions)
end
--===========================================================================
-- Trigger: Gruul
--===========================================================================
function Trig_Gruul_Conditions()
    return (( GetLearnedSkillBJ() == FourCC('A18S') )) and (( GetUnitAbilityLevelSwapped(FourCC('A18S'), GetTriggerUnit()) >= 1 ))
end
function Trig_Gruul_Actions()
    UnitAddAbilityBJ(FourCC('A18T'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A18T'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A18S'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Gruul()
    gg_trg_Gruul=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Gruul, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Gruul, Condition(Trig_Gruul_Conditions))
    TriggerAddAction(gg_trg_Gruul, Trig_Gruul_Actions)
end
--===========================================================================
-- Trigger: GruulSpell
--===========================================================================
function Trig_GruulSpell_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    Gruul[pi]=GetSpellAbilityUnit()
    EnableTrigger(gg_trg_RRR)
    
    -- ????? ????? ?????? ?????? 1.10+ 0.15 ?????? ???
    TriggerSleepAction(( 1.10 + ( 0.15 * I2R(GetUnitAbilityLevel(Gruul[pi], FourCC('A18Q'))) ) ))
    
    
    DisableTrigger(gg_trg_RRR)
    -- ??????? ??????????
    Gruul[pi]=nil
end
--===========================================================================
function InitTrig_GruulSpell()
    gg_trg_GruulSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GruulSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GruulSpell, function()
        if GetSpellAbilityId() ~= FourCC('A18Q') then return end
        Trig_GruulSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: BegYel
--===========================================================================
function Trig_BegYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_BegYel_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegYel_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegYel_Actions()
    if Trig_BegYel_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegYel_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegYel()
    gg_trg_BegYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegYel, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegYel, Condition(Trig_BegYel_Conditions))
    TriggerAddAction(gg_trg_BegYel, Trig_BegYel_Actions)
end
--===========================================================================
-- Trigger: CanYel
--===========================================================================
function Trig_CanYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_CanYel_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanYel_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanYel_Actions()
    if Trig_CanYel_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanYel_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanYel()
    gg_trg_CanYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanYel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanYel, Condition(Trig_CanYel_Conditions))
    TriggerAddAction(gg_trg_CanYel, Trig_CanYel_Actions)
end
--===========================================================================
-- Trigger: FinYel
--===========================================================================
function Trig_FinYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_FinYel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinYel()
    gg_trg_FinYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinYel, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinYel, Condition(Trig_FinYel_Conditions))
    TriggerAddAction(gg_trg_FinYel, Trig_FinYel_Actions)
end
--===========================================================================
-- Trigger: BegRed
--===========================================================================
function Trig_BegRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_BegRed_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegRed_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegRed_Actions()
    if Trig_BegRed_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegRed_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegRed()
    gg_trg_BegRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegRed, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegRed, Condition(Trig_BegRed_Conditions))
    TriggerAddAction(gg_trg_BegRed, Trig_BegRed_Actions)
end
--===========================================================================
-- Trigger: CanRed
--===========================================================================
function Trig_CanRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_CanRed_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanRed_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanRed_Actions()
    if Trig_CanRed_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanRed_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanRed()
    gg_trg_CanRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanRed, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanRed, Condition(Trig_CanRed_Conditions))
    TriggerAddAction(gg_trg_CanRed, Trig_CanRed_Actions)
end
--===========================================================================
-- Trigger: FinRed
--===========================================================================
function Trig_FinRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_FinRed_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03S'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinRed()
    gg_trg_FinRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinRed, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinRed, Condition(Trig_FinRed_Conditions))
    TriggerAddAction(gg_trg_FinRed, Trig_FinRed_Actions)
end
--===========================================================================
-- Trigger: BegBlue
--===========================================================================
function Trig_BegBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_BegBlue_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegBlue_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegBlue_Actions()
    if Trig_BegBlue_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegBlue_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegBlue()
    gg_trg_BegBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegBlue, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegBlue, Condition(Trig_BegBlue_Conditions))
    TriggerAddAction(gg_trg_BegBlue, Trig_BegBlue_Actions)
end
--===========================================================================
-- Trigger: CanBlue
--===========================================================================
function Trig_CanBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_CanBlue_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanBlue_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanBlue_Actions()
    if Trig_CanBlue_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanBlue_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanBlue()
    gg_trg_CanBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanBlue, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanBlue, Condition(Trig_CanBlue_Conditions))
    TriggerAddAction(gg_trg_CanBlue, Trig_CanBlue_Actions)
end
--===========================================================================
-- Trigger: FinBlue
--===========================================================================
function Trig_FinBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_FinBlue_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03R'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinBlue()
    gg_trg_FinBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinBlue, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinBlue, Condition(Trig_FinBlue_Conditions))
    TriggerAddAction(gg_trg_FinBlue, Trig_FinBlue_Actions)
end
--===========================================================================
-- Trigger: Begred
--===========================================================================
function Trig_Begred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Begred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Begred()
    gg_trg_Begred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Begred, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Begred, Condition(Trig_Begred_Conditions))
    TriggerAddAction(gg_trg_Begred, Trig_Begred_Actions)
end
--===========================================================================
-- Trigger: Canred
--===========================================================================
function Trig_Canred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Canred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Canred()
    gg_trg_Canred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Canred, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Canred, Condition(Trig_Canred_Conditions))
    TriggerAddAction(gg_trg_Canred, Trig_Canred_Actions)
end
--===========================================================================
-- Trigger: Finred
--===========================================================================
function Trig_Finred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Finred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03V'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Finred()
    gg_trg_Finred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Finred, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Finred, Condition(Trig_Finred_Conditions))
    TriggerAddAction(gg_trg_Finred, Trig_Finred_Actions)
end
--===========================================================================
-- Trigger: BegWhite
--===========================================================================
function Trig_BegWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_BegWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegWhite()
    gg_trg_BegWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegWhite, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegWhite, Condition(Trig_BegWhite_Conditions))
    TriggerAddAction(gg_trg_BegWhite, Trig_BegWhite_Actions)
end
--===========================================================================
-- Trigger: CanWhite
--===========================================================================
function Trig_CanWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_CanWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanWhite()
    gg_trg_CanWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanWhite, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanWhite, Condition(Trig_CanWhite_Conditions))
    TriggerAddAction(gg_trg_CanWhite, Trig_CanWhite_Actions)
end
--===========================================================================
-- Trigger: FinWhite
--===========================================================================
function Trig_FinWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_FinWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03U'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinWhite()
    gg_trg_FinWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinWhite, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinWhite, Condition(Trig_FinWhite_Conditions))
    TriggerAddAction(gg_trg_FinWhite, Trig_FinWhite_Actions)
end
--===========================================================================
-- Trigger: BegBlack
--===========================================================================
function Trig_BegBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_BegBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegBlack()
    gg_trg_BegBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegBlack, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegBlack, Condition(Trig_BegBlack_Conditions))
    TriggerAddAction(gg_trg_BegBlack, Trig_BegBlack_Actions)
end
--===========================================================================
-- Trigger: CanBlack
--===========================================================================
function Trig_CanBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_CanBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanBlack()
    gg_trg_CanBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanBlack, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanBlack, Condition(Trig_CanBlack_Conditions))
    TriggerAddAction(gg_trg_CanBlack, Trig_CanBlack_Actions)
end
--===========================================================================
-- Trigger: FinBlack
--===========================================================================
function Trig_FinBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_FinBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03T'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinBlack()
    gg_trg_FinBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinBlack, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinBlack, Condition(Trig_FinBlack_Conditions))
    TriggerAddAction(gg_trg_FinBlack, Trig_FinBlack_Actions)
end
--===========================================================================
-- Trigger: UltDanath
--
-- ??? ??????? ???????. ??????? ?????????? ??????????.
-- ? ????????: (Ability beng cast) ????? ""
-- ???????? ????????:
-- 1. ??????? ????????? ?????????? ?????
-- 2. ???? ????? ?? ???????? ??????????? ??????????? "", ??????????? ""
-- 3. ? ????????? ?????????? ????? ????????? ????? ?? ???????? ????????? ???????????
-- 4. ??????? ??????? ? ????? ????? ?????????????? ???????????
-- 5. ?? ????????? ??????? ???????? ? ????? ?????????????? ???????????
-- ? 5 ?????? 'AEev' - ??? ??? ??????????? '??????? ????????'
-- ???? ???-?? ?? ??????? - ?????????.
-- by Dragonear for xgm.guru
--===========================================================================
function Trig_UltDanath_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A17T'))
    RemoveAbilityTimed(u , FourCC('A17T') , 60)
    u=nil
end
--===========================================================================
function InitTrig_UltDanath()
    gg_trg_UltDanath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UltDanath, EVENT_PLAYER_UNIT_SPELL_CHANNEL)
    TriggerAddAction(gg_trg_UltDanath, function()
        if GetSpellAbilityId() ~= FourCC('A17S') then return end
        Trig_UltDanath_Actions()
    end)
end
--===========================================================================
-- Trigger: GeneralRegen
--===========================================================================
function Trig_GeneralRegen_Conditions()
    return GetLearnedSkillBJ() == FourCC('A0Y8')
end
function Trig_GeneralRegen_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()) == 1
end
function Trig_GeneralRegen_Actions()
    if Trig_GeneralRegen_Func001C() then
        UnitAddAbilityBJ(FourCC('A104'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A104'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()))
    else
        SetUnitAbilityLevelSwapped(FourCC('A104'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_GeneralRegen()
    gg_trg_GeneralRegen=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GeneralRegen, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_GeneralRegen, Condition(Trig_GeneralRegen_Conditions))
    TriggerAddAction(gg_trg_GeneralRegen, Trig_GeneralRegen_Actions)
end
--===========================================================================
-- Trigger: Pribavka k zoloty
--===========================================================================
function Trig_Pribavka_k_zoloty_Actions()
    AdjustPlayerStateBJ(( 2000 * GetUnitAbilityLevelSwapped(FourCC('A0ZN'), GetTriggerUnit()) ), GetOwningPlayer(GetTriggerUnit()), PLAYER_STATE_RESOURCE_GOLD)
end
--===========================================================================
function InitTrig_Pribavka_k_zoloty()
    gg_trg_Pribavka_k_zoloty=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pribavka_k_zoloty, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Pribavka_k_zoloty, function()
        if GetSpellAbilityId() ~= FourCC('A0ZN') then return end
        Trig_Pribavka_k_zoloty_Actions()
    end)
end
--===========================================================================
-- Trigger: StromgardOn
--===========================================================================
function Trig_StromgardOn_Actions()
    EnableTrigger(gg_trg_PaladinTank)
    EnableTrigger(gg_trg_PaladinVozdoyn)
    EnableTrigger(gg_trg_PaladinHeal)
    
    EnableTrigger(gg_trg_Tank1)
    EnableTrigger(gg_trg_Heal1)
    EnableTrigger(gg_trg_Vozdoyanie1)
    EnableTrigger(gg_trg_Tank2)
    EnableTrigger(gg_trg_Heal2)
    EnableTrigger(gg_trg_Vozdoyanie2)
    EnableTrigger(gg_trg_Priziv)
    EnableTrigger(gg_trg_Priziv2)
    EnableTrigger(gg_trg_Proffesian)
    EnableTrigger(gg_trg_Professian2)
    EnableTrigger(gg_trg_MassArmy)
    EnableTrigger(gg_trg_UpSystem)
    EnableTrigger(gg_trg_MassArmy)
    EnableTrigger(gg_trg_ShieldUp)
    EnableTrigger(gg_trg_MassArmy)
    
    
    
    
end
--===========================================================================
function InitTrig_StromgardOn()
    gg_trg_StromgardOn=CreateTrigger()
    TriggerAddAction(gg_trg_StromgardOn, Trig_StromgardOn_Actions)
end
--===========================================================================
-- Trigger: Priziv2
--===========================================================================
function Trig_Priziv2_Conditions()
    return GetResearched() == FourCC('R0D6')
end
function Trig_Priziv2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D5'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Priziv2()
    gg_trg_Priziv2=CreateTrigger()
    DisableTrigger(gg_trg_Priziv2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Priziv2, Condition(Trig_Priziv2_Conditions))
    TriggerAddAction(gg_trg_Priziv2, Trig_Priziv2_Actions)
end
--===========================================================================
-- Trigger: Priziv
--===========================================================================
function Trig_Priziv_Conditions()
    return GetResearched() == FourCC('R0D6')
end
function Trig_Priziv_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D5'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Priziv()
    gg_trg_Priziv=CreateTrigger()
    DisableTrigger(gg_trg_Priziv)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Priziv, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Priziv, Condition(Trig_Priziv_Conditions))
    TriggerAddAction(gg_trg_Priziv, Trig_Priziv_Actions)
end
--===========================================================================
-- Trigger: Professian2
--===========================================================================
function Trig_Professian2_Conditions()
    return GetResearched() == FourCC('R0D5')
end
function Trig_Professian2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D6'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Professian2()
    gg_trg_Professian2=CreateTrigger()
    DisableTrigger(gg_trg_Professian2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Professian2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Professian2, Condition(Trig_Professian2_Conditions))
    TriggerAddAction(gg_trg_Professian2, Trig_Professian2_Actions)
end
--===========================================================================
-- Trigger: Proffesian
--===========================================================================
function Trig_Proffesian_Conditions()
    return GetResearched() == FourCC('R0D5')
end
function Trig_Proffesian_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0D6'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Proffesian()
    gg_trg_Proffesian=CreateTrigger()
    DisableTrigger(gg_trg_Proffesian)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Proffesian, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Proffesian, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Proffesian, Condition(Trig_Proffesian_Conditions))
    TriggerAddAction(gg_trg_Proffesian, Trig_Proffesian_Actions)
end
--===========================================================================
-- Trigger: MassArmy
--===========================================================================
function Trig_MassArmy_Conditions()
    local id=GetUnitTypeId(GetTrainedUnit())
    return GetPlayerTechCountSimple(FourCC('R0D6'), GetOwningPlayer(GetTriggerUnit())) == 1 and ( id == FourCC('h0GS') or id == FourCC('h0GV') or id == FourCC('h0GU') or id == FourCC('h0GW') or id == FourCC('h0GX') or id == FourCC('h0L3') )
end
function Trig_MassArmy_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local u=  CreateUnitAtLoc(GetOwningPlayer(GetTriggerUnit()), GetUnitTypeId(GetTrainedUnit()), l, bj_UNIT_FACING)
    RemoveLocation(l)
    l=GetUnitRallyPoint(GetTriggerUnit())
    IssuePointOrderLoc(GetTrainedUnit(), "move", l)
    IssuePointOrderLoc(u, "move", l)
    RemoveLocation(l)
    l=nil
    u=nil
end
--===========================================================================
function InitTrig_MassArmy()
    gg_trg_MassArmy=CreateTrigger()
    DisableTrigger(gg_trg_MassArmy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassArmy, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_MassArmy, Condition(Trig_MassArmy_Conditions))
    TriggerAddAction(gg_trg_MassArmy, Trig_MassArmy_Actions)
end
--===========================================================================
-- Trigger: UpSystem
--===========================================================================
function Trig_UpSystem_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ()) >= 1
end
function Trig_UpSystem_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ()) >= 2
end
function Trig_UpSystem_Actions()
    if Trig_UpSystem_Func001C() then
        udg_LocalUnit2=GetKillingUnitBJ()
        ReplaceUnit(udg_LocalUnit2 , FourCC('h0HE') , bj_UNIT_STATE_METHOD_RELATIVE)
    else
        IncUnitAbilityLevelSwapped(FourCC('A0VI'), GetKillingUnitBJ())
    end
end
--===========================================================================
function InitTrig_UpSystem()
    gg_trg_UpSystem=CreateTrigger()
    DisableTrigger(gg_trg_UpSystem)
    TriggerRegisterAnyUnitEventBJ(gg_trg_UpSystem, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_UpSystem, Condition(Trig_UpSystem_Conditions))
    TriggerAddAction(gg_trg_UpSystem, Trig_UpSystem_Actions)
end
--===========================================================================
-- Trigger: ShieldUp
--===========================================================================
function Trig_ShieldUp_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0WI'), GetTriggerUnit()) == 1
end
function Trig_ShieldUp_Actions()
    if Trig_ShieldUp_Func001C() then
        UnitRemoveAbilityBJ(FourCC('A0WI'), GetTriggerUnit())
    else
        UnitAddAbilityBJ(FourCC('A0WI'), GetTriggerUnit())
    end
end
--===========================================================================
function InitTrig_ShieldUp()
    gg_trg_ShieldUp=CreateTrigger()
    DisableTrigger(gg_trg_ShieldUp)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShieldUp, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ShieldUp, function()
        if GetSpellAbilityId() ~= FourCC('A0WG') then return end
        Trig_ShieldUp_Actions()
    end)
end
--===========================================================================
-- Trigger: EnterKazna
--===========================================================================
function Trig_EnterKazna_Conditions()
    return GetLearnedSkill() == FourCC('A0XV')
end
function Trig_EnterKazna_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    income[pi]=income[pi] + ( 100 + GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0XV')) * 100 )
    -- ??????????? ????? ? ??????? ????? ?????????
end
--===========================================================================
function InitTrig_EnterKazna()
    gg_trg_EnterKazna=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EnterKazna, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_EnterKazna, Condition(Trig_EnterKazna_Conditions))
    TriggerAddAction(gg_trg_EnterKazna, Trig_EnterKazna_Actions)
end
--===========================================================================
-- Trigger: ChillBonus
--===========================================================================
function Trig_ChillBonus_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('A1R3')) > 0 and GetUnitAbilityLevel(GetKillingUnit(), FourCC('A1R5')) == 0
end
function Trig_ChillBonus_Actions()
        UnitAddAbility(GetKillingUnit(), FourCC('A1R5'))
        RemoveAbilityTimed(GetKillingUnit() , FourCC('A1R5') , 9)
end
--===========================================================================
function InitTrig_ChillBonus()
    gg_trg_ChillBonus=CreateTrigger()
    --call DisableTrigger( gg_trg_ChillBonus )
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChillBonus, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_ChillBonus, Condition(Trig_ChillBonus_Conditions))
    TriggerAddAction(gg_trg_ChillBonus, Trig_ChillBonus_Actions)
end
--===========================================================================
-- Trigger: Passive
--===========================================================================
function Trig_Passive_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1CJ')
end
function Trig_Passive_Actions()
    UnitAddAbilityBJ(FourCC('A1CI'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1CI'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1CJ'), GetTriggerUnit()))
    UnitAddAbilityBJ(FourCC('A1CH'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A1CH'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1CJ'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Passive()
    gg_trg_Passive=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Passive, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Passive, Condition(Trig_Passive_Conditions))
    TriggerAddAction(gg_trg_Passive, Trig_Passive_Actions)
end
--===========================================================================
-- Trigger: Sluga qqgsarona
--===========================================================================
function Trig_Sluga_qqgsarona_Func010A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12G'), GetEnumPlayer())
end
function Trig_Sluga_qqgsarona_Func012001002()
    return IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups)
end
function Trig_Sluga_qqgsarona_Func012A()
    GroupRemoveUnitSimple(GetEnumUnit(), udg_StolicaGroups)
    ReplaceUnitBJ(GetEnumUnit(), GetUnitTypeId(GetEnumUnit()), bj_UNIT_STATE_METHOD_RELATIVE)
end
function Trig_Sluga_qqgsarona_Func017A()
    UnitShareVisionBJ(true, gg_unit_n03A_0657, GetEnumPlayer())
end
function Trig_Sluga_qqgsarona_Actions()
    SetUnitOwner(gg_unit_n03A_0657, GetOwningPlayer(GetSpellAbilityUnit()), true)
    RemoveUnit(gg_unit_n03C_0660)
    RemoveUnit(gg_unit_n03C_0661)
    RemoveUnit(gg_unit_n03C_0663)
    RemoveUnit(gg_unit_n03C_0662)
    RemoveUnit(gg_unit_n03B_0664)
    RemoveUnit(gg_unit_n03B_0665)
    RemoveUnit(gg_unit_n03B_0658)
    RemoveUnit(gg_unit_n03B_0659)
    ForForce(GetPlayersAll(), Trig_Sluga_qqgsarona_Func010A)
    -- --
    ForGroupBJ(GetUnitsOfPlayerMatching(GetOwningPlayer(GetTriggerUnit()), Condition(Trig_Sluga_qqgsarona_Func012001002)), Trig_Sluga_qqgsarona_Func012A)
    GroupAddUnitSimple(gg_unit_n03A_0657, udg_StolicaGroups)
    BlzSetUnitStringFieldBJ(gg_unit_n03A_0657, UNIT_SF_NAME, ( "cffd45e19r" .. GetUnitName(gg_unit_n03A_0657) ))
    ForForce(GetPlayersAll(), Trig_Sluga_qqgsarona_Func017A)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Sluga_qqgsarona()
    gg_trg_Sluga_qqgsarona=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sluga_qqgsarona, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Sluga_qqgsarona, function()
        if GetSpellAbilityId() ~= FourCC('A12G') then return end
        Trig_Sluga_qqgsarona_Actions()
    end)
end
--===========================================================================
-- Trigger: Sila2
--===========================================================================
function Trig_Sila2_Conditions()
    return GetResearched() == FourCC('R0F7')
end
function Trig_Sila2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F8'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sila2()
    gg_trg_Sila2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Sila2, Condition(Trig_Sila2_Conditions))
    TriggerAddAction(gg_trg_Sila2, Trig_Sila2_Actions)
end
--===========================================================================
-- Trigger: Sila1
--===========================================================================
function Trig_Sila1_Conditions()
    return GetResearched() == FourCC('R0F7')
end
function Trig_Sila1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F8'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Sila1()
    gg_trg_Sila1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Sila1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Sila1, Condition(Trig_Sila1_Conditions))
    TriggerAddAction(gg_trg_Sila1, Trig_Sila1_Actions)
end
--===========================================================================
-- Trigger: Skorost2
--===========================================================================
function Trig_Skorost2_Conditions()
    return GetResearched() == FourCC('R0F8')
end
function Trig_Skorost2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F7'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Skorost2()
    gg_trg_Skorost2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Skorost2, Condition(Trig_Skorost2_Conditions))
    TriggerAddAction(gg_trg_Skorost2, Trig_Skorost2_Actions)
end
--===========================================================================
-- Trigger: Skorost1
--===========================================================================
function Trig_Skorost1_Conditions()
    return GetResearched() == FourCC('R0F8')
end
function Trig_Skorost1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0F7'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Skorost1()
    gg_trg_Skorost1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Skorost1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Skorost1, Condition(Trig_Skorost1_Conditions))
    TriggerAddAction(gg_trg_Skorost1, Trig_Skorost1_Actions)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik
--===========================================================================
function Trig_ZdaniyaBezlik_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01T'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik()
    gg_trg_ZdaniyaBezlik=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik, function()
        if GetSpellAbilityId() ~= FourCC('A0LK') then return end
        Trig_ZdaniyaBezlik_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01Q'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy()
    gg_trg_ZdaniyaBezlik_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LN') then return end
        Trig_ZdaniyaBezlik_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01S'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy()
    gg_trg_ZdaniyaBezlik_Copy_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LM') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy 2
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_2_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01R'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy_2()
    gg_trg_ZdaniyaBezlik_Copy_Copy_2=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy_2)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy_2, function()
        if GetSpellAbilityId() ~= FourCC('A0LO') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_2_Actions()
    end)
end
--===========================================================================
-- Trigger: ZdaniyaBezlik Copy Copy 2 Copy
--===========================================================================
function Trig_ZdaniyaBezlik_Copy_Copy_2_Copy_Actions()
    udg_Untitled_Variable_001[GetConvertedPlayerId(GetOwningPlayer(GetSpellAbilityUnit()))]=GetSpellTargetLoc()
    CreateNUnitsAtLoc(1, FourCC('n01U'), GetOwningPlayer(GetTriggerUnit()), udg_Untitled_Variable_001[1], bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_ZdaniyaBezlik_Copy_Copy_2_Copy()
    gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy=CreateTrigger()
    DisableTrigger(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy)
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZdaniyaBezlik_Copy_Copy_2_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A0LP') then return end
        Trig_ZdaniyaBezlik_Copy_Copy_2_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: CreateFFarm
--===========================================================================
function Trig_CreateFFarm_Actions()
    FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CreateFFarm()
    gg_trg_CreateFFarm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CreateFFarm, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_CreateFFarm, function()
        if GetSpellAbilityId() ~= FourCC('A11G') then return end
        Trig_CreateFFarm_Actions()
    end)
end
--===========================================================================
-- Trigger: DeadFFarm
--===========================================================================
function Trig_DeadFFarm_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('u02E')
end
function Trig_DeadFFarm_Actions()
    FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DeadFFarm()
    gg_trg_DeadFFarm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadFFarm, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DeadFFarm, Condition(Trig_DeadFFarm_Conditions))
    TriggerAddAction(gg_trg_DeadFFarm, Trig_DeadFFarm_Actions)
end
--===========================================================================
-- Trigger: FinishFaceBuild
--===========================================================================
function Trig_FinishFaceBuild_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h0HZ')
end
function Trig_FinishFaceBuild_Actions()
    GroupAddUnitSimple(GetConstructedStructure(), udg_FacelessLumberBuildings)
end
--===========================================================================
function InitTrig_FinishFaceBuild()
    gg_trg_FinishFaceBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinishFaceBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FinishFaceBuild, Condition(Trig_FinishFaceBuild_Conditions))
    TriggerAddAction(gg_trg_FinishFaceBuild, Trig_FinishFaceBuild_Actions)
end
--===========================================================================
-- Trigger: DeadFaceBuild
--===========================================================================
function Trig_DeadFaceBuild_Conditions()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0HZ')
end
function Trig_DeadFaceBuild_Actions()
    GroupRemoveUnitSimple(GetTriggerUnit(), udg_FacelessLumberBuildings)
end
--===========================================================================
function InitTrig_DeadFaceBuild()
    gg_trg_DeadFaceBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DeadFaceBuild, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DeadFaceBuild, Condition(Trig_DeadFaceBuild_Conditions))
    TriggerAddAction(gg_trg_DeadFaceBuild, Trig_DeadFaceBuild_Actions)
end
--===========================================================================
-- Trigger: LumberTest
--===========================================================================
function KillTextTag()
    local t= TT
    TriggerSleepAction(3)
    DestroyTextTag(t)
    t=nil
end
function TT2()
    local t= CreateTextTag()
    local p= Player(0)
    local s= I2S(5)
    local f= GetEnumDestructable()
    local l= Location(GetDestructableX(f), GetDestructableY(f))
    
    DisplayTextToPlayer(Player(0), 0, 0, "")
    AdjustPlayerStateBJ(5, p, PLAYER_STATE_RESOURCE_LUMBER)
    
    
    t=CreateTextTagLocBJ(s, l, 0, 10, 0.00, 100, 0.00, 0)
    SetTextTagPermanent(t, false)
    SetTextTagLifespan(t, 3.00)
    SetTextTagVelocity(t, 50.00, 90)
    SetTextTagFadepoint(t, 1.00)
    RemoveLocation(l)
    l=nil
    f=nil
    TT=t
    t=nil
    p=nil
    s=nil
    ExecuteFunc("KillTextTag")
end
    
function Trig_LumberTest_Actions()
    local g= CreateGroup()
    local d
    local u= nil
    local l
    local r
    
    local radius
    local centerX
    local centerY
    --call DisplayTextToPlayer(Player(0),0,0,"0")
    GroupAddGroup(udg_FacelessLumberBuildings, g)
    --call DisplayTextToPlayer(Player(0),0,0, I2S(CountUnitsInGroup(g)))
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        DisplayTextToPlayer(Player(0), 0, 0, "")
        udg_LocalPlayer=GetOwningPlayer(u)
        l=GetUnitLoc(u)
        --call EnumDestructablesInCircleBJ( 500.00, l, function TT2 )
        
        
        radius=650
        
        --set r = GetRectFromCircleBJ(loc, radius)
        --set centerX = GetLocationX(l)
        --set centerY = GetLocationY(l)
        
        bj_enumDestructableCenter=l
        bj_enumDestructableRadius=radius
        r=GetRectFromCircleBJ(l, radius)
        --set r = Rect(centerX - radius, centerY - radius, centerX + radius, centerY + radius)
        DisplayTextToPlayer(Player(0), 0, 0, "2")
        EnumDestructablesInRect(r, filterEnumDestructablesInCircleBJ, TT2)
        RemoveRect(r)
        
        
        
        
        
        
        RemoveLocation(l)
        GroupRemoveUnit(g, u)
        r=nil
        l=nil
        TriggerSleepAction(0.01)
    end
    RemoveRect(r)
    r=nil
    RemoveLocation(l)
    l=nil
    DestroyGroup(g)
    u=nil
    g=nil
end
--===========================================================================
function InitTrig_LumberTest()
    gg_trg_LumberTest=CreateTrigger()
    DisableTrigger(gg_trg_LumberTest)
    TriggerRegisterTimerEventPeriodic(gg_trg_LumberTest, 5.00)
    TriggerAddAction(gg_trg_LumberTest, Trig_LumberTest_Actions)
end
--===========================================================================
-- Trigger: Spell2
--===========================================================================
function Trig_Spell2_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('A122')) == 1 and not IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE)
end
function Trig_Spell2_Actions()
    UnitDamageTargetBJ(GetAttacker(), GetTriggerUnit(), ( GetUnitStateSwap(UNIT_STATE_MAX_LIFE, GetTriggerUnit()) * 0.014 ), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_COLD)
end
--===========================================================================
function InitTrig_Spell2()
    gg_trg_Spell2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_Spell2, Condition(Trig_Spell2_Conditions))
    TriggerAddAction(gg_trg_Spell2, Trig_Spell2_Actions)
end
--===========================================================================
-- Trigger: SpellRes
--===========================================================================
function Trig_SpellRes_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A123'), GetKillingUnitBJ()) == 1
end
function Trig_SpellRes_Actions()
    BlzEndUnitAbilityCooldown(GetKillingUnitBJ(), FourCC('A123'))
end
--===========================================================================
function InitTrig_SpellRes()
    gg_trg_SpellRes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellRes, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_SpellRes, Condition(Trig_SpellRes_Conditions))
    TriggerAddAction(gg_trg_SpellRes, Trig_SpellRes_Actions)
end
--===========================================================================
-- Trigger: Muscules
--===========================================================================
function Trig_Muscules_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A0PQ'))
    TriggerSleepAction(20.00)
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0PQ') , 20)
end
--===========================================================================
function InitTrig_Muscules()
    gg_trg_Muscules=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Muscules, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Muscules, function()
        if GetSpellAbilityId() ~= FourCC('A0QS') then return end
        Trig_Muscules_Actions()
    end)
end
--===========================================================================
-- Trigger: BuidingThatSellRecruts
--===========================================================================
function Trig_BuidingThatSellRecruts_Conditions()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('h0NX') -- ????????? ??????, ??????
end
function NewMember()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 1)
    local uid= GetHandleId(u)
    if UnitAlive(u) then
        SaveInteger(Hash, uid, 1, IMaxBJ(LoadInteger(Hash, uid, 1) + 1, 3))
    
    else
        
        DestroyTimer(t)
        FlushChildHashtable(Hash, id)
        FlushChildHashtable(Hash, uid)
    end
    t=nil
    u=nil
end
function Trig_BuidingThatSellRecruts_Actions()
    local u= GetConstructedStructure()
    local t= CreateTimer()
    local id= GetHandleId(t)
    local uid= GetHandleId(u)
    local startCount= 1
    UnitAddAbility(u, FourCC('Asud'))
    AddUnitToStock(u, FourCC('h0NC'), startCount, 3) --???? ??????? ?????????
    AddUnitToStock(u, FourCC('h0NL'), startCount, 3) --???? ??????? ?????????
    
    TimerStart(t, 30, true, NewMember)
    SaveUnitHandle(Hash, id, 1, u)
    SaveInteger(Hash, uid, 1, startCount)
    u=nil
    t=nil
end
--===========================================================================
function InitTrig_BuidingThatSellRecruts()
    gg_trg_BuidingThatSellRecruts=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidingThatSellRecruts, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_BuidingThatSellRecruts, Condition(Trig_BuidingThatSellRecruts_Conditions))
    TriggerAddAction(gg_trg_BuidingThatSellRecruts, Trig_BuidingThatSellRecruts_Actions)
end
--
--      call AddUnitToStockBJ( 'hfoo', GetTriggerUnit(), 0, 1 )
--    call RemoveUnitFromStockBJ( 'hfoo', GetTriggerUnit() )
--===========================================================================
-- Trigger: BuidingSell
--===========================================================================
function Trig_BuidingSell_Conditions()
    return GetUnitTypeId(GetSellingUnit()) == FourCC('h0NX') -- ????????? ??????, ??????
end
function Trig_BuidingSell_Actions()
    local u= GetSellingUnit()
    local uid= GetHandleId(u)
    local currentCount= LoadInteger(Hash, uid, 1)
    SaveInteger(Hash, uid, 1, currentCount - 1)
    RemoveUnitFromStock(u, FourCC('h0NC')) --???? ??????? ?????????
    RemoveUnitFromStock(u, FourCC('h0NL')) --???? ??????? ?????????
    
    AddUnitToStock(u, FourCC('h0NC'), currentCount - 1, 3) --???? ??????? ?????????
    AddUnitToStock(u, FourCC('h0NL'), currentCount - 1, 3) --???? ??????? ?????????
    
    
end
--===========================================================================
function InitTrig_BuidingSell()
    gg_trg_BuidingSell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidingSell, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_BuidingSell, Condition(Trig_BuidingSell_Conditions))
    TriggerAddAction(gg_trg_BuidingSell, Trig_BuidingSell_Actions)
end
--
--      call AddUnitToStockBJ( 'hfoo', GetTriggerUnit(), 0, 1 )
--    call RemoveUnitFromStockBJ( 'hfoo', GetTriggerUnit() )
--===========================================================================
-- Trigger: JumpSTR
--===========================================================================
-- ?????????? ?????????? ?????? ?????? ???
--===================================================================================================================================
-- ???????? ???????, ??? ?????? ?????? ?? ?????
--===================================================================================================================================
--================================================================================================================================================================================
-- ???? 0 - ??? ???????
--================
function JSTRUgolMT()
    return bj_RADTODEG * Atan2(y2 - y1, x2 - x1)
end
function JSTRRastMT()
    local dx= x2 - x1
    local dy= y2 - y1
    return SquareRoot(dx * dx + dy * dy)
end
function JSTRParabolaZ()
  return ( 4 * h / d ) * ( d - x ) * ( x / d )
end
--h - ???????????? ?????? ? ?????? ?? ???????? ?????????? (x = d / 2),
--d - ????? ?????????? ?? ????
--x - ?????????? ?? ???????? ???? ?? ?????, ??? ??????? ????? ?????? ?? ????????.
--================================================================================================================================================================================
-- ???? 1 - ???????? ????? - ????? ??? ??? ??????)))
--================
function Trig_JumpSTR_Conditions()
end
--================================================================================================================================================================================
-- ???? 3 - ??????? ??????
--================
function Trig_JumpSTR_move_units()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local un= LoadUnitHandle(Hash, h, 1)
    local ugol= LoadReal(Hash, h, 2)
    local kol= LoadInteger(Hash, h, 3)
    local x= GetUnitX(un)
    local y= GetUnitY(un)
    -- ---------
    x=x + 10 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=y + 10 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    if kol >= 0 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
        SetUnitX(un, x)
        SetUnitY(un, y)
        SaveInteger(Hash, h, 3, kol - 1)
    else
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
    end
    -- ----------
    un=nil
    t=nil
end
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_JumpSTR_move_hero()
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
        SetUnitFlyHeight(GT, w, 0)
    else
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "attack")
        SetUnitFlyHeight(GT, 0, 0)
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
function Trig_JumpSTR_Actions()
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
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.025, true, Trig_JumpSTR_move_hero) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_JumpSTR()
    gg_trg_JumpSTR=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_JumpSTR, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_JumpSTR, function()
        if GetSpellAbilityId() ~= FourCC('A1E2') then return end
        if not Trig_JumpSTR_Conditions() then return end
        Trig_JumpSTR_Actions()
    end)
end
--===========================================================================
-- Trigger: TrainW2
--===========================================================================
function Trig_TrainW2_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('w2a0')) > 0
end
function Trig_TrainW2_Actions()
    local u= GetTrainedUnit()
    local uh= GetHandleId(u)
    local p= GetOwningPlayer(u)
    local r
    SaveInteger(Hash, uh, 0, 0) --StringHash("lvl"),0)
    SaveReal(Hash, uh, 1, 0) --StringHash("xp"),0)
    
    r=GetPlayerTechCount(p, FourCC('w2r3'), true)
    if r > 0 then
        AddXp(u , 100 * r + 25 * r)
    end
    
    u=nil
end
--===========================================================================
function InitTrig_TrainW2()
    gg_trg_TrainW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainW2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainW2, Condition(Trig_TrainW2_Conditions))
    TriggerAddAction(gg_trg_TrainW2, Trig_TrainW2_Actions)
end
--===========================================================================
-- Trigger: DamagerW2
--===========================================================================
function Trig_DamagerW2_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_DamagerW2_Actions()
    local u= GetEventDamageSource()
    local damage= GetEventDamage()
    AddXp(u , damage * 0.25)
    
    u=nil
end
--===========================================================================
function InitTrig_DamagerW2()
    gg_trg_DamagerW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamagerW2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamagerW2, Condition(Trig_DamagerW2_Conditions))
    TriggerAddAction(gg_trg_DamagerW2, Trig_DamagerW2_Actions)
end
--===========================================================================
-- Trigger: DamageBeforeW2
--===========================================================================
function Trig_DamageBeforeW2_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('w2a0')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL
end
function Trig_DamageBeforeW2_Actions()
    local u= GetEventDamageSource()
    local uh= GetHandleId(u)
    local lvl= LoadInteger(Hash, uh, 0)
    local damage= GetEventDamage()
    
    DisableTrigger(gg_trg_DamageBeforeW2)
    DisableTrigger(gg_trg_DamagerW2)
    if u ~= nil then
        UnitDamageTargetBJ(u, GetTriggerUnit(), damage * 0.02 * lvl, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL)
    else
        UnitDamageTargetBJ(GetTriggerUnit(), GetTriggerUnit(), damage * 0.02 * lvl, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL)
    end
    EnableTrigger(gg_trg_DamageBeforeW2)
    EnableTrigger(gg_trg_DamagerW2)
        
    
    u=nil
end
--===========================================================================
function InitTrig_DamageBeforeW2()
    gg_trg_DamageBeforeW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamageBeforeW2, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_DamageBeforeW2, Condition(Trig_DamageBeforeW2_Conditions))
    TriggerAddAction(gg_trg_DamageBeforeW2, Trig_DamageBeforeW2_Actions)
end
--===========================================================================
-- Trigger: DamagedW2
--===========================================================================
function Trig_DamagedW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_DamagedW2_Actions()
    local u= GetTriggerUnit()
    local Damage= GetEventDamage()
    
    
    
    AddXp(u , Damage * 0.25)
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_DamagedW2()
    gg_trg_DamagedW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamagedW2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamagedW2, Condition(Trig_DamagedW2_Conditions))
    TriggerAddAction(gg_trg_DamagedW2, Trig_DamagedW2_Actions)
end
--===========================================================================
-- Trigger: AlmostDiyW2
--===========================================================================
function Trig_AlmostDiyW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
end
function FZepp()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('w2a1')) > 0 and GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and UnitAlive(GetFilterUnit()) --and GetUnitUserData(GetFilterUnit())<6
end
function Trig_AlmostDiyW2_Actions()
    local u= GetTriggerUnit()
    local Damage= GetEventDamage()
    local hp= GetUnitState(u, UNIT_STATE_LIFE)
    local Zepp
    local u2
    local g
    
    
    
    
    if hp - Damage < 1 and Random(5 + GetPlayerTechCount(GetOwningPlayer(u), FourCC('w2rq'), true) , 10) then
        
        udg_LocalPlayer=GetOwningPlayer(u)
        Zepp=Condition(FZepp)
        g=CreateGroup()
        GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 1000, Zepp, 5)
        
        
        u2=BlzGroupUnitAt(g, GetRandomInt(1, BlzGroupGetSize(g)))
        if u2 ~= nil and UnitAlive(u2) then
            
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanFlakCannonsFlakTarget.mdl", GetUnitX(u), GetUnitY(u)) , 1)
            SetUnitState(u, UNIT_STATE_LIFE, hp + Damage)
            SetUnitPosition(u, GetUnitX(u2), GetUnitY(u2))
            IssueTargetOrder(u, "smart", u2)
        end
        
        DestroyGroup(g)
        g=nil
        u2=nil
    end
    
    
    
    
    u=nil
    
end
--===========================================================================
function InitTrig_AlmostDiyW2()
    gg_trg_AlmostDiyW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AlmostDiyW2, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_AlmostDiyW2, Condition(Trig_AlmostDiyW2_Conditions))
    TriggerAddAction(gg_trg_AlmostDiyW2, Trig_AlmostDiyW2_Actions)
end
--===========================================================================
-- Trigger: SpellW2
--===========================================================================
function Trig_SpellW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
end
function Trig_SpellW2_Actions()
    AddXp(GetTriggerUnit() , 4)
end
--===========================================================================
function InitTrig_SpellW2()
    gg_trg_SpellW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellW2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_SpellW2, Condition(Trig_SpellW2_Conditions))
    TriggerAddAction(gg_trg_SpellW2, Trig_SpellW2_Actions)
end
--===========================================================================
-- Trigger: DiyGoblinW2
--===========================================================================
function Trig_DiyGoblinW2_Conditions()
    --return GetUnitAbilityLevel(GetTriggerUnit(),'w2a0' ) > 0 
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('w206')
end
function Trig_DiyGoblinW2_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local hp= GetUnitState(u, UNIT_STATE_LIFE)
    local uh= GetHandleId(u)
    local lvl= LoadInteger(Hash, uh, 0)
    local Zepp
    local u2
    local g
    
    
    
    
    if Random(3 , 4) then
        
        udg_LocalPlayer=GetOwningPlayer(u)
        Zepp=Condition(FZepp)
        g=CreateGroup()
        GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 1000, Zepp, 5)
        
        
        u2=BlzGroupUnitAt(g, GetRandomInt(1, BlzGroupGetSize(g)))
        if u2 ~= nil and UnitAlive(u2) then
                   
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanFlakCannonsFlakTarget.mdl", GetUnitX(u2), GetUnitY(u2)) , 1)
            CreateUnit(p, FourCC('w206'), GetUnitX(u2), GetUnitY(u2), 0.0)
            AddXp(u2 , 100 * lvl + 25 * lvl)
        end
    end
    
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_DiyGoblinW2()
    gg_trg_DiyGoblinW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DiyGoblinW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DiyGoblinW2, Condition(Trig_DiyGoblinW2_Conditions))
    TriggerAddAction(gg_trg_DiyGoblinW2, Trig_DiyGoblinW2_Actions)
end
--===========================================================================
-- Trigger: DiyW2
--
-- ??? ??????? ??????????
--===========================================================================
function Trig_DiyW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
    
end
function deadEdly()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    local uh= LoadInteger(Hash, id, 1)
    
    if u == nil then
        FlushChildHashtable(Hash, uh)
    
    end
    t=nil
    u=nil
end
function Trig_DiyW2_Actions()
    local u= GetTriggerUnit()
    local uh= GetHandleId(u)
    
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 45, false, deadEdly)
    SaveUnitHandle(Hash, id, 0, u)
    SaveInteger(Hash, id, 1, uh)
    t=nil
    u=nil
end
--===========================================================================
function InitTrig_DiyW2()
    gg_trg_DiyW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DiyW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DiyW2, Condition(Trig_DiyW2_Conditions))
    TriggerAddAction(gg_trg_DiyW2, Trig_DiyW2_Actions)
end
--===========================================================================
-- Trigger: KillW2
--===========================================================================
function Trig_KillW2_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_KillW2_Actions()
    local u= GetKillingUnit()
    
    
    
    AddXp(u , 55)
    u=nil
end
--===========================================================================
function InitTrig_KillW2()
    gg_trg_KillW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KillW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_KillW2, Condition(Trig_KillW2_Conditions))
    TriggerAddAction(gg_trg_KillW2, Trig_KillW2_Actions)
end
--===========================================================================
-- Trigger: SummonRune
--===========================================================================
function Trig_SummonRune_Conditions()
    return GetUnitTypeId(GetSummonedUnit()) == FourCC('w216')
end
function Trig_SummonRune_Actions()
    UnitApplyTimedLifeBJ(2.00, FourCC('BTLF'), GetSummonedUnit())
end
--===========================================================================
function InitTrig_SummonRune()
    gg_trg_SummonRune=CreateTrigger()
    DisableTrigger(gg_trg_SummonRune)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SummonRune, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_SummonRune, Condition(Trig_SummonRune_Conditions))
    TriggerAddAction(gg_trg_SummonRune, Trig_SummonRune_Actions)
end
--===========================================================================
-- Trigger: RuneExplode
--===========================================================================
function Trig_RuneExplode_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('w216')
end
function Trig_RuneExplode_Actions()
    local u= GetTriggerUnit()
    RemoveEffectTimed(AddSpecialEffect("AbilitiesWeaponsBoltBoltImpact.mdl", GetUnitX(u), GetUnitY(u)) , 2)
    u=nil
end
--===========================================================================
function InitTrig_RuneExplode()
    gg_trg_RuneExplode=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RuneExplode, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_RuneExplode, Condition(Trig_RuneExplode_Conditions))
    TriggerAddAction(gg_trg_RuneExplode, Trig_RuneExplode_Actions)
end
--===========================================================================
-- Trigger: SpellArmorDamage
--===========================================================================
function Trig_SpellArmorDamage_Actions()
    UnitDamageTargetBJ(GetTriggerUnit(), GetSpellTargetUnit(), RMinBJ(GetUnitState(GetSpellTargetUnit(), UNIT_STATE_LIFE) * 0.33, 500), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_DEATH)
end
--===========================================================================
function InitTrig_SpellArmorDamage()
    gg_trg_SpellArmorDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellArmorDamage, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellArmorDamage, function()
        if GetSpellAbilityId() ~= FourCC('w2a8') then return end
        Trig_SpellArmorDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellMassAxes
--===========================================================================
function Trig_SpellMassAxes_Actions()
    local l= GetSpellTargetLoc()
    local caster= GetTriggerUnit()
    local p= GetOwningPlayer(caster)
    local bex
    local dammyAbility= FourCC('w2aa')
    local level= GetUnitAbilityLevel(caster, GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 150, bex)
    
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
            
            UnitAddAbility(u2, dammyAbility)
            SetUnitAbilityLevel(u2, dammyAbility, level)
            IssueTargetOrder(u2, "thunderbolt", u)
            RemoveUnitTimed(u2 , 2)
            i=i + 1
            GroupRemoveUnit(g, u)
        end
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
function InitTrig_SpellMassAxes()
    gg_trg_SpellMassAxes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellMassAxes, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellMassAxes, function()
        if GetSpellAbilityId() ~= FourCC('w2af') then return end
        Trig_SpellMassAxes_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellArrow
--===========================================================================
function FireDark()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    --local integer aid = LoadInteger(Hash,id,1)
    local times= LoadInteger(Hash, id, 2)
    local level= LoadInteger(Hash, id, 3)
    local loc= LoadLocationHandle(Hash, id, 4)
    local u2= CreateUnit(GetOwningPlayer(u), Dummy, GetUnitX(u), GetUnitY(u), bj_UNIT_FACING)
    SetUnitFlyHeight(u2, 100.00, 10)
    UnitAddAbility(u2, FourCC('w2aE'))
    SetUnitAbilityLevel(u2, FourCC('w2aE'), level)
    IssuePointOrderLoc(u2, "carrionswarm", loc)
    RemoveUnitTimed(u2 , 2)
    
    
    times=times + 1
    SaveInteger(Hash, id, 2, times)
    if times > 8 then
        RemoveLocation(loc)
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
    end
    
    
    u=nil
    u2=nil
    t=nil
    
    loc=nil
end
function Trig_SpellArrow_Actions()
    local u= GetTriggerUnit()
    
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 0.35, true, FireDark)
    SaveUnitHandle(Hash, id, 0, u)
    --call SaveInteger(Hash,id,1, 'w2aW')
    SaveInteger(Hash, id, 2, 0)
    SaveInteger(Hash, id, 3, GetUnitAbilityLevel(u, FourCC('w2aW')))
    SaveLocationHandle(Hash, id, 4, GetSpellTargetLoc())
    t=nil
    u=nil
    
end
--===========================================================================
function InitTrig_SpellArrow()
    gg_trg_SpellArrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellArrow, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellArrow, function()
        if GetSpellAbilityId() ~= FourCC('w2aW') then return end
        if not (IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO)) then return end
        Trig_SpellArrow_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonHP
--===========================================================================
function Trig_DragonHP_Actions()
    SetPlayerTechResearchedSwap(FourCC('w292'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w290'), GetOwningPlayer(GetTriggerUnit()))
    
    SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonHP()
    gg_trg_DragonHP=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonHP, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonHP, function()
        if GetSpellAbilityId() ~= FourCC('w294') then return end
        Trig_DragonHP_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonDamage
--===========================================================================
function Trig_DragonDamage_Actions()
    SetPlayerTechResearchedSwap(FourCC('w293'), 1, GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerAbilityAvailableBJ( true, 'w290', GetOwningPlayer(GetTriggerUnit()) )
        SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonDamage()
    gg_trg_DragonDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonDamage, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonDamage, function()
        if GetSpellAbilityId() ~= FourCC('w297') then return end
        Trig_DragonDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonMage
--===========================================================================
function Trig_DragonMage_Actions()
    SetPlayerTechResearchedSwap(FourCC('w291'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w289'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w288'), GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerAbilityAvailableBJ( true, 'w290', GetOwningPlayer(GetTriggerUnit()) )
    
    SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonMage()
    gg_trg_DragonMage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonMage, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonMage, function()
        if GetSpellAbilityId() ~= FourCC('w295') then return end
        Trig_DragonMage_Actions()
    end)
end
--===========================================================================
-- Trigger: OgrimmCharge
--===========================================================================
-- ???? 1 - ???????? ????? - ????? ??? ??? ??????)))
--================
--================================================================================================================================================================================
-- ???? 3 - ??????? ??????
--================
function Ogrimm2()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local un= LoadUnitHandle(Hash, h, 1)
    local ugol= LoadReal(Hash, h, 2)
    local kol= LoadInteger(Hash, h, 3)
    local x= GetUnitX(un)
    local y= GetUnitY(un)
    -- ---------
    x=x + 10 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=y + 10 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    if kol >= 0 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
        SetUnitX(un, x)
        SetUnitY(un, y)
        SaveInteger(Hash, h, 3, kol - 1)
    else
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
    end
    -- ----------
    un=nil
    t=nil
end
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Ogrimm1()
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
        SetUnitFlyHeight(GT, w, 0)
    else
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "attack")
        SetUnitFlyHeight(GT, 0, 0)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, GetSpellAbilityId())
            
            -- ????? - ???????? ?? ?????
            uron=1.3 * lvl * GetHeroStr(GT, true) + lvl * 50
            
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
                ----------
                -- ??????? ????? ? ?????? ??????? ?? ???????
                
                ugol=JSTRUgolMT(dx , GetUnitX(un) , dy , GetUnitY(un))
                t1=CreateTimer()
                h1=GetHandleId(t1)
                SaveUnitHandle(Hash, h1, 1, un)
                SaveReal(Hash, h1, 2, ugol)
                SaveInteger(Hash, h1, 3, 17)
                TimerStart(t1, 0.015, true, Ogrimm2)
                
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
function Trig_OgrimmCharge_Actions()
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
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.025, true, Ogrimm1) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_OgrimmCharge()
    gg_trg_OgrimmCharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgrimmCharge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_OgrimmCharge, function()
        if GetSpellAbilityId() ~= FourCC('w2o6') then return end
        Trig_OgrimmCharge_Actions()
    end)
end
--===========================================================================
-- Trigger: Duel
--===========================================================================
function Duel()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    local u2= LoadUnitHandle(Hash, id, 1)
    local l1=GetUnitLoc(u)
    local l2=GetUnitLoc(u2)
    UnitRemoveAbility(u, FourCC('Avul'))
    UnitRemoveAbility(u2, FourCC('Avul'))
    PauseUnit(u, true)
    PauseUnit(u2, true)
    SetUnitAnimation(u, "attack")
    SetUnitAnimation(u2, "attack")
    SetUnitLookAt(u, "bone_chest", u2, 0, 0, 0)
    SetUnitLookAt(u2, "bone_chest", u, 0, 0, 0)
    
    
    UnitDamageTargetBJ(u, u2, BlzGetUnitBaseDamage(u, 1), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    if UnitAlive(u2) then
         UnitDamageTargetBJ(u2, u, BlzGetUnitBaseDamage(u, 1), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    end
   
    UnitAddAbility(u, FourCC('Avul'))
    UnitAddAbility(u2, FourCC('Avul'))
    if not UnitAlive(u) then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "death")
        SetUnitAnimation(u2, "stand")
        UnitAddAbility(u2, FourCC('w2oz'))
        IssueImmediateOrder(u2, "howlofterror")
            UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        
    elseif not UnitAlive(u2) then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "stand")
        SetUnitAnimation(u2, "death")
        UnitAddAbility(u, FourCC('w2oz'))
        IssueImmediateOrder(u, "howlofterror")
        UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        
    elseif u == nil or u2 == nil or DistanceBetweenPoints(l1, l2) > 500 then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "stand")
        SetUnitAnimation(u2, "stand")
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
    
    end
    t=nil
    u=nil
    u2=nil
    
    RemoveLocation(l1)
    RemoveLocation(l2)
    l1=nil
    l2=nil
end
function Trig_Duel_Actions()
    local u= GetTriggerUnit()
    local u2= GetSpellTargetUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 1, true, Duel)
    SaveUnitHandle(Hash, id, 0, u)
    SaveUnitHandle(Hash, id, 1, u2)
    
    UnitAddAbility(u, FourCC('Avul'))
    UnitAddAbility(u2, FourCC('Avul'))
    
    
    --call SaveInteger(Hash,id,1, 'w2aW')
    --call SaveInteger(Hash,id,2, 0)
    --call SaveInteger(Hash,id,3, GetUnitAbilityLevel(u,'w2aW'))
    --call SaveLocationHandle(Hash,id,4, GetSpellTargetLoc())
    t=nil
    u=nil
    u2=nil
    
end
--===========================================================================
function InitTrig_Duel()
