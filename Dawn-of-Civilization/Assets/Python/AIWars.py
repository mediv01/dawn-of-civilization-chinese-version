# Rhye's and Fall of Civilization - AI Wars

from CvPythonExtensions import *
import CvUtil
import PyHelpers  # LOQ
import Popup
#import cPickle as pickle
from Consts import *
import Areas
from RFCUtils import utils
import UniquePowers
from StoredData import data  # edead
import Stability as sta

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer  # LOQ
up = UniquePowers.UniquePowers()

### Constants ###

iMinIntervalEarly = 10
iMaxIntervalEarly = 20
iMinIntervalLate = 40
iMaxIntervalLate = 60
iThreshold = 100
iMinValue = 30

iRomeCarthageYear = -220
tRomeCarthageTL = (53, 37)
tRomeCarthageBR = (61, 40)

iRomeGreeceYear = -150
tRomeGreeceTL = (64, 40)
tRomeGreeceBR = (68, 45)

iRomeMesopotamiaYear = -100
tRomeMesopotamiaTL = (70, 38)
tRomeMesopotamiaBR = (78, 45)

iRomeAnatoliaYear = -100
tRomeAnatoliaTL = (70, 38)
tRomeAnatoliaBR = (75, 45)

iRomeCeltiaYear = -50
tRomeCeltiaTL = (52, 45)
tRomeCeltiaBR = (59, 51)

iRomeEgyptYear = 0
tRomeEgyptTL = (65, 31)
tRomeEgyptBR = (72, 36)

# following setup: iPlayer, iPreferredTarget, TL, BR, iNumTargets, iStartYear, iTurnInterval
tConquestRomeCarthage = (0, iRome, iCarthage, tRomeCarthageTL, tRomeCarthageBR, 2, iRomeCarthageYear, 10)
tConquestRomeGreece = (1, iRome, iGreece, tRomeGreeceTL, tRomeGreeceBR, 2, iRomeGreeceYear, 10)
tConquestRomeAnatolia = (2, iRome, iGreece, tRomeAnatoliaTL, tRomeAnatoliaBR, 2, iRomeAnatoliaYear, 10)
tConquestRomeCelts = (3, iRome, iCeltia, tRomeCeltiaTL, tRomeCeltiaBR, 2, iRomeCeltiaYear, 10)
tConquestRomeEgypt = (4, iRome, iEgypt, tRomeEgyptTL, tRomeEgyptBR, 2, iRomeEgyptYear, 10)

iAlexanderYear = -400
tGreeceMesopotamiaTL = (70, 38)
tGreeceMesopotamiaBR = (78, 45)
tGreeceEgyptTL = (65, 31)
tGreeceEgyptBR = (72, 36)
tGreecePersiaTL = (79, 37)
tGreecePersiaBR = (85, 45)

tConquestGreeceMesopotamia = (5, iGreece, iBabylonia, tGreeceMesopotamiaTL, tGreeceMesopotamiaBR, 2, iAlexanderYear, 20)
tConquestGreeceEgypt = (6, iGreece, iEgypt, tGreeceEgyptTL, tGreeceEgyptBR, 2, iAlexanderYear, 20)
tConquestGreecePersia = (7, iGreece, iPersia, tGreecePersiaTL, tGreecePersiaBR, 2, iAlexanderYear, 20)

iCholaSumatraYear = 880
tCholaSumatraTL = (98, 26)
tCholaSumatraBR = (101, 28)

tConquestCholaSumatra = (8, iTamils, iIndonesia, tCholaSumatraTL, tCholaSumatraBR, 1, iCholaSumatraYear, 10)

iSpainMoorsYear = 1200
tSpainMoorsTL = (50, 40)
tSpainMoorsBR = (54, 42)

tConquestSpainMoors = (9, iSpain, iMoors, tSpainMoorsTL, tSpainMoorsBR, 1, iSpainMoorsYear, 10)

iTurksPersiaYear = 1000
tTurksPersiaTL = (78, 37)
tTurksPersiaBR = (85, 43)

iTurksAnatoliaYear = 1100
tTurksAnatoliaTL = (69, 37)
tTurksAnatoliaBR = (78, 45)

tConquestTurksPersia = (10, iTurks, iArabia, tTurksPersiaTL, tTurksPersiaBR, 4, iTurksPersiaYear, 20)
tConquestTurksAnatolia = (11, iTurks, iByzantium, tTurksAnatoliaTL, tTurksAnatoliaBR, 5, iTurksAnatoliaYear, 20)

iMongolsPersiaYear = 1220
tMongolsPersiaTL = (76, 37)
tMongolsPersiaBR = (85, 55)

tConquestMongolsPersia = (12, iMongolia, iTurks, tMongolsPersiaTL, tMongolsPersiaBR, 7, iMongolsPersiaYear, 10)
#lConquests = [tConquestRomeCarthage, tConquestRomeGreece, tConquestRomeAnatolia, tConquestRomeCelts, tConquestRomeEgypt, tConquestGreeceMesopotamia, tConquestGreeceEgypt, tConquestGreecePersia, tConquestCholaSumatra, tConquestSpainMoors, tConquestTurksPersia, tConquestTurksAnatolia, tConquestMongolsPersia]

