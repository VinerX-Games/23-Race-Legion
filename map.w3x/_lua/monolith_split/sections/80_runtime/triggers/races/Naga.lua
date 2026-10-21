
--===========================================================================
-- Trigger: NagaStart
--===========================================================================
NagaSubraceByPlayer = NagaSubraceByPlayer or {}

function NagaApplySubrace(p, branch)
    branch = branch == "murloc" and "murloc" or "naga"
    NagaSubraceByPlayer[GetPlayerId(p)] = branch
    local murloc = branch == "murloc"
    SetPlayerTechResearched(p, FourCC('R0FE'), murloc and 0 or 1)
    SetPlayerTechResearched(p, FourCC('R0FF'), murloc and 1 or 0)
    for _, id in ipairs({ 'n053', 'n052', 'n050', 'n054' }) do
        SetPlayerTechMaxAllowed(p, FourCC(id), murloc and -1 or 0)
    end
    for _, id in ipairs({ 'n051', 'n057', 'nnsw', 'nmyr', 'nnrg' }) do
        SetPlayerTechMaxAllowed(p, FourCC(id), murloc and 0 or -1)
    end
    SetPlayerTechMaxAllowed(p, FourCC('H0OZ'), murloc and 1 or 0)
    SetPlayerTechMaxAllowed(p, FourCC('H0JU'), murloc and 0 or 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0FQ'), murloc and 3 or 0)
    SetPlayerTechResearched(p, FourCC('R0KZ'), murloc and 0 or 1)
    SetPlayerTechMaxAllowed(p, FourCC('R0FE'), 0)
    SetPlayerTechMaxAllowed(p, FourCC('R0FF'), 0)
end

function NagaStartLimits_act()
    SetPlayerTechMaxAllowedSwap(FourCC('n054'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n053'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n052'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n050'), 0, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('n051'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('n057'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nnsw'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nmyr'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('nnrg'), 0, GetEnumPlayer())
    
     SetPlayerTechMaxAllowedSwap(FourCC('N07A'), 1, GetEnumPlayer())
     
     SetPlayerTechMaxAllowedSwap(FourCC('H0OZ'), 0, GetEnumPlayer())
     SetPlayerTechMaxAllowedSwap(FourCC('H0JU'), 0, GetEnumPlayer()) --HERO
    SetPlayerTechMaxAllowedSwap(FourCC('H0JV'), 1, GetEnumPlayer())
 
    --Murloc Grades
    SetPlayerTechMaxAllowedSwap(FourCC('R0FQ'), 0, GetEnumPlayer())
    local p = GetEnumPlayer()
    if NagaSubraceByPlayer[GetPlayerId(p)] ~= nil then
        NagaApplySubrace(p, NagaSubraceByPlayer[GetPlayerId(p)])
    end
    
end
function NagaStartLimits()
    ForForce(udg_AllPlayers, NagaStartLimits_act)
    ForForce(udg_Bots, NagaStartLimits_act)
end
function Trig_NagaStart_Actions()
    NagaStartLimits()
end
--===========================================================================
function InitTrig_NagaStart()
    gg_trg_NagaStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_NagaStart, 2.00)
    TriggerAddAction(gg_trg_NagaStart, Trig_NagaStart_Actions)
end
--===========================================================================
-- Trigger: Coatl
--===========================================================================
function Trig_Coatl_Conditions()
    gUnit=GetTrainedUnit()
    return GetUnitTypeId(gUnit) == FourCC('nwgs')
end
function Trig_Coatl_Actions()
    UnitAddAbility(gUnit, FourCC('Aave'))
    SetUnitFlyHeightBJ(gUnit, 240.00, 1)
    UnitRemoveAbility(gUnit, FourCC('Aave'))
    
end
--===========================================================================
function InitTrig_Coatl()
    gg_trg_Coatl=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Coatl, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Coatl, Condition(Trig_Coatl_Conditions))
    TriggerAddAction(gg_trg_Coatl, Trig_Coatl_Actions)
end
--===========================================================================
-- Trigger: VaishBuria
--===========================================================================
function Trig_VaishBuria_Actions()
    local loc= GetSpellTargetLoc()
    local u2= CreateUnitAtLoc(GetOwningPlayer(GetTriggerUnit()), FourCC('ntor'), loc, bj_UNIT_FACING)
    UnitApplyTimedLife(u2, FourCC('BTLF'), 30.00)
    u2=nil
    RemoveLocation(loc)
    loc=nil
end
--===========================================================================
function InitTrig_VaishBuria()
    gg_trg_VaishBuria=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VaishBuria, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_VaishBuria, function()
        if GetSpellAbilityId() ~= FourCC('A16E') then return end
        Trig_VaishBuria_Actions()
    end)
