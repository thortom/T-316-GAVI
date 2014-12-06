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


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec  6 18:22:53 2014
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
        MainWindow.resize(632, 521)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 60, 291, 381))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 161, 103))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.genTop10 = QtGui.QPushButton(self.gridLayoutWidget)
        self.genTop10.setObjectName(_fromUtf8("genTop10"))
        self.gridLayout.addWidget(self.genTop10, 5, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(0, _fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.comboBox_1 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.setItemText(0, _fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_1, 2, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(0, _fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 21))
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
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Action", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Adventure", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Animation", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Children\'s", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Comedy", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Crime", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Documentary", None))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Drama", None))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Fantasy", None))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Film-Noir", None))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Horror", None))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Musical", None))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Mystery", None))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Romance", None))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Sci-fi", None))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Thriller", None))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "War", None))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Western", None))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Action", None))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Adventure", None))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "Animation", None))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "Children\'s", None))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "Comedy", None))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "Crime", None))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "Documentary", None))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "Drama", None))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "Fantasy", None))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "Film-Noir", None))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "Horror", None))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "Musical", None))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "Mystery", None))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "Romance", None))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "Sci-fi", None))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "Thriller", None))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "War", None))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "Western", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Action", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Adventure", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Animation", None))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Children\'s", None))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Comedy", None))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Crime", None))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Documentary", None))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Drama", None))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Fantasy", None))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Film-Noir", None))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Horror", None))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Musical", None))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Mystery", None))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Romance", None))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "Sci-fi", None))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "Thriller", None))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "War", None))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "Western", None))

