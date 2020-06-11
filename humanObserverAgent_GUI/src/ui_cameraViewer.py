# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameraViewer.ui'
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


class Ui_CamViewer(object):
    def setupUi(self, CamViewer):
        if CamViewer.objectName():
            CamViewer.setObjectName(u"CamViewer")
        CamViewer.resize(744, 576)
        self.frame = QFrame(CamViewer)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(48, 48, 640, 480))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.retranslateUi(CamViewer)

        QMetaObject.connectSlotsByName(CamViewer)
    # setupUi

    def retranslateUi(self, CamViewer):
        CamViewer.setWindowTitle(QCoreApplication.translate("CamViewer", u"CamViewer", None))
    # retranslateUi

