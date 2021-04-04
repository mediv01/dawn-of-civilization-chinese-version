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
import GameScore
import Stability as sta


gc = CyGlobalContext()
localText = CyTranslator()

def checkTurn(iGameTurn):
    if iGameTurn % 2 == 0:
        Check_Resurrection_Civ(iGameTurn)
    pass

def Check_Resurrection_Civ(iGameTurn):



    #大唐时期的复兴
    Check_Resurrection_Civ_with_Year(iGameTurn, iChina, 600, 900)

    # 蒙古后中华文明的复兴
    Check_Resurrection_Civ_with_Year(iGameTurn, iChina, 1400, 1800)

    # 中华人民共和国
    Check_Resurrection_Civ_with_Year(iGameTurn, iChina, 1949, 2020)

    # 百年战争后的复兴
    Check_Resurrection_Civ_with_Year(iGameTurn, iFrance, 1500, 1800)

    # 一战法国
    Check_Resurrection_Civ_with_Year(iGameTurn, iFrance, 1918, 1939)

    # 一战德国
    Check_Resurrection_Civ_with_Year(iGameTurn, iGermany, 1918, 1939)

    # 苏联
    Check_Resurrection_Civ_with_Year(iGameTurn, iRussia, 1918, 1990)

    # 二战法国
    Check_Resurrection_Civ_with_Year(iGameTurn, iFrance, 1960, 2020)

    # 二战德国
    Check_Resurrection_Civ_with_Year(iGameTurn, iGermany, 1990, 2020)



    pass

def Check_Resurrection_Civ_with_Year(iGameTurn,iCiv,year_start,year_end):
    if (gc.getPlayer(iCiv).isAlive()): return
    if(iGameTurn>=getTurnForYear(year_start) and (iGameTurn<=getTurnForYear(year_end))):
        if (not gc.getPlayer(iCiv).isAlive()):
            doResurrection_Civ(iCiv)

def doResurrection_Civ(iCiv):

    lCityList = sta.getResurrectionCities(iCiv)
    sta.doResurrection(iCiv, lCityList)