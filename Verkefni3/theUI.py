import sys
import os
import pandas as pd
import random as r
import numpy as np
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
from ui.window import Ui_MainWindow
import pyqtgraph.examples
import re
import math

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
        self.ui.ScatterPlot.clicked.connect(self.ScatterPlot_clicked)
        self.ui.Plot.clicked.connect(self.Plot_clicked)
        self.ListCol = []
        # self.legend = pg.LegendItem((100,60), (60,10))
        # self.legend.setParentItem(self.Graph.graphicsItem())
        self.list = self.ui.listView
        self.initializeDropdowns()
        self.setCheckBoxes()
        self.setInfo()

        self.ui.CountryBox.currentIndexChanged.connect(self.setCheckBoxes)
        
        self.ui.beer_btn.clicked.connect(self.print_stats)

    def initializeDropdowns(self):
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

        catagories = Country
        self.dropdowns = [self.ui.CountryBox]

        for dropdown in self.dropdowns:
            for catagorie in catagories:
                dropdown.addItem(catagorie)

    def findColumns(self):
        columns = []
        self.curr.execute("Select * from world_info LIMIT 0")
        for idx, col in enumerate(self.curr.description):
            if col[0] != 'country' and col[0] != 'year':
                self.curr.execute("Select count(%s) from world_info where country = '%s'" %(col[0],self.ui.CountryBox.currentText()))
                rows = self.curr.fetchall()
                # Use only data when 3 or more data points are available
                if rows[0][0] >= 3:
                    columns.append(col[0])
        return columns

    def getLabelForCheck(self, checkItem):
        # TODO:
        s = "select series_code_text from lable where series_code='%s'" %checkItem.replace('_','.').upper()
        # print('s',s)
        self.curr.execute(s)
        text = self.curr.fetchone()
        ret = 'none'
        for item in text:
            ret = item
        return ret


    def setCheckBoxes(self):
        self.model = QtGui.QStandardItemModel(self.list)
        self.foods = self.findColumns()
        # print('foods: ', self.foods)
        checkBoxText = []
        for food in self.foods:
            checkBox = self.getLabelForCheck(food)
            # TODO: check if text was found
            # if checkBox == 'none':
            #     continue
            checkBoxText.append(checkBox)
        # Sort in alphabetical order
        checkBoxText.sort()
        for checkBox in checkBoxText:
            self.item = QtGui.QStandardItem(checkBox)
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

    def CheckBox_changed(self, item):
        i = 0
        self.ListCol = []
        while self.model.item(i):
            state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(i).checkState()]
            if state == "CHECKED":
                self.ListCol.append(self.model.item(i).text())
            i += 1

    def UnToggleAll(self):
        i = 0
        while self.model.item(i):
            state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(i).checkState()]
            if state == "CHECKED":
                self.model.item(i).setCheckState(QtCore.Qt.Unchecked)
            i += 1

    def ClearPlot_clicked(self):
        self.Graph.clear()
        self.UnToggleAll()
        self.Graph.clear()

    def getNameOfCol(self, checkBoxText):
        s = "select series_code from lable where series_code_text='%s'" %checkBoxText.replace("'","''")
        self.curr.execute(s)
        nameOfCol = self.curr.fetchone()[0]
        nameOfCol = nameOfCol.replace('.','_').lower()
        return nameOfCol

    def Plot_clicked(self):
        # print(self.ListCol)
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append('Choose some data')
        else:
            for Col in self.ListCol:
                Data = []
                Datayear = []
                nameOfCol = self.getNameOfCol(Col)
                s = "SELECT {}, year from world_info where country = '{}' ORDER BY year".format(nameOfCol, Country)
                self.curr.execute(s)
                row = self.curr.fetchall()
                for i in row:
                    Data.append(i[0])
                    Datayear.append(i[1])
                # print(Data)
                # print(Datayear)
                count = 0
                for i in Data:
                    if i == None:
                        Data[count] = np.nan
                    count += 1
                # print(Data)
                # print(self.list)
                c1 = r.randint(20,255)
                c2 = r.randint(20,255)
                c3 = r.randint(20,255)

                s = self.Graph.plot(Datayear,Data, pen = pg.mkPen(color = (c1,c2,c3),width = 3))
                self.Graph.enableAutoRange(axis = None, enable = True, x = None, y = None)


    def ScatterPlot_clicked(self):
        # print(dir(self.Graph))
        # print(self.ListCol)
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append('Choose some data')
        else:
            for Col in self.ListCol:
                Data = []
                Datayear = []
                nameOfCol = self.getNameOfCol(Col)
                self.curr.execute("SELECT {}, year from world_info where country = '{}' ORDER BY year".format(nameOfCol, Country))
                row = self.curr.fetchall()
                for i in row:
                    Data.append(i[0])
                    Datayear.append(i[1])
                # print(Data)
                # print(Datayear)
                count = 0
                for i in Data:
                    if i == None:
                        Data[count] = np.nan
                    count += 1
                # print(Data)
                # print(self.list)
                c1 = r.randint(20,255)
                c2 = r.randint(20,255)
                c3 = r.randint(20,255)

                s = pg.ScatterPlotItem(Datayear, Data, pen = pg.mkPen(color = (c1,c2,c3),width = 3))
                self.Graph.addItem(s)
                self.Graph.enableAutoRange(axis = None, enable = True, x = None, y = None)

    def print_stats(self):
        print('yoyo')
        command = "Select %s from world_info where %s = '%s'"
        cat = 'SP.DYN.LE00.MA.IN'.replace('.','_')
        print(cat)
        print(command)
        self.curr.execute(command %(cat,"country",str(self.ui.CountryBox.currentText())))
        rows = self.curr.fetchall()
        #print(rows)
        data = []
        years = []
        yearBefore = None
        for i, row in enumerate(rows):
            row = row[0]
            if yearBefore is None:
                yearBefore = row
            if row is not None:
                data.append([row, round((row/yearBefore-1)*100,2)])
                years.append(1960+i)
            yearBefore = row
        print('data', data)
        data = pd.DataFrame(data, columns=['DataValue', 'IncrEachYear%'], index=years)
        print(data)
