# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec 13 14:57:07 2014
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 180, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 250, 127, 80))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 290, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 420, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(390, 70, 256, 192))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Verkefni 3", None))
        self.label.setText(_translate("MainWindow", "Wazup bitches", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

from pyqtgraph import PlotWidget
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec 13 15:10:22 2014
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 561, 271))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 420, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Verkefni 3", None))

from pyqtgraph import PlotWidget
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec 13 15:18:43 2014
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 731, 311))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 111, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout.addWidget(self.checkBox_5)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 130, 91, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
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
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox", None))

from pyqtgraph import PlotWidget
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec 13 16:45:33 2014
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 731, 311))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 111, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout.addWidget(self.checkBox_5)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 130, 91, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(200, 390, 256, 192))
        self.treeView.setObjectName(_fromUtf8("treeView"))
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
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox", None))

from pyqtgraph import PlotWidget
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Dec 13 17:13:37 2014
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 731, 311))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 111, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout.addWidget(self.checkBox_5)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 130, 91, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(510, 390, 256, 192))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 390, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
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
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox", None))

from pyqtgraph import PlotWidget
