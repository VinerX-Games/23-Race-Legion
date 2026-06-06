-- library SanctifiedEnchantment:
--  ===============================================================
-- Implemented from module BindTemplate:
---@param h handle
---@param i integer
---@param s integer
---@return nothing
function s__SanctifiedEnchantment_Save(h, i, s)
	SaveInteger(Global_Hash, GetHandleId(h), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + i, s)
end
---@param this integer
---@param h handle
---@param i integer
---@return nothing
function s__SanctifiedEnchantment_SaveThis(this, h, i)
	SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i), (this))	--  INLINED!!
end
---@param h handle
---@param i integer
---@return integer
function s__SanctifiedEnchantment_Load(h, i)
	return LoadInteger(Global_Hash, GetHandleId(h), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + i)
end
---@param h handle
---@param i integer
---@return nothing
function s__SanctifiedEnchantment_Flush(h, i)
	SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i), (0))	--  INLINED!!
end
---@param h handle
---@param s integer
---@return nothing
function s__SanctifiedEnchantment_SaveUnique(h, s)
	SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (-1), (s))	--  INLINED!!
end
---@param this integer
---@param h handle
---@return nothing
function s__SanctifiedEnchantment_SaveThisUnique(this, h)
	SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (-1), ((this)))	--  INLINED!!
end
---@param h handle
---@return integer
function s__SanctifiedEnchantment_LoadUnique(h)
	return (LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (-1)))	--  INLINED!!
end
---@param h handle
---@return nothing
function s__SanctifiedEnchantment_FlushUnique(h)
	SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + ((-1)), (0))	--  INLINED!!
end
---@param h handle
---@param c integer
---@return nothing
function s__SanctifiedEnchantment_BindTemplate___SetCount(h, c)
	SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0), (c))	--  INLINED!!
end
---@param h handle
---@return integer
function s__SanctifiedEnchantment_GetCount(h)
	return (LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0)))	--  INLINED!!
end
---@param h handle
---@param s integer
---@return nothing
function s__SanctifiedEnchantment_Add(h, s)
	local c = (LoadInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0))) + 1	--  INLINED!!
	if c < JASS_MAX_ARRAY_SIZE then
		SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (c), (s))	--  INLINED!!
		SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0), ((c)))	--  INLINED!!
	end
end
---@param this integer
---@param h handle
---@return nothing
function s__SanctifiedEnchantment_AddThis(this, h)
	s__SanctifiedEnchantment_Add(h, this)
end
---@param h handle
---@param s integer
---@return nothing
function s__SanctifiedEnchantment_Remove(h, s)
	local c = (LoadInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0)))	--  INLINED!!
	local i = c
	while true do
		if i <= 0 then break end
		if (LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i))) == s then	--  INLINED!!
			SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i), ((LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (c)))))	--  INLINED!!
			SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + ((c)), (0))	--  INLINED!!
			SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0), ((c - 1)))	--  INLINED!!
			if true then break end
		end
		i = i - 1
	end
end
---@param this integer
---@param h handle
---@return nothing
function s__SanctifiedEnchantment_RemoveThis(this, h)
	s__SanctifiedEnchantment_Remove(h, this)
