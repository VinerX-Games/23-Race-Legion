--===========================================================================
-- Пандарены: Пьянящая настойка хмелевара.
-- APb1 (автоприменяемое «Проклятие») лишь выбирает цель и вешает короткий баф без
-- промахов, чтобы автокаст не повторялся по той же цели. Настоящий эффект APb2
-- накладывает даммик в момент, когда долетает бочка.
--===========================================================================
PandarenBrew = {
    missiles = {}, timer = nil, loc = nil,
    ids = {barrel = FourCC('APb1'), drunk = FourCC('APb2')},
    speed = 900, tick = 0.03125, launchZ = 60, impactZ = 60, arc = 0.15,
    fx = {missile = "Abilities\\Weapons\\BrewmasterMissile\\BrewmasterMissile.mdl"},
}

function PandarenBrew.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function PandarenBrew.GroundZ(x, y)
    if PandarenBrew.loc == nil then PandarenBrew.loc = Location(x, y) end
    MoveLocation(PandarenBrew.loc, x, y)
    return GetLocationZ(PandarenBrew.loc)
end

function PandarenBrew.Launch(caster, target)
    if not PandarenBrew.Alive(caster) or not PandarenBrew.Alive(target) then return end
    local x, y = GetUnitX(caster), GetUnitY(caster)
    local missile = {target = target, owner = GetOwningPlayer(caster), x = x, y = y,
        z = PandarenBrew.GroundZ(x, y) + PandarenBrew.launchZ, travelled = 0,
        effect = AddSpecialEffect(PandarenBrew.fx.missile, x, y)}
    local dx, dy = GetUnitX(target) - x, GetUnitY(target) - y
    missile.total = math.max(1, math.sqrt(dx * dx + dy * dy))
    BlzSetSpecialEffectZ(missile.effect, missile.z)
    BlzSetSpecialEffectYaw(missile.effect, Atan2(dy, dx))
    PandarenBrew.missiles[#PandarenBrew.missiles + 1] = missile
    if PandarenBrew.timer == nil then
        PandarenBrew.timer = CreateTimer()
        TimerStart(PandarenBrew.timer, PandarenBrew.tick, true, PandarenBrew.Tick)
    end
end

function PandarenBrew.Impact(missile)
    local target = missile.target
    if not PandarenBrew.Alive(target) then return end
    local dummy = CreateUnit(missile.owner, gDummy, GetUnitX(target), GetUnitY(target), 0)
    if dummy == nil then return end
    UnitAddAbility(dummy, PandarenBrew.ids.drunk)
    IssueTargetOrder(dummy, "curse", target)
    RemoveUnitTimed(dummy, 2.0)
end

-- Возвращает true, когда бочка долетела или цель пропала.
function PandarenBrew.Step(missile)
    local target = missile.target
    if GetUnitTypeId(target) == 0 then return true end
    local tx, ty = GetUnitX(target), GetUnitY(target)
    local dx, dy = tx - missile.x, ty - missile.y
    local distance = math.sqrt(dx * dx + dy * dy)
    local step = PandarenBrew.speed * PandarenBrew.tick
    if distance <= step then
        PandarenBrew.Impact(missile)
        return true
    end
    missile.x, missile.y = missile.x + dx / distance * step, missile.y + dy / distance * step
    missile.travelled = missile.travelled + step
    -- Дуга по доле пройденного пути; цель может убегать, поэтому доля ограничена.
    local t = math.min(1, missile.travelled / (missile.travelled + distance - step))
    local base = missile.z + (PandarenBrew.GroundZ(tx, ty) + PandarenBrew.impactZ - missile.z) * t
    local height = PandarenBrew.arc * missile.total * 4 * t * (1 - t)
    BlzSetSpecialEffectPosition(missile.effect, missile.x, missile.y, base + height)
    BlzSetSpecialEffectYaw(missile.effect, Atan2(dy, dx))
    return false
end

function PandarenBrew.Tick()
    local list = PandarenBrew.missiles
    for i = #list, 1, -1 do
        local missile = list[i]
        if PandarenBrew.Step(missile) then
            DestroyEffect(missile.effect)
            table.remove(list, i)
        end
    end
    if #list == 0 then
        local t = PandarenBrew.timer
        PandarenBrew.timer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function PandarenBrew.Init()
    if PandarenBrew.spellTrigger ~= nil then return end
    PandarenBrew.spellTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(PandarenBrew.spellTrigger, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(PandarenBrew.spellTrigger, function()
        if GetSpellAbilityId() ~= PandarenBrew.ids.barrel then return end
        PandarenBrew.Launch(GetTriggerUnit(), GetSpellTargetUnit())
    end)
    -- Автоприменение включено с появления хмелевара (и у ботов); игрок может выключить.
    -- Только корневой Allmap (заполняется в StartInc): свой регион на всю карту,
    -- созданный при инициализации, ломает наземные пути (docs/FEC12DE_MOVEMENT_INVESTIGATION.md).
    PandarenBrew.enterTrigger = CreateTrigger()
    TriggerRegisterEnterRegion(PandarenBrew.enterTrigger, Allmap, nil)
    TriggerAddAction(PandarenBrew.enterTrigger, function()
        local u = GetTriggerUnit()
        if GetUnitAbilityLevel(u, PandarenBrew.ids.barrel) > 0 then IssueImmediateOrder(u, "curseon") end
    end)
end

function InitTrig_PandarenBrew()
    PandarenBrew.Init()
end
