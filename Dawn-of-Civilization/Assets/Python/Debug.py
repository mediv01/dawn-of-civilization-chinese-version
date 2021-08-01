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


def main():

    import MapDrawer
    #MapDrawer.createMaps()
    import MapDrawer_Mediv01
    #MapDrawer_Mediv01.main()
    #debug_tradeval()



    pass

def debug_tradeval():
    eplayer=utils.getHumanID()
    myplayer=iEngland
    techtypeID=9
    iTech = iUrbanPlanning
    techmoney = gc.getAIdealValuetoMoney(eplayer,myplayer,techtypeID,iTech)
    utils.log2(str(techmoney),'testtradetechval')