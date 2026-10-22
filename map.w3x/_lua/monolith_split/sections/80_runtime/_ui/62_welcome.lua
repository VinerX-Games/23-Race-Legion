-- ***************************************************************************
-- *  WelcomePanel
-- Greeting shown in the middle of the screen at the start of the lobby.
-- Presentation only; closing it is local to the player who clicked.
local WELCOME_DISCORD = "discord.gg/UV5tbXXunU"
local WELCOME_LOGO = "war3mapImported\\23RaceForeverLogo.tga"
local WELCOME_LOGO_W, WELCOME_LOGO_H = 0.24, 0.101   -- texture is 600x253
local WELCOME_W = 0.36
local WELCOME_HOLD = 10       -- seconds fully visible
local WELCOME_FADE = 3        -- seconds of fade-out
local WELCOME_BODY_H = 0.058   -- two short paragraphs at HudBody size

local welcome, welcomeLink

-- Map version, taken from the map name ("23 Race Forever 1.6.NNN") so it has one source.
local function WelcomeVersion()
	local name = GetLocalizedString("TRIGSTR_003") or ""
	return string.match(name, "(%d+%.%d+%.%d+)") or "—"
end

local function WelcomeHide()
	FrameSetShown(welcome, false)
end

function ShowWelcomePanel()
	if welcome ~= nil then return end
	if not BlzLoadTOCFile("war3mapimported\\Templates.toc") or not BlzLoadTOCFile("war3mapimported\\HudText.toc") then
		ProbeLogWrite("[WELCOME] templates not loaded")
		return
	end
	BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
	local parent = BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0)
	welcome = BlzCreateFrame("BoxedTextBackgroundTemplate", parent, 0, 700)
	BlzFrameSetLevel(welcome, 10)

	local y = -0.014
	if WELCOME_LOGO ~= nil then
		local logo = BlzCreateFrameByType("BACKDROP", "WelcomeLogo", welcome, "", 0)
		BlzFrameSetTexture(logo, WELCOME_LOGO, 0, true)
		BlzFrameSetSize(logo, WELCOME_LOGO_W, WELCOME_LOGO_H)
		BlzFrameSetPoint(logo, FRAMEPOINT_TOP, welcome, FRAMEPOINT_TOP, 0, y)
		y = y - WELCOME_LOGO_H - 0.008
	end

	local title = BlzCreateFrame("HudTitle", welcome, 0, 701)
	BlzFrameSetTextAlignment(title, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_CENTER)
	BlzFrameSetSize(title, WELCOME_W - 0.02, 0.02)
	BlzFrameSetPoint(title, FRAMEPOINT_TOP, welcome, FRAMEPOINT_TOP, 0, y)
	BlzFrameSetText(title, Loc("lua.auto_5af126ac29237012"))
	BlzFrameSetEnable(title, false)
	y = y - 0.026

	local body = BlzCreateFrame("HudBody", welcome, 0, 702)
	BlzFrameSetTextAlignment(body, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
	BlzFrameSetSize(body, WELCOME_W - 0.03, WELCOME_BODY_H)
	BlzFrameSetPoint(body, FRAMEPOINT_TOPLEFT, welcome, FRAMEPOINT_TOPLEFT, 0.015, y)
	BlzFrameSetText(body, Loc("lua.auto_10d2294a0945e72b")
		.. Loc("lua.auto_4fc761f6b9fabde4")
		.. Loc("lua.auto_89204bd7b2a4d0a2"))
	BlzFrameSetEnable(body, false)
	y = y - WELCOME_BODY_H - 0.004

	-- Edit box: the link can be selected and copied with Ctrl+C. Edits are undone.
	welcomeLink = BlzCreateFrame("EscMenuEditBoxTemplate", welcome, 0, 703)
	BlzFrameSetSize(welcomeLink, 0.2, 0.03)
	BlzFrameSetPoint(welcomeLink, FRAMEPOINT_TOP, welcome, FRAMEPOINT_TOP, 0, y)
	BlzFrameSetText(welcomeLink, WELCOME_DISCORD)
	local guard = CreateTrigger()
	BlzTriggerRegisterFrameEvent(guard, welcomeLink, FRAMEEVENT_EDITBOX_TEXT_CHANGED)
	TriggerAddAction(guard, function()
		if GetTriggerPlayer() == GetLocalPlayer() and BlzGetTriggerFrameText() ~= WELCOME_DISCORD then
			BlzFrameSetText(welcomeLink, WELCOME_DISCORD)
		end
	end)
	y = y - 0.03 - 0.008

	local version = BlzCreateFrame("HudBody", welcome, 0, 704)
	BlzFrameSetTextAlignment(version, TEXT_JUSTIFY_TOP, TEXT_JUSTIFY_LEFT)
	BlzFrameSetSize(version, WELCOME_W - 0.03, 0.016)
	BlzFrameSetPoint(version, FRAMEPOINT_TOPLEFT, welcome, FRAMEPOINT_TOPLEFT, 0.015, y)
	BlzFrameSetText(version, Loc("lua.auto_ac18f75e920230db") .. WelcomeVersion() .. "|r")
	BlzFrameSetEnable(version, false)
	y = y - 0.018

	local close = BlzCreateFrame("ScriptDialogButton", welcome, 0, 705)
	BlzFrameSetSize(close, 0.09, 0.028)
	BlzFrameSetPoint(close, FRAMEPOINT_TOP, welcome, FRAMEPOINT_TOP, 0, y)
	BlzFrameSetText(close, Loc("lua.auto_a7a4033657e89fc9"))
	local onClose = CreateTrigger()
	BlzTriggerRegisterFrameEvent(onClose, close, FRAMEEVENT_CONTROL_CLICK)
	TriggerAddAction(onClose, function()
		if GetTriggerPlayer() == GetLocalPlayer() then WelcomeHide() end
	end)
	y = y - 0.028 - 0.012

	BlzFrameSetSize(welcome, WELCOME_W, -y)
	FrameSetAbsPoint(welcome, FRAMEPOINT_CENTER, 0.4, 0.37)
	FrameSetShown(welcome, true)
	-- Hold, then fade out and hide.
	local step, steps = 0, R2I(WELCOME_FADE / 0.05)
	TimerStart(CreateTimer(), WELCOME_HOLD, false, function()
		TimerStart(GetExpiredTimer(), 0.05, true, function()
			step = step + 1
			if step >= steps then
				WelcomeHide()
				DestroyTimer(GetExpiredTimer())
				return
			end
			BlzFrameSetAlpha(welcome, R2I(255 * (1 - step / steps)))
		end)
	end)
end
