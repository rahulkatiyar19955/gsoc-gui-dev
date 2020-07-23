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
#include "specificworker.h"

/**
* \brief Default constructor
*/
SpecificWorker::SpecificWorker(MapPrx& mprx, bool startup_check) : GenericWorker(mprx)
{
	active = false;
	worldModel = AGMModel::SPtr(new AGMModel());
	worldModel->name = "worldModel";
	this->startup_check_flag = startup_check;
}

/**
* \brief Default destructor
*/
SpecificWorker::~SpecificWorker()
{
	std::cout << "Destroying SpecificWorker" << std::endl;
}

bool SpecificWorker::setParams(RoboCompCommonBehavior::ParameterList params)
{
//	THE FOLLOWING IS JUST AN EXAMPLE
//	To use innerModelPath parameter you should uncomment specificmonitor.cpp readConfig method content
//	try
//	{
//		RoboCompCommonBehavior::Parameter par = params.at("InnerModelPath");
//		std::string innermodel_path = par.value;
//		innerModel = std::make_shared(innermodel_path);
//	}
//	catch(const std::exception &e) { qFatal("Error reading config params"); }



	innerModel = std::make_shared<InnerModel>(new InnerModel());
	try
	{
		RoboCompAGMWorldModel::World w = agmexecutive_proxy->getModel();
		AGMExecutiveTopic_structuralChange(w);
	}
	catch(...)
	{
		printf("The executive is probably not running, waiting for first AGM model publication...");
	}



	return true;
}

void SpecificWorker::initialize(int period)
{
	std::cout << "Initialize worker" << std::endl;
	this->Period = period;
	if(this->startup_check_flag)
	{
		this->startup_check();
	}
	else
	{
		timer.start(Period);
	}
    navStoreFile_obj = new NavStoreFile(omnirobot_proxy, laser_proxy);

}

void SpecificWorker::compute()
{




    RoboCompGenericBase::TBaseState newState;
    // retrieve model
    if (worldModel->getIdentifierByType("robot") < 0)
    {
        try
        {
            RoboCompAGMWorldModel::World w = agmexecutive_proxy->getModel();
            AGMExecutiveTopic_structuralChange(w);
        }
        catch(...)
        {
            printf("The executive is probably not running, waiting for first AGM model publication...");
        }
    }
    try
    {
        RoboCompGenericBase::TBaseState omniState;
        omnirobot_proxy->getBaseState(omniState);
        newState = omniState;
//        std::cout<<newState.isMoving<<" robotRY: "<<newState.alpha<<" count:"<<this->tempCount<<std::endl;
        if(!newState.isMoving && this->firstTime) {
            this->firstTime = false;
            std::cout<<navStoreFile_obj->initializeFile()<<std::endl;
        }
        else if (!newState.isMoving){
            navStoreFile_obj->insertNewEntry();
        }
        else if(!this->firstTime)
        {
            std::cout<<"closing file.."<<std::endl;
            this->navStoreFile_obj->closeFile();
            this->firstTime = true;
        }

//        if(this->firstTime)
//            this->tempCount=0;
//        if(this->tempCount>100)
//        {
//            std::cout<<"close file"<<std::endl;
//            navStoreFile_obj->closeFile();
//
//        }
//        else
//        {
//            if(!newState.isMoving && this->firstTime) {
//                this->firstTime = false;
//                navStoreFile_obj->initializeFile();
//            }
//            else if (!newState.isMoving){
//                navStoreFile_obj->insertNewEntry();
//            }
//        }
//        this->tempCount++;
    }
    catch (...)
    {
        printf("Can't connect to the robot!!\n");
    }


	
	
}

int SpecificWorker::startup_check()
{
	std::cout << "Startup check" << std::endl;
	QTimer::singleShot(200, qApp, SLOT(quit()));
	return 0;
}


bool SpecificWorker::AGMCommonBehavior_activateAgent(const RoboCompAGMCommonBehavior::ParameterMap &prs)
{
//implementCODE
	bool activated = false;
	if (setParametersAndPossibleActivation(prs, activated))
	{
		if (not activated)
		{
			return activate(p);
		}
	}
	else
	{
		return false;
	}
	return true;
}

