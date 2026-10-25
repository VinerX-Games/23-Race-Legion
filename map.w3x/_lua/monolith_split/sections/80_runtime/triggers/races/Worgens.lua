
--===========================================================================
-- Trigger: StartWorgens
--===========================================================================
function Trig_StartWorgens_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('H0J2'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J6'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J7'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('H0J8'), 1, GetEnumPlayer())
end
function Trig_StartWorgens_Actions()
    ForForce(udg_AllPlayers, Trig_StartWorgens_Func001A)
end
--===========================================================================
function InitTrig_StartWorgens()
    gg_trg_StartWorgens=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartWorgens, 0.01)
    TriggerAddAction(gg_trg_StartWorgens, Trig_StartWorgens_Actions)
end
--===========================================================================
-- Trigger: LegGer
--===========================================================================
function Trig_LegGer_Actions()
    local u= GetTriggerUnit()
    
    
    if GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 1 then
        UnitAddAbilityBJ(FourCC('A11V'), u)
        RemoveAbilityTimed(u , FourCC('A11V') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 2 then
        UnitAddAbilityBJ(FourCC('A11W'), u)
        RemoveAbilityTimed(u , FourCC('A11W') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 3 then
        UnitAddAbilityBJ(FourCC('A11X'), u)
        RemoveAbilityTimed(u , FourCC('A11X') , 15)
    
    elseif GetUnitAbilityLevelSwapped(FourCC('A11U'), GetTriggerUnit()) == 4 then
        UnitAddAbilityBJ(FourCC('A11Y'), u)
        RemoveAbilityTimed(u , FourCC('A11Y') , 15)
      
    end
    u=nil
end
--===========================================================================
function InitTrig_LegGer()
    gg_trg_LegGer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LegGer, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_LegGer, function()
        if GetSpellAbilityId() ~= FourCC('A11U') then return end
        Trig_LegGer_Actions()
    end)
end
--===========================================================================
-- Лорд друид (H0J6): Семя Тал'дорена, Тропа корней, Проклятие Гоэмона, Полнолуние.
-- Q/E/R — Channel без своих эффектов, W — Berserk (ускорение). Метку Проклятия и промах
-- Полнолуния накладывает даммик nWd1. Числа совпадают с scripts/implement_worgen_druid.py.
-- Время семян и лоз считается целыми тиками по 0.05 сек.
--===========================================================================
WorgenDruid = {
    seeds = {}, trails = {}, marks = {}, markCount = 0, step = 0, timer = nil, clock = nil,
    ids = {
        seed = FourCC('AWd1'), trail = FourCC('AWd2'), curse = FourCC('AWd3'), moon = FourCC('AWd4'),
        mark = FourCC('AWd5'), miss = FourCC('AWd6'), markBuff = FourCC('BWd2'),
        caster = FourCC('nWd1'),
    },
    tick = 0.05,
    seedTicks = 60, seedRadius = 200, seedHeal = {120, 190, 260, 330},
    seedRange = 700, seedMinLost = 100,
    trailEvery = 10, trailDrops = 6, trailLife = 10,   -- 0.5 сек.; 6 лоз; живут 10 шагов (5 сек.)
    trailRadius = 120, trailDamage = {5, 8, 11, 14},
    markTime = 10, markJump = 300, markAmp = 1.5, markPrune = 200, curseRange = 700,
    moonRadius = 1200, moonHeal = {150, 250}, moonMinEnemies = 8,
    fx = {
        seed = "Doodads\\Ashenvale\\Plants\\AshenBush0\\AshenBush0.mdl",
        bloom = "Objects\\Spawnmodels\\NightElf\\NightElfLargeDeathExplode\\NightElfLargeDeathExplode.mdl",
        heal = "Abilities\\Spells\\Human\\Heal\\HealTarget.mdl",
        vine = "Abilities\\Spells\\NightElf\\EntanglingRoots\\EntanglingRootsTarget.mdl",
        moon = "Abilities\\Spells\\NightElf\\MoonWell\\MoonWellCasterArt.mdl",
    },
}

function WorgenDruid.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function WorgenDruid.Now()
    return TimerGetElapsed(WorgenDruid.clock)
end

function WorgenDruid.Heal(u, amount)
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + amount)
    DestroyEffect(AddSpecialEffectTarget(WorgenDruid.fx.heal, u, "origin"))
