# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        fileRunPath = os.path.dirname(__file__)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(fileRunPath + "/resource/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(15, 15, 400, 470))
        self.groupBox.setObjectName("groupBox")
        self.swordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.swordEdit.setGeometry(QtCore.QRect(15, 25, 295, 40))
        self.swordEdit.setPlaceholderText("")
        self.swordEdit.setObjectName("swordEdit")
        self.startSearchWordButton = QtWidgets.QPushButton(self.groupBox)
        self.startSearchWordButton.setGeometry(QtCore.QRect(317, 24, 70, 42))
        self.startSearchWordButton.setAutoDefault(False)
        self.startSearchWordButton.setObjectName("startSearchWordButton")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(15, 75, 370, 327))
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.initButton = QtWidgets.QPushButton(self.groupBox)
        self.initButton.setGeometry(QtCore.QRect(15, 412, 182, 42))
        self.initButton.setObjectName("initButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox)
        self.exitButton.setGeometry(QtCore.QRect(204, 412, 182, 42))
        self.exitButton.setObjectName("exitButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 15, 550, 470))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webView.setGeometry(QtCore.QRect(15, 25, 520, 432))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMG CRAWLING"))
        self.groupBox.setTitle(_translate("MainWindow", "검색"))
        self.startSearchWordButton.setText(_translate("MainWindow", "시작"))
        self.initButton.setText(_translate("MainWindow", "초기화"))
        self.exitButton.setText(_translate("MainWindow", "종료"))
        self.groupBox_2.setTitle(_translate("MainWindow", "미리보기"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
