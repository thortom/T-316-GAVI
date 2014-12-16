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
            #print('year:',row[0])
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
        s = "select series_code from lable where series_code_text='%s'" %checkBoxText.replace("'","''")
        self.curr.execute(s)
        nameOfCol = self.curr.fetchone()[0]
        nameOfCol = nameOfCol.replace('.','_').lower()
        return nameOfCol

    def PrintCheckBox(self, Col):
        Data2 = []
        Data3 = []

        s2 = "SELECT description from lable where series_code_text = '{}';".format(Col.replace("'","''"))
        s3 = "SELECT series_code_text from lable where series_code_text = '{}';".format(Col.replace("'","''"))

        self.curr.execute(s2)
        row2 = self.curr.fetchall()
        for i in row2:
            Data2.append(i[0])

        self.curr.execute(s3)
        row3 = self.curr.fetchall()
        for i in row3:
            Data3.append(i[0])

        self.ui.textBrowser.clear()
        self.ui.textBrowser.append(Data3[0] + ': \n')
        self.ui.textBrowser.append(Data2[0])

    def Plot(self, Col, Country):
        Data = []
        Datayear = []
        nameOfCol = self.getNameOfCol(Col)
        s = "SELECT {}, year from world_info where country = '{}' ORDER BY year".format(nameOfCol, Country)
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
                #print(Yearsfixed)
                #print(Datafixed)
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
        path = self.ui.Filepath.text()
        print(path)

    def Add_legend(self, c1,c2,c3,Country, Col):
        Legend = Country + "," + Col
        Color = QtGui.QColor(c1,c2,c3)
        self.ui.textBrowser_2.setTextColor(Color)
        self.ui.textBrowser_2.append(Legend)

    def print_stats(self):
        if self.lastChecked is not None:
            nameOfCol = self.getNameOfCol(self.lastChecked)
            command = "Select %s from world_info where country = '%s'" %(nameOfCol,str(self.ui.CountryBox.currentText()))
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

    def rank(self):
        if self.lastChecked is not None:
            selectedCountry = str(self.ui.CountryBox.currentText())
            col = self.lastChecked
            code = self.getNameOfCol(col)
            year = self.ui.toplist_cb.currentText()
            #command = "Select %s from world_info where %s = '%s'"
            #print('selectedCountry',selectedCountry)
            #print('lastChecked',col)
            #print('code', code)

            ##Get 2014 life expects

            valueOfSelected = 70

            command = "SELECT DISTINCT country from world_info where country != '%s' and %s > %s and year = 2014" %(selectedCountry,code,valueOfSelected)
            self.curr.execute(command)
            rows = self.curr.fetchall()
            for row in rows:
                print(row[0])
            #print('number of countries:',x)
        
    def topList(self):
        if self.lastChecked != None:
            selectedCountry = str(self.ui.CountryBox.currentText())
            col = self.lastChecked
            code = self.getNameOfCol(col)
            year = str(self.ui.toplist_cb.currentText())
            order = str(self.ui.toplist_cb2.currentText())

            #print('selectedCountry',selectedCountry)
            #print('lastChecked',col)
            #print('code', code)
            #print('year', year)
            
            command ="""
            Create view tempTopList as (select rank() over (order by %s desc) as rank, country, %s
            from world_info
            where year = %s
            and %s is not null
            order by %s %s);

            (select rank, country, %s
            from tempTopList
            limit 10)
            union
            (select rank, country, %s
            from tempTopList
            where country = '%s')
            order by %s %s""" %(code,code,year,code,code,order,code,code,selectedCountry,code,order)

            self.curr.execute(command)
            rows = self.curr.fetchall()
            self.curr.execute("drop view tempTopList")

            string ="Rank\t%s\tCountry\n"%(col)
            for row in rows:
                string += str(row[0])+'\t'+str(round(float(row[2]),1))+'\t\t\t'+str(row[1])+'\n'
            print(string)
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
            self.curr.execute('''select * from
                                    (select country, "%s"/(SELECT max(ta."%s")
                                                                                FROM world_info as ta
                                                                                where ta.year=tb.year
                                                                        ) as grade
                                        from world_info as tb
                                        where tb.year=%s
                                        order by "%s" desc
                                    ) as temp
                                order by grade desc''' %(key, key, year, key))
        except:
            print('Missing data for: ', self.getLabelForCheck(key))
            # self.ui.textBrowser.append('Missing data for data: ' + self.getLabelForCheck(key))
            return None
        rows = self.curr.fetchall()
        ratingList = {}
        for row in rows:
            country = row[0]
            grade = row[1]
            try:
                ratingList[country] = float(grade)
            except TypeError:
                ratingList[country] = 0.0                           # TODO: maybe not use half rating

        return ratingList


    def getGradingItems(self):
        '''
        # "CO2 emissions (metric tons per capita)";"EN.ATM.CO2E.PC"
        "Electricity production from renewable sources (kWh)";"EG.ELC.RNEW.KH"
        "GDP (current US$)";"NY.GDP.MKTP.CD"
        "Health expenditure, total (% of GDP)";"SH.XPD.TOTL.ZS"
        "Long-term unemployment (% of total unemployment)";"SL.UEM.LTRM.ZS"
        "Mortality rate, infant (per 1,000 live births)";"SP.DYN.IMRT.IN"
        "Public spending on education, total (% of GDP)";"SE.XPD.TOTL.GD.ZS"
        "Strength of legal rights index (0=weak to 12=strong)";"IC.LGL.CRED.XQ"
        "Tax revenue (% of GDP)";"GC.TAX.TOTL.GD.ZS"
        "Unemployment, total (% of total labor force) (national estimate)";"SL.UEM.TOTL.NE.ZS"

        "Electric power consumption (kWh per capita)";"EG.USE.ELEC.KH.PC"
        # "Motor vehicles (per 1,000 people)";"IS.VEH.NVEH.P3"
        "Life expectancy at birth, total (years)";"SP.DYN.LE00.IN"
        "Internet users (per 100 people)";"IT.NET.USER.P2"
        '''

        self.gradingItems = {}
        if len(self.ListCol) > 0:
            for item in self.ListCol:
                column = self.getNameOfCol(item)
                self.gradingItems[column.replace(".","_").lower()] = 1                           # TODO: get true value from user +/-
        else:
            self.gradingItems = {"EG.USE.ELEC.KH.PC".replace(".","_").lower(): 1, "SP.DYN.LE00.IN".replace(".","_").lower(): 1, "SH.XPD.TOTL.ZS".replace(".","_").lower(): 1,
                                "SL.UEM.LTRM.ZS".replace(".","_").lower(): -1, "SP.DYN.IMRT.IN".replace(".","_").lower(): -1, "SE.XPD.TOTL.GD.ZS".replace(".","_").lower(): 1, "IC.LGL.CRED.XQ".replace(".","_").lower(): 1,
                                "GC.TAX.TOTL.GD.ZS".replace(".","_").lower(): 1, "SL.UEM.TOTL.NE.ZS".replace(".","_").lower(): -1, "IT.NET.USER.P2".replace(".","_").lower(): 1}

        
