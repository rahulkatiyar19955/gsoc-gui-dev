#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2020 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#
import PySide2
from genericworker import *

try:
    from ui_activity_form import *
except:
    print("Can't import UI file. Did you run 'make'?")


# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel


class OpenActivityForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_activityForm()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.pushButton.clicked.connect(self.button_ok)
        self.ui.pushButton_2.clicked.connect(self.button_cancel)
        self.ui.comboBox_4.currentIndexChanged.connect(self.type_check)
        self.ui.comboBox_5.activated.connect(self.location_check)
        self.ui.textEdit_3.setText("Activity " + str(self.parent.ui.comboBox_3.count()+1))
        self.ui.comboBox_6.addItems({"Stretcher", "Robot"})

    # save the data when ok button is pressed
    def button_ok(self):
        print("ok button")
        self.parent.ui.comboBox_3.addItem(self.ui.textEdit_3.toPlainText())
        self.hide()

    # exit the form and discard all the data
    def button_cancel(self):
        self.hide()

    # check the type of the activity
    def type_check(self, index):
        if self.ui.comboBox_4.itemText(index) == "Individual":
            self.ui.label_9.show()
            self.ui.textEdit.show()
        else:
            self.ui.label_9.hide()
            self.ui.textEdit.hide()

    # check the location
    def location_check(self, index):
        if self.ui.comboBox_5.itemText(index) == "Physical therapy room":
            self.ui.comboBox_6.clear()
            self.ui.comboBox_6.addItems({"Stretcher", "Robot"})
        else:
            self.ui.comboBox_6.clear()
            self.ui.comboBox_6.addItems({"Table", "Robot", "TV"})


class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map):
        super(SpecificWorker, self).__init__(proxy_map)
        self.timer.timeout.connect(self.compute)
        self.Period = 2000
        self.timer.start(self.Period)
        self.ui.pushButton_10.clicked.connect(self.newActivity)

        # self.ui2 = Ui_activityForm()
        # self.ui2.setupUi(self)

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):
        # try:
        #	self.innermodel = InnerModel(params["InnerModelPath"])
        # except:
        #	traceback.print_exc()
        #	print("Error reading config params")
        return True

    @QtCore.Slot()
    def compute(self):
        print('SpecificWorker.compute...')
        # computeCODE
        # try:
        #   self.differentialrobot_proxy.setSpeedBase(100, 0)
        # except Ice.Exception as e:
        #   traceback.print_exc()
        #   print(e)

        # The API of python-innermodel is not exactly the same as the C++ version
        # self.innermodel.updateTransformValues('head_rot_tilt_pose', 0, 0, 0, 1.3, 0, 0)
        # z = librobocomp_qmat.QVec(3,0)
        # r = self.innermodel.transform('rgbd', z, 'laser')
        # r.printvector('d')
        # print(r[0], r[1], r[2])

        return True

    #
    # SUBSCRIPTION to edgeUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_edgeUpdated(self, modification):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to edgesUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_edgesUpdated(self, modifications):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to selfEdgeAdded method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeAdded(self, nodeid, edgeType, attributes):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to selfEdgeDeleted method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeDeleted(self, nodeid, edgeType):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to structuralChange method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_structuralChange(self, w):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to symbolUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolUpdated(self, modification):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to symbolsUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolsUpdated(self, modifications):
        #
        # subscribesToCODE
        #
        pass

    # =============== Methods for Component Implements ==================
    # ===================================================================

    #
    # activateAgent
    #
    def AGMCommonBehavior_activateAgent(self, prs):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # deactivateAgent
    #
    def AGMCommonBehavior_deactivateAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # getAgentParameters
    #
    def AGMCommonBehavior_getAgentParameters(self):
        ret = ParameterMap()
        #
        # implementCODE
        #
        return ret

    #
    # getAgentState
    #
    def AGMCommonBehavior_getAgentState(self):
        ret = StateStruct()
        #
        # implementCODE
        #
        return ret

    #
    # killAgent
    #
    def AGMCommonBehavior_killAgent(self):
        #
        # implementCODE
        #
        pass

    #
    # reloadConfigAgent
    #
    def AGMCommonBehavior_reloadConfigAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # setAgentParameters
    #
    def AGMCommonBehavior_setAgentParameters(self, prs):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # uptimeAgent
    #
    def AGMCommonBehavior_uptimeAgent(self):
        ret = int()
        #
        # implementCODE
        #
        return ret

    # ===================================================================
    # ===================================================================

    # ======functions for ui=============
    def newActivity(self):
        print("button Clicked2")
        self.activityForm = OpenActivityForm(self)
        self.activityForm.show()
