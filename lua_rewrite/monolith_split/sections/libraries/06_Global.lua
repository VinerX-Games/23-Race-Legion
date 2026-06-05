-- library Global:
-- ==========================================
---@param x real
---@param y real
---@return real
function GetPosZ(x, y)
	MoveLocation(Global_TempLoc, x, y)
	return GetLocationZ(Global_TempLoc)
end
---@param u unit
---@return real
function GetUnitZ(u)
	return GetPosZ(GetUnitX(u), GetUnitY(u)) + GetUnitFlyHeight(u)
end
---@param u unit
---@param z real
---@return nothing
function SetUnitZ(u, z)
	SetUnitFlyHeight(u, z - GetPosZ(GetUnitX(u), GetUnitY(u)), 0)
end
---@param x1 real
---@param y1 real
---@param x2 real
---@param y2 real
---@return real
function DistanceBetweenCoords(x1, y1, x2, y2)
	return SquareRoot(Pow(x2 - x1, 2) + Pow(y2 - y1, 2))
end
---@param w widget
---@param x real
---@param y real
---@return real
function DistanceBetweenWidgetAndCoords(w, x, y)
	return SquareRoot(Pow(x - GetWidgetX(w), 2) + Pow(y - GetWidgetY(w), 2))
end
---@param x real
---@param y real
---@param w widget
---@return real
function DistanceBetweenCoordsAndWidget(x, y, w)
	return SquareRoot(Pow(GetWidgetX(w) - x, 2) + Pow(GetWidgetY(w) - y, 2))
end
---@param w1 widget
---@param w2 widget
---@return real
function DistanceBetweenWidgets(w1, w2)
	return SquareRoot(Pow(GetWidgetX(w2) - GetWidgetX(w1), 2) + Pow(GetWidgetY(w2) - GetWidgetY(w1), 2))
end
---@param x1 real
---@param y1 real
---@param x2 real
---@param y2 real
---@return real
function AngleBetweenCoords(x1, y1, x2, y2)
	return Atan2(y2 - y1, x2 - x1) * bj_RADTODEG
end
---@param w widget
---@param x real
---@param y real
---@return real
function AngleBetweenWidgetAndCoords(w, x, y)
	return Atan2(y - GetWidgetY(w), x - GetWidgetX(w)) * bj_RADTODEG
end
---@param x real
---@param y real
---@param w widget
---@return real
function AngleBetweenCoordsAndWidget(x, y, w)
	return Atan2(GetWidgetY(w) - y, GetWidgetX(w) - x) * bj_RADTODEG
end
---@param w1 widget
---@param w2 widget
---@return real
function AngleBetweenWidgets(w1, w2)
	return Atan2(GetWidgetY(w2) - GetWidgetY(w1), GetWidgetX(w2) - GetWidgetX(w1)) * bj_RADTODEG
end
---@param x real
---@param d real
---@param a real
---@return real
function PolarProjectionX(x, d, a)
	return x + d * Cos(a * bj_DEGTORAD)
end
---@param x real
---@param d real
---@param a real
---@return real
function PolarProjectionY(x, d, a)
	return x + d * Sin(a * bj_DEGTORAD)
end
---@param a real
---@param b real
---@return real
function AngleDifference(a, b)
	local r
	if a > 180 then
		a = a - 360
	elseif a < -180 then
		a = a + 360
	end
	if b > 180 then
		b = b - 360
	elseif b < -180 then
		b = b + 360
	end
	r = RMaxBJ(a, b) - RMinBJ(a, b)
	return RMinBJ(r, 360 - r)
end
---@param c1 real
---@param c2 real
---@param t real
---@return real
function BezierCurves_2C(c1, c2, t)
	local u = 1 - t
	return c1 * u + c2 * t
end
---@param c1 real
---@param c2 real
---@param c3 real
---@param t real
---@return real
function BezierCurves_3C(c1, c2, c3, t)
	local u = 1 - t
	return c1 * u * u + c2 * 2 * t * u + c3 * t * t
end
---@param c1 real
---@param c2 real
---@param c3 real
---@param c4 real
---@param t real
---@return real
function BezierCurves_4C(c1, c2, c3, c4, t)
	local u = 1 - t
	return c1 * u * u * u + c2 * 3 * t * u * u + c3 * 3 * t * t * u + c4 * t * t * t
end
-- ==========================================
---@param u unit
---@return boolean
function AvalibleUnit(u)
	return  not IsUnitType(u, UNIT_TYPE_STRUCTURE) and  not IsUnitType(u, UNIT_TYPE_ANCIENT) and UnitAlive(u)
