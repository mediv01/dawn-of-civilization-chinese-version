from CvPythonExtensions import *
from StoredData import data
from Consts import *
from RFCUtils import utils
import heapq
import Areas
import CityNameManager as cnm
import DynamicCivs as dc
import BugCore
import Consts as con

AdvisorOpt = BugCore.game.Advisors
AlertsOpt = BugCore.game.MoreCiv4lerts

### GLOBALS ###

gc = CyGlobalContext()
localText = CyTranslator()


def playerCommerceOutput(iPlayer):
    return gc.getPlayer(iPlayer).calculateTotalYield(YieldTypes.YIELD_COMMERCE)


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


def isTopCulture(self, iPlayer):
    """Checks whether iPlayer has accumulated the higest number of Culture."""
    bTopCulture = True
    iCulture = gc.getPlayer(iPlayer).countTotalCulture()
    for iPlayerLoop in range(con.iNumPlayers):
        if gc.getPlayer(iPlayerLoop).isAlive() and iPlayerLoop != iPlayer:
            if gc.getPlayer(iPlayerLoop).countTotalCulture() > iCulture:
                bTopCulture = False
                break
    return bTopCulture


def isHighestPopulation(self, iPlayer):
    """Checks whether iPlayer has the highest total population."""
    iPop = gc.getPlayer(iPlayer).getRealPopulation()
    bHighest = True
    for iLoopCiv in range(con.iNumPlayers):
        if iPop < gc.getPlayer(iLoopCiv).getRealPopulation():
            bHighest = False
            break
    return bHighest


def isMostProductive(self, iPlayer):
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


def isHasLegendaryCity(self, iPlayer):
    """Checks whether iPlayer has a city with Legendary culture."""
    # apCityList = PyPlayer(iPlayer).getCityList
    apCityList = utils.getCityList(iPlayer)
    for pCity in apCityList:
        if pCity.GetCy().getCultureTimes100(iPlayer) >= utils.getTurns(2500000):
            return True
    return False


def getNumVassals(self, iPlayer):
    """Returns the number of vassals belonging to iPlayer."""
    iCounter = 0
    for iCiv in range(con.iNumPlayers):
        if iCiv != iPlayer:
            if gc.getPlayer(iCiv).isAlive():
                if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iPlayer):
                    iCounter += 1
    return iCounter
