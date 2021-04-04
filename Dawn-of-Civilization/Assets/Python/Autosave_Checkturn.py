import AutoSave

import os.path
import time
import CvUtil
import BugCore
import BugPath
import BugUtil
import MapFinder
import PlayerUtil
from CvPythonExtensions import *
from Consts import *
from RFCUtils import utils
## Constants

# Save Types

SINGLE = "single"
MULTI = "multi"
PBEM = "pbem"
HOTSEAT = "hotseat"
PITBOSS = "pitboss"
WORLDBUILDER = "WorldBuilder"

# Save Variants

AUTO = "auto"
QUICK = "quick"


## Globals

gc = CyGlobalContext()
options = BugCore.game.AutoSave


def checkTurn(iGameTurn):
    #AutoSave.saveGame(type="auto", variant=None)
    if (gc.getDefineINT("PYTHON_AUTO_SAVE_EVERY_TURN") == 1):
        saveGame(type="auto", variant=None)

    pass


def saveGame(type="auto", variant=None):
    """
    Saves the current game to the folder designated by the type and optional variant
    and returns the full path to it.

    All in the types except WORLDBUILDER allow the AUTO variant while only SINGLE allows QUICK.
    """
    if(gc.getDefineINT("PYTHON_AUTO_SAVE_WHEN_AUTO_PLAY") == 1):
        pass
    else:
        human_id=utils.getHumanID()
        if gc.getGame().getGameTurnYear()<tBirth[human_id]-30:
            return
        pass



    if (gc.getDefineINT("PYTHON_AUTO_SAVE_EVERY_TURN_DIR") == 1):
        savedir=''
    else:
        savedir='auto'
    epoch = "BC"
    names='mediv01 - '+gc.getPlayer(human_id).getCivilizationShortDescription(0)+' - '
    curtime1 = str(' ['+time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))+'] ')
    if gc.getGame().getGameTurnYear() > 0: epoch = "AD"
    filePath = BugPath.join(BugPath.getRootDir(), 'Saves', 'single', savedir,
                            '%s Save %s %d (turn %d) %s.CivBeyondSwordSave' % (
                                names,epoch,abs(gc.getGame().getGameTurnYear())
                                , gc.getGame().getGameTurn(),curtime1))
    gc.getGame().saveGame(filePath.encode('utf8', 'xmlcharrefreplace'))

