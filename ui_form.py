# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(281, 296)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.labelDe = QLabel(Widget)
        self.labelDe.setObjectName(u"labelDe")

        self.gridLayout.addWidget(self.labelDe, 7, 0, 1, 1)

        self.label_1 = QLabel(Widget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_1, 0, 2, 1, 1)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.labelRo = QLabel(Widget)
        self.labelRo.setObjectName(u"labelRo")

        self.gridLayout.addWidget(self.labelRo, 5, 0, 1, 1)

        self.labelRe = QLabel(Widget)
        self.labelRe.setObjectName(u"labelRe")

        self.gridLayout.addWidget(self.labelRe, 6, 0, 1, 1)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)

        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_8, 7, 2, 1, 1)

        self.labelF = QLabel(Widget)
        self.labelF.setObjectName(u"labelF")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelF.sizePolicy().hasHeightForWidth())
        self.labelF.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelF, 1, 0, 1, 1)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)

        self.labelK = QLabel(Widget)
        self.labelK.setObjectName(u"labelK")

        self.gridLayout.addWidget(self.labelK, 2, 0, 1, 1)

        self.labelC = QLabel(Widget)
        self.labelC.setObjectName(u"labelC")
        sizePolicy1.setHeightForWidth(self.labelC.sizePolicy().hasHeightForWidth())
        self.labelC.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelC, 0, 0, 1, 1)

        self.labelR = QLabel(Widget)
        self.labelR.setObjectName(u"labelR")

        self.gridLayout.addWidget(self.labelR, 3, 0, 1, 1)

        self.labelN = QLabel(Widget)
        self.labelN.setObjectName(u"labelN")

        self.gridLayout.addWidget(self.labelN, 4, 0, 1, 1)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)

        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)

        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_6, 5, 1, 1, 1)

        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_7, 6, 1, 1, 1)

        self.pushButton_8 = QPushButton(Widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)
        self.pushButton_8.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_8, 7, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Conversor de temperatura", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"\u00b0C", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"\u00b0F", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"K", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"R", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"\u00b0N", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Widget", u"\u00b0R\u00f8", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Widget", u"\u00b0R\u00e9", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Widget", u"\u00b0De", None))

        self.label_2.setText(QCoreApplication.translate("Widget", u"\u00b0F", None))
        self.labelDe.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"\u00b0C", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"K", None))
        self.labelRo.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.labelRe.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u00b0R\u00f8", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u00b0De", None))
        self.labelF.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"R", None))
        self.labelK.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.labelC.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.labelR.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.labelN.setText(QCoreApplication.translate("Widget", u"0.000", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u00b0N", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u00b0Re", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
    # retranslateUi

