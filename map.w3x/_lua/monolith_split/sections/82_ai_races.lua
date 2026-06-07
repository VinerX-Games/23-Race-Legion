-- Automatically split from 81_ai.lua: race definitions + join functions
-- Load order: after 81_ai.lua (engines must exist before races register)


RegisterAiRace("Scarlet", {
    tokens = {"scarlet", "so"},
    weight = 1,
    altar = FourCC('h05X'),
    start = startScarlet,
    buildings = {
        seed = FourCC('h05Y'),
        { FourCC('h05U'), 4, 4 }, { FourCC('h05Y'), 15, 4 }, { FourCC('h05Z'), 15, 4 },
        { FourCC('h063'), 25, 1 }, { FourCC('h062'), 5, 2 }, { FourCC('h060'), 6, 2 },
        { FourCC('h05X'), 3, 5 },
        { FourCC('h064'), 7, 8, gate = "tier2" }, { FourCC('h061'), 15, 8, gate = "tier2" },
        { FourCC('h068'), 15, 10, gate = "church" },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h05V')) + getAiCount(pi, FourCC('h05W')) >= 1 end,
        tier3 = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,
        church = function(pi) return getAiCount(pi, FourCC('h05W')) >= 1 end,
        has_h060 = function(pi) return getAiCount(pi, FourCC('h060')) >= 1 end,
        R040_church = function(pi) return (AiData[pi][FourCC('R040')] or false) and getAiCount(pi, FourCC('h05W')) >= 1 end,
        R03Z_church = function(pi) return (AiData[pi][FourCC('R03Z')] or false) and getAiCount(pi, FourCC('h05W')) >= 1 end,
    },
    production = {
        [FourCC('h05Z')] = {
            { FourCC('h03B'), 1 },
            { FourCC('n007'), 1, gate = "has_h060" },
            { FourCC('h039'), 4, gate = "tier2" },
            { FourCC('h066'), 6, gate = "tier3" },
        },
        [FourCC('h064')] = {
            { FourCC('o00I'), 1 },
        },
        [FourCC('h061')] = {
            { FourCC('h067') }, { FourCC('n008') },
        },
        [FourCC('h05X')] = {
            { FourCC('H06C') }, { FourCC('H03H') }, { FourCC('H06B') },
        },
        [FourCC('h068')] = {
            { 0, 1 },
            { FourCC('h03F'), 1, gate = "R040_church" },
            { FourCC('h03D'), 1, gate = "R040_church" },
            { FourCC('h03I'), 1, gate = "R03Z_church" },
            { FourCC('h03G'), 1, gate = "R03Z_church" },
        },
        pre = function(id, pi, u)
            if id == FourCC('h05U') then
                local r = GetRandomInt(1, 3)
                if r == 1 and getAiCount(pi, FourCC('h014')) < 20 then
                    IssueImmediateOrderById(u, FourCC('h014'))
                elseif r == 2 and getAiCount(pi, FourCC('h03C')) < 15 then
                    IssueImmediateOrderById(u, FourCC('h03C'))
                elseif r == 3 and getAiCount(pi, FourCC('h03A')) < 15 then
                    IssueImmediateOrderById(u, FourCC('h03A'))
                end
                return true
            end
            return false
        end,
    },
    ecoWeights = {
        [FourCC('h05Y')] = 1, [FourCC('h05U')] = 2,
        [FourCC('h05V')] = 5, [FourCC('h05W')] = 8,
    },
    strategData = {
        gradeCap = 100,
        pre = function(i, pi, p)
            if i > 65 and getAiCount(pi, FourCC('h05V')) >= 1 then
                local r = GetRandomInt(1, 2)
                if r == 1 then
                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R040'), 1)
                    AiData[pi][FourCC('R040')] = true
                else
                    MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R03Z'), 1)
                    AiData[pi][FourCC('R03Z')] = true
                end
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R044'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R043'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R042'), 3)
                MakeGradeCheckCap(p, FourCC('h068'), FourCC('R041'), 3)
            end
        end,
        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h060'), FourCC('R04B'), 6}, {FourCC('h060'), FourCC('R04A'), 6}, {FourCC('h060'), FourCC('R049'), 6}, {FourCC('h060'), FourCC('R048'), 6}, {FourCC('h060'), FourCC('R04C'), 6},
                {FourCC('h062'), FourCC('RHac'), 6}, {FourCC('h062'), FourCC('Rhlh'), 6},
                {FourCC('h05Z'), FourCC('R03K'), 3},
            }},
            { at = 17, action = "tryBuy" },
            { at = 35, gate = "tier2", action = "research", rows = {
                {FourCC('h05Z'), FourCC('R03W'), 2}, {FourCC('h05Z'), FourCC('R03V'), 2},
                {FourCC('h05Z'), FourCC('R03L'), 2}, {FourCC('h05Z'), FourCC('R03M'), 2},
                {FourCC('h061'), FourCC('R03Y'), 3}, {FourCC('h061'), FourCC('R03X'), 3},
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h064'), FourCC('R03T'), 6} },
                { {FourCC('h064'), FourCC('R03S'), 6} },
            }},
            { at = 35, gate = "tier2", action = "research", rows = {
                {FourCC('h064'), FourCC('R047'), 6}, {FourCC('h064'), FourCC('R046'), 6}, {FourCC('h064'), FourCC('R045'), 6}, {FourCC('h064'), FourCC('R03U'), 6},
            }},
            { at = 45, action = "fleet", wall = FourCC('h011') },
            { at = 25, action = "techUp", from = FourCC('h05U'), to = FourCC('h05V'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h05V'), to = FourCC('h05W'), cap = 3 },
            { at = 60, action = "mageTp" },
        },
    },
    attackerData = {
        [FourCC('H06C')] = {
            { order = "firebolt", chance = 5, type = "target" },
            { order = "flamestrike", chance = 5, type = "point" },
            { order = "waterelemental", chance = 5, type = "immediate" },
        },
        [FourCC('H06B')] = {
            { order = "berserk", chance = 5, type = "immediate" },
            { order = "thunderclap", chance = 5, type = "immediate" },
            { order = "roar", chance = 5, type = "immediate" },
        },
        [FourCC('H03H')] = {
            { order = "firebolt", chance = 5, type = "heal", allyRange = 450 },
            { order = "roar", chance = 5, type = "immediate" },
            { order = "resurrection", chance = 5, type = "immediate" },
        },
        [FourCC('h067')] = {
            { order = "flamingarrows", chance = 4, type = "target" },
            { order = "devourmagic", chance = 4, type = "target", range = 525 },
        },
        [FourCC('n008')] = {
            { order = "flamingarrows", chance = 4, type = "target" },
            { order = "dispel", chance = 4, type = "point", range = 490 },
        },
        [FourCC('h03G')] = {
            { order = "berserk", chance = 3, type = "target" },
            { order = "roar", chance = 3, type = "point" },
        },
        [FourCC('h00Z')] = {
            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },
            { order = "clusterrockets", chance = 6, type = "point", range = 300 },
            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },
        },
        [FourCC('h00Y')] = {
            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },
            { order = "clusterrockets", chance = 6, type = "point", range = 300 },
            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },
        },
    },
    attackedData = {
        [FourCC('h039')] = {
            { order = "defend", chance = 5, type = "immediate" },
            { order = "magicdefense", chance = 5, type = "immediate" },
            { order = "undefend", chance = 5, type = "immediate" },
            { order = "magicundefense", chance = 5, type = "immediate" },
        },
        [FourCC('h03B')] = {
            { order = "defend", chance = 3, type = "immediate" },
            { order = "undefend", chance = 3, type = "immediate" },
        },
    },
    getLvlData = {
        [FourCC('H06C')] = { ult = FourCC('A09M'), skills = { FourCC('A09K'), FourCC('A09L'), FourCC('A09N') } },
        [FourCC('H06B')] = { ult = FourCC('A09J'), skills = { FourCC('A09F'), FourCC('A09G'), FourCC('A09I') } },
        [FourCC('H03H')] = { ult = FourCC('A09E'), skills = { FourCC('A097'), FourCC('A09C'), FourCC('A09D') } },
    },
    chooseBuild = ChooseBuildings_ScarletOrden,
    perebor = PereborBuildings_ScarletOrden,
    join = Join_Skarlet,
    strateg = Strateg_Scarlet,
    strategEC = Strateg_Scarlet_EC,
    upgrade = UpgradeScarlet,
    naval = aiNavalTrain_Common,
    wall = FourCC('h011'),
})

