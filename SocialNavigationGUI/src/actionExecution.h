//
// Created by robolab on 22/07/20.
//

#ifndef ACTIONEXECUTION_H
#define ACTIONEXECUTION_H
#include <genericworker.h>

class ActionExecution {

public:
    using retActions = std::tuple <bool,QPointF>;

    void initialize(AGMModel::SPtr worldModel_);
    void updateWordModel(AGMModel::SPtr worldModel_);
    void update(std::string action_,  RoboCompAGMCommonBehavior::ParameterMap params_);
    ActionExecution::retActions runActions();


private:
    AGMModel::SPtr worldModel;
    std::string action;
    RoboCompAGMCommonBehavior::ParameterMap params;
    bool newActionReceived = false;

    ActionExecution::retActions action_ChangeRoom();
    ActionExecution::retActions action_GoToPerson();
    QPolygonF getRoomPolyline(AGMModelSymbol::SPtr roomSymbol);


};

#endif //ACTIONEXECUTION_H
