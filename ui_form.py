# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModal)
        Widget.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setPointSize(12)
        Widget.setFont(font)
        Widget.setFocusPolicy(Qt.NoFocus)
        Widget.setStyleSheet(u"QWidget#Widget {background-color: qlineargradient(spread:pad, x1:0.134, y1:0.892045, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-10, 0, 1381, 771))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(self.gridLayoutWidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setMaximumSize(QSize(16777215, 350))
        self.gridFrame.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame.setFrameShape(QFrame.Panel)
        self.gridFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(4)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 9, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"border-radius: 10; background-color: rgb(245, 245, 245); height:40")

        self.gridLayout.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.label_3 = QLabel(self.gridFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 10, 1, 1, 1)

        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"border-radius: 10; background-color: rgb(245, 245, 245); height:40")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_2, 9, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 13, 1, 1, 1)

        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 2, 1, 1)

        self.pushButton = QPushButton(self.gridFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(20)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(102000, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"border-radius: 20;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 50; width:250;  position: relative;  margin-left: 50%; margin-right: 50%; QWidget#Widget {hover: colorr: rgb(255, 0, 255)}; ")
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(False)

        self.gridLayout.addWidget(self.pushButton, 12, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 4, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(500, 100))
        self.label_4.setPixmap(QPixmap(u"Vers\u00e3o preta.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 4, 2, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"Senha", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Usu\u00e1rio", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Entrar", None))
        self.label_4.setText("")
    # retranslateUi

