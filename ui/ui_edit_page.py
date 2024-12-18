# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_pagehpGcCT.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_editPage(object):
    def setupUi(self, editPage):
        if not editPage.objectName():
            editPage.setObjectName(u"editPage")
        editPage.resize(404, 481)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editPage.sizePolicy().hasHeightForWidth())
        editPage.setSizePolicy(sizePolicy)
        editPage.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        editPage.setFont(font)
        self.verticalLayout = QVBoxLayout(editPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.scrollArea = QScrollArea(editPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 372, 476))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameTitle = QLabel(self.scrollAreaWidgetContents)
        self.nameTitle.setObjectName(u"nameTitle")

        self.verticalLayout_2.addWidget(self.nameTitle)

        self.nameField = QLineEdit(self.scrollAreaWidgetContents)
        self.nameField.setObjectName(u"nameField")

        self.verticalLayout_2.addWidget(self.nameField)

        self.typeTitle = QLabel(self.scrollAreaWidgetContents)
        self.typeTitle.setObjectName(u"typeTitle")

        self.verticalLayout_2.addWidget(self.typeTitle)

        self.typeField = QComboBox(self.scrollAreaWidgetContents)
        self.typeField.setObjectName(u"typeField")

        self.verticalLayout_2.addWidget(self.typeField)

        self.innTitle = QLabel(self.scrollAreaWidgetContents)
        self.innTitle.setObjectName(u"innTitle")

        self.verticalLayout_2.addWidget(self.innTitle)

        self.innField = QLineEdit(self.scrollAreaWidgetContents)
        self.innField.setObjectName(u"innField")

        self.verticalLayout_2.addWidget(self.innField)

        self.rateTitle = QLabel(self.scrollAreaWidgetContents)
        self.rateTitle.setObjectName(u"rateTitle")

        self.verticalLayout_2.addWidget(self.rateTitle)

        self.rateField = QSpinBox(self.scrollAreaWidgetContents)
        self.rateField.setObjectName(u"rateField")
        self.rateField.setMaximum(10)

        self.verticalLayout_2.addWidget(self.rateField)

        self.addressTitle = QLabel(self.scrollAreaWidgetContents)
        self.addressTitle.setObjectName(u"addressTitle")

        self.verticalLayout_2.addWidget(self.addressTitle)

        self.addressField = QLineEdit(self.scrollAreaWidgetContents)
        self.addressField.setObjectName(u"addressField")

        self.verticalLayout_2.addWidget(self.addressField)

        self.directorTitle = QLabel(self.scrollAreaWidgetContents)
        self.directorTitle.setObjectName(u"directorTitle")

        self.verticalLayout_2.addWidget(self.directorTitle)

        self.directorFiled = QLineEdit(self.scrollAreaWidgetContents)
        self.directorFiled.setObjectName(u"directorFiled")

        self.verticalLayout_2.addWidget(self.directorFiled)

        self.phoneTitle = QLabel(self.scrollAreaWidgetContents)
        self.phoneTitle.setObjectName(u"phoneTitle")

        self.verticalLayout_2.addWidget(self.phoneTitle)

        self.phoneField = QLineEdit(self.scrollAreaWidgetContents)
        self.phoneField.setObjectName(u"phoneField")

        self.verticalLayout_2.addWidget(self.phoneField)

        self.emailTitle = QLabel(self.scrollAreaWidgetContents)
        self.emailTitle.setObjectName(u"emailTitle")

        self.verticalLayout_2.addWidget(self.emailTitle)

        self.emailField = QLineEdit(self.scrollAreaWidgetContents)
        self.emailField.setObjectName(u"emailField")

        self.verticalLayout_2.addWidget(self.emailField)

        self.editButton = QPushButton(self.scrollAreaWidgetContents)
        self.editButton.setObjectName(u"editButton")

        self.verticalLayout_2.addWidget(self.editButton)

        self.cancelButton = QPushButton(self.scrollAreaWidgetContents)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(editPage)

        QMetaObject.connectSlotsByName(editPage)
    # setupUi

    def retranslateUi(self, editPage):
        editPage.setWindowTitle(QCoreApplication.translate("editPage", u"Form", None))
        self.nameTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.typeTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.innTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.rateTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.addressTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.directorTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.phoneTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.emailTitle.setText(QCoreApplication.translate("editPage", u"TextLabel", None))
        self.editButton.setText(QCoreApplication.translate("editPage", u"PushButton", None))
        self.cancelButton.setText(QCoreApplication.translate("editPage", u"PushButton", None))
    # retranslateUi

