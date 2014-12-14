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
        self.ui.ClearPlot.clicked.connect(self.ClearPlot_clicked)
        self.ui.Plot.clicked.connect(self.Plot_clicked)
        self.ListCol = []

        self.list = self.ui.listView
        self.initializeDropdowns()
        self.setCheckBoxes()
        self.setInfo()

    def initializeDropdowns(self):
        self.curr.execute("SELECT Distinct country from world_info")
        row = self.curr.fetchall()
        Country = []
        for i in row:
            Country.append(i[0])
        Country.sort()

        catagories = Country
        self.dropdowns = [self.ui.CountryBox]

        for dropdown in self.dropdowns:
            for catagorie in catagories:
                dropdown.addItem(catagorie)

    def findColumns(self):
        columns = []
        self.curr.execute("Select * from world_info LIMIT 0")
        for idx, col in enumerate(self.curr.description):
            print(col[0])
            if col[0] != 'country' and col[0] != 'year':
                self.curr.execute("Select count(%s) from world_info where country = '%s'" %(col[0],self.ui.CountryBox.currentText()))
                rows = self.curr.fetchall()
                if rows[0][0] != 0:
                    columns.append(col[0])
        return columns

    def setCheckBoxes(self):
        self.model = QtGui.QStandardItemModel(self.list)
        self.foods = self.findColumns()
        for food in self.foods:
            self.item = QtGui.QStandardItem(food)
            self.item.setCheckable(True)
            self.model.appendRow(self.item)
        self.list.setModel(self.model)
        self.list.show()

        self.model.itemChanged.connect(self.CheckBox_changed)


    def setInfo(self,left='Value',bottom='Years',x1=1930,x2=2020):
        self.Graph.setLabel('left', left)
        self.Graph.setLabel('bottom', bottom)
        self.Graph.setXRange(x1, x2)
        #self.Graph.setYRange(0, 100)


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

    def ClearPlot_clicked(self):
        self.Graph.clear()

    def Plot_clicked(self):
        print(self.ListCol)
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            print('Col Bitch')
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






        # self.curr.execute("SELECT child_survival_and_health,year from world_info where country = '{}' ORDER BY year ".format(Country))
        # #print(self.curr.fetchall())
        # row = self.curr.fetchall()
        # Data = []
        # Datayear = []
        # for i in row:
        #     Data.append(i[0])
        #     Datayear.append(i[1])

        # print(Data)
        # print(Datayear)



        # self.Graph.plot(Datayear,Data, pen='r')

        # state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(1).checkState()]
        # print(self.model.item(1))
        # if state == 'CHECKED':
        #     self.Graph.plot([0,1,2,3,4,5], [3,2,1,4,5,7], pen='r')
        
        state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(0).checkState()]
        print(self.model.item(0))
        if state == 'CHECKED':
            self.Graph.plot([0,2,4,6,10],[5,1,7,9,7], pen='b')

        #rect = QtGui.QGraphicsRectItem(QtCore.QRectF(1990, 10, 20, 80))
        #rect.setPen(QtGui.QPen(QtGui.QColor(100, 200, 100)))
        #self.Graph.addItem(rect,'green rect')

        # state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(0).checkState()]
        # print(self.model.item(0))
        # if state == 'CHECKED':
        #     self.Graph.plot([0,2,4,6,10],[5,1,7,9,7], pen='b')