RegisterAiRace("BloodElves", {
    tokens = {"be", "bloodelves", "ek"},
    weight = 1,
    altar = FourCC('h05J'),
    start = startBloodElves,
    buildings = {
        seed = FourCC('h04M'),
        { FourCC('h04C'), 4, 4 }, { FourCC('h04M'), 15, 4 }, { FourCC('h04D'), 15, 4 },
        { FourCC('h04N'), 25, 1 }, { FourCC('h04Q'), 5, 2 }, { FourCC('h04R'), 6, 2 },
        { FourCC('h05J'), 3, 8 },
        { FourCC('h04G'), 15, 8, gate = "tier2" }, { FourCC('h04E'), 15, 8, gate = "tier2" },
        { FourCC('h04F'), 12, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h04B')) + getAiCount(pi, FourCC('h04A')) >= 1 end,
        tier3 = function(pi) return getAiCount(pi, FourCC('h04A')) >= 1 end,
        has_h04R = function(pi) return getAiCount(pi, FourCC('h04R')) >= 1 end,
    },
    production = {
        [FourCC('h04D')] = {
            { FourCC('h03V'), 1 },
            { FourCC('n00I'), 1, gate = "has_h04R" },
            { FourCC('h03X'), 4, gate = "tier2" },
            { FourCC('h03Y'), 6, gate = "tier3" },
        },
        [FourCC('h04G')] = {
            { FourCC('e001'), 1, gate = "tier2" },
            { FourCC('h046'), 2, gate = "tier2" },
            { FourCC('e030'), 1, gate = "tier2" },
            { FourCC('h03Z'), 6, gate = "tier3" },
        },
        [FourCC('h04E')] = {
            { FourCC('h03W') }, { FourCC('h040') }, { FourCC('h041') }, { FourCC('h042') },
        },
        [FourCC('h05J')] = {
            { FourCC('Hjnd') }, { FourCC('H043') }, { FourCC('H045') },
        },
        worker = { id = FourCC('h04K'), cap = 20,
                   from = { FourCC('h04C') } },
    },
    ecoWeights = {
        [FourCC('h04M')] = 1, [FourCC('h04C')] = 2,
        [FourCC('h04B')] = 5, [FourCC('h04A')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h04R'), FourCC('R01L'), 6}, {FourCC('h04R'), FourCC('R01J'), 6}, {FourCC('h04R'), FourCC('R01K'), 6}, {FourCC('h04R'), FourCC('R01M'), 6} },
                { {FourCC('h04R'), FourCC('R01R'), 6}, {FourCC('h04Q'), FourCC('R03I'), 6}, {FourCC('h04Q'), FourCC('R03J'), 6}, {FourCC('h04Q'), FourCC('R01N'), 6} },
                { {FourCC('h04Q'), FourCC('R01T'), 6}, {FourCC('h04Q'), FourCC('R03E'), 6}, {FourCC('h04Q'), FourCC('R03F'), 6}, {FourCC('h04D'), FourCC('R03K'), 1} },
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h04D'), FourCC('R01Y'), 1}, {FourCC('h04D'), FourCC('R01X'), 1}, {FourCC('h04D'), FourCC('R01W'), 2}, {FourCC('h04E'), FourCC('R0BU'), 1}, {FourCC('h04E'), FourCC('R01O'), 6} },
                { {FourCC('h04E'), FourCC('R01P'), 6}, {FourCC('h04E'), FourCC('R01Q'), 6}, {FourCC('h04E'), FourCC('R01S'), 1}, {FourCC('h04G'), FourCC('R03N'), 6}, {FourCC('h04G'), FourCC('R021'), 6} },
                { {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('R03Q'), 6}, {FourCC('h04G'), FourCC('R021'), 6}, {FourCC('h04G'), FourCC('Rhcd'), 6} },
            }},
            { at = 35, gate = "tier2", action = "random", branches = {
                { {FourCC('h04F'), FourCC('R03R'), 3} },
                { {FourCC('h04F'), FourCC('R01H'), 3} },
                { {FourCC('h04F'), FourCC('R01I'), 3} },
                { {FourCC('h04F'), FourCC('R01G'), 3} },
                { {FourCC('h04F'), FourCC('R01D'), 3} },
            }},
            { at = 45, gate = "tier2", action = "fleet", wall = FourCC('h011') },
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h04C'), to = FourCC('h04B'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h04B'), to = FourCC('h04A'), cap = 3 },
            { at = 60, action = "mageTp", cap = 3 },
        },
    },
    attackerData = {
        [FourCC('H043')] = {
            { order = "banish", chance = 6, type = "target" },
            { order = "steal", chance = 6, type = "target" },
            { order = "flamestrike", chance = 6, type = "point" },
            { order = "summonphoenix", chance = 6, type = "immediate" },
        },
        [FourCC('Hjnd')] = {
            { order = "shadowstrike", chance = 3, type = "target", notStructure = true },
            { order = "faeriefire", chance = 3, type = "target" },
        },
        [FourCC('H045')] = {
            { order = "roar", chance = 5, type = "immediate" },
            { order = "fanofknives", chance = 5, type = "immediate" },
            { order = "resurrection", chance = 5, type = "immediate" },
        },
        [FourCC('H03H')] = {
            { order = "berserk", chance = 4, type = "immediate" },
        },
        [FourCC('n040')] = {
            { order = "frostarmoron", chance = 5, type = "immediate" },
            { order = "curseon", chance = 5, type = "immediate" },
            { order = "carrionswarm", chance = 5, type = "point", range = 490 },
        },
        [FourCC('h041')] = {
            { order = "polymorph", chance = 3, type = "target" },
            { order = "devourmagic", chance = 3, type = "target", range = 490 },
        },
        [FourCC('h042')] = {
            { order = "faeriefireon", chance = 6, type = "immediate" },
            { order = "curseon", chance = 6, type = "immediate" },
            { order = "bloodluston", chance = 6, type = "immediate" },
        },
        [FourCC('H03Y')] = {
            { order = "healingwave", chance = 3, type = "heal", allyRange = 550 },
        },
        [FourCC('h00Z')] = {
            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },
            { order = "clusterrockets", chance = 6, type = "point", range = 300 },
            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },
        },
        [FourCC('h00Y')] = {
            { order = "ancestralspirit", chance = 6, type = "target", range = 125 },
            { order = "clusterrockets", chance = 6, type = "point", range = 300 },
            { order = "tranquility", chance = 6, type = "immediate", hp = 45 },
        },
    },
    attackedData = {
        [FourCC('h03V')] = {
            { order = "defend", chance = 5, type = "immediate" },
            { order = "manashieldon", chance = 5, type = "immediate" },
            { order = "undefend", chance = 5, type = "immediate" },
        },
        [FourCC('h03B')] = {
            { order = "defend", chance = 3, type = "immediate" },
            { order = "undefend", chance = 3, type = "immediate" },
        },
    },
    getLvlData = {
        [FourCC('H043')] = { ult = FourCC('AHpx'), skills = { FourCC('AHfs'), FourCC('AHdr'), FourCC('AHpx') } },
        [FourCC('Hjnd')] = { ult = FourCC('A07V'), skills = { FourCC('A07U'), FourCC('A0LQ'), FourCC('AEar') } },
        [FourCC('H045')] = { ult = FourCC('AHre'), skills = { FourCC('A08H'), FourCC('A07W'), FourCC('AHbh') } },
    },
    chooseBuild = ChooseBuildings_BloodElves,
    perebor = PereborBuildings2_BloodElves,
    join = Join_BloodElves,
    strateg = Strateg_BloodElves,
    strategEC = Strateg_BloodElves_EC,
    upgrade = UpgradeBloodElves,
    naval = aiNavalTrain_Common,
    wall = FourCC('h011'),
})

RegisterAiRace("Goblins", {
    tokens = {"goblins", "gob"},
    weight = 1,
    altar = FourCC('o016'),
    start = startGoblins,
    buildings = {
        seed = FourCC('h077'),
        { FourCC('h070'), 4, 5 }, { FourCC('h077'), 20, 3 }, { FourCC('h073'), 18, 7 },
        { FourCC('h07S'), 30, 1 }, { FourCC('h079'), 5, 3 }, { FourCC('h076'), 18, 4 },
        { FourCC('o016'), 3, 8 },
        { FourCC('h074'), 15, 2, gate = "grades8" }, { FourCC('h075'), 15, 2, gate = "grades8" },
    },
    gates = {
        grades8 = function(pi) return Grades[pi] > 8 end,
    },
    production = {
        [FourCC('h070')] = {
            { FourCC('n00V'), 2, limit = 25 },
        },
        [FourCC('h074')] = {
            { FourCC('h06S'), 2 }, { FourCC('h06U'), 2 },
            { FourCC('h06Y'), 4 }, { FourCC('h06R'), 3 }, { FourCC('h06T'), 3 },
        },
        [FourCC('h075')] = {
            { FourCC('o00W'), 2 }, { FourCC('o00Y'), 2 },
            { FourCC('o00X'), 3 }, { FourCC('h06P'), 3 },
        },
        [FourCC('o016')] = {
            { FourCC('H0BD'), 1, limit = 1 },
            { FourCC('Galh'), 1, limit = 1 },
            { FourCC('Gmex'), 1, limit = 1 },
        },
        pre = function(id, pi, u)
            if id == FourCC('h073') then
                if Random(1, 6) then
                    IssueNeutralImmediateOrderById(Player(pi), u, FourCC('h07R'))
                else
                    return false
                end
                return true
            end
            return false
        end,
        [FourCC('h073')] = {
            { FourCC('h06K'), 2 },
            { FourCC('h060'), 1, gate = "grades8" },
            { FourCC('h06Q'), 3, gate = "grades8" },
            { FourCC('h06L'), 3, gate = "grades8" },
            { FourCC('h06N'), 3, gate = "grades8" },
            { FourCC('h078'), 3, gate = "grades8" },
            { FourCC('h06M'), 3, gate = "grades8" },
        },
    },
    ecoWeights = {
        [FourCC('h077')] = 1, [FourCC('h070')] = 4,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { at = 17, action = "research", rows = {
                {FourCC('h076'), FourCC('R04P'), 6}, {FourCC('h076'), FourCC('R04E'), 6}, {FourCC('h076'), FourCC('R04F'), 6}, {FourCC('h076'), FourCC('R04G'), 6}, {FourCC('h076'), FourCC('R04H'), 6},
                {FourCC('h076'), FourCC('R04I'), 6}, {FourCC('h076'), FourCC('R04J'), 6}, {FourCC('h076'), FourCC('R04K'), 6}, {FourCC('h076'), FourCC('R04L'), 6}, {FourCC('h076'), FourCC('R04M'), 6},
                {FourCC('h079'), FourCC('R056'), 6}, {FourCC('h079'), FourCC('R07A'), 6}, {FourCC('h079'), FourCC('R05X'), 6}, {FourCC('h079'), FourCC('R05Y'), 6}, {FourCC('h079'), FourCC('R04N'), 6},
                {FourCC('h079'), FourCC('R04Q'), 6}, {FourCC('h079'), FourCC('R04R'), 6}, {FourCC('h079'), FourCC('R053'), 6}, {FourCC('h079'), FourCC('R05W'), 6},
                {FourCC('h070'), FourCC('R0D4'), 6},
            }},
            { at = 17, action = "tryBuy" },
            { at = 60, action = "mageTp" },
        },
    },
    attackerData = {
        [FourCC('h06K')] = {
            { order = "flamestrike", chance = 4, type = "point" },
        },
        [FourCC('h06Y')] = {
            { order = "bearform", chance = 4, type = "immediate" },
        },
        [FourCC('h06Z')] = {
            { order = "bearform", chance = 4, type = "immediate" },
        },
        [FourCC('h06P')] = {
            { order = "berserk", chance = 3, type = "immediate" },
            { order = "dispel", chance = 6, type = "point", range = 280 },
            { order = "ward", chance = 6, type = "point" },
        },
        [FourCC('H0BD')] = {
            { order = "silence", chance = 5, type = "point" },
            { order = "clusterrockets", chance = 5, type = "point" },
            { order = "blizzard", chance = 5, type = "point" },
        },
        [FourCC('Galh')] = {
            { order = "transmute", chance = 5, type = "target" },
            { order = "acidbomb", chance = 5, type = "target" },
            { order = "chemicalrage", chance = 5, type = "immediate" },
            { order = "healingspray", chance = 5, type = "self" },
        },
        [FourCC('Gmex')] = {
            { order = "summonfactory", chance = 5, type = "point" },
            { order = "clusterrockets", chance = 5, type = "point" },
            { order = "robogoblin", chance = 5, type = "immediate" },
        },
        [FourCC('h06X')] = {
            { order = "berserk", chance = 4, type = "immediate" },
            { order = "blackarrowon", chance = 5, type = "target" },
            { order = "tranquility", chance = 6, type = "immediate", hp = 40 },
        },
        [FourCC('h06V')] = {
            { order = "ravenform", chance = 4, type = "immediate" },
        },
        [FourCC('h06W')] = {
            { order = "ravenform", chance = 4, type = "immediate" },
        },
        post = {
            { order = "berserk", chance = 4, type = "immediate", needAbil = FourCC('A0BL') },
        },
    },
    getLvlData = {
        [FourCC('H0BD')] = { ult = FourCC('A0D7'), skills = { FourCC('A0D8'), FourCC('AEar'), FourCC('A0D5') } },
        [FourCC('Galh')] = { ult = FourCC('ANtm'), skills = { FourCC('ANhs'), FourCC('ANab'), FourCC('ANcr') } },
        [FourCC('Gmex')] = { ult = FourCC('ANrg'), skills = { FourCC('ANsy'), FourCC('ANcs'), FourCC('ANeg') } },
    },
    chooseBuild = ChooseBuildings_Goblins,
    perebor = PereborBuildings_Goblins,
    join = Join_Goblins,
    strateg = Strateg_Goblins,
    strategEC = Strateg_Goblins_EC,
    naval = aiNavalTrain_Goblins,
    wall = FourCC('h0D7'),
})

