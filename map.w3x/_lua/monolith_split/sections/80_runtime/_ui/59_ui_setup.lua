
-- ***************************************************************************
-- *  PlayerUI
local imageTest
local minimapBorder
local commandBorder

---@return nothing
function UISetup()
	-- Local Variables
	local consoleBackdrop = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	local upperButtonBar = BlzGetFrameByName("UpperButtonBarFrame", 0)
	ProbeLogWrite("[UI] ConsoleUIBackdrop=" .. tostring(consoleBackdrop ~= nil) .. " UpperButtonBarFrame=" .. tostring(upperButtonBar ~= nil))
	if consoleBackdrop == nil or upperButtonBar == nil then
		ProbeLogWrite("[UI] skipped: required frames missing")
		return
	end
	local fh
	local chatButton
	local questButton
	local allyButton
	local MiniMap
	local gridButtons
	imageTest = imageTest or BlzCreateFrameByType("BACKDROP", "image", consoleBackdrop, "ButtonBackdropTemplate", 0)
	
	-- Top UI & System Buttons
	fh = upperButtonBar
	BlzFrameSetVisible(fh, true)
	allyButton = BlzGetFrameByName("UpperButtonBarAlliesButton", 0)
	fh = BlzGetFrameByName("UpperButtonBarMenuButton", 0)
	chatButton = BlzGetFrameByName("UpperButtonBarChatButton", 0)
	questButton = BlzGetFrameByName("UpperButtonBarQuestsButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameClearAllPoints(allyButton)
	BlzFrameClearAllPoints(chatButton)
	BlzFrameClearAllPoints(questButton)
	BlzFrameSetAbsPoint(questButton, FRAMEPOINT_TOPLEFT, 0.05, 0.6)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPLEFT, -0.03, 0.6)
	BlzFrameSetAbsPoint(allyButton, FRAMEPOINT_TOPLEFT, 0.05, 0.583)
	BlzFrameSetAbsPoint(chatButton, FRAMEPOINT_TOPLEFT, -0.03, 0.583)
	
	-- Hiding clock UI and creating new frame bar
	BlzFrameSetTexture(imageTest, "UI\\ResourceBar.tga", 0, true)
	BlzFrameSetPoint(imageTest, FRAMEPOINT_TOP, BlzGetOriginFrame(ORIGIN_FRAME_WORLD_FRAME, 0), FRAMEPOINT_TOP, 0, 0)
	BlzFrameSetSize(imageTest, 0.52, 0.025)
	BlzFrameSetLevel(imageTest, 1)
	
	-- Food
	fh = BlzGetFrameByName("ResourceBarSupplyText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.640, 0.5965)
	
	-- Upkeep
	fh = BlzGetFrameByName("ResourceBarUpkeepText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.8, 0.6965)
	
	-- Gold
	fh = BlzGetFrameByName("ResourceBarGoldText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.329, 0.5965)
	
	-- Lumber
	fh = BlzGetFrameByName("ResourceBarLumberText", 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.546, 0.5965)
	
	-- Bottom UI & Idle Worker Icon
	
	-- set fh = BlzGetFrameByName("ConsoleUI", 0)
	-- set fh = BlzFrameGetChild(fh, 7)
	fh = BlzGetFrameByName("ConsoleBottomBar", 0)
	if fh ~= nil then
		fh = BlzFrameGetChild(fh, 3)
		if fh ~= nil then
			fh = BlzFrameGetChild(fh, 0)
			if fh ~= nil then
				BlzFrameClearAllPoints(fh)
				BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.09, 0.179)
			end
		end
	end
	
	-- Remove Deadspace
	fh = BlzGetFrameByName("ConsoleUI", 0)
	BlzFrameSetVisible(BlzFrameGetChild(fh, 5), false)
	
	-- Minimap
	MiniMap = BlzGetFrameByName("MiniMapFrame", 0)
	BlzFrameSetVisible(MiniMap, true)
	BlzFrameClearAllPoints(MiniMap)
	BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_BOTTOMLEFT, 0.0525, 0.0)
	BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_TOPRIGHT, 0.2125, 0.141)
	
	-- Minimap Buttons
	fh = BlzGetFrameByName("MiniMapCreepButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.214, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.234, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MiniMapAllyButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.234, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.254, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MiniMapTerrainButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.254, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.274, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	fh = BlzGetFrameByName("MinimapSignalButton", 0)
	BlzFrameSetVisible(fh, false)
	fh = BlzGetFrameByName("FormationButton", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.274, 0.116)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.294, 0.136)
	BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
	
	-- Minimap Border
	minimapBorder = minimapBorder or BlzCreateFrameByType("BACKDROP", "MinimapBorder", MiniMap, "", 0)
	fh = minimapBorder
	BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, MiniMap, FRAMEPOINT_TOPLEFT, 0, 0)
	BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, MiniMap, FRAMEPOINT_BOTTOMRIGHT, 0, 0)
	BlzFrameSetTexture(fh, "UI\\MiniMapBorder.dds", 0, true)
	
	-- Tooltips
	fh = BlzGetOriginFrame(ORIGIN_FRAME_TOOLTIP, 0)
	BlzFrameSetVisible(fh, true)
	fh = BlzGetOriginFrame(ORIGIN_FRAME_UBERTOOLTIP, 0)
	BlzFrameSetVisible(fh, true)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMRIGHT, 0.7725, 0.141)
	
	-- Command Buttons
	gridButtons = BlzGetFrameByName("CommandBarFrame", 0)
	BlzFrameSetVisible(gridButtons, true)
	BlzFrameClearAllPoints(gridButtons)
	BlzFrameSetAbsPoint(gridButtons, FRAMEPOINT_BOTTOMLEFT, 0.5950, 0.005)
	
	-- Backdrop
	fh = BlzGetFrameByName("ConsoleUIBackdrop", 0)
	BlzFrameClearAllPoints(fh)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.052, 0)
	BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.770, 0.141)
	
	-- Command buttons border
	commandBorder = commandBorder or BlzCreateFrameByType("BACKDROP", "CommandBorder", MiniMap, "", 0)
	fh = commandBorder
	BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, gridButtons, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
	BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, gridButtons, FRAMEPOINT_BOTTOMRIGHT, 0.0025, -0.005)
	BlzFrameSetTexture(fh, "UI\\CommandCard.dds", 0, true)
	
	--  Prevent multiplayer desyncs by forcing the creation of the QuestDialog frame
	-- 	call BlzFrameClick(BlzGetFrameByName("UpperButtonBarQuestsButton", 0))
	-- 	call ForceUICancel()
	
	--  Expand TextArea
	local questDisplay = BlzGetFrameByName("QuestDisplay", 0)
	local questTitle = BlzGetFrameByName("QuestDetailsTitle", 0)
	local questDisplayBackdrop = BlzGetFrameByName("QuestDisplayBackdrop", 0)
	local questBackdrop = BlzGetFrameByName("QuestBackdrop", 0)
	local questAcceptButton = BlzGetFrameByName("QuestAcceptButton", 0)
	if questDisplay ~= nil and questTitle ~= nil and questDisplayBackdrop ~= nil then
		BlzFrameSetPoint(questDisplay, FRAMEPOINT_TOPLEFT, questTitle, FRAMEPOINT_BOTTOMLEFT, 0.003, -0.003)
		BlzFrameSetPoint(questDisplay, FRAMEPOINT_BOTTOMRIGHT, questDisplayBackdrop, FRAMEPOINT_BOTTOMRIGHT, -0.003, 0.)
	end
	
	--  Relocate button
	if questDisplayBackdrop ~= nil and questBackdrop ~= nil then
		BlzFrameSetPoint(questDisplayBackdrop, FRAMEPOINT_BOTTOM, questBackdrop, FRAMEPOINT_BOTTOM, 0., 0.017)
	end
	if questAcceptButton ~= nil and questBackdrop ~= nil then
		BlzFrameClearAllPoints(questAcceptButton)
		BlzFrameSetPoint(questAcceptButton, FRAMEPOINT_TOPRIGHT, questBackdrop, FRAMEPOINT_TOPRIGHT, -0.016, -0.016)
		BlzFrameSetText(questAcceptButton, "×")
		BlzFrameSetSize(questAcceptButton, 0.03, 0.03)
	end
	
	--  Add back ally resource icons
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyGoldIcon", 7), "UI\\RGReplacement.dds", 0, false)
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyWoodIcon", 7), "UI\\RLReplacement.dds", 0, false)
	BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyFoodIcon", 7), "UI\\RSReplacement.dds", 0, false)
	
end
--  scope init begins
---@return nothing
function init___Init()
	UISetup()
end
