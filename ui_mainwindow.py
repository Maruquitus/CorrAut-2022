# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        Form.setStyleSheet(u"QWidget#Form {background-color: qlineargradient(spread:pad, x1:0.134, y1:0.892045, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1361, 101))
        font = QFont()
        font.setFamilies([u"Open Sans Extrabold"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridFrame = QFrame(Form)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(110, 110, 500, 561))
        self.gridFrame.setMaximumSize(QSize(16777215, 1000))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(12)
        self.gridFrame.setFont(font1)
        self.gridFrame.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame.setFrameShape(QFrame.Panel)
        self.gridFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(4)
        self.comboBox = QComboBox(self.gridFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet(u"QComboBox#comboBox{border-radius: 10; background-color: rgb(245, 245, 245); height:40}\n"
"QComboBox#comboBox::hover {background-color: rgb(248, 248, 250)}\n"
"QComboBox#comboBox::down-arrow{image: url(coisas/arrow.png);}\n"
"QComboBox#comboBox::drop-down{border-radius: 0;}")
        self.comboBox.setFrame(True)

        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.gridFrame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font1)
        self.doubleSpinBox.setStyleSheet(u"QDoubleSpinBox#doubleSpinBox{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(0.000000000000000)
        self.doubleSpinBox.setMaximum(50.000000000000000)
        self.doubleSpinBox.setValue(45.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox, 13, 1, 1, 1)

        self.label_7 = QLabel(self.gridFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_7, 18, 1, 1, 1)

        self.label_3 = QLabel(self.gridFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 10, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.gridFrame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox_2.setStyleSheet(u"QComboBox#comboBox_2{border-radius: 10; background-color: rgb(245, 245, 245); height:40}\n"
"QComboBox#comboBox_2::drop-down{border:10px}\n"
"QComboBox#comboBox_2::hover {background-color: rgb(248, 248, 250)}\n"
"QComboBox#comboBox_2::down-arrow{image: url(coisas/arrow.png);}")

        self.gridLayout.addWidget(self.comboBox_2, 10, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 11, 1, 1, 1)

        self.label_6 = QLabel(self.gridFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_6, 14, 1, 1, 1)

        self.label_8 = QLabel(self.gridFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_8, 16, 1, 1, 1)

        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Open Sans Semibold"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: black")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 2, 3)

        self.label_4 = QLabel(self.gridFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 10, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.gridFrame)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setFont(font1)
        self.doubleSpinBox_2.setStyleSheet(u"QDoubleSpinBox#doubleSpinBox_2{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(5.000000000000000)
        self.doubleSpinBox_2.setMaximum(45.000000000000000)
        self.doubleSpinBox_2.setValue(26.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_2, 15, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 22, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit#lineEdit_2{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit_2, 17, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"QLineEdit#lineEdit{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setCursorPosition(61)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit, 19, 1, 1, 1)

        self.label_5 = QLabel(self.gridFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout.addWidget(self.label_5, 12, 1, 1, 1)

        self.pushButton = QPushButton(self.gridFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(102000, 16777215))
        self.pushButton.setBaseSize(QSize(0, 72))
        font4 = QFont()
        font4.setFamilies([u"Open Sans"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 100; width:250;  position: relative;  margin-left: 50%; margin-right: 50%;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255)); color: rgb(255, 255, 255);\n"
"} \n"
"QPushButton#pushButton:pressed {\n"
"background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(False)

        self.gridLayout.addWidget(self.pushButton, 21, 1, 1, 1)

        self.gridFrame_2 = QFrame(Form)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setGeometry(QRect(640, 110, 621, 561))
        self.gridFrame_2.setMaximumSize(QSize(16777215, 1000))
        self.gridFrame_2.setFont(font1)
        self.gridFrame_2.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame_2.setFrameShape(QFrame.Panel)
        self.gridFrame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.gridFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(4)
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 14, 1, 1, 1)

        self.label_12 = QLabel(self.gridFrame_2)
        self.label_12.setObjectName(u"label_12")
        font5 = QFont()
        font5.setFamilies([u"Open Sans"])
        font5.setPointSize(20)
        font5.setBold(False)
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color: rgb(50, 50, 50)")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridFrame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(102000, 40))
        self.pushButton_3.setBaseSize(QSize(0, 72))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 100; position: relative;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255)); color: rgb(255, 255, 255);\n"
"} \n"
"QPushButton#pushButton_3:pressed {\n"
"background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_3, 12, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 7, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridFrame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(102000, 40))
        self.pushButton_4.setBaseSize(QSize(0, 72))
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 100; position: relative;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255)); color: rgb(255, 255, 255);\n"
"} \n"
"QPushButton#pushButton_4:pressed {\n"
"background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_4, 12, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 10, 1, 1, 1)

        self.label_9 = QLabel(self.gridFrame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(480, 360))
        self.label_9.setMaximumSize(QSize(480, 360))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgb(100, 100, 100); border-radius:20; color: rgb(200, 200, 200)")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 7, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 7, 0, 1, 1)

        self.label_11 = QLabel(self.gridFrame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: black")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 3)

        self.pushButton_2 = QPushButton(self.gridFrame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(102000, 40))
        self.pushButton_2.setBaseSize(QSize(0, 72))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"QPushButton:active {\n"
"    border-radius: 10;\n"
"    background-color: QLinearGradient(x1: 0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255));\n"
"    color: rgb(253, 253, 253);\n"
"    height: 100;\n"
"    width:250;\n"
"    position: relative\n"
"    }\n"
"QPushButton:disabled {\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(170, 170, 170, 255), stop:1 rgba(190, 190, 190, 255)); color: rgb(253, 253, 253); height: 100; width:250;  position: relative;\n"
"    }\n"
"QPushButton:hover {\n"
"    background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255));\n"
"    color: rgb(255, 255, 255)\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"    color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_2, 12, 1, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(490, 710, 382, 38))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(102000, 16777215))
        self.pushButton_5.setBaseSize(QSize(0, 72))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 100; width:250;  position: relative\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255)); color: rgb(255, 255, 255);\n"
"} \n"
"QPushButton#pushButton:pressed {\n"
"background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(False)

        self.retranslateUi(Form)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Cadastro de Gabarito", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1\u00ba Ano", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"2\u00ba Ano", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"3\u00ba Ano", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Pasta de Destino", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Curso", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Turismo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Enfermagem", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Inform\u00e1tica", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"Agroind\u00fastria", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Quantidade de quest\u00f5es", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Avalia\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Informa\u00e7\u00f5es", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"S\u00e9rie", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Avalia\u00e7\u00e3o de Exemplo", None))
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"C:\\Users\\Marco\\OneDrive\\Documentos\\feiradeciencias\\Avalia\u00e7\u00f5es", None))
        self.lineEdit.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Quantidade de alunos", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Escolher Pasta", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Gabarito 1/45", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"->", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"<-", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Carregando webcam...", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Webcam", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Visualiza\u00e7\u00e3o de gabaritos", None))
    # retranslateUi

