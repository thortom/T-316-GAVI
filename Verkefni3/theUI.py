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
        self.Graph = self.ui.graphicsView

        self.mydb = mydb
        self.curr = self.mydb.cursor

        self.curr.execute("SELECT Distinct country from world_info")
        row = self.curr.fetchall()
        Country = []
        for i in row:
            Country.append(i[0])
        Country.sort()

        self.ui.ClearPlot.clicked.connect(self.ClearPlot_clicked)
        self.ui.Plot.clicked.connect(self.Plot_clicked)
        catagories = Country #["Pick Country","Iceland", "Denmark", "Sweden", "Norway", "Penis"]
        self.dropdowns = [self.ui.CountryBox]

        for dropdown in self.dropdowns:
            for catagorie in catagories:
                dropdown.addItem(catagorie)

        # self.ui.checkBox.clicked.connect(self.chb1_clicked)
        # self.ui.checkBox_2.clicked.connect(self.chb2_clicked)
        # self.ui.checkBox_3.clicked.connect(self.chb3_clicked)

        #app = QtGui.QApplication(sys.argv) 
        #list = QtGui.QListView()
        self.list = self.ui.listView
        #list.setWindowTitle('Example List')
        #list.setMinimumSize(600, 400)
        self.model = QtGui.QStandardItemModel(self.list)
        self.foods = ['GDP','School Enrollment','c']
        for food in self.foods:
            self.item = QtGui.QStandardItem(food)
            self.item.setCheckable(True)
            self.model.appendRow(self.item)
        self.list.setModel(self.model)
        self.list.show()

        self.model.itemChanged.connect(self.CheckBox_changed)

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

    def CheckBox_changed(self, item):
        i = 0
        while self.model.item(i):
            state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(i).checkState()]
            print(self.model.item(i).text(), state)
            i += 1

    def ClearPlot_clicked(self):
        self.Graph.clear()

    def Plot_clicked(self):

        Country = str(self.ui.CountryBox.currentText())
        self.curr.execute("SELECT child_survival_and_health from world_info where country = '{}' ".format(Country))
        print(self.curr.fetchall())
        state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(1).checkState()]
        print(self.model.item(1))
        if state == 'CHECKED':
            self.Graph.plot([0,1,2,3,4,5], [3,2,1,4,5,7], pen='r')
        
        state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(0).checkState()]
        print(self.model.item(0))
        if state == 'CHECKED':
            self.Graph.plot([0,2,4,6,10],[5,1,7,9,7], pen='b')