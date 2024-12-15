# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partners_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_partnersPage(object):
    def setupUi(self, partnersPage):
        if not partnersPage.objectName():
            partnersPage.setObjectName(u"partnersPage")
        partnersPage.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(partnersPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pageTitle = QLabel(partnersPage)
        self.pageTitle.setObjectName(u"pageTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageTitle.sizePolicy().hasHeightForWidth())
        self.pageTitle.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pageTitle)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.partnersArea = QScrollArea(partnersPage)
        self.partnersArea.setObjectName(u"partnersArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.partnersArea.sizePolicy().hasHeightForWidth())
        self.partnersArea.setSizePolicy(sizePolicy1)
        self.partnersArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 254))
        self.partnersArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.partnersArea)


        self.retranslateUi(partnersPage)

        QMetaObject.connectSlotsByName(partnersPage)
    # setupUi

    def retranslateUi(self, partnersPage):
        partnersPage.setWindowTitle(QCoreApplication.translate("partnersPage", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("partnersPage", u"TextLabel", None))
    # retranslateUi

