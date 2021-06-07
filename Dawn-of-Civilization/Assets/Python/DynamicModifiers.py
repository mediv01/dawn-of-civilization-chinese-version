from CvPythonExtensions import *
from Consts import *
from RFCUtils import utils

import Modifiers

'''
#动态科研系数、造兵成本和建筑成本，跟年代挂钩
'''

iNumModifiers = 13
(iModifierCulture, iModifierUnitUpkeep, iModifierResearchCost, iModifierDistanceMaintenance, iModifierCitiesMaintenance,
 iModifierCivicUpkeep, iModifierHealth, iModifierUnitCost, iModifierWonderCost, iModifierBuildingCost,
 iModifierInflationRate, iModifierGreatPeopleThreshold, iModifierGrowthThreshold) = range(iNumModifiers)

ModifiersName = (
    'iModifierCulture', 'iModifierUnitUpkeep', 'iModifierResearchCost', 'iModifierDistanceMaintenance', 'iModifierCitiesMaintenance',
    'iModifierCivicUpkeep', 'iModifierHealth', 'iModifierUnitCost', 'iModifierWonderCost', 'iModifierBuildingCost',
    'iModifierInflationRate', 'iModifierGreatPeopleThreshold', 'iModifierGrowthThreshold'
)

bHistoryFortuneAI = (gc.getDefineINT("PYTHON_ALLOW_HISTORY_FORTUNE_TO_AI") > 0)
bHistoryFortuneHuman = (gc.getDefineINT("PYTHON_ALLOW_HISTORY_FORTUNE_TO_HUMAN") > 0)
bHistoryFortune = bHistoryFortuneAI or bHistoryFortuneHuman


def logSetModifiers(iPlayer, iModifier):
    NewModifier = gc.getPlayer(iPlayer).getModifier(iModifier)
    txt = utils.getCivName(iPlayer) + ' Modifier of ' + ModifiersName[iModifier] + ' is ' + str(NewModifier)
    utils.log2(txt, 'DoC_SmallMap_Log_ModifiersChange')
    pass


# 直接设置
def setModifier(iPlayer, iModifier, iModifierNew):
    Modifiers.setModifier(iPlayer, iModifier, iModifierNew)
    logSetModifiers(iPlayer, iModifier)


# 倍数，不推荐使用
'''
def adjustModifier(iPlayer, iModifier, iPercent):
    Modifiers.setModifier(iPlayer, iModifier, gc.getPlayer(iPlayer).getModifier(iModifier) * iPercent / 100)
'''


def checkturn(iGameTurn):
    if (not bHistoryFortune): return

    adjustChina()
    adjustRussia()
    adjustByzantium()
    adjustArabia()
    adjustItaly()
    adjustEngland()

    # adjusthuman()  #测试使用


def logSetModifiersAll(iPlayer):
    for iModifier in range(iNumModifiers):
        logSetModifiers(iPlayer, iModifier)
    pass


def checkpass(iPlayer):
    bHuman = (utils.getHumanID() == iPlayer)
    if (bHuman):
        if not bHistoryFortuneHuman:
            return True
    else:
        if not bHistoryFortuneAI:
            return True

    return False

def adjustEngland():
    iPlayer = iEngland
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 第一次工业革命
    if iGameTurn == getTurnForYear(1750):
        setModifier(iPlayer, iModifierCulture, 150)
        setModifier(iPlayer, iModifierResearchCost, 70)
        setModifier(iPlayer, iModifierBuildingCost, 70)
        setModifier(iPlayer, iModifierUnitCost, 70)
        setModifier(iPlayer, iModifierWonderCost, 70)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 70)
        pass


    # 第二次工业革命结束
    if iGameTurn == getTurnForYear(1860):
        setModifier(iPlayer, iModifierCulture, 120)
        setModifier(iPlayer, iModifierResearchCost, 100)
        setModifier(iPlayer, iModifierBuildingCost, 100)
        setModifier(iPlayer, iModifierUnitCost, 100)
        setModifier(iPlayer, iModifierWonderCost, 100)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 100)
        pass

