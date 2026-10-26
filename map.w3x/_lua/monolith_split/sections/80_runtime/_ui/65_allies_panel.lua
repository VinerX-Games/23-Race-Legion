-- ***************************************************************************
-- *  AlliesPanel
-- Окно «Союзники» вместо стандартного окна союзов (F11). Союз заключается
-- предложением и согласием; лимит союзов (DipMode), налог союза, вассалитет и
-- журнал видны в одном окне. Передача ресурсов — ползунками, архонт — кнопкой.
-- Стандартное окно остаётся, но после DipStart смена союзов и передача ресурсов
-- в нём заблокированы флагами карты: всё меняют триггеры этого окна.
--
-- Синхронизация: все клики, колесо мыши, ползунки и F11 — синхронные события
-- фреймов; обработчики меняют общее состояние (AP.open/offset/pending/...).
-- Отрисовка — только внешний вид фреймов локального игрока, без хендлов и без
-- изменения игровых данных. Строка списка → игрок вычисляется из общего
-- смещения AP.offset, поэтому клик попадает в того же игрока, что виден.
-- У каждого действия своя кнопка: клик по устаревшей кнопке отбрасывается
-- проверкой AP.Actions, а не превращается в другое действие.
-- Локалы — внутри do-блока, состояние и функции — в таблице AP: главный чанк
-- war3map.lua упирается в лимит регистров Lua.
AlliesPanelActive = false   -- окно создано и заменяет стандартное

