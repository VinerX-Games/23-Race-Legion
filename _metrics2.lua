-- Per-race AI metrics snapshot. Returns one line per AI-controlled slot.
local g = CreateGroup()
local out = {}
local tot = { units=0, struct=0, navy=0, transp=0, grade=0, cap=0, capAlive=0, n=0 }

-- transport type set (from AiTransportTypes values)
local transpSet = {}
if AiTransportTypes then
    for _, v in pairs(AiTransportTypes) do transpSet[v] = true end
end

local function capthCount(pi)
    -- count ZahvatBuildings owned by this player
    local c = 0
    local zg = udg_ZahvatBuildings
    if zg == nil then return 0 end
    local n = BlzGroupGetSize(zg)
    local me = Player(pi)
    for i = 0, n - 1 do
        local u = BlzGroupUnitAt(zg, i)
        if u ~= nil and GetOwningPlayer(u) == me and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            c = c + 1
        end
    end
    return c
end

for pi = 0, 23 do
    if udg_AiControl and udg_AiControl[pi] then
        local p = Player(pi)
        local units, struct, transp = 0, 0, 0
        GroupEnumUnitsOfPlayer(g, p, nil)
        local n = BlzGroupGetSize(g)
        for i = 0, n - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local tid = GetUnitTypeId(u)
                if transpSet[tid] then transp = transp + 1 end
                if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                    struct = struct + 1
                elseif not IsUnitType(u, UNIT_TYPE_PEON) then
                    units = units + 1
                end
            end
        end
        local navy = udg_Ai_navy[pi] and BlzGroupGetSize(udg_Ai_navy[pi]) or 0
        local grade = Grades and Grades[pi] or 0
        local cap = capthCount(pi)
        local capU = playerCapital[pi]
        local alive = (capU ~= nil and GetUnitState(capU, UNIT_STATE_LIFE) > 0.405) and 1 or 0
        local race = tostring(AiRace[pi] or "?")
        out[#out+1] = string.format("pi=%d %-12s U=%d S=%d navy=%d trn=%d grd=%d cap=%d capAlive=%d",
            pi, race, units, struct, navy, transp, grade, cap, alive)
        tot.units = tot.units + units; tot.struct = tot.struct + struct
        tot.navy = tot.navy + navy; tot.transp = tot.transp + transp
        tot.grade = tot.grade + grade; tot.cap = tot.cap + cap
        tot.capAlive = tot.capAlive + alive; tot.n = tot.n + 1
    end
end
DestroyGroup(g)
local nn = math.max(tot.n, 1)
out[#out+1] = string.format("TOTALS n=%d avgU=%.1f avgS=%.1f navy=%d transp=%d avgGrd=%.1f cap=%d capAlive=%d/%d  t=%.0fs",
    tot.n, tot.units/nn, tot.struct/nn, tot.navy, tot.transp, tot.grade/nn, tot.cap, tot.capAlive, tot.n, GetTimeOfDay())
return table.concat(out, "\n")
