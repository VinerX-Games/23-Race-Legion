-- Water tile: WALKABILITY=true(blocked), FLOATABILITY=false(floatable).
-- Land tile:  WALKABILITY=false(walkable), FLOATABILITY=true(not floatable).
-- Shipyard wants a water spot at the shore (water with land nearby).
local function isWater(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_FLOATABILITY)) end
local function isLand(x,y) return (not IsTerrainPathable(x,y,PATHING_TYPE_WALKABILITY)) end
local pi = 11
local ship = AiRaces[AiRace[pi]].shipyard
local cap = playerCapital[pi]
local cx, cy = GetUnitX(cap), GetUnitY(cap)
local cand = {}
local r = 384
while r <= 6000 and #cand < 6 do
    for s = 0, 23 do
        local ang = (s/24) * 2 * bj_PI
        local x = cx + r * Cos(ang)
        local y = cy + r * Sin(ang)
        if isWater(x,y) then
            local landNear = false
            for _, o in ipairs({{384,0},{-384,0},{0,384},{0,-384}}) do
                if isLand(x+o[1], y+o[2]) then landNear = true; break end
            end
            if landNear then cand[#cand+1] = {x=x,y=y,r=r} end
        end
    end
    r = r + 384
end
local msg = "pi=11 waterShoreCand="..#cand
if #cand > 0 then
    local sp = cand[1]
    msg = msg .. string.format(" dist=%d (%d,%d)", sp.r, math.floor(sp.x), math.floor(sp.y))
    local w = AiFindFreeWorker(pi)
    if w then IssueBuildOrderById(w, ship, sp.x, sp.y); msg = msg.." -> issued" else msg=msg.." noWorker" end
end
return msg
