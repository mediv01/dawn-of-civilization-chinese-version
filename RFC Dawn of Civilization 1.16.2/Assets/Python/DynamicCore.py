from CvPythonExtensions import *
from Consts import *
from RFCUtils import utils

# Peak that change to hills during the game, like Bogota
lPeakExceptions = [(31, 13), (32, 19), (27, 29), (88, 47), (40, 66)]
gc = CyGlobalContext()

tCoreAreaChina = [[[100, 43],    [104, 46]],              #中国在BC2070年核心的初始值
[[100, 43],    [107, 47]],                 #BC221年秦朝统一六国
[[100, 42],    [107, 47]],                 #AD280晋朝建立
[[100, 41],    [107, 47]],                 #AD610 贞观之治
[[98, 39],    [106, 44]],                 #AD1127南宋建立，北京沦陷，客家人南迁
[[98, 39],    [107, 47]],                 #AD1368明朝建立，收复北方
[[98, 39],    [107, 49]],                 #AD1710 清朝康乾盛世，核心拓展至沈阳
[[99, 43],    [106, 47]],                 #AD1851太平天朝，核心缩小到北方省份
[[100, 39],    [107, 43]],                 #AD1912民国时期核心进一步减小到南方省份
[[100, 39],    [107, 43]],                 #AD1937 抗日战争后缩小至西南
[[98, 38],    [107, 54]],                 #AD1949 新中国成立后核心恢复
]

tCoreAreaPerisa = [[[79, 37],    [85, 44]],               #BC850
[[76, 37],    [87, 46]],               #BC550
[[79, 37],    [85, 44]],               #AD300
]

