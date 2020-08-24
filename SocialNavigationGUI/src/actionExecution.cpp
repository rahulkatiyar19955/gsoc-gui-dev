//
// Created by robolab on 22/07/20.
//


#include "actionExecution.h"


void ActionExecution::initialize(AGMModel::SPtr worldModel_)
{
    worldModel = worldModel_;
}

void ActionExecution::updateWordModel(AGMModel::SPtr worldModel_)
{
    worldModel = worldModel_;

}
void ActionExecution::update(std::string action_,  RoboCompAGMCommonBehavior::ParameterMap params_)
{
    action = action_;
    params = params_;
    newActionReceived = true;
}



//////////////////////////////////missions//////////////////////////////////////////

ActionExecution::retActions ActionExecution::runActions()
{
    qDebug() << "---------------------------------------------------";
    qDebug() <<__FUNCTION__ <<"Checking ACTION: " << QString::fromStdString(action);

    static std::string previousAction = "";

    retActions ret;
    bool newAction = (previousAction != action);

    if (newAction)
    {
        printf("prev:%s  new:%s\n", previousAction.c_str(), action.c_str());
        rDebug2(("action %s") % action.c_str() );
    }


    if (action == "changeroom")
    {
        ret = action_ChangeRoom();
    }

    if (action == "gotoperson")
    {
        ret = action_GoToPerson();
    }

    if (newAction)
    {
        previousAction = action;
        printf("New action: %s\n", action.c_str());
    }

    return ret;

}


ActionExecution::retActions ActionExecution::action_ChangeRoom()
{

    qDebug()<<"-------------------------------"<< __FUNCTION__<< "-------------------------------";
    AGMModelSymbol::SPtr roomSymbol;
    AGMModelSymbol::SPtr robotSymbol;

    bool needsReplanning = false;
    QPointF newTarget = QPointF();

    try
    {
        roomSymbol = worldModel->getSymbolByIdentifier(std::stoi(params["room2"].value));
        robotSymbol = worldModel->getSymbolByIdentifier(std::stoi(params["robot"].value));
    }
    catch( const Ice::Exception& ex)
    {
        std::cout << "Exception:: Error reading room and robot symbols" << ex << endl;
    }


    int32_t destRoomID = roomSymbol->identifier;
    printf("Quiero llegar a : %d\n",  destRoomID);
    std::string imName =roomSymbol->getAttribute("imName");
//    printf("imName: <%s>\n", imName.c_str());

    int32_t currentRoom = -1;

    try
    {

        for (AGMModelSymbol::iterator edge = robotSymbol->edgesBegin(worldModel);
             edge!=robotSymbol->edgesEnd(worldModel);
             edge++) {
            if (edge->getLabel()=="in") {
                const std::pair<int32_t, int32_t> symbolPair = edge->getSymbolPair();
                auto second = worldModel->getSymbol(symbolPair.second);
                if (second->typeString() == "room")
                {
                    qDebug() << "El robot está en : " << second->identifier;
                    currentRoom = second->identifier;
                }
            }
        }

    }

    catch( const Ice::Exception& ex)
    {
        std::cout << "Exception:: Cant get edge between robot and room:" << ex << endl;
    }

    if (currentRoom == -1)
    {
        qDebug()<< "shit";
        exit(-1);
    }

    if (currentRoom == destRoomID)
    {
        needsReplanning = false;
    }

    else if (newActionReceived)
    {
        auto roomPolygon = getRoomPolyline(roomSymbol);
        newTarget = roomPolygon.boundingRect().center();

        newActionReceived = false;
        needsReplanning = true;

    }

    qDebug()<<  __FUNCTION__ << "Returning "<< needsReplanning << newTarget;
    return std::make_tuple(needsReplanning, newTarget);
};



ActionExecution::retActions ActionExecution::action_GoToPerson()
{
    qDebug()<<"-------------------------------"<< __FUNCTION__<< "-------------------------------";
    AGMModelSymbol::SPtr personSymbol;
    AGMModelSymbol::SPtr robotSymbol;

    bool needsReplanning = false;
    QPointF newTarget = QPointF();

    try
    {
        personSymbol = worldModel->getSymbolByIdentifier(std::stoi(params["p"].value));
        robotSymbol = worldModel->getSymbolByIdentifier(std::stoi(params["robot"].value));
    }
    catch( const Ice::Exception& ex)
    {
        std::cout << "Exception:: Error reading room and robot symbols" << ex << endl;
    }



    return std::make_tuple(needsReplanning, newTarget);


}




QPolygonF ActionExecution::getRoomPolyline(AGMModelSymbol::SPtr roomSymbol)
{
    qDebug() << __FUNCTION__;


    QPolygonF polygon;

    try {
        auto polyline = QString::fromStdString(roomSymbol->getAttribute("polyline"));

        for (auto pxz : polyline.split(";"))
        {
            auto p = pxz.split(" ");

            if (p.size() != 2)
                continue;

            auto x = std::stof(p[0].toStdString());
            auto z = std::stof(p[1].toStdString());

            polygon << QPointF(x,z);
        }

        return polygon;

    }

    catch (std::exception& e) {
        std::cout << "Exception reading room "<< roomSymbol->identifier << " polyline: " << e.what() << std::endl;
    }

}
