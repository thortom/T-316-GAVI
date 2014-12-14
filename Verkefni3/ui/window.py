# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Dec 14 12:40:17 2014
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
        MainWindow.resize(992, 655)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow,\n"
"QAbstractItemView\n"
"{\n"
" color: #EAEAEA;\n"
" background: #5C5C5C;\n"
"}\n"
" \n"
"QComboBox\n"
"{\n"
"   color: #FFFFFF;\n"
"   background-color: #5C5C5C;\n"
"   min-height: 15px;\n"
"   min-width: 60px;\n"
"   max-width: 360px;\n"
"   padding-left: 5px;\n"
"   padding-right: 15px;\n"
"   border-style: solid;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView\n"
"{\n"
"   color: #000000;\n"
"   background-color: #CFCFCF;\n"
"   selection-background-color: #1D1D1D;\n"
"   border-style: solid;\n"
"}\n"
" \n"
"QHeaderView::section\n"
"{\n"
"   color: white;\n"
"   background-color: #7F7F7F;\n"
"   padding-left: 4px;\n"
"   border: 1px solid #6c6c6c;\n"
"}\n"
" \n"
"QTreeView\n"
"{\n"
"   color: #000000;\n"
"   background-color: #B6B6B6;\n"
"   alternate-background-color: #A5A5A5;\n"
"   selection-color: #000000;\n"
"   selection-background-color: #7FB3E6;\n"
"}\n"
" \n"
"QTreeView::branch:item\n"
"{\n"
"   color: #714DFF;\n"
"}\n"
" \n"
"QListView\n"
"{\n"
"   color: #000000;\n"
"   background-color: #D7D7D7;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 731, 381))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 160, 381))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.CountryBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.CountryBox.setObjectName(_fromUtf8("CountryBox"))
        self.verticalLayout.addWidget(self.CountryBox)
        self.listView = QtGui.QListView(self.verticalLayoutWidget)
        self.listView.setAutoFillBackground(False)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.Plot = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Plot.setObjectName(_fromUtf8("Plot"))
        self.verticalLayout.addWidget(self.Plot)
        self.ClearPlot = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ClearPlot.setObjectName(_fromUtf8("ClearPlot"))
        self.verticalLayout.addWidget(self.ClearPlot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Verkefni 3", None))
        self.Plot.setText(_translate("MainWindow", "Plot", None))
        self.ClearPlot.setText(_translate("MainWindow", "Clear Plot", None))

from pyqtgraph import PlotWidget
