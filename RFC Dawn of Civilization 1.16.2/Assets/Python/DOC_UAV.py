from CvPythonExtensions import *
from StoredData import data
from Consts import *
import Consts as con
from RFCUtils import utils
import heapq
import Areas
import CityNameManager as cnm
import DynamicCivs as dc
import BugCore

### GLOBALS ###

gc = CyGlobalContext()
localText = CyTranslator()


# (iAncient, iClassical, iMedieval, iRenaissance, iIndustrial, iGlobal, iDigital)
# 远古时代：首都建造2座奇观，并且文化达到4级；
# 古典时代：首都人口达到10以上，首都所在区域没有其他文明的城市，拥有6座以上的城市；
# 中古时代：拥有3个以上的附庸，人口、军力、文化同时为世界第一；
# 启蒙时代：有3个以上的文明对你亲密，科研、文化、商业同时为世界第一；
# 工业时代：在5个以上的地区拥有殖民地；工业、军力、商业同时为世界第一；

# 远古时代：首都建造2座奇观，并且文化达到4级；

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

    return False


def getNumVassals(iPlayer):
    """Returns the number of vassals belonging to iPlayer."""
    iCounter = 0
    for iCiv in range(con.iNumPlayers):
        if iCiv != iPlayer:
            if gc.getPlayer(iCiv).isAlive():
                if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iPlayer):
                    iCounter += 1
    return iCounter


def isTopTech(self, iPlayer):
    """Checks whether iPlayer has accumulated the higest amount of Science."""
    iNumTotalTechs = gc.getNumTechInfos()
    bTopTech = True
    iNumTechs = 0
    for iTechLoop in range(iNumTotalTechs):
        if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTechLoop):
            iNumTechs += 1
    for iPlayerLoop in range(con.iNumPlayers):
        if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
            iPlayerNumTechs = 0
            for iTechLoop in range(iNumTotalTechs):
                if gc.getTeam(gc.getPlayer(iPlayerLoop).getTeam()).isHasTech(iTechLoop):
                    iPlayerNumTechs = iPlayerNumTechs + 1
            if iPlayerNumTechs >= iNumTechs:
                bTopTech = False
                break
    return bTopTech


def isTopCulture(iPlayer):
    """Checks whether iPlayer has accumulated the higest number of Culture."""
    bTopCulture = True
    iCulture = gc.getPlayer(iPlayer).countTotalCulture()
    for iPlayerLoop in range(con.iNumPlayers):
        if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
            if gc.getPlayer(iPlayerLoop).countTotalCulture() > iCulture:
                bTopCulture = False
                break
    return bTopCulture


def isHighestPopulation(iPlayer):
    """Checks whether iPlayer has the highest total population."""
    iPop = gc.getPlayer(iPlayer).getRealPopulation()
    bHighest = True
    for iLoopCiv in range(con.iNumPlayers):
        if iPop < gc.getPlayer(iLoopCiv).getRealPopulation():
            bHighest = False
            break
    return bHighest


def isMostProductive(iPlayer):
    """Checks whether iPlayer has the highest amount of total Production in this cities."""
    iTopValue = 0
    iTopCiv = -1
    for iLoopPlayer in range(con.iNumPlayers):
        pLoopPlayer = gc.getPlayer(iLoopPlayer)
        if pLoopPlayer.getNumCities() > 0:
            iValue = pLoopPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
            if iValue > iTopValue:
                iTopValue = iValue
                iTopCiv = iLoopPlayer
    return (iTopCiv == iPlayer)


def isHasLegendaryCity(iPlayer):
    """Checks whether iPlayer has a city with Legendary culture."""
    apCityList = PyPlayer(iPlayer).getCityList()
    for pCity in apCityList:
        if pCity.GetCy().getCultureTimes100(iPlayer) >= utils.getTurns(2500000):
            return True
    return False


# def isMostCommerce(iPlayer):
#    """Checks whether iPlayer has the highest amount of total Commerce in this cities."""
#    iTopValue = 0
#    iTopCiv = -1
#    for iLoopPlayer in range(con.iNumPlayers):
#        iValue = gc.getPlayer(iLoopPlayer).calculateTotalYield(YieldTypes.YIELD_COMMERCE)
#        if iValue > iTopValue:
#            iTopValue = iValue
#            iTopCiv = iLoopPlayer
#           
#    return iPlayer == iTopCiv

def isMostCommerce(iPlayer):
    """Checks whether iPlayer has the highest amount of total Commerce in this cities."""
    iTopValue = 0
    iTopCiv = -1
    for iLoopPlayer in range(con.iNumPlayers):
        iValue = gc.getPlayer(iLoopPlayer).calculateTotalCommerce()
        if iValue > iTopValue:
            iTopValue = iValue
            iTopCiv = iLoopPlayer

    return iPlayer == iTopCiv


def isTopPower(iPlayer):
    iTopValue = 0
    iTopCiv = -1
    for iLoopPlayer in range(con.iNumPlayers):
        iValue = gc.getPlayer(iLoopPlayer).getPower()
        if iValue > iTopValue:
            iTopValue = iValue
            iTopCiv = iLoopPlayer

    return iPlayer == iTopCiv

def getWonderList():
    lBuildings = []
    lWonders = []
    for i in xrange(gc.getNumBuildingInfos()):
        Info = gc.getBuildingInfo(i)
        if isLimitedWonderClass(Info.getBuildingClassType()):
            lWonders.append(i)
        else:
            lBuildings.append(i)

    return lWonders

def countCityWonders(iPlayer, tPlot, bIncludeObsolete=False):
    iCount = 0
    x, y = tPlot
    plot = gc.getMap().plot(x, y)
    if not plot.isCity(): return 0
    if plot.getPlotCity().getOwner() != iPlayer: return 0

    lWonders = getWonderList()

    for iWonder in lWonders:
        iObsoleteTech = gc.getBuildingInfo(iWonder).getObsoleteTech()
        if not bIncludeObsolete and iObsoleteTech != -1 and gc.getTeam(iPlayer).isHasTech(iObsoleteTech): continue
        if plot.getPlotCity().isHasRealBuilding(iWonder): iCount += 1

    return iCount


def countPlayersWithAttitude(iPlayer, eAttitude):
    iCount = 0
    for iOtherPlayer in range(iNumPlayers) :
        if gc.getPlayer(iPlayer).canContact(iOtherPlayer) and gc.getPlayer(iOtherPlayer).AI_getAttitude(iPlayer) >= eAttitude:
            iCount += 1
    return iCount

# def conntCityRegions(iPlayer):
#   
#    getRegionID()