do
	local AP = {
		W = 0.64, LEFT = 0.08, TOP = 0.565, PAD = 0.014,
		ROWS = 9, ROW_H = 0.026, BTN_H = 0.019, GAP = 0.003,
		TIMEOUT = 30, TICK = 0.5, LOG_MAX = 5, CHAR_W = 0.0058, SCROLL_W = 0.012,
		TEAM_TEX = "ReplaceableTextures\\TeamColor\\TeamColor%02d.blp",
		-- Порядок кнопок действий в строке.
		KINDS = { "accept", "decline", "propose", "cancel", "break", "res", "archont" },
		rows = {}, btnW = {}, upperSlot = {},
		seen = {}, open = {}, offset = {}, pending = {}, log = {},
		resTarget = {}, sendG = {}, sendL = {}, ctlAdded = {},
		clock = 0, uiShown = true, sliderMax = -1,
	}

	-- Цвета палитры docs/UI_COLOR_PALETTE.md.
	AP.C_TEXT, AP.C_WHITE, AP.C_POS, AP.C_NEG = "|cffced4da", "|cffffffff", "|cffc8e087", "|cffef8173"
	AP.C_WARN, AP.C_NAME, AP.C_SEC = "|cfff2a35e", "|cffebc56c", "|cffb99d66"

	-- ===================================================================
	-- Состояние партии (синхронный код)
	-- ===================================================================

	function AP.IsParticipant(pi)
		local p = Player(pi)
		if Observers ~= nil and IsPlayerInForce(p, Observers) then return false end
		return GetPlayerSlotState(p) == PLAYER_SLOT_STATE_PLAYING or udg_AiControl[pi] == true
	end

	-- Выбыл: ушёл из игры, стал зрителем или выбрал расу и остался без столицы.
	function AP.IsOut(pi)
		if not AP.IsParticipant(pi) then return true end
		return CustomHudPlayerRaceName ~= nil and CustomHudPlayerRaceName(pi) ~= nil and playerCapital[pi] == nil
	end

	-- Все, кто когда-либо участвовал, кроме v; выбывшие остаются в списке, чтобы
	-- строки не съезжали.
	function AP.Targets(v)
		local list = {}
		for pi = 0, 23 do
			if pi ~= v and AP.seen[pi] then list[#list + 1] = pi end
		end
		return list
	end

	function AP.MaxOffset(n)
		return math.max(0, n - AP.ROWS)
	end

	function AP.Offset(v, n)
		return math.max(0, math.min(AP.offset[v] or 0, AP.MaxOffset(n)))
	end

	function AP.Allied(a, b)
		return IsPlayerAlly(Player(a), Player(b)) and IsPlayerAlly(Player(b), Player(a))
	end

	function AP.OtherAllies(p)
		local n = 0
		for j = 0, 23 do
			if j ~= p and AP.Allied(p, j) then n = n + 1 end
		end
		return n
	end

	-- Счёт союзников так же, как в Trig_StartAlly_Actions: именно с ним
	-- сравнивается DipMode при сбросе союзов.
	function AP.EnumAllies(p)
		ForceEnumAllies(AP.force, Player(p), nil)
		local n = CountPlayersInForceBJ(AP.force)
		ForceClear(AP.force)
		return n
	end

	-- Новый союз превысит лимит и сбросит все союзы игрока.
	function AP.Full(p)
		return DipMode ~= nil and DipMode > 1 and AP.EnumAllies(p) + 1 > DipMode
	end

	-- Сколько союзников разрешено сверх самого игрока (для подписи «N из M»).
	function AP.AllowedAllies()
		if DipMode == nil or DipMode <= 1 then return nil end
		return DipMode - (AP.selfInEnum and 1 or 0)
	end

	function AP.Pending(from, to)
		return AP.pending[from] ~= nil and AP.pending[from][to] ~= nil
	end

	function AP.ClearPending(a, b)
		if AP.pending[a] ~= nil then AP.pending[a][b] = nil end
		if AP.pending[b] ~= nil then AP.pending[b][a] = nil end
	end

	function AP.Relation(v, t)
		if AP.IsOut(t) then return "out" end
		if Senior[t] == Player(v) then return "vassal" end
		if Senior[v] == Player(t) then return "liege" end
		if AP.Allied(v, t) then return "ally" end
		if AP.Pending(t, v) then return "pending_in" end
		if AP.Pending(v, t) then return "pending_out" end
		return "war"
	end

	-- Доступные игроку v действия над игроком t, в порядке AP.KINDS.
	function AP.Actions(v, t)
		local rel = AP.Relation(v, t)
		if rel == "out" or AP.IsOut(v) then return {} end
		local ffa = DipMode == 1
		local list
		if rel == "vassal" or rel == "liege" then
			list = { "res", "archont" }
		elseif rel == "ally" then
			list = { "break", "res", "archont" }
		elseif rel == "pending_in" then
			list = { "accept", "decline" }
		elseif rel == "pending_out" then
			list = { "cancel", "res" }
		else
			list = { "propose", "res" }
		end
		local out = {}
		for i = 1, #list do
			local k = list[i]
			if not (ffa and (k == "res" or k == "propose")) then out[#out + 1] = k end
		end
		return out
	end

	function AP.Has(list, kind)
		for i = 1, #list do
			if list[i] == kind then return true end
		end
		return false
	end

	function AP.Name(pi)
		return GetPlayerName(Player(pi)) or ""
	end

	-- Запись в журнал игрока p; chat — продублировать сообщением на экране.
	-- Текст хранится ключом и аргументами: Loc() вызывается только при показе.
	function AP.Note(p, chat, key, ...)
		local list = AP.log[p]
		if list == nil then
			list = {}
			AP.log[p] = list
		end
		list[#list + 1] = { t = AP.clock, key = key, args = { ... } }
		if #list > AP.LOG_MAX then table.remove(list, 1) end
		if chat then
			DisplayTimedTextToPlayer(Player(p), 0, 0, 8, string.format(Loc(key), ...))
		end
	end

	-- ===================================================================
	-- Действия (синхронный код)
	-- ===================================================================

	function AP.MakeAlliance(a, b)
		AP.ClearPending(a, b)
		SetPlayerAllianceStateBJ(Player(a), Player(b), bj_ALLIANCE_ALLIED_VISION)
		SetPlayerAllianceStateBJ(Player(b), Player(a), bj_ALLIANCE_ALLIED_VISION)
	end

	-- Ответ бота. Пока дипломатия ботов выключена (AiDiplomatEnabled), боты
	-- союзов не заключают — так же, как при стандартном окне.
	function AP.BotAnswer(bot, from)
		if not AiDiplomatEnabled or AiDiplomatCfg == nil then return nil end
		local cfg = AiDiplomatCfg(bot)
		if cfg == nil then return nil end
		if DipAllyCount(bot) >= cfg.allianceMax then return false end
		return AiDiplomatEvaluate(bot, from) >= 1.0 - cfg.allianceDesire * 0.7
	end

	function AP.Propose(v, t)
		if AP.Pending(t, v) then
			AP.Accept(v, t)
			return
		end
		if AP.Full(v) then
			AP.Note(v, true, "allies.log.limit_self")
			return
		end
		if AP.Full(t) then
			AP.Note(v, true, "allies.log.limit_other", AP.Name(t))
			return
		end
		if udg_AiControl[t] then
			local yes = AP.BotAnswer(t, v)
			if yes == nil then
				AP.Note(v, true, "allies.log.bot_declines", AP.Name(t))
			elseif yes then
				AP.MakeAlliance(v, t)
				AP.Note(v, true, "allies.log.accepted_by", AP.Name(t))
			else
				AP.Note(v, true, "allies.log.declined_by", AP.Name(t))
			end
			return
		end
		AP.pending[v] = AP.pending[v] or {}
		AP.pending[v][t] = AP.clock + AP.TIMEOUT
		AP.Note(v, false, "allies.log.proposed", AP.Name(t))
		AP.Note(t, true, "allies.log.received", AP.Name(v))
	end

	function AP.Accept(v, from)
		if not AP.Pending(from, v) then return end
		if AP.Full(v) then
			AP.Note(v, true, "allies.log.limit_self")
			return
		end
		if AP.Full(from) then
			AP.ClearPending(v, from)
			AP.Note(v, true, "allies.log.limit_other", AP.Name(from))
			return
		end
		AP.MakeAlliance(v, from)
		AP.Note(v, false, "allies.log.you_accepted", AP.Name(from))
		AP.Note(from, true, "allies.log.accepted_by", AP.Name(v))
	end

	function AP.Decline(v, from)
		if not AP.Pending(from, v) then return end
		AP.ClearPending(v, from)
		AP.Note(v, false, "allies.log.you_declined", AP.Name(from))
		AP.Note(from, true, "allies.log.declined_by", AP.Name(v))
	end

	function AP.Cancel(v, t)
		if not AP.Pending(v, t) then return end
		AP.pending[v][t] = nil
		AP.Note(v, false, "allies.log.withdrawn", AP.Name(t))
		AP.Note(t, true, "allies.log.withdrawn_by", AP.Name(v))
	end

	function AP.Break(v, t)
		SetPlayerAllianceStateBJ(Player(v), Player(t), bj_ALLIANCE_UNALLIED)
		SetPlayerAllianceStateBJ(Player(t), Player(v), bj_ALLIANCE_UNALLIED)
		AP.Note(v, false, "allies.log.broke", AP.Name(t))
		AP.Note(t, true, "allies.log.broken_by", AP.Name(v))
	end

	-- Архонт: полный контроль юнитов v отдаётся t. Обычный общий контроль,
	-- который был до включения (вассал → сюзерен), при выключении остаётся.
	function AP.Archont(v, t)
		local p, q = Player(v), Player(t)
		AP.ctlAdded[v] = AP.ctlAdded[v] or {}
		if not GetPlayerAlliance(p, q, ALLIANCE_SHARED_ADVANCED_CONTROL) then
			AP.ctlAdded[v][t] = not GetPlayerAlliance(p, q, ALLIANCE_SHARED_CONTROL)
			SetPlayerAlliance(p, q, ALLIANCE_SHARED_CONTROL, true)
			SetPlayerAlliance(p, q, ALLIANCE_SHARED_ADVANCED_CONTROL, true)
			AP.Note(v, false, "allies.log.archont_on", AP.Name(t))
			AP.Note(t, true, "allies.log.archont_on_by", AP.Name(v))
		else
			SetPlayerAlliance(p, q, ALLIANCE_SHARED_ADVANCED_CONTROL, false)
			if AP.ctlAdded[v][t] then SetPlayerAlliance(p, q, ALLIANCE_SHARED_CONTROL, false) end
			AP.ctlAdded[v][t] = nil
			AP.Note(v, false, "allies.log.archont_off", AP.Name(t))
			AP.Note(t, true, "allies.log.archont_off_by", AP.Name(v))
		end
	end

	function AP.SendResources(v, t, gold, lumber)
		local p, q = Player(v), Player(t)
		gold = math.max(0, math.min(math.floor(gold or 0), GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)))
		lumber = math.max(0, math.min(math.floor(lumber or 0), GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER)))
		if gold + lumber <= 0 then return end
		SetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) - gold)
		SetPlayerState(q, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(q, PLAYER_STATE_RESOURCE_GOLD) + gold)
		SetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER) - lumber)
		SetPlayerState(q, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(q, PLAYER_STATE_RESOURCE_LUMBER) + lumber)
		AP.Note(v, false, "allies.log.sent", AP.Name(t), gold, lumber)
		AP.Note(t, true, "allies.log.received_res", AP.Name(v), gold, lumber)
	end

	-- Входящее предложение для всплывающего оповещения: истекает раньше всех.
	function AP.OldestIncoming(v)
		local best, bestT
		for from = 0, 23 do
			if AP.Pending(from, v) and (bestT == nil or AP.pending[from][v] < bestT) then
				best, bestT = from, AP.pending[from][v]
			end
		end
		return best
	end

	function AP.IncomingCount(v)
		local n = 0
		for from = 0, 23 do
			if AP.Pending(from, v) then n = n + 1 end
		end
		return n
	end

	-- Период: участники, истечение предложений, отрисовка.
	function AP.Tick()
		AP.clock = AP.clock + AP.TICK
		for pi = 0, 23 do
			if not AP.seen[pi] and AP.IsParticipant(pi) then AP.seen[pi] = true end
		end
		for from = 0, 23 do
			for to = 0, 23 do
				if AP.Pending(from, to) then
					if AP.IsOut(from) or AP.IsOut(to) then
						AP.pending[from][to] = nil
					elseif AP.clock >= AP.pending[from][to] then
						AP.pending[from][to] = nil
						AP.Note(from, true, "allies.log.expired_out", AP.Name(to))
						AP.Note(to, false, "allies.log.expired_in", AP.Name(from))
					end
				end
			end
		end
		AP.Render()
	end

	-- ===================================================================
	-- Отрисовка (только фреймы локального игрока)
	-- ===================================================================

	function AP.TextW(text)
		local w = 0
		if AP.measure ~= nil then
			BlzFrameSetText(AP.measure, text)
			w = BlzFrameGetWidth(AP.measure) or 0
		end
		return math.max(w, (utf8.len(text) or string.len(text)) * AP.CHAR_W)
	end

	function AP.Clock(t)
		local s = math.floor(t)
		return string.format("%d:%02d", s // 60, s % 60)
	end

	function AP.Color(pi)
		return string.format(AP.TEAM_TEX, GetHandleId(GetPlayerColor(Player(pi))) % 100)
	end

	function AP.RaceName(pi)
		local name = CustomHudPlayerRaceName ~= nil and CustomHudPlayerRaceName(pi) or nil
		return name or "—"
	end

	AP.STATUS = {
		ally = { "allies.status.ally", AP.C_POS },
		war = { "allies.status.war", AP.C_NEG },
		pending_in = { "allies.status.pending_in", AP.C_POS },
		pending_out = { "allies.status.pending_out", AP.C_WARN },
		vassal = { "allies.status.vassal", AP.C_NAME },
		liege = { "allies.status.liege", AP.C_NAME },
		out = { "allies.status.out", AP.C_SEC },
	}

	function AP.ChipsText(v)
		local mode
		if DipMode == 1 then
			mode = Loc("allies.chip.mode_ffa")
		elseif DipMode == nil or DipMode == 0 then
			mode = Loc("allies.chip.mode_free")
		else
			mode = string.format(Loc("allies.chip.mode_limit"), DipMode)
		end
		local allowed = AP.AllowedAllies()
		local allies = allowed ~= nil and string.format(Loc("allies.chip.allies_of"), AP.OtherAllies(v), allowed)
			or string.format(Loc("allies.chip.allies"), AP.OtherAllies(v))
		local pct = math.floor((AllyTax[v] or 0) * 100 + 0.5)
		local tax = string.format(Loc("allies.chip.tax"),
			pct > 0 and (AP.C_NEG .. "−" .. pct .. "%") or (AP.C_WHITE .. "0%"))
		local vassals = Vassals[v] ~= nil and CountPlayersInForceBJ(Vassals[v]) or 0
		return mode .. "     " .. allies .. "     " .. tax .. "     "
			.. string.format(Loc("allies.chip.vassals"), vassals) .. "|r"
	end

	function AP.VassalageText()
		local lines = {}
		for j = 0, 23 do
			local names = {}
			for k = 0, 23 do
				if Senior[k] ~= nil and Senior[k] == Player(j) then names[#names + 1] = AP.Name(k) end
			end
			if #names > 0 and #lines < AP.LOG_MAX then
				lines[#lines + 1] = string.format(Loc("allies.vassalage.line"), AP.Name(j), table.concat(names, ", "))
			end
		end
		if #lines == 0 then return Loc("allies.vassalage.none") end
		return table.concat(lines, "|n")
	end

	function AP.LogText(v)
		local list = AP.log[v]
		if list == nil or #list == 0 then return Loc("allies.log.empty") end
		local lines = {}
		for i = #list, 1, -1 do
			local e = list[i]
			lines[#lines + 1] = AP.C_SEC .. AP.Clock(e.t) .. "|r  " .. string.format(Loc(e.key), table.unpack(e.args))
		end
		return table.concat(lines, "|n")
	end

	-- Закреплённая строка «Вы»: раса и города самого игрока, без кнопок.
	function AP.RenderSelf(v)
		local row = AP.selfRow
		BlzFrameSetTexture(row.swatch, AP.Color(v), 0, true)
		BlzFrameSetText(row.name, AP.C_NAME .. AP.Name(v) .. "|r")
		local sub = Senior[v] ~= nil and string.format(Loc("allies.sub.vassal_of"), GetPlayerName(Senior[v]) or "")
			or Loc("allies.sub.you")
		BlzFrameSetText(row.sub, AP.C_SEC .. sub .. "|r")
		BlzFrameSetText(row.race, AP.C_TEXT .. AP.RaceName(v) .. "|r")
		BlzFrameSetText(row.cities, AP.C_WHITE .. math.floor(CityPlayerCount ~= nil and CityPlayerCount[v] or 0) .. "|r")
		BlzFrameSetText(row.status, AP.IsOut(v) and (AP.C_SEC .. Loc("allies.status.out") .. "|r") or "")
	end

	function AP.RenderRow(v, row, t)
		local show = t ~= nil
		for _, f in ipairs(row.parts) do BlzFrameSetVisible(f, show) end
		for i = 1, #AP.KINDS do FrameSetShown(row.btn[AP.KINDS[i]], false) end
		if not show then return end
		local rel = AP.Relation(v, t)
		BlzFrameSetTexture(row.swatch, AP.Color(t), 0, true)
		BlzFrameSetText(row.name, AP.C_NAME .. AP.Name(t) .. "|r")
		local sub = ""
		if Senior[t] ~= nil and rel ~= "vassal" and rel ~= "liege" then
			sub = string.format(Loc("allies.sub.vassal_of"), GetPlayerName(Senior[t]) or "")
		elseif udg_AiControl[t] then
			sub = Loc("allies.sub.bot")
		end
		BlzFrameSetText(row.sub, AP.C_SEC .. sub .. "|r")
		BlzFrameSetText(row.race, AP.C_TEXT .. AP.RaceName(t) .. "|r")
		BlzFrameSetText(row.cities, AP.C_WHITE .. math.floor(CityPlayerCount ~= nil and CityPlayerCount[t] or 0) .. "|r")
		local st = AP.STATUS[rel]
		BlzFrameSetText(row.status, st[2] .. Loc(st[1]) .. "|r")
		local x = 0
		local acts = AP.Actions(v, t)
		for i = 1, #acts do
			local kind = acts[i]
			local b = row.btn[kind]
			if kind == "archont" then
				local on = GetPlayerAlliance(Player(v), Player(t), ALLIANCE_SHARED_ADVANCED_CONTROL)
				BlzFrameSetText(row.label.archont, on and (AP.C_WARN .. Loc("allies.act.archont_on") .. "|r")
					or (AP.C_TEXT .. Loc("allies.act.archont") .. "|r"))
			end
			FrameSetPoint(b, FRAMEPOINT_LEFT, AP.root, FRAMEPOINT_TOPLEFT, row.actX + x, row.y)
			FrameSetShown(b, true)
			x = x + AP.btnW[kind] + AP.GAP
		end
	end

	function AP.RenderToast(v)
		local from = (not AP.open[v]) and AP.OldestIncoming(v) or nil
		FrameSetShown(AP.toast, from ~= nil and AP.uiShown)
		if from == nil then return end
		local left = math.max(0, AP.pending[from][v] - AP.clock)
		BlzFrameSetTexture(AP.toastSwatch, AP.Color(from), 0, true)
		BlzFrameSetText(AP.toastBody, string.format(Loc("allies.toast.text"), AP.Name(from), AP.RaceName(from)))
		BlzFrameSetText(AP.toastTimer, string.format(Loc("allies.toast.timer"), math.ceil(left)))
		BlzFrameSetSize(AP.toastBar, math.max(0.001, AP.toastBarW * left / AP.TIMEOUT), 0.002)
	end

	function AP.RenderDialog(v)
		local t = AP.resTarget[v]
		FrameSetShown(AP.dialog, t ~= nil)
		if t == nil then return end
		local p = Player(v)
		local gold, lumber = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD), GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER)
		BlzFrameSetText(AP.dialogTo, string.format(Loc("allies.res.to"), AP.Name(t)))
		BlzFrameSetText(AP.goldText, string.format(Loc("allies.res.gold"), math.min(AP.sendG[v] or 0, gold), gold))
		BlzFrameSetText(AP.lumberText, string.format(Loc("allies.res.lumber"), math.min(AP.sendL[v] or 0, lumber), lumber))
		-- Границы — только при изменении запаса: смена границ может сдвинуть ползунок.
		if AP.dlgMaxG ~= gold then
			AP.dlgMaxG = gold
			BlzFrameSetMinMaxValue(AP.goldSlider, 0, math.max(gold, 1))
		end
		if AP.dlgMaxL ~= lumber then
			AP.dlgMaxL = lumber
			BlzFrameSetMinMaxValue(AP.lumberSlider, 0, math.max(lumber, 1))
		end
	end

	function AP.Render()
		if AP.root == nil then return end
		local v = GetPlayerId(GetLocalPlayer())
		local n = AP.IncomingCount(v)
		BlzFrameSetText(AP.buttonText, AP.UpperLabel("allies.button", "F11")
			.. (n > 0 and (" " .. AP.C_WARN .. "(" .. n .. ")") or "") .. "|r")
		AP.RenderToast(v)
		local open = AP.open[v] == true and AP.uiShown
		FrameSetShown(AP.root, open)
		if not open then return end
		BlzFrameSetText(AP.chips, AP.ChipsText(v))
		AP.RenderSelf(v)
		local list = AP.Targets(v)
		local off = AP.Offset(v, #list)
		for r = 1, AP.ROWS do AP.RenderRow(v, AP.rows[r], list[off + r]) end
		local maxOff = AP.MaxOffset(#list)
		BlzFrameSetVisible(AP.empty, #list == 0)
		BlzFrameSetVisible(AP.range, #list > 0)
		BlzFrameSetText(AP.range, string.format(Loc("allies.range"),
			math.min(#list, off + 1), math.min(#list, off + AP.ROWS), #list))
		BlzFrameSetVisible(AP.slider, maxOff > 0)
		if AP.sliderMax ~= maxOff then
			AP.sliderMax = maxOff
			BlzFrameSetMinMaxValue(AP.slider, 0, math.max(maxOff, 1))
		end
		-- У вертикального ползунка максимум сверху.
		if maxOff > 0 and math.floor(BlzFrameGetValue(AP.slider) + 0.5) ~= maxOff - off then
			BlzFrameSetValue(AP.slider, maxOff - off)
		end
		BlzFrameSetText(AP.vassalText, AP.VassalageText())
		BlzFrameSetText(AP.logText, AP.LogText(v))
		AP.RenderDialog(v)
	end

	-- ===================================================================
	-- События фреймов (синхронные)
	-- ===================================================================

	-- Снять фокус с кнопки, иначе пробел/Enter продолжают нажимать её.
	function AP.Release(p)
		local f = BlzGetTriggerFrame()
		if GetLocalPlayer() == p and f ~= nil then
			BlzFrameSetEnable(f, false)
			BlzFrameSetEnable(f, true)
		end
	end

	function AP.OnEvent(frame, event, fn)
		local t = CreateTrigger()
		BlzTriggerRegisterFrameEvent(t, frame, event)
		TriggerAddAction(t, function()
			local p = GetTriggerPlayer()
			if event == FRAMEEVENT_CONTROL_CLICK then AP.Release(p) end
			fn(GetPlayerId(p))
			AP.Render()
		end)
	end

	function AP.Scroll(v, delta)
		local n = #AP.Targets(v)
		AP.offset[v] = math.max(0, math.min(AP.Offset(v, n) + delta, AP.MaxOffset(n)))
	end

	function AP.OnWheel(frame)
		AP.OnEvent(frame, FRAMEEVENT_MOUSE_WHEEL, function(v)
			AP.Scroll(v, BlzGetTriggerFrameValue() > 0 and -1 or 1)
		end)
	end

	function AP.Toggle(v)
		AP.open[v] = not AP.open[v]
		if not AP.open[v] then AP.resTarget[v] = nil end
	end

	function AP.RowClick(v, r, kind)
		if not AP.open[v] then return end
		local list = AP.Targets(v)
		local t = list[AP.Offset(v, #list) + r]
		if t == nil or not AP.Has(AP.Actions(v, t), kind) then return end
		if kind == "propose" then AP.Propose(v, t)
		elseif kind == "accept" then AP.Accept(v, t)
		elseif kind == "decline" then AP.Decline(v, t)
		elseif kind == "cancel" then AP.Cancel(v, t)
		elseif kind == "break" then AP.Break(v, t)
		elseif kind == "archont" then AP.Archont(v, t)
		elseif kind == "res" then
			AP.resTarget[v], AP.sendG[v], AP.sendL[v] = t, 0, 0
			if GetLocalPlayer() == Player(v) then
				BlzFrameSetValue(AP.goldSlider, 0)
				BlzFrameSetValue(AP.lumberSlider, 0)
			end
		end
	end

	-- ===================================================================
	-- Создание фреймов (у всех клиентов одинаково)
	-- ===================================================================

	function AP.Text(parent, tpl, w, h, justifyH)
		local f = BlzCreateFrame(tpl, parent, 0, 0)
		BlzFrameSetSize(f, w, h)
		BlzFrameSetTextAlignment(f, TEXT_JUSTIFY_MIDDLE, justifyH or TEXT_JUSTIFY_LEFT)
		BlzFrameSetEnable(f, false)
		return f
	end

	function AP.At(f, x, y, point)
		BlzFrameSetPoint(f, point or FRAMEPOINT_TOPLEFT, AP.root, FRAMEPOINT_TOPLEFT, x, y)
	end

	-- Кнопка с подписью; возвращает кнопку и текст подписи.
	function AP.Button(parent, w, label)
		local b = BlzCreateFrame("TasButtonTemplate", parent, 0, 0)
		BlzFrameSetSize(b, w, AP.BTN_H)
		local text = BlzCreateFrame("HudText", b, 0, 0)
		BlzFrameSetAllPoints(text, b)
		BlzFrameSetTextAlignment(text, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_CENTER)
		BlzFrameSetText(text, label)
		BlzFrameSetEnable(text, false)
		return b, text
	end

	-- Подсказка над кнопкой; показывает и прячет её движок.
	function AP.Tip(button, text)
		local box = BlzCreateFrame("BoxedTextBackgroundTemplate", button, 0, 0)
		local body = BlzCreateFrame("HudBody", box, 0, 0)
		BlzFrameSetTextAlignment(body, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
		BlzFrameSetSize(body, 0.22, 0)
		BlzFrameSetPoint(body, FRAMEPOINT_BOTTOM, button, FRAMEPOINT_TOP, 0, 0.012)
		BlzFrameSetText(body, text)
		BlzFrameSetPoint(box, FRAMEPOINT_TOPLEFT, body, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
		BlzFrameSetPoint(box, FRAMEPOINT_BOTTOMRIGHT, body, FRAMEPOINT_BOTTOMRIGHT, 0.007, -0.007)
		BlzFrameSetTooltip(button, box)
		BlzFrameSetVisible(box, false)
	end

	AP.ACT_KEY = {
		accept = { "allies.act.accept", AP.C_POS },
		decline = { "allies.act.decline", AP.C_NEG },
		propose = { "allies.act.propose", AP.C_POS },
		cancel = { "allies.act.cancel", AP.C_TEXT },
		["break"] = { "allies.act.break", AP.C_NEG },
		res = { "allies.act.res", AP.C_NAME },
		archont = { "allies.act.archont", AP.C_TEXT },
	}

	-- Колонки: x от левого поля и ширина. «Города» — по центру своей ширины.
	AP.COL_X = { 0.012, 0.135, 0.245, 0.305, 0.395 }
	AP.COL_W = { 0.12, 0.105, 0.05, 0.088 }

	-- Тонкая серая линия-разделитель по верхнему краю строки, слева от ползунка
	-- (или заданной ширины w — для разделов окна).
	function AP.Line(y, w)
		local line = BlzCreateFrameByType("BACKDROP", "AlliesPanelLine", AP.root, "", 0)
		BlzFrameSetTexture(line, string.format(AP.TEAM_TEX, 8), 0, true)
		BlzFrameSetSize(line, w or (AP.W - AP.PAD * 2 - AP.SCROLL_W - 0.004), 0.0008)
		BlzFrameSetAlpha(line, 110)
		AP.At(line, AP.PAD, y)
		return line
	end

	-- Текстовые части строки игрока с верхним краем y. Линия над строкой отделяет
	-- её от предыдущей (у строки «вы» — от шапки колонок).
	function AP.CreateRowParts(y)
		local colX, colW = AP.COL_X, AP.COL_W
		local cy = y - AP.ROW_H / 2
		local row = { y = cy, actX = AP.PAD + colX[5], btn = {}, label = {} }
		row.line = AP.Line(y + 0.001)
		row.swatch = BlzCreateFrameByType("BACKDROP", "AlliesPanelSwatch", AP.root, "", 0)
		BlzFrameSetSize(row.swatch, 0.009, 0.009)
		AP.At(row.swatch, AP.PAD, cy, FRAMEPOINT_LEFT)
		row.name = AP.Text(AP.root, "HudBody", colW[1], 0.012)
		AP.At(row.name, AP.PAD + colX[1], y - 0.002)
		row.sub = AP.Text(AP.root, "HudText", colW[1], 0.011)
		AP.At(row.sub, AP.PAD + colX[1], y - 0.0135)
		row.race = AP.Text(AP.root, "HudText", colW[2], AP.ROW_H)
		AP.At(row.race, AP.PAD + colX[2], y)
		row.cities = AP.Text(AP.root, "HudBody", colW[3], AP.ROW_H, TEXT_JUSTIFY_CENTER)
		AP.At(row.cities, AP.PAD + colX[3], y)
		row.status = AP.Text(AP.root, "HudText", colW[4], AP.ROW_H)
		AP.At(row.status, AP.PAD + colX[4], y)
		row.parts = { row.line, row.swatch, row.name, row.sub, row.race, row.cities, row.status }
		return row
	end

	function AP.CreateRows(innerW)
		local colX = AP.COL_X
		local headers = { "allies.col.player", "allies.col.race", "allies.col.cities", "allies.col.status", "allies.col.actions" }
		local y0 = -(AP.PAD + 0.022 + 0.006 + 0.016 + 0.008)
		AP.Line(y0 + 0.004, innerW)  -- отделяет сводку от таблицы
		for i = 1, #headers do
			local center = i == 3
			local h = AP.Text(AP.root, "HudText", center and AP.COL_W[3] or 0.1, 0.012,
				center and TEXT_JUSTIFY_CENTER or nil)
			AP.At(h, AP.PAD + colX[i], y0)
			BlzFrameSetText(h, AP.C_SEC .. Loc(headers[i]) .. "|r")
		end
		AP.range = AP.Text(AP.root, "HudText", 0.14, 0.012, TEXT_JUSTIFY_RIGHT)
		AP.At(AP.range, AP.W - AP.PAD - 0.14, y0)
		AP.selfRow = AP.CreateRowParts(y0 - 0.014)
		local rowsTop = y0 - 0.014 - AP.ROW_H
		AP.empty = AP.Text(AP.root, "HudText", innerW, AP.ROW_H)
		AP.At(AP.empty, AP.PAD + colX[1], rowsTop)
		BlzFrameSetText(AP.empty, AP.C_SEC .. Loc("allies.empty") .. "|r")
		for i = 1, #AP.KINDS do
			local k = AP.KINDS[i]
			local w = math.max(AP.TextW(Loc(AP.ACT_KEY[k][1])), k == "archont" and AP.TextW(Loc("allies.act.archont_on")) or 0)
			AP.btnW[k] = math.max(0.036, w + 0.012)
		end
		for r = 1, AP.ROWS do
			local row = AP.CreateRowParts(rowsTop - (r - 1) * AP.ROW_H)
			for i = 1, #AP.KINDS do
				local kind = AP.KINDS[i]
				local key = AP.ACT_KEY[kind]
				local b, text = AP.Button(AP.root, AP.btnW[kind], key[2] .. Loc(key[1]) .. "|r")
				row.btn[kind], row.label[kind] = b, text
				if kind == "archont" then AP.Tip(b, Loc("allies.tip.archont")) end
				if kind == "propose" then AP.Tip(b, Loc("allies.tip.propose")) end
				local rr = r
				AP.OnEvent(b, FRAMEEVENT_CONTROL_CLICK, function(v) AP.RowClick(v, rr, kind) end)
				AP.OnWheel(b)
				FrameSetShown(b, false)
			end
			AP.rows[r] = row
		end
		-- Вертикальный ползунок справа от строк; стрелки — часть шаблона.
		AP.slider = BlzCreateFrameByType("SLIDER", "AlliesPanelScroll", AP.root, "QuestMainListScrollBar", 0)
		BlzFrameSetSize(AP.slider, AP.SCROLL_W, AP.ROWS * AP.ROW_H)
		AP.At(AP.slider, AP.W - AP.PAD, rowsTop, FRAMEPOINT_TOPRIGHT)
		BlzFrameSetStepSize(AP.slider, 1)
		AP.OnWheel(AP.slider)
		AP.OnEvent(AP.slider, FRAMEEVENT_SLIDER_VALUE_CHANGED, function(v)
			local n = #AP.Targets(v)
			local maxOff = AP.MaxOffset(n)
			AP.offset[v] = math.max(0, math.min(maxOff - math.floor(BlzGetTriggerFrameValue() + 0.5), maxOff))
		end)
		return rowsTop - AP.ROWS * AP.ROW_H
	end

	function AP.CreateBottom(y, innerW)
		local colW = 0.2
		local h = 0.012 * AP.LOG_MAX
		AP.Line(y + 0.005, innerW)  -- отделяет таблицу от вассалитета и журнала
		local vt = AP.Text(AP.root, "HudBody", colW, 0.014)
		AP.At(vt, AP.PAD, y)
		BlzFrameSetText(vt, AP.C_NAME .. Loc("allies.vassalage") .. "|r")
		AP.vassalText = AP.Text(AP.root, "HudText", colW, h)
		BlzFrameSetTextAlignment(AP.vassalText, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
		AP.At(AP.vassalText, AP.PAD, y - 0.016)
		local lt = AP.Text(AP.root, "HudBody", innerW - colW - 0.02, 0.014)
		AP.At(lt, AP.PAD + colW + 0.02, y)
		BlzFrameSetText(lt, AP.C_NAME .. Loc("allies.log") .. "|r")
		AP.logText = AP.Text(AP.root, "HudText", innerW - colW - 0.02, h)
		BlzFrameSetTextAlignment(AP.logText, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
		AP.At(AP.logText, AP.PAD + colW + 0.02, y - 0.016)
		return y - 0.016 - h
	end

	function AP.CreateDialog(top)
		local w, h = 0.30, 0.15
		local d = BlzCreateFrame("BoxedTextBackgroundTemplate", AP.root, 0, 0)
		AP.dialog = d
		BlzFrameSetLevel(d, 3)
		BlzFrameSetSize(d, w, h)
		FrameSetPoint(d, FRAMEPOINT_TOP, AP.root, FRAMEPOINT_TOP, 0, top)
		local block = BlzCreateFrameByType("BUTTON", "AlliesDialogBlocker", d, "", 0)
		BlzFrameSetAllPoints(block, d)
		local function at(f, x, y, point) BlzFrameSetPoint(f, point or FRAMEPOINT_TOPLEFT, d, FRAMEPOINT_TOPLEFT, x, y) end
		local title = AP.Text(d, "HudTitle", w - 0.03, 0.02)
		at(title, 0.015, -0.012)
		BlzFrameSetText(title, AP.C_NAME .. Loc("allies.res.title") .. "|r")
		AP.dialogTo = AP.Text(d, "HudBody", w - 0.03, 0.014)
		at(AP.dialogTo, 0.015, -0.034)
		AP.goldText = AP.Text(d, "HudBody", w - 0.03, 0.014)
		at(AP.goldText, 0.015, -0.054)
		AP.goldSlider = BlzCreateFrame("EscMenuSliderTemplate", d, 0, 0)
		BlzFrameSetSize(AP.goldSlider, w - 0.03, 0.012)
		at(AP.goldSlider, 0.015, -0.07)
		AP.lumberText = AP.Text(d, "HudBody", w - 0.03, 0.014)
		at(AP.lumberText, 0.015, -0.088)
		AP.lumberSlider = BlzCreateFrame("EscMenuSliderTemplate", d, 0, 0)
		BlzFrameSetSize(AP.lumberSlider, w - 0.03, 0.012)
		at(AP.lumberSlider, 0.015, -0.104)
		for _, s in ipairs({ AP.goldSlider, AP.lumberSlider }) do
			BlzFrameSetMinMaxValue(s, 0, 1)
			BlzFrameSetStepSize(s, 50)
			BlzFrameSetValue(s, 0)
		end
		AP.OnEvent(AP.goldSlider, FRAMEEVENT_SLIDER_VALUE_CHANGED, function(v)
			AP.sendG[v] = math.max(0, math.floor(BlzGetTriggerFrameValue() + 0.5))
		end)
		AP.OnEvent(AP.lumberSlider, FRAMEEVENT_SLIDER_VALUE_CHANGED, function(v)
			AP.sendL[v] = math.max(0, math.floor(BlzGetTriggerFrameValue() + 0.5))
		end)
		local bw = 0.08
		local cancel = AP.Button(d, bw, AP.C_TEXT .. Loc("allies.res.cancel") .. "|r")
		at(cancel, w - 0.015 - bw * 2 - AP.GAP, -0.122)
		AP.OnEvent(cancel, FRAMEEVENT_CONTROL_CLICK, function(v) AP.resTarget[v] = nil end)
		local send = AP.Button(d, bw, AP.C_POS .. Loc("allies.res.send") .. "|r")
		AP.dialogSend = send
		at(send, w - 0.015 - bw, -0.122)
		AP.OnEvent(send, FRAMEEVENT_CONTROL_CLICK, function(v)
			local t = AP.resTarget[v]
			AP.resTarget[v] = nil
			if t ~= nil and AP.open[v] and AP.Has(AP.Actions(v, t), "res") then
				AP.SendResources(v, t, AP.sendG[v], AP.sendL[v])
			end
		end)
		FrameSetShown(d, false)
	end

	function AP.CreateToast(parent)
		local w, h = 0.36, 0.07
		local box = BlzCreateFrame("BoxedTextBackgroundTemplate", parent, 0, 0)
		AP.toast = box
		BlzFrameSetLevel(box, 5)
		BlzFrameSetSize(box, w, h)
		FrameSetAbsPoint(box, FRAMEPOINT_TOP, 0.4, AP.TOP)
		local block = BlzCreateFrameByType("BUTTON", "AlliesToastBlocker", box, "", 0)
		BlzFrameSetAllPoints(block, box)
		local function at(f, x, y, point) BlzFrameSetPoint(f, point or FRAMEPOINT_TOPLEFT, box, FRAMEPOINT_TOPLEFT, x, y) end
		AP.toastSwatch = BlzCreateFrameByType("BACKDROP", "AlliesToastSwatch", box, "", 0)
		BlzFrameSetSize(AP.toastSwatch, 0.011, 0.011)
		at(AP.toastSwatch, 0.012, -0.012)
		local title = AP.Text(box, "HudText", 0.15, 0.012)
		at(title, 0.028, -0.011)
		BlzFrameSetText(title, AP.C_POS .. Loc("allies.toast.title") .. "|r")
		AP.toastBody = AP.Text(box, "HudBody", w - 0.024, 0.014)
		at(AP.toastBody, 0.012, -0.031)
		local bw = 0.07
		local accept = AP.Button(box, bw, AP.C_POS .. Loc("allies.act.accept") .. "|r")
		at(accept, w - 0.012 - bw * 2 - AP.GAP, -0.009)
		local decline = AP.Button(box, bw, AP.C_NEG .. Loc("allies.act.decline") .. "|r")
		at(decline, w - 0.012 - bw, -0.009)
		AP.toastAccept, AP.toastDecline = accept, decline
		AP.OnEvent(accept, FRAMEEVENT_CONTROL_CLICK, function(v)
			local from = AP.OldestIncoming(v)
			if from ~= nil then AP.Accept(v, from) end
		end)
		AP.OnEvent(decline, FRAMEEVENT_CONTROL_CLICK, function(v)
			local from = AP.OldestIncoming(v)
			if from ~= nil then AP.Decline(v, from) end
		end)
		AP.toastBarW = w - 0.024
		AP.toastBar = BlzCreateFrameByType("BACKDROP", "AlliesToastBar", box, "", 0)
		BlzFrameSetTexture(AP.toastBar, string.format(AP.TEAM_TEX, 6), 0, true)
		BlzFrameSetSize(AP.toastBar, AP.toastBarW, 0.002)
		at(AP.toastBar, 0.012, -0.050)
		AP.toastTimer = AP.Text(box, "HudText", w - 0.024, 0.011)
		at(AP.toastTimer, 0.012, -0.055)
		FrameSetShown(box, false)
	end

	-- Подпись кнопки верхней панели: название и горячая клавиша в скобках.
	function AP.UpperLabel(key, hot)
		return AP.C_TEXT .. Loc(key) .. " [" .. AP.C_NAME .. hot .. AP.C_TEXT .. "]|r"
	end

	-- Остальные кнопки верхней панели остаются нативными (клики, F9/F10/F12,
	-- подсказки), сверху — подложка с подписью в стиле кнопки «Союзники».
	-- Подложка и текст мышь не перехватывают.
	AP.UPPER = {
		{ kind = "menu", key = "ui.upper.menu", hot = "F10" },
		{ kind = "quests", key = "ui.upper.quests", hot = "F9" },
		{ kind = "chat", key = "ui.upper.chat", hot = "F12" },
	}

	function AP.CreateUpper(parent)
		AP.upper = {}
		for i = 1, #AP.UPPER do
			local u = AP.UPPER[i]
			local look = BlzCreateFrameByType("BACKDROP", "AlliesUpperLook", parent, "TasButtonLookTemplate", 0)
			local text = BlzCreateFrame("HudText", look, 0, 0)
			BlzFrameSetAllPoints(text, look)
			BlzFrameSetTextAlignment(text, TEXT_JUSTIFY_MIDDLE, TEXT_JUSTIFY_CENTER)
			BlzFrameSetText(text, AP.UpperLabel(u.key, u.hot))
			BlzFrameSetEnable(text, false)
			FrameSetShown(look, false)
			AP.upper[u.kind] = look
		end
	end

	function AP.PlaceUpper()
		if AP.upper == nil then return end
		for i = 1, #AP.UPPER do
			local kind = AP.UPPER[i].kind
			local look, s = AP.upper[kind], AP.upperSlot[kind]
			if s ~= nil then
				BlzFrameSetSize(look, s.w, s.h)
				FrameSetAbsPoint(look, FRAMEPOINT_TOPLEFT, s.x, s.y)
			end
			FrameSetShown(look, s ~= nil and AP.uiShown)
		end
	end

	-- Вызывается из UISetup: координаты нативной кнопки kind (menu/quests/chat).
	function AlliesPanelPlaceUpper(kind, x, y, w, h)
		AP.upperSlot[kind] = { x = x, y = y, w = w, h = h }
		if AlliesPanelActive then AP.PlaceUpper() end
	end

	-- Кнопка «Союзники» на месте стандартной (координаты задаёт UISetup).
	function AP.PlaceButton()
		if AP.button == nil or AP.slot == nil then return end
		local s = AP.slot
		BlzFrameSetSize(AP.button, s.w, s.h)
		FrameSetAbsPoint(AP.button, FRAMEPOINT_TOPLEFT, s.x, s.y)
		if s.native ~= nil then BlzFrameSetVisible(s.native, false) end
		FrameSetShown(AP.button, AP.uiShown)
	end

	-- Вызывается из UISetup на каждом проходе: нативную кнопку только скрываем.
	function AlliesPanelPlaceButton(native, x, y, w, h)
		AP.slot = { native = native, x = x, y = y, w = w, h = h }
		if AlliesPanelActive then AP.PlaceButton() end
	end

	-- Стандартный интерфейс скрыт (выбор расы, панель хоста): прячем и окно. Локально.
	function AlliesPanelSetUIShown(show)
		AP.uiShown = show
		if AP.root == nil then return end
		FrameSetShown(AP.button, show)
		AP.PlaceUpper()
		AP.Render()
	end

	-- Создаёт окно у всех клиентов одинаково. false — шаблоны не загрузились,
	-- тогда остаётся стандартное окно союзов.
	function AlliesPanel_Create()
		if AP.root ~= nil then return true end
		if not BlzLoadTOCFile("war3mapimported\\HudText.toc") or not BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
			or not BlzLoadTOCFile("war3mapimported\\TasItemShop.toc") then
			ProbeLogWrite("[ALLIES] templates not loaded, keeping native allies dialog")
			return false
		end
		AP.force = CreateForce()
		AP.selfInEnum = AP.EnumAllies(0) > AP.OtherAllies(0)
		for pi = 0, 23 do AP.seen[pi] = AP.IsParticipant(pi) or nil end
		AP.uiShown = not StandardUIHidden

		local parent = BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0)
		AP.root = BlzCreateFrame("BoxedTextBackgroundTemplate", parent, 0, 0)
		BlzFrameSetLevel(AP.root, 4)
		AP.measure = BlzCreateFrame("HudText", AP.root, 0, 0)
		BlzFrameSetAbsPoint(AP.measure, FRAMEPOINT_TOPLEFT, 0.0, FRAME_PARK_Y)
		BlzFrameSetAlpha(AP.measure, 0)
		BlzFrameSetEnable(AP.measure, false)
		local innerW = AP.W - AP.PAD * 2
		-- Подложка ловит колесо мыши и не пропускает клики в мир под окном.
		local block = BlzCreateFrameByType("BUTTON", "AlliesPanelBlocker", AP.root, "", 0)
		BlzFrameSetAllPoints(block, AP.root)
		AP.OnWheel(block)

		local title = AP.Text(AP.root, "HudTitle", 0.3, 0.022)
		AP.At(title, AP.PAD, -AP.PAD)
		BlzFrameSetText(title, AP.C_NAME .. Loc("allies.title") .. "|r")
		local close = AP.Button(AP.root, 0.022, AP.C_TEXT .. "×|r")
		BlzFrameSetSize(close, 0.022, 0.022)
		AP.At(close, AP.W - AP.PAD, -AP.PAD, FRAMEPOINT_TOPRIGHT)
		AP.OnEvent(close, FRAMEEVENT_CONTROL_CLICK, function(v)
			AP.open[v] = nil
			AP.resTarget[v] = nil
		end)
		AP.chips = AP.Text(AP.root, "HudText", innerW, 0.016)
		AP.At(AP.chips, AP.PAD, -(AP.PAD + 0.022 + 0.006))

		local y = AP.CreateRows(innerW)
		y = AP.CreateBottom(y - 0.01, innerW)
		local height = -y + AP.PAD
		BlzFrameSetSize(AP.root, AP.W, height)
		FrameSetAbsPoint(AP.root, FRAMEPOINT_TOPLEFT, AP.LEFT, AP.TOP)
		AP.CreateDialog(-(AP.PAD + 0.07))
		FrameSetShown(AP.measure, false)
		FrameSetShown(AP.root, false)

		AP.CreateToast(parent)
		local text
		AP.button, text = AP.Button(parent, 0.084, "")
		AP.buttonText = text
		AP.OnEvent(AP.button, FRAMEEVENT_CONTROL_CLICK, AP.Toggle)

		local key = CreateTrigger()
		for pi = 0, 23 do BlzTriggerRegisterPlayerKeyEvent(key, Player(pi), OSKEY_F11, 0, true) end
		TriggerAddAction(key, function()
			AP.Toggle(GetPlayerId(GetTriggerPlayer()))
			AP.Render()
		end)
		-- ESC закрывает сначала окно передачи ресурсов, затем само окно.
		local esc = CreateTrigger()
		for pi = 0, 23 do BlzTriggerRegisterPlayerKeyEvent(esc, Player(pi), OSKEY_ESCAPE, 0, true) end
		TriggerAddAction(esc, function()
			local v = GetPlayerId(GetTriggerPlayer())
			if not AP.open[v] then return end
			if AP.resTarget[v] ~= nil then
				AP.resTarget[v] = nil
			else
				AP.Toggle(v)
			end
			AP.Render()
		end)

		-- Подложки «Меню» и «Журнала» стоят левее области 4:3 (x < 0), как и нативные
		-- кнопки: вне её движок пускает только потомков ConsoleUIBackdrop.
		AP.CreateUpper(BlzGetFrameByName("ConsoleUIBackdrop", 0) or parent)
		AlliesPanelActive = true
		AP.PlaceButton()
		AP.PlaceUpper()
		TimerStart(CreateTimer(), AP.TICK, true, AP.Tick)
		AP.Render()
		ProbeLogWrite("[ALLIES] panel created")
		return true
	end

	-- Для тестов и моста: доступ к внутреннему состоянию.
	AlliesPanelState = AP
end
