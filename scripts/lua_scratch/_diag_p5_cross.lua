-- Where are P5's army units physically? Are any crossing the portal to EK?
local pi = 5
local p = Player(pi)
local out = {}
local function L(s) out[#out+1]=s end

local army = udg_Ai_army[pi]
local sz = BlzGroupGetSize(army)
local byCont = {}
local orders = {}
local portalX, portalY = -17920, -23360
local nearPortal = 0
local sample = {}
for i=0,sz-1 do
  local u = BlzGroupUnitAt(army,i)
  if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
     and not IsUnitType(u,UNIT_TYPE_PEON) and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then
    local x,y = GetUnitX(u), GetUnitY(u)
    local c = AiContinentOf(x,y) or "nil"
    byCont[c] = (byCont[c] or 0)+1
    local o = GetUnitCurrentOrder(u)
    orders[o] = (orders[o] or 0)+1
    local dx,dy = x-portalX, y-portalY
    if dx*dx+dy*dy < 600*600 then nearPortal=nearPortal+1 end
    if #sample < 6 then
      sample[#sample+1] = "  u="..GetUnitName(u).." ("..R2I(x)..","..R2I(y)..") cont="..c
        .." order="..tostring(o)
    end
  end
end

L("=== P5 army distribution by continent:")
for c,n in pairs(byCont) do L("  "..c.." = "..n) end
L("near Dark Portal (<600u) = "..nearPortal)
L("=== order codes (count):")
for o,n in pairs(orders) do L("  order "..tostring(o).." = "..n) end
L("=== sample units:")
for _,s in ipairs(sample) do L(s) end

-- Is the portal a waygate with a destination set?
local g = CreateGroup()
GroupEnumUnitsInRange(g, portalX, portalY, 400, nil)
local gsz = BlzGroupGetSize(g)
L("=== units within 400u of portal coord: "..gsz)
for i=0,gsz-1 do
  local u = BlzGroupUnitAt(g,i)
  if u then
    local nm = GetUnitName(u)
    if nm and (nm:find("ортал") or IsUnitType(u,UNIT_TYPE_STRUCTURE)) then
      local active = WaygateIsActive(u)
      local dx = WaygateGetDestinationX(u)
      local dy = WaygateGetDestinationY(u)
      L("  WAYGATE? "..nm.." active="..tostring(active).." dest=("..R2I(dx)..","..R2I(dy)..") destCont="..tostring(AiContinentOf(dx,dy)))
    end
  end
end
DestroyGroup(g)

return table.concat(out,"\n")
