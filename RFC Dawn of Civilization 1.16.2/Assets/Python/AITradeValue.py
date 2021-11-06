from CvPythonExtensions import *
from Consts import *
from RFCUtils import utils
import TradeUtil
import Stability


gc = CyGlobalContext()

def getAITechValue(AIplayer,tradeitemID):
    eplayer=utils.getHumanID()
    tradetypeID=TRADE_TECHNOLOGIES
    techmoney = gc.getAIdealValuetoMoney(eplayer,AIplayer,tradetypeID,tradeitemID)
    #utils.log2(str(techmoney),'testtradetechval')
    return techmoney

def getAITradableMoney(AIplayer):
    iMoney = gc.getPlayer(AIplayer).AI_maxGoldTrade(utils.getHumanID())
    return iMoney

def cantradeTech(AIplayer,tradeitemID):

    team = gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam())
    if not team.isHasTech(tradeitemID):
        return False

    tradeData = TradeData()
    tradeData.ItemType = TradeableItems.TRADE_TECHNOLOGIES
    tradeData.iData = tradeitemID
    pPlayer=gc.getPlayer(utils.getHumanID())
    bTechTrade=(pPlayer.canTradeItem(AIplayer, tradeData, False))
    if not bTechTrade:
        return False

    return True


# 科技可以被卖 且卖的价格合适
def isTechTradalbeAndWorthy(AIplayer,tradeitemID):
    if gc.getDefineINT("PYTHON_CAN_USE_TECHTRADE_VALUE_ALERT") <= 0:
        return False

    if (not cantradeTech(AIplayer,tradeitemID)):
        return False

    if AIplayer==utils.getHumanID():
        return False
    # 独立城邦
    if AIplayer >= iNumPlayers:
        return False
    iValue=getAITechValue(AIplayer,tradeitemID)
    iAImaxMoney=getAITradableMoney(AIplayer)

    iMinPercent=gc.getDefineINT("PYTHON_TECHTRADE_VALUE_MIN_PERCENT")
    iThreshold=iValue * iMinPercent /100

    if (iAImaxMoney >= iThreshold):
        return True