####修改开始#####

#英法百年战争1--英国
tEnglandFranceTL = (51, 45)
tEnglandFranceBR = (57, 52)
tConquestEnglandFrance = (13, iEngland, iFrance, tEnglandFranceTL, tEnglandFranceBR, 2, 1340, 10)
#tConquestEnglandFrance=(13, iHarappa , iFrance, tEnglandFranceTL, tEnglandFranceBR, 3, 610, 10)

#英法百年战争2----法国
tEnglandFranceTL = (51, 45)
tEnglandFranceBR = (57, 52)
tConquestFranceEngland = (14, iFrance, iEngland, tEnglandFranceTL, tEnglandFranceBR, 4, 1445, 10)

#十字军东征1 Crusades
tCrusadesTL = (72, 37)
tCrusadesBR = (74, 41)
tConquestCrusades01 = (15, iFrance, iArabia, tCrusadesTL, tCrusadesBR, 1, 1095, 10)
tConquestCrusades02 = (16, iEngland, iArabia, tCrusadesTL, tCrusadesBR, 1, 1095, 10)
tConquestCrusades03 = (17, iHolyRome, iArabia, tCrusadesTL, tCrusadesBR, 1, 1095, 10)

#萨拉丁
tConquestCrusadesSalading01 = (18, iArabia, iFrance, tCrusadesTL, tCrusadesBR, 1, 1170, 10)
tConquestCrusadesSalading02 = (19, iArabia, iEngland, tCrusadesTL, tCrusadesBR, 1, 1170, 10)
tConquestCrusadesSalading03 = (20, iArabia, iHolyRome, tCrusadesTL, tCrusadesBR, 1, 1170, 10)

#拿破仑

tConquestNapol01 = (21, iFrance, iGermany, (56, 39), (70, 57), 3, 1790, 10)
tConquestNapol02 = (22, iFrance, iHolyRome, (56, 39), (70, 57), 3, 1790, 10)
tConquestNapol03 = (23, iFrance, iItaly, (56, 39), (70, 57), 3, 1790, 10)
tConquestNapol04 = (24, iFrance, iRussia, (64, 47), (74, 58), 3, 1790, 10)
# #反拿破仑
tConquestAntiNapol01 = (25, iGermany, iFrance, (56, 39), (70, 57), 3, 1815, 10)
tConquestAntiNapol02 = (26, iHolyRome, iFrance, (56, 39), (70, 57), 3, 1815, 10)
tConquestAntiNapol03 = (27, iItaly, iFrance, (56, 39), (70, 57), 3, 1815, 10)
tConquestAntiNapol04 = (28, iRussia, iFrance, (64, 47), (74, 58), 3, 1815, 10)

#一战
tww1_01 = (29, iGermany, iFrance, (51, 39), (70, 57), 3, 1914, 10)
tww1_02 = (30, iGermany, iEngland, (51, 39), (70, 57), 1, 1915, 10)
tww1_03 = (31, iGermany, iRussia, (64, 47), (74, 58), 1, 1916, 10)
tww1_04 = (32, iHolyRome, iRussia, (64, 47), (74, 58), 3, 1914, 10)

tww1_05 = (33, iFrance, iHolyRome, (51, 39), (70, 57), 2, 1917, 10)
tww1_06 = (34, iEngland, iGermany, (51, 39), (70, 57), 1, 1917, 10)
tww1_07 = (35, iAmerica, iGermany, (51, 39), (70, 57), 1, 1917, 10)
tww1_08 = (36, iRussia, iHolyRome, (51, 39), (70, 57), 2, 1917, 10)

#二战
tww2_01 = (37, iGermany, iFrance, (51, 39), (70, 57), 4, 1940, 10)
tww2_02 = (38, iGermany, iEngland, (51, 39), (70, 57), 1, 1940, 10)
tww2_03 = (39, iGermany, iPoland, (51, 39), (70, 57), 4, 1939, 10)
tww2_04 = (40, iGermany, iRussia, (64, 47), (74, 58), 5, 1941, 10)
tww2_05 = (41, iItaly, iFrance, (51, 39), (70, 57), 2, 1940, 10)
tww2_06 = (42, iJapan, iChina, (103, 39), (109, 55), 5, 1937, 10)

tww2_07 = (43, iFrance, iGermany, (51, 39), (70, 57), 2, 1945, 10)
tww2_08 = (44, iEngland, iGermany, (51, 39), (70, 57), 3, 1944, 10)
tww2_09 = (45, iAmerica, iGermany, (51, 39), (70, 57), 5, 1944, 10)
tww2_10 = (46, iRussia, iGermany, (51, 39), (70, 57), 5, 1945, 10)
tww2_10 = (47, iRussia, iJapan, (103, 49), (109, 55), 3, 1945, 10)
tww2_11 = (48, iChina, iJapan, (103, 39), (109, 55), 5, 1945, 10)
tww2_12 = (49, iAmerica, iItaly, (57, 39), (61, 47), 2, 1943, 10)
tww2_13 = (50, iAmerica, iJapan, (109, 39), (117, 52), 4, 1945, 10)