end
--===========================================================================
-- Trigger: VaishArrow
--===========================================================================
function Trig_VaishArrow_Conditions()
    gTarget=BlzGetEventDamageTarget()
    gCaster=GetEventDamageSource()
    --call BJDebugMsg("Test1"+GetUnitName(gTarget)+GetUnitName(gCaster)+I2S(GetUnitAbilityLevel(gTarget, 'B06P'))+I2S(GetUnitAbilityLevel(gTarget, 'B06Q')) )
    --return GetUnitAbilityLevel(gTarget, 'B06P')>0 and GetUnitAbilityLevel(gTarget, 'B06Q')==0 
    return GetUnitAbilityLevel(gCaster, FourCC('A16C')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL and Random(1 , 10)
end
function Trig_VaishArrow_Actions()
    --call BJDebugMsg("Test2"+GetUnitName(gTarget)+GetUnitName(gCaster))
    DummyCastTargetLevel(FourCC('A16D') , "frostnova" , gCaster , gTarget , GetUnitAbilityLevel(gCaster, FourCC('A16C')))
end
--===========================================================================
function InitTrig_VaishArrow()
    gg_trg_VaishArrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_VaishArrow, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_VaishArrow, Condition(Trig_VaishArrow_Conditions))
    TriggerAddAction(gg_trg_VaishArrow, Trig_VaishArrow_Actions)
end
--===========================================================================
-- Trigger: NagaPas
--===========================================================================
function Trig_NagaPas_Conditions()
    return GetLearnedSkillBJ() == FourCC('A13A')
end
function Trig_NagaPas_Func002Func001Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 4
end
function Trig_NagaPas_Func002Func001Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 3
end
function Trig_NagaPas_Func002Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 2
end
function Trig_NagaPas_Func002C()
    return GetUnitAbilityLevelSwapped(FourCC('A13A'), GetTriggerUnit()) == 1
end
function Trig_NagaPas_Actions()
    if Trig_NagaPas_Func002C() then
        UnitAddAbilityBJ(FourCC('A136'), GetTriggerUnit())
    else
        if Trig_NagaPas_Func002Func001C() then
            UnitAddAbilityBJ(FourCC('A137'), GetTriggerUnit())
            UnitRemoveAbilityBJ(FourCC('A136'), GetTriggerUnit())
        else
            if Trig_NagaPas_Func002Func001Func002C() then
                UnitAddAbilityBJ(FourCC('A138'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A137'), GetTriggerUnit())
            else
                if Trig_NagaPas_Func002Func001Func002Func001C() then
                    UnitAddAbilityBJ(FourCC('A139'), GetTriggerUnit())
                    UnitRemoveAbilityBJ(FourCC('A138'), GetTriggerUnit())
                end
            end
        end
    end
end
--===========================================================================
function InitTrig_NagaPas()
    gg_trg_NagaPas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NagaPas, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_NagaPas, Condition(Trig_NagaPas_Conditions))
    TriggerAddAction(gg_trg_NagaPas, Trig_NagaPas_Actions)
end
--===========================================================================
-- Trigger: NagaCommonSpell
--===========================================================================
function Trig_NagaCommonSpell_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('S00E'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('S00E') , 180)
end
--===========================================================================
function InitTrig_NagaCommonSpell()
    gg_trg_NagaCommonSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NagaCommonSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NagaCommonSpell, function()
        if GetSpellAbilityId() ~= FourCC('A1LT') then return end
        if not (not IsTerrainPathable(GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), PATHING_TYPE_FLOATABILITY)) then return end
        Trig_NagaCommonSpell_Actions()
    end)
end

--===========================================================================
-- Наги: Мутация (мурлок-мутант) и Гарпун (морской охотник).
-- Мутация выпадает один раз при появлении юнита: общая пассивка AMu1 заменяется
-- пассивкой выпавшей мутации, поэтому повторный вход в мир ничего не меняет.
-- Списки жабр и притягиваний — массивы: порядок обхода детерминирован.
--===========================================================================
NagaCombat = {
    gills = {}, pulls = {}, pulling = {}, regenTimer = nil, pullTimer = nil, probe = nil,
    ids = {
        mutation = FourCC('AMu1'), claws = FourCC('AMu2'), shell = FourCC('AMu3'), gills = FourCC('AMu4'),
        harpoon = FourCC('AMh1'), harpoonTech = FourCC('R0FP'),
    },
    clawsDamage = 8, shellArmor = 3,
    gillsRegen = 8, regenTick = 0.5,        -- HP в секунду, пока мутант в воде
    harpoonOrder = "acidbomb",              -- базовый приказ Канала в AMh1
    harpoonDamage = 40, harpoonPull = 300, harpoonHeroPull = 150,
    harpoonGap = 90,                        -- цель не притягивается вплотную к охотнику
    harpoonAiMin = 250, harpoonAiRange = 500,
    pullSpeed = 1000, pullTick = 0.03125,
    fx = {
        hit = "Objects\\Spawnmodels\\Critters\\Albatross\\CritterBloodAlbatross.mdl",
        rope = "LEAS",
    },
}