tCoreAreaTamils = [[[90, 27],    [93, 32]],               #BC400
[[88, 27],    [93, 34]],               #AD100
[[90, 27],    [93, 32]],               #AD1200
]# Tamils
def checkturn(iGameTurn):
    if (gc.getDefineINT("PYTHON_ALLOW_DYNAMIC_CORE") == 0):return
    iPlayer = iChina  #中国
    if gc.getGame().getGameTurn() == getTurnForYear(-221):
        updateCore(iPlayer,tCoreAreaChina[1])    #0是初始值！
        if utils.getHumanID() == iPlayer:      utils.show('&#31206;&#22987;&#30343;&#19968;&#32479;&#20845;&#22269;&#65292;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#21306;&#22495;&#20063;&#38543;&#20043;&#25193;&#24352;&#21040;&#21271;&#26041;&#22320;&#21306;&#65281;')  #秦始皇一统六国，中华文明的核心区域也随之扩张到北方地区！
        pass    
    elif gc.getGame().getGameTurn() == getTurnForYear(280):
        updateCore(iPlayer,tCoreAreaChina[2])    
        if utils.getHumanID() == iPlayer:      utils.show('&#35199;&#26187;&#29579;&#26397;&#30340;&#24314;&#31435;&#32467;&#26463;&#20102;&#19977;&#22269;&#26102;&#26399;&#20013;&#21326;&#25991;&#26126;&#30340;&#20998;&#35010;&#65292;&#20013;&#21326;&#27665;&#26063;&#30340;&#26680;&#24515;&#20063;&#38543;&#20043;&#21335;&#25193;&#65281;')  #西晋王朝的建立结束了三国时期中华文明的分裂，中华民族的核心也随之南扩！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(610):                     
        updateCore(iPlayer,tCoreAreaChina[3])    
        if utils.getHumanID() == iPlayer:      utils.show('&#36126;&#35266;&#20043;&#27835;&#24320;&#21551;&#20102;&#20013;&#21326;&#30427;&#19990;&#65292;&#27743;&#21335;&#22320;&#21306;&#20063;&#34987;&#20013;&#21326;&#25991;&#26126;&#36827;&#19968;&#27493;&#24320;&#21457;&#20026;&#24093;&#22269;&#30340;&#26680;&#24515;&#21306;&#22495;&#65281;')  #贞观之治开启了中华盛世，江南地区也被中华文明进一步开发为帝国的核心区域！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1127):
        updateCore(iPlayer,tCoreAreaChina[4])    
        if utils.getHumanID() == iPlayer:      utils.show('&#21335;&#23435;&#26102;&#26399;&#37329;&#26397;&#23835;&#36215;&#65292;&#20013;&#21326;&#25991;&#26126;&#20002;&#22833;&#20102;&#21271;&#26041;&#30340;&#26680;&#24515;&#22320;&#21306;&#65292;&#37096;&#20998;&#26680;&#24515;&#20154;&#27665;&#34987;&#36843;&#21335;&#36801;&#33267;&#24191;&#19996;&#21644;&#31119;&#24314;&#65281;')  #南宋时期金朝崛起，中华文明丢失了北方的核心地区，部分核心人民被迫南迁至广东和福建！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1368):
        updateCore(iPlayer,tCoreAreaChina[5])    
        if utils.getHumanID() == iPlayer:      utils.show('&#22823;&#26126;&#29579;&#26397;&#30340;&#24314;&#31435;&#37325;&#26032;&#32479;&#19968;&#20102;&#20013;&#21326;&#22823;&#22320;&#65292;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#20063;&#38543;&#20043;&#25193;&#22823;&#65281;')  #大明王朝的建立重新统一了中华大地，中华文明的核心也随之扩大！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1710):
        updateCore(iPlayer,tCoreAreaChina[6])    
        if utils.getHumanID() == iPlayer:      utils.show('&#28165;&#29579;&#26397;&#36827;&#20837;&#24247;&#20094;&#30427;&#19990;&#65292;&#19996;&#21271;&#22320;&#21306;&#20063;&#32435;&#20837;&#20013;&#21326;&#24093;&#22269;&#30340;&#26680;&#24515;&#39046;&#22320;&#65281;')  #清王朝进入康乾盛世，东北地区也纳入中华帝国的核心领地！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1851):
        updateCore(iPlayer,tCoreAreaChina[7])    
        if utils.getHumanID() == iPlayer:      utils.show('&#22826;&#24179;&#22825;&#22269;&#36215;&#20041;&#20351;&#24471;&#28165;&#29579;&#26397;&#20002;&#22833;&#20102;&#21335;&#26041;&#30340;&#26680;&#24515;&#39046;&#22320;&#65281;')  #太平天国起义使得清王朝丢失了南方的核心领地！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1912):
        updateCore(iPlayer,tCoreAreaChina[8])    
        if utils.getHumanID() == iPlayer:      utils.show('&#36763;&#20133;&#38761;&#21629;&#21518;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#36716;&#31227;&#33267;&#20013;&#21326;&#25991;&#26126;&#30340;&#21335;&#37096;&#22320;&#21306;&#65281;')  #辛亥革命后中华文明的核心转移至中华文明的南部地区！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1937):
        updateCore(iPlayer,tCoreAreaChina[9])    
        if utils.getHumanID() == iPlayer:      utils.show('&#25239;&#26085;&#25112;&#20105;&#30340;&#29190;&#21457;&#33268;&#20351;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#21306;&#22495;&#32553;&#23567;&#33267;&#22235;&#24029;&#38468;&#36817;&#65281;')  #抗日战争的爆发致使中华文明的核心区域缩小至四川附近！
        pass
    elif gc.getGame().getGameTurn() == getTurnForYear(1949):
        updateCore(iPlayer,tCoreAreaChina[10])    
        if utils.getHumanID() == iPlayer:      utils.show('&#26032;&#20013;&#22269;&#24314;&#31435;&#20102;&#65281;&#20013;&#22269;&#20154;&#27665;&#20174;&#27492;&#31449;&#20102;&#36215;&#26469;&#65281;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#20063;&#38543;&#20043;&#25299;&#23637;&#20102;&#65281;')  #新中国建立了！中国人民从此站了起来！中华文明的核心也随之拓展了！
        pass
    

    iPlayer= iPersia  #波斯
    if gc.getGame().getGameTurn() == getTurnForYear(-550):
        updateCore(iPlayer,tCoreAreaPerisa[1])    #0是初始值！
        #if utils.getHumanID() == iPlayer:      utils.show('&#31206;&#22987;&#30343;&#19968;&#32479;&#20845;&#22269;&#65292;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#21306;&#22495;&#20063;&#38543;&#20043;&#25193;&#24352;&#21040;&#21271;&#26041;&#22320;&#21306;&#65281;')  #秦始皇一统六国，中华文明的核心区域也随之扩张到北方地区！
        pass    
    if gc.getGame().getGameTurn() == getTurnForYear(300):
        updateCore(iPlayer,tCoreAreaPerisa[2])    
        #if utils.getHumanID() == iPlayer:      utils.show('&#35199;&#26187;&#29579;&#26397;&#30340;&#24314;&#31435;&#32467;&#26463;&#20102;&#19977;&#22269;&#26102;&#26399;&#20013;&#21326;&#25991;&#26126;&#30340;&#20998;&#35010;&#65292;&#20013;&#21326;&#27665;&#26063;&#30340;&#26680;&#24515;&#20063;&#38543;&#20043;&#21335;&#25193;&#65281;')  #西晋王朝的建立结束了三国时期中华文明的分裂，中华民族的核心也随之南扩！
        pass

    iPlayer= iTamils  #泰米尔
    if gc.getGame().getGameTurn() == getTurnForYear(100):
        updateCore(iPlayer,tCoreAreaTamils[1])    #0是初始值！
        #if utils.getHumanID() == iPlayer:      utils.show('&#31206;&#22987;&#30343;&#19968;&#32479;&#20845;&#22269;&#65292;&#20013;&#21326;&#25991;&#26126;&#30340;&#26680;&#24515;&#21306;&#22495;&#20063;&#38543;&#20043;&#25193;&#24352;&#21040;&#21271;&#26041;&#22320;&#21306;&#65281;')  #秦始皇一统六国，中华文明的核心区域也随之扩张到北方地区！
        pass    
    if gc.getGame().getGameTurn() == getTurnForYear(1200):
        updateCore(iPlayer,tCoreAreaTamils[2])    
        #if utils.getHumanID() == iPlayer:      utils.show('&#35199;&#26187;&#29579;&#26397;&#30340;&#24314;&#31435;&#32467;&#26463;&#20102;&#19977;&#22269;&#26102;&#26399;&#20013;&#21326;&#25991;&#26126;&#30340;&#20998;&#35010;&#65292;&#20013;&#21326;&#27665;&#26063;&#30340;&#26680;&#24515;&#20063;&#38543;&#20043;&#21335;&#25193;&#65281;')  #西晋王朝的建立结束了三国时期中华文明的分裂，中华民族的核心也随之南扩！
        pass
    
    



def getCoreArea(iPlayer,iCoreArea):
    lExceptions = []
    #lExceptions = getOrElse(dExceptions, iPlayer, [])
    left, bottom = iCoreArea[0]
    right, top = iCoreArea[1]
    return [(x, y) for x in range(left, right + 1) for y in range(bottom, top + 1) if (x, y) not in lExceptions]


def updateCore(iPlayer,iCoreArea):
#    if utils.getHumanID() == iPlayer: utils.show('The Core Area of Your
#    Civilization has been changed!') #The Core Area of Your Civilization has been
#    changed!
    lCore = getCoreArea(iPlayer,iCoreArea)
    for x in range(iWorldX):
        for y in range(iWorldY):
            plot = gc.getMap().plot(x, y)
            if plot.isWater() or (plot.isPeak() and (x, y) not in lPeakExceptions): continue
            plot.setCore(iPlayer, (x, y) in lCore)