bool SpecificWorker::AGMCommonBehavior_deactivateAgent()
{
//implementCODE
	return deactivate();
}

RoboCompAGMCommonBehavior::ParameterMap SpecificWorker::AGMCommonBehavior_getAgentParameters()
{
//implementCODE
	return params;
}

RoboCompAGMCommonBehavior::StateStruct SpecificWorker::AGMCommonBehavior_getAgentState()
{
//implementCODE
	RoboCompAGMCommonBehavior::StateStruct s;
	if (isActive())
	{
		s.state = RoboCompAGMCommonBehavior::StateEnum::Running;
	}
	else
	{
		s.state = RoboCompAGMCommonBehavior::StateEnum::Stopped;
	}
	s.info = p.action.name;
	return s;
}

void SpecificWorker::AGMCommonBehavior_killAgent()
{
//implementCODE

}

bool SpecificWorker::AGMCommonBehavior_reloadConfigAgent()
{
//implementCODE
	return true;
}

bool SpecificWorker::AGMCommonBehavior_setAgentParameters(const RoboCompAGMCommonBehavior::ParameterMap &prs)
{
//implementCODE
	bool activated = false;
	return setParametersAndPossibleActivation(prs, activated);
}

int SpecificWorker::AGMCommonBehavior_uptimeAgent()
{
//implementCODE
	return 0;
}

//SUBSCRIPTION to edgeUpdated method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_edgeUpdated(const RoboCompAGMWorldModel::Edge &modification)
{
//subscribesToCODE
	QMutexLocker locker(mutex);
	AGMModelConverter::includeIceModificationInInternalModel(modification, worldModel);
	AGMInner::updateImNodeFromEdge(worldModel, modification, innerModel.get());

}

//SUBSCRIPTION to edgesUpdated method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_edgesUpdated(const RoboCompAGMWorldModel::EdgeSequence &modifications)
{
//subscribesToCODE
	QMutexLocker lockIM(mutex);
	for (auto modification : modifications)
	{
		AGMModelConverter::includeIceModificationInInternalModel(modification, worldModel);
		AGMInner::updateImNodeFromEdge(worldModel, modification, innerModel.get());
	}

}

//SUBSCRIPTION to selfEdgeAdded method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_selfEdgeAdded(const int nodeid, const std::string &edgeType, const RoboCompAGMWorldModel::StringDictionary &attributes)
{
//subscribesToCODE
	QMutexLocker lockIM(mutex);
 	try { worldModel->addEdgeByIdentifiers(nodeid, nodeid, edgeType, attributes); } catch(...){ printf("Couldn't add an edge. Duplicate?\n"); }
 
	try { innerModel = std::make_shared<InnerModel>(AGMInner::extractInnerModel(worldModel)); } catch(...) { printf("Can't extract an InnerModel from the current model.\n"); }
}

//SUBSCRIPTION to selfEdgeDeleted method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_selfEdgeDeleted(const int nodeid, const std::string &edgeType)
{
//subscribesToCODE
	QMutexLocker lockIM(mutex);
 	try { worldModel->removeEdgeByIdentifiers(nodeid, nodeid, edgeType); } catch(...) { printf("Couldn't remove an edge\n"); }
 
	try { innerModel = std::make_shared<InnerModel>(AGMInner::extractInnerModel(worldModel)); } catch(...) { printf("Can't extract an InnerModel from the current model.\n"); }
}

//SUBSCRIPTION to structuralChange method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_structuralChange(const RoboCompAGMWorldModel::World &w)
{
//subscribesToCODE
	QMutexLocker lockIM(mutex);
 	AGMModelConverter::fromIceToInternal(w, worldModel);
 
	innerModel = std::make_shared<InnerModel>(AGMInner::extractInnerModel(worldModel));
}

//SUBSCRIPTION to symbolUpdated method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_symbolUpdated(const RoboCompAGMWorldModel::Node &modification)
{
//subscribesToCODE
	QMutexLocker locker(mutex);
	AGMModelConverter::includeIceModificationInInternalModel(modification, worldModel);

}

