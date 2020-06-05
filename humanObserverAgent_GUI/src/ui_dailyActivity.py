# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dailyActivity.ui'
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


class Ui_DailyActivity(object):
    def setupUi(self, DailyActivity):
        if DailyActivity.objectName():
            DailyActivity.setObjectName(u"DailyActivity")
        DailyActivity.resize(704, 300)
        DailyActivity.setMaximumSize(QSize(16777215, 300))
        self.tableWidget = QTableWidget(DailyActivity)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-2, 0, 705, 299))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)

        self.retranslateUi(DailyActivity)

        QMetaObject.connectSlotsByName(DailyActivity)
    # setupUi

    def retranslateUi(self, DailyActivity):
        DailyActivity.setWindowTitle(QCoreApplication.translate("DailyActivity", u"Dialog", None))
    # retranslateUi

