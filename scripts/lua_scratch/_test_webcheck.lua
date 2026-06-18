local pi = 5
local army = udg_Ai_army[pi]
local sz = BlzGroupGetSize(army)
local bc = {}
for i=0,sz-1 do
  local u = BlzGroupUnitAt(army,i)
  if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
     and not IsUnitType(u,UNIT_TYPE_PEON) and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then
    local c = AiContinentOf(GetUnitX(u),GetUnitY(u)) or "nil"
    bc[c]=(bc[c] or 0)+1
  end
end
local b = {}
for c,n in pairs(bc) do b[#b+1]=c.."="..n end
return "AFTER: "..table.concat(b,", ")
