-- Controlled test: grab 3 P5 units near the portal, order them to move a bit PAST
-- the gate (toward its EK destination) and report. A second call checks if they crossed.
local pi = 5
local army = udg_Ai_army[pi]
local sz = BlzGroupGetSize(army)
local portalX, portalY = -17920, -23360
local destX, destY = 19936, -6240

-- direction gate->dest, push target = gate + 300u toward dest
local ddx, ddy = destX-portalX, destY-portalY
local dlen = math.sqrt(ddx*ddx+ddy*ddy)
local pushX = portalX + ddx/dlen*350
local pushY = portalY + ddy/dlen*350

-- tag 3 units, remember them on a global so a follow-up call can re-locate
_P5TEST = _P5TEST or {}
if #_P5TEST == 0 then
  local picked = 0
  for i=0,sz-1 do
    local u = BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
       and not IsUnitType(u,UNIT_TYPE_PEON) and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then
      _P5TEST[#_P5TEST+1] = u
      IssuePointOrder(u, "move", pushX, pushY)
      picked = picked+1
      if picked >= 3 then break end
    end
  end
  return "PUSHED "..picked.." units toward ("..R2I(pushX)..","..R2I(pushY)..") [350u past gate]. Re-run to check crossing."
else
  local r = {}
  for _,u in ipairs(_P5TEST) do
    local x,y = GetUnitX(u), GetUnitY(u)
    r[#r+1] = GetUnitName(u).." ("..R2I(x)..","..R2I(y)..") cont="..tostring(AiContinentOf(x,y)).." order="..tostring(GetUnitCurrentOrder(u))
  end
  _P5TEST = {}
  return "AFTER:\n"..table.concat(r,"\n")
end