end
---@param h handle
---@param s integer
---@return nothing
function s__SanctifiedEnchantment_RemoveOrdered(h, s)
	local b = false
	local c = (LoadInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0)))	--  INLINED!!
	local i = 1
	while true do
		if i > c then break end
		if  not b then
			if (LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i))) == s then	--  INLINED!!
				b = true
			end
		end
		if b then
			SaveInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i), ((LoadInteger(Global_Hash, GetHandleId((h)), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (i + 1)))))	--  INLINED!!
		end
		i = i + 1
	end
	if b then
		SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + ((c)), (0))	--  INLINED!!
		SaveInteger(Global_Hash, GetHandleId(((h))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (0), ((c - 1)))	--  INLINED!!
	end
end
---@param this integer
---@param h handle
---@return nothing
function s__SanctifiedEnchantment_RemoveThisOrdered(this, h)
	s__SanctifiedEnchantment_RemoveOrdered(h, this)
end
---@param this integer
---@param c unit
---@return nothing
function s__SanctifiedEnchantment_update(this, c)
	s__SanctifiedEnchantment_Time[this] = 0
	s__SanctifiedEnchantment_Level[this] = GetUnitAbilityLevel(c, SanctifiedEnchantment_SkillId)
	SetUnitAbilityLevel(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillAbilityStatusId, s__SanctifiedEnchantment_Level[this])
	SetUnitAbilityLevel(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_AbilitySplashId, s__SanctifiedEnchantment_Level[this])
end
---@param this integer
---@return nothing
function s__SanctifiedEnchantment_destroy(this)
	DisableTrigger(s__SanctifiedEnchantment_Trigger[this])
	SaveInteger(Global_Hash, GetHandleId((((s__SanctifiedEnchantment_Trigger[this])))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + ((-1)), (0))	--  INLINED!!
	DestroyTrigger(s__SanctifiedEnchantment_Trigger[this])
	s__SanctifiedEnchantment_Trigger[this] = nil
	--  ====================
	SaveInteger(Global_Hash, GetHandleId((((s__SanctifiedEnchantment_Target[this])))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + ((-1)), (0))	--  INLINED!!
	UnitRemoveAbility(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillBookId)
	UnitRemoveAbility(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillBuffStatusId)
	s__SanctifiedEnchantment_Target[this] = nil
	s__SanctifiedEnchantment_deallocate(this)
end
---@return boolean
function s__SanctifiedEnchantment_Function()
	local this = (LoadInteger(Global_Hash, GetHandleId(((GetTriggeringTrigger()))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (-1)))	--  INLINED!!
	if GetTriggerEventId() == EVENT_GAME_TIMER_EXPIRED then
		s__SanctifiedEnchantment_Time[this] = s__SanctifiedEnchantment_Time[this] + s__SanctifiedEnchantment_Date
		if s__SanctifiedEnchantment_Time[this] >= SanctifiedEnchantment_BuffDuration[s__SanctifiedEnchantment_Levelthis] or GetUnitAbilityLevel(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillBuffStatusId) == 0 then
			s__SanctifiedEnchantment_destroy(this)
		end
	else
		s__SanctifiedEnchantment_destroy(this)
	end
	return false
end
---@param c unit
---@param t unit
---@return integer
function s__SanctifiedEnchantment_create(c, t)
	local this = s__SanctifiedEnchantment__allocate()
	s__SanctifiedEnchantment_Level[this] = GetUnitAbilityLevel(c, SanctifiedEnchantment_SkillId)
	s__SanctifiedEnchantment_Target[this] = t
	UnitAddAbility(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillBookId)
	UnitMakeAbilityPermanent(s__SanctifiedEnchantment_Target[this], true, SanctifiedEnchantment_SkillBookId)
	UnitMakeAbilityPermanent(s__SanctifiedEnchantment_Target[this], true, SanctifiedEnchantment_SkillAbilityStatusId)
	UnitMakeAbilityPermanent(s__SanctifiedEnchantment_Target[this], true, SanctifiedEnchantment_AbilitySplashId)
	SetUnitAbilityLevel(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_SkillAbilityStatusId, s__SanctifiedEnchantment_Level[this])
	SetUnitAbilityLevel(s__SanctifiedEnchantment_Target[this], SanctifiedEnchantment_AbilitySplashId, s__SanctifiedEnchantment_Level[this])
	s__SanctifiedEnchantment_SaveThisUnique(this, s__SanctifiedEnchantment_Target[this])
	--  ====================
	s__SanctifiedEnchantment_Trigger[this] = CreateTrigger()
	s__SanctifiedEnchantment_SaveThisUnique(this, s__SanctifiedEnchantment_Trigger[this])
	TriggerAddCondition(s__SanctifiedEnchantment_Trigger[this], Condition(s__SanctifiedEnchantment_Function))
	TriggerRegisterDeathEvent(s__SanctifiedEnchantment_Trigger[this], s__SanctifiedEnchantment_Target[this])
	TriggerRegisterTimerEvent(s__SanctifiedEnchantment_Trigger[this], s__SanctifiedEnchantment_Date, true)
	return this
end
---@return nothing
function SanctifiedEnchantment___SkillAction_EFFECT()
	local se = (LoadInteger(Global_Hash, GetHandleId(((GetSpellTargetUnit()))), 10000 + JASS_MAX_ARRAY_SIZE * s__SanctifiedEnchantment_Key + (-1)))	--  INLINED!!
	if se > 0 then
		s__SanctifiedEnchantment_update(se, GetTriggerUnit())
	else
		s__SanctifiedEnchantment_create(GetTriggerUnit(), GetSpellTargetUnit())
	end
end
---@return boolean
function SanctifiedEnchantment___SkillCondition_EFFECT()
	return GetSpellAbilityId() == SanctifiedEnchantment_SkillId
end
---@return nothing
function SanctifiedEnchantment___InitPreload()
	local index = 0
	while true do
		SetPlayerAbilityAvailable(Player(index), SanctifiedEnchantment_SkillBookId, false)
		index = index + 1
		if index == bj_MAX_PLAYER_SLOTS then break end
	end
end
---@return nothing
function SanctifiedEnchantment___Init()
	local trg = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(trg, EVENT_PLAYER_UNIT_SPELL_EFFECT)
	TriggerAddCondition(trg, Condition(SanctifiedEnchantment___SkillCondition_EFFECT))
	TriggerAddAction(trg, SanctifiedEnchantment___SkillAction_EFFECT)
	trg = nil
	SanctifiedEnchantment___InitPreload()
	--  ====================
	SanctifiedEnchantment_BuffDuration[1] = 40
	SanctifiedEnchantment_BuffDuration[2] = 40
	SanctifiedEnchantment_BuffDuration[3] = 40
	SanctifiedEnchantment_BuffDuration[4] = 40
end
-- library SanctifiedEnchantment ends
