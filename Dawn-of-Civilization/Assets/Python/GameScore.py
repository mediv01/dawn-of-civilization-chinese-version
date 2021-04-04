from StoredData import data # edead
from CvPythonExtensions import *
from StoredData import data
from Consts import *
from RFCUtils import utils
import heapq
import Areas
import CityNameManager as cnm
import DynamicCivs as dc
import BugCore
import BugPath
import time
gc = CyGlobalContext()
localText = CyTranslator()


def log_path():
    # filepath='D:\\DoC_Log\\'
    filepath = BugPath.join(BugPath.getRootDir(), 'Saves', 'logs', '')
    return filepath


def log_gettime(iGameTurn):
    curtime1 = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # curtime1 = str(time.strftime('%Y-%m-%d %H:%M:%S', time.time()))
    strturn = u' [' + str(gc.getGame().getGameTurnYear()) + ']  T[' + str(iGameTurn) + ']  '
    log_gettime = curtime1 + strturn
    return log_gettime


def manual_debug():
    if (gc.getDefineINT("PYTHON_LOG_MANUAL_DEBUG_SCORE") == 1):
        log_reset()
        for i in range(gc.getGame().getGameTurn()):
            ignoredeath=True
            log_tech_score(i,ignoredeath)
            log_power_score(i,ignoredeath)


def checkTurn(iGameTurn):
    ignoredeath=False
    if (gc.getDefineINT("PYTHON_LOG_ON_TECHSCORE") == 1):  # output the debug info
        log_tech_score(iGameTurn,ignoredeath)
    if (gc.getDefineINT("PYTHON_LOG_ON_POWERSCORE") == 1):  # output the debug info
        log_power_score(iGameTurn,ignoredeath)
    pass

def log_reset():
    if (gc.getDefineINT("PYTHON_USE_LOG") == 1):  # output the debug info
        f = open(log_path() + "DoC_SmallMap_Log_TechScore.log", 'w')
        f.write('')
        f.close
        f = open(log_path() + "DoC_SmallMap_Log_PowerScore.log", 'w')
        f.write('')
        f.close


def log_tech_score(iGameTurn,ignoredeath):

    if (gc.getDefineINT("PYTHON_USE_LOG") == 1):  # output the debug info
        aHelp = tech_score(iGameTurn,ignoredeath)
        f = open(log_path() + "DoC_SmallMap_Log_TechScore.log", 'a')
        f.write((log_gettime(iGameTurn)  + u'**************'+str(iGameTurn)+ u'*****************').encode('utf8', 'xmlcharrefreplace'))
        f.write('\n')
        for strText in aHelp:

            f.write((log_gettime(iGameTurn) + str(strText) + u'').encode('utf8', 'xmlcharrefreplace'))
            f.write('\n')
        f.close
    pass


def log_power_score(iGameTurn,ignoredeath):

    if (gc.getDefineINT("PYTHON_USE_LOG") == 1):  # output the debug info
        aHelp = power_score(iGameTurn,ignoredeath)
        f = open(log_path() + "DoC_SmallMap_Log_PowerScore.log", 'a')
        f.write((log_gettime(iGameTurn)  + u'**************'+str(iGameTurn)+ u'*****************').encode('utf8', 'xmlcharrefreplace'))
        f.write('\n')
        for strText in aHelp:

            f.write((log_gettime(iGameTurn) + str(strText) + u'').encode('utf8', 'xmlcharrefreplace'))
            f.write('\n')
        f.close
    pass

def tech_score(iGameTurn,ignoredeath):
    aHelp=[]
    techlist = []
    for iCiv in range(iNumPlayers):
        if (gc.getPlayer(iCiv).isAlive() or ignoredeath):
            iTechValue = gc.getPlayer(iCiv).getTechHistory(iGameTurn)
            techlist.append([iCiv, iTechValue])
        pass

    techlist.sort(key=lambda x: -x[1])
    for i in range(len(techlist)):
        iCiv = techlist[i][0]
        iTechValue = techlist[i][1]
        aHelp.append(' RANK (' + str(i + 1) + ') : ' + gc.getPlayer(iCiv).getCivilizationShortDescription(0) + '             with ' + str(iTechValue))
    return aHelp
    pass

def power_score(iGameTurn,ignoredeath):
    aHelp=[]
    techlist = []
    for iCiv in range(iNumPlayers):
        if (gc.getPlayer(iCiv).isAlive() or ignoredeath):
            iTechValue = gc.getPlayer(iCiv).getPowerHistory(iGameTurn)
            techlist.append([iCiv, iTechValue])
        pass

    techlist.sort(key=lambda x: -x[1])
    for i in range(len(techlist)):
        iCiv = techlist[i][0]
        iTechValue = techlist[i][1]
        aHelp.append(' RANK (' + str(i + 1) + ') : ' + gc.getPlayer(iCiv).getCivilizationShortDescription(0) + '             with ' + str(iTechValue))
    return aHelp
    pass