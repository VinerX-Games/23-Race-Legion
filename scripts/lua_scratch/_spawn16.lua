-- Small-but-strong test: set dials BEFORE spawning, then spawn 16 random-race bots.
AiBrainDesiredArmy = 80
AiBotAuras = { {FourCC('aib0'), 10}, {FourCC('aib1'), 10} }  -- +50% atk/move speed, +7 armor
AiBotHPMult = 1.5
AiBotDmgMult = 1.5

local n = 0
for pi = 1, 16 do
    createAiPlayer(pi, nil)  -- nil = random race
    n = n + 1
end

-- Verify handicaps actually applied (does >100% stick or clamp?)
local hp = GetPlayerHandicap(Player(1))
local dmg = (GetPlayerHandicapDamage ~= nil) and GetPlayerHandicapDamage(Player(1)) or -1
return "spawned " .. n .. " random bots | desiredArmy=" .. AiBrainDesiredArmy
    .. " | P1 handicap HP=" .. tostring(hp) .. " dmg=" .. tostring(dmg)
    .. " | listlen=" .. #AiBrainBotList
