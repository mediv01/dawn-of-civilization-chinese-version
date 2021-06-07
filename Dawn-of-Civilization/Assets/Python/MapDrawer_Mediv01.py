from CvPythonExtensions import *
from Consts import *
import Areas
from SettlerMaps import *
from RFCUtils import utils
import csv

#IMAGE_LOCATION = "E:\\DoC Maps"
IMAGE_LOCATION_NEW = "D:\\Civilization4\\Beyond the Sword\\Mods\\RFC Dawn of Civilization 1.16.2\\NewMap\\"

DISPLAY_FOREIGN_CORE = False
DISPLAY_CONTESTED = True

#(LAND, WATER, PEAK, CORE, HISTORICAL, CONTESTED, FOREIGN, FOREIGN_CORE, FLIPZONE) = range(9)


gc = CyGlobalContext()

def main():
    iPlayer= iChina
    createMap_History(iPlayer)
    createMap_SettlerMap(iPlayer)


def createMap_SettlerMap(iPlayer, iReborn=0):
    WATER = -1
    LAND = -2
    PEAK = -3

    iCivilization = gc.getPlayer(iPlayer).getCivilizationType()
    if iReborn == 1: iCivilization = dRebirthCiv[iPlayer]
    sName = gc.getCivilizationInfo(iCivilization).getShortDescription(0)

    file = open(IMAGE_LOCATION_NEW + "" + sName + "_settlermap.csv", 'wt')

    lCorePlots = Areas.getCoreArea(iPlayer, iReborn == 1)
    lForeignCorePlots = getForeignCorePlots(iPlayer, iReborn)
    try:
        writer = csv.writer(file)
        for y in reversed(range(iWorldY)):
            lRow = []
            for x in range(iWorldX):
                plot = gc.getMap().plot(x, y)
                iSettlerValue = getMapValue(iCivilization, x, y)


                if plot.isWater():
                    lRow.append(WATER)
                elif plot.isPeak():
                    lRow.append(PEAK)
                elif iSettlerValue>0:
                    lRow.append(iSettlerValue)
                else:
                    lRow.append(LAND)
            writer.writerow(lRow)
    finally:
        file.close()


def createMap_History(iPlayer, iReborn=0):
    WATER = 0
    LAND = 1
    PEAK = 2
    FOREIGN = 3
    FOREIGN_CORE = 4
    HISTORICAL = 90
    CONTESTED = 300
    CORE = 500
    iCivilization = gc.getPlayer(iPlayer).getCivilizationType()
    if iReborn == 1: iCivilization = dRebirthCiv[iPlayer]
    sName = gc.getCivilizationInfo(iCivilization).getShortDescription(0)

    file = open(IMAGE_LOCATION_NEW + "" + sName + "_his.csv", 'wt')

    lCorePlots = Areas.getCoreArea(iPlayer, iReborn == 1)
    lForeignCorePlots = getForeignCorePlots(iPlayer, iReborn)
    try:
        writer = csv.writer(file)
        for y in reversed(range(iWorldY)):
            lRow = []
            for x in range(iWorldX):
                plot = gc.getMap().plot(x, y)
                iSettlerValue = getMapValue(iCivilization, x, y)
                bForeignCore = ((x, y) in lForeignCorePlots)

                if plot.isWater():
                    lRow.append(WATER)
                elif plot.isPeak():
                    lRow.append(PEAK)
                elif (x, y) in lCorePlots:
                    lRow.append(CORE)
                elif iSettlerValue >= 90 and (not bForeignCore or not DISPLAY_CONTESTED):
                    lRow.append(HISTORICAL)
                elif iSettlerValue >= 90 and bForeignCore:
                    lRow.append(CONTESTED)
                elif iSettlerValue < 90 and (not bForeignCore or not DISPLAY_FOREIGN_CORE):
                    lRow.append(FOREIGN)
                elif iSettlerValue < 90 and bForeignCore:
                    lRow.append(FOREIGN_CORE)
                else:
                    lRow.append(LAND)
            writer.writerow(lRow)
    finally:
        file.close()




def createMaps():
    for iPlayer in range(iNumPlayers):
        createMap_notuse(iPlayer, 0)
        if iPlayer in dRebirth:
            createMap_notuse(iPlayer, 1)
            pass


