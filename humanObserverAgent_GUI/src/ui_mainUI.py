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


class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(649, 170)
        self.label_9 = QLabel(guiDlg)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 0, 151, 21))
        self.label_22 = QLabel(guiDlg)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 30, 21, 31))
        self.pushButton_14 = QPushButton(guiDlg)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(146, 30, 101, 23))
        self.line_5 = QFrame(guiDlg)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(246, 2, 20, 91))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_24 = QLabel(guiDlg)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(306, 0, 151, 21))
        self.pushButton_10 = QPushButton(guiDlg)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(266, 60, 91, 23))
        self.pushButton_11 = QPushButton(guiDlg)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(366, 60, 91, 23))
        self.comboBox_3 = QComboBox(guiDlg)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(266, 30, 191, 22))
        self.label = QLabel(guiDlg)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(40, 62, 271, 17))
        font = QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.ImhNone)
        self.dateEdit = QDateEdit(guiDlg)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(36, 28, 93, 26))

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"humanObserverAgent_GUI", None))
        self.label_9.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Date</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><img src=\":/GUI/Icons/calendar.png\" /></p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("guiDlg", u"View agenda", None))
        self.label_24.setText(QCoreApplication.translate("guiDlg", u"<html><head/><body><p><span style=\" font-weight:600; color:#054e27;\">Activity agenda</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("guiDlg", u"New activity", None))
        self.pushButton_11.setText(QCoreApplication.translate("guiDlg", u"Set activity", None))
        self.label.setText(QCoreApplication.translate("guiDlg", u"Loading", None))
    # retranslateUi

