#include "CvGameCoreDLL.h"
#include "CyHallOfFameInfo.h"
#include "CyReplayInfo.h"
//mediv01 CY系列主要是接口函数，对接CV中的游戏逻辑 202000822
CyHallOfFameInfo::CyHallOfFameInfo()
{
}


void CyHallOfFameInfo::loadReplays()
{
	m_hallOfFame.loadReplays();
}

int CyHallOfFameInfo::getNumGames() const
{
	return m_hallOfFame.getNumGames();
}

CyReplayInfo* CyHallOfFameInfo::getReplayInfo(int i)
{
	return (new CyReplayInfo(m_hallOfFame.getReplayInfo(i)));
}