def createMap_notuse(iPlayer, iReborn):
    iCivilization = gc.getPlayer(iPlayer).getCivilizationType()
    if iReborn == 1: iCivilization = dRebirthCiv[iPlayer]
    sName = gc.getCivilizationInfo(iCivilization).getShortDescription(0)

    file = open(IMAGE_LOCATION + "\Stability\\" + sName, 'wt')

    lCorePlots = Areas.getCoreArea(iPlayer, iReborn == 1)
    lForeignCorePlots = getForeignCorePlots(iPlayer, iReborn)

    try:
        writer = csv.writer(file)
        for y in reversed(range(iWorldY)):
            lRow = []
            for x in range(iWorldX):
                plot = gc.getMap().plot(x, y)
                iSettlerValue = getMapValue(iCivilization, x, y)
                bForeignCore = ((x, y) in lForeignCorePlots)

                if plot.isWater():
                    lRow.append(WATER)
                elif plot.isPeak():
                    lRow.append(PEAK)
                elif (x, y) in lCorePlots:
                    lRow.append(CORE)
                elif iSettlerValue >= 90 and (not bForeignCore or not DISPLAY_CONTESTED):
                    lRow.append(HISTORICAL)
                elif iSettlerValue >= 90 and bForeignCore:
                    lRow.append(CONTESTED)
                elif iSettlerValue < 90 and (not bForeignCore or not DISPLAY_FOREIGN_CORE):
                    lRow.append(FOREIGN)
                elif iSettlerValue < 90 and bForeignCore:
                    lRow.append(FOREIGN_CORE)
                else:
                    lRow.append(LAND)
            writer.writerow(lRow)
    finally:
        file.close()

    file = open(IMAGE_LOCATION + "\Spawns\\" + sName, 'wt')

    lFlipzonePlots = []
    if iReborn == 0:
        lFlipzonePlots = Areas.getBirthArea(iPlayer)
    else:
        lFlipzonePlots = Areas.getRebirthArea(iPlayer)

    try:
        writer = csv.writer(file)
        writer.writerow((gc.getPlayer(iPlayer).getPlayerTextColorR(), gc.getPlayer(iPlayer).getPlayerTextColorG(), gc.getPlayer(iPlayer).getPlayerTextColorB()))

        for y in reversed(range(iWorldY)):
            lRow = []
            for x in range(iWorldX):
                plot = gc.getMap().plot(x, y)
                if plot.isWater():
                    lRow.append(0)
                elif (x, y) in lFlipzonePlots:
                    lRow.append(1)
                else:
                    lRow.append(0)
            writer.writerow(lRow)
    finally:
        file.close()

    file = open(IMAGE_LOCATION + "\ExtendedCores\\" + sName, 'wt')

    lExtendedCorePlots = []

    if iReborn == 0 and iPlayer in dRebirth:
        lExtendedCorePlots = Areas.getCoreArea(iPlayer, True)

    try:
        writer = csv.writer(file)

        for y in reversed(range(iWorldY)):
            lRow = []
            for x in range(iWorldX):
                plot = gc.getMap().plot(x, y)
                if (x, y) in lExtendedCorePlots and (x, y) not in lCorePlots and not plot.isWater():
                    lRow.append(1)
                else:
                    lRow.append(0)
            writer.writerow(lRow)
    finally:
        file.close()


def getForeignCorePlots(iPlayer, iReborn):
    lForeignCorePlots = []
    iSpawnDate = tBirth[iPlayer]
    if iReborn == 1: iSpawnDate = dRebirth[iPlayer]

    for iLoopPlayer in range(iNumPlayers):
        if iLoopPlayer != iPlayer:
            if utils.canEverRespawn(iLoopPlayer, getTurnForYear(iSpawnDate)) or tBirth[iLoopPlayer] > iSpawnDate:
                for tPlot in Areas.getCoreArea(iLoopPlayer, iLoopPlayer in dRebirth and iSpawnDate >= dRebirth[iLoopPlayer]):
                    if not tPlot in lForeignCorePlots:
                        lForeignCorePlots.append(tPlot)

    return lForeignCorePlots