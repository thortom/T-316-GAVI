import sys
import os
import pandas as pd
import random as r
import numpy as np
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
from ui.window import Ui_MainWindow
import pyqtgraph.examples

def loadUI(mydb):
    app = QtGui.QApplication(sys.argv)  
    window = Main(mydb)
    window.show()
    sys.exit(app.exec_())
    return window

class Main(QtGui.QMainWindow):
    def __init__(self,mydb):
        #pyqtgraph.examples.run()    
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Graph = self.ui.graphicsView
        self.mydb = mydb
        self.curr = self.mydb.cursor
        self.ListCol = []



        self.curr.execute("SELECT Distinct country from world_info")
        row = self.curr.fetchall()
        Country = []
        for i in row:
            Country.append(i[0])
        Country.sort()
        self.Columns = []
        self.curr.execute("Select * from world_info LIMIT 0")
        for idx, col in enumerate(self.curr.description):
            self.Columns.append(col[0])

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
        self.foods = self.Columns
        for food in self.foods:
            self.item = QtGui.QStandardItem(food)
            self.item.setCheckable(True)
            self.model.appendRow(self.item)
        self.list.setModel(self.model)
        self.list.show()

        self.model.itemChanged.connect(self.CheckBox_changed)

        
        self.Graph.setLabel('left', 'Value')
        self.Graph.setLabel('bottom', 'Years')
        self.Graph.setXRange(1960, 2020)
        #self.Graph.setYRange(0, 100)

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
        self.ListCol = []
        while self.model.item(i):
            state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(i).checkState()]
            print(self.model.item(i).text(), state)
            if state == "CHECKED":
                self.ListCol.append(self.model.item(i).text())
            i += 1
    def UnToggleAll(self):
        i = 0
        for food in self.foods:
            self.model.removeColumn(i)
            i += 1
            print(i)
        self.Window()

    def Window(self):
        self.model = QtGui.QStandardItemModel(self.list)
        self.foods = self.Columns
        for food in self.foods:
            self.item = QtGui.QStandardItem(food)
            self.item.setCheckable(True)
            self.model.appendRow(self.item)
        self.list.setModel(self.model)
        self.list.show()

    def ClearPlot_clicked(self):
        self.Graph.clear()
        self.UnToggleAll()


    def Plot_clicked(self):
        print(self.ListCol)
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append('Choose some data')
        else:
            for Col in self.ListCol:
                Data = []
                Datayear = []
                self.curr.execute("SELECT {}, year from world_info where country = '{}' ORDER BY year".format(Col, Country))
                row = self.curr.fetchall()
                for i in row:
                    Data.append(i[0])
                    Datayear.append(i[1])
                print(Data)
                print(Datayear)
                count = 0
                for i in Data:
                    if i == None:
                        Data[count] = np.nan
                    count += 1
                print(Data)
                print(self.list)
                c1 = r.randint(0,260)
                c2 = r.randint(0,260)
                c3 = r.randint(0,260)
                self.Graph.plot(Datayear,Data, pen = pg.mkPen(color = (c1,c2,c3),width = 3))