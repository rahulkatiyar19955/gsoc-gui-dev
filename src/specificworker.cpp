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
#include <QFileDialog>
#include <QMessageBox>

/**
* \brief Default constructor
*/
SpecificWorker::SpecificWorker(MapPrx &mprx, bool startup_check) : GenericWorker(mprx)
{
	this->startup_check_flag = startup_check;
}

/**
* \brief Default destructor
*/
SpecificWorker::~SpecificWorker()
{
	std::cout << "Destroying SpecificWorker" << std::endl;
	emit t_compute_to_finalize();
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

	defaultMachine.start();

	return true;
}

void SpecificWorker::initialize(int period)
{
	std::cout << "Initialize worker" << std::endl;
	this->Period = period;
	if (this->startup_check_flag)
	{
		this->startup_check();
	}
	else
	{
		timer.start(Period);
		emit this->t_initialize_to_compute();
	}

	isFileOpened = false;

	connect(browseButton, SIGNAL(clicked()), this, SLOT(browseButtonClick()));
	connect(writeButton, SIGNAL(clicked()), this, SLOT(writeButtonClick()));
	tableWidget1->setColumnCount(8);
	tableWidget1->setHorizontalHeaderItem(0, new QTableWidgetItem("Time"));
	tableWidget1->setHorizontalHeaderItem(1, new QTableWidgetItem("X Pose"));
	tableWidget1->setHorizontalHeaderItem(2, new QTableWidgetItem("Z pose"));
	tableWidget1->setHorizontalHeaderItem(3, new QTableWidgetItem("RY Rot"));
	tableWidget1->setHorizontalHeaderItem(4, new QTableWidgetItem("Dist. Travelled"));
	tableWidget1->setHorizontalHeaderItem(5, new QTableWidgetItem("Target Info"));
	tableWidget1->setHorizontalHeaderItem(6, new QTableWidgetItem("Obst.(angle)"));
	tableWidget1->setHorizontalHeaderItem(7, new QTableWidgetItem("Obst.(dist.)"));
}
void SpecificWorker::writeButtonClick()
{
	QString fileNameSaved = QFileDialog::getSaveFileName(this,
														 tr("Save Nav Data"),
														 "",
														 tr("CSV File (*.csv);"));

	if (fileNameSaved.isEmpty())
		return;
	else
	{

		QFile file(fileNameSaved);

		if (!file.open(QIODevice::WriteOnly))
		{
			QMessageBox::information(this, tr("Unable to open file"),
									 file.errorString());
			return;
		}

		QTextStream out(&file);
		// out << "rahul";

		FILE *infile;
		NavData input;

		// Open person.dat for reading
		infile = fopen(fileName.toStdString().c_str(), "r");
		if (infile == NULL)
		{
			fprintf(stderr, "\nError opening file\n");
			return;
		}
		// read file contents till end of file
		try
		{

			while (fread(&input, sizeof(class NavData), 1, infile))
			{
				out << input.time_str << "," << input.robotposeX << "," << input.robotposeZ << "," << input.robotposeRY << ","
					<< input.dist_travelled << "," << input.target_achived << ","
					<< input.min_dist_obj.x() << "," << input.min_dist_obj.y() << "\n";
			}
		}
		catch (const std::exception &e)
		{
			std::cerr << e.what() << '\n';
		}

		// close file
		fclose(infile);
	}
}

void SpecificWorker::browseButtonClick()
{
	qDebug() << __FUNCTION__;
	fileName = QFileDialog::getOpenFileName(this,
											tr("Open Image"),
											"/home/jana",
											tr("Dat Files (*.dat)"));

	if (readNavData())
	{
		writeButton->setEnabled(true);
		isFileOpened = true;
	}
	else
	{
		writeButton->setEnabled(false);
		isFileOpened = false;
	}

	calculate_pathLength();
	calculate_pathSmoothness();
	drawChart();
}

