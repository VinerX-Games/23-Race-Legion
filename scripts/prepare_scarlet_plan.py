# -*- coding: utf-8 -*-
"""Comprehensive plan preparation for Race 12: Scarlet Crusade (Алый Орден) UI text standardization.

Generates docs/ui_text/scarlet_plan.json containing:
- wts_updates: dict mapping string_id -> new_standardized_value
- checks_def: verification definitions for HiveWE object inspection
- statistics and metadata
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

wts_path = ROOT / "map.w3x/war3map.wts"
wts_content = wts_path.read_text(encoding="utf-8")

def check_wts_has(sid):
    pattern = rf"STRING 0*{sid}\s*\{{\s*\r?\n"
    return bool(re.search(pattern, wts_content))

wts_updates = {}

# =========================================================================
# 1. SELECTION (A0HM)
# =========================================================================
wts_updates[38865] = "|cffe4cfa3Алый Орден|r"
wts_updates[38866] = "|cffe4cfa3Алый Орден|r (|cffffffffQ|r)"
wts_updates[11204] = (
    "|cffa6afb8РАСА:|cffced4da Религиозно-военный орден паладинов, инквизиторов и фанатиков Света.|r|n|n"
    "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor(Яхве)|r|n"
    "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
    "|cffa6afb8Сложность:|r |cffffffff●●|cffa6afb8●●●|r|n"
    "|cffa6afb8Период:|r |cffa9c7de«Классический WoW» — «Битва за Азерот»|r|n|n"
    "|cffced4daАлый Орден — непримиримая религиозная организация, сформированная из остатков войск павшего королевства Лордерон. "
    "Фанатично веруя в праведность своего дела, воины ордена ведут беспощадную войну против нежити и всех, кого подозревают в скверне. "
    "В монастырях и бастионах ордена выковываются несгибаемые паладины, искусные арбалетчики и карающие инквизиторы, несущие очищающий огонь на весь Азерот.|r"
)

# =========================================================================
# 2. BUILDINGS (12)
# =========================================================================

# h05U: Ратуша (Q)
wts_updates[17404] = "|cffe4cfa3Ратуша|r"
wts_updates[17405] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
wts_updates[12539] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Главная ставка и центр сбора ресурсов Алого Ордена (первая ступень). Позволяет обучать работников, дровосеков и ополченцев, а также доставлять добытые золото и древесину.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da: базовый строитель и добытчик ресурсов.|n"
    "- |cffa9c7deДровосек|cffced4da: специализированный добытчик древесины.|n"
    "- |cffa9c7deОполченец|cffced4da: дешёвый пехотинец ополчения.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n"
    "- |cffa9c7deФорт|cffced4da: открывает передовые строения и технологии.|r"
)

# h05V: Форт (Z)
wts_updates[17406] = "|cffe4cfa3Форт|r"
wts_updates[17407] = "|cffe4cfa3Форт|r (|cffffffffZ|r)"
wts_updates[12962] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Укреплённая крепость Алого Ордена (вторая ступень). Расширяет возможности базы, открывая доступ к Мастерской, Храму Алого Ордена и тяжёлой пехоте.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da: базовый строитель и добытчик ресурсов.|n"
    "- |cffa9c7deДровосек|cffced4da: специализированный добытчик древесины.|n"
    "- |cffa9c7deОполченец|cffced4da: дешёвый пехотинец ополчения.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n"
    "- |cffa9c7deЗамок|cffced4da: высшая ступень ставки Алого Ордена.|r"
)

# h05W: Замок (Z)
wts_updates[17408] = "|cffe4cfa3Замок|r"
wts_updates[17409] = "|cffe4cfa3Замок|r (|cffffffffZ|r)"
wts_updates[12963] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Неприступная цитадель Алого Ордена (третья ступень). Открывает высшие улучшения, Церковь Алого Ордена и выбор религиозного пути ордена.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da: базовый строитель и добытчик ресурсов.|n"
    "- |cffa9c7deДровосек|cffced4da: специализированный добытчик древесины.|n"
    "- |cffa9c7deОполченец|cffced4da: дешёвый пехотинец ополчения.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deАлый Орден|cffced4da: верность классическому пути, открывает паладинов и берсерков.|n"
    "- |cffa9c7deАлый Натиск|cffced4da: радикальный путь натиска, открывает инквизиторов и гладиаторов.|r"
)

# h05X: Алтарь Покорности (S)
wts_updates[17410] = "|cffe4cfa3Алтарь Покорности|r"
wts_updates[17411] = "|cffe4cfa3Алтарь Покорности|r (|cffffffffS|r)"
wts_updates[9278] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Священное место призыва и воскрешения предводителей Алого Ордена.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da: герой-защитник, целитель и вдохновитель войск.|n"
    "- |cffa9c7deЕпископ Ордена|cffced4da: герой-маг, карающий священным пламенем и призывающий фанатиков.|n"
    "- |cffa9c7deКапитан Ордена|cffced4da: герой-воитель, мастер яростного штурма и усиления атак.|r"
)

# h05Y: Ферма (A)
wts_updates[17412] = "|cffe4cfa3Ферма|r"
wts_updates[17413] = "|cffe4cfa3Ферма|r (|cffffffffA|r)"
wts_updates[31660] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Жилое и хозяйственное строение. Обеспечивает лагерь провизией, поддерживая численность армии и принося регулярный доход.|n|n"
    "|cffa6afb8Особенности:|cffced4da|n"
    "- Даёт |cffc8e087+20|cffced4da к доходу за выплату.|r"
)

# h05Z: Казармы (W)
wts_updates[17415] = "|cffe4cfa3Казармы|r"
wts_updates[17416] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
wts_updates[12982] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Военный лагерь подготовки пехоты, стрелков и тяжёлой кавалерии Алого Ордена.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deМечник|cffced4da: базовый пехотинец передовой линии.|n"
    "- |cffa9c7deТяжелый Пехотинец|cffced4da: элитный бронированный штурмовик с защитой от магии.|n"
    "- |cffa9c7deАрбалетчик|cffced4da: стрелок дальнего боя, пробивающий броню.|n"
    "- |cffa9c7deРыцарь Ордена|cffced4da: мощный тяжелобронированный всадник.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deУкрыться за щитом|cffced4da: защита мечников от стрел.|n"
    "- |cffa9c7deСтальной наконечник болта|cffced4da: урон арбалетчиков по тяжёлой броне.|n"
    "- |cffa9c7deУлучшенная тетива|cffced4da: дальность стрельбы арбалетчиков.|n"
    "- |cffa9c7deБроня Алого Ордена|cffced4da: снижение урона для тяжёлой пехоты и рыцарей.|n"
    "- |cffa9c7deТяжелые Тренировки|cffced4da: урон и скорость боя рыцарей.|r"
)

# h060: Кузница (R)
wts_updates[17417] = "|cffe4cfa3Кузница|r"
wts_updates[17418] = "|cffe4cfa3Кузница|r (|cffffffffR|r)"
wts_updates[20437] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Оружейная мастерская ордена. Позволяет исследовать улучшения оружия, доспехов и экипировки войск.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deЖелезные мечи|cffced4da: урон воинов ближнего боя (до 6 уровней).|n"
    "- |cffa9c7deЖелезная броня|cffced4da: защита воинов ближнего боя (до 6 уровней).|n"
    "- |cffa9c7deДоспехи из клепаной кожи|cffced4da: защита воинов дальнего боя (до 6 уровней).|n"
    "- |cffa9c7deМеткость|cffced4da: урон стрелков дальнего боя (до 6 уровней).|n"
    "- |cffa9c7deУчение Алого Ордена|cffced4da: подавление регенерации враждебной нежити.|r"
)

# h061: Храм Алого Ордена (D)
wts_updates[17258] = "|cffe4cfa3Храм Алого Ордена|r"
wts_updates[17259] = "|cffe4cfa3Храм Алого Ордена|r (|cffffffffD|r)"
wts_updates[12971] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище духовных служителей Алого Ордена. Позволяет готовить жрецов и монахинь, а также совершенствовать их магическое искусство.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da: заклинательница поддержки и очищения Светом.|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da: целитель и боевой маг, владеющий рассеиванием чар.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deВера в Пламя|cffced4da: здоровье, мана и способности служителей.|n"
    "- |cffa9c7deПросветление|cffced4da: высшее мастерство жрецов и монахинь.|r"
)

# h062: Лесопилка (E)
wts_updates[17419] = "|cffe4cfa3Лесопилка|r"
wts_updates[17420] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
wts_updates[12985] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Пункт приёма древесины и лесозаготовительное предприятие. Позволяет исследовать улучшения прочности построек и добычи древесины.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deУлучшенная кладка|cffced4da: прочность и защита всех зданий базы.|n"
    "- |cffa9c7deУлучшенные инструменты|cffced4da: вместимость переносимой древесины у работников.|r"
)

# h063: Сторожевая Башня (Z)
wts_updates[17260] = "|cffe4cfa3Сторожевая Башня|r"
wts_updates[17261] = "|cffe4cfa3Сторожевая Башня|r (|cffffffffZ|r)"
wts_updates[8049] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное укрепление Алого Ордена. Оснащена баллистой, обстреливающей наземных и воздушных противников.|n|n"
    "|cffa6afb8Особенности:|cffced4da|n"
    "- Получает бонусы от улучшения |cffa9c7deМеткость|cffced4da.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# h064: Мастерская (F)
wts_updates[17421] = "|cffe4cfa3Мастерская|r"
wts_updates[17422] = "|cffe4cfa3Мастерская|r (|cffffffffF|r)"
wts_updates[12987] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Инженерный арсенал Алого Ордена. Позволяет собирать осадную технику и разрабатывать специализированное оружие.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deКатапульта|cffced4da: осадное орудие дальнего боя для сокрушения укреплений.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deГорючая смесь|cffced4da: поджигающие снаряды катапульт.|n"
    "- |cffa9c7deДлинный Арбалет|cffced4da: повышенная дальность стрельбы арбалетчиков.|n"
    "- |cffa9c7deКороткий Арбалет|cffced4da: увеличенная скорострельность арбалетчиков.|n"
    "- |cffa9c7deБроня Берсерка|cffced4da: шипы и защита берсерков.|n"
    "- |cffa9c7deЗачарованные топоры|cffced4da: оглушающие удары берсерков.|n"
    "- |cffa9c7deУлучшенная секира|cffced4da: критические удары гладиаторов.|r"
)

# h068: Церковь Алого Ордена (X)
wts_updates[17264] = "|cffe4cfa3Церковь Алого Ордена|r"
wts_updates[17265] = "|cffe4cfa3Церковь Алого Ордена|r (|cffffffffX|r)"
wts_updates[12988] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Высший духовный бастион фанатиков ордена. Готовит элитных воинов и чемпионов веры в зависимости от выбранного религиозного пути.|n|n"
    "|cffa6afb8Обучает (Алый Орден):|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da: паладин-целитель с аурой воеводы и рассечением.|n"
    "- |cffa9c7deБерсерк|cffced4da: универсальный воин ближнего и дальнего боя.|n|n"
    "|cffa6afb8Обучает (Алый Натиск):|cffced4da|n"
    "- |cffa9c7deИнквизитор|cffced4da: боевой жрец со священным молотом и воскрешением.|n"
    "- |cffa9c7deГладиатор|cffced4da: свирепый боец с боевым кличем и яростью.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deУчения Паладина|cffced4da: регенерация паладинов ордена.|n"
    "- |cffa9c7deОсвящение молота|cffced4da: урон и поджог инквизиторов.|n"
    "- |cffa9c7deЯрость Инквизиции|cffced4da: здоровье и мана инквизиторов.|n"
    "- |cffa9c7deТренировочные бои|cffced4da: скорость боя воинов церкви.|r"
)

# =========================================================================
# 3. HEROES (3)
# =========================================================================

# H03H: Паладин Алого Ордена (C)
wts_updates[861] = "|cffe4cfa3Паладин Алого Ордена|r"
wts_updates[6475] = "Паладин Алого Ордена"
wts_updates[6477] = "|cffe4cfa3Паладин Алого Ордена|r (|cffffffffC|r)"
wts_updates[31647] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Праведный воитель и духовный лидер ближнего боя, исцеляющий союзников, укрепляющий их защиту и возвращающий к жизни павших воинов.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deВолна исцеления|cffced4da: исцеляет выбранную цель и союзников по цепочке.|n"
    "- |cffa9c7deБлагословление|cffced4da: временно увеличивает броню союзников в области.|n"
    "- |cffa9c7deАура Воеводы|cffced4da: постоянно повышает урон от атак ближайших союзников.|n"
    "- |cffa9c7deВоскрешение|cffced4da: возвращает к жизни павших союзных бойцов.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# H06C: Епископ Ордена (Z)
wts_updates[6549] = "|cffe4cfa3Епископ Ордена|r"
wts_updates[6550] = "Епископ Ордена"
wts_updates[6552] = "|cffe4cfa3Епископ Ордена|r (|cffffffffZ|r)"
wts_updates[31673] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный духовный наставник и маг дальнего боя, карающий еретиков священным огнём и призывающий фанатиков ордена.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deОгненный столб|cffced4da: наносит периодический урон в области и поджигает врагов.|n"
    "- |cffa9c7deОгненная стрела|cffced4da: поражает врага огненным снарядом и оглушает его.|n"
    "- |cffa9c7deМольба к свету|cffced4da: ускоряет восстановление маны союзников аурой.|n"
    "- |cffa9c7deФанатики|cffced4da: призывает преданных воинов ордена на поле боя.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# H06B: Капитан Ордена (X)
wts_updates[6479] = "|cffe4cfa3Капитан Ордена|r"
wts_updates[6480] = "Капитан Ордена"
wts_updates[6482] = "|cffe4cfa3Капитан Ордена|r (|cffffffffX|r)"
wts_updates[31672] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Закалённый командир штурмовых отрядов ближнего боя, наносящий глубокие раны врагам и воодушевляющий войска на сокрушительную атаку.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЯрость|cffced4da: многократно увеличивает скорость атаки и бега капитана.|n"
    "- |cffa9c7deКровотечение|cffced4da: заставляет раненых врагов истекать кровью при атаках.|n"
    "- |cffa9c7deРаскат грома|cffced4da: сотрясает землю, нанося урон и замедляя врагов.|n"
    "- |cffa9c7deВдохновляющая Речь|cffced4da: значительно увеличивает базовый урон союзников.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# =========================================================================
# 4. UNITS (15)
# =========================================================================

# h014: Работник (W)
wts_updates[5249] = "|cffe4cfa3Работник|r"
wts_updates[5250] = "|cffe4cfa3Работник|r (|cffffffffW|r)"
wts_updates[13415] = (
    "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Алого Ордена. Добывает золото и древесину, а также возводит и ремонтирует здания базы.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deДобывать ресурсы|cffced4da: заготовка золота и древесины.|n"
    "- |cffa9c7deРемонтировать|cffced4da: восстановление прочности строений и техники.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h03C: Дровосек (W)
wts_updates[5255] = "|cffe4cfa3Дровосек|r"
wts_updates[5256] = "|cffe4cfa3Дровосек|r (|cffffffffW|r)"
wts_updates[31643] = (
    "|cffa6afb8ЮНИТ:|cffced4da Специализированный рабочий лесозаготовок. Быстро рубит деревья и доставляет древесину в ратушу или на лесопилку.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deДобывать ресурсы|cffced4da: заготовка древесины в лесах.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h03A: Ополченец (E)
wts_updates[5251] = "|cffe4cfa3Ополченец|r"
wts_updates[5252] = "|cffe4cfa3Ополченец|r (|cffffffffE|r)"
wts_updates[19302] = (
    "|cffa6afb8ЮНИТ:|cffced4da Легковооружённый боец ополчения. Дешёвый вспомогательный воин ближнего боя для обороны базы и прикрытия стрелков.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h03B: Мечник (Q)
wts_updates[5253] = "|cffe4cfa3Мечник|r"
wts_updates[5254] = "|cffe4cfa3Мечник|r (|cffffffffQ|r)"
wts_updates[19447] = (
    "|cffa6afb8ЮНИТ:|cffced4da Основной пехотинец Алого Ордена. Стойкий боец передовой линии, способный укрываться за щитом от стрел.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deУкрыться за щитом|cffced4da: уменьшает получаемый урон от стрел и отражает их.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# n007: Арбалетчик (W)
wts_updates[5247] = "|cffe4cfa3Арбалетчик|r"
wts_updates[5248] = "|cffe4cfa3Арбалетчик|r (|cffffffffW|r)"
wts_updates[21615] = (
    "|cffa6afb8ЮНИТ:|cffced4da Меткий стрелок дальнего боя. Наносит повышенный урон по тяжёлой броне и улучшает дальность либо скорострельность арбалета.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deСтальной наконечник болта|cffced4da: бонусный урон по тяжёлой броне.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# h039: Тяжелый Пехотинец (E)
wts_updates[5311] = "|cffe4cfa3Тяжелый Пехотинец|r"
wts_updates[5312] = "|cffe4cfa3Тяжелый Пехотинец|r (|cffffffffE|r)"
wts_updates[16938] = (
    "|cffa6afb8ЮНИТ:|cffced4da Элитный закованный в латы штурмовик ордена. Обладает защитой от магии, тяжёлой бронёй и способностью перерождаться после гибели.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЗащита от магии|cffced4da: невосприимчивость к магии ценой скорости бега.|n"
    "- |cffa9c7deУкрыться за щитом|cffced4da: снижение урона от пронзающих атак.|n"
    "- |cffa9c7deБроня Алого Ордена|cffced4da: поглощение части получаемого урона.|n"
    "- |cffa9c7deВозрождение|cffced4da: автоматическое воскрешение после гибели.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h066: Рыцарь Ордена (R)
wts_updates[5302] = "|cffe4cfa3Рыцарь Ордена|r"
wts_updates[5303] = "|cffe4cfa3Рыцарь Ордена|r (|cffffffffR|r)"
wts_updates[21617] = (
    "|cffa6afb8ЮНИТ:|cffced4da Мощный тяжелобронированный всадник Алого Ордена. Сокрушает вражеские ряды стремительным натиском и возрождается в бою.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deТяжелые Тренировки|cffced4da: повышенный урон и скорость боя.|n"
    "- |cffa9c7deБроня Алого Ордена|cffced4da: поглощение части получаемого урона.|n"
    "- |cffa9c7deВозрождение|cffced4da: автоматическое воскрешение после гибели.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# o00I: Катапульта (Q)
wts_updates[1232] = "|cffe4cfa3Катапульта|r"
wts_updates[1233] = "|cffe4cfa3Катапульта|r (|cffffffffQ|r)"
wts_updates[24741] = (
    "|cffa6afb8ЮНИТ:|cffced4da Тяжёлое осадное орудие дальнего боя. Сокрушает укрепления противника и поражает скопления пехоты зажигательными снарядами.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deГорючая смесь|cffced4da: снаряды поджигают землю в месте попадания.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h067: Монахиня Алого Ордена (Q)
wts_updates[5306] = "|cffe4cfa3Монахиня Алого Ордена|r"
wts_updates[5307] = "|cffe4cfa3Монахиня Алого Ордена|r (|cffffffffQ|r)"
wts_updates[21618] = (
    "|cffa6afb8ЮНИТ:|cffced4da Служительница ордена, владеющая защитной и поддерживающей магией Света. Усиливает соратников бронёй и поглощает чужие чары.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deВнутренний огонь|cffced4da: повышает урон и броню союзника.|n"
    "- |cffa9c7deПоглощение Света|cffced4da: снимает эффекты и восполняет здоровье и ману.|n"
    "- |cffa9c7deОчищающий Огонь|cffced4da: добавляет урон от огня к атакам.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# n008: Жрец Алого Ордена (W)
wts_updates[1231] = "|cffe4cfa3Жрец Алого Ордена|r"
wts_updates[919] = "|cffe4cfa3Жрец Алого Ордена|r (|cffffffffW|r)"
wts_updates[22381] = (
    "|cffa6afb8ЮНИТ:|cffced4da Священник ордена, владеющий исцелением, рассеиванием вражеской магии и ускоряющей союзников молитвой.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deИсцеление|cffced4da: восполняет здоровье раненым союзникам.|n"
    "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты в области и ранит призванных существ.|n"
    "- |cffa9c7deМолитва|cffced4da: аура ускоряет перемещение и атаку союзников.|n"
    "- |cffa9c7deОчищающий Огонь|cffced4da: добавляет урон от огня к атакам.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# h03F: Паладин Алого Ордена (R) (Церковь)
wts_updates[5259] = "|cffe4cfa3Паладин Алого Ордена|r"
wts_updates[5260] = "|cffe4cfa3Паладин Алого Ордена|r (|cffffffffR|r)"
wts_updates[20904] = (
    "|cffa6afb8ЮНИТ:|cffced4da Элитный паладин Церкви Алого Ордена. Сочетает мощные удары по области, ауру воеводы, исцеление союзников и перерождение.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deСвет небес|cffced4da: восполняет здоровье союзнику или наносит урон нежити.|n"
    "- |cffa9c7deРассекающий удар|cffced4da: наносит урон соседним врагам при атаке.|n"
    "- |cffa9c7deАура Воеводы|cffced4da: повышает урон окружающих союзников.|n"
    "- |cffa9c7deВозрождение|cffced4da: автоматическое воскрешение после гибели.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h03D: Берсерк (W) (Церковь)
wts_updates[5257] = "|cffe4cfa3Берсерк|r"
wts_updates[5258] = "|cffe4cfa3Берсерк|r (|cffffffffW|r)"
wts_updates[25177] = (
    "|cffa6afb8ЮНИТ:|cffced4da Неистовый боец Алого Ордена. Способен переключаться между ближним боем с секирами и метанием топоров на дистанции.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПерейти в дальний бой|cffced4da: переключает оружие на метательные топоры.|n"
    "- |cffa9c7deБроня Берсерка|cffced4da: шипы отражают урон и повышают броню.|n"
    "- |cffa9c7deОглушающее попадание|cffced4da: шанс оглушить цель и нанести дополнительный урон.|n"
    "- |cffa9c7deВозрождение|cffced4da: автоматическое воскрешение после гибели.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h065: Берсерк (W) (Форма ближнего боя)
wts_updates[5300] = "|cffe4cfa3Берсерк|r"
wts_updates[5301] = "|cffe4cfa3Берсерк|r (|cffffffffW|r)"
wts_updates[21616] = (
    "|cffa6afb8ЮНИТ:|cffced4da Неистовый берсерк ордена в стойке ближнего боя с боевыми секирами.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПерейти в ближний бой|cffced4da: возврат в ближний строй.|n"
    "- |cffa9c7deБроня Берсерка|cffced4da: шипы отражают урон и повышают броню.|n"
    "- |cffa9c7deОглушающее попадание|cffced4da: шанс оглушить врага при ударе.|n"
    "- |cffa9c7deВозрождение|cffced4da: автоматическое воскрешение после гибели.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# h03I: Инквизитор (E) (Церковь - Алый Натиск)
wts_updates[8785] = "|cffe4cfa3Инквизитор|r"
wts_updates[14748] = "|cffe4cfa3Инквизитор|r (|cffffffffE|r)"
wts_updates[21611] = (
    "|cffa6afb8ЮНИТ:|cffced4da Неумолимый каратель Алого Натиска. Обладает аурой регенерации, огненным молотом, массовым исцелением и воскрешением павших бойцов.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deСвященный Молот|cffced4da: дополнительный урон и поджог целей атаки.|n"
    "- |cffa9c7deМассовая благодать|cffced4da: исцеляет союзников вокруг инквизитора.|n"
    "- |cffa9c7deВоскрешение|cffced4da: возвращает к жизни павшего соратника.|n"
    "- |cffa9c7deАура Алого ордена|cffced4da: ускоряет восстановление здоровья союзников.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные и воздушные|cffced4da цели.|r"
)

# h03G: Гладиатор (Q) (Церковь - Алый Натиск)
wts_updates[5261] = "|cffe4cfa3Гладиатор|r"
wts_updates[5262] = "|cffe4cfa3Гладиатор|r (|cffffffffQ|r)"
wts_updates[21283] = (
    "|cffa6afb8ЮНИТ:|cffced4da Свирепый воин-рукопашник Алого Натиска. Впадает в боевую ярость, усиливает соратников кличем и наносит сокрушительные критические удары.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЯрость|cffced4da: повышает скорость атаки ценой получаемого урона.|n"
    "- |cffa9c7deБоевой клич|cffced4da: увеличивает урон находящихся рядом союзников.|n"
    "- |cffa9c7deКритический удар|cffced4da: шанс нанести многократный урон при атаке.|n"
    "- |cffa9c7deНенависть|cffced4da: подавление регенерации враждебной нежити.|n|n"
    "|cffced4daАтакует |cffffffffназемные|cffced4da цели.|r"
)

# =========================================================================
# 5. HERO ABILITIES (12)
# =========================================================================

# --- Паладин Алого Ордена (H03H) ---

# A097: Волна исцеления (Q)
wts_updates[6376] = "|cffe4cfa3Волна исцеления|r"
wts_updates[6377] = "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)"
wts_updates[622] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну священной энергии, восполняющую здоровье выбранной цели и переходящую на ближайших союзников. С каждым переходом сила исцеления уменьшается.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da восполняет |cffc8e087130|cffced4da ед. здоровья, до |cffffffff3|cffced4da целей.|n"
    "|cffa6afb8Уровень 2:|cffced4da восполняет |cffc8e087215|cffced4da ед. здоровья, до |cffffffff4|cffced4da целей.|n"
    "|cffa6afb8Уровень 3:|cffced4da восполняет |cffc8e087300|cffced4da ед. здоровья, до |cffffffff5|cffced4da целей.|n"
    "|cffa6afb8Уровень 4:|cffced4da восполняет |cffc8e087420|cffced4da ед. здоровья, до |cffffffff8|cffced4da целей.|r"
)
wts_updates[6378] = "|cffe4cfa3Волна исцеления — уровень 1|r (|cffffffffQ|r)"
wts_updates[5862] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Волна энергии восполняет |cffc8e087130|cffced4da ед. здоровья цели и переходит на союзников (до |cffffffff3|cffced4da целей). С каждым переходом исцеление слабеет.|r"
wts_updates[6379] = "|cffe4cfa3Волна исцеления — уровень 2|r (|cffffffffQ|r)"
wts_updates[5863] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Волна энергии восполняет |cffc8e087215|cffced4da ед. здоровья цели и переходит на союзников (до |cffffffff4|cffced4da целей). С каждым переходом исцеление слабеет.|r"
wts_updates[6380] = "|cffe4cfa3Волна исцеления — уровень 3|r (|cffffffffQ|r)"
wts_updates[725] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Волна энергии восполняет |cffc8e087300|cffced4da ед. здоровья цели и переходит на союзников (до |cffffffff5|cffced4da целей). С каждым переходом исцеление слабеет.|r"
wts_updates[6381] = "|cffe4cfa3Волна исцеления — уровень 4|r (|cffffffffQ|r)"
wts_updates[615] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Волна энергии восполняет |cffc8e087420|cffced4da ед. здоровья цели и переходит на союзников (до |cffffffff8|cffced4da целей). С каждым переходом исцеление слабеет.|r"

# A09C: Благословление (W)
wts_updates[6438] = "|cffe4cfa3Благословление|r"
wts_updates[6507] = "|cffe4cfa3Благословление|r (|cffffffffW|r)"
wts_updates[825] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников благословенным щитом, временно увеличивая их защиту. Время действия — |cffffffff20|cffced4da сек.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+2|cffced4da к броне.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+3|cffced4da к броне.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffc8e087+4|cffced4da к броне.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffc8e087+6|cffced4da к броне.|r"
)
wts_updates[6437] = "|cffe4cfa3Благословление — уровень 1|r (|cffffffffW|r)"
wts_updates[11127] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+2|cffced4da к броне на |cffffffff20|cffced4da сек.|r"
wts_updates[6440] = "|cffe4cfa3Благословление — уровень 2|r (|cffffffffW|r)"
wts_updates[11207] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+3|cffced4da к броне на |cffffffff20|cffced4da сек.|r"
wts_updates[6441] = "|cffe4cfa3Благословление — уровень 3|r (|cffffffffW|r)"
wts_updates[11208] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+4|cffced4da к броне на |cffffffff20|cffced4da сек.|r"
wts_updates[6442] = "|cffe4cfa3Благословление — уровень 4|r (|cffffffffW|r)"
wts_updates[11381] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+6|cffced4da к броне на |cffffffff20|cffced4da сек.|r"
wts_updates[6449] = "|cffe4cfa3Благословление — уровень 1|r"
wts_updates[6445] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+2|cffced4da к броне.|r"
wts_updates[6450] = "|cffe4cfa3Благословление — уровень 2|r"
wts_updates[6443] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+3|cffced4da к броне.|r"
wts_updates[6451] = "|cffe4cfa3Благословление — уровень 3|r"
wts_updates[6439] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+4|cffced4da к броне.|r"
wts_updates[6452] = "|cffe4cfa3Благословление — уровень 4|r"
wts_updates[6444] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт находящимся рядом союзникам |cffc8e087+6|cffced4da к броне.|r"

# A09D: Аура Воеводы (E - Hero passive)
wts_updates[6457] = "|cffe4cfa3Аура Воеводы|r"
wts_updates[6460] = "|cffe4cfa3Аура Воеводы|r (|cffffffffE|r)"
wts_updates[828] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Постоянная аура паладина, увеличивающая урон от атак находящихся рядом союзных бойцов.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+10%|cffced4da к урону.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+15%|cffced4da к урону.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffc8e087+20%|cffced4da к урону.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffc8e087+25%|cffced4da к урону.|r"
)
wts_updates[6458] = "|cffe4cfa3Аура Воеводы — уровень 1|r"
wts_updates[2579] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак ближайших союзников на |cffc8e087+10%|cffced4da.|r"
wts_updates[6461] = "|cffe4cfa3Аура Воеводы — уровень 2|r"
wts_updates[829] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак ближайших союзников на |cffc8e087+15%|cffced4da.|r"
wts_updates[6462] = "|cffe4cfa3Аура Воеводы — уровень 3|r"
wts_updates[831] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак ближайших союзников на |cffc8e087+20%|cffced4da.|r"
wts_updates[6471] = "|cffe4cfa3Аура Воеводы — уровень 4|r"
wts_updates[2577] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак ближайших союзников на |cffc8e087+25%|cffced4da.|r"

# A09E: Воскрешение (R - Ult)
wts_updates[6468] = "|cffe4cfa3Воскрешение|r"
wts_updates[6469] = "|cffe4cfa3Воскрешение|r (|cffffffffR|r)"
wts_updates[4368] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни павших союзных бойцов в указанной области.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da воскрешает до |cffffffff12|cffced4da бойцов.|n"
    "|cffa6afb8Уровень 2:|cffced4da воскрешает до |cffffffff24|cffced4da бойцов.|r"
)
wts_updates[6470] = "|cffe4cfa3Воскрешение — уровень 1|r (|cffffffffR|r)"
wts_updates[4369] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff12|cffced4da павших союзных воинов в области действия.|r"
wts_updates[6466] = "|cffe4cfa3Воскрешение — уровень 2|r (|cffffffffR|r)"
wts_updates[2581] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff24|cffced4da павших союзных воинов в области действия.|r"

# --- Епископ Ордена (H06C) ---

# A09K: Огненный столб (Q)
wts_updates[6559] = "|cffe4cfa3Огненный столб|r"
wts_updates[6560] = "|cffe4cfa3Огненный столб|r (|cffffffffQ|r)"
wts_updates[15394] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт столб священного пламени, наносящий концентрированный урон в области и поджигающий врагов.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffffffff45|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffffffff80|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffffffff110|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffffffff135|cffced4da урона/сек. в течение |cffffffff4|cffced4da сек.|r"
)
wts_updates[6556] = "|cffe4cfa3Огненный столб — уровень 1|r (|cffffffffQ|r)"
wts_updates[15395] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным врагам в области |cffffffff45|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек., затем наносит остаточный урон.|r"
wts_updates[6558] = "|cffe4cfa3Огненный столб — уровень 2|r (|cffffffffQ|r)"
wts_updates[15396] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным врагам в области |cffffffff80|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек., затем наносит остаточный урон.|r"
wts_updates[6557] = "|cffe4cfa3Огненный столб — уровень 3|r (|cffffffffQ|r)"
wts_updates[15397] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным врагам в области |cffffffff110|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек., затем наносит остаточный урон.|r"
wts_updates[6554] = "|cffe4cfa3Огненный столб — уровень 4|r (|cffffffffQ|r)"
wts_updates[15393] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным врагам в области |cffffffff135|cffced4da урона/сек. в течение |cffffffff4|cffced4da сек., затем наносит остаточный урон.|r"

# A09L: Огненная стрела (W)
wts_updates[6561] = "|cffe4cfa3Огненная стрела|r"
wts_updates[6562] = "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)"
wts_updates[15035] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком священного огня, нанося урон и оглушая её.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffffffff75|cffced4da урона, оглушение на |cffffffff2|cffced4da сек.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffffffff150|cffced4da урона, оглушение героев на |cffffffff2|cffced4da сек., воинов на |cffffffff3|cffced4da сек.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffffffff270|cffced4da урона, оглушение героев на |cffffffff2|cffced4da сек., воинов на |cffffffff4|cffced4da сек.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffffffff350|cffced4da урона, оглушение героев на |cffffffff2|cffced4da сек., воинов на |cffffffff5|cffced4da сек.|r"
)
wts_updates[6563] = "|cffe4cfa3Огненная стрела — уровень 1|r (|cffffffffW|r)"
wts_updates[6570] = "|cffe4cfa3Огненная стрела — уровень 1|r"
wts_updates[2567] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff75|cffced4da урона и оглушает её на |cffffffff2|cffced4da сек.|r"
wts_updates[6564] = "|cffe4cfa3Огненная стрела — уровень 2|r (|cffffffffW|r)"
wts_updates[6571] = "|cffe4cfa3Огненная стрела — уровень 2|r"
wts_updates[2564] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff150|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff3|cffced4da сек.|r"
wts_updates[6567] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff150|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff3|cffced4da сек.|r"
wts_updates[6565] = "|cffe4cfa3Огненная стрела — уровень 3|r (|cffffffffW|r)"
wts_updates[6572] = "|cffe4cfa3Огненная стрела — уровень 3|r"
wts_updates[2565] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff270|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff4|cffced4da сек.|r"
wts_updates[6568] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff270|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff4|cffced4da сек.|r"
wts_updates[6566] = "|cffe4cfa3Огненная стрела — уровень 4|r (|cffffffffW|r)"
wts_updates[6573] = "|cffe4cfa3Огненная стрела — уровень 4|r"
wts_updates[2566] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff350|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff5|cffced4da сек.|r"
wts_updates[6569] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff350|cffced4da урона и оглушает героев на |cffffffff2|cffced4da сек., воинов на |cffffffff5|cffced4da сек.|r"

# A09N: Мольба к свету (E - Passive aura)
wts_updates[6590] = "|cffe4cfa3Мольба к свету|r"
wts_updates[6591] = "|cffe4cfa3Мольба к свету|r (|cffffffffE|r)"
wts_updates[15402] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Священная аура епископа, ускоряющая восстановление маны находящихся рядом союзников.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+0.7|cffced4da к восстановлению маны в секунду.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+1.5|cffced4da к восстановлению маны в секунду.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffc8e087+2.25|cffced4da к восстановлению маны в секунду.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffc8e087+3.0|cffced4da к восстановлению маны в секунду.|r"
)
wts_updates[6592] = "|cffe4cfa3Мольба к свету — уровень 1|r"
wts_updates[15403] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны союзников на |cffc8e087+0.7|cffced4da ед. в секунду.|r"
wts_updates[6593] = "|cffe4cfa3Мольба к свету — уровень 2|r"
wts_updates[15404] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны союзников на |cffc8e087+1.5|cffced4da ед. в секунду.|r"
wts_updates[6594] = "|cffe4cfa3Мольба к свету — уровень 3|r"
wts_updates[15405] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны союзников на |cffc8e087+2.25|cffced4da ед. в секунду.|r"
wts_updates[6595] = "|cffe4cfa3Мольба к свету — уровень 4|r"
wts_updates[15401] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны союзников на |cffc8e087+3.0|cffced4da ед. в секунду.|r"

# A09M: Фанатики (R - Ult, 2 levels)
wts_updates[6578] = "|cffe4cfa3Фанатики|r"
wts_updates[6579] = "|cffe4cfa3Фанатики|r (|cffffffffR|r)"
wts_updates[15400] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Епископ призывает на поле боя отряд фанатично преданных воинов ордена.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da призывает |cffffffff5|cffced4da гладиаторов.|n"
    "|cffa6afb8Уровень 2:|cffced4da призывает |cffffffff10|cffced4da паладинов ордена.|r"
)
wts_updates[6580] = "|cffe4cfa3Фанатики — уровень 1|r (|cffffffffR|r)"
wts_updates[15398] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff5|cffced4da гладиаторов ордена на |cffffffff60|cffced4da сек.|r"
wts_updates[6581] = "|cffe4cfa3Фанатики — уровень 2|r (|cffffffffR|r)"
wts_updates[15399] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff10|cffced4da паладинов ордена на |cffffffff60|cffced4da сек.|r"

# --- Капитан Ордена (H06B) ---

# A09G: Ярость (Q)
wts_updates[5990] = "|cffe4cfa3Ярость|r"
wts_updates[6509] = "|cffe4cfa3Ярость|r (|cffffffffQ|r)"
wts_updates[21897] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Капитан впадает в ярость, значительно увеличивая скорость боя и бега.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+100%|cffced4da к скорости боя, |cffc8e087+20%|cffced4da к скорости бега.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+200%|cffced4da к скорости боя, |cffc8e087+20%|cffced4da к скорости бега.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffc8e087+300%|cffced4da к скорости боя, |cffc8e087+20%|cffced4da к скорости бега.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffc8e087+400%|cffced4da к скорости боя, |cffc8e087+20%|cffced4da к скорости бега.|r"
)
wts_updates[6511] = "|cffe4cfa3Ярость — уровень 1|r (|cffffffffQ|r)"
wts_updates[15385] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffc8e087+100%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da.|r"
wts_updates[6512] = "|cffe4cfa3Ярость — уровень 2|r (|cffffffffQ|r)"
wts_updates[15382] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffc8e087+200%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da.|r"
wts_updates[6513] = "|cffe4cfa3Ярость — уровень 3|r (|cffffffffQ|r)"
wts_updates[15383] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffc8e087+300%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da.|r"
wts_updates[6514] = "|cffe4cfa3Ярость — уровень 4|r (|cffffffffQ|r)"
wts_updates[15384] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffc8e087+400%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da.|r"
wts_updates[6518] = "|cffe4cfa3Ярость — уровень 1|r"
wts_updates[6517] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки капитана.|r"
wts_updates[6520] = "|cffe4cfa3Ярость — уровень 2|r"
wts_updates[6524] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки капитана.|r"
wts_updates[6521] = "|cffe4cfa3Ярость — уровень 3|r"
wts_updates[6523] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки капитана.|r"
wts_updates[6522] = "|cffe4cfa3Ярость — уровень 4|r"
wts_updates[6525] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки капитана.|r"

# A09F: Кровотечение (W - Passive on attack)
wts_updates[39147] = "|cffe4cfa3Кровотечение|r"
wts_updates[39148] = "|cffe4cfa3Кровотечение|r (|cffffffffW|r)"
wts_updates[6375] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Удары капитана вызывают у противников сильное кровотечение, наносящее периодический урон.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffffffff5|cffced4da ед. урона/сек. Длительность: герои — |cffffffff5|cffced4da сек., воины — |cffffffff20|cffced4da сек.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffffffff7|cffced4da ед. урона/сек. Длительность: герои — |cffffffff7|cffced4da сек., воины — |cffffffff20|cffced4da сек.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffffffff9|cffced4da ед. урона/сек. Длительность: герои — |cffffffff9|cffced4da сек., воины — |cffffffff20|cffced4da сек.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffffffff11|cffced4da ед. урона/сек. Длительность: герои — |cffffffff11|cffced4da сек., воины — |cffffffff20|cffced4da сек.|r"
)
wts_updates[39149] = "|cffe4cfa3Кровотечение — уровень 1|r"
wts_updates[9832] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит раненым врагам |cffffffff5|cffced4da ед. урона/сек. Длительность: герои — |cffffffff5|cffced4da сек., воины — |cffffffff20|cffced4da сек.|r"
wts_updates[39150] = "|cffe4cfa3Кровотечение — уровень 2|r"
wts_updates[35327] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит раненым врагам |cffffffff7|cffced4da ед. урона/сек. Длительность: герои — |cffffffff7|cffced4da сек., воины — |cffffffff20|cffced4da сек.|r"
wts_updates[39151] = "|cffe4cfa3Кровотечение — уровень 3|r"
wts_updates[35468] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит раненым врагам |cffffffff9|cffced4da ед. урона/сек. Длительность: герои — |cffffffff9|cffced4da сек., воины — |cffffffff20|cffced4da сек.|r"
wts_updates[39152] = "|cffe4cfa3Кровотечение — уровень 4|r"
wts_updates[35470] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит раненым врагам |cffffffff11|cffced4da ед. урона/сек. Длительность: герои — |cffffffff11|cffced4da сек., воины — |cffffffff20|cffced4da сек.|r"
wts_updates[39153] = "|cffe4cfa3Кровотечение — уровень 1|r"
wts_updates[6486] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает периодический урон от кровотечения у атакованных врагов.|r"
wts_updates[39154] = "|cffe4cfa3Кровотечение — уровень 2|r"
wts_updates[6491] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает периодический урон от кровотечения у атакованных врагов.|r"
wts_updates[39155] = "|cffe4cfa3Кровотечение — уровень 3|r"
wts_updates[6492] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает периодический урон от кровотечения у атакованных врагов.|r"
wts_updates[39156] = "|cffe4cfa3Кровотечение — уровень 4|r"
wts_updates[6493] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает периодический урон от кровотечения у атакованных врагов.|r"

# A09I: Раскат грома (E)
wts_updates[890] = "|cffe4cfa3Раскат грома|r"
wts_updates[5682] = "|cffe4cfa3Раскат грома|r (|cffffffffE|r)"
wts_updates[9524] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный сокрушительный удар о землю, наносящий урон наземным противникам вокруг капитана и замедляющий их передвижение и атаку.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffffffff100|cffced4da ед. урона, замедление бега и атаки на |cffe69a8d50%|cffced4da.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffffffff175|cffced4da ед. урона, замедление бега и атаки на |cffe69a8d50%|cffced4da.|n"
    "|cffa6afb8Уровень 3:|cffced4da |cffffffff250|cffced4da ед. урона, замедление бега и атаки на |cffe69a8d50%|cffced4da.|n"
    "|cffa6afb8Уровень 4:|cffced4da |cffffffff400|cffced4da ед. урона, замедление бега и атаки на |cffe69a8d50%|cffced4da.|r"
)
wts_updates[6249] = "|cffe4cfa3Раскат грома — уровень 1|r (|cffffffffE|r)"
wts_updates[10551] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff100|cffced4da ед. урона наземным врагам в области и замедляет их передвижение и атаку на |cffe69a8d50%|cffced4da.|r"
wts_updates[6264] = "|cffe4cfa3Раскат грома — уровень 2|r (|cffffffffE|r)"
wts_updates[10552] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff175|cffced4da ед. урона наземным врагам в области и замедляет их передвижение и атаку на |cffe69a8d50%|cffced4da.|r"
wts_updates[6532] = "|cffe4cfa3Раскат грома — уровень 3|r (|cffffffffE|r)"
wts_updates[10553] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da ед. урона наземным врагам в области и замедляет их передвижение и атаку на |cffe69a8d50%|cffced4da.|r"
wts_updates[6533] = "|cffe4cfa3Раскат грома — уровень 4|r (|cffffffffE|r)"
wts_updates[9523] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff400|cffced4da ед. урона наземным врагам в области и замедляет их передвижение и атаку на |cffe69a8d50%|cffced4da.|r"

# A09J: Вдохновляющая Речь (R - Ult, 2 levels)
wts_updates[6540] = "|cffe4cfa3Вдохновляющая Речь|r"
wts_updates[6544] = "|cffe4cfa3Вдохновляющая Речь|r (|cffffffffR|r)"
wts_updates[15391] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Капитан произносит пламенную речь, значительно повышая урон от атак всех ближайших союзных бойцов.|n|n"
    "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+30%|cffced4da к урону.|n"
    "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+40%|cffced4da к урону.|r"
)
wts_updates[6541] = "|cffe4cfa3Вдохновляющая Речь — уровень 1|r (|cffffffffR|r)"
wts_updates[23630] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает базовый урон от атак союзников в области на |cffc8e087+30%|cffced4da.|r"
wts_updates[6542] = "|cffe4cfa3Вдохновляющая Речь — уровень 2|r (|cffffffffR|r)"
wts_updates[14840] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает базовый урон от атак союзников в области на |cffc8e087+40%|cffced4da.|r"

# =========================================================================
# 6. UNIT ABILITIES (30)
# =========================================================================

# A07I: Ярость (Гладиатор) (Q)
wts_updates[5701] = "|cffe4cfa3Ярость|r"
wts_updates[5702] = "|cffe4cfa3Ярость|r (|cffffffffQ|r)"

# A07X: Укрыться за щитом (Мечник, Тяж. пехотинец) (Q)
wts_updates[3743] = "|cffe4cfa3Укрыться за щитом|r"
wts_updates[3744] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffQ|r)"
wts_updates[3745] = "|cffe4cfa3Отменить защитную стойку|r (|cffffffffQ|r)"

# A07Y: Стальной наконечник болта (Арбалетчик passive)
wts_updates[5707] = "|cffe4cfa3Стальной наконечник болта|r"
wts_updates[5708] = "|cffe4cfa3Стальной наконечник болта|r"
wts_updates[5709] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон арбалетчика по целям с тяжёлой бронёй на |cffc8e087+20%|cffced4da.|r"

# A07Z: Защита от магии (Тяж. пехотинец) (W)
wts_updates[5912] = "|cffe4cfa3Защита от магии|r"
wts_updates[5913] = "|cffe4cfa3Защита от магии|r (|cffffffffW|r)"
wts_updates[5914] = "|cffe4cfa3Отменить защиту от магии|r (|cffffffffW|r)"

# A080: Броня Алого Ордена (Тяж. пехотинец, Рыцарь passive)
wts_updates[5915] = "|cffe4cfa3Броня Алого Ордена|r"
wts_updates[5916] = "|cffe4cfa3Броня Алого Ордена|r"
wts_updates[2001] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Тяжёлые латы поглощают |cffc8e0875|cffced4da ед. получаемого урона от каждой физической атаки.|r"

# A081: Возрождение (Тяж. пехотинец, Рыцарь, Берсерк, Паладин passive)
wts_updates[5917] = "|cffe4cfa3Возрождение|r"
wts_updates[5918] = "|cffe4cfa3Возрождение|r"
wts_updates[5919] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воин возвращается к жизни на месте своей гибели. Время восстановления — |cffffffff180|cffced4da сек.|r"

# A082: Тяжелые Тренировки (Рыцарь)
wts_updates[5929] = "|cffe4cfa3Тяжелые Тренировки|r"
wts_updates[5930] = "|cffe4cfa3Тяжелые Тренировки|r"
wts_updates[1592] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет атаку рыцарей Алого Ордена на |cffc8e087+20%|cffced4da.|r"

# A08N: Тяжелые Тренировки (Рыцарь passive 2)
wts_updates[5931] = "|cffe4cfa3Тяжелые Тренировки|r"
wts_updates[5932] = "|cffe4cfa3Тяжелые Тренировки|r"
wts_updates[13115] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон рыцарей Алого Ордена на |cffc8e087+2|cffced4da.|r"

# A083: Священный Молот (Инквизитор)
wts_updates[6038] = "|cffe4cfa3Священный Молот|r"
wts_updates[6039] = "|cffe4cfa3Священный Молот|r"
wts_updates[6040] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит дополнительный урон и поджигает атакованных противников священным огнём.|r"

# A08J: Священный Молот (Инквизитор passive level 2)
wts_updates[6041] = "|cffe4cfa3Священный Молот|r"
wts_updates[6042] = "|cffe4cfa3Священный Молот|r"
wts_updates[13117] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffc8e087+5|cffced4da к урону от атак и поджигает цели, нанося |cffffffff2|cffced4da ед. урона/сек.|r"

# A084: Перейти в ближний бой (Берсерк) (Q)
wts_updates[5936] = "|cffe4cfa3Перейти в ближний бой|r"
wts_updates[5937] = "|cffe4cfa3Перейти в ближний бой|r (|cffffffffQ|r)"
wts_updates[5938] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк берёт в руки боевые топоры и переходит в строй ближнего боя.|r"
wts_updates[5939] = "|cffe4cfa3Перейти в ближний бой|r (|cffffffffQ|r)"
wts_updates[5940] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк берёт в руки боевые топоры и переходит в строй ближнего боя.|r"

# A085: Перейти в дальний бой (Берсерк) (Q)
wts_updates[5943] = "|cffe4cfa3Перейти в дальний бой|r"
wts_updates[5944] = "|cffe4cfa3Перейти в дальний бой|r (|cffffffffQ|r)"
wts_updates[5945] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк переходит на метательные топоры, поражая противников на дистанции.|r"
wts_updates[5946] = "|cffe4cfa3Перейти в дальний бой|r (|cffffffffQ|r)"
wts_updates[5947] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк переходит на метательные топоры, поражая противников на дистанции.|r"

# A087: Молитва (Жрец passive aura)
wts_updates[5951] = "|cffe4cfa3Молитва|r"
wts_updates[5952] = "|cffe4cfa3Молитва|r"
wts_updates[6501] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура жреца ускоряет перемещение союзников на |cffc8e087+5%|cffced4da и скорость их боя на |cffc8e087+3%|cffced4da.|r"

# A088: Внутренний огонь (Монахиня) (W)
wts_updates[5953] = "|cffe4cfa3Внутренний огонь|r"
wts_updates[5954] = "|cffe4cfa3Внутренний огонь|r (|cffffffffW|r)"
wts_updates[38980] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет союзника святой силой, повышая его урон на |cffc8e087+10%|cffced4da и броню на |cffc8e087+4|cffced4da.|r"

# A089: Поглощение Света (Монахиня) (Q)
wts_updates[5955] = "|cffe4cfa3Поглощение Света|r"
wts_updates[5956] = "|cffe4cfa3Поглощение Света|r (|cffffffffQ|r)"

# A08A: Исцеление (Жрец) (Q)
wts_updates[5958] = "|cffe4cfa3Исцеление|r"
wts_updates[5959] = "|cffe4cfa3Исцеление|r (|cffffffffQ|r)"
wts_updates[6502] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет раненому живому союзнику |cffc8e08725|cffced4da ед. здоровья. Не действует на технику.|r"

# A08B: Рассеивание заклинаний (Жрец) (W)
wts_updates[5960] = "|cffe4cfa3Рассеивание заклинаний|r"
wts_updates[5961] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffW|r)"

# A08C: Очищающий Огонь (Монахиня, Жрец автокаст) (E)
wts_updates[5963] = "|cffe4cfa3Очищающий Огонь|r"
wts_updates[5964] = "|cffe4cfa3Очищающий Огонь|r (|cffffffffE|r)"

# A08D: Оглушающее попадание (Берсерк passive)
wts_updates[5978] = "|cffe4cfa3Оглушающее попадание|r"
wts_updates[5979] = "|cffe4cfa3Оглушающее попадание|r"
wts_updates[13105] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атака может нанести дополнительный урон и оглушить цель на |cffffffff1|cffced4da сек. (героев на |cffffffff0.3|cffced4da сек.).|r"

# A08E: Броня Берсерка (Берсерк passive)
wts_updates[5980] = "|cffe4cfa3Броня Берсерка|r"
wts_updates[5981] = "|cffe4cfa3Броня Берсерка|r"
wts_updates[5982] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает броню берсерка на |cffc8e087+3|cffced4da и отражает |cffc8e08715%|cffced4da урона ближнего боя в атакующих.|r"

# A08F: Критический удар (Гладиатор passive)
wts_updates[5984] = "|cffe4cfa3Критический удар|r"
wts_updates[5985] = "|cffe4cfa3Критический удар|r"

# A08G: Боевой клич (Гладиатор) (W)
wts_updates[26492] = "|cffe4cfa3Боевой клич|r"
wts_updates[38799] = "|cffe4cfa3Боевой клич|r (|cffffffffW|r)"
wts_updates[38818] = "|cffe4cfa3Боевой клич|r (|cffffffffW|r)"
wts_updates[6503] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак находящихся рядом союзников на |cffc8e087+15%|cffced4da на |cffffffff30|cffced4da сек. в радиусе |cffffffff500|cffced4da.|r"
wts_updates[13116] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак находящихся рядом союзников на |cffc8e087+15%|cffced4da на |cffffffff30|cffced4da сек. в радиусе |cffffffff500|cffced4da.|r"

# A08K: Аура Алого ордена (Инквизитор passive aura)
wts_updates[6055] = "|cffe4cfa3Аура Алого ордена|r"
wts_updates[6056] = "|cffe4cfa3Аура Алого ордена|r"
wts_updates[1705] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление здоровья союзников в радиусе |cffffffff400|cffced4da на |cffc8e087+0.5|cffced4da ед./сек.|r"

# A08L: Воскрешение (Инквизитор) (R)
wts_updates[39046] = "|cffe4cfa3Воскрешение|r"
wts_updates[39048] = "|cffe4cfa3Воскрешение|r (|cffffffffR|r)"
wts_updates[6046] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни |cffffffff1|cffced4da павшего союзного воина.|r"

# A08M: Массовая благодать (Инквизитор) (Q)
wts_updates[6047] = "|cffe4cfa3Массовая благодать|r"
wts_updates[6048] = "|cffe4cfa3Массовая благодать|r (|cffffffffQ|r)"
wts_updates[7204] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет |cffc8e087100|cffced4da ед. здоровья всем союзникам в радиусе |cffffffff300|cffced4da.|r"

# A08O: Рассекающий удар (Паладин юнит passive)
wts_updates[6061] = "|cffe4cfa3Рассекающий удар|r"
wts_updates[6059] = "|cffe4cfa3Рассекающий удар|r"
wts_updates[13107] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Удары паладина наносят |cffffffff7%|cffced4da урона соседним вражеским целям в радиусе |cffffffff200|cffced4da.|r"

# A08P: Аура Воеводы (Паладин юнит passive) (E)
wts_updates[6062] = "|cffe4cfa3Аура Воеводы|r"
wts_updates[6063] = "|cffe4cfa3Аура Воеводы|r"
wts_updates[6126] = "|cffe4cfa3Аура Воеводы|r"
wts_updates[13119] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак находящихся рядом союзников на |cffc8e087+10%|cffced4da в радиусе |cffffffff400|cffced4da.|r"
wts_updates[13578] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон от атак находящихся рядом союзников на |cffc8e087+10%|cffced4da в радиусе |cffffffff400|cffced4da.|r"

# A08X: Свет небес (Паладин юнит автокаст) (E)
wts_updates[6120] = "|cffe4cfa3Свет небес|r"
wts_updates[6119] = "|cffe4cfa3Свет небес|r (|cffffffffE|r)"
wts_updates[6121] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет |cffc8e087150|cffced4da ед. здоровья союзнику или наносит |cffffffff75|cffced4da ед. урона нежити.|r"

# A08Y: Свет небес (Паладин юнит таргет) (T)
wts_updates[6123] = "|cffe4cfa3Свет небес|r"
wts_updates[6124] = "|cffe4cfa3Свет небес|r (|cffffffffT|r)"

# A09O: Ненависть (Расовая пассивная аура всех воинов ордена)
wts_updates[6608] = "|cffe4cfa3Ненависть|r"
wts_updates[6609] = "|cffe4cfa3Ненависть|r"
wts_updates[35489] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Священная ненависть ордена замедляет регенерацию здоровья нежити в радиусе |cffffffff400|cffced4da на |cffe69a8d-1.0|cffced4da ед./сек.|r"

# =========================================================================
# 7. BUFFS (13)
# =========================================================================

# B01K: Молитва (Жрец)
wts_updates[5966] = "|cffe4cfa3Молитва|r"

# B01L: Броня Берсерка (Берсерк)
wts_updates[5989] = "|cffe4cfa3Броня Берсерка|r"

# B01M: Ярость (Гладиатор)
wts_updates[39268] = "|cffe4cfa3Ярость|r"

# B01N: Боевой клич (Гладиатор)
wts_updates[39163] = "|cffe4cfa3Боевой клич|r"

# B01P: Аура Алого ордена (Инквизитор)
wts_updates[6064] = "|cffe4cfa3Аура Алого ордена|r"

# B01R: Аура Воеводы (Паладин юнит)
wts_updates[6472] = "|cffe4cfa3Аура Воеводы|r"

# B01W: Аура Воеводы (Герой)
wts_updates[17826] = "|cffe4cfa3Аура Воеводы|r"
wts_updates[6473] = "(герой)"

# B01X: Кровотечение (Герой W)
wts_updates[6487] = "|cffe4cfa3Кровотечение|r"

# B01Y: Кровотечение (Герой W)
wts_updates[6504] = "|cffe4cfa3Кровотечение|r"

# B01Z: Ярость (Герой Q)
wts_updates[39269] = "|cffe4cfa3Ярость|r"
wts_updates[6547] = "(герой)"

# B020: Вдохновляющая Речь (Герой ult)
wts_updates[14839] = "|cffe4cfa3Вдохновляющая Речь|r"

# B021: Мольба к свету (Герой E)
wts_updates[6596] = "|cffe4cfa3Мольба к свету|r"

# B022: Ненависть (Расовая аура)
wts_updates[6611] = "|cffe4cfa3Ненависть|r"
wts_updates[6612] = "|cffa6afb8ЭФФЕКТ:|cffced4da Восстановление здоровья снижено под действием священной ненависти ордена.|r"

# =========================================================================
# 8. RESEARCHES (27)
# =========================================================================

# R040: Алый Орден (Цитадель)
wts_updates[6175] = "|cffe4cfa3Алый Орден|r"
wts_updates[6176] = "|cffe4cfa3Алый Орден|r"
wts_updates[6220] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Сохраняет верность классическому Алому Ордену, открывая обучение Паладинов Алого Ордена и Берсерков в Церкви.|n|n"
    "|cffa6afb8Бонусы:|cffced4da|n"
    "- Запас здоровья: |cffc8e087+50|cffced4da.|n"
    "- Запас маны: |cffc8e087+75|cffced4da.|n"
    "- Восстановление здоровья: |cffc8e087+3%|cffced4da.|n|n"
    "|cffe6c07bВнимание:|cffced4da исключает исследование |cffa9c7deАлый Натиск|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЦерковь Алого Ордена|cffced4da|n"
    "- |cffa9c7deВойска Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R03Z: Алый Натиск (Цитадель)
wts_updates[6168] = "|cffe4cfa3Алый Натиск|r"
wts_updates[6169] = "|cffe4cfa3Алый Натиск|r"
wts_updates[41177] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Преобразует армию в радикальный Алый Натиск, открывая обучение Инквизиторов и Гладиаторов в Церкви.|n|n"
    "|cffa6afb8Бонусы:|cffced4da|n"
    "- Урон от атак: |cffc8e087+6|cffced4da.|n"
    "- Скорость боя: |cffc8e087+15%|cffced4da.|n|n"
    "|cffe6c07bВнимание:|cffced4da исключает исследование |cffa9c7deАлый Орден|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЦерковь Алого Ордена|cffced4da|n"
    "- |cffa9c7deВойска Алого Натиска|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R03K: Укрыться за щитом (Казармы) (A)
wts_updates[5703] = "|cffe4cfa3Укрыться за щитом|r"
wts_updates[5714] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffA|r)"
wts_updates[5715] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает мечников использовать ростовой щит для защиты от стрел и отражения пронзающих атак.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deМечник|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R03L: Стальной наконечник болта (Казармы) (S)
wts_updates[5717] = "|cffe4cfa3Стальной наконечник болта|r"
wts_updates[5718] = "|cffe4cfa3Стальной наконечник болта|r (|cffffffffS|r)"
wts_updates[5719] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает арбалетчиков гранёными стальными наконечниками, повышая урон по целям с тяжёлой бронёй.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R03M: Улучшенная тетива (Казармы, 2 levels) (X)
wts_updates[38951] = "|cffe4cfa3Улучшенная тетива — уровень 1|r"
wts_updates[38966] = "|cffe4cfa3Улучшенная тетива — уровень 1|r (|cffffffffX|r)"
wts_updates[15145] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность стрельбы арбалетчиков на |cffc8e087+70|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/2|r"
)
wts_updates[39093] = "|cffe4cfa3Улучшенная тетива — уровень 2|r"
wts_updates[39094] = "|cffe4cfa3Улучшенная тетива — уровень 2|r (|cffffffffX|r)"
wts_updates[15146] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает дальность стрельбы арбалетчиков на |cffc8e087+70|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/2|r"
)

# R03V: Броня Алого Ордена (Казармы, 2 levels) (D)
wts_updates[39095] = "|cffe4cfa3Броня Алого Ордена — уровень 1|r"
wts_updates[39096] = "|cffe4cfa3Броня Алого Ордена — уровень 1|r (|cffffffffD|r)"
wts_updates[6131] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заковывает штурмовиков в латы, поглощающие |cffc8e0875|cffced4da ед. урона от каждой физической атаки.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deТяжелый Пехотинец|cffced4da|n"
    "- |cffa9c7deРыцарь Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/2|r"
)
wts_updates[39097] = "|cffe4cfa3Броня Алого Ордена — уровень 2|r"
wts_updates[39098] = "|cffe4cfa3Броня Алого Ордена — уровень 2|r (|cffffffffD|r)"
wts_updates[6134] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно укрепляет латы тяжёлой пехоты и рыцарей ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deТяжелый Пехотинец|cffced4da|n"
    "- |cffa9c7deРыцарь Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/2|r"
)

# R03W: Тяжелые Тренировки (Казармы) (D)
wts_updates[6136] = "|cffe4cfa3Тяжелые Тренировки|r"
wts_updates[6135] = "|cffe4cfa3Тяжелые Тренировки|r (|cffffffffD|r)"
wts_updates[6137] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Закаляет рыцарей в конных учениях, увеличивая урон на |cffc8e087+2|cffced4da и скорость боя на |cffc8e087+20%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРыцарь Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R03S: Длинный Арбалет (Мастерская, 2 levels) (A)
wts_updates[5892] = "|cffe4cfa3Длинный Арбалет — уровень 1|r"
wts_updates[5893] = "|cffe4cfa3Длинный Арбалет — уровень 1|r (|cffffffffA|r)"
wts_updates[15147] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность стрельбы арбалетчиков на |cffc8e087+100|cffced4da, но снижает скорость боя на |cffe69a8d-10%|cffced4da.|n|n"
    "|cffe6c07bВнимание:|cffced4da исключает исследование |cffa9c7deКороткий Арбалет|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/2|r"
)
wts_updates[5897] = "|cffe4cfa3Длинный Арбалет — уровень 2|r"
wts_updates[5898] = "|cffe4cfa3Длинный Арбалет — уровень 2|r (|cffffffffA|r)"
wts_updates[15148] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно совершенствует конструкцию длинного арбалета.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/2|r"
)

# R03T: Короткий Арбалет (Мастерская, 2 levels) (S)
wts_updates[5902] = "|cffe4cfa3Короткий Арбалет — уровень 1|r"
wts_updates[5903] = "|cffe4cfa3Короткий Арбалет — уровень 1|r (|cffffffffS|r)"
wts_updates[18138] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость стрельбы арбалетчиков на |cffc8e087+10%|cffced4da, но снижает дальность стрельбы на |cffe69a8d-100|cffced4da.|n|n"
    "|cffe6c07bВнимание:|cffced4da исключает исследование |cffa9c7deДлинный Арбалет|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/2|r"
)
wts_updates[5907] = "|cffe4cfa3Короткий Арбалет — уровень 2|r"
wts_updates[5908] = "|cffe4cfa3Короткий Арбалет — уровень 2|r (|cffffffffS|r)"
wts_updates[18173] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает скорострельность короткого арбалета.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/2|r"
)

# R03U: Горючая смесь (Мастерская) (W)
wts_updates[5976] = "|cffe4cfa3Горючая смесь|r"
wts_updates[5977] = "|cffe4cfa3Горючая смесь|r (|cffffffffW|r)"

# R03X: Вера в Пламя (Храм, 3 levels) (Z)
wts_updates[6139] = "|cffe4cfa3Вера в Пламя — уровень 1|r"
wts_updates[6141] = "|cffe4cfa3Вера в Пламя — уровень 1|r (|cffffffffZ|r)"
wts_updates[11722] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье жрецов и монахинь на |cffc8e087+25|cffced4da, запас маны на |cffc8e087+125|cffced4da, регенерацию маны на |cffc8e087+0.3|cffced4da/сек., а также открывает заклинание |cffa9c7deРассеивание заклинаний|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/3|r"
)
wts_updates[6140] = "|cffe4cfa3Вера в Пламя — уровень 2|r"
wts_updates[6142] = "|cffe4cfa3Вера в Пламя — уровень 2|r (|cffffffffZ|r)"
wts_updates[11723] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье жрецов и монахинь на |cffc8e087+25|cffced4da, ману на |cffc8e087+125|cffced4da и регенерацию маны на |cffc8e087+0.3|cffced4da/сек.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/3|r"
)
wts_updates[6147] = "|cffe4cfa3Вера в Пламя — уровень 3|r"
wts_updates[6146] = "|cffe4cfa3Вера в Пламя — уровень 3|r (|cffffffffZ|r)"
wts_updates[11724] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье жрецов и монахинь на |cffc8e087+25|cffced4da, ману на |cffc8e087+125|cffced4da и регенерацию маны на |cffc8e087+0.3|cffced4da/сек.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/3|r"
)

# R03Y: Просветление (Храм, 3 levels) (X)
wts_updates[39099] = "|cffe4cfa3Просветление — уровень 1|r"
wts_updates[39104] = "|cffe4cfa3Просветление — уровень 1|r (|cffffffffX|r)"
wts_updates[11725] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье жрецов и монахинь на |cffc8e087+40|cffced4da, запас маны на |cffc8e087+100|cffced4da, регенерацию маны на |cffc8e087+0.3|cffced4da/сек., а также совершенствует их чары.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/3|r"
)
wts_updates[39100] = "|cffe4cfa3Просветление — уровень 2|r"
wts_updates[39101] = "|cffe4cfa3Просветление — уровень 2|r (|cffffffffX|r)"
wts_updates[11726] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffc8e087+40|cffced4da, ману на |cffc8e087+100|cffced4da и регенерацию маны на |cffc8e087+0.3|cffced4da/сек.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/3|r"
)
wts_updates[39103] = "|cffe4cfa3Просветление — уровень 3|r"
wts_updates[39102] = "|cffe4cfa3Просветление — уровень 3|r (|cffffffffX|r)"
wts_updates[11727] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffc8e087+40|cffced4da, ману на |cffc8e087+100|cffced4da и регенерацию маны на |cffc8e087+0.3|cffced4da/сек.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deЖрец Алого Ордена|cffced4da|n"
    "- |cffa9c7deМонахиня Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/3|r"
)

# R041: Ярость Инквизиции (Церковь, 3 levels) (S)
wts_updates[6183] = "|cffe4cfa3Ярость Инквизиции — уровень 1|r"
wts_updates[6184] = "|cffe4cfa3Ярость Инквизиции — уровень 1|r (|cffffffffS|r)"
wts_updates[41810] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье инквизиторов на |cffc8e087+70|cffced4da и запас маны на |cffc8e087+50|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deИнквизитор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/3|r"
)
wts_updates[6190] = "|cffe4cfa3Ярость Инквизиции — уровень 2|r"
wts_updates[6192] = "|cffe4cfa3Ярость Инквизиции — уровень 2|r (|cffffffffS|r)"
wts_updates[41178] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье инквизиторов на |cffc8e087+70|cffced4da и запас маны на |cffc8e087+50|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deИнквизитор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/3|r"
)
wts_updates[6191] = "|cffe4cfa3Ярость Инквизиции — уровень 3|r"
wts_updates[6193] = "|cffe4cfa3Ярость Инквизиции — уровень 3|r (|cffffffffS|r)"
wts_updates[41224] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье инквизиторов на |cffc8e087+70|cffced4da и запас маны на |cffc8e087+50|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deИнквизитор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/3|r"
)

# R042: Учения Паладина (Церковь, 3 levels) (D)
wts_updates[6196] = "|cffe4cfa3Учения Паладина — уровень 1|r"
wts_updates[39164] = "|cffe4cfa3Учения Паладина — уровень 1|r (|cffffffffD|r)"
wts_updates[6198] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает регенерацию здоровья паладинов ордена на |cffc8e087+3%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/3|r"
)
wts_updates[6197] = "|cffe4cfa3Учения Паладина — уровень 2|r"
wts_updates[39165] = "|cffe4cfa3Учения Паладина — уровень 2|r (|cffffffffD|r)"
wts_updates[6206] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает регенерацию здоровья паладинов на |cffc8e087+3%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/3|r"
)
wts_updates[6202] = "|cffe4cfa3Учения Паладина — уровень 3|r"
wts_updates[39166] = "|cffe4cfa3Учения Паладина — уровень 3|r (|cffffffffD|r)"
wts_updates[6207] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает регенерацию здоровья паладинов на |cffc8e087+3%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/3|r"
)

# R043: Освящение молота (Церковь) (C)
wts_updates[6208] = "|cffe4cfa3Освящение молота|r"
wts_updates[6209] = "|cffe4cfa3Освящение молота|r (|cffffffffC|r)"
wts_updates[6210] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Освящает боевые молоты инквизиторов священным огнём, увеличивая урон на |cffc8e087+5|cffced4da и поджигая врагов.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deИнквизитор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R044: Тренировочные бои (Церковь, 2 levels) (A)
wts_updates[6228] = "|cffe4cfa3Тренировочные бои — уровень 1|r"
wts_updates[6229] = "|cffe4cfa3Тренировочные бои — уровень 1|r (|cffffffffA|r)"
wts_updates[18258] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Проводит регулярные учебные поединки, увеличивая скорость атаки воинов церкви на |cffc8e087+30%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da|n"
    "- |cffa9c7deБерсерк|cffced4da|n"
    "- |cffa9c7deГладиатор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/2|r"
)
wts_updates[6234] = "|cffe4cfa3Тренировочные бои — уровень 2|r"
wts_updates[6236] = "|cffe4cfa3Тренировочные бои — уровень 2|r (|cffffffffA|r)"
wts_updates[18264] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает скорость боя воинов церкви на |cffc8e087+30%|cffced4da.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deПаладин Алого Ордена|cffced4da|n"
    "- |cffa9c7deБерсерк|cffced4da|n"
    "- |cffa9c7deГладиатор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/2|r"
)

# R045: Улучшенная секира (Мастерская) (D)
wts_updates[6240] = "|cffe4cfa3Улучшенная секира|r"
wts_updates[6241] = "|cffe4cfa3Улучшенная секира|r (|cffffffffD|r)"
wts_updates[6242] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Перековывает секиры гладиаторов, обучая их наносить сокрушительные критические удары.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deГладиатор|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R046: Броня Берсерка (Мастерская) (X)
wts_updates[6251] = "|cffe4cfa3Броня Берсерка|r"
wts_updates[6252] = "|cffe4cfa3Броня Берсерка|r (|cffffffffX|r)"
wts_updates[39105] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает доспехи берсерков острыми шипами, увеличивая броню на |cffc8e087+3|cffced4da и отражая |cffc8e08715%|cffced4da урона ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deБерсерк|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R047: Зачарованные топоры (Мастерская) (Z)
wts_updates[6255] = "|cffe4cfa3Зачарованные топоры|r"
wts_updates[6256] = "|cffe4cfa3Зачарованные топоры|r (|cffffffffZ|r)"
wts_updates[6257] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Накладывает чары оглушения на топоры берсерков, давая шанс оглушить цель и нанести дополнительный урон.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deБерсерк|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R048: Учение Алого Ордена (Кузница) (E)
wts_updates[6613] = "|cffe4cfa3Учение Алого Ордена|r"
wts_updates[6614] = "|cffe4cfa3Учение Алого Ордена|r (|cffffffffE|r)"
wts_updates[20101] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Вселяет священную ненависть в сердца воинов, подавляя восстановление здоровья вражеской нежити рядом с ними.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВсе воины Алого Ордена|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/1|r"
)

# R049: Мечи (Кузница, 6 levels: Железные, Стальные, Мифриловые) (Q)
wts_updates[6616] = "|cffe4cfa3Железные мечи — уровень 1|r"
wts_updates[6622] = "|cffe4cfa3Железные мечи — уровень 1|r (|cffffffffQ|r)"
wts_updates[15154] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак воинов ближнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/6|r"
)
wts_updates[6618] = "|cffe4cfa3Железные мечи — уровень 2|r"
wts_updates[6623] = "|cffe4cfa3Железные мечи — уровень 2|r (|cffffffffQ|r)"
wts_updates[15155] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/6|r"
)
wts_updates[6617] = "|cffe4cfa3Стальные мечи — уровень 3|r"
wts_updates[6624] = "|cffe4cfa3Стальные мечи — уровень 3|r (|cffffffffQ|r)"
wts_updates[15156] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заменяет оружие на стальные клинки, повышая урон воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/6|r"
)
wts_updates[6621] = "|cffe4cfa3Стальные мечи — уровень 4|r"
wts_updates[6627] = "|cffe4cfa3Стальные мечи — уровень 4|r (|cffffffffQ|r)"
wts_updates[15151] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 4/6|r"
)
wts_updates[6620] = "|cffe4cfa3Мифриловые мечи — уровень 5|r"
wts_updates[6626] = "|cffe4cfa3Мифриловые мечи — уровень 5|r (|cffffffffQ|r)"
wts_updates[15152] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Выковывает клинки из мифрила, существенно повышая урон воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 5/6|r"
)
wts_updates[6619] = "|cffe4cfa3Мифриловые мечи — уровень 6|r"
wts_updates[6625] = "|cffe4cfa3Мифриловые мечи — уровень 6|r (|cffffffffQ|r)"
wts_updates[15153] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Достигает наивысшей заточки мифриловых мечей воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 6/6|r"
)

# R04A: Железная броня (Кузница, 6 levels: Железная, Стальная, Мифриловая) (A)
wts_updates[6638] = "|cffe4cfa3Железная броня — уровень 1|r"
wts_updates[6652] = "|cffe4cfa3Железная броня — уровень 1|r (|cffffffffA|r)"
wts_updates[20810] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню воинов ближнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/6|r"
)
wts_updates[6639] = "|cffe4cfa3Железная броня — уровень 2|r"
wts_updates[6651] = "|cffe4cfa3Железная броня — уровень 2|r (|cffffffffA|r)"
wts_updates[20811] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/6|r"
)
wts_updates[6640] = "|cffe4cfa3Стальная броня — уровень 3|r"
wts_updates[6650] = "|cffe4cfa3Стальная броня — уровень 3|r (|cffffffffA|r)"
wts_updates[20812] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заменяет железные доспехи на стальные, увеличивая защиту воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/6|r"
)
wts_updates[6643] = "|cffe4cfa3Стальная броня — уровень 4|r"
wts_updates[6655] = "|cffe4cfa3Стальная броня — уровень 4|r (|cffffffffA|r)"
wts_updates[15157] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает стальную броню воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 4/6|r"
)
wts_updates[6642] = "|cffe4cfa3Мифриловая броня — уровень 5|r"
wts_updates[6654] = "|cffe4cfa3Мифриловая броня — уровень 5|r (|cffffffffA|r)"
wts_updates[20808] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Выковывает доспехи из мифрила, существенно увеличивая защиту воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 5/6|r"
)
wts_updates[6641] = "|cffe4cfa3Мифриловая броня — уровень 6|r"
wts_updates[6653] = "|cffe4cfa3Мифриловая броня — уровень 6|r (|cffffffffA|r)"
wts_updates[20809] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Достигает наивысшей защиты мифриловой брони воинов ближнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины ближнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 6/6|r"
)

# R04B: Доспехи из клепаной кожи (Кузница, 6 levels) (S)
wts_updates[6660] = "|cffe4cfa3Доспехи из клепаной кожи — уровень 1|r"
wts_updates[6663] = "|cffe4cfa3Доспехи из клепаной кожи — уровень 1|r (|cffffffffS|r)"
wts_updates[20815] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню стрелков и воинов дальнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/6|r"
)
wts_updates[6661] = "|cffe4cfa3Доспехи из клепаной кожи — уровень 2|r"
wts_updates[6664] = "|cffe4cfa3Доспехи из клепаной кожи — уровень 2|r (|cffffffffS|r)"
wts_updates[20816] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков и воинов дальнего боя Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/6|r"
)
wts_updates[6662] = "|cffe4cfa3Доспехи из армированной кожи — уровень 3|r"
wts_updates[6665] = "|cffe4cfa3Доспехи из армированной кожи — уровень 3|r (|cffffffffS|r)"
wts_updates[20817] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заменяет клепаную кожу на армированную, увеличивая защиту воинов дальнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/6|r"
)
wts_updates[6671] = "|cffe4cfa3Доспехи из армированной кожи — уровень 4|r"
wts_updates[6668] = "|cffe4cfa3Доспехи из армированной кожи — уровень 4|r (|cffffffffS|r)"
wts_updates[15158] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает армированные доспехи воинов дальнего боя.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 4/6|r"
)
wts_updates[6670] = "|cffe4cfa3Доспехи из драконьей кожи — уровень 5|r"
wts_updates[6667] = "|cffe4cfa3Доспехи из драконьей кожи — уровень 5|r (|cffffffffS|r)"
wts_updates[20813] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Изготавливает доспехи из чешуи драконов, значительно повышая защиту стрелков.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 5/6|r"
)
wts_updates[6669] = "|cffe4cfa3Доспехи из драконьей кожи — уровень 6|r"
wts_updates[6666] = "|cffe4cfa3Доспехи из драконьей кожи — уровень 6|r (|cffffffffS|r)"
wts_updates[20814] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Достигает наивысшей прочности доспехов из драконьей кожи.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deВоины дальнего боя|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 6/6|r"
)

# R04C: Меткость (Кузница, 6 levels) (W)
wts_updates[6682] = "|cffe4cfa3Меткость — уровень 1|r"
wts_updates[6688] = "|cffe4cfa3Меткость — уровень 1|r (|cffffffffW|r)"
wts_updates[15162] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от дистанционных атак стрелков и сторожевых башен Алого Ордена.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/6|r"
)
wts_updates[6683] = "|cffe4cfa3Меткость — уровень 2|r"
wts_updates[6689] = "|cffe4cfa3Меткость — уровень 2|r (|cffffffffW|r)"
wts_updates[15163] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от дистанционных атак стрелков и башен.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/6|r"
)
wts_updates[6684] = "|cffe4cfa3Меткость — уровень 3|r"
wts_updates[6690] = "|cffe4cfa3Меткость — уровень 3|r (|cffffffffW|r)"
wts_updates[15164] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от дистанционных атак стрелков и башен.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/6|r"
)
wts_updates[6685] = "|cffe4cfa3Меткость — уровень 4|r"
wts_updates[6691] = "|cffe4cfa3Меткость — уровень 4|r (|cffffffffW|r)"
wts_updates[15159] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от дистанционных атак стрелков и башен.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 4/6|r"
)
wts_updates[6686] = "|cffe4cfa3Меткость — уровень 5|r"
wts_updates[6692] = "|cffe4cfa3Меткость — уровень 5|r (|cffffffffW|r)"
wts_updates[15160] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от дистанционных атак стрелков и башен.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 5/6|r"
)
wts_updates[6687] = "|cffe4cfa3Меткость — уровень 6|r"
wts_updates[6693] = "|cffe4cfa3Меткость — уровень 6|r (|cffffffffW|r)"
wts_updates[15161] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Достигает наивысшей меткости и дальнобойного урона стрелков и сторожевых башен.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deАрбалетчик|cffced4da|n"
    "- |cffa9c7deСторожевая Башня|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 6/6|r"
)

# R07B: Маркер расы Алый Орден
wts_updates[7373] = "|cffe4cfa3Алый Орден|r"
wts_updates[7508] = "|cffe4cfa3Алый Орден|r"
wts_updates[5597] = (
    "|cffa6afb8РАСА:|cffced4da Религиозно-военная организация людей бывшего королевства Лордерон, поставившая своей целью искоренение нежити и очищение земель Азерота священным огнём.|r"
)

# R0KG: Улучшенная кладка (Лесопилка)
wts_updates[39121] = "|cffe4cfa3Улучшенная кладка|r"

# R0KH: Улучшенные инструменты (Лесопилка, 6 levels) (Z)
wts_updates[6129] = "|cffe4cfa3Улучшенные инструменты — уровень 1|r"
wts_updates[6261] = "|cffe4cfa3Улучшенные инструменты — уровень 1|r (|cffffffffZ|r)"
wts_updates[39144] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём переносимой работниками древесины на |cffc8e087+6|cffced4da ед.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 1/6|r"
)
wts_updates[6130] = "|cffe4cfa3Улучшенные инструменты — уровень 2|r"
wts_updates[6263] = "|cffe4cfa3Улучшенные инструменты — уровень 2|r (|cffffffffZ|r)"
wts_updates[39139] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём переносимой древесины на |cffc8e087+6|cffced4da ед.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 2/6|r"
)
wts_updates[6132] = "|cffe4cfa3Улучшенные инструменты — уровень 3|r"
wts_updates[6465] = "|cffe4cfa3Улучшенные инструменты — уровень 3|r (|cffffffffZ|r)"
wts_updates[39140] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём переносимой древесины на |cffc8e087+6|cffced4da ед.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 3/6|r"
)
wts_updates[6133] = "|cffe4cfa3Улучшенные инструменты — уровень 4|r"
wts_updates[6484] = "|cffe4cfa3Улучшенные инструменты — уровень 4|r (|cffffffffZ|r)"
wts_updates[39141] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём переносимой древесины на |cffc8e087+6|cffced4da ед.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 4/6|r"
)
wts_updates[6248] = "|cffe4cfa3Улучшенные инструменты — уровень 5|r"
wts_updates[6485] = "|cffe4cfa3Улучшенные инструменты — уровень 5|r (|cffffffffZ|r)"
wts_updates[39142] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём переносимой древесины на |cffc8e087+6|cffced4da ед.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 5/6|r"
)
wts_updates[6253] = "|cffe4cfa3Улучшенные инструменты — уровень 6|r"
wts_updates[6488] = "|cffe4cfa3Улучшенные инструменты — уровень 6|r (|cffffffffZ|r)"
wts_updates[39143] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Достигает максимального объёма заготовки древесины работниками.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n"
    "- |cffa9c7deРаботник|cffced4da|n"
    "- |cffa9c7deДровосек|cffced4da|n|n"
    "|cffa6afb8Уровень исследования:|cffffffff 6/6|r"
)

# =========================================================================
# VALIDATION AND CHECKS_DEF
# =========================================================================

# Validate all string IDs exist in war3map.wts
missing = [sid for sid in wts_updates if not check_wts_has(sid)]
if missing:
    print(f"ERROR: {len(missing)} missing WTS IDs: {missing}")
    sys.exit(1)

print(f"Total verified WTS updates for Scarlet Crusade: {len(wts_updates)}")

# Build verification checks definition for HiveWE readback
checks_def = []

# Selection check
checks_def.append({"type": "ability", "id": "A0HM", "field": "name", "expected_sid": 38865})
checks_def.append({"type": "ability", "id": "A0HM", "field": "tip1", "expected_sid": 38866})
checks_def.append({"type": "ability", "id": "A0HM", "field": "ubertip1", "expected_sid": 11204})

# Buildings check
bld_check_map = {
    'h05U': (17404, 17405, 12539),
    'h05V': (17406, 17407, 12962),
    'h05W': (17408, 17409, 12963),
    'h05X': (17410, 17411, 9278),
    'h05Y': (17412, 17413, 31660),
    'h05Z': (17415, 17416, 12982),
    'h060': (17417, 17418, 20437),
    'h061': (17258, 17259, 12971),
    'h062': (17419, 17420, 12985),
    'h063': (17260, 17261, 8049),
    'h064': (17421, 17422, 12987),
    'h068': (17264, 17265, 12988),
}
for bid, (nsid, tsid, usid) in bld_check_map.items():
    checks_def.append({"type": "unit", "id": bid, "field": "name", "expected_sid": nsid})
    checks_def.append({"type": "unit", "id": bid, "field": "tip", "expected_sid": tsid})
    checks_def.append({"type": "unit", "id": bid, "field": "ubertip", "expected_sid": usid})

# Heroes check
hero_check_map = {
    'H03H': (861, 6477, 31647),
    'H06C': (6549, 6552, 31673),
    'H06B': (6479, 6482, 31672),
}
for hid, (nsid, tsid, usid) in hero_check_map.items():
    checks_def.append({"type": "unit", "id": hid, "field": "name", "expected_sid": nsid})
    checks_def.append({"type": "unit", "id": hid, "field": "tip", "expected_sid": tsid})
    checks_def.append({"type": "unit", "id": hid, "field": "ubertip", "expected_sid": usid})

# Units check
unit_check_map = {
    'h014': (5249, 5250, 13415),
    'h039': (5311, 5312, 16938),
    'h03A': (5251, 5252, 19302),
    'h03B': (5253, 5254, 19447),
    'h03C': (5255, 5256, 31643),
    'h03D': (5257, 5258, 25177),
    'h03F': (5259, 5260, 20904),
    'h03G': (5261, 5262, 21283),
    'h03I': (8785, 14748, 21611),
    'h065': (5300, 5301, 21616),
    'h066': (5302, 5303, 21617),
    'h067': (5306, 5307, 21618),
    'n007': (5247, 5248, 21615),
    'n008': (1231, 919, 22381),
    'o00I': (1232, 1233, 24741),
}
for uid, (nsid, tsid, usid) in unit_check_map.items():
    checks_def.append({"type": "unit", "id": uid, "field": "name", "expected_sid": nsid})
    checks_def.append({"type": "unit", "id": uid, "field": "tip", "expected_sid": tsid})
    checks_def.append({"type": "unit", "id": uid, "field": "ubertip", "expected_sid": usid})

# Hero Abilities and Upgrades use direct WTS strings validated via regex and dry-run

plan_payload = {
    "race": "Scarlet Crusade",
    "total_wts_updates": len(wts_updates),
    "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
    "checks_def": checks_def
}

docs_dir = ROOT / "docs/ui_text"
docs_dir.mkdir(parents=True, exist_ok=True)
plan_file = docs_dir / "scarlet_plan.json"
plan_file.write_text(json.dumps(plan_payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Plan saved to {plan_file} ({len(wts_updates)} updates, {len(checks_def)} checks)")
