from Consts import *
from RFCUtils import utils

from GlobalDefineAlt import PYTHON_HUMAN_MODIFIER_ENABLE,PYTHON_HUMAN_MODIFIER
def getHumanModifer(iPlayer,iModifier):
	if (utils.getHumanID() is not iPlayer) or (PYTHON_HUMAN_MODIFIER_ENABLE is not 1):
		return 1
	iHumanModifier = 1
	iHumanModifier *= PYTHON_HUMAN_MODIFIER[iModifier] / 100
	return iHumanModifier

def getModifier(iPlayer, iModifier):
	iCivilization = gc.getPlayer(iPlayer).getCivilizationType()
	iHumanModifier = getHumanModifer(iPlayer,iModifier)

	if iCivilization in lOrder:
		initmodifier = tModifiers[iModifier][lOrder.index(iCivilization)]
		initmodifier *= iHumanModifier
		return initmodifier
	return tDefaults[iModifier] * iHumanModifier
	
def getAdjustedModifier(iPlayer, iModifier):
	if utils.getScenario() > i3000BC and iPlayer < iVikings:
		if iModifier in dLateScenarioModifiers:
			return getModifier(iPlayer, iModifier) * dLateScenarioModifiers[iModifier] / 100
	return getModifier(iPlayer, iModifier)
	
def setModifier(iPlayer, iModifier, iNewValue):
	gc.getPlayer(iPlayer).setModifier(iModifier, iNewValue)
	
def changeModifier(iPlayer, iModifier, iChange):
	setModifier(iPlayer, iModifier, gc.getPlayer(iPlayer).getModifier(iModifier) + iChange)
	
def adjustModifier(iPlayer, iModifier, iPercent):
	setModifier(iPlayer, iModifier, gc.getPlayer(iPlayer).getModifier(iModifier) * iPercent / 100)
	
def adjustModifiers(iPlayer):
	for iModifier in dLateScenarioModifiers:
		adjustModifier(iPlayer, iModifier, dLateScenarioModifiers[iModifier])
		
def adjustInflationModifier(iPlayer):
	adjustModifier(iPlayer, iModifierInflationRate, dLateScenarioModifiers[iModifierInflationRate])
	
def updateModifier(iPlayer, iModifier):
	setModifier(iPlayer, iModifier, getModifier(iPlayer, iModifier))
	
def updateModifiers(iPlayer):
	for iModifier in range(iNumModifiers):
		updateModifier(iPlayer, iModifier)
		
def init():
	for iPlayer in range(iNumTotalPlayersB):
		updateModifiers(iPlayer)
		
		if utils.getScenario() > i3000BC and iPlayer < iVikings:
			adjustModifiers(iPlayer)
		
		gc.getPlayer(iPlayer).updateMaintenance()
		

### Modifier types ###

iNumModifiers = 13
(iModifierCulture, iModifierUnitUpkeep, iModifierResearchCost, iModifierDistanceMaintenance, iModifierCitiesMaintenance,
iModifierCivicUpkeep, iModifierHealth, iModifierUnitCost, iModifierWonderCost, iModifierBuildingCost,
iModifierInflationRate, iModifierGreatPeopleThreshold, iModifierGrowthThreshold) = range(iNumModifiers)

### Sequence of spawns ###

lOrder = [iCivEgypt, iCivBabylonia, iCivHarappa, iCivChina, iCivGreece, iCivIndia, iCivCarthage, iCivPolynesia, iCivPersia, iCivRome, iCivMaya, iCivTamils, iCivEthiopia, iCivKorea, iCivByzantium, iCivJapan, iCivVikings, iCivTurks, iCivArabia, iCivTibet, iCivIndonesia, iCivMoors, iCivSpain, iCivFrance, iCivKhmer, iCivEngland, iCivHolyRome, iCivRussia, iCivMali, iCivPoland, iCivPortugal, iCivInca, iCivItaly, iCivMongols, iCivAztecs, iCivMughals, iCivOttomans, iCivThailand, iCivCongo, iCivIran, iCivNetherlands, iCivGermany, iCivAmerica, iCivArgentina, iCivMexico, iCivColombia, iCivBrazil, iCivCanada, iCivIndependent, iCivIndependent2, iCivNative, iCivCeltia, iCivBarbarian]

### Modifiers (by civilization!) ###

# 				            EGY BAB HAR CHI GRE IND CAR PLY PER ROM          MAY TAM ETH KOR BYZ JAP VIK TUR ARA TIB          INO MOO SPA FRA KHM ENG HRE RUS MAL POL          POR INC ITA MON AZT MUG OTT THA CON IRA          NET GER AME ARG MEX COL BRA CAN     IND IND NAT CEL SEL BAR 

tCulture =		          (  90, 80,100,100,100,100,100,100,130,100         ,100,110,100, 50,100,110,130,150,110,125         ,120,125,125,160,130,130,150,130,130,110         ,147,140,150,135,140,125,200,130,130,135         ,165,150,140,130,140,140,140,140,     20, 20, 20, 50, 50, 30 )