end

-- Служебный юнит без точки каста применяет метку/промах от имени владельца друида.
function WorgenDruid.Cast(owner, x, y, ability, level, order, target)
    local caster = CreateUnit(owner, WorgenDruid.ids.caster, x, y, 0)
    if caster == nil then return false end
    SetUnitAbilityLevel(caster, ability, level)
    if IssueTargetOrder(caster, order, target) then
        RemoveUnitTimed(caster, 2.0)
        return true
    end
    RemoveUnit(caster)
    return false
end

-- Цель Проклятия Гоэмона: не герой, не механизм и не здание.
function WorgenDruid.Markable(t, owner)
    return WorgenDruid.Alive(t) and IsUnitEnemy(t, owner)
        and not IsUnitType(t, UNIT_TYPE_HERO) and not IsUnitType(t, UNIT_TYPE_MECHANICAL)
        and not IsUnitType(t, UNIT_TYPE_STRUCTURE) and not IsUnitType(t, UNIT_TYPE_MAGIC_IMMUNE)
        and not BlzIsUnitInvulnerable(t)
end

function WorgenDruid.EnsureTimer()
    if WorgenDruid.timer == nil then
        WorgenDruid.timer = CreateTimer()
        TimerStart(WorgenDruid.timer, WorgenDruid.tick, true, WorgenDruid.Tick)
    end
end

function WorgenDruid.Seed(caster, x, y, level)
    local fx = AddSpecialEffect(WorgenDruid.fx.seed, x, y)
    BlzSetSpecialEffectScale(fx, 0.5)
    WorgenDruid.seeds[#WorgenDruid.seeds + 1] = {
        fx = fx, x = x, y = y, owner = GetOwningPlayer(caster), age = 0,
        heal = WorgenDruid.seedHeal[level] or WorgenDruid.seedHeal[1],
    }
    WorgenDruid.EnsureTimer()
end

function WorgenDruid.Bloom(seed)
    DestroyEffect(seed.fx)
    DestroyEffect(AddSpecialEffect(WorgenDruid.fx.bloom, seed.x, seed.y))
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, seed.x, seed.y, WorgenDruid.seedRadius, nil)
    for i = 0, BlzGroupGetSize(group) - 1 do
        local u = BlzGroupUnitAt(group, i)
        if WorgenDruid.Alive(u) and IsUnitAlly(u, seed.owner)
            and not IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            WorgenDruid.Heal(u, seed.heal)
        end
    end
    DestroyGroup(group)
end

