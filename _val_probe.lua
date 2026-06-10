local function validate(rk)
  local race = AiRaces and AiRaces[rk]
  if not race then return "NO def" end
  local P = {}
  local prod = race.production
  if not prod then P[#P+1]="no .production"
  else
    local w = prod.worker
    if not w then P[#P+1]="no worker"
    else
      if w.id==nil then P[#P+1]="worker.id nil" end
      if not w.from or #w.from==0 then P[#P+1]="worker.from empty" end
    end
  end
  local blds = race.buildings
  if not blds then P[#P+1]="no .buildings"
  else
    local n=0
    for _,row in ipairs(blds) do n=n+1; if type(row[1])~="number" then P[#P+1]="bld["..n.."] not num" end end
    if n==0 and blds.seed==nil then P[#P+1]="buildings empty" end
  end
  local comp = race.compTarget
  if comp and prod then
    local miss=0
    for unitId,_ in pairs(comp) do
      if type(unitId)=="number" then
        local found=false
        for bt,rows in pairs(prod) do
          if bt~="worker" and type(rows)=="table" then
            for _,row in ipairs(rows) do
              if row[1]==unitId or (row.branch and (row.black==unitId or row.other==unitId)) then found=true break end
            end
          end
          if found then break end
        end
        if not found then miss=miss+1 end
      end
    end
    if miss>0 then P[#P+1]="compTarget "..miss.." units w/o producer" end
  end
  if #P==0 then return "OK" else return table.concat(P,"; ") end
end
local seen,out={}, {}
for pi=2,23 do
  local rk=AiRace[pi]
  if rk and not seen[rk] then seen[rk]=true; out[#out+1]=rk..": "..validate(rk) end
end
return table.concat(out,"\n")
