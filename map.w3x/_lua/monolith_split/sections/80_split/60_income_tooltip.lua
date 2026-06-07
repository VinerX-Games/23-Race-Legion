-- *  IncomeTooltip
---@return nothing
function Face2()
	
	
	BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
	face = BlzCreateFrameByType("BACKDROP", "Face", BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0), "", 0)
	faceHover = BlzCreateFrameByType("FRAME", "FaceFrame", face, "", 0)
	IncomeTextFr = BlzCreateFrameByType("TEXT", "MyTextFrame", BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0), "", 0)
	tooltip = BlzCreateFrame("BoxedText", face, 0, 0)
	tooltipBody = BlzGetFrameByName("BoxedTextValue", 0)
	tooltipTitle = BlzGetFrameByName("BoxedTextTitle", 0)
	BlzFrameSetText(IncomeTextFr, "999999")
	BlzFrameSetAbsPoint(IncomeTextFr, FRAMEPOINT_TOPRIGHT, 0.2337, 0.5937)
	BlzFrameSetEnable(IncomeTextFr, false)
	BlzFrameSetScale(IncomeTextFr, 1.075)
	BlzFrameSetTextAlignment(IncomeTextFr, TEXT_JUSTIFY_CENTER, TEXT_JUSTIFY_LEFT)
	BlzFrameSetAllPoints(faceHover, face)
	BlzFrameSetTooltip(faceHover, tooltip)
	
	BlzFrameSetSize(face, 0.085, 0.015)
	BlzFrameSetAbsPoint(face, FRAMEPOINT_TOPRIGHT, 0.239, 0.5965)
	BlzFrameSetAbsPoint(tooltip, FRAMEPOINT_TOPRIGHT, 0.289, 0.5685)
	BlzFrameSetPoint(tooltip, FRAMEPOINT_BOTTOM, face, FRAMEPOINT_TOP, 0.0, -0.1)
	BlzFrameSetSize(tooltip, 0.03, 0.03)
	
	BlzFrameSetText(tooltipBody, "????? = ??????-???????")
	BlzFrameSetText(tooltipTitle, "?????")
	
	BlzFrameSetTexture(face, "ResourceBar222.tga", 0, true)
	
end
--  scope init2 begins
---@return nothing
function init2___Init()
	Face2()
end
--  scope init2 ends
-- ***************************************************************************
