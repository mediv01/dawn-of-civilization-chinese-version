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
import CvUtil

gc = CyGlobalContext()
MainOpt = BugCore.game.MainInterface

interface = CyInterface()
translator = CyTranslator()
engine = CyEngine()
game = gc.getGame()
map = gc.getMap()

def text(key, *format):
	return translator.getText(str(key), tuple(format))

def CheckTurn(iGameTurn):
    if (gc.getDefineINT("PYTHON_ENABLE_OBSERVER_MODE")>0):
        if (data.ObserverTurn>0):
            data.ObserverTurn -=1
            pass
        else:
            endObserverMode()
        pass
def rnfEventApply4568(playerID, netUserData, popupReturn):
    if (gc.getDefineINT("PYTHON_ENABLE_OBSERVER_MODE") > 0):
        iDestinationYear = int(popupReturn.getEditBoxString(0))
        iAutoplayTurns = utils.getTurnForYear(iDestinationYear) - utils.getGameTurn()
        StartObServerMode(iAutoplayTurns)

def KeyDownEvent():
    if (gc.getDefineINT("PYTHON_ENABLE_OBSERVER_MODE") > 0):
        popup = CyPopup(4568, EventContextTypes.EVENTCONTEXT_ALL, True)
        popup.setHeaderString(text("TXT_KEY_INTERFACE_OBSERVER_MODE_HEADER"), CvUtil.FONT_LEFT_JUSTIFY)
        popup.setBodyString(text("TXT_KEY_INTERFACE_OBSERVER_MODE_BODY"), CvUtil.FONT_LEFT_JUSTIFY)
        popup.createEditBox(str(game.getGameTurnYear()), 0)
        popup.launch(True, PopupStates.POPUPSTATE_IMMEDIATE)

    pass
def StartObServerMode(iTurns):
    data.ObserverTurn = iTurns
    data.iBeforeObserverSlot = utils.getHumanID()
    if gc.getPlayer(iHarappa).isAlive():
        iObserverSlot = iCanada
    else:
        iObserverSlot = iHarappa
        gc.getTeam(gc.getPlayer(iHarappa).getTeam()).setHasTech(iCalendar, True, iHarappa, False, False)
    utils.makeUnit(iCatapult,iObserverSlot, (0, 0),1)
    gc.getGame().setActivePlayer(iObserverSlot, False)
    gc.getGame().setAIAutoPlay(iTurns)

def endObserverMode():
    if data.iBeforeObserverSlot != -1:
        if gc.getPlayer(data.iBeforeObserverSlot).isAlive():
            gc.getGame().setActivePlayer(data.iBeforeObserverSlot, False)
            data.iBeforeObserverSlot = -1
        else:
            utils.makeUnit(iCatapult, data.iBeforeObserverSlot, (0, 0), 1)
            gc.getGame().setActivePlayer(data.iBeforeObserverSlot, False)
            data.iBeforeObserverSlot = -1

