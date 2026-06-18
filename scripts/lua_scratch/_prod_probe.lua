local pi=11
local race=AiRaceOf(pi)
local prod=race.production
local comp=race.compTarget
local o={}
o[#o+1]="race="..tostring(AiRace[pi])
-- worker
local w=prod.worker
o[#o+1]="worker.id="..tostring(w and w.id).." from#="..tostring(w and w.from and #w.from)
-- for each compTarget unit: current count, producer building found?
local cnt=0
for unitId,ratio in pairs(comp) do
  if type(unitId)=="number" and cnt<12 then
    cnt=cnt+1
    local cur=getAiCount and getAiCount(pi,unitId) or -1
    -- find producer bld type
    local bt=nil
    for bldType,rows in pairs(prod) do
      if bldType~="worker" and type(rows)=="table" then
        for _,row in ipairs(rows) do
          if row[1]==unitId then bt=bldType break end
        end
      end
      if bt then break end
    end
    local prodBld = bt and AiFindProdBuilding(pi,bt) or nil
    o[#o+1]=string.format("u=%d ratio=%.2f cur=%d bldType=%s prodBldFound=%s",unitId,ratio,cur,tostring(bt),tostring(prodBld~=nil))
  end
end
return table.concat(o,"\n")
