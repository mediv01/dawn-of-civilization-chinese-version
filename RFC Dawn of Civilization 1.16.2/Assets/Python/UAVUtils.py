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
