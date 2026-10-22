-- ====================================================================
-- AI Diplomat Module: bot-to-bot alliances, resource exchange, betrayal.
-- Personality-driven, configurable per-race via def.diplomat.
-- Tag: BRAINDIP (toggle: -log on:BRAINDIP)
-- ====================================================================

AiDiplomat = AiDiplomat or {}              -- [pi] = runtime state
AiDiplomatTicks = AiDiplomatTicks or {}    -- [pi] = internal tick counter
AiDiplomatProposalTime = AiDiplomatProposalTime or {} -- [pi] = { [other_pi]=time }
AiDiplomatProposalTimeout = AiDiplomatProposalTimeout or 30

-- ====================================================================
-- Personality presets: each is a table of parameter overrides.
-- A race can pick a preset via def.diplomat = "pragmatic", or
-- override individual fields via def.diplomat = { preset="pragmatic",
-- loyalty=0.95, ... }.
-- ====================================================================
AiDiplomatPresets = {
    -- Warm, loyal, generous, actively seeks allies.
    diplomat = {
        allianceDesire    = 0.9,  breakOnWeakness    = 0.15,
        allianceMax       = 3,    breakOnNoThreat    = 0.15,
        loyalty           = 0.9,  breakChanceBase    = 0.0,
        allyAgainstThreat = 0.9,  allyWithStronger   = 0.4,
        tradeGoldFraction = 0.30, tradeLumberFraction = 0.30,
        tradeFrequency    = 30,   helpWeakAllies     = 0.9,
        selfishness       = 0.2,  betrayalChance     = 0.0,
        threatWeight      = 0.8,  powerWeight        = 0.5,
        proximityWeight   = 0.5,  resourceWeight     = 0.6,
    },
    -- Calculated, allies only under pressure, restrained trades.
    pragmatic = {
        allianceDesire    = 0.4,  breakOnWeakness    = 0.45,
        allianceMax       = 2,    breakOnNoThreat    = 0.50,
        loyalty           = 0.6,  breakChanceBase    = 0.05,
        allyAgainstThreat = 0.8,  allyWithStronger   = 0.3,
        tradeGoldFraction = 0.15, tradeLumberFraction = 0.15,
        tradeFrequency    = 50,   helpWeakAllies     = 0.5,
        selfishness       = 0.5,  betrayalChance     = 0.05,
        threatWeight      = 1.2,  powerWeight        = 0.8,
        proximityWeight   = 0.5,  resourceWeight     = 0.4,
    },
    -- Opportunistic: allies easily, breaks easily, can betray.
    traitor = {
        allianceDesire    = 0.7,  breakOnWeakness    = 0.60,
        allianceMax       = 2,    breakOnNoThreat    = 0.70,
        loyalty           = 0.2,  breakChanceBase    = 0.15,
        allyAgainstThreat = 0.4,  allyWithStronger   = 0.8,
        tradeGoldFraction = 0.10, tradeLumberFraction = 0.05,
        tradeFrequency    = 70,   helpWeakAllies     = 0.2,
        selfishness       = 0.8,  betrayalChance     = 0.30,
        threatWeight      = 0.5,  powerWeight        = 1.2,
        proximityWeight   = 0.7,  resourceWeight     = 0.3,
        betrayAttackDelay = 120,  betrayTimeMin      = 90,
    },
    -- Avoids alliances completely, never trades.
    isolationist = {
        allianceDesire    = 0.0,  breakOnWeakness    = 0.90,
        allianceMax       = 0,    breakOnNoThreat    = 0.90,
        loyalty           = 0.0,  breakChanceBase    = 0.90,
        allyAgainstThreat = 0.0,  allyWithStronger   = 0.0,
        tradeGoldFraction = 0.0,  tradeLumberFraction = 0.0,
        tradeFrequency    = 9999, helpWeakAllies     = 0.0,
        selfishness       = 1.0,  betrayalChance     = 0.0,
        threatWeight      = 1.5,  powerWeight        = 1.0,
        proximityWeight   = 0.8,  resourceWeight     = 0.0,
    },
    -- Reliable ally, rarely breaks, helps the weak, never betrays.
    loyal = {
        allianceDesire    = 0.6,  breakOnWeakness    = 0.10,
        allianceMax       = 2,    breakOnNoThreat    = 0.10,
        loyalty           = 0.95, breakChanceBase    = 0.0,
        allyAgainstThreat = 0.9,  allyWithStronger   = 0.2,
        tradeGoldFraction = 0.25, tradeLumberFraction = 0.25,
        tradeFrequency    = 35,   helpWeakAllies     = 0.8,
        selfishness       = 0.3,  betrayalChance     = 0.0,
        threatWeight      = 0.9,  powerWeight        = 0.6,
        proximityWeight   = 0.5,  resourceWeight     = 0.5,
    },
    -- Default: balanced mix, no extremes.
    balanced = {
        allianceDesire    = 0.5,  breakOnWeakness    = 0.40,
        allianceMax       = 2,    breakOnNoThreat    = 0.35,
        loyalty           = 0.7,  breakChanceBase    = 0.05,
        allyAgainstThreat = 0.7,  allyWithStronger   = 0.35,
        tradeGoldFraction = 0.20, tradeLumberFraction = 0.15,
        tradeFrequency    = 45,   helpWeakAllies     = 0.6,
        selfishness       = 0.5,  betrayalChance     = 0.03,
        threatWeight      = 1.0,  powerWeight        = 0.7,
        proximityWeight   = 0.5,  resourceWeight     = 0.4,
    },
}

-- Diplomacy module disabled entirely (user request): bot-to-bot alliances,
-- resource exchange and chat RP are off. NOTE: `or true` re-enabled this even
-- after 83_ai_brain set it false (load order 83<84, false or true == true), so
-- it is now hard-set to false here, the last word on the flag.
AiDiplomatEnabled = false
AiDiplomatRpEnabled = false