RegisterAiRace("Naga", {
    tokens = {"naga"},
    weight = 1,
    altar = FourCC('nnad'),
    start = startNaga,
    buildings = {
        seed = FourCC('nnfm'),
        { FourCC('nntt'), 3, 5 }, { FourCC('nnfm'), 20, 4 }, { FourCC('nnsg'), 18, 6 },
        { FourCC('nntg'), 30, 1 }, { FourCC('h0JW'), 5, 2 }, { FourCC('nnad'), 3, 6 },
        { FourCC('nnsa'), 15, 2 }, { FourCC('n055'), 15, 3 },
    },
    chooseBuild = ChooseBuildings_Naga,
    perebor = PereborBuildings_Naga,
    production = {
        [FourCC('nnsg')] = {
            { FourCC('n04Z'), 2 },
            { FourCC('nsnp'), 2, gate = "has_h0JW" },
            { FourCC('nhyc'), 1, gate = "has_h0JX" },
            { branch = "murloc", black = FourCC('n052'), other = FourCC('nmyr'), weight = 3, gate = "has_h0JX" },
        },
        [FourCC('nnsa')] = {
            { FourCC('n053'), 6, gate = "murloc_h0JX" },
            { FourCC('n054'), 6, gate = "murloc_h0JX" },
            { FourCC('n051'), 1, gate = "naga_h0JX" },
            { FourCC('nnsw'), 4, gate = "naga_h0JX" },
        },
        [FourCC('n055')] = {
            { branch = "murloc", black = FourCC('n050'), other = FourCC('nnrg'), weight = 2, gate = "has_h0JY" },
            { FourCC('n056'), 1, gate = "has_h0JY" },
            { FourCC('nwgs'), 1 },
        },
        [FourCC('nnad')] = {
            { FourCC('N07A'), 1, limit = 1 },
            { FourCC('H0JV'), 1, limit = 1 },
            { branch = "murloc", black = FourCC('H0OZ'), other = FourCC('H0JU'), weight = 1, limit = 1 },
        },
        worker = { id = FourCC('nmpe'), cap = 25,
                   from = { FourCC('nntt'), FourCC('h0JX'), FourCC('h0JY') } },
        pre = function(id, pi, u)
            if id == FourCC('nntt') or id == FourCC('h0JX') or id == FourCC('h0JY') then
                if getAiCount(pi, FourCC('nmpe')) >= 25 and GetRandomInt(1, 2) == 1 then
                    IssueImmediateOrderById(u, FourCC('nnmg'))
                    return true
                end
                return false
            end
            return false
        end,
    },
    gates = {
        has_h0JW = function(pi) return getAiCount(pi, FourCC('h0JW')) > 0 end,
        has_h0JX = function(pi) return getAiCount(pi, FourCC('h0JX')) > 0 end,
        has_h0JY = function(pi) return getAiCount(pi, FourCC('h0JY')) > 0 end,
        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
        naga = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
        murloc_h0JX = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,
        naga_h0JX = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) and getAiCount(pi, FourCC('h0JX')) > 0 end,
    },
    branches = {
        murloc = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true) end,
    },
    ecoWeights = {
        [FourCC('nnfm')] = 1, [FourCC('nntt')] = 4,
        [FourCC('h0JX')] = 6, [FourCC('h0JY')] = 8,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { before = 50, action = "research", rows = {
                {FourCC('nntt'), FourCC('R0FE'), 1}, {FourCC('nntt'), FourCC('R0FF'), 1},
            }},
            { at = 17, action = "research", rows = {
                {FourCC('h0JW'), FourCC('R0FD'), 6}, {FourCC('h0JW'), FourCC('R0FH'), 6}, {FourCC('h0JW'), FourCC('Rnat'), 6}, {FourCC('h0JW'), FourCC('Rnam'), 6}, {FourCC('h0JW'), FourCC('Rnsb'), 6},
                {FourCC('nnsa'), FourCC('Rnsw'), 6}, {FourCC('nnsa'), FourCC('Rnsi'), 6},
                {FourCC('nnsg'), FourCC('R0FR'), 6}, {FourCC('nnsg'), FourCC('Rnen'), 6},
            }},
            { at = 17, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('nntt'), to = FourCC('h0JX'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0JX'), to = FourCC('h0JY'), cap = 3 },
            { at = 60, action = "mageTp" },
        },
    },
    attackerData = {
        pre = {
            { order = "blight", chance = 1, type = "immediate", terrain = "water", notAbil = FourCC('S00E'), ret = true },
        },
        [FourCC('H0JV')] = {
            { order = "berserk", chance = 3, type = "immediate" },
            { order = "clusterrockets", chance = 5, type = "point" },
            { order = "blink", chance = 5, type = "point" },
        },
        [FourCC('N07A')] = {
            { order = "banish", chance = 5, type = "target" },
            { order = "rainoffire", chance = 5, type = "point" },
            { order = "tranquility", chance = 5, type = "immediate" },
        },
        [FourCC('H0JU')] = {
            { order = "doom", chance = 6, type = "target" },
            { order = "frostnova", chance = 6, type = "target" },
            { order = "stomp", chance = 6, type = "immediate" },
        },
        [FourCC('H0OZ')] = {
            { order = "doom", chance = 6, type = "target" },
            { order = "frostnova", chance = 6, type = "target" },
            { order = "stomp", chance = 6, type = "immediate" },
        },
        [FourCC('n051')] = {
            { order = "healon", chance = 4, type = "immediate" },
            { order = "dispel", chance = 4, type = "point" },
        },
        [FourCC('nnsw')] = {
            { order = "cyclone", chance = 6, type = "target" },
            { order = "frostarmoron", chance = 6, type = "immediate" },
            { order = "parasiteon", chance = 6, type = "immediate" },
        },
        [FourCC('nnrg')] = {
            { order = "thunderbolt", chance = 6, type = "target" },
            { order = "carrionswarm", chance = 6, type = "point" },
        },
    },
    getLvlData = {
        [FourCC('H0JV')] = { ult = FourCC('A13C'), skills = { FourCC('A13A'), FourCC('AEbl') } },
        [FourCC('H0JU')] = { skills = { FourCC('A14I'), FourCC('A14G') } },
        [FourCC('N07A')] = { ult = FourCC('ANrg'), skills = { FourCC('ANsy'), FourCC('ANcs'), FourCC('ANeg') } },
    },
    join = Join_Naga,
    strateg = Strateg_Naga,
    strategEC = Strateg_Naga_EC,
    upgrade = UpgradeNaga,
    naval = aiNavalTrain_Naga,
    wall = FourCC('n04L'),
    usesWaterPoint = false,
    continentalNaga = true,
})

