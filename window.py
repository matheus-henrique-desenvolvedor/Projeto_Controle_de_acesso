# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(395, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 50, 201, 51))
        font = QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.pushButtonValidate = QPushButton(self.tab)
        self.pushButtonValidate.setObjectName(u"pushButtonValidate")
        self.pushButtonValidate.setGeometry(QRect(90, 410, 171, 101))
        self.pushButtonValidate.setFont(font)
        self.label_video = QLabel(self.tab)
        self.label_video.setObjectName(u"label_video")
        self.label_video.setGeometry(QRect(40, 160, 281, 211))
        self.label_video.setStyleSheet(u"border-color: rgb(172, 172, 172);\n"
"background-color: rgb(208, 208, 208);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 111, 16))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 261, 121))
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 360, 51, 20))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 330, 71, 20))
        self.inputCep = QLineEdit(self.tab_2)
        self.inputCep.setObjectName(u"inputCep")
        self.inputCep.setGeometry(QRect(150, 300, 131, 20))
        self.lineName = QLineEdit(self.tab_2)
        self.lineName.setObjectName(u"lineName")
        self.lineName.setGeometry(QRect(150, 210, 131, 20))
        self.inputFone = QLineEdit(self.tab_2)
        self.inputFone.setObjectName(u"inputFone")
        self.inputFone.setGeometry(QRect(150, 330, 131, 20))
        self.btRegister = QPushButton(self.tab_2)
        self.btRegister.setObjectName(u"btRegister")
        self.btRegister.setGeometry(QRect(150, 450, 75, 23))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 300, 71, 20))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 210, 91, 20))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 270, 51, 20))
        self.inputCpf = QLineEdit(self.tab_2)
        self.inputCpf.setObjectName(u"inputCpf")
        self.inputCpf.setGeometry(QRect(150, 270, 131, 20))
        self.dateEdit = QDateEdit(self.tab_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(150, 240, 131, 22))
        self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(150, 360, 82, 17))
        self.radioButton_2 = QRadioButton(self.tab_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(220, 360, 82, 17))
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 395, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Validar QR code</p></body></html>", None))
        self.pushButtonValidate.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label_video.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Valida\u00e7\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Data de nascimento:</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastrar aluno no</p><p align=\"center\">sistemas</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Genero:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Telefone:</p></body></html>", None))
        self.inputCep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000-000", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu nome", None))
        self.inputFone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00000-0000", None))
        self.btRegister.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">CEP:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Nome:</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">CPF:</p></body></html>", None))
        self.inputCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Menino", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Menina", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
    # retranslateUi