-- Churn dampening (anti "ally then immediately drop"): a freshly-formed alliance
-- is protected from weakness/no-threat breaks for MinAllyAge ticks, and after a
-- break the pair can't re-ally for ReallyCooldown ticks. Betrayal is exempt.
AiDiplomatMinAllyAge = AiDiplomatMinAllyAge or 40
AiDiplomatReallyCooldown = AiDiplomatReallyCooldown or 60

-- ====================================================================
-- Display name helper: bot player names already include their slot number.
-- ====================================================================
---@param pi integer
---@return string
function DiplomatName(pi)
    local playerName = GetPlayerName(Player(pi)) or "Неизвестный игрок"
    return "|cffebc56c[" .. playerName .. "]|r"
end

-- ====================================================================
-- Broadcast: send a message to all players (humans + bots).
-- ====================================================================
---@param msg string
function DipBroadcast(msg)
    for i = 0, 23 do
        local p = Player(i)
        if p ~= nil then
            DisplayTimedTextToPlayer(p, 0, 0, 10.0, msg)
        end
    end
end

-- ====================================================================
-- RP broadcast: "[RaceName (Slot#)] says: message"
-- ====================================================================
---@param pi integer
---@param msg string
function DipRpBroadcast(pi, msg)
    local full = DiplomatName(pi) .. "|cffced4da: «" .. msg .. "»|r"
    DipBroadcast(full)
    DipLog(pi, "[RP] " .. msg)
end

-- ====================================================================
-- Resolve diplomat config for a bot. Returns nil if the race has no
-- diplomat config (opt-in: only races with def.diplomat are diplomats).
-- Otherwise returns a plain table with all keys filled.
-- ====================================================================
---@param pi integer
---@return table|nil
function AiDiplomatCfg(pi)
    local race = AiRaceOf(pi)
    if race == nil or race.diplomat == nil then
        return nil -- race didn't opt in
    end
    local cfg = {
        allianceDesire=0.5, allianceMax=2, loyalty=0.7,
        breakOnWeakness=0.4, breakOnNoThreat=0.35, breakChanceBase=0.05,
        allyAgainstThreat=0.7, allyWithStronger=0.35,
        tradeGoldFraction=0.2, tradeLumberFraction=0.15,
        tradeFrequency=45, helpWeakAllies=0.6, selfishness=0.5,
        betrayalChance=0.0, betrayAttackDelay=180, betrayTimeMin=120,
        threatWeight=1.0, powerWeight=0.7, proximityWeight=0.5, resourceWeight=0.4,
    }
    local raw = race.diplomat
    -- If raw is a string, resolve preset by name.
    if type(raw) == "string" then
        local pre = AiDiplomatPresets[raw]
        if pre ~= nil then
            for k, v in pairs(pre) do cfg[k] = v end
        end
    -- If raw is a table: apply preset first, then overrides.
    elseif type(raw) == "table" then
        if raw.preset ~= nil then
            local pre = AiDiplomatPresets[raw.preset]
            if pre ~= nil then
                for k, v in pairs(pre) do cfg[k] = v end
            end
        end
        for k, v in pairs(raw) do
            if k ~= "preset" then cfg[k] = v end
        end
    end
    -- Respect the map's global alliance cap (DipMode). If a bot is allowed more
    -- allies than DipMode, the StartAlly trigger force-clears it the moment it
    -- exceeds — which both looks like alliance churn ("ally then instantly drop")
    -- and drives the ClearAllies cascade. DipMode==0 means "no cap".
    if DipMode ~= nil and DipMode > 0 and cfg.allianceMax > DipMode then
        cfg.allianceMax = DipMode
    end
    return cfg
end

-- ====================================================================
-- Runtime state initialisation / retrieval.
-- ====================================================================
---@param pi integer
---@return table
function AiDiplomatState(pi)
    local st = AiDiplomat[pi]
    if st == nil then
        st = {
            allies = {},            -- [other_pi] = true
            relations = {},         -- [other_pi] = { trust, threat, ... }
            pendingOffers = {},     -- [other_pi] = offer time
            pendingRequests = {},   -- [other_pi] = request time
            lastTrade = {},         -- [other_pi] = last trade tick
            lastEval = 0,           -- last evaluation tick
            betrayTargets = {},     -- [other_pi] = tick when to betray
            chatMsgCount = 0,       -- throttle chat messages
        }
        AiDiplomat[pi] = st
    end
    return st
end

-- ====================================================================
-- Logging helper: logs to probe-log, visible only when BRAINDIP tag is
-- enabled. Throttled per (pi, key) every N calls to avoid spam.
-- ====================================================================
---@param pi integer
---@param msg string
function DipLog(pi, msg)
    ProbeLogWrite("[BRAINDIP] pi=" .. tostring(pi) .. " " .. msg)
end

---@param pi integer
---@param key string
---@param n integer
---@param msg string
function DipLogEvery(pi, key, n, msg)
    local st = AiDiplomatState(pi)
    local kk = "dipogn_" .. key
    local c = (st[kk] or 0) + 1
    st[kk] = c
    if c % n == 0 then
        DipLog(pi, msg)
    end
end

-- ====================================================================
-- Chat: send a message to a player as if from this bot.
-- ====================================================================
---@param pi integer
---@param targetPi integer
---@param msg string
function DipChat(pi, targetPi, msg)
    local full = DiplomatName(pi) .. "|cffced4da " .. msg .. "|r"
    DisplayTimedTextToPlayer(Player(targetPi), 0, 0, 10.0, full)
    DipLog(pi, "chat to " .. tostring(targetPi) .. ": " .. msg)
