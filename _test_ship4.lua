local function isWater(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_FLOATABILITY)) end
local function isLand(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_WALKABILITY)) end
local function waterWithin(x,y,rad)
    local steps = 8
    for i=0,steps-1 do
        local a = (i/steps)*2*bj_PI
        if isWater(x+rad*Cos(a), y+rad*Sin(a)) then return true end
        if isWater(x+(rad*0.6)*Cos(a), y+(rad*0.6)*Sin(a)) then return true end
    end
    return false
end
local pi = 11
local ship = AiRaces[AiRace[pi]].shipyard
local cap = playerCapital[pi]
local cx, cy = GetUnitX(cap), GetUnitY(cap)
-- LAND (buildable) point with water within 360 (< requirewaterradius 384)
local spot
local r = 384
while r <= 6000 and not spot do
    for s = 0, 31 do
        local ang = (s/32) * 2 * bj_PI
        local x = cx + r * Cos(ang)
        local y = cy + r * Sin(ang)
        if isLand(x,y) and waterWithin(x,y,360) then spot = {x=x,y=y,r=r}; break end
    end
    r = r + 384
end
if not spot then return "no land-near-water spot" end
local w = AiFindFreeWorker(pi)
if not w then return "spot dist="..spot.r.." but no free worker" end
IssueBuildOrderById(w, ship, spot.x, spot.y)
return string.format("issued at LAND (%d,%d) dist=%d workerOrdAfter=%d",
    math.floor(spot.x), math.floor(spot.y), spot.r, GetUnitCurrentOrder(w))
