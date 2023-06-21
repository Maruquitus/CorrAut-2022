# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gabarito.ui'
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
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        Form.setStyleSheet(u"QWidget#Form {background-color: qlineargradient(spread:pad, x1:0.134, y1:0.892045, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-30, 10, 1361, 101))
        font = QFont()
        font.setFamilies([u"Open Sans Extrabold"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridFrame = QFrame(Form)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(120, 120, 500, 211))
        self.gridFrame.setMaximumSize(QSize(16777215, 1000))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(12)
        self.gridFrame.setFont(font1)
        self.gridFrame.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame.setFrameShape(QFrame.Panel)
        self.gridFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.gridFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(4)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 16, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 16, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(102000, 16777215))
        self.pushButton_5.setBaseSize(QSize(0, 72))
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 40; width:250;  position: relative;  margin-left: 50%; margin-right: 50%;\n"
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

        self.gridLayout_3.addWidget(self.pushButton_5, 5, 1, 1, 1)

        self.label_16 = QLabel(self.gridFrame)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setFamilies([u"Open Sans Semibold"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: black")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)

        self.label_10 = QLabel(self.gridFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridFrame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        font4 = QFont()
        font4.setFamilies([u"Open Sans"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.lineEdit_4.setFont(font4)
        self.lineEdit_4.setStyleSheet(u"QLineEdit#lineEdit_4{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4.setCursorPosition(81)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.gridFrame_2 = QFrame(Form)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setGeometry(QRect(650, 120, 591, 561))
        self.gridFrame_2.setMaximumSize(QSize(16777215, 1000))
        self.gridFrame_2.setFont(font1)
        self.gridFrame_2.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame_2.setFrameShape(QFrame.Panel)
        self.gridFrame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.gridFrame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(4)
        self.label_21 = QLabel(self.gridFrame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: black")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_21, 2, 1, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 7, 0, 1, 1)

        self.listWidget = QListWidget(self.gridFrame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 400))
        font5 = QFont()
        font5.setFamilies([u"Open Sans"])
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        self.listWidget.setFont(font5)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setStyleSheet(u"border-radius: 10; background-color: rgb(250, 250, 250); \n"
"font: 600 20pt \"Open Sans\"; color: rgb(70, 70, 70);")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setViewMode(QListView.ListMode)

        self.gridLayout_4.addWidget(self.listWidget, 3, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 6, 1, 2, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 7, 2, 1, 1)

        self.gridFrame_3 = QFrame(Form)
        self.gridFrame_3.setObjectName(u"gridFrame_3")
        self.gridFrame_3.setGeometry(QRect(120, 340, 500, 341))
        self.gridFrame_3.setMaximumSize(QSize(16777215, 1000))
        self.gridFrame_3.setFont(font1)
        self.gridFrame_3.setStyleSheet(u"background-color: rgb(253, 253, 254); border-radius:30")
        self.gridFrame_3.setFrameShape(QFrame.Panel)
        self.gridFrame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.gridFrame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(4)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 18, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 23, 1, 1, 1)

        self.label_17 = QLabel(self.gridFrame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: black")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_17, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridFrame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font4)
        self.lineEdit_5.setStyleSheet(u"QLineEdit#lineEdit_5{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit_5.setEchoMode(QLineEdit.Normal)
        self.lineEdit_5.setCursorPosition(2)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit_5, 6, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 18, 0, 1, 1)

        self.label_13 = QLabel(self.gridFrame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout_5.addWidget(self.label_13, 1, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridFrame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setStyleSheet(u"QLineEdit#lineEdit_7{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit_7.setEchoMode(QLineEdit.Normal)
        self.lineEdit_7.setCursorPosition(7)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridFrame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setStyleSheet(u"QLineEdit#lineEdit_6{border-radius: 10; background-color: rgb(245, 245, 245); height:40}")
        self.lineEdit_6.setEchoMode(QLineEdit.Normal)
        self.lineEdit_6.setCursorPosition(6)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.label_15 = QLabel(self.gridFrame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout_5.addWidget(self.label_15, 5, 1, 1, 1)

        self.label_14 = QLabel(self.gridFrame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(100, 100, 100)")

        self.gridLayout_5.addWidget(self.label_14, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(480, 710, 382, 40))
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(102000, 16777215))
        self.pushButton_6.setBaseSize(QSize(0, 72))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"QPushButton#pushButton_6{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 40; width:250;  position: relative;\n"
"}\n"
"QPushButton#pushButton_6:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 182, 30, 255), stop:1 rgba(255, 112, 10, 255)); color: rgb(255, 255, 255);\n"
"} \n"
"QPushButton#pushButton:pressed {\n"
"background-color: QLinearGradient(x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 200, 30, 255), stop:1 rgba(255, 130, 20, 255));\n"
"color: rgb(255, 255, 255)\n"
"} ")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1010, 620, 191, 40))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(200, 40))
        self.pushButton_3.setBaseSize(QSize(0, 72))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"border-radius: 10;  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(237, 172, 20, 255), stop:1 rgba(255, 102, 0, 255)); color: rgb(253, 253, 253); height: 100; position: relative; width:20;\n"
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
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(895, 620, 111, 31))
        font6 = QFont()
        font6.setFamilies([u"Open Sans"])
        font6.setPointSize(22)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color:rgb(50, 50, 05)")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(690, 620, 200, 40))
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(200, 40))
        self.pushButton_4.setBaseSize(QSize(0, 72))
        self.pushButton_4.setFont(font2)
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
        self.acertoslabel = QLabel(Form)
        self.acertoslabel.setObjectName(u"acertoslabel")
        self.acertoslabel.setGeometry(QRect(890, 555, 251, 66))
        font7 = QFont()
        font7.setFamilies([u"Open Sans"])
        font7.setPointSize(18)
        font7.setBold(False)
        self.acertoslabel.setFont(font7)
        self.acertoslabel.setStyleSheet(u"color:rgb(50, 50, 05)")
        self.acertoslabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notalabel = QLabel(Form)
        self.notalabel.setObjectName(u"notalabel")
        self.notalabel.setGeometry(QRect(1150, 555, 51, 66))
        self.notalabel.setFont(font7)
        self.notalabel.setStyleSheet(u"color:rgb(170, 50, 50)")
        self.notalabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Visualiza\u00e7\u00e3o de Gabaritos", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Escolher Arquivo", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Pesquisa", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Arquivo da avalia\u00e7\u00e3o", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"C:\\Users\\Marco\\OneDrive\\Documentos\\feiradeciencias\\Avalia\u00e7\u00f5es\\Avalia\u00e7\u00e3o Teste.dat", None))
        self.lineEdit_4.setPlaceholderText("")
        self.label_21.setText(QCoreApplication.translate("Form", u"Gabarito", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Propriedades", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"26", None))
        self.lineEdit_5.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"S\u00e9rie", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"Turismo", None))
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"1\u00ba Ano", None))
        self.lineEdit_6.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"N\u00famero de quest\u00f5es", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Curso", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Voltar para Cadastro", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"->", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"1/45", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"<-", None))
        self.acertoslabel.setText(QCoreApplication.translate("Form", u"Nota:", None))
        self.notalabel.setText(QCoreApplication.translate("Form", u"9,0", None))
    # retranslateUi

