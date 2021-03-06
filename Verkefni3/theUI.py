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
from collections import Counter
import os.path

def loadUI(mydb, importer):
    app = QtGui.QApplication(sys.argv)  
    window = Main(mydb,importer)
    window.show()
    sys.exit(app.exec_())
    return window

class Main(QtGui.QMainWindow):
    def __init__(self,mydb, importer):
        QtGui.QMainWindow.__init__(self)
        self.importer = importer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Graph = self.ui.graphicsView
        self.mydb = mydb
        self.curr = self.mydb.cursor
        self.ui.ClearPlot.clicked.connect(self.ClearPlot_clicked)
        self.ui.ScatterPlot.clicked.connect(self.ScatterPlot_clicked)
        self.ui.Plot.clicked.connect(self.Plot_clicked)
        self.ui.Trendline.clicked.connect(self.Trendline_clicked)
        self.ui.Add_data_btn.clicked.connect(self.Add_data_btn_clicked)
        self.ListCol = []
        self.list = self.ui.listView
        self.initializeDropdowns()
        self.initializeTopList()
        self.setCheckBoxes()
        self.setInfo()

        self.ui.CountryBox.currentIndexChanged.connect(self.setCheckBoxes)
        
        self.ui.beer_btn.clicked.connect(self.print_stats)
        self.ui.toplist_pb.clicked.connect(self.topList)
        self.ui.toplist_pb_2.clicked.connect(self.getTopCountryList)

        self.lastChecked = None

    def initializeTopList(self):
        self.curr.execute("Select distinct year from world_info order by year desc")
        rows = self.curr.fetchall()
        for row in rows:
            self.ui.toplist_cb.addItem(str(row[0]))

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
            for catagory in catagories:
                dropdown.addItem(catagory)

    def getLabelForCheck(self, checkItem):
        s = "select series_code_text from notes where series_code='%s'" %checkItem
        self.curr.execute(s)
        text = self.curr.fetchone()
        if text is None:
            text = checkItem
        elif text is not None:
            text = text[0]
        return text


    def setCheckBoxes(self):
        self.model = QtGui.QStandardItemModel(self.list)
        s = '''select series, count(value)
                from world_info
                where country='%s'
                group by series''' %self.ui.CountryBox.currentText()
        self.curr.execute(s)
        rows = self.curr.fetchall()
        checkBoxText = []
        for row in rows:
            series = row[0]
            value = row[1]
            if value >= 3:
                checkBox = self.getLabelForCheck(series)
                checkBoxText.append(checkBox)

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

    def CheckBox_changed(self, item):
        i = 0
        
        newListCol = []
        while self.model.item(i):
            state = ['UNCHECKED', 'TRISTATE',  'CHECKED'][self.model.item(i).checkState()]
            if state == "CHECKED":
                newListCol.append(self.model.item(i).text())
                if self.model.item(i).text() not in self.ListCol:
                    self.lastChecked = self.model.item(i).text()
            i += 1

        self.ListCol = newListCol

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
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser.clear()

    def getNameOfCol(self, checkBoxText):
        s = "select series_code from notes where series_code_text='%s'" %checkBoxText.replace("'","''")
        self.curr.execute(s)
        try:
            nameOfCol = self.curr.fetchone()[0]
        except:
            nameOfCol = checkBoxText
        return nameOfCol

    def PrintCheckBox(self, Col):
        Data2 = []
        Data3 = []

        s2 = "SELECT description from notes where series_code_text = '{}';".format(Col.replace("'","''"))

        self.ui.textBrowser.clear()
        self.ui.textBrowser.append(Col + ': \n')

        self.curr.execute(s2)
        row2 = self.curr.fetchall()
        for i in row2:
            self.ui.textBrowser.append(i[0])

    def Plot(self, Col, Country):
        Data = []
        Datayear = []
        nameOfCol = self.getNameOfCol(Col)
        s = "SELECT value, year from world_info where series = '{}' and country = '{}' ORDER BY year".format(nameOfCol, Country)
        self.curr.execute(s)
        row = self.curr.fetchall()
        for i in row:
            Data.append(i[0])
            Datayear.append(i[1])
        count = 0
        for i in Data:
            if i == None:
                Data[count] = np.nan
            count += 1
        c1 = r.randint(20,255)
        c2 = r.randint(20,255)
        c3 = r.randint(20,255)
        return c1,c2,c3,Data,Datayear

    def Plot_clicked(self):
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.No_Data()
        else:
            for Col in self.ListCol:
                c1,c2,c3,Data,Datayear = self.Plot(Col,Country)
                s = self.Graph.plot(Datayear,Data, pen = pg.mkPen(color = (c1,c2,c3),width = 3))
                self.Graph.enableAutoRange(axis = None, enable = True, x = None, y = None)
                self.Add_legend(c1,c2,c3,Country,Col)
                self.PrintCheckBox(Col)

    def ScatterPlot_clicked(self):
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.No_Data()
        else:
            for Col in self.ListCol:
                c1,c2,c3,Data,Datayear = self.Plot(Col,Country)
                s = pg.ScatterPlotItem(Datayear, Data, pen = pg.mkPen(color = (c1,c2,c3),width = 3))
                self.Graph.addItem(s)
                self.Graph.enableAutoRange(axis = None, enable = True, x = None, y = None)
                self.Add_legend(c1,c2,c3,Country,Col)
                self.PrintCheckBox(Col)

    def Trendline_clicked(self):
        Country = str(self.ui.CountryBox.currentText())
        if not self.ListCol:
            self.No_Data()
        else:
            for Col in self.ListCol:
                c1,c2,c3,Data,Datayear = self.Plot(Col,Country)
                def Least_Squares(Datayear,Data):
                    Yearsfixed = []
                    Datafixed = []
                    s=0
                    for i in Data:
                        if not math.isnan(i):
                            Yearsfixed.append(Datayear[s])
                            Datafixed.append(i)
                            s+=1
                        if math.isnan(i):
                            s+=1
                    A = np.vstack([Yearsfixed, np.ones(len(Yearsfixed))]).T
                    w = np.linalg.lstsq(A,Datafixed)[0]
                    year_np = np.array(Yearsfixed)
                    line = w[0]*year_np + w[1]
                    return Yearsfixed,line,w
                Yearsfixed,line,w = Least_Squares(Datayear,Data)
                s = self.Graph.plot(Yearsfixed,line, pen = pg.mkPen(color = (c1,c2,c3), width = 1, style = QtCore.Qt.DashLine))
                self.Graph.enableAutoRange(axis = None, enable = True, x = None, y = None)
                self.Add_legend(c1,c2,c3,Country,Col)
                self.PrintCheckBox(Col)

    def Add_data_btn_clicked(self):
        fileName = self.ui.Filepath.text()
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append('Locating new data')
        if not os.path.exists(fileName):
            self.ui.textBrowser.append('Invalid filepath')
        elif os.path.exists(fileName):
            self.ui.textBrowser.append('Data located')
            self.importer.addData(fileName)

    def Add_legend(self, c1,c2,c3,Country, Col):
        Legend = Country + "," + Col
        Color = QtGui.QColor(c1,c2,c3)
        self.ui.textBrowser_2.setTextColor(Color)
        self.ui.textBrowser_2.append(Legend)

    def print_stats(self):
        if self.lastChecked is not None:
            nameOfCol = self.getNameOfCol(self.lastChecked)
            command = "Select value from world_info where series='%s' and country = '%s'" %(nameOfCol,str(self.ui.CountryBox.currentText()))
            self.curr.execute(command)
            rows = self.curr.fetchall()
            
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
            data = pd.DataFrame(data, columns=['DataValue', 'IncrEachYear%'], index=years)
            print(data)
        else:
            self.No_Data()
        
    def topList(self):
        if self.lastChecked != None:
            selectedCountry = str(self.ui.CountryBox.currentText())
            col = self.lastChecked
            code = self.getNameOfCol(col)
            year = str(self.ui.toplist_cb.currentText())
            order = str(self.ui.toplist_cb2.currentText())
            
            command ="""select country, value
                        from world_info
                        where series='%s' and year=%s
                        order by value %s
                        """ %(code, year, order)

            self.curr.execute(command)
            rows = self.curr.fetchall()

            string ="Rank\tCountry\t%s\n"%(col)
            for idx, row in enumerate(rows):
                # print('row', row)
                country = row[0]
                value = round(float(row[1]),1)
                if idx < 10 or country == selectedCountry:
                    string += str(idx+1)+'\t'+str(country)+'\t\t\t'+str(value)+'\n'
            # print(string)
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append(string)
        else:
            self.No_Data()

    def No_Data(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append('Choose some data')

    def getTopCountryList(self, year):
        self.getGradingItems()
        year = str(self.ui.toplist_cb.currentText())

        countryList = {}
        for key, value in self.gradingItems.items():
            tempCountryList = self.getRatingListForCountry(key, year)
            if tempCountryList is None:
                # Skip this catagory if data is missing
                continue
            for key2, value2 in tempCountryList.items():
                tempCountryList[key2] = tempCountryList.get(key2)*value2*0.1
                countryList[key2] = countryList.get(key2, 0)+tempCountryList[key2]

        listToCount = Counter(countryList)
        top = listToCount.most_common(10)

        self.ui.textBrowser.clear()
        self.ui.textBrowser.append('---------------------'+year+'----------------------')
        self.ui.textBrowser.append('Country:\t\tRating:')
        self.ui.textBrowser.append('-------------------------------------------------')
        for country in top:
            tab = 20 - len(country[0])
            text = country[0] + '\t\t' + str(round(country[1], 4))
            self.ui.textBrowser.append(text)

        self.ui.textBrowser.append('\n\nThis list was rated by:')
        for key, value in self.gradingItems.items():
            keyText = self.getLabelForCheck(key)
            self.ui.textBrowser.append(keyText)


    def getRatingListForCountry(self, key, year):
        try:
            self.curr.execute('''select country, value/(
                                                        select max(value)
                                                        from world_info
                                                        where series='%s' and year=%s) as grade
                                from world_info
                                where series='%s' and year=%s
                                order by grade''' %(key, year, key, year))
        except:
            print('Missing data for: ', self.getLabelForCheck(key))
            # self.ui.textBrowser.append('Missing data for data: ' + self.getLabelForCheck(key))
            return None
        rows = self.curr.fetchall()
        ratingList = {}
        for row in rows:
            # print('row', row)
            country = row[0]
            grade = row[1]
            try:
                ratingList[country] = float(grade)
            except TypeError:
                ratingList[country] = 0.0                           # TODO: maybe not use half rating

        return ratingList


    def getGradingItems(self):
        '''
        "Health expenditure, total (% of GDP)";"SH.XPD.TOTL.ZS"
        "Long-term unemployment (% of total unemployment)";"SL.UEM.LTRM.ZS"
        "Mortality rate, infant (per 1,000 live births)";"SP.DYN.IMRT.IN"
        "Public spending on education, total (% of GDP)";"SE.XPD.TOTL.GD.ZS"
        "Strength of legal rights index (0=weak to 12=strong)";"IC.LGL.CRED.XQ"
        "Tax revenue (% of GDP)";"GC.TAX.TOTL.GD.ZS"
        "Unemployment, total (% of total labor force) (national estimate)";"SL.UEM.TOTL.NE.ZS"
        "Electric power consumption (kWh per capita)";"EG.USE.ELEC.KH.PC"
        "Life expectancy at birth, total (years)";"SP.DYN.LE00.IN"
        "Internet users (per 100 people)";"IT.NET.USER.P2"
        '''

        self.gradingItems = {}
        if len(self.ListCol) > 0:
            for item in self.ListCol:
                column = self.getNameOfCol(item)
                self.gradingItems[column] = 1                           # TODO: get true value from user +/-
        else:
            self.gradingItems = {"EG.USE.ELEC.KH.PC": 1, "SP.DYN.LE00.IN": 1, "SH.XPD.TOTL.ZS": 1,
                                "SL.UEM.LTRM.ZS": -1, "SP.DYN.IMRT.IN": -1, "SE.XPD.TOTL.GD.ZS": 1, "IC.LGL.CRED.XQ": 1,
                                "GC.TAX.TOTL.GD.ZS": 1, "SL.UEM.TOTL.NE.ZS": -1, "IT.NET.USER.P2": 1}

        