//SUBSCRIPTION to symbolsUpdated method from AGMExecutiveTopic interface
void SpecificWorker::AGMExecutiveTopic_symbolsUpdated(const RoboCompAGMWorldModel::NodeSequence &modifications)
{
//subscribesToCODE
	QMutexLocker l(mutex);
	for (auto modification : modifications)
		AGMModelConverter::includeIceModificationInInternalModel(modification, worldModel);

}



bool SpecificWorker::setParametersAndPossibleActivation(const RoboCompAGMCommonBehavior::ParameterMap &prs, bool &reactivated)
{
	printf("<<< setParametersAndPossibleActivation\n");
	// We didn't reactivate the component
	reactivated = false;

	// Update parameters
	params.clear();
	for (RoboCompAGMCommonBehavior::ParameterMap::const_iterator it=prs.begin(); it!=prs.end(); it++)
	{
		params[it->first] = it->second;
	}

	try
	{
		action = params["action"].value;
		std::transform(action.begin(), action.end(), action.begin(), ::tolower);
		//TYPE YOUR ACTION NAME
		if (action == "actionname")
		{
			active = true;
		}
		else
		{
			active = true;
		}
	}
	catch (...)
	{
		printf("exception in setParametersAndPossibleActivation %d\n", __LINE__);
		return false;
	}

	// Check if we should reactivate the component
	if (active)
	{
		active = true;
		reactivated = true;
	}

	printf("setParametersAndPossibleActivation >>>\n");

	return true;
}

void SpecificWorker::sendModificationProposal(AGMModel::SPtr &worldModel, AGMModel::SPtr &newModel)
{
	try
	{
		AGMMisc::publishModification(newModel, agmexecutive_proxy, "dataCaptureAgent");
	}
/*	catch(const RoboCompAGMExecutive::Locked &e)
	{
	}
	catch(const RoboCompAGMExecutive::OldModel &e)
	{
	}
	catch(const RoboCompAGMExecutive::InvalidChange &e)
	{
	}
*/
	catch(const Ice::Exception& e)
	{
		exit(1);
	}
}

/**************************************/
// From the RoboCompAGMExecutive you can call this methods:
// this->agmexecutive_proxy->activate(...)
// this->agmexecutive_proxy->addSelfEdge(...)
// this->agmexecutive_proxy->broadcastModel(...)
// this->agmexecutive_proxy->broadcastPlan(...)
// this->agmexecutive_proxy->deactivate(...)
// this->agmexecutive_proxy->delSelfEdge(...)
// this->agmexecutive_proxy->edgeUpdate(...)
// this->agmexecutive_proxy->edgesUpdate(...)
// this->agmexecutive_proxy->getData(...)
// this->agmexecutive_proxy->getEdge(...)
// this->agmexecutive_proxy->getModel(...)
// this->agmexecutive_proxy->getNode(...)
// this->agmexecutive_proxy->setMission(...)
// this->agmexecutive_proxy->structuralChangeProposal(...)
// this->agmexecutive_proxy->symbolUpdate(...)
// this->agmexecutive_proxy->symbolsUpdate(...)

/**************************************/
// From the RoboCompLaser you can call this methods:
// this->laser_proxy->getLaserAndBStateData(...)
// this->laser_proxy->getLaserConfData(...)
// this->laser_proxy->getLaserData(...)

/**************************************/
// From the RoboCompLaser you can use this types:
// RoboCompLaser::LaserConfData
// RoboCompLaser::TData

/**************************************/
// From the RoboCompOmniRobot you can call this methods:
// this->omnirobot_proxy->correctOdometer(...)
// this->omnirobot_proxy->getBasePose(...)
// this->omnirobot_proxy->getBaseState(...)
// this->omnirobot_proxy->resetOdometer(...)
// this->omnirobot_proxy->setOdometer(...)
// this->omnirobot_proxy->setOdometerPose(...)
// this->omnirobot_proxy->setSpeedBase(...)
// this->omnirobot_proxy->stopBase(...)

/**************************************/
// From the RoboCompOmniRobot you can use this types:
// RoboCompOmniRobot::TMechParams

/**************************************/
// From the RoboCompAGMCommonBehavior you can use this types:
// RoboCompAGMCommonBehavior::StateStruct
// RoboCompAGMCommonBehavior::Parameter

