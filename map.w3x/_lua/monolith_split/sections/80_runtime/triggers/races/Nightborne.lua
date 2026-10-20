--===========================================================================
-- Ночнорождённые: Лунный снаряд глефомёта. Ночью после попадания глефа дважды
-- отскакивает в ближайших ещё не задетых врагов, теряя 20% урона за отскок.
-- Артиллерийский сплэш даёт по событию урона на каждого задетого юнита: отскоки
-- запускает только первое событие выстрела, остальные в том же кадре пропускаются.
--===========================================================================
NightborneGlaive = {
    flights = {}, busy = {}, timer = nil, loc = nil,
    ids = {moon = FourCC('AMn1'), tech = FourCC('RMn1')},
    bounces = 2, falloff = 0.8, radius = 450, speed = 800, tick = 0.03125, height = 60,
    fx = {missile = "Abilities\\Weapons\\GlaiveMissile\\GlaiveMissile.mdl"},
}

function NightborneGlaive.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function NightborneGlaive.IsNight()
    local time = GetFloatGameState(GAME_STATE_TIME_OF_DAY)
    return time < 6 or time >= 18
end

function NightborneGlaive.Z(x, y)
    if NightborneGlaive.loc == nil then NightborneGlaive.loc = Location(x, y) end
    MoveLocation(NightborneGlaive.loc, x, y)
    return GetLocationZ(NightborneGlaive.loc) + NightborneGlaive.height
end

-- Урон одного выстрела без сплэша: база с улучшениями плюс среднее по кубикам.
function NightborneGlaive.ShotDamage(u)
    local dice, sides = BlzGetUnitDiceNumber(u, 0), BlzGetUnitDiceSides(u, 0)
    return BlzGetUnitBaseDamage(u, 0) + dice * (sides + 1) / 2
end

function NightborneGlaive.Bounceable(u, owner, hit)
    return NightborneGlaive.Alive(u) and not hit[u] and IsUnitEnemy(u, owner)
        and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_FLYING)
        and not IsUnitType(u, UNIT_TYPE_WARD) and not BlzIsUnitInvulnerable(u)
        and not IsUnitHidden(u) and IsUnitVisible(u, owner)
end

-- Ближайшая цель; равные расстояния разрешаются по handle — выбор детерминирован.
function NightborneGlaive.Next(x, y, owner, hit)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, NightborneGlaive.radius, nil)
    local best, bestDistance = nil, nil
    for i = 0, BlzGroupGetSize(group) - 1 do
        local u = BlzGroupUnitAt(group, i)
        if NightborneGlaive.Bounceable(u, owner, hit) then
            local d = (GetUnitX(u) - x) ^ 2 + (GetUnitY(u) - y) ^ 2
            if best == nil or d < bestDistance or (d == bestDistance and GetHandleId(u) < GetHandleId(best)) then
                best, bestDistance = u, d
            end
        end
    end
    DestroyGroup(group)
    return best
end

-- Запустить следующий отскок из точки x, y; false — целей нет или отскоки кончились.
function NightborneGlaive.Launch(flight, x, y)
    if flight.left <= 0 then return false end
    local target = NightborneGlaive.Next(x, y, flight.owner, flight.hit)
    if target == nil then return false end
    flight.left, flight.target, flight.x, flight.y = flight.left - 1, target, x, y
    flight.damage = flight.damage * NightborneGlaive.falloff
    flight.hit[target] = true
    if flight.effect == nil then
        flight.effect = AddSpecialEffect(NightborneGlaive.fx.missile, x, y)
    end
    BlzSetSpecialEffectPosition(flight.effect, x, y, NightborneGlaive.Z(x, y))
    return true
end

function NightborneGlaive.Start(source, primary)
    local owner = GetOwningPlayer(source)
    local flight = {source = source, owner = owner, left = NightborneGlaive.bounces,
        damage = NightborneGlaive.ShotDamage(source), hit = {[primary] = true}}
    if not NightborneGlaive.Launch(flight, GetUnitX(primary), GetUnitY(primary)) then return end
    NightborneGlaive.flights[#NightborneGlaive.flights + 1] = flight
    if NightborneGlaive.timer == nil then
        NightborneGlaive.timer = CreateTimer()
        TimerStart(NightborneGlaive.timer, NightborneGlaive.tick, true, NightborneGlaive.Tick)
    end
end

-- Возвращает true, когда глефа закончила полёт.
function NightborneGlaive.Step(flight)
    local target = flight.target
    if GetUnitTypeId(target) == 0 then return true end
    local tx, ty = GetUnitX(target), GetUnitY(target)
    local dx, dy = tx - flight.x, ty - flight.y
    local distance = math.sqrt(dx * dx + dy * dy)
    local step = NightborneGlaive.speed * NightborneGlaive.tick
    if distance > step then
        flight.x, flight.y = flight.x + dx / distance * step, flight.y + dy / distance * step
        BlzSetSpecialEffectPosition(flight.effect, flight.x, flight.y, NightborneGlaive.Z(flight.x, flight.y))
        BlzSetSpecialEffectYaw(flight.effect, Atan2(dy, dx))
        return false
    end
    if NightborneGlaive.Alive(target) and GetUnitTypeId(flight.source) ~= 0 then
        -- attack=false: отскок не считается атакой и не запускает новые отскоки.
        UnitDamageTarget(flight.source, target, flight.damage, false, true, ATTACK_TYPE_SIEGE,
            DAMAGE_TYPE_NORMAL, WEAPON_TYPE_WHOKNOWS)
    end
    return not NightborneGlaive.Launch(flight, tx, ty)
end

function NightborneGlaive.Tick()
    local list = NightborneGlaive.flights
    for i = #list, 1, -1 do
        local flight = list[i]
        if NightborneGlaive.Step(flight) then
            DestroyEffect(flight.effect)
            table.remove(list, i)
        end
    end
    if #list == 0 then
        local t = NightborneGlaive.timer
        NightborneGlaive.timer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function NightborneGlaive.Damage()
    if not BlzGetEventIsAttack() then return end
    local source = GetEventDamageSource()
    if source == nil or GetUnitAbilityLevel(source, NightborneGlaive.ids.moon) == 0
        or NightborneGlaive.busy[source] or IsUnitIllusion(source) then return end
    if GetPlayerTechCount(GetOwningPlayer(source), NightborneGlaive.ids.tech, true) == 0
        or not NightborneGlaive.IsNight() then return end
    local target = BlzGetEventDamageTarget()
    if not NightborneGlaive.Alive(target) then return end
    NightborneGlaive.busy[source] = true
    local t = CreateTimer()
    TimerStart(t, 0, false, function()
        DestroyTimer(t)
        NightborneGlaive.busy[source] = nil
    end)
    NightborneGlaive.Start(source, target)
end

function NightborneGlaive.Init()
    if NightborneGlaive.damageTrigger ~= nil then return end
    NightborneGlaive.damageTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(NightborneGlaive.damageTrigger, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddAction(NightborneGlaive.damageTrigger, NightborneGlaive.Damage)
end

function InitTrig_NightborneGlaive()
    NightborneGlaive.Init()
end
