# coding=utf-8
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
import Stability


gc = CyGlobalContext()
localText = CyTranslator()

def isDecline(iPlayer):
    return utils.getHumanID() != iPlayer and not utils.isReborn(
        iPlayer) and gc.getGame().getGameTurn() >= getTurnForYear(tFall[iPlayer])

def calculateTopCities_population():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getPopulation()
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities

def calculateTopCities_culture():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getCulture(iLoopPlayer)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities

def calculateTopCities_production():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_PRODUCTION)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities


def calculateTopCities_COMMERCE():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_COMMERCE)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities


def calculateTopCities_FOOD():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_FOOD)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities

def getTechValue(BuyTechPlayer, tradeitemID, sellTechPlayer=utils.getHumanID()):
    tradetypeID = TRADE_TECHNOLOGIES
    techmoney = gc.getAIdealValuetoMoney(sellTechPlayer, BuyTechPlayer, tradetypeID, tradeitemID)
    return techmoney


def canTradeTech(BuyPlayer, tradeitemID, SellPlayer=utils.getHumanID()):
    team = gc.getTeam(gc.getPlayer(SellPlayer).getTeam())
    if not team.isHasTech(tradeitemID):
        return False

    tradeData = TradeData()
    tradeData.ItemType = TradeableItems.TRADE_TECHNOLOGIES
    tradeData.iData = tradeitemID

    bTechTrade = (gc.getPlayer(SellPlayer).canTradeItem(BuyPlayer, tradeData, False))
    if not bTechTrade:
        return False

    return True


