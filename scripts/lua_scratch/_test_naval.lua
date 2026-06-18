-- Test naval shipyard placement for Undead bots (shipyard=h0D1).
local out = {}
for pi = 0, 27 do
    local race = AiRace and AiRace[pi]
    if race and AiRaces[race] and AiRaces[race].shipyard then
        local def = AiRaces[race]
        local ship = def.shipyard
        local cap = playerCapital[pi]
        if cap then
            local cx, cy = GetUnitX(cap), GetUnitY(cap)
            -- nearest water point
            local best, bd = nil, 1e18
            for _, wp in ipairs(udg_WaterPoints) do
                local dx, dy = wp.x - cx, wp.y - cy
                local d = dx*dx + dy*dy
                if d < bd then bd = d; best = wp end
            end
            local existing = AiCountBuildingsOfType(pi, ship)
            local placeable = best and AiBuildPlaceable(best.x, best.y) or false
            -- terrain probe at the water point
            local wlk = best and IsTerrainPathable(best.x, best.y, PATHING_TYPE_WALKABILITY)
            local flt = best and IsTerrainPathable(best.x, best.y, PATHING_TYPE_FLOATABILITY)
            out[#out+1] = string.format("pi=%d %s ship=%s existing=%d nearWaterDist=%d placeable=%s walkBlocked=%s floatBlocked=%s",
                pi, tostring(race), tostring(ship~=nil), existing, math.floor(math.sqrt(bd)),
                tostring(placeable), tostring(wlk), tostring(flt))
        end
    end
end
return table.concat(out, "\n")
