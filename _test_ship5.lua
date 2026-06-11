local function isWater(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_FLOATABILITY)) end
local function isLand(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_WALKABILITY)) end
-- 4x4 footprint all water: sample center + ring at +-256 and +-128
local function footprintWater(x,y)
    if not isWater(x,y) then return false end
    for _,d in ipairs({256,128}) do
        for _,o in ipairs({{d,0},{-d,0},{0,d},{0,-d},{d,d},{-d,-d},{d,-d},{-d,d}}) do
            if not isWater(x+o[1],y+o[2]) then return false end
        end
    end
    return true
end
local function landWithin(x,y,rad)
    for i=0,11 do local a=(i/12)*2*bj_PI
        if isLand(x+rad*Cos(a),y+rad*Sin(a)) then return true end end
    return false
end
local pi = 11
local ship = AiRaces[AiRace[pi]].shipyard
local cap = playerCapital[pi]
local cx, cy = GetUnitX(cap), GetUnitY(cap)
local spot
local r = 384
while r <= 7000 and not spot do
    for s = 0, 35 do
        local ang = (s/36)*2*bj_PI
        local x = cx + r*Cos(ang); local y = cy + r*Sin(ang)
        if footprintWater(x,y) and landWithin(x,y,640) then spot={x=x,y=y,r=r}; break end
    end
    r = r + 256
end
if not spot then return "no open-water-near-shore spot found within 7000" end
local w = AiFindFreeWorker(pi)
if not w then return "spot dist="..spot.r.." but no free worker" end
IssueBuildOrderById(w, ship, spot.x, spot.y)
return string.format("issued OPEN-WATER (%d,%d) dist=%d ordAfter=%d", math.floor(spot.x), math.floor(spot.y), spot.r, GetUnitCurrentOrder(w))
