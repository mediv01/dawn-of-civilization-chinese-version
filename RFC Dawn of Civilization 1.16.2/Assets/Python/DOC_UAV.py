from CvPythonExtensions import *
from StoredData import data
from Consts import *
import Consts as con
from RFCUtils import utils
from UAVUtils import *
import heapq
import Areas
import CityNameManager as cnm
import DynamicCivs as dc





# (iAncient, iClassical, iMedieval, iRenaissance, iIndustrial, iGlobal, iDigital)
# 远古时代：首都建造2座奇观，并且文化达到4级；
# 古典时代：首都人口达到10以上，首都所在区域没有其他文明的城市，拥有6座以上的城市；
# 中古时代：拥有3个以上的附庸，人口、军力、文化同时为世界第一；
# 启蒙时代：有3个以上的文明对你亲密，科研、文化、商业同时为世界第一；
# 工业时代：在5个以上的地区拥有殖民地；工业、军力、商业同时为世界第一；

# 远古时代：首都建造2座奇观，并且文化达到4级；


def getScreenHelp():
    aHelp = []
    aHelp.append(localText.getText("TXT_KEY_VICTORY_UAV01_TECH", ()))
    aHelp.append(str(data.UAVGoals[0]))
    aHelp.append(str(data.UAVGoals[1]))


    aHelp.append(" ")
    aHelp.append(" ")
    aHelp.append(" ")
    aHelp.append(" ")
    return aHelp

def CheckTurn(iGameTurn):
    pass


def UAV1(iPlayer):
    if not gc.getPlayer(iPlayer).isAlive():
        return False
    pCapital = gc.getPlayer(iPlayer).getCapitalCity()
    # 远古时代
    condition1 = gc.getPlayer(iPlayer).getCurrentEra() == iAncient
    # 首都建造2座奇观
    condition2 = countCityWonders(iPlayer, (pCapital.getX(), pCapital.getY())) >= 2
    # 首都文化达到4级
    condition3 = pCapital.getCulture(iPlayer) >= gc.getCultureLevelInfo(4).getSpeedThreshold(gc.getGame().getGameSpeedType())

    if condition1 and condition2 and condition3:
        return True
    return False


# 古典时代：首都人口达到10以上，首都所在区域没有其他文明的城市，拥有6座以上的城市
def UAV2(iPlayer):
    if not gc.getPlayer(iPlayer).isAlive():
        return False
    pCapital = gc.getPlayer(iPlayer).getCapitalCity()
    # 古典时代
    condition1 = gc.getPlayer(iPlayer).getCurrentEra() == iClassical
    # 首都人口达到10以上
    condition2 = pCapital.getPopulation() >= 10
    # 首都所在区域没有其他文明的城市

    # 拥有6座以上的城市
    condition3 = gc.getPlayer(iPlayer).getNumCities() >= 6

    if condition1 and condition2 and condition3:
        return True
    return False


# 中古时代：拥有3个以上的附庸，人口、军力、文化同时为世界第一；
def UAV3(iPlayer):
    if not gc.getPlayer(iPlayer).isAlive():
        return False
    # 中古时代
    condition1 = gc.getPlayer(iPlayer).getCurrentEra() == iMedieval
    # 拥有3个以上的附庸
    condition2 = getNumVassals(iPlayer) >= 3
    # 人口为世界第一
    condition3 = isHighestPopulation(iPlayer)
    # 军力为世界第一
    condition4 = isTopPower(iPlayer)
    # 文化为世界第一
    condition5 = isTopCulture(iPlayer)

    if condition1 and condition2 and condition3 and condition4 and condition5:
        return True
    return False


# 启蒙时代：有3个以上的文明对你亲密，科研、文化、商业同时为世界第一；
def UAV4(iPlayer):
    if not gc.getPlayer(iPlayer).isAlive():
        return False

    # 启蒙时代
    condition1 = gc.getPlayer(iPlayer).getCurrentEra() == iRenaissance
    # 有3个以上的文明对你亲密
    condition2 = countPlayersWithAttitude(iPlayer, AttitudeTypes.ATTITUDE_FRIENDLY) >= 3
    # 科研为世界第一
    condition3 = isTopTech(iPlayer)
    # 文化为世界第一
    condition4 = isTopCulture(iPlayer)
    # 商业为世界第一
    condition5 = isMostCommerce(iPlayer)

    if condition1 and condition2 and condition3 and condition4 and condition5:
        return True
    return False


# 工业时代：在5个以上的地区拥有殖民地；工业、军力、商业同时为世界第一；
def UAV5(iPlayer):
    if not gc.getPlayer(iPlayer).isAlive():
        return False

    # 工业时代
    condition1 = gc.getPlayer(iPlayer).getCurrentEra() == iIndustrial

    # 工业为世界第一
    condition2 = isMostProductive(iPlayer)
    # 军力为世界第一
    condition3 = isTopPower(iPlayer)
    # 商业为世界第一
    condition4 = isMostCommerce(iPlayer)

    # 在5个以上的地区拥有殖民地
    # bNAmerica = getNumCitiesInArea(iEngland, utils.getPlotList(tNorthAmericaTL, tNorthAmericaBR)) < 5
    # bSCAmerica = getNumCitiesInArea(iEngland, utils.getPlotList(tSouthCentralAmericaTL, tSouthCentralAmericaBR)) < 3
    # bAfrica = getNumCitiesInArea(iEngland, utils.getPlotList(tAfricaTL, tAfricaBR)) < 4
    # bAsia = getNumCitiesInArea(iEngland, utils.getPlotList(tAsiaTL, tAsiaBR)) < 6
    # bOceania = getNumCitiesInArea(iEngland, utils.getPlotList(tOceaniaTL, tOceaniaBR)) < 6

    if condition1 and condition2 and condition3 and condition4:
        return True
    return False

