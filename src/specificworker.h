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

#ifndef SPECIFICWORKER_H
#define SPECIFICWORKER_H

#include <genericworker.h>
#include <innermodel/innermodel.h>

struct NavData
{
	char time_str[20];
	float robotposeX;
	float robotposeZ;
	float robotposeRY;
	double dist_travelled;
	char target_achived[20];
	QPointF min_dist_obj; // for angle and distance
};

class SpecificWorker : public GenericWorker
{
	Q_OBJECT
public:
	SpecificWorker(MapPrx &mprx, bool startup_check);
	~SpecificWorker();
	bool setParams(RoboCompCommonBehavior::ParameterList params);
	void readNavData();

public slots:
	void
	compute();
	int startup_check();
	void initialize(int period);
	//Specification slot methods State Machine
	void sm_compute();
	void sm_initialize();
	void sm_finalize();
	void browseButtonClick();
	void writeButtonClick();

	//--------------------
private:
	std::shared_ptr<InnerModel>
		innerModel;
	bool startup_check_flag;
	QString fileName;
};

#endif