function NagaCombat.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function NagaCombat.InWater(u)
    return not IsTerrainPathable(GetUnitX(u), GetUnitY(u), PATHING_TYPE_FLOATABILITY)
end

function NagaCombat.Mutate(u)
    local ids = NagaCombat.ids
    if GetUnitAbilityLevel(u, ids.mutation) == 0 or IsUnitIllusion(u) then return end
    UnitRemoveAbility(u, ids.mutation)
    local roll = GetRandomInt(1, 3)
    if roll == 1 then
        UnitAddAbility(u, ids.claws)
        BlzSetUnitBaseDamage(u, BlzGetUnitBaseDamage(u, 0) + NagaCombat.clawsDamage, 0)
    elseif roll == 2 then
        UnitAddAbility(u, ids.shell)
        BlzSetUnitArmor(u, BlzGetUnitArmor(u) + NagaCombat.shellArmor)
    else
        UnitAddAbility(u, ids.gills)
        NagaCombat.gills[#NagaCombat.gills + 1] = u
        if NagaCombat.regenTimer == nil then
            NagaCombat.regenTimer = CreateTimer()
            TimerStart(NagaCombat.regenTimer, NagaCombat.regenTick, true, NagaCombat.Regen)
        end
    end
end

function NagaCombat.Regen()
    local list, amount = NagaCombat.gills, NagaCombat.gillsRegen * NagaCombat.regenTick
    for i = #list, 1, -1 do
        local u = list[i]
        -- Мёртвый мутант остаётся в списке, пока есть труп: его могут воскресить.
        if GetUnitTypeId(u) == 0 or GetUnitAbilityLevel(u, NagaCombat.ids.gills) == 0 then
            table.remove(list, i)
        elseif NagaCombat.Alive(u) and not IsUnitLoaded(u) and NagaCombat.InWater(u) then
            SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + amount)
        end
    end
    if #list == 0 then
        local t = NagaCombat.regenTimer
        NagaCombat.regenTimer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function NagaCombat.HarpoonTarget(caster, target)
    return NagaCombat.Alive(caster) and NagaCombat.Alive(target) and target ~= caster
        and IsUnitEnemy(target, GetOwningPlayer(caster))
        and not IsUnitType(target, UNIT_TYPE_STRUCTURE) and not IsUnitType(target, UNIT_TYPE_FLYING)
        and not IsUnitType(target, UNIT_TYPE_WARD) and not BlzIsUnitInvulnerable(target)
        and not IsUnitHidden(target) and not IsUnitLoaded(target)
        and not NagaCombat.pulling[target]
end