RegisterAiRace("Horde", {
    tokens = {"horde"},
    weight = 1,
    altar = FourCC('oalt'),
    start = startHorde,
    buildings = {
        seed = FourCC('otrb'),
        { FourCC('ogre'), 3, 5 }, { FourCC('otrb'), 20, 3 }, { FourCC('obar'), 3, 7 },
        { FourCC('obar'), 18, 3 }, { FourCC('obea'), 18, 2 }, { FourCC('owtw'), 30, 1 },
        { FourCC('ofor'), 5, 3 }, { FourCC('oalt'), 3, 6 },
        { FourCC('osld'), 15, 10, gate = "spirit" }, { FourCC('otto'), 15, 10, gate = "spirit" },
        { FourCC('osld'), 15, 1 }, { FourCC('otto'), 15, 1 }, { FourCC('ovln'), 1, 6 },
    },
    gates = {
        spirit = function(pi) return getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,
        ironHorde = function(pi) return GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,
        notIronHorde = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) end,
        spirit_notIron = function(pi) return not GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true) and getAiCount(pi, FourCC('ostr')) + getAiCount(pi, FourCC('ofrt')) > 0 end,
        fortress = function(pi) return getAiCount(pi, FourCC('ofrt')) > 0 end,
    },
    production = {
        [FourCC('obar')] = {
            { FourCC('o01N'), 2, gate = "ironHorde" },
            { FourCC('ogru'), 2, gate = "notIronHorde" },
            { FourCC('o029'), 3, gate = "spirit_notIron" },
            { FourCC('orai'), 5, gate = "fortress" },
            { FourCC('otau'), 5, gate = "fortress" },
        },
        [FourCC('obea')] = {
            { FourCC('o02B'), 2, gate = "ironHorde" },
            { FourCC('ohun'), 2, gate = "notIronHorde" },
            { FourCC('o01P'), 3, gate = "spirit_notIron" },
            { FourCC('okod'), 5, gate = "fortress" },
        },
        [FourCC('osld')] = {
            { FourCC('oshm'), 8 },
            { FourCC('o01W'), 2 },
        },
        [FourCC('otto')] = {
            { FourCC('ocat'), 2 },
            { FourCC('o022'), 1 },
            { FourCC('h0CY'), 2, gate = "ironHorde" },
        },
        [FourCC('oalt')] = {
            { FourCC('Ofar'), 1, limit = 1 },
            { FourCC('Obla'), 1, limit = 1 },
            { FourCC('Otch'), 1, limit = 1 },
        },
        worker = { id = FourCC('opeo'), cap = 25,
                   from = { FourCC('ogre'), FourCC('ostr'), FourCC('ofrt') } },
    },
    ecoWeights = {
        [FourCC('nnfm')] = 1, [FourCC('ogre')] = 4,
        [FourCC('ostr')] = 6, [FourCC('ofrt')] = 8,
    },
    strategData = {
        gradeCap = 150,
        steps = {
            { before = 50, action = "research", rows = {
                {FourCC('nntt'), FourCC('R0FE'), 1}, {FourCC('nntt'), FourCC('R0FF'), 1},
            }},
            { at = 17, action = "research", rows = {
                {FourCC('ogre'), FourCC('Ropg'), 1},
                {FourCC('ofor'), FourCC('R0G5'), 6}, {FourCC('ofor'), FourCC('R0E6'), 6}, {FourCC('ofor'), FourCC('Rome'), 6}, {FourCC('ofor'), FourCC('Roar'), 6}, {FourCC('ofor'), FourCC('Rora'), 6}, {FourCC('ofor'), FourCC('Rosp'), 3}, {FourCC('ofor'), FourCC('Rorb'), 3},
                {FourCC('obar'), FourCC('R0EC'), 3}, {FourCC('obea'), FourCC('R0ED'), 3}, {FourCC('otto'), FourCC('R0EF'), 3},
                {FourCC('osld'), FourCC('Rost'), 3}, {FourCC('osld'), FourCC('Rowt'), 3}, {FourCC('osld'), FourCC('Rowd'), 3},
            }},
            { at = 17, action = "tryBuy" },
            { at = 17, action = "fleet", wall = FourCC('h0HO') },
            { action = "random", branches = {
                { {FourCC('ovln'), FourCC('R0F3'), 1}, {FourCC('ovln'), FourCC('R0F4'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0EI'), 1} },
                { {FourCC('ovln'), FourCC('R0EE'), 1}, {FourCC('ovln'), FourCC('R0EA'), 1}, {FourCC('ovln'), FourCC('R0E9'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },
                { {FourCC('ovln'), FourCC('R0E4'), 1}, {FourCC('ovln'), FourCC('R0E3'), 1}, {FourCC('ovln'), FourCC('R0E1'), 1}, {FourCC('ovln'), FourCC('R0E0'), 1} },
                { {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0DY'), 1}, {FourCC('ovln'), FourCC('R0DX'), 1}, {FourCC('ovln'), FourCC('R0DW'), 1} },
                { {FourCC('ovln'), FourCC('R0EB'), 1}, {FourCC('ovln'), FourCC('R0EH'), 1}, {FourCC('ovln'), FourCC('R0DZ'), 1}, {FourCC('ovln'), FourCC('R0E5'), 1} },
            }},
        },
    },
    attackerData = {
        [FourCC('o01W')] = {
            { order = "bloodlust", chance = 4, type = "target" },
            { order = "lightningshield", chance = 4, type = "target" },
            { order = "purge", chance = 4, type = "target" },
        },
        [FourCC('h0CY')] = {
            { order = "berserk", chance = 3, type = "immediate" },
            { order = "selfdestruct", chance = 6, type = "immediate", hp = 20 },
        },
        [FourCC('o01J')] = {
            { order = "bloodlust", chance = 4, type = "target" },
            { order = "lightningshield", chance = 4, type = "target" },
            { order = "purge", chance = 4, type = "target" },
            { order = "dispel", chance = 4, type = "point" },
        },
        [FourCC('o01V')] = {
            { order = "soulburn", chance = 4, type = "target" },
            { order = "waterelemental", chance = 4, type = "immediate" },
            { order = "monsoon", chance = 4, type = "point" },
            { order = "dispel", chance = 4, type = "point" },
        },
        [FourCC('o023')] = {
            { order = "flamestrike", chance = 4, type = "point" },
            { order = "stampede", chance = 5, type = "point" },
        },
        [FourCC('o024')] = {
            { order = "evileye", chance = 4, type = "point" },
            { order = "stasistrap", chance = 4, type = "point" },
            { order = "healingward", chance = 4, type = "self" },
        },
        [FourCC('o02L')] = {
            { order = "evileye", chance = 4, type = "point" },
            { order = "stasistrap", chance = 4, type = "point" },
            { order = "healingward", chance = 4, type = "self" },
            { order = "acidbomb", chance = 5, type = "target" },
        },
        [FourCC('Obla')] = {
            { order = "windwalk", chance = 3, type = "immediate" },
            { order = "roar", chance = 5, type = "immediate" },
            { order = "whirlwind", chance = 5, type = "immediate" },
        },
        [FourCC('Ofar')] = {
            { order = "chainlightning", chance = 4, type = "target" },
            { order = "spiritwolf", chance = 6, type = "immediate" },
            { order = "monsoon", chance = 6, type = "point" },
        },
        [FourCC('Otch')] = {
            { order = "stomp", chance = 4, type = "immediate" },
            { order = "carrionswarm", chance = 6, type = "point" },
        },
        [FourCC('O02Z')] = {
            { order = "stomp", chance = 4, type = "immediate" },
            { order = "carrionswarm", chance = 6, type = "point" },
        },
        [FourCC('h0D0')] = {
            { order = "clusterrockets", chance = 4, type = "point" },
            { order = "blackarrowon", chance = 5, type = "target" },
            { order = "tranquility", chance = 6, type = "immediate", hp = 40 },
        },
    },
    getLvlData = {
        [FourCC('Obla')] = { ult = FourCC('AOww'), skills = { FourCC('A12F'), FourCC('AOcr') } },
        [FourCC('Ofar')] = { skills = { FourCC('A12E'), FourCC('AOcl'), FourCC('AOsf'), FourCC('AOfs') } },
        [FourCC('Otch')] = { ult = FourCC('AOre'), skills = { FourCC('AOre'), FourCC('AOr2'), FourCC('A026') } },
        [FourCC('O02Z')] = { ult = FourCC('AOre'), skills = { FourCC('AOre'), FourCC('AOr2'), FourCC('A026') } },
    },
    chooseBuild = ChooseBuildings_Horde,
    perebor = PereborBuildings_Horde,
    join = Join_Horde,
    strateg = Strateg_Horde,
    strategEC = Strateg_Horde_EC,
    upgrade = UpgradeHorde,
    naval = aiNavalTrain_Horde,
    wall = FourCC('h0HO'),
})

RegisterAiRace("JungleTrolls", {
    tokens = {"jt", "jungletrolls", "trolls"},
    weight = 1,
    altar = FourCC('h0N0'),
    start = startJungleTrolls,
    -- Phase 3 declarative build order (engine: AiRunChooseBuildings). Mirrors
    -- ChooseBuildings_JungleTrolls exactly. chooseBuild kept as fallback.
    buildings = {
        seed = FourCC('h0N2'),
        { FourCC('h0N5'), 4, 4 },
        { FourCC('h0N2'), 18, 4 },
        { FourCC('h0MY'), 10, 4 },
        { FourCC('h0N3'), 5, 2 },
        { FourCC('h0N0'), 3, 6 },
        { FourCC('h0MX'), 8, 6, gate = "tier2" },
        { FourCC('h0MW'), 8, 6, gate = "tier2" },
        { FourCC('h0D3'), 2, 1, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1
        end,
        tier3 = function(pi)
            return getAiCount(pi, FourCC('h0N6')) >= 1
        end,
    },
    -- Phase 3 declarative production (engine: AiRunProduction).
    production = {
        [FourCC('h0MY')] = {
            { FourCC('o04M'), 5 },
            { FourCC('o04L'), 4 },
            { FourCC('o05E'), 1, gate = "tier2" },
        },
        [FourCC('h0MX')] = {
            { FourCC('o04O'), 3 },
            { FourCC('o04R'), 3 },
            { branch = "jt", black = FourCC('o04N'), other = FourCC('o04P'), weight = 4 },
        },
        [FourCC('h0MW')] = {
            { FourCC('o04S'), 3 },
            { FourCC('o04U'), 4 },
            { FourCC('o05J'), 2, gate = "tier2" },
            { FourCC('o05G'), 2, gate = "tier3" },
        },
        [FourCC('h0N0')] = {
            { FourCC('O054'), 1, limit = 1 }, { FourCC('O05A'), 1, limit = 1 }, { FourCC('O05D'), 1, limit = 1 },
            { branch = "jt", black = FourCC('O05L'), other = FourCC('O055'), limit = 1 },
        },
        worker = { id = FourCC('o04Q'), cap = 18,
                   from = { FourCC('h0N5'), FourCC('h0N1'), FourCC('h0N6') } },
    },
    branches = {
        jt = function(pi) return JungleTrollsBranchIsBlack(pi) end,
    },
    -- Phase 3 declarative strategy (engine: AiRunStrateg).
    ecoWeights = {
        [FourCC('h0N2')] = 1,
        [FourCC('h0N5')] = 2,
        [FourCC('h0N1')] = 5,
        [FourCC('h0N6')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0N3'), FourCC('R0I8'), 6}, {FourCC('h0N3'), FourCC('R0I9'), 6}, {FourCC('h0N3'), FourCC('R0IA'), 6}, {FourCC('h0N3'), FourCC('R0II'), 2} },
                { {FourCC('h0MY'), FourCC('R0IK'), 6}, {FourCC('h0MY'), FourCC('R0IM'), 6}, {FourCC('h0N2'), FourCC('R0IJ'), 6} },
                { {FourCC('h0MX'), FourCC('R0IB'), 6}, {FourCC('h0MX'), FourCC('R0IC'), 6}, {FourCC('h0MX'), FourCC('R0ID'), 6} },
                { {FourCC('h0MW'), FourCC('R0IL'), 6}, {FourCC('h0MW'), FourCC('R0IN'), 6}, {FourCC('h0MW'), FourCC('R0IJ'), 6} },
            }},
            { at = 45, action = "fleet", wall = FourCC('h0D3') },
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0N5'), to = FourCC('h0N1'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0N1'), to = FourCC('h0N6'), cap = 3 },
        },
    },
    attackerData = {
        [FourCC('o04U')] = {
            { order = "berserk", chance = 3, type = "immediate" },
        },
        [FourCC('o04O')] = {
            { order = "bloodlust", chance = 4, type = "target" },
            { order = "dispel", chance = 4, type = "point" },
            { order = "slow", chance = 4, type = "target" },
        },
        [FourCC('o04R')] = {
            { order = "stasistrap", chance = 4, type = "point" },
            { order = "evileye", chance = 4, type = "point" },
            { order = "healingward", chance = 4, type = "self" },
        },
        [FourCC('o04N')] = {
            { order = "flamingarrows", chance = 4, type = "target" },
            { order = "Vengeance", chance = 5, type = "target" },
            { order = "hex", chance = 4, type = "target", notStructure = true },
        },
        [FourCC('o04P')] = {
            { order = "frostarmor", chance = 4, type = "target" },
            { order = "blizzard", chance = 4, type = "point" },
        },
        [FourCC('o04S')] = {
            { order = "ravenform", chance = 4, type = "immediate" },
        },
        [FourCC('o05J')] = {
            { order = "ravenform", chance = 4, type = "immediate" },
        },
        [FourCC('o04M')] = {
            { order = "chemicalrage", chance = 4, type = "immediate" },
        },
        [FourCC('O054')] = {
            { order = "hex", chance = 3, type = "target", notStructure = true },
        },
        [FourCC('O05A')] = {
            { order = "whirlwind", chance = 4, type = "immediate" },
        },
    },
    getLvlData = {
        [FourCC('O054')] = { ult = FourCC('AOsw'), skills = { FourCC('AOhw'), FourCC('A1E0'), FourCC('A1D0') } },
        [FourCC('O05A')] = { ult = FourCC('A1E4'), skills = { FourCC('A1E2'), FourCC('A1E3'), FourCC('A1D0') } },
        [FourCC('O05D')] = { ult = FourCC('A1E8'), skills = { FourCC('A1E6'), FourCC('A1E9'), FourCC('A1EA') } },
        [FourCC('O055')] = { ult = FourCC('A1DM'), skills = { FourCC('A1DB'), FourCC('A1DC'), FourCC('A1EL') } },
        [FourCC('O05L')] = { ult = FourCC('A1ET'), skills = { FourCC('A1ES'), FourCC('A1EV'), FourCC('A1EY') } },
    },
    chooseBuild = ChooseBuildings_JungleTrolls,
    perebor = PereborBuildings2_JungleTrolls,
    join = Join_JungleTrolls,
    strateg = Strateg_JungleTrolls,
    strategEC = Strateg_JungleTrolls_EC,
    upgrade = UpgradeJungleTrolls,
    naval = aiNavalTrain_JungleTrolls,
    wall = FourCC('h0N2'),
})

-- ====================================================================
-- ForestTrolls (Phase 3 data-driven)
-- TODO: verify building/unit mappings and research assignments
-- ====================================================================
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_ForestTrolls(id, pi, u)
    if id == FourCC('o04V') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("ForestTrolls", {
    tokens = {"ft", "foresttrolls"},
    weight = 1,
    altar = FourCC('h0MU'),
    start = startForestTrolls,
    buildings = {
        seed = FourCC('h0MV'),
        { FourCC('h0MT'), 4, 4 }, { FourCC('h0MV'), 18, 4 },
        { FourCC('h0MS'), 10, 4 }, { FourCC('h0N7'), 5, 2 },
        { FourCC('h0MU'), 3, 6 }, { FourCC('h0N4'), 25, 1 },
        { FourCC('h0MZ'), 8, 6, gate = "tier2" },
        { FourCC('h0MR'), 8, 6, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0N8')) + getAiCount(pi, FourCC('h0N9')) >= 1
        end,
    },
    production = {
        [FourCC('h0MT')] = {
            { FourCC('o04V'), 3, limit = 20 },
            { FourCC('o04X'), 1 },
        },
        [FourCC('h0N8')] = {
            { FourCC('o04V'), 3, limit = 20 },
            { FourCC('o04X'), 1 },
        },
        [FourCC('h0N9')] = {
            { FourCC('o04V'), 3, limit = 20 },
            { FourCC('o04X'), 1 },
        },
        [FourCC('h0MS')] = {
            { FourCC('o04W'), 5 },
            { FourCC('o04X'), 3 },
            { FourCC('o04Y'), 3, gate = "tier2" },
            { FourCC('o05F'), 2, gate = "tier2" },
        },
        [FourCC('h0MZ')] = {
            { FourCC('o051'), 3 },
            { FourCC('o052'), 3 },
        },
        [FourCC('h0MR')] = {
            { FourCC('o04Z'), 3 },
            { FourCC('o050'), 4 },
            { FourCC('o053'), 4 },
        },
        [FourCC('h0MU')] = {
            { FourCC('O059') }, { FourCC('O058') }, { FourCC('O057') },
            { FourCC('o05M'), 1, limit = 1, gate = "tier2" },
            { FourCC('o05N'), 1, limit = 1, gate = "tier2" },
            { FourCC('o05O'), 1, limit = 1, gate = "tier2" },
        },
    },
    ecoWeights = {
        [FourCC('h0MV')] = 1, [FourCC('h0MT')] = 2,
        [FourCC('h0N8')] = 5, [FourCC('h0N9')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0N7'), FourCC('R0D2'), 6}, {FourCC('h0N7'), FourCC('R0D3'), 6} },
                { {FourCC('h0MS'), FourCC('R0DY'), 6}, {FourCC('h0MS'), FourCC('R0EE'), 6} },
                { {FourCC('h0MZ'), FourCC('R0EH'), 6}, {FourCC('h0MZ'), FourCC('R0EI'), 6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0MT'), to = FourCC('h0N8'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0N8'), to = FourCC('h0N9'), cap = 3 },
        },
    },
    attackerData = {
        [FourCC('o04W')] = {
            { order = "berserk", chance = 4, type = "immediate" },
        },
        [FourCC('o04Y')] = {
            { order = "berserk", chance = 4, type = "immediate" },
        },
        [FourCC('o04Z')] = {
            { order = "berserk", chance = 3, type = "immediate" },
        },
        [FourCC('o053')] = {
            { order = "thunderbolt", chance = 4, type = "target" },
            { order = "berserk", chance = 4, type = "immediate" },
        },
        [FourCC('o050')] = {
            { order = "Thornyshield", chance = 4, type = "target" },
        },
        [FourCC('o051')] = {
            { order = "clusterrockets", chance = 4, type = "point" },
            { order = "ward", chance = 4, type = "point" },
        },
        [FourCC('o052')] = {
            { order = "heal", chance = 4, type = "heal", allyRange = 550 },
            { order = "dispel", chance = 4, type = "point" },
            { order = "innerfire", chance = 4, type = "target" },
        },
        [FourCC('o05M')] = {
            { order = "roar", chance = 4, type = "immediate" },
        },
        [FourCC('o05N')] = {
            { order = "howlofterror", chance = 4, type = "immediate" },
            { order = "berserk", chance = 4, type = "immediate" },
        },
        [FourCC('o05O')] = {
            { order = "chainlightning", chance = 4, type = "target" },
            { order = "monsoon", chance = 4, type = "point" },
        },
    },
    join = Join_ForestTrolls,
    naval = aiNavalTrain_JungleTrolls,
    wall = FourCC('h0N4'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_HordeW2(id, pi, u)
    if id == FourCC('w200') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif id == FourCC('w201') or id == FourCC('w220') then
        GroupAddUnit(udg_Ai_navy[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("HordeW2", {
    tokens = {"hw2", "hordew2", "orda2"},
    weight = 1,
    altar = FourCC('w20a'),
    start = startHordeW2,
    buildings = {
        seed = FourCC('w20y'),
        { FourCC('w20q'), 4, 4 }, { FourCC('w20y'), 18, 4 },
        { FourCC('w20r'), 10, 4 }, { FourCC('w214'), 5, 2 },
        { FourCC('w20a'), 3, 6 },
        { FourCC('w20i'), 8, 6, gate = "tier2" },
        { FourCC('w20t'), 8, 6, gate = "tier2" },
        { FourCC('w210'), 4, 4, gate = "tier2" },
        { FourCC('w212'), 4, 4, gate = "tier2" },
        { FourCC('w20u'), 25, 1 },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('w20w')) + getAiCount(pi, FourCC('w20e')) >= 1
        end,
    },
    production = {
        [FourCC('w20q')] = { {FourCC('w200'),3,limit=20} },
        [FourCC('w20w')] = { {FourCC('w200'),3,limit=20} },
        [FourCC('w20e')] = { {FourCC('w200'),3,limit=20} },
        [FourCC('w20r')] = {
            {FourCC('w203'), 4}, {FourCC('w204'), 4}, {FourCC('w208'), 3,gate="tier2"},
        },
        [FourCC('w20i')] = {
            {FourCC('w201'), 2}, {FourCC('w206'), 3}, {FourCC('w207'), 2,gate="tier2"},
        },
        [FourCC('w20t')] = {
            {FourCC('w205'), 3}, {FourCC('w209'), 2,gate="tier2"}, {FourCC('w211'), 3},
        },
        [FourCC('w20a')] = {
            {FourCC('W200'), 1, limit = 1}, {FourCC('W201'), 1, limit = 1}, {FourCC('W202'), 1, limit = 1},
        },
        [FourCC('w210')] = { {FourCC('w202'), 3} },
        [FourCC('w212')] = { {FourCC('w213'), 3} },
    },
    ecoWeights = {
        [FourCC('w20y')] = 1, [FourCC('w20q')] = 2,
        [FourCC('w20w')] = 5, [FourCC('w20e')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('w214'),FourCC('w2r0'),6},{FourCC('w214'),FourCC('w2r1'),6},{FourCC('w214'),FourCC('w2r2'),6},{FourCC('w214'),FourCC('w2rb'),6} },
                { {FourCC('w20r'),FourCC('w2r7'),6},{FourCC('w20r'),FourCC('w2r8'),6},{FourCC('w20r'),FourCC('w2r9'),6} },
                { {FourCC('w20t'),FourCC('w2r4'),6},{FourCC('w20t'),FourCC('w2r5'),6},{FourCC('w20t'),FourCC('w2r6'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('w20q'), to = FourCC('w20w'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('w20w'), to = FourCC('w20e'), cap = 3 },
        },
    },
    attackerData = {
        [FourCC('w208')] = {
            { order = "frenzy", chance = 4, type = "immediate" },
        },
        [FourCC('w201')] = {
            { order = "windwalk", chance = 4, type = "immediate" },
        },
        [FourCC('w206')] = {
            { order = "selfdestruct", chance = 6, type = "immediate", hp = 30 },
        },
        [FourCC('w205')] = {
            { order = "bloodlust", chance = 4, type = "target" },
            { order = "spiritwolf", chance = 5, type = "immediate" },
        },
        [FourCC('w209')] = {
            { order = "frostarmor", chance = 4, type = "target" },
            { order = "raisedead", chance = 5, type = "point" },
        },
        [FourCC('w211')] = {
            { order = "heal", chance = 4, type = "heal", allyRange = 550 },
            { order = "dispel", chance = 4, type = "point" },
            { order = "slow", chance = 4, type = "target" },
        },
        [FourCC('w202')] = {
            { order = "flamestrike", chance = 4, type = "point" },
            { order = "breathoffire", chance = 4, type = "point" },
        },
    },
    join = Join_HordeW2,
    wall = FourCC('w20u'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Nerubs(id, pi, u)
    if id == FourCC('h0BE') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif id == FourCC('u019') then
        -- Cocoon built - upgrade to intended building
        local target = AiData[pi]["upgradeCocoon"]
        if target ~= nil and target ~= 0 then
            IssueImmediateOrderById(u, target)
            AiData[pi]["upgradeCocoon"] = nil
        end
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Nerubs", {
    tokens = {"nerub", "nerubs"},
    weight = 1,
    altar = FourCC('h0CU'),
    start = startNerubs,
    chooseBuild = function(pi)
        -- Nerubs workers can only build cocoons (u019), which then upgrade
        local realBuilding = AiRunChooseBuildings(pi, AiRaces["Nerubs"])
        if realBuilding ~= 0 then
            AiData[pi]["upgradeCocoon"] = realBuilding
            return FourCC('u019')
        end
        return 0
    end,
    buildings = {
        seed = FourCC('h0GH'),
        { FourCC('h0CO'), 4, 4 }, { FourCC('h0GH'), 18, 4 },
        { FourCC('h0CR'), 10, 4 }, { FourCC('h0CS'), 5, 2 },
        { FourCC('h0CU'), 3, 6 }, { FourCC('u01A'), 25, 1 },
        { FourCC('h0CT'), 8, 6, gate = "tier2" },
        { FourCC('h0CV'), 8, 6, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0CP')) + getAiCount(pi, FourCC('h0CQ')) >= 1
        end,
    },
    production = {
        [FourCC('h0CO')] = { {FourCC('h0BE'),3,limit=20} },
        [FourCC('h0CP')] = { {FourCC('h0BE'),3,limit=20} },
        [FourCC('h0CQ')] = { {FourCC('h0BE'),3,limit=20} },
        [FourCC('h0CR')] = {
            {FourCC('u01J'), 4}, {FourCC('u01G'), 4}, {FourCC('u01F'), 3},
        },
        [FourCC('h0CT')] = {
            {FourCC('u01C'), 3}, {FourCC('u01K'), 2, gate="tier2"},
            {FourCC('u01B'), 2, gate="tier2"}, {FourCC('u01I'), 3},
        },
        [FourCC('h0CV')] = {
            {FourCC('u01H'), 3}, {FourCC('u01D'), 3},
        },
        [FourCC('h0CU')] = {
            {FourCC('U01U'), 1, limit = 1}, {FourCC('U01V'), 1, limit = 1}, {FourCC('U01W'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0GH')] = 1, [FourCC('h0CO')] = 2,
        [FourCC('h0CP')] = 5, [FourCC('h0CQ')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0CS'),FourCC('Abds'),6},{FourCC('h0CS'),FourCC('Arlm'),6} },
                { {FourCC('h0CR'),FourCC('Abds'),6} },
                { {FourCC('h0CT'),FourCC('Abds'),6},{FourCC('h0CV'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0CO'), to = FourCC('h0CP'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0CP'), to = FourCC('h0CQ'), cap = 3 },
        },
    },
    attackerData = {
        [FourCC('u01C')] = {
            { order = "parasite", chance = 4, type = "target" },
        },
        [FourCC('u01H')] = {
            { order = "heal", chance = 3, type = "heal", allyRange = 550 },
            { order = "dispel", chance = 3, type = "point" },
            { order = "lightningshield", chance = 3, type = "target" },
        },
        [FourCC('u01D')] = {
            { order = "thunderbolt", chance = 4, type = "target" },
            { order = "ward", chance = 4, type = "point" },
            { order = "entanglingroots", chance = 4, type = "target" },
        },
        [FourCC('u01E')] = {
            { order = "web", chance = 4, type = "target" },
            { order = "raisedead", chance = 5, type = "point" },
        },
    },
    join = Join_Nerubs,
    wall = FourCC('u01A'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Forsaken(id, pi, u)
    if id == FourCC('h0J5') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Forsaken", {
    tokens = {"forsaken", "fors", "ud"},
    weight = 1,
    altar = FourCC('h0JR'),
    start = startForsaken,
    buildings = {
        seed = FourCC('h0JD'),
        { FourCC('h0JP'), 4, 4 }, { FourCC('h0JD'), 18, 4 },
        { FourCC('h0JJ'), 10, 4 }, { FourCC('h0JO'), 5, 2 },
        { FourCC('h0JR'), 3, 6 }, { FourCC('h0JM'), 25, 1 },
        { FourCC('h0JI'), 4, 2, gate = "tier2" },
        { FourCC('h0JK'), 8, 6, gate = "tier2" },
    },
    gates = {
        tier2 = function(pi)
            return getAiCount(pi, FourCC('h0JQ')) + getAiCount(pi, FourCC('h0JL')) >= 1
        end,
    },
    production = {
        [FourCC('h0JP')] = { {FourCC('h0J5'), 3, limit = 22} },
        [FourCC('h0JQ')] = { {FourCC('h0J5'), 3, limit = 22} },
        [FourCC('h0JL')] = { {FourCC('h0J5'), 3, limit = 22} },
        [FourCC('h0JJ')] = {
            {FourCC('n04T'), 4}, {FourCC('h0JC'), 4},
            {FourCC('h0JN'), 3, gate = "tier2"}, {FourCC('n04U'), 2, gate = "tier2"},
        },
        [FourCC('h0JK')] = {
            {FourCC('n04Y'), 3}, {FourCC('n04X'), 3},
            {FourCC('n04V'), 2, gate = "tier2"}, {FourCC('h0JA'), 1, gate = "tier2"},
        },
        [FourCC('h0JI')] = {
            {FourCC('o02X'), 3}, {FourCC('u02C'), 2, gate = "tier2"}, {FourCC('o02Y'), 2, gate = "tier2"},
        },
        [FourCC('h0JR')] = {
            {FourCC('N058'), 1, limit = 1}, {FourCC('O031'), 1, limit = 1}, {FourCC('O030'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0JD')] = 1, [FourCC('h0JP')] = 2,
        [FourCC('h0JQ')] = 5, [FourCC('h0JL')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0JO'), FourCC('Arlm'), 6} },
                { {FourCC('h0JK'), FourCC('Abds'), 6} },
                { {FourCC('h0JJ'), FourCC('Abds'), 6},{FourCC('h0JI'), FourCC('Abds'), 6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0JP'), to = FourCC('h0JQ'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0JQ'), to = FourCC('h0JL'), cap = 3 },
        },
    },
    attackerData = {
        [FourCC('n04T')] = {
            { order = "cannibalize", chance = 4, type = "immediate", hp = 60 },
        },
        [FourCC('h0JN')] = {
            { order = "shadowstrike", chance = 4, type = "target", notStructure = true },
        },
        [FourCC('n04U')] = {
            { order = "cannibalize", chance = 4, type = "immediate", hp = 60 },
            { order = "defend", chance = 3, type = "immediate" },
        },
        [FourCC('n04Y')] = {
            { order = "curse", chance = 5, type = "target" },
            { order = "faeriefire", chance = 6, type = "target" },
        },
        [FourCC('n04X')] = {
            { order = "carrionswarm", chance = 4, type = "point" },
            { order = "rainoffire", chance = 4, type = "point" },
            { order = "cannibalize", chance = 5, type = "immediate", hp = 50 },
        },
        [FourCC('n04V')] = {
            { order = "windwalk", chance = 4, type = "immediate" },
            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },
        },
        [FourCC('h0JA')] = {
            { order = "animatedead", chance = 4, type = "point" },
            { order = "raisedead", chance = 4, type = "point" },
            { order = "resurrection", chance = 5, type = "immediate" },
        },
        [FourCC('o02X')] = {
            { order = "channel", chance = 4, type = "self" },
        },
        [FourCC('u02C')] = {
            { order = "cannibalize", chance = 4, type = "immediate", hp = 50 },
        },
    },
    join = Join_Forsaken,
    wall = FourCC('h0JM'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Alliance(id, pi, u)
    if id == FourCC('hpea') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Alliance", {
    tokens = {"alliance", "ally"},
    weight = 1,
    altar = FourCC('halt'),
    start = startAlliance,
    buildings = {
        seed = FourCC('hhou'),
        { FourCC('htow'), 4, 4 }, { FourCC('hhou'), 18, 4 },
        { FourCC('hbar'), 10, 4 }, { FourCC('halt'), 3, 6 },
        { FourCC('harm'), 5, 2 }, { FourCC('hbla'), 8, 6, gate = "tier2" },
        { FourCC('hars'), 8, 6, gate = "tier2" },
        { FourCC('hwtw'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('hkee')) + getAiCount(pi, FourCC('hcas')) >= 1 end,
    },
    production = {
        [FourCC('htow')] = { {FourCC('hpea'),3,limit=18} },
        [FourCC('hkee')] = { {FourCC('hpea'),3,limit=18} },
        [FourCC('hcas')] = { {FourCC('hpea'),3,limit=18} },
        [FourCC('hbar')] = {
            {FourCC('hfoo'), 4}, {FourCC('hkni'), 3},
        },
        [FourCC('hbla')] = {
            {FourCC('hrif'), 3}, {FourCC('hmtm'), 2},
        },
        [FourCC('hars')] = {
            {FourCC('hsor'), 3}, {FourCC('hmpr'), 3},
        },
        [FourCC('halt')] = {
            {FourCC('Hpal'), 1, limit = 1}, {FourCC('Hamg'), 1, limit = 1}, {FourCC('Hmkg'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('hhou')] = 1, [FourCC('htow')] = 2,
        [FourCC('hkee')] = 5, [FourCC('hcas')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('harm'),FourCC('Abds'),6},{FourCC('harm'),FourCC('Arlm'),6} },
                { {FourCC('hbar'),FourCC('Abds'),6} },
                { {FourCC('hbla'),FourCC('Abds'),6},{FourCC('hars'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('htow'), to = FourCC('hkee'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('hkee'), to = FourCC('hcas'), cap = 3 },
        },
    },
    join = Join_Alliance,
    wall = FourCC('hgtw'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Bandits(id, pi, u)
    if id == FourCC('h002') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Bandits", {
    tokens = {"bandit", "bandits"},
    weight = 1,
    altar = FourCC('h051'),
    start = startBandits,
    buildings = {
        seed = FourCC('h00A'),
        { FourCC('h007'), 4, 4 }, { FourCC('h00A'), 18, 4 },
        { FourCC('h051'), 3, 6 }, { FourCC('h00B'), 10, 4 },
        { FourCC('h01W'), 8, 4 }, { FourCC('h00O'), 8, 6, gate = "tier2" },
        { FourCC('h03O'), 5, 2 }, { FourCC('h03P'), 5, 2 },
        { FourCC('h03Q'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h008')) + getAiCount(pi, FourCC('h009')) >= 1 end,
    },
    production = {
        [FourCC('h007')] = { {FourCC('h002'),3,limit=18} },
        [FourCC('h008')] = { {FourCC('h002'),3,limit=18} },
        [FourCC('h009')] = { {FourCC('h002'),3,limit=18} },
        [FourCC('h00B')] = {
            {FourCC('h003'), 4}, {FourCC('h005'), 3}, {FourCC('h006'), 2},
            {FourCC('n000'), 4}, {FourCC('n002'), 3}, {FourCC('n004'), 2},
        },
        [FourCC('h01W')] = {
            {FourCC('h02Q'), 3}, {FourCC('h02R'), 2}, {FourCC('h02S'), 2},
        },
        [FourCC('h00O')] = {
            {FourCC('h00P'), 3}, {FourCC('h00S'), 2}, {FourCC('h00U'), 1},
            {FourCC('h029'), 3}, {FourCC('h02A'), 2}, {FourCC('h02B'), 1},
        },
        [FourCC('h051')] = {
            {FourCC('H03S'), 1, limit = 1}, {FourCC('H047'), 1, limit = 1}, {FourCC('H048'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h00A')] = 1, [FourCC('h007')] = 2,
        [FourCC('h008')] = 5, [FourCC('h009')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h03O'),FourCC('Abds'),6},{FourCC('h03P'),FourCC('Arlm'),6} },
                { {FourCC('h00B'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h007'), to = FourCC('h008'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h008'), to = FourCC('h009'), cap = 3 },
        },
    },
    join = Join_Bandits,
    wall = FourCC('h03Q'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Undead(id, pi, u)
    if id == FourCC('u00P') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Undead", {
    tokens = {"undead", "scourge"},
    weight = 1,
    altar = FourCC('u00K'),
    start = startUndead,
    buildings = {
        seed = FourCC('u00H'),
        { FourCC('n014'), 4, 4 }, { FourCC('u00H'), 18, 4 },
        { FourCC('u00K'), 3, 6 }, { FourCC('u00M'), 10, 4 },
        { FourCC('u00N'), 8, 6, gate = "tier2" }, { FourCC('u00L'), 5, 2 },
        { FourCC('n012'), 8, 4 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('u00F')) + getAiCount(pi, FourCC('u00G')) >= 1 end,
    },
    production = {
        [FourCC('n014')] = { {FourCC('u00P'),3,limit=18} },
        [FourCC('u00F')] = { {FourCC('u00P'),3,limit=18} },
        [FourCC('u00G')] = { {FourCC('u00P'),3,limit=18} },
        [FourCC('u00M')] = {
            {FourCC('u00A'), 4}, {FourCC('u00B'), 3}, {FourCC('u00D'), 2},
        },
        [FourCC('u00N')] = {
            {FourCC('u00C'), 3}, {FourCC('u008'), 3}, {FourCC('u00E'), 2},
        },
        [FourCC('u00K')] = {
            {FourCC('U00O'), 1, limit = 1}, {FourCC('U00V'), 1, limit = 1}, {FourCC('U00U'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('u00H')] = 1, [FourCC('n014')] = 2,
        [FourCC('u00F')] = 5, [FourCC('u00G')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('u00L'),FourCC('Abds'),6},{FourCC('u00L'),FourCC('Arlm'),6} },
                { {FourCC('u00M'),FourCC('Abds'),6} },
                { {FourCC('u00N'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('n014'), to = FourCC('u00F'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('u00F'), to = FourCC('u00G'), cap = 3 },
        },
    },
    join = Join_Undead,
    wall = FourCC('u00I'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Demons(id, pi, u)
    if id == FourCC('e02Y') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Demons", {
    tokens = {"demon", "demons", "legion"},
    weight = 1,
    altar = FourCC('h0DX'),
    start = startDemons,
    buildings = {
        seed = FourCC('h0DS'),
        { FourCC('h0DU'), 4, 4 }, { FourCC('h0DS'), 18, 4 },
        { FourCC('h0DT'), 8, 4 }, { FourCC('h0DX'), 3, 6 },
        { FourCC('h0DY'), 10, 4 }, { FourCC('h0E1'), 8, 6, gate = "tier2" },
        { FourCC('h0E0'), 8, 6, gate = "tier2" },
        { FourCC('h0DZ'), 5, 2 }, { FourCC('n02C'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h0DV')) + getAiCount(pi, FourCC('h0DW')) >= 1 end,
    },
    production = {
        [FourCC('h0DU')] = { {FourCC('e02Y'),3,limit=20} },
        [FourCC('h0DV')] = { {FourCC('e02Y'),3,limit=20} },
        [FourCC('h0DW')] = { {FourCC('e02Y'),3,limit=20} },
        [FourCC('h0DY')] = {
            {FourCC('n025'), 4}, {FourCC('n023'), 4}, {FourCC('n026'), 3},
            {FourCC('n027'), 3}, {FourCC('n02D'), 2}, {FourCC('n02E'), 2},
        },
        [FourCC('h0E1')] = {
            {FourCC('n024'), 3}, {FourCC('n022'), 2}, {FourCC('n021'), 2},
        },
        [FourCC('h0E0')] = {
            {FourCC('n020'), 3}, {FourCC('n028'), 2},
        },
        [FourCC('h0DX')] = {
            {FourCC('N02F'), 1, limit = 1}, {FourCC('N02A'), 1, limit = 1}, {FourCC('U028'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0DS')] = 1, [FourCC('h0DU')] = 2,
        [FourCC('h0DV')] = 5, [FourCC('h0DW')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0DZ'),FourCC('Abds'),6},{FourCC('h0DZ'),FourCC('Arlm'),6} },
                { {FourCC('h0DY'),FourCC('Abds'),6} },
                { {FourCC('h0E0'),FourCC('Abds'),6},{FourCC('h0E1'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0DU'), to = FourCC('h0DV'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0DV'), to = FourCC('h0DW'), cap = 3 },
        },
    },
    join = Join_Demons,
    wall = FourCC('n02C'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Draenei(id, pi, u)
    if id == FourCC('h012') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Draenei", {
    tokens = {"draenei", "draeneis"},
    weight = 1,
    altar = FourCC('h057'),
    start = startDraenei,
    buildings = {
        seed = FourCC('h05C'),
        { FourCC('h015'), 4, 4 }, { FourCC('h05C'), 18, 4 },
        { FourCC('h057'), 3, 6 }, { FourCC('h033'), 10, 4 },
        { FourCC('h058'), 8, 6, gate = "tier2" }, { FourCC('h056'), 8, 6, gate = "tier2" },
        { FourCC('h055'), 5, 2 }, { FourCC('h05A'), 8, 4 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h016')) + getAiCount(pi, FourCC('h017')) >= 1 end,
    },
    production = {
        [FourCC('h015')] = { {FourCC('h012'),3,limit=18} },
        [FourCC('h016')] = { {FourCC('h012'),3,limit=18} },
        [FourCC('h017')] = { {FourCC('h012'),3,limit=18} },
        [FourCC('h033')] = {
            {FourCC('h01S'), 3}, {FourCC('h01P'), 3}, {FourCC('e000'), 4},
        },
        [FourCC('h058')] = {
            {FourCC('h01O'), 2}, {FourCC('h01R'), 3}, {FourCC('h059'), 3}, {FourCC('h01T'), 2},
        },
        [FourCC('h056')] = {
            {FourCC('h01U'), 3}, {FourCC('h01Q'), 3},
        },
        [FourCC('h05A')] = {
            {FourCC('n005'), 4}, {FourCC('h05E'), 2}, {FourCC('h05D'), 2},
        },
        [FourCC('h057')] = {
            {FourCC('H05K'), 1, limit = 1}, {FourCC('H05L'), 1, limit = 1}, {FourCC('H05M'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h05C')] = 1, [FourCC('h015')] = 2,
        [FourCC('h016')] = 5, [FourCC('h017')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h055'),FourCC('Abds'),6},{FourCC('h055'),FourCC('Arlm'),6} },
                { {FourCC('h033'),FourCC('Abds'),6} },
                { {FourCC('h056'),FourCC('Abds'),6},{FourCC('h058'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h015'), to = FourCC('h016'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h016'), to = FourCC('h017'), cap = 3 },
        },
    },
    join = Join_Draenei,
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Stromgard(id, pi, u)
    if id == FourCC('h0G9') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Stromgard", {
    tokens = {"stromgard", "stromgarde"},
    weight = 1,
    altar = FourCC('h0H3'),
    start = startStromgard,
    buildings = {
        seed = FourCC('h0H2'),
        { FourCC('h0GZ'), 4, 4 }, { FourCC('h0H2'), 18, 4 },
        { FourCC('h0H3'), 3, 6 }, { FourCC('h0H4'), 10, 4 },
        { FourCC('h0HI'), 8, 6, gate = "tier2" }, { FourCC('h0HF'), 8, 6, gate = "tier2" },
        { FourCC('h0H5'), 5, 2 }, { FourCC('h0H6'), 5, 2 },
        { FourCC('h0HG'), 4, 2 }, { FourCC('h0HU'), 6, 4 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h0H0')) + getAiCount(pi, FourCC('h0H1')) >= 1 end,
    },
    production = {
        [FourCC('h0GZ')] = { {FourCC('h0G9'),3,limit=18} },
        [FourCC('h0H0')] = { {FourCC('h0G9'),3,limit=18} },
        [FourCC('h0H1')] = { {FourCC('h0G9'),3,limit=18} },
        [FourCC('h0H4')] = {
            {FourCC('h0F4'), 3}, {FourCC('h0GT'), 3}, {FourCC('h0GU'), 2},
            {FourCC('h0GS'), 2}, {FourCC('h0GV'), 2},
        },
        [FourCC('h0HI')] = {
            {FourCC('h0GX'), 3}, {FourCC('h0GW'), 3},
        },
        [FourCC('h0HF')] = {
            {FourCC('h0L3'), 3}, {FourCC('h0GY'), 2},
        },
        [FourCC('h0HU')] = {
            {FourCC('h0HD'), 2},
        },
        [FourCC('h0H3')] = {
            {FourCC('H0HB'), 1, limit = 1}, {FourCC('H0HL'), 1, limit = 1}, {FourCC('H0HA'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0H2')] = 1, [FourCC('h0GZ')] = 2,
        [FourCC('h0H0')] = 5, [FourCC('h0H1')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0H6'),FourCC('Abds'),6},{FourCC('h0H5'),FourCC('Arlm'),6} },
                { {FourCC('h0H4'),FourCC('Abds'),6} },
                { {FourCC('h0HF'),FourCC('Abds'),6},{FourCC('h0HI'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0GZ'), to = FourCC('h0H0'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0H0'), to = FourCC('h0H1'), cap = 3 },
        },
    },
    join = Join_Stromgard,
    wall = FourCC('h0HG'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Illidari(id, pi, u)
    if id == FourCC('h0EI') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Illidari", {
    tokens = {"illidari", "illidan"},
    weight = 1,
    altar = FourCC('h0ED'),
    start = startIllidari,
    buildings = {
        seed = FourCC('h0EC'),
        { FourCC('h0E9'), 4, 4 }, { FourCC('h0EC'), 18, 4 },
        { FourCC('h0ED'), 3, 6 }, { FourCC('h0EE'), 10, 4 },
        { FourCC('h0EF'), 8, 6, gate = "tier2" }, { FourCC('h0EG'), 8, 6, gate = "tier2" },
        { FourCC('o01C'), 8, 4 }, { FourCC('h0EH'), 5, 2 },
        { FourCC('h0EM'), 5, 2 }, { FourCC('h0EN'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h0EA')) + getAiCount(pi, FourCC('h0EB')) >= 1 end,
    },
    production = {
        [FourCC('h0E9')] = { {FourCC('h0EI'),3,limit=18} },
        [FourCC('h0EA')] = { {FourCC('h0EI'),3,limit=18} },
        [FourCC('h0EB')] = { {FourCC('h0EI'),3,limit=18} },
        [FourCC('h0EE')] = {
            {FourCC('h0EJ'), 3}, {FourCC('o01A'), 3}, {FourCC('o01B'), 2}, {FourCC('o019'), 2},
        },
        [FourCC('h0EF')] = {
            {FourCC('h0EK'), 3}, {FourCC('h0EL'), 3},
        },
        [FourCC('h0EG')] = {
            {FourCC('n02O'), 4}, {FourCC('n02M'), 3}, {FourCC('n02N'), 2},
        },
        [FourCC('o01C')] = {
            {FourCC('h04Y'), 3}, {FourCC('h04Z'), 3}, {FourCC('h050'), 2},
        },
        [FourCC('h0ED')] = {
            {FourCC('H043'), 1, limit = 1}, {FourCC('E01W'), 1, limit = 1}, {FourCC('E025'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0EC')] = 1, [FourCC('h0E9')] = 2,
        [FourCC('h0EA')] = 5, [FourCC('h0EB')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0EM'),FourCC('Abds'),6},{FourCC('h0EH'),FourCC('Arlm'),6} },
                { {FourCC('h0EE'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0E9'), to = FourCC('h0EA'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('h0EA'), to = FourCC('h0EB'), cap = 3 },
        },
    },
    join = Join_Illidari,
    wall = FourCC('h0EN'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Worgen(id, pi, u)
    if id == FourCC('h0IT') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Worgen", {
    tokens = {"worgen", "gilneas"},
    weight = 1,
    altar = FourCC('h0IN'),
    start = startWorgen,
    buildings = {
        seed = FourCC('h0IM'),
        { FourCC('h0IK'), 4, 4 }, { FourCC('h0IM'), 18, 4 },
        { FourCC('h0IN'), 3, 6 }, { FourCC('h0IO'), 10, 4 },
        { FourCC('h0IR'), 8, 6, gate = "tier2" }, { FourCC('h0IS'), 8, 6, gate = "tier2" },
        { FourCC('h0IQ'), 5, 2 }, { FourCC('h0JT'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('h0IL')) >= 1 end,
    },
    production = {
        [FourCC('h0IK')] = { {FourCC('h0IT'),3,limit=18} },
        [FourCC('h0IL')] = { {FourCC('h0IT'),3,limit=18} },
        [FourCC('h0IO')] = {
            {FourCC('h0IU'), 3}, {FourCC('h0IV'), 3}, {FourCC('o02T'), 2},
        },
        [FourCC('h0IR')] = {
            {FourCC('h0NA'), 2}, {FourCC('h0IW'), 3}, {FourCC('h0J0'), 2},
        },
        [FourCC('h0IS')] = {
            {FourCC('h0J1'), 3}, {FourCC('h0IX'), 2},
        },
        [FourCC('h0IN')] = {
            {FourCC('H0J2'), 1, limit = 1}, {FourCC('H0J6'), 1, limit = 1}, {FourCC('H0J7'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('h0IM')] = 1, [FourCC('h0IK')] = 2,
        [FourCC('h0IL')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('h0IQ'),FourCC('Abds'),6} },
                { {FourCC('h0IO'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('h0IK'), to = FourCC('h0IL'), cap = 3 },
        },
    },
    join = Join_Worgen,
    wall = FourCC('h0JT'),
})

---@param id integer
---@param pi integer
---@param u unit
function Join_Ogres(id, pi, u)
    if id == FourCC('o03W') then
        GroupAddUnit(udg_Ai_builders[pi], u)
    elseif aiUnitJoinsCapitalGuard(u, pi) then
    else
        aiUnitJoinsArmy(u, pi)
    end
end

RegisterAiRace("Ogres", {
    tokens = {"ogre", "ogres"},
    weight = 1,
    altar = FourCC('o037'),
    start = startOgres,
    buildings = {
        seed = FourCC('o036'),
        { FourCC('o035'), 4, 4 }, { FourCC('o036'), 18, 4 },
        { FourCC('o037'), 3, 6 }, { FourCC('o03A'), 10, 4 },
        { FourCC('o039'), 8, 4 }, { FourCC('o03J'), 8, 6, gate = "tier2" },
        { FourCC('o03C'), 8, 6, gate = "tier2" }, { FourCC('o03B'), 5, 2 },
        { FourCC('o038'), 4, 2 },
    },
    gates = {
        tier2 = function(pi) return getAiCount(pi, FourCC('o03D')) + getAiCount(pi, FourCC('o03E')) >= 1 end,
    },
    production = {
        [FourCC('o035')] = { {FourCC('o03W'),3,limit=18} },
        [FourCC('o03D')] = { {FourCC('o03W'),3,limit=18} },
        [FourCC('o03E')] = { {FourCC('o03W'),3,limit=18} },
        [FourCC('o03A')] = {
            {FourCC('o03I'), 3}, {FourCC('o03H'), 3}, {FourCC('o03G'), 2}, {FourCC('o03F'), 2},
        },
        [FourCC('o039')] = {
            {FourCC('o03L'), 3}, {FourCC('o03M'), 2}, {FourCC('o03K'), 2},
        },
        [FourCC('o03J')] = {
            {FourCC('o03P'), 3}, {FourCC('o03N'), 2}, {FourCC('o03O'), 2},
        },
        [FourCC('o03C')] = {
            {FourCC('o03U'), 3}, {FourCC('o03T'), 3}, {FourCC('o03V'), 2},
            {FourCC('o03Q'), 2}, {FourCC('o03R'), 2}, {FourCC('o03S'), 2},
        },
        [FourCC('o037')] = {
            {FourCC('N05L'), 1, limit = 1}, {FourCC('N05K'), 1, limit = 1}, {FourCC('N05J'), 1, limit = 1},
        },
    },
    ecoWeights = {
        [FourCC('o036')] = 1, [FourCC('o035')] = 2,
        [FourCC('o03D')] = 5, [FourCC('o03E')] = 8,
    },
    strategData = {
        gradeCap = 100,
        steps = {
            { at = 17, action = "random", branches = {
                { {FourCC('o03B'),FourCC('Abds'),6},{FourCC('o03B'),FourCC('Arlm'),6} },
                { {FourCC('o03A'),FourCC('Abds'),6} },
            }},
            { at = 20, action = "tryBuy" },
            { at = 25, action = "techUp", from = FourCC('o035'), to = FourCC('o03D'), cap = 3 },
            { at = 55, action = "techUp", from = FourCC('o03D'), to = FourCC('o03E'), cap = 3 },
        },
    },
    join = Join_Ogres,
    wall = FourCC('o038'),
})
