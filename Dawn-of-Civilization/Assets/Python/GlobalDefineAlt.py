# coding=utf-8
from Consts import *

# 禁用的国家的ID，该国家不会出生
PYTHON_NO_BIRTH_COUNTRY=()

# 禁用的AIWAR ID，该AIWAR不会发生
PYTHON_NO_AIWAR_ID=()

#  人类玩家修正系数是否启用
PYTHON_HUMAN_MODIFIER_ENABLE = 0
#  S表示数值越小对人类玩家惩罚越大，B表示数值越大对人类玩家的惩罚越大
#                         文化（S）  升级经验阈值（B）  科研惩罚（B）  距离维护费（B）  城市数量维护费（B） 政策经验阈值（B） 此项别改   造单位费用（B）    造奇观费用（B）      造建筑费用（B）     通胀率（B）     伟人阈值（B）    人口增长阈值（B）
PYTHON_HUMAN_MODIFIER =(    100,       100,            100,          100,            100,           100,             100,            100,               100,               100,             100,            100,             100)

# 例如：增大人类玩家难度的参数组合
# PYTHON_HUMAN_MODIFIER =(     80,       150,            1000,          150,            150,           150,            100,          150,               150,               150,             120,            120,             120)



