# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewLaser.ui'
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


class Ui_LaserViewer(object):
    def setupUi(self, LaserViewer):
        if LaserViewer.objectName():
            LaserViewer.setObjectName(u"LaserViewer")
        LaserViewer.resize(584, 376)
        self.label_3 = QLabel(LaserViewer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 62, 67, 17))
        self.widget = QWidget(LaserViewer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(14, 14, 105, 51))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(6)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.000050000000000)
        self.doubleSpinBox.setValue(0.004000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox)

        self.widget1 = QWidget(LaserViewer)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(400, 20, 156, 40))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalSlider = QSlider(self.widget1)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.retranslateUi(LaserViewer)
        self.horizontalSlider.valueChanged.connect(self.label_3.setNum)

        QMetaObject.connectSlotsByName(LaserViewer)
    # setupUi

    def retranslateUi(self, LaserViewer):
        LaserViewer.setWindowTitle(QCoreApplication.translate("LaserViewer", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("LaserViewer", u"1", None))
        self.label.setText(QCoreApplication.translate("LaserViewer", u"pixel/mm ratio", None))
        self.label_2.setText(QCoreApplication.translate("LaserViewer", u"Refresh Rate/sec           ", None))
    # retranslateUi

