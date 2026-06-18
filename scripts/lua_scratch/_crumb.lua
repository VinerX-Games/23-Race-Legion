-- Single-slot breadcrumb: each wrapped fn overwrites 23race_crumb.pld with its
-- name IMMEDIATELY (unbuffered PreloadGenEnd) before running. After a hard crash
-- the file holds the last fn entered = the crashing one. Reentrancy shows as the
-- same name; a depth counter reveals nesting.
CrumbDepth = 0
function Crumb(s)
  pcall(function()
    PreloadGenClear(); PreloadGenStart()
    Preload(tostring(s) .. " depth=" .. tostring(CrumbDepth))
    PreloadGenEnd("23race_crumb.pld")
  end)
end
local function wrap(name, getctx)
  local orig = _G[name]
  if type(orig) ~= "function" then return name .. ":MISSING" end
  _G[name] = function(...)
    CrumbDepth = CrumbDepth + 1
    local args = { ... }
    local ctx = ""
    if getctx then pcall(function() ctx = getctx(table.unpack(args)) end) end
    Crumb(name .. ctx)
    local r = { orig(table.unpack(args)) }
    CrumbDepth = CrumbDepth - 1
    return table.unpack(r)
  end
  return name .. ":ok"
end

-- Instrumented AiEnemyPowerAround: per-unit crumb BEFORE GetUnitState.
-- Uses the real (blacklist-safe) EPA, with per-unit logging added.
local _origAiEnemyPowerAround = _G["AiEnemyPowerAround"]
if type(_origAiEnemyPowerAround) == "function" then
  _G["AiEnemyPowerAround"] = function(p, x, y, radius)
    CrumbDepth = CrumbDepth + 1
    Crumb("AiEnemyPowerAround")
    CrumbDepth = CrumbDepth - 1
    local scanGroup = _G["AiBrainScanGroup"] or CreateGroup()
    _G["AiBrainScanGroup"] = scanGroup
    GroupEnumUnitsInRange(scanGroup, x, y, radius, nil)
    local now = _G["AiBrainTickCounter"] or 0
    local gcAge = (_G["gStaleBlacklistMaxAge"] or 600)
    if now % (_G["gStaleBlacklistGcEvery"] or 120) == 0 then
      local bl = _G["gStaleBlacklist"]
      if bl ~= nil then for hid, t in pairs(bl) do if now - t > gcAge then bl[hid] = nil end end end
    end
    local pow = 0.0
    local sz = BlzGroupGetSize(scanGroup)
    local i = 0
    while i < sz do
      local u = BlzGroupUnitAt(scanGroup, i)
      if u ~= nil then
        local hid, ux, uy, uhid, utype = "?", "?", "?", "?", "?"
        pcall(function() hid = GetHandleId(u) end)
        pcall(function() ux = R2I(GetUnitX(u)) end)
        pcall(function() uy = R2I(GetUnitY(u)) end)
        pcall(function() uhid = tostring(IsUnitHidden(u)) end)
        pcall(function() utype = tostring(GetUnitTypeId(u)) end)
        CrumbDepth = CrumbDepth + 1
        Crumb("EPA u=" .. tostring(hid) .. " x=" .. tostring(ux) .. " y=" .. tostring(uy)
          .. " hid=" .. uhid .. " type=" .. utype)
        CrumbDepth = CrumbDepth - 1
        local bl = _G["gStaleBlacklist"]
        if bl == nil or bl[hid] == nil then
          local owner = GetOwningPlayer(u)
          if owner ~= nil and IsPlayerEnemy(owner, p)
              and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            pow = pow + (_G["AiUnitPower"] ~= nil and _G["AiUnitPower"](u) or 0)
          end
        end
      end
      i = i + 1
    end
    GroupClear(scanGroup)
    return pow
  end
end

local function pictx(pi) return " pi=" .. tostring(pi) end
local out = {}
-- legacy / continental / portal machinery
out[#out+1] = wrap("TryAttack")
out[#out+1] = wrap("ProcessContinentalStuff")
out[#out+1] = wrap("ProcessContinentalStuffNaga")
out[#out+1] = wrap("HandleOutland")
out[#out+1] = wrap("RequestPort")
out[#out+1] = wrap("PortTo")
out[#out+1] = wrap("checkGreenArea")
-- brain subsystems
out[#out+1] = wrap("AiBrainArmyTickInner", pictx)
out[#out+1] = wrap("AiBrainPerceive", pictx)
out[#out+1] = wrap("BrainProduce", pictx)
out[#out+1] = wrap("BrainBuild", pictx)
out[#out+1] = wrap("AiBrainCollectObjectives", pictx)
out[#out+1] = wrap("AiSquadReapDead", pictx)
out[#out+1] = wrap("BrainFocus", pictx)
out[#out+1] = wrap("BrainNavalFocus", pictx)
out[#out+1] = wrap("AiBuyPirateFleet", pictx)
out[#out+1] = wrap("AiDiplomatTick", pictx)
out[#out+1] = wrap("AiArmyLegacyTick")
-- perceive callees (narrow within AiBrainPerceive)
out[#out+1] = wrap("AiEnsureCapital", pictx)
out[#out+1] = wrap("AiGroupCentroid")
-- AiEnemyPowerAround is handled specially above (per-unit crumbs)
out[#out+1] = wrap("AiContinentOf")
out[#out+1] = wrap("AiSquadAssign", pictx)
return table.concat(out, ", ")
