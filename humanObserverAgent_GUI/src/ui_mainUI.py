# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import mainUIDate_rc

class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(888, 654)
        self.roboNavControl = QGroupBox(guiDlg)
        self.roboNavControl.setObjectName(u"roboNavControl")
        self.roboNavControl.setGeometry(QRect(12, 160, 575, 185))
        self.label_11 = QLabel(self.roboNavControl)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(214, 51, 16, 17))
        self.label_12 = QLabel(self.roboNavControl)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(183, 113, 55, 17))
        self.label_13 = QLabel(self.roboNavControl)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 51, 53, 17))
        self.label_16 = QLabel(self.roboNavControl)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(214, 28, 38, 17))
        self.pushButton_4 = QPushButton(self.roboNavControl)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 97, 82, 25))
        self.label_17 = QLabel(self.roboNavControl)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(370, 28, 76, 17))
        self.progressBar = QProgressBar(self.roboNavControl)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(458, 51, 95, 25))
        self.progressBar.setValue(24)
        self.pushButton_5 = QPushButton(self.roboNavControl)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(458, 97, 89, 25))
        self.label_15 = QLabel(self.roboNavControl)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(214, 82, 16, 17))
        self.viewLaser_button = QPushButton(self.roboNavControl)
        self.viewLaser_button.setObjectName(u"viewLaser_button")
        self.viewLaser_button.setGeometry(QRect(370, 144, 82, 25))
        self.view_camera_button = QPushButton(self.roboNavControl)
        self.view_camera_button.setObjectName(u"view_camera_button")
        self.view_camera_button.setGeometry(QRect(458, 144, 98, 25))
        self.lineEdit = QLineEdit(self.roboNavControl)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(244, 51, 95, 25))
        self.lineEdit_2 = QLineEdit(self.roboNavControl)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(244, 82, 95, 25))
        self.lineEdit_3 = QLineEdit(self.roboNavControl)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(244, 113, 95, 25))
        self.pushButton_8 = QPushButton(self.roboNavControl)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(244, 144, 80, 25))
        self.pushButton_9 = QPushButton(self.roboNavControl)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(12, 148, 155, 25))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(239, 41, 41);")
        self.layoutWidget = QWidget(self.roboNavControl)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(14, 51, 155, 93))
        self.keycontrols = QGridLayout(self.layoutWidget)
        self.keycontrols.setObjectName(u"keycontrols")
        self.keycontrols.setContentsMargins(0, 0, 0, 0)
        self.up_button = QPushButton(self.layoutWidget)
        self.up_button.setObjectName(u"up_button")
        icon = QIcon()
        icon.addFile(u":/backImages/icons/up.png", QSize(), QIcon.Normal, QIcon.On)
        self.up_button.setIcon(icon)

        self.keycontrols.addWidget(self.up_button, 0, 1, 1, 1)

        self.left_button = QPushButton(self.layoutWidget)
        self.left_button.setObjectName(u"left_button")
        icon1 = QIcon()
        icon1.addFile(u":/backImages/icons/left.png", QSize(), QIcon.Normal, QIcon.On)
        self.left_button.setIcon(icon1)

        self.keycontrols.addWidget(self.left_button, 1, 0, 1, 1)

        self.stop_button = QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        icon2 = QIcon()
        icon2.addFile(u":/backImages/icons/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.stop_button.setIcon(icon2)

        self.keycontrols.addWidget(self.stop_button, 1, 1, 1, 1)

        self.right_button = QPushButton(self.layoutWidget)
        self.right_button.setObjectName(u"right_button")
        icon3 = QIcon()
        icon3.addFile(u":/backImages/icons/right.png", QSize(), QIcon.Normal, QIcon.On)
        self.right_button.setIcon(icon3)

        self.keycontrols.addWidget(self.right_button, 1, 2, 1, 1)

        self.down_button = QPushButton(self.layoutWidget)
        self.down_button.setObjectName(u"down_button")
        icon4 = QIcon()
        icon4.addFile(u":/backImages/icons/down.png", QSize(), QIcon.Normal, QIcon.On)
        self.down_button.setIcon(icon4)

        self.keycontrols.addWidget(self.down_button, 2, 1, 1, 1)

        self.c_button = QPushButton(self.layoutWidget)
        self.c_button.setObjectName(u"c_button")
        icon5 = QIcon()
        icon5.addFile(u":/backImages/icons/C.png", QSize(), QIcon.Normal, QIcon.On)
        self.c_button.setIcon(icon5)

        self.keycontrols.addWidget(self.c_button, 0, 2, 1, 1)

        self.cc_button = QPushButton(self.layoutWidget)
        self.cc_button.setObjectName(u"cc_button")
        icon6 = QIcon()
        icon6.addFile(u":/backImages/icons/CC.png", QSize(), QIcon.Normal, QIcon.On)
        self.cc_button.setIcon(icon6)

        self.keycontrols.addWidget(self.cc_button, 0, 0, 1, 1)

        self.line_7 = QFrame(guiDlg)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 138, 921, 21))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.humanObsAgent = QGroupBox(guiDlg)
        self.humanObsAgent.setObjectName(u"humanObsAgent")
        self.humanObsAgent.setEnabled(True)
        self.humanObsAgent.setGeometry(QRect(14, 354, 819, 281))
        self.layoutWidget1 = QWidget(self.humanObsAgent)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 28, 231, 243))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.photo_viewer = QGraphicsView(self.layoutWidget1)
        self.photo_viewer.setObjectName(u"photo_viewer")
        self.photo_viewer.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.photo_viewer)

        self.addPhotoB = QPushButton(self.layoutWidget1)
        self.addPhotoB.setObjectName(u"addPhotoB")

        self.verticalLayout_4.addWidget(self.addPhotoB)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.id_list = QComboBox(self.layoutWidget1)
        self.id_list.setObjectName(u"id_list")

        self.horizontalLayout_2.addWidget(self.id_list)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newHuman_button = QPushButton(self.layoutWidget1)
        self.newHuman_button.setObjectName(u"newHuman_button")

        self.horizontalLayout_3.addWidget(self.newHuman_button)

        self.setHuman_button = QPushButton(self.layoutWidget1)
        self.setHuman_button.setObjectName(u"setHuman_button")

        self.horizontalLayout_3.addWidget(self.setHuman_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(self.humanObsAgent)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(264, 28, 139, 17))
        self.layoutWidget_2 = QWidget(self.humanObsAgent)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(590, 52, 195, 133))
        self.formLayout = QFormLayout(self.layoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.x_sb = QSpinBox(self.layoutWidget_2)
        self.x_sb.setObjectName(u"x_sb")
        self.x_sb.setMinimum(-10000)
        self.x_sb.setMaximum(10000)
        self.x_sb.setSingleStep(100)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_sb)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.z_sb = QSpinBox(self.layoutWidget_2)
        self.z_sb.setObjectName(u"z_sb")
        self.z_sb.setMinimum(-10000)
        self.z_sb.setMaximum(10000)
        self.z_sb.setSingleStep(100)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.z_sb)

        self.label_20 = QLabel(self.layoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.rot_sb = QDoubleSpinBox(self.layoutWidget_2)
        self.rot_sb.setObjectName(u"rot_sb")
        self.rot_sb.setMinimum(-3.140000000000000)
        self.rot_sb.setMaximum(3.140000000000000)
        self.rot_sb.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rot_sb)

        self.setPose_pb = QPushButton(self.layoutWidget_2)
        self.setPose_pb.setObjectName(u"setPose_pb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.setPose_pb)

        self.label_21 = QLabel(self.humanObsAgent)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(590, 30, 45, 17))
        self.layoutWidget2 = QWidget(self.humanObsAgent)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(262, 50, 311, 221))
        self.formLayout_2 = QFormLayout(self.layoutWidget2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.H_name = QLineEdit(self.layoutWidget2)
        self.H_name.setObjectName(u"H_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.H_name)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.H_age = QComboBox(self.layoutWidget2)
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.setObjectName(u"H_age")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.H_age)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.H_userType = QComboBox(self.layoutWidget2)
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.setObjectName(u"H_userType")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.H_userType)

        self.label_18 = QLabel(self.layoutWidget2)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_18)

        self.H_phyDep = QSpinBox(self.layoutWidget2)
        self.H_phyDep.setObjectName(u"H_phyDep")
        self.H_phyDep.setMaximum(100)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.H_phyDep)

        self.label_19 = QLabel(self.layoutWidget2)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_19)

        self.H_cogDep = QSpinBox(self.layoutWidget2)
        self.H_cogDep.setObjectName(u"H_cogDep")
        self.H_cogDep.setMaximum(100)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.H_cogDep)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.H_emoSate = QComboBox(self.layoutWidget2)
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.setObjectName(u"H_emoSate")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.H_emoSate)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_10)

        self.H_activity = QComboBox(self.layoutWidget2)
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.setObjectName(u"H_activity")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.H_activity)

        self.sendtoDSR_button = QPushButton(self.humanObsAgent)
        self.sendtoDSR_button.setObjectName(u"sendtoDSR_button")
        self.sendtoDSR_button.setGeometry(QRect(588, 192, 195, 73))
        self.CalendarEvents = QGroupBox(guiDlg)
        self.CalendarEvents.setObjectName(u"CalendarEvents")
        self.CalendarEvents.setGeometry(QRect(2, 4, 581, 131))
        self.layoutWidget3 = QWidget(self.CalendarEvents)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(292, 22, 237, 93))
        self.setnewactivity = QGridLayout(self.layoutWidget3)
        self.setnewactivity.setObjectName(u"setnewactivity")
        self.setnewactivity.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.layoutWidget3)
        self.label_24.setObjectName(u"label_24")

        self.setnewactivity.addWidget(self.label_24, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.layoutWidget3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.setnewactivity.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.setnewactivity.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.layoutWidget3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.setnewactivity.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.setnewactivity.addWidget(self.comboBox_3, 1, 0, 1, 3)

        self.layoutWidget4 = QWidget(self.CalendarEvents)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(2, 22, 239, 93))
        self.viewagenda = QGridLayout(self.layoutWidget4)
        self.viewagenda.setObjectName(u"viewagenda")
        self.viewagenda.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget4)
        self.label_9.setObjectName(u"label_9")

        self.viewagenda.addWidget(self.label_9, 0, 1, 1, 2)

        self.label_22 = QLabel(self.layoutWidget4)
        self.label_22.setObjectName(u"label_22")

        self.viewagenda.addWidget(self.label_22, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.layoutWidget4)
        self.dateEdit.setObjectName(u"dateEdit")

        self.viewagenda.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.layoutWidget4)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.viewagenda.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.ImhNone)

        self.viewagenda.addWidget(self.label, 2, 1, 1, 2)

        self.line_5 = QFrame(self.CalendarEvents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(260, 20, 20, 109))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(guiDlg)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 338, 921, 21))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"humanObserverAgent_GUI", None))
        self.roboNavControl.setTitle(QCoreApplication.translate("guiDlg", u"Robot navigation and control", None))
        self.label_11.setText(QCoreApplication.translate("guiDlg", u"x", None))
        self.label_12.setText(QCoreApplication.translate("guiDlg", u"heading", None))
        self.label_13.setText(QCoreApplication.translate("guiDlg", u"Battery", None))
        self.label_16.setText(QCoreApplication.translate("guiDlg", u"Go to", None))
        self.pushButton_4.setText(QCoreApplication.translate("guiDlg", u"Stop robot", None))
        self.label_17.setText(QCoreApplication.translate("guiDlg", u"Monitoring", None))
        self.pushButton_5.setText(QCoreApplication.translate("guiDlg", u"Reset robot", None))
        self.label_15.setText(QCoreApplication.translate("guiDlg", u"z", None))
        self.viewLaser_button.setText(QCoreApplication.translate("guiDlg", u"View Laser", None))
        self.view_camera_button.setText(QCoreApplication.translate("guiDlg", u"View Camera", None))
        self.lineEdit.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.lineEdit_3.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("guiDlg", u"GO", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("guiDlg", u"<html><head/><body><p>w -&gt; forward </p><p>s -&gt; backward </p><p>a -&gt; left </p><p>d -&gt; right </p><p>f -&gt; CClockwise </p><p>g -&gt; clockwise </p><p>backspace -&gt; stop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText(QCoreApplication.translate("guiDlg", u"Keyboard Control Off", None))
        self.up_button.setText("")
        self.left_button.setText("")
        self.stop_button.setText("")
        self.right_button.setText("")
        self.down_button.setText("")
        self.c_button.setText("")
        self.cc_button.setText("")
        self.humanObsAgent.setTitle(QCoreApplication.translate("guiDlg", u"Human observer agent", None))
        self.addPhotoB.setText(QCoreApplication.translate("guiDlg", u"Add Photo", None))
        self.label_14.setText(QCoreApplication.translate("guiDlg", u"Id", None))
        self.newHuman_button.setText(QCoreApplication.translate("guiDlg", u"New human", None))
        self.setHuman_button.setText(QCoreApplication.translate("guiDlg", u"Set human", None))
        self.label_4.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600;\">Human information</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("guiDlg", u"Position X", None))
#if QT_CONFIG(tooltip)
        self.x_sb.setToolTip(QCoreApplication.translate("guiDlg", u"mm", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("guiDlg", u"Position Z", None))
#if QT_CONFIG(tooltip)
        self.z_sb.setToolTip(QCoreApplication.translate("guiDlg", u"mm", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("guiDlg", u"Rotation", None))
        self.setPose_pb.setText(QCoreApplication.translate("guiDlg", u"Set pose", None))
        self.label_21.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600;\">Pose</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("guiDlg", u"Name", None))
        self.H_name.setText("")
        self.label_6.setText(QCoreApplication.translate("guiDlg", u"Age", None))
        self.H_age.setItemText(0, QCoreApplication.translate("guiDlg", u"Age<30", None))
        self.H_age.setItemText(1, QCoreApplication.translate("guiDlg", u"30<Age<60", None))
        self.H_age.setItemText(2, QCoreApplication.translate("guiDlg", u"60<Age<80", None))
        self.H_age.setItemText(3, QCoreApplication.translate("guiDlg", u"Age>80", None))

        self.label_7.setText(QCoreApplication.translate("guiDlg", u"UserType", None))
        self.H_userType.setItemText(0, QCoreApplication.translate("guiDlg", u"Clinician", None))
        self.H_userType.setItemText(1, QCoreApplication.translate("guiDlg", u"Caregiver", None))
        self.H_userType.setItemText(2, QCoreApplication.translate("guiDlg", u"Family Member", None))
        self.H_userType.setItemText(3, QCoreApplication.translate("guiDlg", u"Caregiving User", None))

        self.label_18.setText(QCoreApplication.translate("guiDlg", u"PhysicalDependence", None))
        self.label_19.setText(QCoreApplication.translate("guiDlg", u"CognitiveDependence", None))
        self.label_8.setText(QCoreApplication.translate("guiDlg", u"Emotional State", None))
        self.H_emoSate.setItemText(0, QCoreApplication.translate("guiDlg", u"Neutral", None))
        self.H_emoSate.setItemText(1, QCoreApplication.translate("guiDlg", u"Angry", None))
        self.H_emoSate.setItemText(2, QCoreApplication.translate("guiDlg", u"Sad", None))
        self.H_emoSate.setItemText(3, QCoreApplication.translate("guiDlg", u"Happy", None))
        self.H_emoSate.setItemText(4, QCoreApplication.translate("guiDlg", u"Afraid", None))

        self.label_10.setText(QCoreApplication.translate("guiDlg", u"Activity", None))
        self.H_activity.setItemText(0, QCoreApplication.translate("guiDlg", u"Rest", None))
        self.H_activity.setItemText(1, QCoreApplication.translate("guiDlg", u"Robot Attention", None))
        self.H_activity.setItemText(2, QCoreApplication.translate("guiDlg", u"Physical Activity", None))
        self.H_activity.setItemText(3, QCoreApplication.translate("guiDlg", u"Cognitive Activity", None))

        self.sendtoDSR_button.setText(QCoreApplication.translate("guiDlg", u"Send to DSR", None))
        self.CalendarEvents.setTitle(QCoreApplication.translate("guiDlg", u"Activity Calendar", None))
        self.label_24.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Activity agenda</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("guiDlg", u"New activity", None))
        self.pushButton_11.setText(QCoreApplication.translate("guiDlg", u"Set activity", None))
        self.label_9.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Date</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><img src=\":/GUI/Icons/calendar.png\" /></p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("guiDlg", u"View agenda", None))
        self.label.setText("")
    # retranslateUi