def adjustItaly():
    iPlayer = iItaly
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 意大利文艺复兴
    if iGameTurn == getTurnForYear(1300):
        setModifier(iPlayer, iModifierCulture, 200)
        setModifier(iPlayer, iModifierResearchCost, 50)
        setModifier(iPlayer, iModifierBuildingCost, 60)
        setModifier(iPlayer, iModifierUnitCost, 60)
        setModifier(iPlayer, iModifierWonderCost, 60)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 50)
        pass


    # 意大利文艺复兴结束
    if iGameTurn == getTurnForYear(1600):
        setModifier(iPlayer, iModifierCulture, 120)
        setModifier(iPlayer, iModifierResearchCost, 80)
        setModifier(iPlayer, iModifierBuildingCost, 80)
        setModifier(iPlayer, iModifierUnitCost, 80)
        setModifier(iPlayer, iModifierWonderCost, 80)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 80)
        pass


def adjustByzantium():
    iPlayer = iByzantium
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 拜占庭衰落
    if iGameTurn == getTurnForYear(1000):
        setModifier(iPlayer, iModifierResearchCost, 125)
        setModifier(iPlayer, iModifierBuildingCost, 125)
        setModifier(iPlayer, iModifierUnitCost, 125)
        setModifier(iPlayer, iModifierWonderCost, 125)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 125)
        pass


def adjustArabia():
    iPlayer = iArabia
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 阿拉伯衰落
    if iGameTurn == getTurnForYear(1000):
        setModifier(iPlayer, iModifierResearchCost, 125)
        setModifier(iPlayer, iModifierBuildingCost, 125)
        setModifier(iPlayer, iModifierUnitCost, 125)
        setModifier(iPlayer, iModifierWonderCost, 125)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 125)
        pass


def adjustRussia():
    iPlayer = iRussia  # 俄罗斯
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 俄国黄金时代1
    if iGameTurn == getTurnForYear(1710):
        setModifier(iPlayer, iModifierResearchCost, 100)
        setModifier(iPlayer, iModifierBuildingCost, 100)
        setModifier(iPlayer, iModifierUnitCost, 100)
        setModifier(iPlayer, iModifierWonderCost, 100)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 85)
        pass

    # 俄国黄金时代1结束
    if iGameTurn == getTurnForYear(1800):
        setModifier(iPlayer, iModifierResearchCost, 120)
        setModifier(iPlayer, iModifierBuildingCost, 120)
        setModifier(iPlayer, iModifierUnitCost, 120)
        setModifier(iPlayer, iModifierWonderCost, 120)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 100)
        pass

    # 俄国黑暗时期
    if iGameTurn == getTurnForYear(1850):
        setModifier(iPlayer, iModifierResearchCost, 140)
        setModifier(iPlayer, iModifierBuildingCost, 140)
        setModifier(iPlayer, iModifierUnitCost, 140)
        setModifier(iPlayer, iModifierWonderCost, 140)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 120)
        pass

    # 苏联时期
    if iGameTurn == getTurnForYear(1918):
        setModifier(iPlayer, iModifierResearchCost, 80)
        setModifier(iPlayer, iModifierBuildingCost, 75)
        setModifier(iPlayer, iModifierUnitCost, 70)
        setModifier(iPlayer, iModifierWonderCost, 75)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 150)
        pass

    # 苏联后期
    if iGameTurn == getTurnForYear(1970):
        setModifier(iPlayer, iModifierResearchCost, 110)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 150)
        pass


