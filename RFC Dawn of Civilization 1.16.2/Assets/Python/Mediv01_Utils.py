from CvPythonExtensions import *


gc = CyGlobalContext()
localText = CyTranslator()

def getTurn():
    return gc.getGame().getGameTurn()


def getYear():
    return gc.getGame().getGameTurnYear()


def getTurnForYear(iGameturn):
    return gc.getGame().getTurnYear(iGameturn)


def PlotToStr(tPlot):
    return '(' + str(tPlot[0]) + ', ' + str(tPlot[1]) + ')'

def FillNumberToText(num1,length):
    num = str(num1)
    if (len(num)>=length):
        return str(num)
    else:
        gap=length-len(num)
        s=''
        for i in range(gap):
            s = s + '  '
        s = s +str(num)
        return s