bool SpecificWorker::readNavData()
{
	// tableWidget1->setColumnCount(8);
	qDebug() << __FUNCTION__;
	FILE *infile;
	NavData input;

	// Open person.dat for reading
	infile = fopen(fileName.toStdString().c_str(), "r");
	if (infile == NULL)
	{
		fprintf(stderr, "\nError opening file\n");
		fName->setText("Error opening file");
		return false;
	}
	fName->setText(fileName);
	// read file contents till end of file
	try
	{
		int row_count = 0;
		while (fread(&input, sizeof(class NavData), 1, infile))
		{

			tableWidget1->insertRow(tableWidget1->rowCount());
			QTableWidgetItem *newItem = new QTableWidgetItem(tr("%1").arg(input.time_str));
			tableWidget1->setItem(row_count, 0, newItem);

			QTableWidgetItem *newItem2 = new QTableWidgetItem(tr("%1").arg(input.robotposeX));
			tableWidget1->setItem(row_count, 1, newItem2);

			QTableWidgetItem *newItem3 = new QTableWidgetItem(tr("%1").arg(input.robotposeZ));
			tableWidget1->setItem(row_count, 2, newItem3);

			QTableWidgetItem *newItem4 = new QTableWidgetItem(tr("%1").arg(input.robotposeRY));
			tableWidget1->setItem(row_count, 3, newItem4);

			QTableWidgetItem *newItem5 = new QTableWidgetItem(tr("%1").arg(input.dist_travelled));
			tableWidget1->setItem(row_count, 4, newItem5);

			QTableWidgetItem *newItem6 = new QTableWidgetItem(tr("%1").arg(input.target_achived));
			tableWidget1->setItem(row_count, 5, newItem6);

			QTableWidgetItem *newItem7 = new QTableWidgetItem(tr("%1").arg(input.min_dist_obj.x()));
			tableWidget1->setItem(row_count, 6, newItem7);

			QTableWidgetItem *newItem8 = new QTableWidgetItem(tr("%1").arg(input.min_dist_obj.y()));
			tableWidget1->setItem(row_count, 7, newItem8);

			row_count++;
		}
	}
	catch (const std::exception &e)
	{
		std::cerr << e.what() << '\n';
		return false;
	}

	// close file
	fclose(infile);
	qDebug() << "exit";
	return true;
}
void SpecificWorker::calculate_pathLength()
{
	if (isFileOpened)
	{
		//tableWidget1->item (row,column)
		double startPointDistance = std::stod((tableWidget1->item(1, 4)->text()).toStdString());
		double endPointDistance = std::stod((tableWidget1->item(tableWidget1->rowCount() - 1, 4)->text()).toStdString());

		std::cout << "startPointDistance:" << startPointDistance << std::endl;
		std::cout << "endPointDistance:" << endPointDistance << std::endl;

		std::string distStr = std::to_string(endPointDistance - startPointDistance);
		std::cout << distStr << std::endl;

		QString distanceStr = QString::fromStdString(distStr);
		//plLabel->setText(distanceStr);
		plLabel->setText(tableWidget1->item(tableWidget1->rowCount() - 1, 4)->text());
	}
}
void SpecificWorker::calculate_pathSmoothness()
{
	// 3 index column contains yaw values
	// range of robotposeRY is 4.7 -> -1.57
	double cumm_angle = 0;
	int row_count = tableWidget1->rowCount();
	if (row_count < 2)
		return;

	for (int i = 0; i < row_count - 1; i++)
	{
		// converting the range into -pi <-> +pi  that is -3.14 <-> +3.14
		double temp_angle1 = std::stod((tableWidget1->item(i, 3)->text()).toStdString()) - 1.57;
		double temp_angle2 = std::stod((tableWidget1->item(i + 1, 3)->text()).toStdString()) - 1.57;
		double diff_angle = std::abs(temp_angle1 - temp_angle2);

		// taking the shortest angle measure
		if (diff_angle > 3.14)
			diff_angle = 6.28 - diff_angle;

		cumm_angle += diff_angle;
	}
	cumm_angle /= row_count;
	psLabel->setText(QString::fromStdString(std::to_string(cumm_angle)));
}

void SpecificWorker::drawChart()
{
}

void SpecificWorker::compute()
{
	//computeCODE
	//QMutexLocker locker(mutex);
	//try
	//{
	//  camera_proxy->getYImage(0,img, cState, bState);
	//  memcpy(image_gray.data, &img[0], m_width*m_height*sizeof(uchar));
	//  searchTags(image_gray);
	//}
	//catch(const Ice::Exception &e)
	//{
	//  std::cout << "Error reading from Camera" << e << std::endl;
	//}
}

int SpecificWorker::startup_check()
{
	std::cout << "Startup check" << std::endl;
	QTimer::singleShot(200, qApp, SLOT(quit()));
	return 0;
}

void SpecificWorker::sm_compute()
{
	// std::cout << "Entered state compute" << std::endl;
	compute();
}

void SpecificWorker::sm_initialize()
{
	std::cout << "Entered initial state initialize" << std::endl;
}

void SpecificWorker::sm_finalize()
{
	std::cout << "Entered final state finalize" << std::endl;
}
