# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 662)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 50, 851, 531))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.Practice = QtWidgets.QWidget()
        self.Practice.setObjectName("Practice")
        self.plainTextEdit_manualEnter = QtWidgets.QPlainTextEdit(self.Practice)
        self.plainTextEdit_manualEnter.setGeometry(QtCore.QRect(0, 410, 751, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_manualEnter.setFont(font)
        self.plainTextEdit_manualEnter.setMouseTracking(True)
        self.plainTextEdit_manualEnter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_manualEnter.setTabChangesFocus(True)
        self.plainTextEdit_manualEnter.setObjectName("plainTextEdit_manualEnter")
        self.plainTextEdit_English = QtWidgets.QPlainTextEdit(self.Practice)
        self.plainTextEdit_English.setGeometry(QtCore.QRect(0, 460, 751, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_English.setFont(font)
        self.plainTextEdit_English.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_English.setAutoFillBackground(True)
        self.plainTextEdit_English.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.plainTextEdit_English.setUndoRedoEnabled(False)
        self.plainTextEdit_English.setReadOnly(True)
        self.plainTextEdit_English.setObjectName("plainTextEdit_English")
        self.plainTextEdit_Chinese = QtWidgets.QPlainTextEdit(self.Practice)
        self.plainTextEdit_Chinese.setGeometry(QtCore.QRect(0, 0, 751, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_Chinese.setFont(font)
        self.plainTextEdit_Chinese.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_Chinese.setAutoFillBackground(True)
        self.plainTextEdit_Chinese.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.plainTextEdit_Chinese.setUndoRedoEnabled(False)
        self.plainTextEdit_Chinese.setReadOnly(True)
        self.plainTextEdit_Chinese.setObjectName("plainTextEdit_Chinese")
        self.pushButton_submit = QtWidgets.QPushButton(self.Practice)
        self.pushButton_submit.setGeometry(QtCore.QRect(760, 380, 75, 23))
        self.pushButton_submit.setAutoDefault(True)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_Prev = QtWidgets.QPushButton(self.Practice)
        self.pushButton_Prev.setGeometry(QtCore.QRect(760, 280, 75, 23))
        self.pushButton_Prev.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Prev.setAutoDefault(True)
        self.pushButton_Prev.setObjectName("pushButton_Prev")
        self.pushButton_Next = QtWidgets.QPushButton(self.Practice)
        self.pushButton_Next.setGeometry(QtCore.QRect(760, 330, 75, 23))
        self.pushButton_Next.setAutoDefault(True)
        self.pushButton_Next.setObjectName("pushButton_Next")
        self.plainTextEdit_CN_line = QtWidgets.QPlainTextEdit(self.Practice)
        self.plainTextEdit_CN_line.setGeometry(QtCore.QRect(0, 370, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_CN_line.setFont(font)
        self.plainTextEdit_CN_line.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_CN_line.setAutoFillBackground(True)
        self.plainTextEdit_CN_line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.plainTextEdit_CN_line.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_CN_line.setUndoRedoEnabled(False)
        self.plainTextEdit_CN_line.setReadOnly(True)
        self.plainTextEdit_CN_line.setObjectName("plainTextEdit_CN_line")
        self.label_English_Line_Number = QtWidgets.QLabel(self.Practice)
        self.label_English_Line_Number.setGeometry(QtCore.QRect(760, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_English_Line_Number.setFont(font)
        self.label_English_Line_Number.setObjectName("label_English_Line_Number")
        self.lineEdit_English_Line_Number = QtWidgets.QLineEdit(self.Practice)
        self.lineEdit_English_Line_Number.setGeometry(QtCore.QRect(760, 240, 71, 20))
        self.lineEdit_English_Line_Number.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_English_Line_Number.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_English_Line_Number.setObjectName("lineEdit_English_Line_Number")
        self.tabWidget.addTab(self.Practice, "")
        self.Config = QtWidgets.QWidget()
        self.Config.setObjectName("Config")
        self.label_Chinese_File = QtWidgets.QLabel(self.Config)
        self.label_Chinese_File.setGeometry(QtCore.QRect(20, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Chinese_File.setFont(font)
        self.label_Chinese_File.setObjectName("label_Chinese_File")
        self.lineEdit_Chinese_File = QtWidgets.QLineEdit(self.Config)
        self.lineEdit_Chinese_File.setGeometry(QtCore.QRect(170, 60, 371, 21))
        self.lineEdit_Chinese_File.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_Chinese_File.setObjectName("lineEdit_Chinese_File")
        self.pushButton_openChineseText = QtWidgets.QPushButton(self.Config)
        self.pushButton_openChineseText.setGeometry(QtCore.QRect(550, 60, 75, 23))
        self.pushButton_openChineseText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_openChineseText.setObjectName("pushButton_openChineseText")
        self.lineEdit_English_File = QtWidgets.QLineEdit(self.Config)
        self.lineEdit_English_File.setGeometry(QtCore.QRect(170, 130, 371, 21))
        self.lineEdit_English_File.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_English_File.setObjectName("lineEdit_English_File")
        self.label_English_File = QtWidgets.QLabel(self.Config)
        self.label_English_File.setGeometry(QtCore.QRect(20, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_English_File.setFont(font)
        self.label_English_File.setObjectName("label_English_File")
        self.pushButton_openEnglishText = QtWidgets.QPushButton(self.Config)
        self.pushButton_openEnglishText.setGeometry(QtCore.QRect(550, 130, 75, 23))
        self.pushButton_openEnglishText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_openEnglishText.setObjectName("pushButton_openEnglishText")
        self.tabWidget.addTab(self.Config, "")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(810, 590, 75, 23))
        self.pushButton_Exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_Exit.setAutoDefault(True)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.plainTextEdit_manualEnter, self.pushButton_submit)
        MainWindow.setTabOrder(self.pushButton_submit, self.pushButton_Next)
        MainWindow.setTabOrder(self.pushButton_Next, self.lineEdit_Chinese_File)
        MainWindow.setTabOrder(self.lineEdit_Chinese_File, self.pushButton_openChineseText)
        MainWindow.setTabOrder(self.pushButton_openChineseText, self.lineEdit_English_File)
        MainWindow.setTabOrder(self.lineEdit_English_File, self.pushButton_openEnglishText)
        MainWindow.setTabOrder(self.pushButton_openEnglishText, self.pushButton_Prev)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TransBuddy"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_Prev.setText(_translate("MainWindow", "Pre"))
        self.pushButton_Next.setText(_translate("MainWindow", "Next"))
        self.label_English_Line_Number.setText(_translate("MainWindow", " Go to Line:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Practice), _translate("MainWindow", "Practise"))
        self.label_Chinese_File.setText(_translate("MainWindow", "Translate From"))
        self.pushButton_openChineseText.setText(_translate("MainWindow", "Open"))
        self.label_English_File.setText(_translate("MainWindow", "Translate To"))
        self.pushButton_openEnglishText.setText(_translate("MainWindow", "Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Config), _translate("MainWindow", "Config"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))