#迦太基远征罗马
tConquestCarthageRome = (51, iCarthage, iRome, (58, 46), (60, 47), 1, -220, 10)

#斯巴达克斯起义
tConquestSpartacus = (52, iBarbarian, iRome, (60, 40), (63, 43), 1, -78, 10)

lConquests = [tConquestRomeCarthage, tConquestRomeGreece, tConquestRomeAnatolia, tConquestRomeCelts, tConquestRomeEgypt, tConquestGreeceMesopotamia, tConquestGreeceEgypt, tConquestGreecePersia, tConquestCholaSumatra, tConquestSpainMoors, tConquestTurksPersia, tConquestTurksAnatolia, tConquestMongolsPersia, tConquestEnglandFrance, tConquestFranceEngland, tConquestCrusades01, tConquestCrusades02, tConquestCrusades03, tConquestCrusadesSalading01, tConquestCrusadesSalading02, tConquestCrusadesSalading03, tConquestNapol01, tConquestNapol02, tConquestNapol03, tConquestNapol04, tConquestAntiNapol01, tConquestAntiNapol02, tConquestAntiNapol03, tConquestAntiNapol04, tww1_01, tww1_02, tww1_03, tww1_04, tww1_05, tww1_06, tww1_07, tww1_08, tww2_01, tww2_02, tww2_03, tww2_04, tww2_05, tww2_06, tww2_07, tww2_08, tww2_09, tww2_10, tww2_11, tww2_12, tww2_13, tConquestCarthageRome, tConquestSpartacus]


