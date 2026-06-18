-- Validate: cast "web" on the BlackMountain->EK web-portal, then check if P5 army crossed.
local pi = 5
local portal = _G["gg_unit_n003_0941"]
if portal == nil then return "portal n003_0941 is nil" end

-- before
local army = udg_Ai_army[pi]
local sz = BlzGroupGetSize(army)
local function countByCont()
  local bc = {}
  for i=0,sz-1 do
    local u = BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
       and not IsUnitType(u,UNIT_TYPE_PEON) and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then
      local c = AiContinentOf(GetUnitX(u),GetUnitY(u)) or "nil"
      bc[c]=(bc[c] or 0)+1
    end
  end
  return bc
end
local before = countByCont()
local b = {}
for c,n in pairs(before) do b[#b+1]=c.."="..n end

IssueImmediateOrder(portal, "web")

return "CAST web on n003_0941. BEFORE: "..table.concat(b,", ").."  (re-run _check to see AFTER)"
