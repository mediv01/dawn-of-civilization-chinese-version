# Rhye's and Fall of Civilization - Dynamic land

from CvPythonExtensions import *
import CvUtil
import PyHelpers
# import Popup
from Consts import *
from RFCUtils import utils  # edead
from StoredData import data
import Resources
# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
localText = CyTranslator()

### Constants ###


# initialise bonuses variables
def foundCity(iPlayer, tPlot, sName, iPopulation, iUnitType=-1, iNumUnits=-1, lReligions=[]):
    pPlayer = gc.getPlayer(iPlayer)
    x, y = tPlot
    plot = gc.getMap().plot(x, y)
    plot.setOwner(iPlayer)
    pPlayer.found(x, y)

    if plot.isCity():
        city = gc.getMap().plot(x, y).getPlotCity()

        city.setName(sName, False)
        city.setPopulation(iPopulation)

        plot.changeCulture(iPlayer, 10 * (gc.getGame().getCurrentEra() + 1), True)
        city.changeCulture(iPlayer, 10 * (gc.getGame().getCurrentEra() + 1), True)

        if iNumUnits > 0 and iUnitType > 0:
            #				utils.makeUnit(iUnitType, iPlayer, tPlot, iNumUnits+ round(gc.getGame().getHandicapType()/2))
            utils.makeUnit(iUnitType, iPlayer, tPlot, iNumUnits)
        for iReligion in lReligions:
            if gc.getGame().isReligionFounded(iReligion):
                city.setHasReligion(iReligion, True, False, False)

        return True

    return False


def declareWar(iPlayer, iTarget, iWarPlan=WarPlanTypes.WARPLAN_TOTAL):
    if gc.getTeam(iPlayer).isVassal(iTarget):
        gc.getTeam(iPlayer).setVassal(iTarget, False, False)

    gc.getTeam(iPlayer).declareWar(iTarget, True, iWarPlan)

def checkturn(iGameTurn):
    # 阿根廷出生前1回合，设置马岛，并将马岛设置为阿根廷的UHV
    if iGameTurn == getTurnForYear(1805): #1805
        tPlot=(41,6)
        iPlayer=iEngland
        iBestInfantry = utils.getBestInfantry(iPlayer)
        gc.getMap().plot(tPlot[0], tPlot[1]).setPlotType(PlotTypes.PLOT_HILLS, True, True)
        Resources.Resources().createResource(41, 7, iFish)
        foundCity(iEngland,tPlot,"Falkland",3)
        #utils.makeUnitAI(iSettler, iEngland, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
        utils.makeUnitAI(iBestInfantry, iEngland, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1+gc.getGame().getHandicapType())
        pass
        #self.createResource(88, 37, iHorse)
    if iGameTurn == getTurnForYear(1870): #1805
        if(utils.getHumanID()==iArgentina):
            if(gc.getPlayer(iBrazil).isAlive() and gc.getPlayer(iArgentina).isAlive()):
                pass
                #declareWar(iBrazil,iArgentina)