####修改结束#####
class AIWars:
    def setup(self):
        iTurn = getTurnForYear(-600)
        if utils.getScenario() == i600AD:  #late start condition
            iTurn = getTurnForYear(900)
        elif utils.getScenario() == i1700AD:
            iTurn = getTurnForYear(1720)
        data.iNextTurnAIWar = iTurn + gc.getGame().getSorenRandNum(iMaxIntervalEarly - iMinIntervalEarly, 'random turn')

    def checkTurn(self, iGameTurn):
        #checkturn入口
        #a=PlayerTypes.NO_PLAYER
        #a=gc.AI_considerOfferThreshold(4,13)
        #utils.show(str(a))
        #a=gc.CvPlayerAI().AI_considerOffer_Threshold()
        #gc = CyGlobalContext()
        #a=gc.getPlayer(0).AI_considerOffer_Threshold()
        #utils.show(str(gc.getMAX_PLAYERS()))
        #import TradeUtil
        #a=TradeUtil.getTradeableBonuses111(14,3)#3是中国，14是拜占庭，在AD1700剧本中均存活
        #utils.show(str(a))
        #utils.show(str(TradeUtil.canTrade(13,3)))
        #BugUtil.logToScreen('aa')#可以使用
        #DiplomacyUtil.onTributeDemanded(1,12,0)#回调函数，失败了
        #a=CvTeamAI().AI_isWarPossible()   #utils.show(str(gc.getPlayer(3).getDemandTributeAttitudeThreshold()))
        ###import MapDrawer
        ###MapDrawer.createMaps()  #事实证明这个函数没什么用，生成一堆数组
        #入口结束
        #turn automatically peace on between independent cities and all the major civs
        if iGameTurn % 20 == 7:
            utils.restorePeaceHuman(iIndependent2, False)
        elif iGameTurn % 20 == 14:
            utils.restorePeaceHuman(iIndependent, False)
        if iGameTurn % 60 == 55 and iGameTurn > utils.getTurns(50):
            utils.restorePeaceAI(iIndependent, False)
        elif iGameTurn % 60 == 30 and iGameTurn > utils.getTurns(50):
            utils.restorePeaceAI(iIndependent2, False)
        #turn automatically war on between independent cities and some AI major civs
        if iGameTurn % 13 == 6 and iGameTurn > utils.getTurns(50):  #1 turn after restorePeace()
            utils.minorWars(iIndependent)
        elif iGameTurn % 13 == 11 and iGameTurn > utils.getTurns(50):  #1 turn after restorePeace()
            utils.minorWars(iIndependent2)
        if iGameTurn % 50 == 24 and iGameTurn > utils.getTurns(50):
            utils.minorWars(iCeltia)

        for tConquest in lConquests:
            self.checkConquest(tConquest)

        if iGameTurn == data.iNextTurnAIWar:
            self.planWars(iGameTurn)

        for iLoopPlayer in range(iNumPlayers):
            data.players[iLoopPlayer].iAggressionLevel = tAggressionLevel[iLoopPlayer] + gc.getGame().getSorenRandNum(2, "Random aggression")

    def checkConquest(self, tConquest, tPrereqConquest=(), iWarPlan=WarPlanTypes.WARPLAN_TOTAL):
        iID, iPlayer, iPreferredTarget, tTL, tBR, iNumTargets, iYear, iIntervalTurns = tConquest
        
        iGameTurn = gc.getGame().getGameTurn()
        iStartTurn = getTurnForYear(iYear) - 5 + (data.iSeed % 5)
        if (iStartTurn - iGameTurn in range(0,10)):  #mediv01  alert for AIWAR
            if(iID<200):
                utils.log2("AI WAR ["+str(iID)+"] GAME TURN LEFT: "+str(iStartTurn - iGameTurn),'DoC_SmallMap_Log_AIWar')
                pass
        if (iStartTurn - iGameTurn == 2 and gc.getDefineINT("AIWAR_PY_HUMAN_AI_WAR_ALERT") == 1 and utils.getHumanID() == iPreferredTarget):  #mediv01  alert for AIWAR

            tem_text = '&#35686;&#25253;&#65306;&#25932;&#22269;&#27491;&#22312;&#25105;&#22269;&#36793;&#22659;&#38598;&#32467;&#22823;&#20891;&#65281;&#25112;&#20105;&#30340;&#38452;&#20113;&#31548;&#32617;&#22312;&#25105;&#22269;&#19978;&#31354;&#65281;'  #警报：敌国正在我国边境集结大军！战争的阴云笼罩在我国上空！
            utils.show(tem_text)
            CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
            pass
        if (iStartTurn - iGameTurn == 2 and gc.getDefineINT("AIWAR_PY_HUMAN_AI_WAR_ALERT") == 1 and utils.getHumanID() == iPlayer):  #mediv01  alert for AIWAR

            tem_text = '&#35686;&#25253;&#65306;&#25932;&#20891;&#27491;&#22312;&#36793;&#22659;&#25361;&#34885;&#25105;&#26041;&#20891;&#38431;&#65292;&#25112;&#20105;&#30340;&#38452;&#20113;&#31548;&#32617;&#22312;&#25105;&#22269;&#19978;&#31354;&#65281;&#10;'  #警报：敌军正在边境挑衅我方军队，战争的阴云笼罩在我国上空！
            utils.show(tem_text)
            CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
            pass
        if iGameTurn <= getTurnForYear(tBirth[iPlayer]) + 3: return

        if not (iStartTurn <= iGameTurn <= iStartTurn + iIntervalTurns): return
        if tPrereqConquest and not self.isConquered(tPrereqConquest): return
        if (gc.getDefineINT("AIWAR_PY_CAN_USE_SUPER_AI_WAR") == 0 and int(iID) >= 13): return  #参数控制
        if utils.getHumanID() == iPlayer and gc.getDefineINT("AIWAR_PY_HUMAN_CAN_USE_AI_WAR") == 0: return  #人类可以使用AIWAR开关
        if ((not gc.getPlayer(iPlayer).isAlive()) and gc.getDefineINT("AIWAR_PY_DEAD_CIV_CANNOT_USE_AI_WAR") == 1): return  #参数控制
        #if not gc.getPlayer(iPlayer).isAlive() and iPlayer != iTurks: return  #mediv01

        if ((not gc.getPlayer(iPreferredTarget).isAlive()) and gc.getDefineINT("AIWAR_PY_CAN_USE_AI_WAR_TO_DEAD_CIV") == 0): return  #参数控制    #刷兵目标不存在，返回
        if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isDefensivePact(iPreferredTarget): return
        if gc.getDefineINT("PYTHON_NOAIWAR_WHEN_VASSAL"):
            if (gc.getTeam(gc.getPlayer(iPreferredTarget).getTeam()).isVassal(iPlayer)):
                return
            if (gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isVassal(iPreferredTarget)):
                return



        if gc.getDefineINT("PYTHON_NOAIWAR_WHEN_VASSAL_MASTER") or gc.getDefineINT("PYTHON_NOAIWAR_WHEN_VASSAL_TO_OTHER"):
            for iLoopPlayer in range(iNumPlayers):
                #AIWAR目标附庸他人时，无法发动战争
                if gc.getTeam(gc.getPlayer(iPreferredTarget).getTeam()).isVassal(iLoopPlayer):
                    if (gc.getDefineINT("PYTHON_NOAIWAR_WHEN_VASSAL_TO_OTHER")):
                        return

                #附庸其他人时，无法发动AIWAR
                if gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isVassal(iLoopPlayer):
                    if (iLoopPlayer is not iPlayer and gc.getDefineINT("PYTHON_NOAIWAR_WHEN_VASSAL_MASTER")):
                        return
            pass


        if(iID<len(data.lConquest)):
            if data.lConquest[iID]: return
        else:
            return
        if iPreferredTarget >= 0 and gc.getPlayer(iPreferredTarget).isAlive() and gc.getTeam(iPreferredTarget).isVassal(iPlayer): return

        import GlobalDefineAlt
        if (iID in GlobalDefineAlt.PYTHON_NO_AIWAR_ID): return





        if (iPlayer == iEngland and iYear <= 1250) or (iPlayer == iHolyRome and iYear <= 1250) or (iPlayer == iFrance and iYear <= 1250):  #耶路撒冷在天主教文明手里，则停止刷兵

            lAreaCities = utils.getAreaCities(utils.getPlotList(tCrusadesTL, tCrusadesBR))
            for city in lAreaCities:
                if city.getOwner() in [iByzantium, iEngland, iGermany, iFrance, iVikings, iHolyRome, iPoland, iSpain]: return
        data.lConquest[iID] = True
        if (gc.getDefineINT("PYTHON_LOG_ON_MAIN_AIWAR") == 1):
            utils.logwithid(iPlayer,' Start AI WAR with '+str(gc.getPlayer(iPreferredTarget).getCivilizationShortDescription(0)))
        self.spawnConquerors(iPlayer, iPreferredTarget, tTL, tBR, iNumTargets, iYear, iIntervalTurns, iWarPlan)

    def isConquered(self, tConquest):
        iID, iPlayer, iPreferredTarget, tTL, tBR, iNumTargets, iYear, iIntervalTurns = tConquest

        iNumMinorCities = 0
        lAreaCities = utils.getAreaCities(utils.getPlotList(tTL, tBR))
        for city in lAreaCities:
            if city.getOwner() in [iIndependent, iIndependent2, iBarbarian, iNative]: iNumMinorCities += 1
            elif city.getOwner() != iPlayer: return False

        if 2 * iNumMinorCities > len(lAreaCities): return False

        return True

    def declareWar(self, iPlayer, iTarget, iWarPlan):
        if gc.getTeam(iPlayer).isVassal(iTarget):
            gc.getTeam(iPlayer).setVassal(iTarget, False, False)

        gc.getTeam(iPlayer).declareWar(iTarget, True, iWarPlan)

    def spawnConquerors(self, iPlayer, iPreferredTarget, tTL, tBR, iNumTargets, iYear, iIntervalTurns, iWarPlan=WarPlanTypes.WARPLAN_TOTAL):
        if not gc.getPlayer(iPlayer).isAlive():
            for iTech in sta.getResurrectionTechs(iPlayer):
                gc.getTeam(gc.getPlayer(iPlayer).getTeam()).setHasTech(iTech, True, iPlayer, False, False)

        lCities = []
        for city in utils.getAreaCities(utils.getPlotList(tTL, tBR)):
            if city.getOwner() != iPlayer and not gc.getTeam(city.getOwner()).isVassal(iPlayer):
                if (gc.getDefineINT("AIWAR_PY_CANNOT_DO_AIWAR_TO_HUMAN") > 0 and (city.getOwner() == utils.getHumanID())):
                    pass
                else:
                    lCities.append(city)

        capital = gc.getPlayer(iPlayer).getCapitalCity()

        lTargetCities = []
        for i in range(iNumTargets):
            if len(lCities) == 0: break

            targetCity = utils.getHighestEntry(lCities, lambda x: -utils.calculateDistance(x.getX(), x.getY(), capital.getX(), capital.getY()) + int(x.getOwner() == iPreferredTarget) * 1000)
            lTargetCities.append(targetCity)
            lCities.remove(targetCity)

        lOwners = []
        for city in lTargetCities:
            if city.getOwner() not in lOwners:
                lOwners.append(city.getOwner())

        if iPreferredTarget >= 0 and iPreferredTarget not in lOwners and gc.getPlayer(iPreferredTarget).isAlive():
            if (gc.getDefineINT("AIWAR_PY_CANNOT_DO_AIWAR_TO_HUMAN") > 0 and (iPreferredTarget == utils.getHumanID())):
                pass
            else:
                self.declareWar(iPlayer, iPreferredTarget, iWarPlan)

        for iOwner in lOwners:
            self.declareWar(iPlayer, iOwner, iWarPlan)
            CyInterface().addMessage(iOwner, False, iDuration, CyTranslator().getText("TXT_KEY_UP_CONQUESTS_TARGET", (gc.getPlayer(iPlayer).getCivilizationShortDescription(0), )), "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
#####修改开始#####
#消息传送区
        if (gc.getDefineINT("PYTHON_USE_ADVANCE_ALERT") == 1):  #参数控制
            if iPlayer == iGreece:
                tem_text = '&#19990;&#30028;&#20891;&#20107;&#36895;&#36882;&#65306;&#20122;&#21382;&#23665;&#22823;&#19996;&#24449;&#24320;&#22987;&#20102;&#65281;&#20854;&#40638;&#19979;&#30340;&#20891;&#38431;&#27491;&#22312;&#27178;&#25195;&#27431;&#20122;&#22823;&#38470;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#20122;&#21382;&#23665;&#22823;&#19996;&#24449;&#24320;&#22987;&#20102;&#65281;')
            if iPlayer == iRome:
                tem_text = '&#19990;&#30028;&#20891;&#20107;&#36895;&#36882;&#65306;&#32599;&#39532;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#32599;&#39532;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
            if iPlayer == iMongolia:
                tem_text = '&#19990;&#30028;&#20891;&#20107;&#36895;&#36882;&#65306;&#33945;&#21476;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#25104;&#21513;&#24605;&#27735;&#30340;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#33945;&#21476;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#25104;&#21513;&#24605;&#27735;&#30340;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
            if iPlayer == iTurks:
                tem_text = '&#19990;&#30028;&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
    #百年战争
            if iPlayer == iEngland and iYear <= 1450 and iYear >= 1250:
                tem_text = '&#33521;&#27861;&#30334;&#24180;&#25112;&#20105;&#30340;&#33125;&#39118;&#34880;&#38632;&#27491;&#24335;&#25289;&#24320;&#24119;&#24149;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
    #圣女贞德
            if iPlayer == iFrance and iYear <= 1550 and iYear >= 1350:
                tem_text = '&#22307;&#22899;&#36126;&#24503;&#21796;&#36215;&#20102;&#27861;&#22269;&#20154;&#27665;&#30340;&#27665;&#26063;&#24863;&#65292;&#27861;&#22269;&#20154;&#27665;&#20026;&#20102;&#25421;&#21355;&#23478;&#22253;&#32780;&#25112;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
    #十字军
            if iPlayer == iEngland and iYear <= 1200 and iYear >= 1000:
                tem_text = '&#36720;&#21160;&#20013;&#19996;&#21644;&#27431;&#27954;&#30340;&#21313;&#23383;&#20891;&#19996;&#24449;&#24320;&#22987;&#20102;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
    #萨拉丁
            if iPlayer == iEgypt and iYear <= 1300 and iYear >= 1100:
                tem_text = '&#24180;&#36731;&#30340;&#39046;&#34966;&#33832;&#25289;&#19969;&#29575;&#39046;&#20891;&#38431;&#21521;&#21313;&#23383;&#20891;&#21457;&#36215;&#29467;&#28872;&#30340;&#36827;&#25915;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
    #拿破仑战争
            if iPlayer == iFrance and iYear <= 1900 and iYear >= 1700:
                tem_text = '&#25343;&#30772;&#20177;&#30340;&#20891;&#38431;&#27491;&#22312;&#27431;&#27954;&#25152;&#21521;&#25259;&#38753;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
            if iYear <= 1930 and iYear >= 1900:
                tem_text = '&#31532;&#19968;&#27425;&#19990;&#30028;&#22823;&#25112;&#27491;&#22312;&#36827;&#34892;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')
            if iYear <= 1960 and iYear >= 1930:
                tem_text = '&#31532;&#20108;&#27425;&#19990;&#30028;&#22823;&#25112;&#27491;&#22312;&#36827;&#34892;&#65281;'
                CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)

    #			utils.show('&#20891;&#20107;&#36895;&#36882;&#65306;&#31361;&#21413;&#24093;&#22269;&#27491;&#22312;&#23835;&#36215;&#65292;&#20854;&#20891;&#38431;&#25152;&#21521;&#25259;&#38753;&#65281;')

