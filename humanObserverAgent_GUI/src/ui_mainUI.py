# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import mainUIDate_rc

class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if not guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(1024, 665)
        self.listen_status = QLabel(guiDlg)
        self.listen_status.setObjectName(u"listen_status")
        self.listen_status.setGeometry(QRect(762, 515, 16, 16))
        self.gridLayout_10 = QGridLayout(guiDlg)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.roboNavControl = QGroupBox(guiDlg)
        self.roboNavControl.setObjectName(u"roboNavControl")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roboNavControl.sizePolicy().hasHeightForWidth())
        self.roboNavControl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.roboNavControl.setFont(font)
        self.gridLayout_5 = QGridLayout(self.roboNavControl)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_16 = QLabel(self.roboNavControl)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_17 = QLabel(self.roboNavControl)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 4, 1, 1)

        self.keycontrols = QGridLayout()
        self.keycontrols.setObjectName(u"keycontrols")
        self.up_button = QPushButton(self.roboNavControl)
        self.up_button.setObjectName(u"up_button")
        icon = QIcon()
        icon.addFile(u":/backImages/icons/up.png", QSize(), QIcon.Normal, QIcon.On)
        self.up_button.setIcon(icon)

        self.keycontrols.addWidget(self.up_button, 0, 1, 1, 1)

        self.left_button = QPushButton(self.roboNavControl)
        self.left_button.setObjectName(u"left_button")
        icon1 = QIcon()
        icon1.addFile(u":/backImages/icons/left.png", QSize(), QIcon.Normal, QIcon.On)
        self.left_button.setIcon(icon1)

        self.keycontrols.addWidget(self.left_button, 1, 0, 1, 1)

        self.stop_button = QPushButton(self.roboNavControl)
        self.stop_button.setObjectName(u"stop_button")
        icon2 = QIcon()
        icon2.addFile(u":/backImages/icons/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.stop_button.setIcon(icon2)

        self.keycontrols.addWidget(self.stop_button, 1, 1, 1, 1)

        self.right_button = QPushButton(self.roboNavControl)
        self.right_button.setObjectName(u"right_button")
        icon3 = QIcon()
        icon3.addFile(u":/backImages/icons/right.png", QSize(), QIcon.Normal, QIcon.On)
        self.right_button.setIcon(icon3)

        self.keycontrols.addWidget(self.right_button, 1, 2, 1, 1)

        self.down_button = QPushButton(self.roboNavControl)
        self.down_button.setObjectName(u"down_button")
        icon4 = QIcon()
        icon4.addFile(u":/backImages/icons/down.png", QSize(), QIcon.Normal, QIcon.On)
        self.down_button.setIcon(icon4)

        self.keycontrols.addWidget(self.down_button, 2, 1, 1, 1)

        self.c_button = QPushButton(self.roboNavControl)
        self.c_button.setObjectName(u"c_button")
        icon5 = QIcon()
        icon5.addFile(u":/backImages/icons/C.png", QSize(), QIcon.Normal, QIcon.On)
        self.c_button.setIcon(icon5)

        self.keycontrols.addWidget(self.c_button, 0, 2, 1, 1)

        self.cc_button = QPushButton(self.roboNavControl)
        self.cc_button.setObjectName(u"cc_button")
        icon6 = QIcon()
        icon6.addFile(u":/backImages/icons/CC.png", QSize(), QIcon.Normal, QIcon.On)
        self.cc_button.setIcon(icon6)

        self.keycontrols.addWidget(self.cc_button, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.keycontrols, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.roboNavControl)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.roboNavControl)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_15 = QLabel(self.roboNavControl)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.roboNavControl)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_12 = QLabel(self.roboNavControl)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.roboNavControl)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.roboNavControl)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 1, 2, 2, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.roboNavControl)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.roboNavControl)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_3.addWidget(self.progressBar, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.roboNavControl)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.roboNavControl)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.viewLaser_button = QPushButton(self.roboNavControl)
        self.viewLaser_button.setObjectName(u"viewLaser_button")

        self.gridLayout_3.addWidget(self.viewLaser_button, 2, 0, 1, 1)

        self.view_camera_button = QPushButton(self.roboNavControl)
        self.view_camera_button.setObjectName(u"view_camera_button")

        self.gridLayout_3.addWidget(self.view_camera_button, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 4, 2, 1)

        self.pushButton_9 = QPushButton(self.roboNavControl)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(239, 41, 41);")

        self.gridLayout_5.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.line_4 = QFrame(self.roboNavControl)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 0, 1, 3, 1)

        self.line_3 = QFrame(self.roboNavControl)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 0, 3, 3, 1)


        self.horizontalLayout_8.addWidget(self.roboNavControl)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.line_2 = QFrame(guiDlg)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.groupBox_2 = QGroupBox(guiDlg)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tts_edit = QTextEdit(self.groupBox_2)
        self.tts_edit.setObjectName(u"tts_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tts_edit.sizePolicy().hasHeightForWidth())
        self.tts_edit.setSizePolicy(sizePolicy2)
        self.tts_edit.setMinimumSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.tts_edit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.speak_button = QPushButton(self.groupBox_2)
        self.speak_button.setObjectName(u"speak_button")

        self.horizontalLayout_5.addWidget(self.speak_button)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listen_button = QPushButton(self.groupBox_2)
        self.listen_button.setObjectName(u"listen_button")

        self.horizontalLayout_7.addWidget(self.listen_button)

        self.asr_edit = QTextEdit(self.groupBox_2)
        self.asr_edit.setObjectName(u"asr_edit")
        sizePolicy2.setHeightForWidth(self.asr_edit.sizePolicy().hasHeightForWidth())
        self.asr_edit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.asr_edit)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox_2)


        self.gridLayout_10.addLayout(self.horizontalLayout_8, 2, 0, 1, 5)

        self.line = QFrame(guiDlg)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line, 0, 2, 1, 1)

        self.CalendarEvents = QGroupBox(guiDlg)
        self.CalendarEvents.setObjectName(u"CalendarEvents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CalendarEvents.sizePolicy().hasHeightForWidth())
        self.CalendarEvents.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.CalendarEvents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.viewagenda = QGridLayout()
        self.viewagenda.setObjectName(u"viewagenda")
        self.label_9 = QLabel(self.CalendarEvents)
        self.label_9.setObjectName(u"label_9")

        self.viewagenda.addWidget(self.label_9, 0, 1, 1, 2)

        self.label_22 = QLabel(self.CalendarEvents)
        self.label_22.setObjectName(u"label_22")

        self.viewagenda.addWidget(self.label_22, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.CalendarEvents)
        self.dateEdit.setObjectName(u"dateEdit")

        self.viewagenda.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.CalendarEvents)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.viewagenda.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.label = QLabel(self.CalendarEvents)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font1 = QFont()
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setInputMethodHints(Qt.ImhNone)

        self.viewagenda.addWidget(self.label, 2, 1, 1, 2)


        self.horizontalLayout.addLayout(self.viewagenda)

        self.line_5 = QFrame(self.CalendarEvents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.setnewactivity = QGridLayout()
        self.setnewactivity.setObjectName(u"setnewactivity")
        self.label_24 = QLabel(self.CalendarEvents)
        self.label_24.setObjectName(u"label_24")

        self.setnewactivity.addWidget(self.label_24, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.CalendarEvents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.setnewactivity.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.setnewactivity.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.CalendarEvents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.setnewactivity.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.CalendarEvents)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.setnewactivity.addWidget(self.comboBox_3, 1, 0, 1, 3)


        self.horizontalLayout.addLayout(self.setnewactivity)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_10.addWidget(self.CalendarEvents, 0, 0, 1, 1)

        self.humanObsAgent = QGroupBox(guiDlg)
        self.humanObsAgent.setObjectName(u"humanObsAgent")
        self.humanObsAgent.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.humanObsAgent.sizePolicy().hasHeightForWidth())
        self.humanObsAgent.setSizePolicy(sizePolicy4)
        self.gridLayout_9 = QGridLayout(self.humanObsAgent)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.photo_viewer = QGraphicsView(self.humanObsAgent)
        self.photo_viewer.setObjectName(u"photo_viewer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.photo_viewer.sizePolicy().hasHeightForWidth())
        self.photo_viewer.setSizePolicy(sizePolicy5)
        self.photo_viewer.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.photo_viewer)

        self.addPhotoB = QPushButton(self.humanObsAgent)
        self.addPhotoB.setObjectName(u"addPhotoB")

        self.verticalLayout_4.addWidget(self.addPhotoB)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.humanObsAgent)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.id_list = QComboBox(self.humanObsAgent)
        self.id_list.setObjectName(u"id_list")

        self.horizontalLayout_2.addWidget(self.id_list)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newHuman_button = QPushButton(self.humanObsAgent)
        self.newHuman_button.setObjectName(u"newHuman_button")

        self.horizontalLayout_3.addWidget(self.newHuman_button)

        self.setHuman_button = QPushButton(self.humanObsAgent)
        self.setHuman_button.setObjectName(u"setHuman_button")

        self.horizontalLayout_3.addWidget(self.setHuman_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_9.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.humanObsAgent)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(6)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.H_name = QLineEdit(self.groupBox)
        self.H_name.setObjectName(u"H_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.H_name)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.H_age = QComboBox(self.groupBox)
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.addItem("")
        self.H_age.setObjectName(u"H_age")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.H_age)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.H_userType = QComboBox(self.groupBox)
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.addItem("")
        self.H_userType.setObjectName(u"H_userType")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.H_userType)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.H_phyDep = QSpinBox(self.groupBox)
        self.H_phyDep.setObjectName(u"H_phyDep")
        self.H_phyDep.setMaximum(100)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.H_phyDep)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_19)

        self.H_cogDep = QSpinBox(self.groupBox)
        self.H_cogDep.setObjectName(u"H_cogDep")
        self.H_cogDep.setMaximum(100)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.H_cogDep)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.H_emoSate = QComboBox(self.groupBox)
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.addItem("")
        self.H_emoSate.setObjectName(u"H_emoSate")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.H_emoSate)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.H_activity = QComboBox(self.groupBox)
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.addItem("")
        self.H_activity.setObjectName(u"H_activity")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.H_activity)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.H_gender = QComboBox(self.groupBox)
        self.H_gender.addItem("")
        self.H_gender.addItem("")
        self.H_gender.setObjectName(u"H_gender")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.H_gender)


        self.gridLayout_7.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.humanObsAgent)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.x_sb = QSpinBox(self.groupBox_4)
        self.x_sb.setObjectName(u"x_sb")
        self.x_sb.setMinimum(-10000)
        self.x_sb.setMaximum(10000)
        self.x_sb.setSingleStep(100)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_sb)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.z_sb = QSpinBox(self.groupBox_4)
        self.z_sb.setObjectName(u"z_sb")
        self.z_sb.setMinimum(-10000)
        self.z_sb.setMaximum(10000)
        self.z_sb.setSingleStep(100)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.z_sb)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.rot_sb = QDoubleSpinBox(self.groupBox_4)
        self.rot_sb.setObjectName(u"rot_sb")
        self.rot_sb.setMinimum(-3.140000000000000)
        self.rot_sb.setMaximum(3.140000000000000)
        self.rot_sb.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rot_sb)

        self.setPose_pb = QPushButton(self.groupBox_4)
        self.setPose_pb.setObjectName(u"setPose_pb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.setPose_pb)


        self.gridLayout_8.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.interacion_gb = QGroupBox(self.humanObsAgent)
        self.interacion_gb.setObjectName(u"interacion_gb")
        palette = QPalette()
        brush = QBrush(QColor(5, 78, 39, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.interacion_gb.setPalette(palette)
        self.interacion_gb.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.interacion_gb)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.int1_cb = QComboBox(self.interacion_gb)
        self.int1_cb.setObjectName(u"int1_cb")

        self.gridLayout_2.addWidget(self.int1_cb, 0, 0, 1, 1)

        self.interaction_cb = QComboBox(self.interacion_gb)
        self.interaction_cb.addItem("")
        self.interaction_cb.addItem("")
        self.interaction_cb.addItem("")
        self.interaction_cb.addItem("")
        self.interaction_cb.addItem("")
        self.interaction_cb.setObjectName(u"interaction_cb")

        self.gridLayout_2.addWidget(self.interaction_cb, 0, 1, 1, 1)

        self.ainteraction_pb = QPushButton(self.interacion_gb)
        self.ainteraction_pb.setObjectName(u"ainteraction_pb")

        self.gridLayout_2.addWidget(self.ainteraction_pb, 2, 1, 1, 1)

        self.int2_cb = QComboBox(self.interacion_gb)
        self.int2_cb.setObjectName(u"int2_cb")

        self.gridLayout_2.addWidget(self.int2_cb, 0, 2, 1, 1)

        self.interaction_cb_2 = QComboBox(self.interacion_gb)
        self.interaction_cb_2.addItem("")
        self.interaction_cb_2.addItem("")
        self.interaction_cb_2.addItem("")
        self.interaction_cb_2.addItem("")
        self.interaction_cb_2.setObjectName(u"interaction_cb_2")

        self.gridLayout_2.addWidget(self.interaction_cb_2, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.interaction_lw = QListWidget(self.interacion_gb)
        self.interaction_lw.setObjectName(u"interaction_lw")
        sizePolicy5.setHeightForWidth(self.interaction_lw.sizePolicy().hasHeightForWidth())
        self.interaction_lw.setSizePolicy(sizePolicy5)
        self.interaction_lw.setMinimumSize(QSize(264, 87))

        self.verticalLayout_5.addWidget(self.interaction_lw)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.rinteraction_pb = QPushButton(self.interacion_gb)
        self.rinteraction_pb.setObjectName(u"rinteraction_pb")

        self.horizontalLayout_6.addWidget(self.rinteraction_pb)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 9)

        self.gridLayout_9.addWidget(self.interacion_gb, 0, 3, 1, 1)


        self.gridLayout_10.addWidget(self.humanObsAgent, 4, 0, 1, 5)

        self.groupBox_3 = QGroupBox(guiDlg)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(118, 21))

        self.verticalLayout.addWidget(self.label_25)

        self.graphicsView_4 = QGraphicsView(self.groupBox_3)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.graphicsView_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_4.setSizePolicy(sizePolicy6)
        self.graphicsView_4.setMinimumSize(QSize(0, 0))
        self.graphicsView_4.setMaximumSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.graphicsView_4)


        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(50, 16))

        self.verticalLayout_2.addWidget(self.label_28)

        self.FacialExpr = QComboBox(self.groupBox_3)
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.addItem("")
        self.FacialExpr.setObjectName(u"FacialExpr")
        self.FacialExpr.setMaximumSize(QSize(118, 23))

        self.verticalLayout_2.addWidget(self.FacialExpr)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 4, 1, 1)

        self.line_7 = QFrame(guiDlg)
        self.line_7.setObjectName(u"line_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy7)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_7, 1, 0, 1, 5)

        self.line_8 = QFrame(guiDlg)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_8, 3, 0, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"humanObserverAgent_GUI", None))
        self.listen_status.setText("")
        self.roboNavControl.setTitle(QCoreApplication.translate("guiDlg", u"Robot navigation and control", None))
        self.label_16.setText(QCoreApplication.translate("guiDlg", u"Go to", None))
        self.label_17.setText(QCoreApplication.translate("guiDlg", u"Monitoring", None))
        self.up_button.setText("")
        self.left_button.setText("")
        self.stop_button.setText("")
        self.right_button.setText("")
        self.down_button.setText("")
        self.c_button.setText("")
        self.cc_button.setText("")
        self.label_11.setText(QCoreApplication.translate("guiDlg", u"x", None))
        self.lineEdit.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.label_15.setText(QCoreApplication.translate("guiDlg", u"z", None))
        self.lineEdit_2.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.label_12.setText(QCoreApplication.translate("guiDlg", u"heading", None))
        self.lineEdit_3.setText(QCoreApplication.translate("guiDlg", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("guiDlg", u"GO", None))
        self.label_13.setText(QCoreApplication.translate("guiDlg", u"Battery", None))
        self.pushButton_4.setText(QCoreApplication.translate("guiDlg", u"Stop robot", None))
        self.pushButton_5.setText(QCoreApplication.translate("guiDlg", u"Reset robot", None))
        self.viewLaser_button.setText(QCoreApplication.translate("guiDlg", u"View Laser", None))
        self.view_camera_button.setText(QCoreApplication.translate("guiDlg", u"View Camera", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("guiDlg", u"<html><head/><body><p>w -&gt; forward </p><p>s -&gt; backward </p><p>a -&gt; left </p><p>d -&gt; right </p><p>f -&gt; CClockwise </p><p>g -&gt; clockwise </p><p>backspace -&gt; stop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText(QCoreApplication.translate("guiDlg", u"Keyboard Control Off", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("guiDlg", u"TTS/ASR", None))
        self.label_23.setText(QCoreApplication.translate("guiDlg", u"From robot to human", None))
        self.label_4.setText(QCoreApplication.translate("guiDlg", u"From human to robot", None))
        self.speak_button.setText(QCoreApplication.translate("guiDlg", u"Speak", None))
        self.listen_button.setText(QCoreApplication.translate("guiDlg", u"Listen", None))
        self.CalendarEvents.setTitle(QCoreApplication.translate("guiDlg", u"Activity Calendar", None))
        self.label_9.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Date</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><img src=\":/GUI/Icons/calendar.png\" /></p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("guiDlg", u"View agenda", None))
        self.label.setText("")
        self.label_24.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Activity agenda</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("guiDlg", u"New activity", None))
        self.pushButton_11.setText(QCoreApplication.translate("guiDlg", u"Set activity", None))
        self.humanObsAgent.setTitle(QCoreApplication.translate("guiDlg", u"Human observer agent", None))
        self.addPhotoB.setText(QCoreApplication.translate("guiDlg", u"Add Photo", None))
        self.label_14.setText(QCoreApplication.translate("guiDlg", u"Id", None))
        self.newHuman_button.setText(QCoreApplication.translate("guiDlg", u"New human", None))
        self.setHuman_button.setText(QCoreApplication.translate("guiDlg", u"Set human", None))
        self.groupBox.setTitle(QCoreApplication.translate("guiDlg", u"Human Information", None))
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

        self.label_21.setText(QCoreApplication.translate("guiDlg", u"Gender", None))
        self.H_gender.setItemText(0, QCoreApplication.translate("guiDlg", u"Male", None))
        self.H_gender.setItemText(1, QCoreApplication.translate("guiDlg", u"Female", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("guiDlg", u"Pose", None))
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
        self.interacion_gb.setTitle(QCoreApplication.translate("guiDlg", u"Interaction", None))
        self.interaction_cb.setItemText(0, QCoreApplication.translate("guiDlg", u"isBusy", None))
        self.interaction_cb.setItemText(1, QCoreApplication.translate("guiDlg", u"interacting", None))
        self.interaction_cb.setItemText(2, QCoreApplication.translate("guiDlg", u"block", None))
        self.interaction_cb.setItemText(3, QCoreApplication.translate("guiDlg", u"affordanceBlock", None))
        self.interaction_cb.setItemText(4, QCoreApplication.translate("guiDlg", u"softBlock", None))

        self.ainteraction_pb.setText(QCoreApplication.translate("guiDlg", u"Add", None))
        self.interaction_cb_2.setItemText(0, QCoreApplication.translate("guiDlg", u"Talking", None))
        self.interaction_cb_2.setItemText(1, QCoreApplication.translate("guiDlg", u"Playing", None))
        self.interaction_cb_2.setItemText(2, QCoreApplication.translate("guiDlg", u"using", None))
        self.interaction_cb_2.setItemText(3, QCoreApplication.translate("guiDlg", u"watching", None))

        self.rinteraction_pb.setText(QCoreApplication.translate("guiDlg", u"Remove", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("guiDlg", u"Human-Robot Interaction", None))
        self.label_25.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600;\">Facial expression</span></p><p><br/></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("guiDlg", u"Emotion", None))
        self.FacialExpr.setItemText(0, QCoreApplication.translate("guiDlg", u"anger", None))
        self.FacialExpr.setItemText(1, QCoreApplication.translate("guiDlg", u"crying", None))
        self.FacialExpr.setItemText(2, QCoreApplication.translate("guiDlg", u"happy", None))
        self.FacialExpr.setItemText(3, QCoreApplication.translate("guiDlg", u"lazy", None))
        self.FacialExpr.setItemText(4, QCoreApplication.translate("guiDlg", u"neutral", None))
        self.FacialExpr.setItemText(5, QCoreApplication.translate("guiDlg", u"sad", None))
        self.FacialExpr.setItemText(6, QCoreApplication.translate("guiDlg", u"sadlySurprised", None))
        self.FacialExpr.setItemText(7, QCoreApplication.translate("guiDlg", u"smile", None))
        self.FacialExpr.setItemText(8, QCoreApplication.translate("guiDlg", u"surprised", None))

    # retranslateUi

