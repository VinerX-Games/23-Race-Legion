-- Scan rings around pi=11 capital for a shore spot (land with water within ~300),
-- then attempt to build a shipyard there and report.
local pi = 11
local ship = AiRaces[AiRace[pi]].shipyard
local cap = playerCapital[pi]
local cx, cy = GetUnitX(cap), GetUnitY(cap)
local found = {}
local r = 512
while r <= 6000 and #found < 5 do
    local s = 0
    while s < 24 do
        local ang = (s/24) * 2 * bj_PI
        local x = cx + r * Cos(ang)
        local y = cy + r * Sin(ang)
        -- land center (walkable: WALKABILITY not blocked) with water nearby (floatable blocked at offset)
        local landCenter = not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY)
        if landCenter then
            -- check for water within 320 in any cardinal
            local waterNear = false
            for _, o in ipairs({{320,0},{-320,0},{0,320},{0,-320},{256,256},{-256,-256}}) do
                if not IsTerrainPathable(x+o[1], y+o[2], PATHING_TYPE_FLOATABILITY) then waterNear = true; break end
            end
            if waterNear then
                found[#found+1] = {x=x, y=y, r=r}
            end
        end
        s = s + 1
    end
    r = r + 512
end
local msg = "pi=11 ship="..tostring(ship~=nil).." shoreSpotsFound="..#found
if #found > 0 then
    local sp = found[1]
    msg = msg .. string.format(" firstShore dist=%d (%d,%d)", sp.r, math.floor(sp.x), math.floor(sp.y))
    local w = AiFindFreeWorker(pi)
    if w then
        IssueBuildOrderById(w, ship, sp.x, sp.y)
        msg = msg .. " -> issued build to worker"
    else
        msg = msg .. " (no free worker)"
    end
end
return msg
