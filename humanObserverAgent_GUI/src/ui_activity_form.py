# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activity_form.ui'
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


class Ui_activityForm(object):
    def setupUi(self, activityForm):
        if activityForm.objectName():
            activityForm.setObjectName(u"activityForm")
        activityForm.setEnabled(True)
        activityForm.resize(400, 403)
        activityForm.setModal(False)
        self.label_10 = QLabel(activityForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 50, 41, 21))
        self.comboBox_4 = QComboBox(activityForm)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(160, 50, 191, 22))
        self.label_9 = QLabel(activityForm)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QRect(24, 84, 121, 21))
        self.label_11 = QLabel(activityForm)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 160, 51, 21))
        self.timeEdit = QTimeEdit(activityForm)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(207, 160, 141, 26))
        self.timeEdit_2 = QTimeEdit(activityForm)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setGeometry(QRect(207, 190, 141, 26))
        self.label_12 = QLabel(activityForm)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(126, 164, 51, 21))
        self.label_13 = QLabel(activityForm)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(124, 190, 51, 21))
        self.label_14 = QLabel(activityForm)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 230, 91, 21))
        self.label_15 = QLabel(activityForm)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 260, 61, 21))
        self.label_16 = QLabel(activityForm)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 290, 121, 21))
        self.checkBox = QCheckBox(activityForm)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(160, 290, 92, 23))
        self.comboBox_5 = QComboBox(activityForm)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(160, 230, 191, 22))
        self.comboBox_6 = QComboBox(activityForm)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(160, 260, 191, 22))
        self.textEdit = QTextEdit(activityForm)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(160, 80, 191, 31))
        self.pushButton = QPushButton(activityForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 340, 89, 25))
        self.pushButton_2 = QPushButton(activityForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 340, 89, 25))
        self.label_17 = QLabel(activityForm)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(True)
        self.label_17.setGeometry(QRect(24, 124, 121, 21))
        self.textEdit_2 = QTextEdit(activityForm)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QRect(160, 120, 191, 31))
        self.label_18 = QLabel(activityForm)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        self.label_18.setGeometry(QRect(26, 14, 121, 21))
        self.textEdit_3 = QTextEdit(activityForm)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QRect(160, 10, 191, 31))

        self.retranslateUi(activityForm)

        QMetaObject.connectSlotsByName(activityForm)
    # setupUi

    def retranslateUi(self, activityForm):
        activityForm.setWindowTitle(QCoreApplication.translate("activityForm", u"Dialog", None))
        self.label_10.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Type</span></p><p><span style=\" font-weight:600; color:#054e27;\"><br/></span></p></body></html>", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("activityForm", u"Individual", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("activityForm", u"Collective", None))

        self.label_9.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Individual Name</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Time</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Start</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">End</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Location</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Element</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Notification</span></p></body></html>", None))
        self.checkBox.setText("")
        self.comboBox_5.setItemText(0, QCoreApplication.translate("activityForm", u"Physical therapy room", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("activityForm", u"Occupational therapy room", None))

        self.pushButton.setText(QCoreApplication.translate("activityForm", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("activityForm", u"Cancel", None))
        self.label_17.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Therapist Name</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("activityForm", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Activity Name</span></p></body></html>", None))
    # retranslateUi