function WorgenDruid.Trail(caster, level)
    local trail = {
        caster = caster, owner = GetOwningPlayer(caster), start = WorgenDruid.step,
        damage = WorgenDruid.trailDamage[level] or WorgenDruid.trailDamage[1], drops = 0, vines = {},
    }
    WorgenDruid.trails[#WorgenDruid.trails + 1] = trail
    WorgenDruid.TrailStep(trail, 0)
    WorgenDruid.EnsureTimer()
end

-- Шаг тропы k (раз в 0.5 сек.): новая лоза под друидом, затем урон всех старых лоз.
-- Каждый враг получает урон от лоз одной тропы не больше раза за шаг.
function WorgenDruid.TrailStep(trail, k)
    local caster = trail.caster
    if trail.drops < WorgenDruid.trailDrops then
        if WorgenDruid.Alive(caster) then
            local x, y = GetUnitX(caster), GetUnitY(caster)
            trail.vines[#trail.vines + 1] = {fx = AddSpecialEffect(WorgenDruid.fx.vine, x, y),
                x = x, y = y, born = k}
            trail.drops = trail.drops + 1
        else
            trail.drops = WorgenDruid.trailDrops
        end
    end
    local canHit = GetUnitTypeId(caster) ~= 0
    local hit = {}
    for i = #trail.vines, 1, -1 do
        local vine = trail.vines[i]
        if canHit and k > vine.born then
            local group = CreateGroup()
            GroupEnumUnitsInRange(group, vine.x, vine.y, WorgenDruid.trailRadius, nil)
            for j = 0, BlzGroupGetSize(group) - 1 do
                local t = BlzGroupUnitAt(group, j)
                if not hit[t] and WorgenDruid.Alive(t) and IsUnitEnemy(t, trail.owner)
                    and not IsUnitType(t, UNIT_TYPE_STRUCTURE) and not IsUnitType(t, UNIT_TYPE_FLYING) then
                    hit[t] = true
                    UnitDamageTarget(caster, t, trail.damage, false, false, ATTACK_TYPE_NORMAL,
                        DAMAGE_TYPE_MAGIC, WEAPON_TYPE_WHOKNOWS)
                end
            end
            DestroyGroup(group)
        end
        if k - vine.born >= WorgenDruid.trailLife then
            DestroyEffect(vine.fx)
            table.remove(trail.vines, i)
        end
    end
end

function WorgenDruid.Tick()
    WorgenDruid.step = WorgenDruid.step + 1
    local seeds = WorgenDruid.seeds
    for i = #seeds, 1, -1 do
        local seed = seeds[i]
        seed.age = seed.age + 1
        if seed.age >= WorgenDruid.seedTicks then
            table.remove(seeds, i)
            WorgenDruid.Bloom(seed)
        else
            BlzSetSpecialEffectScale(seed.fx, 0.5 + 0.5 * seed.age / WorgenDruid.seedTicks)
        end
    end
    local trails = WorgenDruid.trails
    for i = #trails, 1, -1 do
        local trail = trails[i]
        local elapsed = WorgenDruid.step - trail.start
        if elapsed % WorgenDruid.trailEvery == 0 then
            WorgenDruid.TrailStep(trail, elapsed // WorgenDruid.trailEvery)
            if trail.drops >= WorgenDruid.trailDrops and #trail.vines == 0 then
                table.remove(trails, i)
            end
        end
    end
    if #seeds == 0 and #trails == 0 then
        local t = WorgenDruid.timer
        WorgenDruid.timer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function WorgenDruid.Mark(target, owner)
    local id = GetHandleId(target)
    if WorgenDruid.marks[id] == nil then
        WorgenDruid.markCount = WorgenDruid.markCount + 1
        if WorgenDruid.markCount > WorgenDruid.markPrune then
            -- Удаление истёкших меток не зависит от порядка обхода.
            local now = WorgenDruid.Now()
            for key, mark in pairs(WorgenDruid.marks) do
                if mark.expire <= now then
                    WorgenDruid.marks[key] = nil
                    WorgenDruid.markCount = WorgenDruid.markCount - 1
                end
            end
        end
    end
    WorgenDruid.marks[id] = {owner = owner, expire = WorgenDruid.Now() + WorgenDruid.markTime}
end

function WorgenDruid.Jump(victim, owner)
    local x, y = GetUnitX(victim), GetUnitY(victim)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, WorgenDruid.markJump, nil)
    local best, bestDist = nil, nil
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if t ~= victim and WorgenDruid.Markable(t, owner) then
            local dx, dy = GetUnitX(t) - x, GetUnitY(t) - y
            local dist = dx * dx + dy * dy
            if bestDist == nil or dist < bestDist then best, bestDist = t, dist end
        end
    end
    DestroyGroup(group)
    if best == nil then return false end
    return WorgenDruid.Cast(owner, GetUnitX(best), GetUnitY(best), WorgenDruid.ids.mark, 1,
        "bloodlust", best)
end

function WorgenDruid.Moon(caster, level)
    local owner, x, y = GetOwningPlayer(caster), GetUnitX(caster), GetUnitY(caster)
    local heal = WorgenDruid.moonHeal[level] or WorgenDruid.moonHeal[1]
    DestroyEffect(AddSpecialEffect(WorgenDruid.fx.moon, x, y))
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, WorgenDruid.moonRadius, nil)
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if WorgenDruid.Alive(t) and not IsUnitType(t, UNIT_TYPE_STRUCTURE)
            and not IsUnitType(t, UNIT_TYPE_MECHANICAL) then
            if IsUnitAlly(t, owner) then
                WorgenDruid.Heal(t, heal)
            elseif IsUnitEnemy(t, owner) and not IsUnitType(t, UNIT_TYPE_MAGIC_IMMUNE)
                and not BlzIsUnitInvulnerable(t) then
                WorgenDruid.Cast(owner, GetUnitX(t), GetUnitY(t), WorgenDruid.ids.miss, level,
                    "curse", t)
            end
        end
    end
    DestroyGroup(group)
