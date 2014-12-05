# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Thu Dec  4 16:30:15 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 60, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 160, 103))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_1 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.gridLayout.addWidget(self.comboBox_1, 1, 0, 1, 1)
        self.genTop10 = QtGui.QPushButton(self.gridLayoutWidget)
        self.genTop10.setObjectName(_fromUtf8("genTop10"))
        self.gridLayout.addWidget(self.genTop10, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie lens", None))
        self.genTop10.setText(_translate("MainWindow", "Generate top 10 list", None))

