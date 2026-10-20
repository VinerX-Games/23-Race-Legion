
--===========================================================================
-- Огры: Пригвоздить (копьеметатель), Нарастающая ярость (огроны), Поступь гронна, Пиршество.
-- Пригвоздить и Пиршество хранят состояние в уровне пассивки: при смерти или удалении
-- юнита ничего не утекает. Отдельный список ведётся только для гроннов.
--===========================================================================
OgreCombat = {
    gronns = {}, clock = 0, timer = nil,
    ids = {
        pin = FourCC('AOg1'), rage = FourCC('AOg2'), stride = FourCC('AOg3'), feast = FourCC('AOg4'),
        root = FourCC('AOg5'), slow = FourCC('AOg6'), caster = FourCC('nOg1'),
        rageTech = FourCC('ROg2'), feastTech = FourCC('ROg4'),
    },
    pinEvery = 5,           -- уровни 1..5: засчитано (уровень - 1) бросков
    rageStep = 0.02,        -- за каждые полные 10% потерянного здоровья
    strideCooldown = 6, strideRadius = 250, strideBuildingDamage = 30,
    feastLife = 15, feastLevels = 11,  -- уровни 1..11: +0..+150 к максимуму здоровья
    tick = 0.25,
    fx = {
        stride = "Abilities\\Spells\\Human\\Thunderclap\\ThunderClapCaster.mdl",
        feast = "Abilities\\Spells\\Undead\\VampiricAura\\VampiricAuraTarget.mdl",
    },
}

function OgreCombat.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function OgreCombat.HasTech(p, id)
    return GetPlayerTechCount(p, id, true) > 0
end

-- Служебный юнит без точки каста применяет корни/замедление от имени огра.
function OgreCombat.Cast(owner, x, y, order, target)
    local caster = CreateUnit(owner, OgreCombat.ids.caster, x, y, 0)
    if caster == nil then return false end
    local ok
    if target ~= nil then
        ok = IssueTargetOrder(caster, order, target)
    else
        ok = IssueImmediateOrder(caster, order)
    end
    if ok then
        RemoveUnitTimed(caster, 2.0)
    else
        RemoveUnit(caster)
    end
    return ok
end

function OgreCombat.Pinnable(target, owner)
    return OgreCombat.Alive(target) and IsUnitEnemy(target, owner)
        and not IsUnitType(target, UNIT_TYPE_STRUCTURE)
        and not IsUnitType(target, UNIT_TYPE_MAGIC_IMMUNE)
        and not BlzIsUnitInvulnerable(target)
end

function OgreCombat.RageBonus(u)
    local max = GetUnitState(u, UNIT_STATE_MAX_LIFE)
    if max <= 0 then return 0 end
    local missing = 1 - GetUnitState(u, UNIT_STATE_LIFE) / max
    return OgreCombat.rageStep * math.floor(missing * 10 + 0.000001)
end

function OgreCombat.Damage()
    local amount = GetEventDamage()
    if amount <= 0 or not BlzGetEventIsAttack() then return end
    local source, target = GetEventDamageSource(), BlzGetEventDamageTarget()
    if not OgreCombat.Alive(source) or IsUnitIllusion(source) then return end
    local ids, owner = OgreCombat.ids, GetOwningPlayer(source)
    if GetUnitAbilityLevel(source, ids.rage) > 0 and OgreCombat.HasTech(owner, ids.rageTech) then
        local bonus = OgreCombat.RageBonus(source)
        if bonus > 0 then BlzSetEventDamage(amount * (1 + bonus)) end
    end
    local level = GetUnitAbilityLevel(source, ids.pin)
    if level > 0 and OgreCombat.Pinnable(target, owner) then
        if level >= OgreCombat.pinEvery then
            SetUnitAbilityLevel(source, ids.pin, 1)
            OgreCombat.Cast(owner, GetUnitX(source), GetUnitY(source), "ensnare", target)
        else
            SetUnitAbilityLevel(source, ids.pin, level + 1)
        end
    end
end

