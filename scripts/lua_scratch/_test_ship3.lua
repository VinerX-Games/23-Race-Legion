local function isWater(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_FLOATABILITY)) end
local function isLand(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_WALKABILITY)) end
local pi = 11
local ship = AiRaces[AiRace[pi]].shipyard
local cap = playerCapital[pi]
local cx, cy = GetUnitX(cap), GetUnitY(cap)
-- nearest shore: LAND point with water within 256 (worker stands on land)
local spot
local r = 384
while r <= 6000 and not spot do
    for s = 0, 31 do
        local ang = (s/32) * 2 * bj_PI
        local x = cx + r * Cos(ang)
        local y = cy + r * Sin(ang)
        if isLand(x,y) then
            for _, o in ipairs({{256,0},{-256,0},{0,256},{0,-256}}) do
                if isWater(x+o[1], y+o[2]) then spot = {x=x,y=y,r=r,wx=x+o[1],wy=y+o[2]}; break end
            end
        end
        if spot then break end
    end
    r = r + 384
end
if not spot then return "no shore spot" end
local w = AiFindFreeWorker(pi)
if not w then return "shore at "..spot.r.." but no free worker" end
-- try building centered between land and water (the shoreline)
local mx, my = (spot.x+spot.wx)/2, (spot.y+spot.wy)/2
IssueBuildOrderById(w, ship, mx, my)
return string.format("issued at shoreline (%d,%d) dist=%d workerOrd=%d workerType=%s",
    math.floor(mx), math.floor(my), spot.r, GetUnitCurrentOrder(w),
    (function() local t=GetUnitTypeId(w) return string.char((t>>24)&255,(t>>16)&255,(t>>8)&255,t&255) end)())
