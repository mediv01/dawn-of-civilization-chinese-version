

def checkturn(iGameTurn):


    import DynamicCore
    import AITrade
    AITrade.checkturn(iGameTurn)
    DynamicCore.checkturn(iGameTurn)


    import Autosave_Checkturn
    Autosave_Checkturn.checkTurn(iGameTurn)
    import DoResurrectionManual
    DoResurrectionManual.checkTurn(iGameTurn)
    import GameScore
    GameScore.checkTurn(iGameTurn)
    import DynamicLand
    DynamicLand.checkturn(iGameTurn)

    import DynamicModifiers
    DynamicModifiers.checkturn(iGameTurn)

    import DOC_UAV
    DOC_UAV.CheckTurn(iGameTurn)

    import ObserverMode
    ObserverMode.CheckTurn(iGameTurn)