#####修改结束#####
####修改开始####
        for city in lTargetCities:
            iExtra = 0 + 2
            # 			if utils.getHumanID() not in [iPlayer, city.getOwner()]:
            # 				iExtra += 1 #max(1, gc.getPlayer(iPlayer).getCurrentEra())
            #
            # 			if iPlayer == iMongolia and utils.getHumanID() != iPlayer:
            # 				iExtra += 1

            tPlot = utils.findNearestLandPlot((city.getX(), city.getY()), iPlayer)
            if(tPlot):

                iBestInfantry = utils.getBestInfantry(iPlayer)
                iBestSiege = utils.getBestSiege(iPlayer)

                if iPlayer == iGreece:
                    iBestInfantry = iHoplite
                    iBestSiege = iCatapult
                if iPlayer == iMongolia:
                    iBestInfantry = iKeshik
                    iExtra += 2

                if iPlayer == iCarthage and iYear <= 150:
                    iExtra = 0
                    iBestInfantry = iWarElephant
                    tem_text = '&#36838;&#22826;&#22522;&#30340;&#27721;&#23612;&#25300;&#23558;&#20891;&#32763;&#36234;&#20102;&#38463;&#23572;&#21329;&#26031;&#23665;&#65292;&#20986;&#29616;&#22312;&#31859;&#20848;&#38468;&#36817;&#65281;'
                    CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
                if iPlayer == iBarbarian and iYear <= 150:
                    iExtra = -1
                    iBestInfantry = iMilitia
                    utils.makeUnitAI(iBestInfantry, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
                    utils.makeUnitAI(iLightSwordsman, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)
                    tem_text = '&#26031;&#24052;&#36798;&#20811;&#26031;&#21561;&#21709;&#20102;&#21453;&#25239;&#32599;&#39532;&#30340;&#36215;&#20041;&#21495;&#35282;&#65281;'
                    CyInterface().addMessage(gc.getGame().getActivePlayer(), False, iDuration, tem_text, "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
                if iPlayer == iEngland and iYear <= 1500:
                    iExtra -= 0
                    iBestInfantry = iLongbowman
    #				utils.makeUnitAI(iBestInfantry, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
    #				iBestSiege = iCatapult
                if (iPlayer == iEngland and iYear <= 1250) or (iPlayer == iHolyRome and iYear <= 1250) or (iPlayer == iFrance and iYear <= 1250):
                    iExtra -= 1


    #				iBestInfantry = iLongbowman
    #				utils.makeUnitAI(iBestInfantry, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2)
    #				iBestSiege = iCatapult
                if iPlayer == iTurks and iYear <= 1250:
                    iExtra -= 2

                if iYear >= 1800:
                    iExtra += 1
                if iYear >= 1900:
                    iExtra += 1
                if iYear >= 1930:
                    iExtra += 1
                if iPreferredTarget == utils.getHumanID() and iYear >= 1300:
                    iExtra = gc.getGame().getHandicapType() + 1

                utils.makeUnitAI(iBestInfantry, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, max(2 + iExtra, 1))
                utils.makeUnitAI(iBestSiege, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, max(1 + iExtra, 1))
                ####修改结束#####
                if iPlayer == iGreece:
                    utils.makeUnitAI(iCompanion, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)

                if iPlayer == iTamils:
                    utils.makeUnitAI(iWarElephant, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 1)

                if iPlayer == iSpain:
                    utils.makeUnitAI(utils.getBestCavalry(iPlayer), iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2 * iExtra)

                if iPlayer == iTurks:
                    utils.makeUnitAI(utils.getBestCavalry(iPlayer), iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK_CITY, 2 + iExtra)

    def forgetMemory(self, iTech, iPlayer):
        if iTech in [iPsychology, iTelevision]:
            pPlayer = gc.getPlayer(iPlayer)
            for iLoopCiv in range(iNumPlayers):
                if iPlayer == iLoopCiv: continue
                if pPlayer.AI_getMemoryCount(iLoopCiv, MemoryTypes.MEMORY_DECLARED_WAR) > 0:
                    pPlayer.AI_changeMemoryCount(iLoopCiv, MemoryTypes.MEMORY_DECLARED_WAR, -1)
                if pPlayer.AI_getMemoryCount(iLoopCiv, MemoryTypes.MEMORY_DECLARED_WAR_ON_FRIEND) > 0:
                    pPlayer.AI_changeMemoryCount(iLoopCiv, MemoryTypes.MEMORY_DECLARED_WAR_ON_FRIEND, -1)

    def getNextInterval(self, iGameTurn):
        if iGameTurn > getTurnForYear(1600):
            iMinInterval = iMinIntervalLate
            iMaxInterval = iMaxIntervalLate
        else:
            iMinInterval = iMinIntervalEarly
            iMaxInterval = iMaxIntervalEarly

        iMinInterval = utils.getTurns(iMinInterval)
        iMaxInterval = utils.getTurns(iMaxInterval)

        return iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval - iMinInterval, 'random turn')

    def planWars(self, iGameTurn):

        # skip if there is a world war
        if iGameTurn > getTurnForYear(1500):
            iCivsAtWar = 0
            for iLoopPlayer in range(iNumPlayers):
                tLoopPlayer = gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam())
                if tLoopPlayer.getAtWarCount(True) > 0:
                    iCivsAtWar += 1
            if 100 * iCivsAtWar / gc.getGame().countCivPlayersAlive() > 50:
                data.iNextTurnAIWar = iGameTurn + self.getNextInterval(iGameTurn)
                return

        iAttackingPlayer = self.determineAttackingPlayer()
        iTargetPlayer = self.determineTargetPlayer(iAttackingPlayer)

        data.players[iAttackingPlayer].iAggressionLevel = 0

        if iTargetPlayer == -1:
            return

        if gc.getTeam(iAttackingPlayer).canDeclareWar(iTargetPlayer):
            gc.getTeam(iAttackingPlayer).AI_setWarPlan(iTargetPlayer, WarPlanTypes.WARPLAN_PREPARING_LIMITED)

        data.iNextTurnAIWar = iGameTurn + self.getNextInterval(iGameTurn)

    def determineAttackingPlayer(self):
        lAggressionLevels = [data.players[i].iAggressionLevel for i in range(iNumPlayers) if self.possibleTargets(i)]
        iHighestEntry = utils.getHighestEntry(lAggressionLevels)

        return lAggressionLevels.index(iHighestEntry)

    def possibleTargets(self, iPlayer):
        return [iLoopPlayer for iLoopPlayer in range(iNumPlayers) if iPlayer != iLoopPlayer and gc.getTeam(gc.getPlayer(iPlayer).getTeam()).canDeclareWar(gc.getPlayer(iLoopPlayer).getTeam())]

    def determineTargetPlayer(self, iPlayer):
        pPlayer = gc.getPlayer(iPlayer)
        tPlayer = gc.getTeam(pPlayer.getTeam())
        lPotentialTargets = []
        lTargetValues = [0 for i in range(iNumPlayers)]

        # determine potential targets
        for iLoopPlayer in self.possibleTargets(iPlayer):
            pLoopPlayer = gc.getPlayer(iLoopPlayer)
            tLoopPlayer = gc.getTeam(pLoopPlayer.getTeam())

            if iLoopPlayer == iPlayer: continue

            # requires live civ and past contact
            if not pLoopPlayer.isAlive(): continue
            if not tPlayer.isHasMet(iLoopPlayer): continue

            # no masters or vassals
            if tPlayer.isVassal(iLoopPlayer): continue
            if tLoopPlayer.isVassal(iPlayer): continue

            # not already at war
            if tPlayer.isAtWar(iLoopPlayer): continue

            lPotentialTargets.append(iLoopPlayer)

        if not lPotentialTargets: return -1

        # iterate the map for all potential targets
        for i in range(124):
            for j in range(68):
                iOwner = gc.getMap().plot(i, j).getOwner()
                if iOwner in lPotentialTargets:
                    lTargetValues[iOwner] += pPlayer.getWarValue(i, j)

        # hard to attack with lost contact
        for iLoopPlayer in lPotentialTargets:
            lTargetValues[iLoopPlayer] /= 8

        # normalization
        iMaxValue = utils.getHighestEntry(lTargetValues)
        if iMaxValue == 0: return -1

        for iLoopPlayer in lPotentialTargets:
            lTargetValues[iLoopPlayer] *= 500
            lTargetValues[iLoopPlayer] /= iMaxValue

        for iLoopPlayer in lPotentialTargets:

            # randomization
            if lTargetValues[iLoopPlayer] <= iThreshold:
                lTargetValues[iLoopPlayer] += gc.getGame().getSorenRandNum(100, 'random modifier')
            else:
                lTargetValues[iLoopPlayer] += gc.getGame().getSorenRandNum(300, 'random modifier')

            # balanced by attitude
            iAttitude = pPlayer.AI_getAttitude(iLoopPlayer) - 2
            if iAttitude > 0:
                lTargetValues[iLoopPlayer] /= 2 * iAttitude

            # exploit plague
            if data.players[iLoopPlayer].iPlagueCountdown > 0 or data.players[iLoopPlayer].iPlagueCountdown < -10:
                if gc.getGame().getGameTurn() > getTurnForYear(tBirth[iLoopPlayer]) + utils.getTurns(20):
                    lTargetValues[iLoopPlayer] *= 3
                    lTargetValues[iLoopPlayer] /= 2

            # determine master
            iMaster = -1
            for iLoopMaster in range(iNumPlayers):
                if tLoopPlayer.isVassal(iLoopMaster):
                    iMaster = iLoopMaster
                    break

            # master attitudes
            if iMaster >= 0:
                iAttitude = gc.getPlayer(iMaster).AI_getAttitude(iLoopPlayer)
                if iAttitude > 0:
                    lTargetValues[iLoopPlayer] /= 2 * iAttitude

            # peace counter
            if not tPlayer.isAtWar(iLoopPlayer):
                iCounter = min(7, max(1, tPlayer.AI_getAtPeaceCounter(iLoopPlayer)))
                if iCounter <= 7:
                    lTargetValues[iLoopPlayer] *= 20 + 10 * iCounter
                    lTargetValues[iLoopPlayer] /= 100

            # defensive pact
            if tPlayer.isDefensivePact(iLoopPlayer):
                lTargetValues[iLoopPlayer] /= 4

            # consider power
            iOurPower = tPlayer.getPower(True)
            iTheirPower = gc.getTeam(iLoopPlayer).getPower(True)
            if iOurPower > 2 * iTheirPower:
                lTargetValues[iLoopPlayer] *= 2
            elif 2 * iOurPower < iTheirPower:
                lTargetValues[iLoopPlayer] /= 2

            # spare smallish civs
            if iLoopPlayer in [iNetherlands, iPortugal, iItaly]:
                lTargetValues[iLoopPlayer] *= 4
                lTargetValues[iLoopPlayer] /= 5

            # no suicide
            if iPlayer == iNetherlands:
                if iLoopPlayer in [iFrance, iHolyRome, iGermany]:
                    lTargetValues[iLoopPlayer] /= 2
            elif iPlayer == iPortugal:
                if iLoopPlayer == iSpain:
                    lTargetValues[iLoopPlayer] /= 2
            elif iPlayer == iItaly:
                if iLoopPlayer in [iFrance, iHolyRome, iGermany]:
                    lTargetValues[iLoopPlayer] /= 2

        return utils.getHighestIndex(lTargetValues)
