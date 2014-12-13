import sys
import os
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
from ui.window import Ui_MainWindow

def loadUI(mydb):
    app = QtGui.QApplication(sys.argv)  
    window = Main(mydb)
    window.show()
    sys.exit(app.exec_())
    return window

class Main(QtGui.QMainWindow):
    def __init__(self,mydb):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.graphicsView.plot([0,1,2,3,4,5], [3,2,1,4,5,7], pen='r')

        self.ui.checkBox.clicked.connect(self.chb1_clicked)
        self.ui.checkBox_2.clicked.connect(self.chb2_clicked)
        self.ui.checkBox_3.clicked.connect(self.chb3_clicked)

        #app = QtGui.QApplication(sys.argv) 
        #list = QtGui.QListView()
        list = self.ui.listView
        #list.setWindowTitle('Example List')
        #list.setMinimumSize(600, 400)
        model = QtGui.QStandardItemModel(list)
        foods = ['a','b','c']
        for food in foods:
            item = QtGui.QStandardItem(food)
            item.setCheckable(True)
            model.appendRow(item)
        list.setModel(model)
        #list.show()
        #app.exec_()

    def chb1_clicked(self):
        print('clickkk')
        print(self.ui.checkBox.checkState())

    def chb2_clicked(self):
        print('clickkk')
        print(self.ui.checkBox_2.checkState())

    def chb3_clicked(self):
        print('clickkk')
        print(self.ui.checkBox_3.checkState())