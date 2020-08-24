/*
 *    Copyright (C) 2020 by YOUR NAME HERE
 *
 *    This file is part of RoboComp
 *
 *    RoboComp is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    RoboComp is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
	\brief
	@author authorname
*/

// THIS IS AN AGENT

#ifndef SPECIFICWORKER_H
#define SPECIFICWORKER_H

#include <genericworker.h>
#include <innermodel/innermodel.h>

class PersonCsvData
{
private:
public:
	double posX;
	double posZ;
	double rotRY;
	PersonCsvData(double posX1 = 0, double posZ1 = 0, double rotRY1 = 0)
	{
		posX = posX1;
		posZ = posZ1;
		rotRY = rotRY1;
	}
	~PersonCsvData()
	{
	}
	void getValues()
	{
		printf("%f -- %f -- %f\n", posX, posZ, rotRY);
	}
};

class SpecificWorker : public GenericWorker
{
	Q_OBJECT

public:
	SpecificWorker(MapPrx &mprx);
	~SpecificWorker();
	bool setParams(RoboCompCommonBehavior::ParameterList params);

	bool AGMCommonBehavior_activateAgent(const ParameterMap &prs);
	bool AGMCommonBehavior_deactivateAgent();
	ParameterMap AGMCommonBehavior_getAgentParameters();
	StateStruct AGMCommonBehavior_getAgentState();
	void AGMCommonBehavior_killAgent();
	bool AGMCommonBehavior_reloadConfigAgent();
	bool AGMCommonBehavior_setAgentParameters(const ParameterMap &prs);
	int AGMCommonBehavior_uptimeAgent();

	void AGMExecutiveTopic_edgeUpdated(const RoboCompAGMWorldModel::Edge &modification);
	void AGMExecutiveTopic_edgesUpdated(const RoboCompAGMWorldModel::EdgeSequence &modifications);
	void AGMExecutiveTopic_selfEdgeAdded(const int nodeid, const string &edgeType, const RoboCompAGMWorldModel::StringDictionary &attributes);
	void AGMExecutiveTopic_selfEdgeDeleted(const int nodeid, const string &edgeType);
	void AGMExecutiveTopic_structuralChange(const RoboCompAGMWorldModel::World &w);
	void AGMExecutiveTopic_symbolUpdated(const RoboCompAGMWorldModel::Node &modification);
	void AGMExecutiveTopic_symbolsUpdated(const RoboCompAGMWorldModel::NodeSequence &modifications);

	void initializeUI();
	int initPersons(int personId);
	vector<double> getNextValue(std::shared_ptr<std::ifstream> fileD);

	int includeInAGM(int id, const RoboCompInnerModelManager::Pose3D &pose, std::string mesh);
	bool includeInRCIS(int id, const RoboCompInnerModelManager::Pose3D &pose, std::string mesh);
	void movePersons(int person_ID, PersonCsvData personPoseData);
	void extractCSV(string filename);

public slots:
	void compute();
	void initialize(int period);
	void browseButtonClicked();
	void browseButton2Clicked();
	void playButton();
	void pauseButton();
	void stopButton();
	void play_timer();
	void frameUpdate();
	void prevButton();
	void nextButton();
	void firstButton();
	void lastButton();
	void horizontalSliderMoved(int val);

private:
	std::shared_ptr<InnerModel> innerModel;
	std::string action;
	ParameterMap params;
	AGMModel::SPtr worldModel;
	bool active;
	bool setParametersAndPossibleActivation(const ParameterMap &prs, bool &reactivated);
	bool sendModificationProposal(AGMModel::SPtr &worldModel, AGMModel::SPtr &newModel);
	vector<shared_ptr<ifstream>> myFiles;
	vector<int> personGenId;
	QTimer playTimer;
	int number_of_person;
	int frameNumber, frameMax;
	map<int, vector<PersonCsvData>> PersonAvailable;
};

#endif