end

-- ====================================================================
-- RP message tables: per-personality flavour quotes for each event.
-- Picks a random entry from the appropriate table.
-- Format: AiDiplomatRpMessages[personality][event] = { "msg1", ... }
-- Events: allyPropose, allyAccept, allyBreak, trade, idle, underAttack
-- ====================================================================
AiDiplomatRpMessages = {
    diplomat = {
        allyPropose = {
            "Вместе мы будем процветать.",
            "Нас ждёт плодотворное сотрудничество.",
            "Давайте строить мосты, а не стены.",
            "Этот союз принесёт пользу нам обоим.",
        },
        allyAccept = {
            "Начинается новая глава нашей дружбы!",
            "Вместе нас ничто не остановит.",
            "О нашей общей силе будут слагать легенды.",
            "Приветствую тебя, верный друг.",
        },
        allyBreak  = {
            "Возможно, в другой раз и в другом месте.",
            "Здесь наши пути расходятся.",
            "Наши цели больше не совпадают.",
            "Прощай, старый друг. Надеюсь, мы встретимся с миром.",
        },
        trade = {
            "Подарок от друга. Без всяких условий.",
            "Ради твоего процветания — и нашего.",
            "Поделимся по-братски!",
        },
        idle = {
            "Торговые караваны сообщают, что всё спокойно.",
            "Рынки стабильны. Хороший знак.",
            "Дипломатия — величайшее оружие.",
        },
        underAttack = {
            "Мы в осаде! Дорогие союзники, нам нужна помощь!",
            "Враг у наших ворот! Будем рады любой помощи!",
        },
    },
    pragmatic = {
        allyPropose = {
            "Наши интересы совпадают. Пора действовать.",
            "Враг моего врага... продолжение ты знаешь.",
            "Временный союз. Не более того.",
        },
        allyAccept = {
            "Стратегическое решение. Не заставляй меня пожалеть о нём.",
            "Хорошо. Пока мы на одной стороне.",
            "Этот союз выгоден нам обоим. Помни об этом.",
        },
        allyBreak  = {
            "Расчёты изменились. Наши пути расходятся.",
            "Обстоятельства больше не благоприятствуют нашему союзу.",
            "Наши приоритеты изменились. Прощай.",
        },
        trade = {
            "Стратегические ресурсы. Распорядись ими разумно.",
            "Продуманное вложение.",
            "Потрать с умом. Я жду результатов.",
        },
        idle = {
            "Соотношение сил... пока приемлемое.",
            "Наблюдаем. Ждём. Рассчитываем.",
            "Любой союз — это сделка.",
        },
        underAttack = {
            "Нас атакуют! Все, кто способен сражаться, к нам!",
            "Оборона подготовлена. Союзники, теперь ваш ход.",
        },
    },
    traitor = {
        allyPropose = {
            "Доверься мне... пока что.",
            "Назовём это союзом по расчёту?",
            "У меня есть предложение, от которого ты не сможешь отказаться.",
        },
        allyAccept = {
            "А, новый... друг. Как приятно.",
            "Да-да. Вместе мы всех покорим!",
            "Твоё доверие принято. Я воспользуюсь им... разумно.",
        },
        allyBreak  = {
            "Ты и вправду считал нас друзьями?",
            "Ты больше... не нужен.",
            "Нож в спину — тоже оружие.",
            "Ничего личного. Только дело.",
        },
        trade = {
            "Бери. Расплатишься потом.",
            "Знак моей... признательности.",
        },
        idle = {
            "Сильные пожирают слабых. Так устроен мир.",
            "Возможности повсюду. Нужно лишь ими воспользоваться.",
            "Верность — это валюта. Трать щедро, копи с умом.",
        },
        underAttack = {
            "Глупцы! Они посмели напасть на нас!",
            "Они заплатят за эту дерзость!",
        },
    },
    isolationist = {
        allyPropose = {
            "Нам не нужны чужаки.",
            "Таким, как ты, здесь не рады.",
            "Не трать слова попусту.",
        },
        allyAccept = {
            "...Неожиданно, но приемлемо.",
            "Не переходи границы дозволенного.",
        },
        allyBreak  = {
            "Всё идёт как должно.",
            "Мы снова одни. Хорошо.",
        },
        trade = {
            "Не жди благодарности.",
            "Не рассчитывай на повторение.",
        },
        idle = {
            "Внешний мир не имеет значения.",
            "Наша сила — в уединении.",
        },
        underAttack = {
            "Чужаки! Защитим рой любой ценой!",
            "Вторжение на наши земли!",
        },
    },
    loyal = {
        allyPropose = {
            "Честь зовёт нас встать плечом к плечу.",
            "Союз, скреплённый доверием, нерушим.",
            "Пусть наша клятва будет вечной.",
        },
        allyAccept = {
            "Клянусь честью, теперь мы едины.",
            "Клянусь жизнью защищать наш союз.",
            "До конца времён мы будем вместе.",
        },
        allyBreak  = {
            "Тяжёлое решение, но необходимое.",
            "Ничто не вечно. Даже честь.",
            "Я освобождаю тебя от нашей клятвы.",
        },
        trade = {
            "Ради общего дела. Всегда.",
            "Мой меч и моё золото — всё ради нашего союза.",
        },
        idle = {
            "Бдительность и честь указывают нам путь.",
            "Истинная сила — в единстве.",
            "Мы помним каждый долг и каждое доброе дело.",
        },
        underAttack = {
            "К оружию, братья! Враг приближается!",
            "Наши священные земли под угрозой! Все на защиту!",
        },
    },
    balanced = {
        allyPropose = {
            "Будем охотиться вместе.",
            "Наша сила — в численности. Всегда.",
            "Союз может принести пользу нам обоим.",
        },
        allyAccept = {
            "Достойный союзник. Начнём.",
            "Вместе мы сильнее.",
            "Приветствую наш новый союз.",
        },
        allyBreak  = {
            "Пришла пора расстаться.",
            "Теперь мы идём своим путём.",
            "Наш союз больше не нужен.",
        },
        trade = {
            "Бери. Тебе нужнее.",
            "Справедливый обмен для верного союзника.",
        },
        idle = {
            "Сегодня в диких землях тихо.",
            "Костёр потрескивает. Всё спокойно.",
        },
        underAttack = {
            "Враги у ворот! Все воины, к обороне!",
            "Нас окружили! Будем рады любой помощи!",
        },
    },
}