function NagaCombat.Harpoon(caster, target)
    if not NagaCombat.HarpoonTarget(caster, target) then return false end
    local cx, cy, tx, ty = GetUnitX(caster), GetUnitY(caster), GetUnitX(target), GetUnitY(target)
    local dx, dy = cx - tx, cy - ty
    local distance = math.sqrt(dx * dx + dy * dy)
    local pull = IsUnitType(target, UNIT_TYPE_HERO) and NagaCombat.harpoonHeroPull or NagaCombat.harpoonPull
    pull = math.min(pull, distance - NagaCombat.harpoonGap)
    UnitDamageTarget(caster, target, NagaCombat.harpoonDamage, false, false, ATTACK_TYPE_NORMAL,
        DAMAGE_TYPE_NORMAL, WEAPON_TYPE_WHOKNOWS)
    DestroyEffect(AddSpecialEffectTarget(NagaCombat.fx.hit, target, "chest"))
    if pull < 1 or not NagaCombat.Alive(target) then return true end
    local state = {caster = caster, target = target, owner = GetOwningPlayer(target),
        ux = dx / distance, uy = dy / distance, left = pull, x = tx, y = ty,
        rope = AddLightning(NagaCombat.fx.rope, true, cx, cy, tx, ty)}
    NagaCombat.pulls[#NagaCombat.pulls + 1] = state
    NagaCombat.pulling[target] = true
    if NagaCombat.pullTimer == nil then
        NagaCombat.pullTimer = CreateTimer()
        TimerStart(NagaCombat.pullTimer, NagaCombat.pullTick, true, NagaCombat.PullTick)
    end
    return true
end

-- Скрытый предмет проверяет динамическую проходимость (деревья, здания) в точке шага.
function NagaCombat.Passable(x, y)
    if IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then return false end
    if NagaCombat.probe == nil then
        NagaCombat.probe = CreateItem(FourCC('ratf'), x, y)
    end
    SetItemVisible(NagaCombat.probe, true)
    SetItemPosition(NagaCombat.probe, x, y)
    local ix, iy = GetItemX(NagaCombat.probe), GetItemY(NagaCombat.probe)
    SetItemVisible(NagaCombat.probe, false)
    return (ix - x) ^ 2 + (iy - y) ^ 2 <= 1
end

-- Возвращает true, когда притягивание закончено.
function NagaCombat.PullStep(state)
    local target = state.target
    if not NagaCombat.Alive(target) or GetOwningPlayer(target) ~= state.owner
        or IsUnitHidden(target) or IsUnitLoaded(target) or BlzIsUnitInvulnerable(target)
        or IsUnitType(target, UNIT_TYPE_FLYING) then return true end
    local tx, ty = GetUnitX(target), GetUnitY(target)
    -- Телепорт или чужое принудительное перемещение прерывают притягивание.
    if (tx - state.x) ^ 2 + (ty - state.y) ^ 2 > 96 * 96 then return true end
    local step = math.min(NagaCombat.pullSpeed * NagaCombat.pullTick, state.left)
    local nx, ny = tx + state.ux * step, ty + state.uy * step
    if not NagaCombat.Passable(nx, ny) then return true end
    -- SetUnitPosition сбросил бы приказы: цель продолжает драться во время рывка.
    SetUnitX(target, nx)
    SetUnitY(target, ny)
    state.x, state.y, state.left = GetUnitX(target), GetUnitY(target), state.left - step
    local caster = state.caster
    if GetUnitTypeId(caster) ~= 0 then
        MoveLightning(state.rope, true, GetUnitX(caster), GetUnitY(caster), state.x, state.y)
    end
    return state.left <= 0.5
end

function NagaCombat.PullTick()
    local list = NagaCombat.pulls
    for i = #list, 1, -1 do
        local state = list[i]
        if NagaCombat.PullStep(state) then
            DestroyLightning(state.rope)
            NagaCombat.pulling[state.target] = nil
            table.remove(list, i)
        end
    end
    if #list == 0 then
        local t = NagaCombat.pullTimer
        NagaCombat.pullTimer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

-- ИИ гарпунит дальнюю цель: сначала героев, затем стрелков; ближняя цель и так в бою.
function NagaCombat.AiHarpoon(caster)
    local ids, owner = NagaCombat.ids, GetOwningPlayer(caster)
    if BlzGetUnitAbilityCooldownRemaining(caster, ids.harpoon) > 0
        or GetPlayerTechCount(owner, ids.harpoonTech, true) == 0 then return false end
    local x, y = GetUnitX(caster), GetUnitY(caster)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, NagaCombat.harpoonAiRange, nil)
    local best, bestScore = nil, -1
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if NagaCombat.HarpoonTarget(caster, t) and IsUnitVisible(t, owner)
            and (GetUnitX(t) - x) ^ 2 + (GetUnitY(t) - y) ^ 2 >= NagaCombat.harpoonAiMin ^ 2 then
            local score = (IsUnitType(t, UNIT_TYPE_HERO) and 2 or 0)
                + (IsUnitType(t, UNIT_TYPE_RANGED_ATTACKER) and 1 or 0)
            if score > bestScore or (score == bestScore and GetHandleId(t) < GetHandleId(best)) then
                best, bestScore = t, score
            end
        end
    end
    DestroyGroup(group)
    return best ~= nil and IssueTargetOrder(caster, NagaCombat.harpoonOrder, best)
end

function NagaCombat.Init()
    if NagaCombat.spellTrigger ~= nil then return end
    NagaCombat.spellTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(NagaCombat.spellTrigger, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(NagaCombat.spellTrigger, function()
        if GetSpellAbilityId() ~= NagaCombat.ids.harpoon then return end
        local caster = GetTriggerUnit()
        if not NagaCombat.Harpoon(caster, GetSpellTargetUnit()) then
            BlzEndUnitAbilityCooldown(caster, NagaCombat.ids.harpoon)
        end
    end)
    NagaCombat.enterTrigger = CreateTrigger()
    TriggerRegisterEnterRegion(NagaCombat.enterTrigger, Allmap, nil)
    TriggerAddAction(NagaCombat.enterTrigger, function() NagaCombat.Mutate(GetTriggerUnit()) end)
end

function InitTrig_NagaCombat()
    NagaCombat.Init()
end
