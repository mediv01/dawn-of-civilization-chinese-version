#include "CvGameCoreDLL.h"
#include "CvHallOfFameInfo.h"
#include "CvGlobals.h"
//mediv01 20200815  ËÆºõÊÇµ×²ãÎÄ¼þ
CvHallOfFameInfo::CvHallOfFameInfo()
{
}

CvHallOfFameInfo::~CvHallOfFameInfo()
{
	for (uint i = 0; i < m_aReplays.size(); i++)
	{
		SAFE_DELETE(m_aReplays[i]);
	}
}

void CvHallOfFameInfo::loadReplays()
{
	gDLL->loadReplays(m_aReplays);
}

int CvHallOfFameInfo::getNumGames() const
{
	return (int)m_aReplays.size();
}

CvReplayInfo* CvHallOfFameInfo::getReplayInfo(int i)
{
	return m_aReplays[i];
}