end
---@param s unit
---@param u unit
---@return boolean
function AvalibleUnitAlly(s, u)
	return IsUnitAlly(u, GetOwningPlayer(s)) and AvalibleUnit(u)
end
---@param s unit
---@param u unit
---@return boolean
function AvalibleUnitEnemy(s, u)
	return IsUnitEnemy(u, GetOwningPlayer(s)) and AvalibleUnit(u)
end
---@return nothing
function Global___GroupCountUnitsEnum()
	Global___TempIntArray[1] = Global___TempIntArray[1] + 1
end
---@param g group
---@return integer
function GroupCountUnits(g)
	Global___TempIntArray[1] = 0
	ForGroup(g, Global___GroupCountUnitsEnum)
	return Global___TempIntArray[1]
end
---@return nothing
function Global___GroupRandomUnitEnum()
	Global___TempIntArray[1] = Global___TempIntArray[1] + 1
	if Global___TempIntArray[1] == Global___TempIntArray[2] then
		Global___TempUnitArray[1] = GetEnumUnit()
	end
end
---@param g group
---@return unit
function GroupRandomUnit(g)
	Global___TempIntArray[2] = GetRandomInt(1, GroupCountUnits(g))
	Global___TempIntArray[1] = 0
	Global___TempUnitArray[1] = nil
	ForGroup(g, Global___GroupRandomUnitEnum)
	return Global___TempUnitArray[1]
end
---@return nothing
function Global___KillDestructablesInRangeEnum()
	if DistanceBetweenWidgetAndCoords(GetEnumDestructable(), Global___TempRealArray[1], Global___TempRealArray[2]) <= Global___TempRealArray[3] then
		KillDestructable(GetEnumDestructable())
	end
end
---@param x real
---@param y real
---@param r real
---@param b boolexpr
---@return nothing
function KillDestructablesInRange(x, y, r, b)
	Global___TempRealArray[1] = x
	Global___TempRealArray[2] = y
	Global___TempRealArray[3] = r
	SetRect(Global_TempRect, Global___TempRealArray[1] - r, Global___TempRealArray[2] - r, Global___TempRealArray[1] + r, Global___TempRealArray[2] + r)
	EnumDestructablesInRect(Global_TempRect, b, Global___KillDestructablesInRangeEnum)
end
---@param i integer
---@return boolean
function InterruptOrderCheck(i)
	if i == 852002 or i == 852003 or i == 852004 or i == 852005 or i == 852006 or i == 852007 or i == 852537 or i > 1000000 then
		return false
	end
	return true
end
---@param u unit
---@param id integer
---@return boolean
function UnitAddPowerUpItem(u, id)
	local it
	local invAdded = false
	local added = true
	it = CreateItem(id, GetUnitX(u), GetUnitY(u))
	if GetUnitAbilityLevel(u, FourCC('AInv')) == 0 then	-- AInv -> Inventory
		invAdded = true
		UnitAddAbility(u, FourCC('AInv'))	-- AInv -> Inventory
	end
	if UnitAddItem(u, it) == false then
		added = false
	elseif GetWidgetLife(it) > 0.00 then
		added = false
	end
	RemoveItem(it)
	if invAdded then
		UnitRemoveAbility(u, FourCC('AInv'))	-- AInv -> Inventory
	end
	it = nil
	return added
end
-- ==========================================
---@param this integer
---@return nothing
function s__StackTemplate_destroy(this)
	if s__StackTemplate_NOW[this] > 0 then
		s__StackTemplate_STACK[s__StackTemplate_NOWthis] = s__StackTemplate_STACK[s__StackTemplate_COUNT]
		s__StackTemplate_NOW[s__StackTemplate_STACKs__StackTemplate_NOWthis] = s__StackTemplate_NOW[this]
		s__StackTemplate_STACK[s__StackTemplate_COUNT] = 0
		s__StackTemplate_COUNT = s__StackTemplate_COUNT - 1
	end
	s__StackTemplate_deallocate(this)
end
---@return integer
function s__StackTemplate_create()
	local this = s__StackTemplate__allocate()
	s__StackTemplate_COUNT = s__StackTemplate_COUNT + 1
	s__StackTemplate_STACK[s__StackTemplate_COUNT] = this
	s__StackTemplate_NOW[s__StackTemplate_STACKs__StackTemplate_COUNT] = s__StackTemplate_COUNT
	return this
end
-- ==========================================
---@return nothing
function Global___Init()
	TimerStart(Global_Timer, 999999, false, nil)
end
-- library Global ends
