# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partner_cardTSTiUC.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_partnerCard(object):
    def setupUi(self, partnerCard):
        if not partnerCard.objectName():
            partnerCard.setObjectName(u"partnerCard")
        partnerCard.resize(400, 125)
        partnerCard.setMinimumSize(QSize(0, 125))
        partnerCard.setMaximumSize(QSize(16777215, 125))
        self.horizontalLayout = QHBoxLayout(partnerCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cardLayout = QWidget(partnerCard)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setStyleSheet(u"#cardLayout{\n"
"	border: 2px solid black;\n"
"	background: #F4E8D3;\n"
"}\n"
"\n"
"#cardLayout:hover{\n"
"	background: #67BA80;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.cardLayout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.cardLayout)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(12)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title)

        self.director = QLabel(self.cardLayout)
        self.director.setObjectName(u"director")

        self.verticalLayout.addWidget(self.director)

        self.phone = QLabel(self.cardLayout)
        self.phone.setObjectName(u"phone")

        self.verticalLayout.addWidget(self.phone)

        self.rate = QLabel(self.cardLayout)
        self.rate.setObjectName(u"rate")

        self.verticalLayout.addWidget(self.rate)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.discount = QLabel(self.cardLayout)
        self.discount.setObjectName(u"discount")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discount.sizePolicy().hasHeightForWidth())
        self.discount.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.discount)


        self.horizontalLayout.addWidget(self.cardLayout)


        self.retranslateUi(partnerCard)

        QMetaObject.connectSlotsByName(partnerCard)
    # setupUi

    def retranslateUi(self, partnerCard):
        partnerCard.setWindowTitle(QCoreApplication.translate("partnerCard", u"Form", None))
        self.title.setText(QCoreApplication.translate("partnerCard", u"TextLabel", None))
        self.director.setText(QCoreApplication.translate("partnerCard", u"TextLabel", None))
        self.phone.setText(QCoreApplication.translate("partnerCard", u"TextLabel", None))
        self.rate.setText(QCoreApplication.translate("partnerCard", u"TextLabel", None))
        self.discount.setText(QCoreApplication.translate("partnerCard", u"TextLabel", None))
    # retranslateUi

