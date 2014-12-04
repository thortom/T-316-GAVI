import tkinter as tk
import newReadCSVRowHeader as csvReader
import statistics as st
import numpy as np
import pylab as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Button
import SlidePlot as plotter
import pandas as pd
import Tolfreadi as Tol
import Septspa as sp



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.uwotm8 = tk.Button(self)
        self.uwotm8["text"] = "Línurit fyrir gistinætur íslendinga"
        self.uwotm8["command"] = self.linurit1
        self.uwotm8.pack(side="top")

        self.random = tk.Button(self)
        self.random["text"] = "Línurit fyrir gistinætur útlendinga"
        self.random["command"] = self.linurit2
        self.random.pack(side="top")

        self.dnolol = tk.Button(self)
        self.dnolol["text"] = "Spá fyrir gistinætum hjá útlendingum yfir Airwaves árið 2014"
        self.dnolol["command"] = self.rit3
        self.dnolol.pack(side="top")

        self.immastabyou = tk.Button(self)
        self.immastabyou["text"] = "Spá fyrir gistinætum hjá íslendingum yfir Airwaves árið 2014"
        self.immastabyou["command"] = self.rit4
        self.immastabyou.pack(side="top")

        self.ubleednoob = tk.Button(self)
        self.ubleednoob["text"] = "Sliderplot fyrir útlendingar gistikomur 1998-2014"
        self.ubleednoob["command"] = self.slider1
        self.ubleednoob.pack(side="top")

        self.udead = tk.Button(self)
        self.udead["text"] = "Sliderplot fyrir útlendingar gestakomur 1998-2014"
        self.udead["command"] = self.slider2
        self.udead.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def linurit1(self):
        fileName1 = "SAM01103cm.csv"
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        sp.septoktspa(dfIslendingarGisti,'október','nóvember','september')

    def linurit2(self):
        fileName1 = "SAM01103cm.csv"
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        sp.septoktspa(dfUtlendingarGisti,'október','nóvember','september')

    def rit3(self):
        fileName1 = "SAM01103cm.csv"
        monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1} 
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        Least_Square_Ut_Gisti = Tol.Stats(dfUtlendingarGisti,monthPlayed)
        Least_Square_Ut_Gisti.plot('Úlendingar gistinætur')
        lineUt, wUt = Least_Square_Ut_Gisti.Least_Squares()
        print('Spá fyrir gistinætum hjá útlendingum yfir Airwaves árið 2014')
        print(wUt[0]*2014+wUt[1])

    def rit4(self):
        fileName1 = "SAM01103cm.csv"
        monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1} 
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        Least_Square_Is_Gisti = Tol.Stats(dfIslendingarGisti,monthPlayed)
        Least_Square_Is_Gisti.plot('Íslendingar gistinætur')
        line, w = Least_Square_Is_Gisti.Least_Squares()
        print('Spá fyrir gistinætum hjá íslendingum yfir Airwaves árið 2014')
        print(w[0]*2014+w[1])

    def slider1(self):
        fileName1 = "SAM01103cm.csv"
        monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        data = reader.getDataArray()
        alls = data[0]
        islendingar = data[1]
        utlendingar = data[2]
        allMonths = data[3]
        dfAllMonthsGesta, dfAllMonthsGisti = allMonths[0], allMonths[1] 
        dfAllsGesta, dfAllsGisti = alls[0], alls[1]
        dfIslendingarGesta, dfIslendingarGisti = islendingar[0], islendingar[1]
        dfUtlendingarGesta, dfUtlendingarGisti = utlendingar[0], utlendingar[1]
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        plotter.SlidePlot(dfUtlendingarGisti.T.values, "Útlendingar gistikomur")

    def slider2(self):
        fileName1 = "SAM01103cm.csv"
        monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        data = reader.getDataArray()
        alls = data[0]
        islendingar = data[1]
        utlendingar = data[2]
        allMonths = data[3]
        dfAllMonthsGesta, dfAllMonthsGisti = allMonths[0], allMonths[1] 
        dfAllsGesta, dfAllsGisti = alls[0], alls[1]
        dfIslendingarGesta, dfIslendingarGisti = islendingar[0], islendingar[1]
        dfUtlendingarGesta, dfUtlendingarGisti = utlendingar[0], utlendingar[1]
        dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
        plotter.SlidePlot(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")

root = tk.Tk()
app = Application(master=root)
app.mainloop()