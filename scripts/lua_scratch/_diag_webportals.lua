-- Resolve every web-portal: position, own continent, dest-rect continent, alive.
-- Pairs are (portalGlobalSuffix, destRectName, radius).
local pairs_ = {
  {"n003_0044","UndecityOutTop",800},{"n003_0046","UndecityOutBot",800},
  {"n003_0050","UndercityInR",800},{"n003_0051","UndercityInTop",800},
  {"n003_0516","OrgrimmarTopIn",800},{"n003_0514","OrgrimmarBotIn",800},
  {"n003_0517","OrgrimmarTopOut",800},{"n003_0518","OrgrimmarBotOut",800},
  {"n003_0521","DeadminersOut",800},{"n003_0420","DeadminerIn",800},
  {"n003_0943","DarkM_4",1200},{"n003_0942","DarkM_3",1200},
  {"n003_0940","DarkM_1",1200},{"n003_0941","DarkM_2",1200},
  {"n003_0098","Nord_5",1200},{"n003_0060","AzNer_5",650},
  {"n003_0097","AzNer_2",1200},{"n003_1004","Nord4",1200},
  {"n003_1002","Nord_1",1200},{"n003_0995","AzNer1",1200},
  {"n003_0118","QtunIn",1200},{"n003_0117","QtunIn2",1200},
  {"n003_0124","QtunOut",1200},{"n003_0123","QtunOu2",1200},
  {"n003_0308","MarodonOut",900},{"n003_0311","MarodonOut2",900},
  {"n003_0305","MarodonIn",900},{"n003_0314","MarodonIn2",900},
  {"n003_0025","GnomreganIn",1200},{"n003_0018","GnomreganOut",1200},
  {"n003_0024","Stalgorn",1200},{"n003_0019","StalgornOut",1200},
  {"n003_0028","TrainIn",1200},{"n003_0149","TrainOut",1200},
  {"n003_0021","GrimBatolOut",1200},{"n003_0022","GrimBatolIn",1200},
  {"n003_0027","UldamanIn",1200},{"n003_0020","UldamanOut",1200},
  {"n003_0126","NaxOut",1200},{"n003_0588","DalaranOut",1200},{"n003_0090","TurtleOut",800},
  {"n01Y_0889","ED_1",750},{"n01Y_1012","ED_1_B",750},{"n01Y_0934","ED_2",750},
  {"n01Y_1013","ED_2_b",750},{"n01Y_0896","ED_3",750},{"n01Y_1014","ED_3_b",750},
  {"n01Y_1015","ED_4_b",750},{"n01Y_0897","ED_4",750},{"n01Z_1016","ED_5",750},{"n01Z_1017","ED_5_B",750},
  {"n006_0023","DarkPortal1",1200},{"n006_0438","DarkPortal2",1200},
  {"n001_0845","Region_009",1200},{"n04O_0136","Region_010",1200},
  {"n00W_0442","EKportalAlterac",1200},{"n00W_0589","OutlandNagrand",1200},
  {"n00W_0446","Region_013",1200},{"n001_0847","Region_014",1200},
  {"n065_0125","ArgusShip",1200},{"n00W_0848","Broken_Island",1200},
  {"n01B_0849","Region_017",1200},{"n01B_0850","Region_018",1200},
  {"n01Y_0578","Teldrasil",1200},{"n01Y_0580","Darnas",1200},
  {"n060_0350","Silvermoon",1200},{"n060_0287","QuelIsland",1200},
}
local out={}
local function L(s) out[#out+1]=s end
local cross=0
for _,t in ipairs(pairs_) do
  local u = _G["gg_unit_"..t[1]]
  local r = _G["gg_rct_"..t[2]]
  if u~=nil and r~=nil then
    local alive = GetUnitState(u,UNIT_STATE_LIFE)>0.405
    local px,py = GetUnitX(u), GetUnitY(u)
    local rx,ry = GetRectCenterX(r), GetRectCenterY(r)
    local sc = AiContinentOf(px,py)
    local dc = AiContinentOf(rx,ry)
    if sc~=dc then
      cross=cross+1
      L(string.format("%-12s (%6d,%6d) %-16s -> %-16s R=%d alive=%s",
        t[1], R2I(px),R2I(py), tostring(sc), tostring(dc), t[3], tostring(alive)))
    end
  else
    L(t[1].."  MISSING unit="..tostring(u~=nil).." rect="..tostring(r~=nil))
  end
end
L("--- cross-continent web-portals: "..cross)
return table.concat(out,"\n")