def getScreenHelp():

    import Debug
    Debug.main()


    aHelp = []
    #游戏基本信息
    if(gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_00") == 1):
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_BASIC", ()))
        iHandicap = gc.getGame().getHandicapType()
        aHelp.append(' Handicap Level (1-5): '+str(iHandicap+1))
        iScenario=utils.getScenario()
        txtScenario=['BC3000', 'AD600', 'AD1700']
        iGameSpeed = gc.getGame().getGameSpeedType()
        speedtext = u"正常速度"
        if iGameSpeed==0:
            speedtext = "马拉松速度"
        elif iGameSpeed==1:
            speedtext = "史诗速度"

        aHelp.append(' Scenario : ' + str(txtScenario[iScenario]) + "     Speed: " + str(speedtext))

    # 勒索国家金币的信息
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_SHOW_AITRADE_ON_MONEY") >0):
        aHelp.append(' ')
        aHelp.append('可勒索金币数量排名')
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive() and iCiv is not utils.getHumanID()):
                iPlayer = iCiv
                human = utils.getHumanID()
                cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                a = gc.AI_considerOfferThreshold(human, iPlayer)  # 3是中国
                b = gc.getPlayer(iPlayer).AI_maxGoldTrade(human)
                c = min(a, b)
                if cantrade and c > 0:
                    civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                    aHelp.append(civname + ':' + str(c))

        pass

    # 科技交易信息
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_SHOW_AITRADE_ON_TECH") >0):
        aHelp.append(' ')
        aHelp.append('AI可卖科技列表：')
        for iCiv in range(iNumPlayers):
            iPlayer = iCiv
            human = utils.getHumanID()
            if (gc.getPlayer(iCiv).isAlive() and iCiv is not human):
                for iTech in range(iNumTechs):
                    cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                    buyplayer = human
                    sellplayer = iPlayer
                    AIhastech = gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTech)
                    Humanhastech = gc.getTeam(gc.getPlayer(human).getTeam()).isHasTech(iTech)
                    if (AIhastech and not Humanhastech):
                        techvalue = getTechValue(buyplayer, iTech, sellplayer)
                        if techvalue > 0:
                            civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                            techname = utils.getTechNameCn(iTech)
                            cantradetext = ''
                            bcantradetech = canTradeTech(buyplayer, iTech, sellplayer)
                            if (not cantrade or not bcantradetech):
                                cantradetext = '[目前无法交易]'
                            aHelp.append(civname + ':     ' + techname + '(' + str(techvalue) + ')' + cantradetext)

        aHelp.append(' ')
        aHelp.append('人类可卖科技列表：')
        for iCiv in range(iNumPlayers):
            iPlayer = iCiv
            human = utils.getHumanID()
            if (gc.getPlayer(iCiv).isAlive() and iCiv is not human):
                for iTech in range(iNumTechs):
                    cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                    buyplayer = iPlayer
                    sellplayer = human
                    AIhastech = gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTech)
                    Humanhastech = gc.getTeam(gc.getPlayer(human).getTeam()).isHasTech(iTech)
                    if (not AIhastech and Humanhastech):
                        techvalue = getTechValue(buyplayer, iTech, sellplayer)
                        if techvalue > 0:
                            civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                            techname = utils.getTechNameCn(iTech)
                            cantradetext = ''
                            bcantradetech = canTradeTech(buyplayer, iTech, sellplayer)

                            bTradeWorth = False
                            iAImaxMoney = gc.getPlayer(buyplayer).AI_maxGoldTrade(utils.getHumanID())
                            PYTHON_TECHTRADE_VALUE_MIN_PERCENT = 80
                            iMinPercent = PYTHON_TECHTRADE_VALUE_MIN_PERCENT
                            iThreshold = techvalue * iMinPercent / 100
                            if (iAImaxMoney >= iThreshold):
                                bTradeWorth = True

                            if (not cantrade or not bcantradetech or not bTradeWorth):
                                cantradetext = '[目前无法交易]'
                                # aHelp.append(civname + ':     ' + techname + '(' + str(techvalue) + ')' + cantradetext)
                            else:
                                txt = '%s:    %s  :  %d (%d' % (civname, techname, techvalue, iAImaxMoney * 100 / techvalue) + '%)'
                                aHelp.append(txt)
                                # aHelp.append(civname + ':     ' + techname+'('+str(techvalue)+')' + cantradetext)

        pass

    #部落村庄信息：
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_11") > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_GOODY", ()))
        goody_list=[]
        for x in range(gc.getMap().getGridWidth()):
            for y in range(gc.getMap().getGridHeight()):
                plot = gc.getMap().plot(x, y)
                isgoody=plot.isGoody()
                regionid = plot.getRegionID()
                if(isgoody):
                    goody_list.append([regionid,x,y])



        goody_list.sort(key=lambda x:x[0])


        for i in range(len(goody_list)):
            regionid=goody_list[i][0]
            x=goody_list[i][1]
            y = goody_list[i][2]
            if regionid >= 0:
                regionname = utils.getRegionNameCn(regionid)
                aHelp.append('Goody ['+str(i)+'] in X:' + str(x) + '  Y: ' + str(y) + ' RegionName: ' + regionname)
            else:

                aHelp.append('Goody in X:' + str(x) + '  Y: ' + str(y))

    # 稳定度信息：
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_12") > 0):
        aHelp.append(' ')
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                #稳定度免疫信息
                Stability_Immune=0
                War_Immune=0
                if Stability.isImmune(iCiv):
                    Stability_Immune=1
                if Stability.isImmune_War(iCiv):
                    War_Immune = 1
                if (Stability_Immune or War_Immune):
                    iPlayer=iCiv
                    civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                    Stability_Immune_Turn1=Stability.calculate_stability_immune_after_Scenario_Start()+utils.getScenarioStartTurn()-gc.getGame().getGameTurn()
                    Stability_Immune_Turn2 = Stability.calculate_stability_immune_after_birth() + getTurnForYear(tBirth[iPlayer])  - gc.getGame().getGameTurn()
                    Stability_Immune_Turn3 = Stability.calculate_stability_immune_after_resurrection() + gc.getPlayer(iPlayer).getLatestRebellionTurn()- gc.getGame().getGameTurn()
                    Stability_Immune_Turn=max(Stability_Immune_Turn1,Stability_Immune_Turn2,Stability_Immune_Turn3,0)
                    War_Immune_Turn1 = Stability.calculate_war_immune() + utils.getScenarioStartTurn() - gc.getGame().getGameTurn()
                    War_Immune_Turn2 = Stability.calculate_war_immune()+ getTurnForYear(tBirth[iPlayer]) - gc.getGame().getGameTurn()
                    War_Immune_Turn3 = Stability.calculate_war_immune() + gc.getPlayer(iPlayer).getLatestRebellionTurn() - gc.getGame().getGameTurn()
                    War_Immune_Turn=max(War_Immune_Turn1,War_Immune_Turn2,War_Immune_Turn3,0)

                    tiptext=civname+": Stability Immune Turn Left: "+str(Stability_Immune_Turn)+"    War Immune Turn Left: " +str(War_Immune_Turn)
                    aHelp.append(tiptext)
    # 1.国际会议回合
    if(gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_01") == 1):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CONGRESS", ())+str(data.iCongressTurns))

        iGameTurn=gc.getGame().getGameTurn()
        ti=0
        for i in range(len(tBirth)):
            if(getTurnForYear(tBirth[i])>=iGameTurn):
                ti=i
                break
        aHelp.append("Next Country    "+gc.getPlayer(ti).getCivilizationShortDescription(0)+"    Birth in "+str(tBirth[ti])+" with turns left: "+str(getTurnForYear(tBirth[i])-iGameTurn))



    # 2.殖民地进度
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_02") == 1):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_COLONIST", ()))
        for iCiv in [iSpain, iEngland, iFrance, iPortugal, iNetherlands, iVikings, iGermany]:
            showtext1=str(gc.getPlayer(iCiv).getCivilizationShortDescription(0)+':    ')
            showtext2=str(data.players[iCiv].iColonistsAlreadyGiven)+' / '+str(dMaxColonists[iCiv])
            showtext3=''
            if (data.players[iCiv].iColonistsAlreadyGiven<dMaxColonists[iCiv]):
                iGameTurn = (data.players[iCiv].iExplorationTurn + 1 + data.players[iCiv].iColonistsAlreadyGiven * 8)-gc.getGame().getGameTurn()
                if (iGameTurn<0):
                    iGameTurn=0
                showtext3=str('                next exploration turn: '+str(iGameTurn))
            aHelp.append(showtext1+showtext2+showtext3)

    #3.瘟疫进度
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_03") == 1):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_PLAGUE", ()))
        for i in range(4):
            plague_turn=data.lGenericPlagueDates[i]
            iGameTurn=max(plague_turn-gc.getGame().getGameTurn(),0)
            aHelp.append('Plague '+str(i+1)+' start in: '+str(plague_turn)+'   turn,    Game turn left:  '+str(iGameTurn))

    #4.科技进度
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_04") >0):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getTechHistory(gc.getGame().getGameTurn()-1)
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass
        AveragePoint=1
        if(len(valuelist)>0 and sum(valuelist)>0):
            AveragePoint=sum(valuelist)/len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_TECHRANK", ()))


        techlist.sort(key=lambda x:-x[1])
        for i in range(len(techlist)):
            if (i<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_04")):
                iCiv = techlist[i][0]
                iTechValue=techlist[i][1]
                civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname=civname+'[F]'

                rank_percent=iTechValue*100/AveragePoint
                aHelp.append(' RANK ('+str(i+1)+') : '+civname+'             with '+str(iTechValue)+'  ('+str(rank_percent)+'%)')

    # 5.军事实力
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_05") >0):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getPowerHistory(gc.getGame().getGameTurn()-1)
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass
        AveragePoint=1
        if(len(valuelist)>0 and sum(valuelist)>0):
            AveragePoint=sum(valuelist)/len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_ARMYRANK", ()))


        techlist.sort(key=lambda x:-x[1])
        for i in range(len(techlist)):
            if (i < gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_05")):
                iCiv = techlist[i][0]
                iTechValue=techlist[i][1]
                civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname=civname+'[F]'

                rank_percent=iTechValue*100/AveragePoint
                aHelp.append(' RANK ('+str(i+1)+') : '+civname+'             with '+str(iTechValue)+'  ('+str(rank_percent)+'%)')


    # 5.文化实力
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_05") >0):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getCultureHistory(gc.getGame().getGameTurn()-1)
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass
        AveragePoint=1
        if(len(valuelist)>0 and sum(valuelist)>0):
            AveragePoint=sum(valuelist)/len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CULTURERANK", ()))


        techlist.sort(key=lambda x:-x[1])
        for i in range(len(techlist)):
            if (i < gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_05")):
                iCiv = techlist[i][0]
                iTechValue=techlist[i][1]
                civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname=civname+'[F]'

                rank_percent=iTechValue*100/AveragePoint
                aHelp.append(' RANK ('+str(i+1)+') : '+civname+'             with '+str(iTechValue)+'  ('+str(rank_percent)+'%)')

    # 5.AI性格
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_05") >0 and 1==2):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                #iTechValue = gc.getPlayer(iCiv).getCultureHistory(gc.getGame().getGameTurn()-1)
                iStrategyNum=gc.showAIstrategy(iCiv)
                #iStrategyNum=1
                iTechValue=iStrategyNum
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass



        for i in range(len(techlist)):

            iCiv = techlist[i][0]
            iTechValue=techlist[i][1]
            civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
            if (isDecline(iCiv)):
                civname=civname+'[F]'
            txt1=civname+' 的策略是 '+str(iTechValue)
            aHelp.append(txt1)


    #6.世界最大城市排名
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_06") >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_POP", ()))
        lCities=calculateTopCities_population()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_06")):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass


    #7.世界文化最高城市排名
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_07") >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_CUL", ()))
        lCities=calculateTopCities_culture()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_07")):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #8.世界工业产量最高城市排名
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_08") >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_PRO", ()))
        lCities=calculateTopCities_production()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_08")):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #9.世界商业产出最高城市排名
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_09") >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_COM", ()))
        lCities=calculateTopCities_COMMERCE()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_09")):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #10.世界食物产出最高城市排名
    if (gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_10") >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_FOOD", ()))
        lCities=calculateTopCities_FOOD()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<gc.getDefineINT("PYTHON_SCREEN_VICTORY_TIPS_10")):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass



    '''
    iDebug=1
    #下面代码仅为DEBUG使用
    if (iDebug):
        for ePlayer in range(iNumActivePlayers):
            researchCost = str(gc.getTeam(gc.getPlayer(ePlayer).getTeam()).getResearchCost(100)*100/3000)
            civname=gc.getPlayer(ePlayer).getCivilizationShortDescription(0)
            utils.debug_manual(civname+','+researchCost,'ResearchCost')
    '''

    return aHelp
    pass