function OgreCombat.Death()
    local killer, victim = GetKillingUnit(), GetTriggerUnit()
    if not OgreCombat.Alive(killer) or IsUnitIllusion(killer) then return end
    local ids, owner = OgreCombat.ids, GetOwningPlayer(killer)
    local level = GetUnitAbilityLevel(killer, ids.feast)
    if level == 0 or level >= OgreCombat.feastLevels
        or not OgreCombat.HasTech(owner, ids.feastTech)
        or not IsUnitEnemy(victim, owner) or IsUnitType(victim, UNIT_TYPE_STRUCTURE)
        or IsUnitType(victim, UNIT_TYPE_WARD) or IsUnitIllusion(victim) then return end
    SetUnitAbilityLevel(killer, ids.feast, level + 1)
    BlzSetUnitMaxHP(killer, BlzGetUnitMaxHP(killer) + OgreCombat.feastLife)
    SetUnitState(killer, UNIT_STATE_LIFE, GetUnitState(killer, UNIT_STATE_LIFE) + OgreCombat.feastLife)
    DestroyEffect(AddSpecialEffectTarget(OgreCombat.fx.feast, killer, "origin"))
end

function OgreCombat.EnsureTimer()
    if OgreCombat.timer == nil then
        OgreCombat.timer = CreateTimer()
        TimerStart(OgreCombat.timer, OgreCombat.tick, true, OgreCombat.Tick)
    end
end

function OgreCombat.Track(u)
    if GetUnitAbilityLevel(u, OgreCombat.ids.stride) == 0 then return end
    for _, data in ipairs(OgreCombat.gronns) do
        if data.unit == u then return end
    end
    OgreCombat.gronns[#OgreCombat.gronns + 1] = {unit = u, ready = OgreCombat.clock}
    OgreCombat.EnsureTimer()
end

-- Возвращает true, если топот сработал: в радиусе были наземные враги или вражеские здания.
function OgreCombat.Stride(u)
    local owner, x, y = GetOwningPlayer(u), GetUnitX(u), GetUnitY(u)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, OgreCombat.strideRadius, nil)
    local buildings, slowed = {}, false
    for i = 0, BlzGroupGetSize(group) - 1 do
        local t = BlzGroupUnitAt(group, i)
        if OgreCombat.Alive(t) and IsUnitEnemy(t, owner) and not IsUnitType(t, UNIT_TYPE_FLYING) then
            if IsUnitType(t, UNIT_TYPE_STRUCTURE) then
                buildings[#buildings + 1] = t
            elseif not BlzIsUnitInvulnerable(t) then
                slowed = true
            end
        end
    end
    DestroyGroup(group)
    if #buildings == 0 and not slowed then return false end
    DestroyEffect(AddSpecialEffect(OgreCombat.fx.stride, x, y))
    for _, b in ipairs(buildings) do
        UnitDamageTarget(u, b, OgreCombat.strideBuildingDamage, false, false, ATTACK_TYPE_CHAOS,
            DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
    end
    if slowed then OgreCombat.Cast(owner, x, y, "thunderclap", nil) end
    return true
end

function OgreCombat.Tick()
    OgreCombat.clock = OgreCombat.clock + OgreCombat.tick
    local now = OgreCombat.clock
    for i = #OgreCombat.gronns, 1, -1 do
        local data = OgreCombat.gronns[i]
        local u = data.unit
        -- Мёртвый гронн остаётся в списке, пока есть труп: его могут воскресить.
        if GetUnitTypeId(u) == 0 or GetUnitAbilityLevel(u, OgreCombat.ids.stride) == 0 then
            table.remove(OgreCombat.gronns, i)
        elseif now >= data.ready and OgreCombat.Alive(u) and not IsUnitHidden(u)
            and not IsUnitPaused(u) and not IsUnitLoaded(u) and OgreCombat.Stride(u) then
            data.ready = now + OgreCombat.strideCooldown
        end
    end
    if #OgreCombat.gronns == 0 then
        local t = OgreCombat.timer
        OgreCombat.timer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function OgreCombat.Init()
    if OgreCombat.damageTrigger ~= nil then return end
    OgreCombat.damageTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(OgreCombat.damageTrigger, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddAction(OgreCombat.damageTrigger, OgreCombat.Damage)
    OgreCombat.deathTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(OgreCombat.deathTrigger, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(OgreCombat.deathTrigger, OgreCombat.Death)
    -- Обученные, призванные и созданные скриптом гронны одинаково входят в регион мира.
    local bounds = GetWorldBounds()
    OgreCombat.world = CreateRegion()
    RegionAddRect(OgreCombat.world, bounds)
    RemoveRect(bounds)
    OgreCombat.enterTrigger = CreateTrigger()
    TriggerRegisterEnterRegion(OgreCombat.enterTrigger, OgreCombat.world, nil)
    TriggerAddAction(OgreCombat.enterTrigger, function() OgreCombat.Track(GetTriggerUnit()) end)
end

function InitTrig_OgreCombat()
    OgreCombat.Init()
end