tUnitUpkeep = 		      ( 135,120,100,100,110,100,115,100,100,110         ,110,100,115,100,100,105, 90,100,100,110         ,100,110,110,100, 90,100,100,100,100,100         ,100,100,100, 75, 90,110,100, 90, 90,110         , 90, 75, 80, 80, 90, 90, 80, 75,      0,  0,100,100, 50,100 )
tResearchCost = 	      ( 140,125,100,100,130,125, 80,200,125,120         ,115,120,100,105,100,120, 85,120,100, 80         ,100, 90, 80, 80, 90, 90,100, 85,110, 80         , 85, 80, 70, 90, 85,120,100,100, 85,110         , 80, 70, 75, 70, 90, 90, 90, 70,    110,110,110,350,110,110 )
tDistanceMaintenance = 	  ( 100,110,100,100, 90,100, 60, 50, 90, 70         ,100, 95,100,120, 80, 95, 70, 60, 90,120         , 80, 80, 55, 65, 80, 55, 70, 70, 80, 90         , 80, 60, 70, 75, 70,100, 80, 80, 80,100         , 70, 80, 60, 50, 70, 70, 80, 70,     20, 20, 20, 20, 20, 20 )
tCitiesMaintenance = 	  ( 135,135,100,100,125,100, 80,100, 90, 60         ,115,100,100,130, 80,110, 75, 90, 90,120         ,100, 70, 50, 70,100, 70, 75, 70, 90, 75         , 85, 80, 80, 75, 85,100, 80,100, 90,100         , 80, 75, 70, 50, 85, 85, 80, 60,     30, 30, 30, 30, 30, 30 )
tCivicUpkeep = 		      ( 120,110,100,100,110,100, 70, 80, 70, 75         , 80, 80, 80, 80, 90, 80, 80,110, 90, 80         ,100, 90, 75, 80,100, 70, 70, 80, 80, 70         , 80, 60, 60, 60, 60, 90, 90, 80, 80, 80         , 70, 60, 50, 50, 70, 70, 75, 75,     70, 70, 70, 70, 70, 70 )
tHealth = 		          (   2,  1,  3,  1,  3,  1,  3,  3,  3,  3         ,  3,  2,  3,  3,  3,  2,  3,  2,  2,  3         ,  3,  2,  2,  2,  3,  2,  2,  2,  2,  2         ,  2,  3,  2,  3,  3,  4,  4,  4,  4,  3         ,  3,  3,  3,  3,  3,  3,  3,  3,      0,  0,  0,  0,  0,  0 )

tUnitCost = 		      ( 110,140,100,100,110,150, 80,100, 90,100         ,105, 85, 90, 80,100, 90, 85,100, 90,100         ,105,100, 90, 90, 90,100, 90, 90, 90, 80         , 90,100,110, 80,100,100,100, 90, 70, 90         , 80, 75, 85, 80, 85, 85, 85, 85,    200,200,150,150,100,140 )
tWonderCost = 		      (  80, 80,100,100, 80,100, 80,100, 85,100         , 90,100,100, 80,100,100, 90,120, 90,100         , 80, 85, 90, 70, 90, 90,100,100, 90,100         , 90, 80, 80, 90, 80, 80, 90, 90,100, 85         ,100, 90, 70, 70, 90, 90, 90, 80,    150,150,150,100,100,100 )
tBuildingCost = 	      ( 110,110,100,100,120, 80, 80, 50,110, 90         , 90, 70,100, 80,100,100, 90,100,100, 80         , 90, 90, 90, 85, 80, 90, 85, 90, 80, 80         , 80, 70, 80, 80, 80, 85, 80, 80, 80, 80         , 80, 70, 70, 70, 80, 80, 75, 80,    100,100,150,100,100,100 )
tInflationRate = 	      ( 130,130,100,100,130,120,100,130,130,130         ,125,110,110, 90,100, 80, 70, 90, 85,100         , 90, 85, 90, 75,100, 70, 70, 75,115, 70         , 80, 80, 85, 90, 80,100,100, 75, 75, 85         , 85, 70, 65, 60, 65, 65, 60, 60,     95, 95, 95, 95, 95, 95 )
tGreatPeopleThreshold =   ( 140,140,100,100,110,100, 80,120,110,110         ,100,110, 80, 80,120,110, 90, 70, 80, 75         , 90, 75, 75, 70, 90, 75, 80, 80, 80, 80         , 75, 70, 65, 70, 70, 75, 80, 80, 85, 80         , 50, 65, 65, 70, 80, 80, 80, 75,    100,100,100,100,100,100 )
tGrowthThreshold = 	      ( 150,150, 80,100,130,100,100,120,130,120         ,110,110, 80,112, 80,110, 80, 80, 80, 80         , 80, 80, 80, 80, 70, 70, 80, 80, 75, 80         , 80, 70, 70, 75, 70, 70, 70, 70, 75, 70         , 75, 70, 70, 70, 70, 70, 70, 70,    125,125,125,125,125,125 )

tModifiers = (tCulture, tUnitUpkeep, tResearchCost, tDistanceMaintenance, tCitiesMaintenance, tCivicUpkeep, tHealth, tUnitCost, tWonderCost, tBuildingCost, tInflationRate, tGreatPeopleThreshold, tGrowthThreshold)

tDefaults = (100, 100, 100, 100, 100, 100, 2, 100, 100, 100, 100, 100, 100)

dLateScenarioModifiers = {
iModifierUnitUpkeep : 90,
iModifierDistanceMaintenance : 85,
iModifierCitiesMaintenance : 80,
iModifierCivicUpkeep : 90,
iModifierInflationRate : 85,
iModifierGreatPeopleThreshold : 85,
iModifierGrowthThreshold : 80,
}