-- ====================================================================
-- Pick and broadcast a random RP message for an event.
-- Throttled: max 1 RP message per bot per 3 diplomat ticks.
-- ====================================================================
---@param pi integer
---@param event string  "allyPropose"|"allyAccept"|"allyBreak"|"trade"|"idle"|"underAttack"
function AiDiplomatRpSay(pi, event)
    if not AiDiplomatRpEnabled then return end
    local cfg = AiDiplomatCfg(pi)
    if cfg == nil then return end
    local st = AiDiplomatState(pi)
    local tick = AiDiplomatTicks[pi] or 0
    if st.lastRpTick ~= nil and tick - st.lastRpTick < 3 then return end

    -- Resolve personality name for RP table lookup
    local race = AiRaceOf(pi)
    local persona = "balanced"
    if race ~= nil and race.diplomat ~= nil then
        if type(race.diplomat) == "string" then
            persona = race.diplomat
        elseif type(race.diplomat) == "table" and race.diplomat.preset ~= nil then
            persona = race.diplomat.preset
        elseif type(race.diplomat) == "table" then
            -- Inline table without preset field: determine personality from key parameters
            if cfg.loyalty > 0.9 then persona = "loyal"
            elseif cfg.betrayalChance > 0.15 then persona = "traitor"
            elseif cfg.allianceDesire > 0.7 then persona = "diplomat"
            elseif cfg.allianceMax == 0 then persona = "isolationist"
            end
        end
    end
    -- Race-specific RP messages override personality table
    local msgs = nil
    if race ~= nil and race.diplomatRp ~= nil and race.diplomatRp[event] ~= nil then
        msgs = race.diplomatRp[event]
    end
    if msgs == nil then
        local tbl = AiDiplomatRpMessages[persona]
        if tbl == nil then tbl = AiDiplomatRpMessages["balanced"] end
        msgs = tbl[event]
    end
    if msgs == nil or #msgs == 0 then return end

    local msg = msgs[GetRandomInt(1, #msgs)]
    DipRpBroadcast(pi, msg)
    st.lastRpTick = tick
end

-- ====================================================================
-- Perception: evaluate all other alive players and update relations.
-- Called periodically. Returns nothing, updates AiDiplomat[pi].relations.
-- ====================================================================
---@param pi integer
function AiDiplomatPerceive(pi)
    local st = AiDiplomatState(pi)
    local cfg = AiDiplomatCfg(pi)
    local me = Player(pi)
    if me == nil then return end

    local capX, capY = 0.0, 0.0
    local hasCap = false
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        capX, capY = GetUnitX(cap), GetUnitY(cap)
        hasCap = true
    elseif udg_Ai_army[pi] ~= nil and FirstOfGroup(udg_Ai_army[pi]) ~= nil then
        -- No capital yet: use army centroid as fallback anchor
        capX, capY, _ = AiGroupCentroid(udg_Ai_army[pi])
        hasCap = true
    end
    -- If no anchor at all (no capital + no army), still track relations
    -- but with proximity=0 for everyone.

    local myPower = Grades[pi] or 0
    if myPower < 1 then myPower = 1 end

    -- Under-attack detection: capital HP dropped significantly
    if hasCap then
        local capHP = GetUnitState(cap, UNIT_STATE_LIFE)
        local prevHP = st.lastCapitalHP
        st.lastCapitalHP = capHP
        if prevHP ~= nil and capHP > 0 and capHP < prevHP - 50 then
            st.underAttackFired = true
        end
    end

    for otherPi = 0, 23 do
        if otherPi ~= pi then
            local other = Player(otherPi)
            if other ~= nil then
                local otherCap = playerCapital[otherPi]
                if otherCap ~= nil and GetUnitState(otherCap, UNIT_STATE_LIFE) > 0.405 then
                    local otherPower = Grades[otherPi] or 0
                    local proximity = 0.0
                    local perceivedThreat = 0.0
                    if hasCap then
                        local ox, oy = GetUnitX(otherCap), GetUnitY(otherCap)
                        local dx, dy = capX - ox, capY - oy
                        local dist = SquareRoot(dx * dx + dy * dy)
                        local maxDist = 60000.0
                        proximity = 1.0 - math.min(dist / maxDist, 1.0)
                        -- Perceived threat: how dangerous they are to us (power * proximity)
                        perceivedThreat = (otherPower / math.max(myPower, 1)) * proximity
                        if IsPlayerEnemy(other, me) then
                            perceivedThreat = perceivedThreat * 1.5
                        end
                    end

                    -- Update or create relations entry
                    local rel = st.relations[otherPi]
                    if rel == nil then
                        rel = { trust=0.3, threat=0.0, proximity=0.0, sharedEnemies={} }
                        st.relations[otherPi] = rel
                    end
                    rel.threat = perceivedThreat
                    rel.proximity = proximity

                    -- Count shared enemies (players that are enemy to both)
                    local shared = 0
                    for thirdPi = 0, 23 do
                        if thirdPi ~= pi and thirdPi ~= otherPi then
                            local third = Player(thirdPi)
                            if third ~= nil and IsPlayerEnemy(me, third) and IsPlayerEnemy(other, third) then
                                shared = shared + 1
                            end
                        end
                    end
                    rel.sharedEnemies = shared
                else
                    -- Dead or no capital: remove relations
                    st.relations[otherPi] = nil
                    st.allies[otherPi] = nil
                end
            end
        end
    end
    st.lastEval = (st.lastEval or 0) + 1
end

-- ====================================================================
-- Evaluate relationship score toward another player (0..1).
-- Higher = more favourable for alliance / trade.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@return real
function AiDiplomatEvaluate(pi, otherPi)
    local st = AiDiplomatState(pi)
    local cfg = AiDiplomatCfg(pi)
    local rel = st.relations[otherPi]
    if rel == nil then return 0.0 end

    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return 0.0 end

    local isAlly = IsPlayerAlly(me, other)
    local isEnemy = IsPlayerEnemy(me, other)
    local myPower = Grades[pi] or 1
    local otherPower = Grades[otherPi] or 1
    local powerRatio = otherPower / math.max(myPower, 1)

    -- Base score components (each 0..1 approx)
    -- Shared enemies reduce mutual threat perception (FFA fix: when all are
    -- enemies, the ones who share foes are natural allies).
    local sharedThreatReduction = math.min(rel.sharedEnemies * 0.08, 0.7)
    local threatPenalty = math.min(1.0 - math.min(rel.threat * cfg.threatWeight, 1.0) + sharedThreatReduction, 1.0)
    local sharedEnemyBonus = math.min(rel.sharedEnemies * 0.2 * cfg.allyAgainstThreat, 1.0)
    local strongerBonus = math.min(powerRatio * cfg.allyWithStronger, 1.0) -- 1.0 only if they're stronger
    local proximityFactor = rel.proximity * cfg.proximityWeight

    -- Trust decays if they're an enemy
    local trust = rel.trust
    if isEnemy then
        trust = trust * 0.9
    end

    local score = (0.3 + sharedEnemyBonus + strongerBonus * 0.3 + trust * 0.3) * threatPenalty
    score = score * (0.5 + proximityFactor * 0.5)

    -- If already allied, score gets loyalty boost
    if isAlly then
        score = score + cfg.loyalty * 0.4
    end

    -- Cap
    if score > 1.0 then score = 1.0 end
    if score < 0.0 then score = 0.0 end
    return score
end

-- ====================================================================
-- Count current allies of this bot (excluding pending requests).
-- ====================================================================
---@param pi integer
---@return integer
function DipAllyCount(pi)
    local me = Player(pi)
    local count = 0
    for otherPi = 0, 23 do
        if otherPi ~= pi then
            local other = Player(otherPi)
            if other ~= nil and IsPlayerAlly(me, other) then
                count = count + 1
            end
        end
    end
    return count
end

-- ====================================================================
-- Proposal: offer alliance to another player (bot or human).
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@return boolean
function AiDiplomatPropose(pi, otherPi)
    local st = AiDiplomatState(pi)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return false end
    if IsPlayerAlly(me, other) then return false end

    -- One-way: set our ally state toward them (vision share).
    -- They need to reciprocate for full alliance.
    SetPlayerAllianceStateBJ(other, me, bj_ALLIANCE_ALLIED_VISION)
    -- Also share vision from us back, so they see our intent
    SetPlayerAllianceStateBJ(me, other, bj_ALLIANCE_ALLIED_VISION)

    st.pendingOffers[otherPi] = AiDiplomatTicks[pi] or 0
    DipLog(pi, "propose alliance to " .. tostring(otherPi) .. " (" .. GetPlayerName(other) .. ")")
    DipChat(pi, otherPi, "Предлагаю заключить союз.")
    AiDiplomatRpSay(pi, "allyPropose")
    return true
end

-- ====================================================================
-- Accept an alliance from another player. Makes it mutual with vision + unit sharing.
-- ====================================================================
---@param pi integer
---@param otherPi integer
function AiDiplomatAccept(pi, otherPi)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return end
    SetPlayerAllianceStateBJ(me, other, bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(other, me, bj_ALLIANCE_ALLIED_VISION)
    SetPlayerAllianceStateBJ(me, other, bj_ALLIANCE_ALLIED_UNITS)
    SetPlayerAllianceStateBJ(other, me, bj_ALLIANCE_ALLIED_UNITS)
    local st = AiDiplomatState(pi)
    st.allies[otherPi] = true
    st.pendingOffers[otherPi] = nil
    st.pendingRequests[otherPi] = nil
    if st.alliedAt == nil then st.alliedAt = {} end
    st.alliedAt[otherPi] = AiDiplomatTicks[pi] or 0
    if st.relations[otherPi] ~= nil then
        st.relations[otherPi].trust = math.min((st.relations[otherPi].trust or 0.3) + 0.3, 1.0)
    end
    DipLog(pi, "accepted alliance with " .. tostring(otherPi))
    DipChat(pi, otherPi, "Принимаю твоё предложение союза.")
    DipBroadcast(DiplomatName(pi) .. "|cffced4da и " .. DiplomatName(otherPi) .. "|cffc8e087 заключили союз!|r")
    AiDiplomatRpSay(pi, "allyAccept")
end

-- ====================================================================
-- Decline an alliance proposal.
-- ====================================================================
---@param pi integer
---@param otherPi integer
function AiDiplomatDecline(pi, otherPi)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return end
    SetPlayerAllianceStateBJ(other, me, bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(me, other, bj_ALLIANCE_UNALLIED)
    local st = AiDiplomatState(pi)
    st.pendingOffers[otherPi] = nil
    st.pendingRequests[otherPi] = nil
    DipLog(pi, "declined alliance with " .. tostring(otherPi))
end

-- ====================================================================
-- Break an existing alliance.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@param reason string
function AiDiplomatBreak(pi, otherPi, reason)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return end
    SetPlayerAllianceStateBJ(me, other, bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(other, me, bj_ALLIANCE_UNALLIED)
    local st = AiDiplomatState(pi)
    st.allies[otherPi] = nil
    st.pendingOffers[otherPi] = nil
    st.pendingRequests[otherPi] = nil
    if st.brokeAt == nil then st.brokeAt = {} end
    st.brokeAt[otherPi] = AiDiplomatTicks[pi] or 0
    if st.alliedAt ~= nil then st.alliedAt[otherPi] = nil end
    -- allow this pair to be re-detected as a fresh proposal later
    if st.processedProposals ~= nil then st.processedProposals[otherPi] = nil end
    if st.relations[otherPi] ~= nil then
        st.relations[otherPi].trust = math.max((st.relations[otherPi].trust or 0.5) - 0.5, 0.0)
    end
    DipLog(pi, "broke alliance with " .. tostring(otherPi) .. " reason=" .. (reason or "?"))
    if reason ~= nil and reason ~= "" then
        DipChat(pi, otherPi, reason)
    end
    DipBroadcast(DiplomatName(pi) .. "|cffef8173 разрывает союз с " .. DiplomatName(otherPi) .. "|cffced4da.|r")
    AiDiplomatRpSay(pi, "allyBreak")
end

-- ====================================================================
-- Resource transfer: send gold and/or lumber to another player.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@param gold integer
---@param lumber integer
---@param reason string|nil
function AiDiplomatTrade(pi, otherPi, gold, lumber, reason)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return end
    if gold <= 0 and lumber <= 0 then return end

    local myGold = GetPlayerState(me, PLAYER_STATE_RESOURCE_GOLD)
    local myLumber = GetPlayerState(me, PLAYER_STATE_RESOURCE_LUMBER)
    if gold > myGold then gold = myGold end
    if lumber > myLumber then lumber = myLumber end

    if gold > 0 then
        SetPlayerStateBJ(me, PLAYER_STATE_RESOURCE_GOLD, myGold - gold)
        SetPlayerStateBJ(other, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(other, PLAYER_STATE_RESOURCE_GOLD) + gold)
    end
    if lumber > 0 then
        SetPlayerStateBJ(me, PLAYER_STATE_RESOURCE_LUMBER, myLumber - lumber)
        SetPlayerStateBJ(other, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(other, PLAYER_STATE_RESOURCE_LUMBER) + lumber)
    end

    local st = AiDiplomatState(pi)
    st.lastTrade[otherPi] = (st.lastTrade[otherPi] or 0) + 1

    local reasonStr = reason or ""
    DipLog(pi, "traded to " .. tostring(otherPi) .. " gold=" .. tostring(gold) .. " lumber=" .. tostring(lumber) .. " " .. reasonStr)
    if reasonStr ~= "" then
        DipChat(pi, otherPi, "Sent " .. tostring(gold) .. "g " .. tostring(lumber) .. "w. " .. reasonStr)
    end
    AiDiplomatRpSay(pi, "trade")
end

-- ====================================================================
-- Decide whether to ally with another player.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@return boolean, string
function AiDiplomatConsiderAlly(pi, otherPi)
    local cfg = AiDiplomatCfg(pi)
    if cfg.allianceMax <= 0 then return false, nil end
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return false, nil end
    if IsPlayerAlly(me, other) then return false, nil end -- already allied

    local allyCount = DipAllyCount(pi)
    if allyCount >= cfg.allianceMax then return false, nil end

    -- Re-ally cooldown: don't immediately re-propose to someone we just broke with.
    local st0 = AiDiplomatState(pi)
    if st0.brokeAt ~= nil and st0.brokeAt[otherPi] ~= nil then
        local since = (AiDiplomatTicks[pi] or 0) - st0.brokeAt[otherPi]
        if since < AiDiplomatReallyCooldown then return false, nil end
    end

    local score = AiDiplomatEvaluate(pi, otherPi)
    local threshold = 1.0 - cfg.allianceDesire * 0.7 -- desire 0→thresh=1.0, desire 1→thresh=0.3

    if score >= threshold then
        local st = AiDiplomatState(pi)
        local rel = st.relations[otherPi]
        local reason = nil
        if rel ~= nil and rel.sharedEnemies > 0 then
            reason = "У нас общий враг. Объединим силы."
        elseif rel ~= nil and rel.threat > 0.5 then
            reason = "Нам угрожает один враг. Союз поможет нам обоим."
        end
        return true, reason
    end
    return false, nil
end

-- ====================================================================
-- Decide whether to break an existing alliance.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@return boolean, string
function AiDiplomatConsiderBreak(pi, otherPi)
    local cfg = AiDiplomatCfg(pi)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return false, nil end
    if not IsPlayerAlly(me, other) then return false, nil end

    local st = AiDiplomatState(pi)
    local rel = st.relations[otherPi]
    if rel == nil then return true, "В наших отношениях больше нет смысла." end

    -- Young alliances are protected from circumstantial breaks (weakness / no
    -- common threat) so power/proximity noise can't make bots ally-and-drop every
    -- few ticks. Betrayal (4) and the rare random break (3) are still allowed.
    local tickNow = AiDiplomatTicks[pi] or 0
    local allyAge = tickNow - ((st.alliedAt and st.alliedAt[otherPi]) or 0)
    -- Сила нужна и проверке слабости (1), и предательству (4) — считать вне if.
    local otherPower = Grades[otherPi] or 0
    local myPower = Grades[pi] or 1
    if allyAge >= AiDiplomatMinAllyAge then
        -- 1. Ally is too weak
        local weakness = 1.0 - (otherPower / math.max(myPower, 1))
        if weakness > cfg.breakOnWeakness then
            return true, "Ты слишком ослаб, чтобы приносить пользу."
        end

        -- 2. No common threat anymore
        if rel.sharedEnemies == 0 and cfg.breakOnNoThreat > 0.5 then
            return true, "Нашего общего врага больше нет. Этот союз мне больше не нужен."
        end
    end

    -- 3. Base random break chance (scaled by inverse of loyalty)
    local breakRoll = GetRandomReal(0.0, 1.0)
    local breakChance = cfg.breakChanceBase * (1.0 - cfg.loyalty)
    if breakRoll < breakChance then
        return true, "Наш союз исчерпал себя."
    end

    -- 4. Betrayal check (traitor personality)
    if cfg.betrayalChance > 0 and cfg.betrayTimeMin ~= nil then
        -- Already marked for betrayal?
        if st.betrayTargets[otherPi] ~= nil then
            local tickNow = AiDiplomatTicks[pi] or 0
            if tickNow >= st.betrayTargets[otherPi] then
                st.betrayTargets[otherPi] = nil
                return true, "Зря ты мне доверился."
            end
        else
            local betrayalRoll = GetRandomReal(0.0, 1.0)
            if betrayalRoll < cfg.betrayalChance and otherPower < myPower then
                local delay = cfg.betrayAttackDelay or 180
                st.betrayTargets[otherPi] = (AiDiplomatTicks[pi] or 0) + delay
                DipLog(pi, "marked betrayal vs " .. tostring(otherPi) .. " delay=" .. tostring(delay))
            end
        end
    end

    return false, nil
end

-- ====================================================================
-- Decide whether to trade resources with an ally.
-- ====================================================================
---@param pi integer
---@param otherPi integer
---@return integer, integer, string|nil   -- gold, lumber, reason
function AiDiplomatConsiderTrade(pi, otherPi)
    local cfg = AiDiplomatCfg(pi)
    if cfg.tradeGoldFraction <= 0 and cfg.tradeLumberFraction <= 0 then
        return 0, 0, nil
    end
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return 0, 0, nil end
    if not IsPlayerAlly(me, other) then return 0, 0, nil end

    local myGold = GetPlayerState(me, PLAYER_STATE_RESOURCE_GOLD)
    local myLumber = GetPlayerState(me, PLAYER_STATE_RESOURCE_LUMBER)
    if myGold < 500 then return 0, 0, nil end -- too poor to trade

    local st = AiDiplomatState(pi)
    local rel = st.relations[otherPi]

    -- How much does the other player need help?
    local otherPower = Grades[otherPi] or 0
    local myPower = Grades[pi] or 1
    local needFactor = 0.0
    if rel ~= nil and rel.threat > 0.3 then
        needFactor = rel.threat * cfg.helpWeakAllies
    end
    if otherPower < myPower * 0.5 then
        needFactor = needFactor + (1.0 - otherPower / myPower) * cfg.helpWeakAllies * 0.5
    end

    if needFactor < 0.2 then return 0, 0, nil end

    local selfish = cfg.selfishness
    local maxGold = R2I(myGold * cfg.tradeGoldFraction * (1.0 - selfish) * needFactor)
    local maxLumber = R2I(myLumber * cfg.tradeLumberFraction * (1.0 - selfish) * needFactor)

    if maxGold < 100 then maxGold = 0 end
    if maxLumber < 50 then maxLumber = 0 end
    if maxGold == 0 and maxLumber == 0 then return 0, 0, nil end

    local reason = nil
    if rel ~= nil and rel.threat > 0.4 then
        reason = "Держи оборону. Это должно помочь."
    elseif otherPower < myPower * 0.5 then
        reason = "Тебе это нужнее, чем мне."
    else
        reason = "Знак нашего союза."
    end

    return maxGold, maxLumber, reason
end

-- ====================================================================
-- Respond to an incoming alliance proposal (instant – called from
-- the alliance-change event handler or from the player command handler).
-- ====================================================================
---@param pi integer  bot who needs to respond
---@param otherPi integer  player who proposed
function AiDiplomatRespondToProposal(pi, otherPi)
    local cfg = AiDiplomatCfg(pi)
    local st = AiDiplomatState(pi)
    local me = Player(pi)
    local other = Player(otherPi)
    if me == nil or other == nil then return end
    if IsPlayerAlly(me, other) then return end -- already allied

    local allyCount = DipAllyCount(pi)
    if allyCount >= cfg.allianceMax then
        AiDiplomatDecline(pi, otherPi)
        DipChat(pi, otherPi, "У меня уже достаточно союзников. Возможно, в другой раз.")
        return
    end

    local score = AiDiplomatEvaluate(pi, otherPi)
    local threshold = 1.0 - cfg.allianceDesire * 0.7

    if score >= threshold then
        AiDiplomatAccept(pi, otherPi)
    else
        AiDiplomatDecline(pi, otherPi)
        DipChat(pi, otherPi, "Сейчас я не заинтересован в союзе.")
    end
end

-- ====================================================================
-- Main diplomat tick. Called periodically per bot.
-- 1. Perceive (rebuild relationship data)
-- 2. Detect incoming proposals from other players
-- 3. Evaluate each other player
-- 4. Decide alliances / resources
-- ====================================================================
---@param pi integer
function AiDiplomatTick(pi)
    if not AiDiplomatEnabled then return end
    local cfg = AiDiplomatCfg(pi)
    if cfg == nil then return end -- race didn't opt in
    AiDiplomatRegister()
    local st = AiDiplomatState(pi)
    local tick = (AiDiplomatTicks[pi] or 0) + 1
    AiDiplomatTicks[pi] = tick

    if tick == 1 then
        --DipLog(pi, "diplomat initialised cfg.allianceMax=" .. tostring(cfg.allianceMax) ..
        --    " cfg.allianceDesire=" .. tostring(cfg.allianceDesire) ..
        --    " cfg.loyalty=" .. tostring(cfg.loyalty))
        --DipBroadcast(DiplomatName(pi) .. " diplomat active. " ..
        --    "desire=" .. tostring(R2I(cfg.allianceDesire * 100)) ..
        --    "% loyalty=" .. tostring(R2I(cfg.loyalty * 100)) .. "%")
    end

    -- Perceive every tick
    AiDiplomatPerceive(pi)

    -- Detect incoming proposals: another player shared vision with us
    -- but we didn't request it, and we're not already in a mutual alliance.
    AiDiplomatDetectProposals(pi)

    -- Clear expired pending offers (timeout)
    for otherPi, offerTime in pairs(st.pendingOffers) do
        local elapsed = tick - (offerTime or 0)
        if elapsed > (AiDiplomatProposalTimeout or 30) then
            AiDiplomatDecline(pi, otherPi)
            DipLog(pi, "offer to " .. tostring(otherPi) .. " timed out")
        end
    end

    -- Evaluate each other player
    for otherPi, rel in pairs(st.relations) do
        local other = Player(otherPi)
        if other ~= nil then
            -- 1. Check if we should break an existing alliance
            local shouldBreak, breakReason = AiDiplomatConsiderBreak(pi, otherPi)
            if shouldBreak then
                AiDiplomatBreak(pi, otherPi, breakReason)
                goto continue
            end

            -- 2. Check if we should propose an alliance
            local shouldAlly, allyReason = AiDiplomatConsiderAlly(pi, otherPi)
            if shouldAlly and st.pendingOffers[otherPi] == nil then
                AiDiplomatPropose(pi, otherPi)
            end

            -- 3. Check if we should trade resources
            local tradeFreq = cfg.tradeFrequency or 9999
            local lastTrade = st.lastTrade[otherPi] or 0
            if tick - lastTrade >= tradeFreq then
                local gold, lumber, tradeReason = AiDiplomatConsiderTrade(pi, otherPi)
                if gold > 0 or lumber > 0 then
                    AiDiplomatTrade(pi, otherPi, gold, lumber, tradeReason)
                end
            end

            ::continue::
        end
    end

    -- Log summary every N ticks
    DipLogEvery(pi, "summary", 10,
        "allies=" .. tostring(DipAllyCount(pi)) ..
        " relations=" .. tostring(DipRelationCount(pi)))

    -- Idle RP: occasional flavour message (~every 20 ticks)
    if (tick % 20) == 0 then
        AiDiplomatRpSay(pi, "idle")
    end

    -- Under-attack RP: capital HP dropped significantly since last perceive
    if st.underAttackFired then
        AiDiplomatRpSay(pi, "underAttack")
        st.underAttackFired = false
    end
end

-- ====================================================================
-- Detect incoming alliance proposals from other players.
-- Compares current alliance state vs our known state.
-- If another player shares vision with us but we haven't allied with them
-- and we haven't already processed this proposal, respond instantly.
-- ====================================================================
---@param pi integer
function AiDiplomatDetectProposals(pi)
    local st = AiDiplomatState(pi)
    local me = Player(pi)
    if me == nil then return end

    for otherPi = 0, 23 do
        if otherPi ~= pi then
            local other = Player(otherPi)
            if other ~= nil and playerCapital[otherPi] ~= nil then
                local otherSharesVision = GetPlayerAlliance(other, me, ALLIANCE_SHARED_VISION)
                local isMutualAlly = IsPlayerAlly(me, other)
                local alreadyProposed = st.pendingRequests[otherPi] ~= nil
                local alreadyProcessed = st.processedProposals and st.processedProposals[otherPi]

                -- Another player started sharing vision with us (proposal signal)
                -- but we haven't yet processed it, we're not already allies, and we didn't initiate it
                if otherSharesVision and not isMutualAlly and not alreadyProposed and not alreadyProcessed then
                    local weShareWithThem = GetPlayerAlliance(me, other, ALLIANCE_SHARED_VISION)
                    if not weShareWithThem then
                        -- It's an incoming proposal (they shared vision, we didn't share back yet)
                        DipLog(pi, "detected proposal from " .. tostring(otherPi))
                        st.pendingRequests[otherPi] = AiDiplomatTicks[pi] or 0
                        if st.processedProposals == nil then st.processedProposals = {} end
                        st.processedProposals[otherPi] = true
                        AiDiplomatRespondToProposal(pi, otherPi)
                    end
                end
            end
        end
    end
end

-- ====================================================================
-- Count of tracked relationships.
-- ====================================================================
---@param pi integer
---@return integer
function DipRelationCount(pi)
    local st = AiDiplomat[pi]
    if st == nil then return 0 end
    local n = 0
    for _ in pairs(st.relations) do n = n + 1 end
    return n
end

-- ====================================================================
-- Lazy registration: called on first diplomat tick to ensure one-time
-- setup. Currently a no-op (proposal detection is purely periodic).
-- ====================================================================
function AiDiplomatRegister()
    if AiDiplomatTriggerRegistered then return end
    AiDiplomatTriggerRegistered = true
    DipLog(-1, "diplomat module activated")
end

-- ====================================================================
-- Force a diplomat tick from the bridge / debug.
-- ====================================================================
---@param pi integer
function AiDiplomatForceTick(pi)
    AiDiplomatTick(pi)
end
