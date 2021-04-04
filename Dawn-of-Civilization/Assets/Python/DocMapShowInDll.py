import Areas
import Barbs
import Companies
from Consts import *
import AIWars
localText = CyTranslator()
gc = CyGlobalContext()





def isCityInArea(tCityPos, tTL, tBR):

    x, y = tCityPos
    tlx, tly = tTL
    brx, bry = tBR

    return ((x >= tlx) and (x <= brx) and (y >= tly) and (y <= bry))


def SearchCompany(x, y):
    #在地图上显示公司信息
    tSilkRouteTL = (80, 46)
    tSilkRouteBR = (99, 52)

    tMiddleEastTL = (68, 38)
    tMiddleEastBR = (85, 46)

    lMiddleEastExceptions = [(68, 39), (69, 39), (71, 40)]

    tCaribbeanTL = (26, 33)
    tCaribbeanBR = (34, 39)

    tSubSaharanAfricaTL = (49, 10)
    tSubSaharanAfricaBR = (77, 29)

    tSouthAsiaTL = (76, 24)
    tSouthAsiaBR = (117, 39)
    tList = []
    plotCity = (x, y)

    tPlot = (x, y)
    iCompany = iSilkRoute
    if iCompany == iSilkRoute:
        if (isCityInArea(tPlot, tSilkRouteTL, tSilkRouteBR) or isCityInArea(
                tPlot, tMiddleEastTL,
                tMiddleEastBR)) and tPlot not in lMiddleEastExceptions:
            tList.append(0)

    iCompany = iTradingCompany
    if iCompany == iTradingCompany:
        if isCityInArea(tPlot, tCaribbeanTL, tCaribbeanBR):
            tList.append(1)
        if isCityInArea(tPlot, tSubSaharanAfricaTL, tSubSaharanAfricaBR):
            tList.append(2)
        if isCityInArea(tPlot, tSouthAsiaTL, tSouthAsiaBR):
            tList.append(3)
    '''
    for i in range(len(Areas.tBirthArea)):
        tArea = Areas.getBirthArea(i)
        if (x, y) in tArea:
            tList.append(i)
        pass
    '''
    return tList


def SearchCore(x, y):
    #在地图上显示翻转区信息
    tList = []

    for i in range(len(Areas.tBirthArea)):
        tArea = Areas.getBirthArea(i)
        if (x, y) in tArea:
            tList.append(i)
        pass
    return tList


def SearchMinorCityBirth(x, y):
    #显示独立城邦诞生时间
    tMinorCities_actual = Barbs.tMinorCities
    iHandicap1 = gc.getGame().getHandicapType()
    if iHandicap1 == 0:  #根据难度区分的独立城邦
        tMinorCities_actual = Barbs.tMinorCities
    elif iHandicap1 == 1:
        tMinorCities_actual = Barbs.tMinorCities_1
    elif iHandicap1 == 2:
        tMinorCities_actual = Barbs.tMinorCities_2
    elif iHandicap1 == 3:
        tMinorCities_actual = Barbs.tMinorCities_3
    elif iHandicap1 == 4:
        tMinorCities_actual = Barbs.tMinorCities_4
    tMinorCities = tMinorCities_actual
    tList = []

    for i in range(len(tMinorCities)):
        iYear = tMinorCities[i][0]
        tPlot = tMinorCities[i][1]

        if x == tPlot[0] and y == tPlot[1]:
            tList.append(int(iYear))

    return tList

def SearchAIWAR(x, y):
    tList = []
    tPlot = (x, y)
    lConquests = AIWars.lConquests
    #tList.append(len(AIWars.lConquests))
    lConquests.append( (1001, iMongolia, iArabia, (73, 31), (84, 43), 7, 1220, 10))
    lConquests.append( (1002, iMongolia, iPersia, (73, 37), (86, 48), 7, 1220, 10))
    lConquests.append( (1003, iMongolia, iByzantium,  (68, 41), (77, 46), 7, 1220, 10))
    lConquests.append( (1004, iMongolia, iRussia, (68, 48),(81, 62), 7, 1220, 10))
    

    for i in range(len(lConquests)):
        #iID, iPlayer, iPreferredTarget, tTL, tBR, iNumTargets, iYear, iIntervalTurns = tConquest
        tConquest = lConquests[i]
        iID = tConquest[0]
        tTL1 = tConquest[3]
        tBR1 = tConquest[4]
        if isCityInArea(tPlot, tTL1, tBR1) and iID not in tList:
            tList.append(iID)
            
            pass
    return tList
#tList=SearchCore(42,47)

# def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
#     """Searches all tile in the square from tTopLeft to tBottomRight and calls function for every tile, passing argsList."""
#     tPaintedList = []
#     for tPlot in self.getPlotList(tTopLeft, tBottomRight):
#         bPaintPlot = function(tPlot, argsList)
#         if bPaintPlot:
#             tPaintedList.append(tPlot)
#     return tPaintedList