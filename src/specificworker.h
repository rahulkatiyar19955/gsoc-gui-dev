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
#include <QVector2D>

class NavData
{
public:
    char time_str[20];
    float robotposeX;
    float robotposeZ;
    float robotposeRY;
    double dist_travelled;
    char target_achieved[20];
    QPointF min_dist_obj;

//    bool operator== (const NavData &n1)
//    {
//        return (this->time_str==n1.time_str);
////        return true;
//    }
};

class NavStoreFile
{
private:
    FILE *outfile;
    vector<NavData> navdata;
    std::time_t t;
    std::tm *now;
    bool isFileOpened;
    QVec currentRobotPose;
    RoboCompOmniRobot::OmniRobotPrx omnirobot_proxy_clone;
    RoboCompLaser::LaserPrx laser_proxy_clone;
public:

    NavStoreFile(RoboCompOmniRobot::OmniRobotPrx omnirobot_proxy_, RoboCompLaser::LaserPrx laser_proxy_)
    {
        this->isFileOpened = false;
        this->omnirobot_proxy_clone = omnirobot_proxy_;
        this->laser_proxy_clone = laser_proxy_;

    }

    std::string initializeFile()
    {
        t = std::time(0);
        now = std::localtime(&t);
        std::string timeStr = "navData_" + std::to_string(now->tm_year + 1900) +
                              std::to_string(now->tm_mon + 1) + std::to_string(now->tm_mday) + std::to_string(now->tm_hour) +
                              std::to_string(now->tm_min) + std::to_string(now->tm_sec) + ".dat";

        outfile = fopen(timeStr.c_str(), "w");
        if (outfile == NULL)
        {
            isFileOpened = false;
            return "File Not Opened";
        }
        isFileOpened = true;
        return "File Created Successfully \n" + timeStr;
    }
    void closeFile()
    {
        if(!this->isFileOpened)
            return;
        for (auto data : this->navdata)
        {
            fwrite(&data, sizeof(class NavData), 1, this->outfile);
        }
        this->navdata.clear();

        isFileOpened = false;
        fclose(outfile);
    }
    void insertNewEntry()
    {
        NavData tempData;
        RoboCompGenericBase::TBaseState omniState;
        this->omnirobot_proxy_clone->getBaseState(omniState);
        strcpy(tempData.time_str,"none");
        tempData.robotposeX = omniState.x;
        tempData.robotposeZ = omniState.z;
        tempData.robotposeRY = omniState.correctedAlpha;
        tempData.dist_travelled = this->calc_dist_travelled(QPointF(omniState.x,omniState.z));
        strcpy(tempData.target_achieved,"inProgress");
        tempData.min_dist_obj = this->laserMinData();
        this->navdata.push_back(tempData);

    }

    bool checkDuplicate(const NavData &n1)
    {
        int lastIndex = this->navdata.size();
        NavData n2 = this->navdata[lastIndex-1];
        return (n1.time_str==n2.time_str &&
                n1.min_dist_obj==n2.min_dist_obj &&
                n1.robotposeX == n2.robotposeX &&
                n1.robotposeZ == n2.robotposeZ &&
                n1.robotposeRY == n2.robotposeRY &&
                n1.dist_travelled == n2.dist_travelled
                );
    }

    double calc_dist_travelled(QPointF p2)
    {
        int lastIndex = this->navdata.size();
        if(lastIndex>0)
        {
            // last point in the vector
            QPointF currRPose = QPointF(this->navdata[lastIndex-1].robotposeX, this->navdata[lastIndex-1].robotposeZ);

            // distance from last point to the current point
            float euc_dist_to_target = std::fabs(QVector2D(currRPose - p2).length());

            // returning the cummulative distance
            return (this->navdata[lastIndex-1].dist_travelled + euc_dist_to_target);
        }
        else{
            return 0.00;
        }

    }
    QPointF laserMinData()
    {
        RoboCompLaser::TLaserData laserData;
        laserData = this->laser_proxy_clone->getLaserData();
        float min = std::numeric_limits<float>::max();
        float angle_ = 0;
        for (auto lData : laserData)
        {
            if (lData.dist < min)
            {
                min = lData.dist;
                angle_ = lData.angle;
            }
        }
        return QPointF(angle_, min);
//        return QPointF(0.00,1.23);
    }
};

class SpecificWorker : public GenericWorker
{
Q_OBJECT
public:
	SpecificWorker(MapPrx& mprx, bool startup_check);
	~SpecificWorker();
	bool setParams(RoboCompCommonBehavior::ParameterList params);

	bool AGMCommonBehavior_activateAgent(const RoboCompAGMCommonBehavior::ParameterMap &prs);
	bool AGMCommonBehavior_deactivateAgent();
	RoboCompAGMCommonBehavior::ParameterMap AGMCommonBehavior_getAgentParameters();
	RoboCompAGMCommonBehavior::StateStruct AGMCommonBehavior_getAgentState();
	void AGMCommonBehavior_killAgent();
	bool AGMCommonBehavior_reloadConfigAgent();
	bool AGMCommonBehavior_setAgentParameters(const RoboCompAGMCommonBehavior::ParameterMap &prs);
	int AGMCommonBehavior_uptimeAgent();

	void AGMExecutiveTopic_edgeUpdated(const RoboCompAGMWorldModel::Edge &modification);
	void AGMExecutiveTopic_edgesUpdated(const RoboCompAGMWorldModel::EdgeSequence &modifications);
	void AGMExecutiveTopic_selfEdgeAdded(const int nodeid, const std::string &edgeType, const RoboCompAGMWorldModel::StringDictionary &attributes);
	void AGMExecutiveTopic_selfEdgeDeleted(const int nodeid, const std::string &edgeType);
	void AGMExecutiveTopic_structuralChange(const RoboCompAGMWorldModel::World &w);
	void AGMExecutiveTopic_symbolUpdated(const RoboCompAGMWorldModel::Node &modification);
	void AGMExecutiveTopic_symbolsUpdated(const RoboCompAGMWorldModel::NodeSequence &modifications);

public slots:
	void compute();
	int startup_check();
	void initialize(int period);
private:
	std::shared_ptr<InnerModel> innerModel;
	std::string action;
	RoboCompAGMCommonBehavior::ParameterMap params;
	AGMModel::SPtr worldModel;
	bool active;
	bool setParametersAndPossibleActivation(const RoboCompAGMCommonBehavior::ParameterMap &prs, bool &reactivated);
	void sendModificationProposal(AGMModel::SPtr &worldModel, AGMModel::SPtr &newModel);
	bool startup_check_flag;
	bool firstTime = true;
    NavStoreFile *navStoreFile_obj;
    int tempCount=0;

};

#endif
