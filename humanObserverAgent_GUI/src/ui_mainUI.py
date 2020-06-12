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
        guiDlg.resize(745, 561)
        self.line_5 = QFrame(guiDlg)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(246, 2, 20, 91))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.roboNavControl = QGroupBox(guiDlg)
        self.roboNavControl.setObjectName(u"roboNavControl")
        self.roboNavControl.setGeometry(QRect(10, 110, 575, 185))
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
        self.line_7.setGeometry(QRect(-2, 88, 921, 21))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.layoutWidget1 = QWidget(guiDlg)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 0, 239, 93))
        self.viewagenda = QGridLayout(self.layoutWidget1)
        self.viewagenda.setObjectName(u"viewagenda")
        self.viewagenda.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.viewagenda.addWidget(self.label_9, 0, 1, 1, 2)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")

        self.viewagenda.addWidget(self.label_22, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.layoutWidget1)
        self.dateEdit.setObjectName(u"dateEdit")

        self.viewagenda.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.layoutWidget1)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.viewagenda.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.ImhNone)

        self.viewagenda.addWidget(self.label, 2, 1, 1, 2)

        self.layoutWidget2 = QWidget(guiDlg)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(282, 8, 211, 81))
        self.setnewactivity = QGridLayout(self.layoutWidget2)
        self.setnewactivity.setObjectName(u"setnewactivity")
        self.setnewactivity.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.layoutWidget2)
        self.label_24.setObjectName(u"label_24")

        self.setnewactivity.addWidget(self.label_24, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.layoutWidget2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.setnewactivity.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.setnewactivity.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.layoutWidget2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.setnewactivity.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget2)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.setnewactivity.addWidget(self.comboBox_3, 1, 0, 1, 3)

        self.humanObsAgent = QGroupBox(guiDlg)
        self.humanObsAgent.setObjectName(u"humanObsAgent")
        self.humanObsAgent.setGeometry(QRect(12, 304, 465, 235))
        self.pushButton_3 = QPushButton(self.humanObsAgent)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(156, 236, 71, 23))
        self.widget = QWidget(self.humanObsAgent)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(236, 30, 219, 193))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout.addWidget(self.lineEdit_7)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.widget1 = QWidget(self.humanObsAgent)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 28, 207, 199))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_2 = QGraphicsView(self.widget1)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_4.addWidget(self.graphicsView_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_15 = QPushButton(self.widget1)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_3.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget1)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_3.addWidget(self.pushButton_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


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
        self.label_9.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Date</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><img src=\":/GUI/Icons/calendar.png\" /></p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("guiDlg", u"View agenda", None))
        self.label.setText("")
        self.label_24.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Activity agenda</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("guiDlg", u"New activity", None))
        self.pushButton_11.setText(QCoreApplication.translate("guiDlg", u"Set activity", None))
        self.humanObsAgent.setTitle(QCoreApplication.translate("guiDlg", u"Human observer agent", None))
        self.pushButton_3.setText(QCoreApplication.translate("guiDlg", u"to DSR", None))
        self.label_4.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600;\">Human information</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("guiDlg", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("guiDlg", u"Age", None))
        self.label_7.setText(QCoreApplication.translate("guiDlg", u"User", None))
        self.label_8.setText(QCoreApplication.translate("guiDlg", u"Activity", None))
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.label_14.setText(QCoreApplication.translate("guiDlg", u"Id", None))
        self.pushButton_15.setText(QCoreApplication.translate("guiDlg", u"New human", None))
        self.pushButton_16.setText(QCoreApplication.translate("guiDlg", u"Set human", None))
    # retranslateUi