end

function WorgenDruid.Spell()
    local ids, id, u = WorgenDruid.ids, GetSpellAbilityId(), GetTriggerUnit()
    if id == ids.seed then
        WorgenDruid.Seed(u, GetSpellTargetX(), GetSpellTargetY(), GetUnitAbilityLevel(u, id))
    elseif id == ids.trail then
        WorgenDruid.Trail(u, GetUnitAbilityLevel(u, id))
    elseif id == ids.curse then
        local t = GetSpellTargetUnit()
        if t ~= nil then
            WorgenDruid.Cast(GetOwningPlayer(u), GetUnitX(t), GetUnitY(t), ids.mark, 1, "bloodlust", t)
        end
    elseif id == ids.mark then
        WorgenDruid.Mark(GetSpellTargetUnit(), GetOwningPlayer(u))
    elseif id == ids.moon then
        WorgenDruid.Moon(u, GetUnitAbilityLevel(u, id))
    end
end

function WorgenDruid.Damage()
    local amount = GetEventDamage()
    if amount > 0 and GetUnitAbilityLevel(BlzGetEventDamageTarget(), WorgenDruid.ids.markBuff) > 0 then
        BlzSetEventDamage(amount * WorgenDruid.markAmp)
    end
end

-- Бафф снимается до события смерти, поэтому метка хранится в таблице со сроком.
function WorgenDruid.Death()
    local victim = GetTriggerUnit()
    local id = GetHandleId(victim)
    local mark = WorgenDruid.marks[id]
    if mark == nil then return end
    WorgenDruid.marks[id] = nil
    WorgenDruid.markCount = WorgenDruid.markCount - 1
    if WorgenDruid.Now() < mark.expire then WorgenDruid.Jump(victim, mark.owner) end
end

-- ИИ: семя под самым раненым союзником, проклятие на крупного не-героя, луна в большой драке.
function WorgenDruid.AiSeed(u)
    local owner = GetOwningPlayer(u)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, GetUnitX(u), GetUnitY(u), WorgenDruid.seedRange, nil)
    local best, lost = nil, WorgenDruid.seedMinLost
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if WorgenDruid.Alive(t) and IsUnitAlly(t, owner) and not IsUnitType(t, UNIT_TYPE_STRUCTURE) then
            local missing = GetUnitState(t, UNIT_STATE_MAX_LIFE) - GetUnitState(t, UNIT_STATE_LIFE)
            if missing >= lost then best, lost = t, missing end
        end
    end
    DestroyGroup(group)
    return best ~= nil and IssuePointOrder(u, "channel", GetUnitX(best), GetUnitY(best))
end

function WorgenDruid.AiCurse(u, target)
    local owner = GetOwningPlayer(u)
    if target == nil or not WorgenDruid.Markable(target, owner) then
        local group = CreateGroup()
        GroupEnumUnitsInRange(group, GetUnitX(u), GetUnitY(u), WorgenDruid.curseRange, nil)
        local life = 0
        target = nil
        for i = 0, BlzGroupGetSize(group) - 1 do
            local t = BlzGroupUnitAt(group, i)
            if WorgenDruid.Markable(t, owner) and IsUnitVisible(t, owner)
                and GetUnitState(t, UNIT_STATE_MAX_LIFE) > life then
                target, life = t, GetUnitState(t, UNIT_STATE_MAX_LIFE)
            end
        end
        DestroyGroup(group)
    end
    return target ~= nil and IssueTargetOrder(u, "curse", target)
end

function WorgenDruid.AiMoon(u)
    local owner = GetOwningPlayer(u)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, GetUnitX(u), GetUnitY(u), WorgenDruid.moonRadius, nil)
    local count = 0
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if WorgenDruid.Alive(t) and IsUnitEnemy(t, owner) and not IsUnitType(t, UNIT_TYPE_STRUCTURE) then
            count = count + 1
        end
    end
    DestroyGroup(group)
    return count >= WorgenDruid.moonMinEnemies and IssueImmediateOrder(u, "starfall")
end