def adjustChina():
    iPlayer = iChina  # 中国
    iGameTurn = gc.getGame().getGameTurn()
    if (checkpass(iPlayer)): return

    # 春秋时期 伟人层出不穷，科研和伟人速度增加  但是战乱导致建筑成本和征兵成本上升
    if iGameTurn == getTurnForYear(-770):
        setModifier(iPlayer, iModifierResearchCost, 70)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 60)
        pass

    # 秦汉时期 大一统王朝 征兵费用、建筑成本和奇观成本下降  焚书坑儒、罢黜百家独尊儒术导致科研和伟人速率下降
    if iGameTurn == getTurnForYear(-220):
        setModifier(iPlayer, iModifierResearchCost, 110)
        setModifier(iPlayer, iModifierBuildingCost, 80)
        setModifier(iPlayer, iModifierUnitCost, 80)
        setModifier(iPlayer, iModifierWonderCost, 80)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 120)
        pass

    # 三国时期 伟人层出不穷 但是战乱导致建筑成本和征兵成本上升
    if iGameTurn == getTurnForYear(220):
        setModifier(iPlayer, iModifierResearchCost, 80)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 90)
        pass

    # 隋唐时期 贞观之治至开元盛世
    if iGameTurn == getTurnForYear(618):
        setModifier(iPlayer, iModifierResearchCost, 50)
        setModifier(iPlayer, iModifierBuildingCost, 70)
        setModifier(iPlayer, iModifierUnitCost, 70)
        setModifier(iPlayer, iModifierWonderCost, 70)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 70)
        pass

    # 安史之乱 第一个盛世结束
    if iGameTurn == getTurnForYear(755):
        setModifier(iPlayer, iModifierResearchCost, 100)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 120)
        pass

    # 北宋 商业活动频繁 伟人也不少 科研也还行  但是军事实力弱
    if iGameTurn == getTurnForYear(960):
        setModifier(iPlayer, iModifierResearchCost, 100)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 120)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 90)
        pass

    # 南宋的黑暗时期
    if iGameTurn == getTurnForYear(1127):
        setModifier(iPlayer, iModifierResearchCost, 110)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 110)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 100)
        pass

    # 明朝盛世
    if iGameTurn == getTurnForYear(1368):
        setModifier(iPlayer, iModifierResearchCost, 90)
        setModifier(iPlayer, iModifierBuildingCost, 80)
        setModifier(iPlayer, iModifierUnitCost, 80)
        setModifier(iPlayer, iModifierWonderCost, 80)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 100)
        pass

    # 明朝后期 开始闭关锁国 科研技术开始落后 思想禁锢伟人也开始下降
    if iGameTurn == getTurnForYear(1600):
        setModifier(iPlayer, iModifierResearchCost, 120)
        setModifier(iPlayer, iModifierBuildingCost, 80)
        setModifier(iPlayer, iModifierUnitCost, 80)
        setModifier(iPlayer, iModifierWonderCost, 80)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 130)
        pass

    # 乾隆时期 与西方国家的差距进一步拉大
    if iGameTurn == getTurnForYear(1730):
        setModifier(iPlayer, iModifierResearchCost, 130)
        setModifier(iPlayer, iModifierBuildingCost, 110)
        setModifier(iPlayer, iModifierUnitCost, 110)
        setModifier(iPlayer, iModifierWonderCost, 100)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 150)
        pass

    # 近代史的黑暗时期
    if iGameTurn == getTurnForYear(1840):
        setModifier(iPlayer, iModifierResearchCost, 150)
        setModifier(iPlayer, iModifierBuildingCost, 120)
        setModifier(iPlayer, iModifierUnitCost, 120)
        setModifier(iPlayer, iModifierWonderCost, 120)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 200)
        pass

    # 新中国
    if iGameTurn == getTurnForYear(1950):
        setModifier(iPlayer, iModifierResearchCost, 75)
        setModifier(iPlayer, iModifierBuildingCost, 75)
        setModifier(iPlayer, iModifierUnitCost, 75)
        setModifier(iPlayer, iModifierWonderCost, 75)
        setModifier(iPlayer, iModifierGreatPeopleThreshold, 75)
        pass


def adjustHuman():
    iPlayer = utils.getHumanID()
    iGameTurn = gc.getGame().getGameTurn()

    bHuman = (utils.getHumanID() == iPlayer)
    if (bHuman):
        if not bHistoryFortuneHuman:
            return
    else:
        if not bHistoryFortuneAI:
            return