function WorgenDruid.Init()
    if WorgenDruid.spellTrigger ~= nil then return end
    WorgenDruid.clock = CreateTimer()
    TimerStart(WorgenDruid.clock, 1000000.0, false, nil)
    WorgenDruid.spellTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(WorgenDruid.spellTrigger, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(WorgenDruid.spellTrigger, WorgenDruid.Spell)
    WorgenDruid.damageTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(WorgenDruid.damageTrigger, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddAction(WorgenDruid.damageTrigger, WorgenDruid.Damage)
    WorgenDruid.deathTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(WorgenDruid.deathTrigger, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(WorgenDruid.deathTrigger, WorgenDruid.Death)
end

function InitTrig_WorgenDruid()
    WorgenDruid.Init()
end
--===========================================================================
-- Trigger: SpellOpletenie
--===========================================================================
function Trig_SpellOpletenie_Actions()
   -- call BJDebugMsg("")
    MassSpell(GetTriggerUnit() , GetSpellAbilityId() , FourCC('A1MA') , "firebolt" , nil , 600 , 1 , false)
end
--===========================================================================
function InitTrig_SpellOpletenie()
    gg_trg_SpellOpletenie=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellOpletenie, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellOpletenie, function()
        if GetSpellAbilityId() ~= FourCC('A1M9') then return end
        Trig_SpellOpletenie_Actions()
    end)
end
--===========================================================================
-- Trigger: flot1 Copy O
--===========================================================================
function Trig_flot1_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1_Copy_O()
    gg_trg_flot1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1_Copy_O, Condition(Trig_flot1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot1_Copy_O, Trig_flot1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy O
--===========================================================================
function Trig_flot2_Copy_O_Conditions()
    return GetResearched() == FourCC('R073')
end
function Trig_flot2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R072'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_O()
    gg_trg_flot2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_O, Condition(Trig_flot2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_O, Trig_flot2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm1 Copy O
--===========================================================================
function Trig_arm1_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm1_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1_Copy_O()
    gg_trg_arm1_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1_Copy_O, Condition(Trig_arm1_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm1_Copy_O, Trig_arm1_Copy_O_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy O
--===========================================================================
function Trig_arm2_Copy_O_Conditions()
    return GetResearched() == FourCC('R072')
end
function Trig_arm2_Copy_O_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R073'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_O()
    gg_trg_arm2_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_O, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_O, Condition(Trig_arm2_Copy_O_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_O, Trig_arm2_Copy_O_Actions)
end
--===========================================================================
-- Trigger: BuidAltar
--===========================================================================
function Trig_BuidAltar_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('h0CV')
end
function Trig_BuidAltar_Actions()
    UnitAddAbilityBJ(FourCC('Asud'), GetTriggerUnit())
    AddUnitToStockBJ(FourCC('h07A'), GetTriggerUnit(), 1, 1)
end
--===========================================================================
function InitTrig_BuidAltar()
    gg_trg_BuidAltar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuidAltar, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
    TriggerAddCondition(gg_trg_BuidAltar, Condition(Trig_BuidAltar_Conditions))
    TriggerAddAction(gg_trg_BuidAltar, Trig_BuidAltar_Actions)
end
--===========================================================================
-- Trigger: Auto set Copy O
--===========================================================================
function Trig_Auto_set_Copy_O_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "ensnare", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_set_Copy_O()
    gg_trg_Auto_set_Copy_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_set_Copy_O, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_set_Copy_O, function()
        if GetSpellAbilityId() ~= FourCC('A09U') then return end
        Trig_Auto_set_Copy_O_Actions()
    end)
end
--===========================================================================
-- Trigger: AutocastSlowOn
--===========================================================================
function Trig_AutocastSlowOn_Conditions()
    return GetResearched() == FourCC('R04S') and GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), FourCC('R04S'), true) == 2
end
function Trig_AutocastSlowOn_Actions()
    GlobalIssue(FourCC('A09S') , GetOwningPlayer(GetTriggerUnit()) , "slowon")
end
--===========================================================================
function InitTrig_AutocastSlowOn()
    gg_trg_AutocastSlowOn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AutocastSlowOn, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_AutocastSlowOn, Condition(Trig_AutocastSlowOn_Conditions))
    TriggerAddAction(gg_trg_AutocastSlowOn, Trig_AutocastSlowOn_Actions)
end